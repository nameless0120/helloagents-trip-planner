#!/usr/bin/env python3
"""Build Best-of-N prompt rows from PlannerContext records."""

from __future__ import annotations

import argparse
import json
import random
import sys
from pathlib import Path
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parents[4]
BACKEND_DIR = PROJECT_ROOT / "backend"
EVAL_SCRIPTS_DIR = PROJECT_ROOT / "training/scripts/eval"
sys.path.insert(0, str(BACKEND_DIR))
sys.path.insert(0, str(EVAL_SCRIPTS_DIR))

from app.agents.prompts import PLANNER_AGENT_PROMPT  # noqa: E402
from eval_utils import read_jsonl, weather_bucket, write_json, write_jsonl  # noqa: E402
from shared.paths import EVAL_DATA_DIR, BESTOFN_DIR  # noqa: E402


DEFAULT_RECORDS = EVAL_DATA_DIR / "records.jsonl"
DEFAULT_OUTPUT = BESTOFN_DIR / "prompts.jsonl"


SMOKE_BUDGET_TARGETS = {
    "limited": 4,
    "standard": 6,
    "comfortable": 7,
    "premium": 3,
}
SMOKE_DAYS_TARGETS = {
    "2": 3,
    "3": 7,
    "4": 6,
    "5": 4,
}
SMOKE_COMPANION_MIN_ONE = {
    "solo",
    "couple",
    "friends",
    "family_with_children",
    "family_with_elders",
    "business",
}
SMOKE_CITY_TIER_MIN_ONE = {"popular", "major", "long_tail"}
SMOKE_DIET_MIN_ONE = {"海鲜过敏", "清真", "素食", "少辣", "清淡饮食"}


def metadata_from_record(record: dict[str, Any]) -> dict[str, Any]:
    """Extract stable slice metadata for audits and later train/val splits."""
    request = record.get("request") or {}
    control = record.get("control_spec") or {}
    return {
        "city": request.get("city", "unknown"),
        "travel_days": request.get("travel_days", "unknown"),
        "weather_bucket": weather_bucket(record),
        "budget_level": control.get("budget_level", "unknown"),
        "companion_type": control.get("companion_type", "unknown"),
        "city_tier": control.get("city_tier", "unknown"),
        "diet": control.get("diet", "unknown"),
        "pace": control.get("pace", "unknown"),
    }


def prompt_row_from_record(record: dict[str, Any], source: str, system_prompt: str) -> dict[str, Any]:
    """Convert one record into a reusable generation prompt row."""
    record_id = record.get("record_id")
    if not record_id:
        raise ValueError("record is missing record_id")
    prompt = record.get("planner_query") or record.get("prompt") or ""
    if not prompt:
        raise ValueError(f"{record_id} is missing planner_query/prompt")
    return {
        "prompt_id": record_id,
        "record_id": record_id,
        "source": source,
        "request": record.get("request") or {},
        "control_spec": record.get("control_spec") or {},
        "planner_context": record.get("planner_context") or {},
        "compact_planner_context": record.get("compact_planner_context") or {},
        "system_prompt": system_prompt,
        "prompt": prompt,
        "metadata": metadata_from_record(record),
    }


def summarize(rows: list[dict[str, Any]], records_path: Path, output_path: Path) -> dict[str, Any]:
    """Small distribution summary for smoke checks."""
    distribution: dict[str, dict[str, int]] = {
        "budget_level": {},
        "companion_type": {},
        "travel_days": {},
        "weather_bucket": {},
        "city_tier": {},
    }
    for row in rows:
        metadata = row.get("metadata") or {}
        for key in distribution:
            value = str(metadata.get(key, "unknown"))
            distribution[key][value] = distribution[key].get(value, 0) + 1
    return {
        "records": str(records_path),
        "output": str(output_path),
        "count": len(rows),
        "distribution": distribution,
    }


def count_selected(rows: list[dict[str, Any]], key: str) -> dict[str, int]:
    counts: dict[str, int] = {}
    for row in rows:
        value = str(metadata_from_record(row).get(key, "unknown"))
        counts[value] = counts.get(value, 0) + 1
    return counts


