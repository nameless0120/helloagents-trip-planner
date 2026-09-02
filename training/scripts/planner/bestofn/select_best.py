#!/usr/bin/env python3
"""Score Best-of-N candidates, select winners, and export trainable data."""

from __future__ import annotations

import argparse
import json
import random
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parents[4]
EVAL_SCRIPTS_DIR = PROJECT_ROOT / "training/scripts/eval"
BACKEND_DIR = PROJECT_ROOT / "backend"
sys.path.insert(0, str(BACKEND_DIR))
sys.path.insert(0, str(EVAL_SCRIPTS_DIR))

from eval_utils import read_jsonl, write_json, write_jsonl  # noqa: E402
from shared.paths import BESTOFN_DIR, LLAMAFACTORY_DIR  # noqa: E402


DEFAULT_PROMPTS = BESTOFN_DIR / "prompts.jsonl"
DEFAULT_CANDIDATES = BESTOFN_DIR / "candidates.jsonl"
DEFAULT_SELECTED = BESTOFN_DIR / "selected.jsonl"
DATASET_INFO = LLAMAFACTORY_DIR / "dataset_info.json"


HARD_KEYS = [
    "json_extract_ok",
    "schema_ok",
    "city_ok",
    "date_range_ok",
    "days_len_ok",
    "day_dates_ok",
    "weather_dates_ok",
    "day_index_ok",
    "accommodation_type_ok",
    "meal_complete",
    "meal_specific_ok",
    "meal_valid_semantics_ok",
    "meal_grounding_ok",
    "attraction_count_ok",
    "attraction_grounding_ok",
    "middle_hotel_ok",
    "invalid_hotel_name_ok",
    "hotel_grounding_ok",
    "hotel_distance_placeholder_ok",
    "location_object_ok",
    "transportation_budget_nonnegative",
    "weather_match",
]

SOFT_WEIGHTS = {
    "sft_hard_pass": 40.0,
    "dpo_soft_pass": 16.0,
    "dpo_soft_recomputed_budget_pass": 18.0,
    "recomputed_budget_fit_ok": 12.0,
    "budget_preference_aligned": 10.0,
    "budget_user_constraint_ok": 8.0,
    "budget_relationship_ok": 10.0,
    "hotel_budget_relation_ok": 5.0,
    "attraction_budget_party_relation_ok": 5.0,
    "meal_cost_scale_ok": 7.0,
    "meal_diversity_ok": 7.0,
    "attraction_diversity_ok": 5.0,
}

ERROR_PENALTIES = {
    "json_extract": 100.0,
    "schema": 80.0,
    "meal_grounding_miss": 25.0,
    "meal_invalid_name": 25.0,
    "meal_placeholder": 25.0,
    "budget_hard_constraint_exceeded": 16.0,
    "weather_mismatch": 14.0,
    "hotel_distance_placeholder": 14.0,
    "middle_hotel_null": 14.0,
    "accommodation_type_mismatch": 12.0,
    "budget_preference_mismatch": 8.0,
    "budget_relationship_mismatch": 7.0,
    "meal_cost_scale_too_low": 6.0,
    "meal_same_day_lunch_dinner_repeat": 6.0,
    "meal_repeat_too_many": 5.0,
    "attraction_repeat_too_many": 4.0,
    "too_many_attractions": 8.0,
}


def bool_metric(metrics: dict[str, Any], key: str) -> bool:
    return metrics.get(key) is True


def error_types(candidate: dict[str, Any]) -> list[str]:
    return [str(item.get("type") or item.get("stage") or "unknown") for item in candidate.get("rule_errors") or []]


def score_candidate(candidate: dict[str, Any]) -> dict[str, Any]:
    """Deterministic reward used for Best-of-N selection.

    The score is intentionally conservative: hard protocol failures are costly,
    and soft rewards only matter once the output is structurally useful.
    """
    metrics = candidate.get("rule_metrics") or {}
    components: dict[str, float] = {}

    if (candidate.get("generation_meta") or {}).get("ok") is False:
        return {
            "score": -200.0,
            "components": {"generation_failed": -200.0},
            "hard_pass": False,
            "schema_ok": False,
        }

    score = 0.0
    for key in HARD_KEYS:
        delta = 2.0 if bool_metric(metrics, key) else -10.0
        components[key] = delta
        score += delta

    for key, weight in SOFT_WEIGHTS.items():
        if bool_metric(metrics, key):
            components[key] = components.get(key, 0.0) + weight
            score += weight

    # Keep rates as small tie-breakers instead of primary objectives.
    for key in ["attraction_grounding_rate", "hotel_grounding_rate", "meal_grounding_rate", "meal_diversity_unique_rate"]:
        try:
            value = float(metrics.get(key) or 0.0)
        except Exception:  # noqa: BLE001
            value = 0.0
        delta = round(value * 3.0, 4)
        components[key] = delta
        score += delta

    for kind in error_types(candidate):
        penalty = ERROR_PENALTIES.get(kind, 2.0)
        components[f"penalty:{kind}"] = components.get(f"penalty:{kind}", 0.0) - penalty
        score -= penalty

    return {
        "score": round(score, 4),
        "components": components,
        "hard_pass": bool_metric(metrics, "sft_hard_pass"),
        "schema_ok": bool_metric(metrics, "schema_ok"),
    }


