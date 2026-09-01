"""构造 DPO prompt 池。

示例:

  .venv-training-py311/bin/python3 training/scripts/eval/dpo_build_prompts.py \
    --records training/data/planner/sft_runs/<run>/records.jsonl \
    --limit 20 \
    --shuffle
"""

from __future__ import annotations

import argparse
import random
from pathlib import Path

from dpo_utils import DEFAULT_DPO_PROMPTS, prompt_row_from_record
from eval_utils import read_jsonl, write_jsonl
from app.agents.prompts import PLANNER_AGENT_PROMPT

def load_existing_ids(path: Path) -> set[str]:
    """读取已存在 prompt_id。"""
    return {row.get("prompt_id", "") for row in read_jsonl(path)}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="构造 DPO prompt 池。")
    parser.add_argument("--records", type=Path, required=True, help="当前 SFT records.jsonl。")
    parser.add_argument("--output", type=Path, default=DEFAULT_DPO_PROMPTS)
    parser.add_argument("--source", default=None, help="写入 prompt.source，默认使用 records 文件名")
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--shuffle", action="store_true")
    parser.add_argument("--resume", action="store_true", help="追加缺失样本，不覆盖已有 prompts.jsonl")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    records = read_jsonl(args.records)
    if args.shuffle:
        rng = random.Random(args.seed)
        records = list(records)
        rng.shuffle(records)
    if args.limit > 0:
        records = records[: args.limit]
    source = args.source or args.records.stem
    rows = [
        prompt_row_from_record(record, source=source, system_prompt=PLANNER_AGENT_PROMPT)
        for record in records
    ]

    if args.resume and args.output.exists():
        done_ids = load_existing_ids(args.output)
        existing_rows = read_jsonl(args.output)
        new_rows = [row for row in rows if row["prompt_id"] not in done_ids]
        rows = existing_rows + new_rows
        print(f"resume: existing={len(existing_rows)}, add={len(new_rows)}")

    write_jsonl(args.output, rows)
    print(f"DPO prompts: {args.output}")
    print(f"records={len(records)}, written={len(rows)}")


if __name__ == "__main__":
    main()