def stratified_smoke_select(records: list[dict[str, Any]], *, limit: int, seed: int, include_luxury: bool) -> list[dict[str, Any]]:
    """Greedy stratified selection for a tiny Best-of-N smoke.

    The source pool remains the existing controlled prompt source. The
    greedy score just prevents a 20-row smoke from accidentally missing budget,
    companion, city-tier, day-count, and diet-risk slices.
    """
    pool = [record for record in records if include_luxury or (record.get("control_spec") or {}).get("budget_level") != "luxury"]
    rng = random.Random(seed)
    pool = list(pool)
    rng.shuffle(pool)

    selected: list[dict[str, Any]] = []
    while pool and len(selected) < limit:
        budget_counts = count_selected(selected, "budget_level")
        days_counts = count_selected(selected, "travel_days")
        companion_counts = count_selected(selected, "companion_type")
        city_tier_counts = count_selected(selected, "city_tier")
        diet_counts = count_selected(selected, "diet")

        best_index = 0
        best_score = -1.0
        for index, record in enumerate(pool):
            metadata = metadata_from_record(record)
            budget = str(metadata.get("budget_level", "unknown"))
            days = str(metadata.get("travel_days", "unknown"))
            companion = str(metadata.get("companion_type", "unknown"))
            city_tier = str(metadata.get("city_tier", "unknown"))
            diet = str(metadata.get("diet", "unknown"))

            score = rng.random() * 0.01
            if budget_counts.get(budget, 0) < SMOKE_BUDGET_TARGETS.get(budget, 0):
                score += 20 + (SMOKE_BUDGET_TARGETS[budget] - budget_counts.get(budget, 0))
            if days_counts.get(days, 0) < SMOKE_DAYS_TARGETS.get(days, 0):
                score += 8 + (SMOKE_DAYS_TARGETS[days] - days_counts.get(days, 0))
            if companion in SMOKE_COMPANION_MIN_ONE and companion_counts.get(companion, 0) == 0:
                score += 14
            if city_tier in SMOKE_CITY_TIER_MIN_ONE and city_tier_counts.get(city_tier, 0) == 0:
                score += 10
            if diet in SMOKE_DIET_MIN_ONE and diet_counts.get(diet, 0) == 0:
                score += 12

            # Prefer rows with explicit avoid / negative constraints in a smoke.
            negative_constraints = (record.get("control_spec") or {}).get("negative_constraints") or []
            if negative_constraints:
                score += min(3, len(negative_constraints))

            if score > best_score:
                best_score = score
                best_index = index
        selected.append(pool.pop(best_index))

    return selected


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build Best-of-N prompt rows.")
    parser.add_argument("--records", type=Path, default=DEFAULT_RECORDS)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--summary-output", type=Path, default=None)
    parser.add_argument("--source", default=None)
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--shuffle", action="store_true")
    parser.add_argument(
        "--stratified-smoke20",
        action="store_true",
        help="Select a stratified 20-row smoke set from the prompt source.",
    )
    parser.add_argument(
        "--include-luxury",
        action="store_true",
        help="Include luxury rows when using --stratified-smoke20.",
    )
    parser.add_argument(
        "--system-prompt-file",
        type=Path,
        default=None,
        help="Optional prompt override. Defaults to backend app.agents.prompts.PLANNER_AGENT_PROMPT.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    records = read_jsonl(args.records)
    if args.stratified_smoke20:
        records = stratified_smoke_select(records, limit=args.limit or 20, seed=args.seed, include_luxury=args.include_luxury)
    elif args.shuffle:
        rng = random.Random(args.seed)
        rng.shuffle(records)
    if args.limit > 0 and not args.stratified_smoke20:
        records = records[: args.limit]

    if args.system_prompt_file:
        system_prompt = args.system_prompt_file.read_text(encoding="utf-8")
    else:
        system_prompt = PLANNER_AGENT_PROMPT

    source = args.source or args.records.stem
    rows = [prompt_row_from_record(record, source, system_prompt) for record in records]
    if args.resume and args.output.exists():
        existing_rows = read_jsonl(args.output)
        done_ids = {row.get("prompt_id") for row in existing_rows if row.get("prompt_id")}
        new_rows = [row for row in rows if row.get("prompt_id") not in done_ids]
        rows = existing_rows + new_rows
        print(f"resume: existing={len(existing_rows)}, add={len(new_rows)}")
    write_jsonl(args.output, rows)

    summary_path = args.summary_output or (args.output.parent / "prompts_summary.json")
    summary = summarize(rows, args.records, args.output)
    write_json(summary_path, summary)
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