def make_training_prompt(system_prompt: str, prompt: str) -> str:
    return f"{system_prompt.strip()}\n\n{prompt.strip()}".strip()


def make_sft_row(prompt_row: dict[str, Any], output: str) -> dict[str, str]:
    return {
        "instruction": prompt_row.get("system_prompt", ""),
        "input": prompt_row.get("prompt", ""),
        "output": output,
    }


def make_pair_row(prompt_row: dict[str, Any], selected: dict[str, Any], rejected: dict[str, Any]) -> dict[str, Any]:
    return {
        "conversations": [
            {
                "from": "human",
                "value": make_training_prompt(prompt_row.get("system_prompt", ""), prompt_row.get("prompt", "")),
            }
        ],
        "chosen": {"from": "gpt", "value": selected.get("output_text", "")},
        "rejected": {"from": "gpt", "value": rejected.get("output_text", "")},
        "preference_reason": (
            f"best_of_n_score {selected.get('bestofn_score')} > {rejected.get('bestofn_score')}; "
            f"chosen={selected.get('candidate_id')} rejected={rejected.get('candidate_id')}"
        ),
    }


def split_rows(rows: list[Any], val_ratio: float, seed: int) -> tuple[list[Any], list[Any]]:
    rows = list(rows)
    rng = random.Random(seed)
    rng.shuffle(rows)
    val_size = max(1, round(len(rows) * val_ratio)) if len(rows) > 1 else 0
    return rows[val_size:], rows[:val_size]


def load_prompt_map(path: Path) -> dict[str, dict[str, Any]]:
    return {row["prompt_id"]: row for row in read_jsonl(path)}


def choose_rejected(scored: list[dict[str, Any]], chosen_id: str, require_schema: bool) -> dict[str, Any] | None:
    candidates = [item for item in scored if item.get("candidate_id") != chosen_id]
    if require_schema:
        candidates = [item for item in candidates if item.get("bestofn_score_meta", {}).get("schema_ok")]
    if not candidates:
        return None
    return sorted(candidates, key=lambda item: item.get("bestofn_score", 0.0))[0]


def update_dataset_info(
    *,
    sft_train: Path | None,
    sft_val: Path | None,
    pair_train: Path | None,
    pair_val: Path | None,
    sft_train_name: str,
    sft_val_name: str,
    pair_train_name: str,
    pair_val_name: str,
) -> None:
    data = json.loads(DATASET_INFO.read_text(encoding="utf-8")) if DATASET_INFO.exists() else {}
    if sft_train and sft_val:
        data[sft_train_name] = {"file_name": llamafactory_file_name(sft_train)}
        data[sft_val_name] = {"file_name": llamafactory_file_name(sft_val)}
    if pair_train and pair_val:
        entry = {
            "ranking": True,
            "formatting": "sharegpt",
            "columns": {
                "messages": "conversations",
                "chosen": "chosen",
                "rejected": "rejected",
            },
        }
        data[pair_train_name] = {"file_name": llamafactory_file_name(pair_train), **entry}
        data[pair_val_name] = {"file_name": llamafactory_file_name(pair_val), **entry}
    write_json(DATASET_INFO, data)


