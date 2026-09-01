"""生成 DPO 数据审计报告。"""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path
from typing import Any

from dpo_utils import (
    DEFAULT_DPO_AUDIT,
    DEFAULT_DPO_CANDIDATES,
    DEFAULT_DPO_JUDGEMENTS,
    DEFAULT_DPO_PAIRS,
    DEFAULT_DPO_PROMPTS,
    hard_filter_pass,
    read_jsonl,
    safe_counter,
    score_summary,
)


def candidate_stats(candidate_rows: list[dict[str, Any]]) -> dict[str, Any]:
    """统计候选生成和硬过滤情况。"""
    total = 0
    hard_pass = 0
    source_counter: Counter = Counter()
    fail_reasons: Counter = Counter()
    for row in candidate_rows:
        for candidate in row.get("candidates") or []:
            total += 1
            source_counter[candidate.get("source_type", "unknown")] += 1
            passed, reasons = hard_filter_pass(candidate)
            if passed:
                hard_pass += 1
            for reason in reasons:
                fail_reasons[reason] += 1
    return {
        "total": total,
        "hard_pass": hard_pass,
        "hard_pass_rate": round(hard_pass / total, 4) if total else 0,
        "source_type": dict(source_counter),
        "fail_reasons": dict(fail_reasons.most_common()),
    }


def judgement_stats(rows: list[dict[str, Any]]) -> dict[str, Any]:
    """统计 judge 分数。"""
    ok_rows = [row for row in rows if row.get("ok")]
    score_keys = ["grounding", "budget_alignment", "preference_alignment", "weather_awareness", "feasibility", "specificity", "overall"]
    scores = {}
    for key in score_keys:
        values = [float(row.get("scores", {}).get(key, 0)) for row in ok_rows]
        if values:
            values_sorted = sorted(values)
            scores[key] = {
                "avg": round(sum(values) / len(values), 4),
                "p50": values_sorted[len(values_sorted) // 2],
                "min": values_sorted[0],
                "max": values_sorted[-1],
            }
    return {
        "total": len(rows),
        "ok": len(ok_rows),
        "scores": scores,
    }


def pairs_stats(pairs: list[dict[str, Any]]) -> dict[str, Any]:
    """统计 pair 分布。"""
    return {
        "total": len(pairs),
        "score_gap": score_summary(pairs, "score_gap"),
        "chosen_source": dict(safe_counter(pairs, ["metadata", "chosen_source"])),
        "rejected_source": dict(safe_counter(pairs, ["metadata", "rejected_source"])),
        "budget_level": dict(safe_counter(pairs, ["metadata", "budget_level"])),
        "companion_type": dict(safe_counter(pairs, ["metadata", "companion_type"])),
        "weather_bucket": dict(safe_counter(pairs, ["metadata", "weather_bucket"])),
        "tags": dict(safe_counter([{"tag": tag} for pair in pairs for tag in pair.get("tags", [])], ["tag"])),
    }


def write_report(path: Path, data: dict[str, Any], pairs: list[dict[str, Any]], sample_size: int) -> None:
    """写 Markdown 审计报告。"""
    lines = ["# DPO Data Audit Report\n\n", "```json\n", json.dumps(data, ensure_ascii=False, indent=2), "\n```\n"]
    lines.append("\n## Sample Pairs\n\n")
    for pair in pairs[:sample_size]:
        lines.append(f"### {pair.get('pair_id')}\n")
        lines.append(f"- record_id: `{pair.get('record_id')}`\n")
        lines.append(f"- chosen: `{pair.get('chosen_candidate_id')}` score={pair.get('chosen_score')}\n")
        lines.append(f"- rejected: `{pair.get('rejected_candidate_id')}` score={pair.get('rejected_score')}\n")
        lines.append(f"- gap: {pair.get('score_gap')}\n")
        lines.append(f"- tags: {pair.get('tags')}\n")
        lines.append(f"- chosen_reason: {pair.get('preference_reason')}\n")
        lines.append(f"- rejected_reason: {pair.get('rejected_reason')}\n\n")
        chosen = str(pair.get("chosen", ""))
        rejected = str(pair.get("rejected", ""))
        lines.append("**chosen snippet**\n\n")
        lines.append("```json\n" + chosen[:1200] + ("\n..." if len(chosen) > 1200 else "") + "\n```\n\n")
        lines.append("**rejected snippet**\n\n")
        lines.append("```json\n" + rejected[:1200] + ("\n..." if len(rejected) > 1200 else "") + "\n```\n\n")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="生成 DPO 数据审计报告。")
    parser.add_argument("--prompts", type=Path, default=DEFAULT_DPO_PROMPTS)
    parser.add_argument("--candidates", type=Path, default=DEFAULT_DPO_CANDIDATES)
    parser.add_argument("--judgements", type=Path, default=DEFAULT_DPO_JUDGEMENTS)
    parser.add_argument("--pairs", type=Path, default=DEFAULT_DPO_PAIRS)
    parser.add_argument("--output", type=Path, default=DEFAULT_DPO_AUDIT)
    parser.add_argument("--sample-size", type=int, default=20)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    prompts = read_jsonl(args.prompts)
    candidates = read_jsonl(args.candidates)
    judgements = read_jsonl(args.judgements)
    pairs = read_jsonl(args.pairs)
    data = {
        "prompts": len(prompts),
        "candidates": candidate_stats(candidates),
        "judgements": judgement_stats(judgements),
        "pairs": pairs_stats(pairs),
    }
    write_report(args.output, data, pairs, args.sample_size)
    print(f"audit report: {args.output}")
    print(json.dumps(data, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
