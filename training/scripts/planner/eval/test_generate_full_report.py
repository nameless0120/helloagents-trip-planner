"""Smoke tests for generate_full_report.py.

Run from the project root:
python3 training/scripts/planner/eval/test_generate_full_report.py
"""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from tempfile import TemporaryDirectory


SCRIPT = Path(__file__).with_name("generate_full_report.py")


def write_records(path: Path, count: int) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as file:
        for index in range(count):
            file.write(json.dumps({"record_id": f"r{index}"}, ensure_ascii=False) + "\n")


def metric(passed: int, total: int) -> dict[str, float | int]:
    return {"pass": passed, "total": total, "rate": passed / total if total else 0.0}


def write_report(
    path: Path,
    records_path: Path,
    total: int,
    hard_pass: int,
    soft_pass: int,
    recomputed_fit: int,
    budget_relationship: int,
    numeric_avg: float,
) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    boolean_metrics = {
        "hard_pass": metric(hard_pass, total),
        "dpo_soft_pass": metric(soft_pass, total),
        "dpo_soft_recomputed_budget_pass": metric(recomputed_fit, total),
        "recomputed_budget_fit_ok": metric(recomputed_fit, total),
        "budget_relationship_ok": metric(budget_relationship, total),
    }
    data = {
        "records_path": str(records_path),
        "raw_generations": total,
        "unique_generations": total,
        "summary": {
            "total": total,
            "boolean_metrics": boolean_metrics,
            "numeric_metrics": {
                "recomputed_budget_total": {"avg": numeric_avg, "p50": numeric_avg, "p90": numeric_avg},
                "recomputed_budget_per_person_day": {"avg": numeric_avg / 10, "p50": numeric_avg / 10, "p90": numeric_avg / 10},
            },
        },
    }
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


def run_report(tmp: Path, *extra_args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(SCRIPT), *extra_args],
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )


def test_weighted_report_and_explicit_comparison_labels(tmp: Path) -> None:
    standard_records = tmp / "standard_records.jsonl"
    hard_records = tmp / "hard_records.jsonl"
    write_records(standard_records, 2)
    write_records(hard_records, 3)

    reports = tmp / "reports"
    for label, values in {
        "candidate": ((1, 2, 1, 1, 10.0), (3, 3, 3, 3, 20.0)),
        "baseline": ((0, 0, 0, 0, 30.0), (1, 1, 1, 1, 40.0)),
        "reference_b": ((1, 1, 1, 1, 50.0), (1, 1, 1, 1, 60.0)),
    }.items():
        for split, records_path, total, values_for_split in [
            ("standard", standard_records, 2, values[0]),
            ("hard", hard_records, 3, values[1]),
        ]:
            hard_pass, soft_pass, recomputed_fit, budget_relationship, numeric_avg = values_for_split
            write_report(
                reports / label / split / "rule_eval_report.json",
                records_path,
                total,
                hard_pass,
                soft_pass,
                recomputed_fit,
                budget_relationship,
                numeric_avg,
            )

    output_dir = tmp / "out"
    result = run_report(
        tmp,
        "--current-label",
        "candidate",
        "--primary-label",
        "reference_b",
        "--baseline-label",
        "baseline",
        "--standard-records",
        str(standard_records),
        "--hard-records",
        str(hard_records),
        "--report",
        f"standard/candidate={reports / 'candidate/standard/rule_eval_report.json'}",
        "--report",
        f"hard/candidate={reports / 'candidate/hard/rule_eval_report.json'}",
        "--report",
        f"standard/baseline={reports / 'baseline/standard/rule_eval_report.json'}",
        "--report",
        f"hard/baseline={reports / 'baseline/hard/rule_eval_report.json'}",
        "--report",
        f"standard/reference_b={reports / 'reference_b/standard/rule_eval_report.json'}",
        "--report",
        f"hard/reference_b={reports / 'reference_b/hard/rule_eval_report.json'}",
        "--output-dir",
        str(output_dir),
        "--comparison-slug",
        "smoke",
    )
    assert result.returncode == 0, result.stderr
    report = (output_dir / "smoke_full_report.md").read_text(encoding="utf-8")
    assert "硬通过 80.0%，高于 reference_b +40.0pp，高于 baseline +60.0pp" in report
    assert "| 硬通过 | 80.0% (4/5) | 40.0% (2/5) | 20.0% (1/5) |" in report
    assert "| 重算总预算 avg | 16.0 | 56.0 | 36.0 |" in report


def test_records_path_mismatch_fails(tmp: Path) -> None:
    standard_records = tmp / "standard_records.jsonl"
    hard_records = tmp / "hard_records.jsonl"
    write_records(standard_records, 1)
    write_records(hard_records, 1)
    wrong_records = tmp / "wrong_records.jsonl"
    write_records(wrong_records, 1)

    report = tmp / "rule_eval_report.json"
    write_report(report, wrong_records, 1, 1, 1, 1, 1, 10.0)
    result = run_report(
        tmp,
        "--current-label",
        "candidate",
        "--standard-records",
        str(standard_records),
        "--hard-records",
        str(hard_records),
        "--report",
        f"standard/candidate={report}",
        "--report",
        f"hard/candidate={report}",
        "--output-dir",
        str(tmp / "out"),
    )
    assert result.returncode != 0
    assert "records_path mismatch" in result.stderr


def main() -> None:
    with TemporaryDirectory() as tmp_dir:
        tmp = Path(tmp_dir)
        test_weighted_report_and_explicit_comparison_labels(tmp / "weighted")
        test_records_path_mismatch_fails(tmp / "mismatch")
    print("generate_full_report smoke tests passed")


if __name__ == "__main__":
    main()