def llamafactory_file_name(path: Path) -> str:
    """Return the dataset_info file_name relative to the LLaMAFactory data root."""
    try:
        return path.relative_to(LLAMAFACTORY_DIR).as_posix()
    except ValueError:
        return path.name


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Select Best-of-N winners and export data.")
    parser.add_argument("--prompts", type=Path, default=DEFAULT_PROMPTS)
    parser.add_argument("--candidates", type=Path, default=DEFAULT_CANDIDATES)
    parser.add_argument("--selected-output", type=Path, default=DEFAULT_SELECTED)
    parser.add_argument("--summary-output", type=Path, default=None)
    parser.add_argument("--val-ratio", type=float, default=0.1)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--no-hard-gate", action="store_true", help="Allow a non-hardpass winner even if hardpass candidates exist.")
    parser.add_argument("--rejected-allow-nonschema", action="store_true")
    parser.add_argument("--lf-sft-train", type=Path, default=None)
    parser.add_argument("--lf-sft-val", type=Path, default=None)
    parser.add_argument("--lf-pair-train", type=Path, default=None)
    parser.add_argument("--lf-pair-val", type=Path, default=None)
    parser.add_argument("--update-dataset-info", action="store_true")
    parser.add_argument("--sft-train-name", default="trip_bestofn_sft_train")
    parser.add_argument("--sft-val-name", default="trip_bestofn_sft_val")
    parser.add_argument("--pair-train-name", default="trip_bestofn_pair_train")
    parser.add_argument("--pair-val-name", default="trip_bestofn_pair_val")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    prompt_map = load_prompt_map(args.prompts)
    selected_rows = []
    sft_rows = []
    pair_rows = []
    missing_prompts = 0
    no_pair = 0

    for row in read_jsonl(args.candidates):
        prompt_id = row.get("prompt_id")
        prompt_row = prompt_map.get(prompt_id)
        if not prompt_row:
            missing_prompts += 1
            continue

        scored = []
        for candidate in row.get("candidates") or []:
            score_meta = score_candidate(candidate)
            item = dict(candidate)
            item["bestofn_score"] = score_meta["score"]
            item["bestofn_score_meta"] = score_meta
            scored.append(item)
        if not scored:
            continue

        if args.no_hard_gate:
            eligible = scored
        else:
            hardpass = [item for item in scored if item.get("bestofn_score_meta", {}).get("hard_pass")]
            eligible = hardpass or scored
        selected = sorted(eligible, key=lambda item: item.get("bestofn_score", -9999.0), reverse=True)[0]
        rejected = choose_rejected(scored, selected["candidate_id"], require_schema=not args.rejected_allow_nonschema)
        if not rejected:
            no_pair += 1

        selected_rows.append(
            {
                "timestamp": datetime.now(timezone.utc).isoformat(),
                "prompt_id": prompt_id,
                "record_id": row.get("record_id"),
                "metadata": row.get("metadata") or {},
                "selected_candidate_id": selected["candidate_id"],
                "selected_score": selected["bestofn_score"],
                "selected_hard_pass": selected.get("bestofn_score_meta", {}).get("hard_pass"),
                "selected_schema_ok": selected.get("bestofn_score_meta", {}).get("schema_ok"),
                "rejected_candidate_id": rejected.get("candidate_id") if rejected else None,
                "rejected_score": rejected.get("bestofn_score") if rejected else None,
                "candidate_scores": [
                    {
                        "candidate_id": item["candidate_id"],
                        "score": item["bestofn_score"],
                        "hard_pass": item.get("bestofn_score_meta", {}).get("hard_pass"),
                        "schema_ok": item.get("bestofn_score_meta", {}).get("schema_ok"),
                        "temperature": item.get("temperature"),
                    }
                    for item in sorted(scored, key=lambda item: item.get("bestofn_score", -9999.0), reverse=True)
                ],
                "selected_output": selected.get("output_text", ""),
                "selected_metrics": selected.get("rule_metrics", {}),
                "selected_errors": selected.get("rule_errors", []),
            }
        )
        sft_rows.append(make_sft_row(prompt_row, selected.get("output_text", "")))
        if rejected:
            pair_rows.append(make_pair_row(prompt_row, selected, rejected))

    write_jsonl(args.selected_output, selected_rows)

    sft_train, sft_val = split_rows(sft_rows, args.val_ratio, args.seed)
    pair_train, pair_val = split_rows(pair_rows, args.val_ratio, args.seed)
    if args.lf_sft_train and args.lf_sft_val:
        write_json(args.lf_sft_train, sft_train)
        write_json(args.lf_sft_val, sft_val)
    if args.lf_pair_train and args.lf_pair_val:
        write_json(args.lf_pair_train, pair_train)
        write_json(args.lf_pair_val, pair_val)
    if args.update_dataset_info:
        update_dataset_info(
            sft_train=args.lf_sft_train,
            sft_val=args.lf_sft_val,
            pair_train=args.lf_pair_train,
            pair_val=args.lf_pair_val,
            sft_train_name=args.sft_train_name,
            sft_val_name=args.sft_val_name,
            pair_train_name=args.pair_train_name,
            pair_val_name=args.pair_val_name,
        )

    hard_selected = sum(1 for row in selected_rows if row.get("selected_hard_pass"))
    schema_selected = sum(1 for row in selected_rows if row.get("selected_schema_ok"))
    summary = {
        "candidates": str(args.candidates),
        "selected_output": str(args.selected_output),
        "selected": len(selected_rows),
        "selected_schema_ok": schema_selected,
        "selected_hard_pass": hard_selected,
        "selected_hard_pass_rate": round(hard_selected / len(selected_rows), 4) if selected_rows else 0.0,
        "pairs": len(pair_rows),
        "sft_train": len(sft_train),
        "sft_val": len(sft_val),
        "pair_train": len(pair_train),
        "pair_val": len(pair_val),
        "missing_prompts": missing_prompts,
        "no_pair": no_pair,
    }
    summary_path = args.summary_output or (args.selected_output.parent / "bestofn_summary.json")
    write_json(summary_path, summary)
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
