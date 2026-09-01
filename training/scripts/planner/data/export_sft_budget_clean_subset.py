"""Export a classified SFT subset.

This script reads a records.jsonl file plus record_classification.jsonl, then
materializes one classification category and matching LLaMAFactory files.
All source and output paths must be provided explicitly so the script can be
used for any run without depending on archived audit outputs.
"""

from __future__ import annotations

import argparse
import json
import random
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parents[4]
LLAMAFACTORY_DIR = PROJECT_ROOT / "training/data/llamafactory"
LLAMAFACTORY_GENERATED_DIR = LLAMAFACTORY_DIR / "generated"
DATASET_INFO = LLAMAFACTORY_DIR / "dataset_info.json"
DEFAULT_CATEGORY = "usable_budget_clean"
SPLIT_SEED = 20260427


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Export a classified SFT subset")
    parser.add_argument("--records", type=Path, required=True)
    parser.add_argument("--classification", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--category", default=DEFAULT_CATEGORY)
    parser.add_argument("--dataset-prefix", required=True)
    parser.add_argument("--val-ratio", type=float, default=0.1)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    classifications = read_jsonl(args.classification)
    records = read_jsonl(args.records)

    keep_ids: list[str] = []
    seen_keep_ids: set[str] = set()
    for row in classifications:
        if row.get("category") != args.category:
            continue
        record_id = str(row["record_id"])
        if record_id in seen_keep_ids:
            continue
        keep_ids.append(record_id)
        seen_keep_ids.add(record_id)

    keep_set = set(keep_ids)
    by_id = {str(row.get("record_id")): row for row in records}
    missing = sorted(record_id for record_id in keep_set if record_id not in by_id)
    if missing:
        raise RuntimeError(f"Missing {len(missing)} records from source records.jsonl: {missing[:10]}")

    subset = [row for row in records if str(row.get("record_id")) in keep_set]
    if len(subset) != len(keep_set):
        raise RuntimeError(f"Expected {len(keep_set)} unique records, got {len(subset)}")

    args.output_dir.mkdir(parents=True, exist_ok=True)
    write_jsonl(args.output_dir / "records.jsonl", subset)
    (args.output_dir / "record_ids.txt").write_text(
        "".join(f"{record_id}\n" for record_id in keep_ids),
        encoding="utf-8",
    )

    lf_rows = [make_lf_row(row) for row in subset]
    train_rows, val_rows = split_train_val(lf_rows, args.val_ratio)
    train_path = LLAMAFACTORY_GENERATED_DIR / f"{args.dataset_prefix}_train.json"
    val_path = LLAMAFACTORY_GENERATED_DIR / f"{args.dataset_prefix}_val.json"
    write_json(train_path, train_rows)
    write_json(val_path, val_rows)
    update_dataset_info(args.dataset_prefix, llamafactory_file_name(train_path), llamafactory_file_name(val_path))

    summary = {
        "created_at": datetime.now(timezone.utc).isoformat(),
        "input_records": str(args.records),
        "source_classification": str(args.classification),
        "category": args.category,
        "records": len(subset),
        "llamafactory_train": len(train_rows),
        "llamafactory_val": len(val_rows),
        "output_dir": str(args.output_dir),
        "llamafactory_train_path": str(train_path),
        "llamafactory_val_path": str(val_path),
    }
    write_json(args.output_dir / "summary.json", summary)
    (args.output_dir / "数据集说明.md").write_text(render_readme(summary), encoding="utf-8")

    print(f"records={args.output_dir / 'records.jsonl'}")
    print(f"ids={args.output_dir / 'record_ids.txt'}")
    print(f"summary={args.output_dir / 'summary.json'}")
    print(f"llamafactory_train={train_path}")
    print(f"llamafactory_val={val_path}")
    print(f"records_count={len(subset)} train={len(train_rows)} val={len(val_rows)}")


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    with path.open("r", encoding="utf-8") as handle:
        return [json.loads(line) for line in handle if line.strip()]


def write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    with path.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False) + "\n")


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


def make_lf_row(record: dict[str, Any]) -> dict[str, str]:
    return {
        "instruction": str(record.get("system_prompt") or ""),
        "input": str(record["planner_query"]),
        "output": str(record["output"]),
    }


def split_train_val(rows: list[dict[str, str]], val_ratio: float) -> tuple[list[dict[str, str]], list[dict[str, str]]]:
    rows = list(rows)
    rng = random.Random(SPLIT_SEED)
    rng.shuffle(rows)
    val_size = max(1, int(len(rows) * val_ratio)) if len(rows) > 1 else 0
    return rows[val_size:], rows[:val_size]


def update_dataset_info(dataset_prefix: str, train_name: str, val_name: str) -> None:
    if DATASET_INFO.exists():
        data = json.loads(DATASET_INFO.read_text(encoding="utf-8"))
    else:
        data = {}
    data[f"{dataset_prefix}_train"] = {"file_name": train_name}
    data[f"{dataset_prefix}_val"] = {"file_name": val_name}
    write_json(DATASET_INFO, data)


def llamafactory_file_name(path: Path) -> str:
    """Return the dataset_info file_name relative to the LLaMAFactory data root."""
    try:
        return path.relative_to(LLAMAFACTORY_DIR).as_posix()
    except ValueError:
        return path.name


def render_readme(summary: dict[str, Any]) -> str:
    return "\n".join(
        [
            "# SFT audited subset",
            "",
            f"这份子集保留按当前审计分类判定为 `{summary['category']}` 的样本。",
            "",
            "## 内容",
            "",
            f"- 样本数：{summary['records']}",
            f"- 输入 records：`{summary['input_records']}`",
            f"- 来源分类：`{summary['source_classification']}`",
            "- 判定口径：来自 `record_classification.jsonl` 的 category 字段。",
            "",
            "## 文件",
            "",
            "- `records.jsonl`：保留的完整原始 records。",
            "- `record_ids.txt`：保留样本 ID。",
            "- `summary.json`：导出摘要。",
            f"- LLaMAFactory train：`{summary['llamafactory_train_path']}` ({summary['llamafactory_train']} 条)",
            f"- LLaMAFactory val：`{summary['llamafactory_val_path']}` ({summary['llamafactory_val']} 条)",
            "",
            "## 用法建议",
            "",
            "- 后续重做全量 SFT 时，不要覆盖本目录；把它作为已审计子集合并或单独训练。",
            "- 未进入本分类的样本应按审计分类修复、重生成或淘汰后再进入预算训练。",
            "",
        ]
    )


if __name__ == "__main__":
    main()
