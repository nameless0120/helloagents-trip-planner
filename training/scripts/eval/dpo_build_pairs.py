"""从 candidates + judgements 构造 DPO chosen/rejected pair。

示例:

  .venv-training-py311/bin/python3 training/scripts/eval/dpo_build_pairs.py \
    --max-pairs-per-prompt 1
"""

from __future__ import annotations

import argparse
import json
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from dpo_utils import (
    DEFAULT_DPO_CANDIDATES,
    DEFAULT_DPO_JUDGEMENTS,
    DEFAULT_DPO_PAIRS,
    DEFAULT_DPO_PAIRS_TRAIN,
    DEFAULT_DPO_PAIRS_VAL,
    DEFAULT_DPO_PROMPTS,
    LLAMAFACTORY_DIR,
    hard_filter_pass,
    read_jsonl,
    safe_counter,
    severe_flags,
    split_pairs,
    tag_from_score_gap,
    write_json,
    write_lf_files,
)
from eval_utils import write_jsonl


def flatten_candidates(rows: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    """candidate_id -> candidate，补 prompt_id/record_id/metadata。"""
    result = {}
    for row in rows:
        for candidate in row.get("candidates") or []:
            item = dict(candidate)
            item["prompt_id"] = row.get("prompt_id")
            item["record_id"] = row.get("record_id")
            item["metadata"] = row.get("metadata") or {}
            result[item["candidate_id"]] = item
    return result


def valid_judgement(row: dict[str, Any]) -> bool:
    """judge 结果是否可用于 pair 构造。"""
    return bool(row.get("ok")) and isinstance(row.get("scores"), dict) and "overall" in row.get("scores", {})


def build_pairs_for_prompt(
    prompt_row: dict[str, Any],
    prompt_judgements: list[dict[str, Any]],
    candidates_by_id: dict[str, dict[str, Any]],
    args: argparse.Namespace,
) -> list[dict[str, Any]]:
    """为单个 prompt 构造 pair。"""
    usable = []
    for judgement in prompt_judgements:
        candidate = candidates_by_id.get(judgement["candidate_id"])
        if not candidate:
            continue
        passed, _ = hard_filter_pass(
            candidate,
            min_attraction_grounding=args.min_attraction_grounding,
            min_hotel_grounding=args.min_hotel_grounding,
        )
        if not passed:
            continue
        usable.append({"candidate": candidate, "judgement": judgement})

    chosen_pool = [
        item
        for item in usable
        if item["judgement"].get("scores", {}).get("overall", 0) >= args.min_chosen_score
        and not severe_flags(item["judgement"].get("hard_flags"))
    ]
    if not chosen_pool:
        return []

    chosen_pool.sort(key=lambda item: item["judgement"]["scores"]["overall"], reverse=True)
    pairs = []
    used_rejected = set()
    for chosen_item in chosen_pool:
        chosen_score = float(chosen_item["judgement"]["scores"]["overall"])
        rejected_pool = [
            item
            for item in usable
            if item["candidate"]["candidate_id"] != chosen_item["candidate"]["candidate_id"]
            and item["candidate"]["candidate_id"] not in used_rejected
            and chosen_score - float(item["judgement"]["scores"].get("overall", 0)) >= args.min_score_gap
        ]
        if not rejected_pool:
            continue
        rejected_pool.sort(key=lambda item: item["judgement"]["scores"]["overall"])
        rejected_item = rejected_pool[0]
        used_rejected.add(rejected_item["candidate"]["candidate_id"])

        chosen = chosen_item["candidate"]
        rejected = rejected_item["candidate"]
        chosen_judge = chosen_item["judgement"]
        rejected_judge = rejected_item["judgement"]
        rejected_score = float(rejected_judge["scores"]["overall"])
        metadata = prompt_row.get("metadata") or {}
        tags = tag_from_score_gap(chosen_judge["scores"], rejected_judge["scores"], threshold=args.tag_gap)
        for key in ["budget_level", "companion_type", "weather_bucket", "diet"]:
            if metadata.get(key):
                tags.append(str(metadata[key]))

        pair = {
            "pair_id": "",
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "prompt_id": prompt_row["prompt_id"],
            "record_id": prompt_row["record_id"],
            "system_prompt": prompt_row.get("system_prompt", ""),
            "prompt": prompt_row.get("prompt", ""),
            "chosen": chosen.get("output_text", ""),
            "rejected": rejected.get("output_text", ""),
            "chosen_candidate_id": chosen["candidate_id"],
            "rejected_candidate_id": rejected["candidate_id"],
            "chosen_score": round(chosen_score, 4),
            "rejected_score": round(rejected_score, 4),
            "score_gap": round(chosen_score - rejected_score, 4),
            "preference_reason": chosen_judge.get("reason", ""),
            "rejected_reason": rejected_judge.get("reason", ""),
            "tags": sorted(set(tags)),
            "metadata": {
                **metadata,
                "chosen_source": chosen.get("source_type"),
                "rejected_source": rejected.get("source_type"),
                "chosen_model": chosen.get("source_model"),
                "rejected_model": rejected.get("source_model"),
            },
            "chosen_scores": chosen_judge.get("scores", {}),
            "rejected_scores": rejected_judge.get("scores", {}),
            "chosen_flags": chosen_judge.get("hard_flags", {}),
            "rejected_flags": rejected_judge.get("hard_flags", {}),
        }
        pairs.append(pair)
        if len(pairs) >= args.max_pairs_per_prompt:
            break
    return pairs


def summarize_pairs(pairs: list[dict[str, Any]]) -> dict[str, Any]:
    """汇总 pair 分布。"""
    return {
        "total": len(pairs),
        "chosen_source": dict(safe_counter(pairs, ["metadata", "chosen_source"])),
        "rejected_source": dict(safe_counter(pairs, ["metadata", "rejected_source"])),
        "budget_level": dict(safe_counter(pairs, ["metadata", "budget_level"])),
        "companion_type": dict(safe_counter(pairs, ["metadata", "companion_type"])),
        "weather_bucket": dict(safe_counter(pairs, ["metadata", "weather_bucket"])),
        "tags": dict(safe_counter([{"tag": tag} for pair in pairs for tag in pair.get("tags", [])], ["tag"])),
    }


def write_summary(path: Path, pairs: list[dict[str, Any]], train_pairs: list[dict[str, Any]], val_pairs: list[dict[str, Any]]) -> None:
    """写构造摘要。"""
    summary = {
        "total": len(pairs),
        "train": len(train_pairs),
        "val": len(val_pairs),
        **summarize_pairs(pairs),
    }
    lines = ["# DPO Pair Build Summary\n\n", "```json\n", json.dumps(summary, ensure_ascii=False, indent=2), "\n```\n"]
    lines.append("\n## Sample Pairs\n\n")
    for pair in pairs[:20]:
        lines.append(f"### {pair['pair_id']}\n")
        lines.append(f"- record_id: `{pair['record_id']}`\n")
        lines.append(f"- chosen: `{pair['chosen_candidate_id']}` score={pair['chosen_score']}\n")
        lines.append(f"- rejected: `{pair['rejected_candidate_id']}` score={pair['rejected_score']}\n")
        lines.append(f"- gap: {pair['score_gap']}\n")
        lines.append(f"- tags: {pair.get('tags')}\n")
        lines.append(f"- reason: {pair.get('preference_reason')}\n\n")
    path.write_text("".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="构造 DPO chosen/rejected pair。")
    parser.add_argument("--prompts", type=Path, default=DEFAULT_DPO_PROMPTS)
    parser.add_argument("--candidates", type=Path, default=DEFAULT_DPO_CANDIDATES)
    parser.add_argument("--judgements", type=Path, default=DEFAULT_DPO_JUDGEMENTS)
    parser.add_argument("--output", type=Path, default=DEFAULT_DPO_PAIRS)
    parser.add_argument("--train-output", type=Path, default=DEFAULT_DPO_PAIRS_TRAIN)
    parser.add_argument("--val-output", type=Path, default=DEFAULT_DPO_PAIRS_VAL)
    parser.add_argument("--lf-output-dir", type=Path, default=LLAMAFACTORY_DIR / "generated")
    parser.add_argument("--lf-copy-dir", type=Path, default=None, help="可选：在本轮输出目录保存一份 LLaMA-Factory 副本。")
    parser.add_argument("--lf-train-file", default="trip_dpo_train.json")
    parser.add_argument("--lf-val-file", default="trip_dpo_val.json")
    parser.add_argument("--dataset-train-name", default="trip_dpo_train")
    parser.add_argument("--dataset-val-name", default="trip_dpo_val")
    parser.add_argument("--val-ratio", type=float, default=0.1)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--min-chosen-score", type=float, default=4.0)
    parser.add_argument("--min-score-gap", type=float, default=0.8)
    parser.add_argument("--tag-gap", type=float, default=0.8)
    parser.add_argument("--max-pairs-per-prompt", type=int, default=1)
    parser.add_argument("--min-attraction-grounding", type=float, default=0.7)
    parser.add_argument("--min-hotel-grounding", type=float, default=0.8)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    prompts = {row["prompt_id"]: row for row in read_jsonl(args.prompts)}
    candidates_by_id = flatten_candidates(read_jsonl(args.candidates))
    judgements_by_prompt: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in read_jsonl(args.judgements):
        if valid_judgement(row):
            judgements_by_prompt[row["prompt_id"]].append(row)

    pairs = []
    for prompt_id, prompt_row in prompts.items():
        rows = build_pairs_for_prompt(prompt_row, judgements_by_prompt.get(prompt_id, []), candidates_by_id, args)
        pairs.extend(rows)

    for index, pair in enumerate(pairs, start=1):
        pair["pair_id"] = f"dpo_{index:06d}"

    train_pairs, val_pairs = split_pairs(pairs, args.val_ratio, args.seed)
    write_jsonl(args.output, pairs)
    write_jsonl(args.train_output, train_pairs)
    write_jsonl(args.val_output, val_pairs)

    lf_train = args.lf_output_dir / args.lf_train_file
    lf_val = args.lf_output_dir / args.lf_val_file
    write_lf_files(
        lf_train,
        lf_val,
        train_pairs,
        val_pairs,
        train_dataset_name=args.dataset_train_name,
        val_dataset_name=args.dataset_val_name,
    )
    if args.lf_copy_dir:
        write_json(args.lf_copy_dir / args.lf_train_file, json.loads(lf_train.read_text(encoding="utf-8")))
        write_json(args.lf_copy_dir / args.lf_val_file, json.loads(lf_val.read_text(encoding="utf-8")))

    summary_path = args.output.parent / "pair_build_summary.md"
    write_summary(summary_path, pairs, train_pairs, val_pairs)
    print(f"pairs={len(pairs)}, train={len(train_pairs)}, val={len(val_pairs)}")
    print(f"pairs: {args.output}")
    print(f"llamafactory: {lf_train}, {lf_val}")
    print(f"summary: {summary_path}")


if __name__ == "__main__":
    main()
