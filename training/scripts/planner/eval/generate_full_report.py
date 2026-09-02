"""Generate a human-readable full report from rule eval reports."""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parents[4]
SCRIPTS_DIR = PROJECT_ROOT / "training/scripts"
sys.path.insert(0, str(SCRIPTS_DIR))

from shared.paths import EVAL_DATA_DIR, EVAL_HARD_DATA_DIR  # noqa: E402

DEFAULT_STANDARD_RECORDS = EVAL_DATA_DIR / "records.jsonl"
DEFAULT_HARD_RECORDS = EVAL_HARD_DATA_DIR / "records.jsonl"

HARDPASS_METRICS = [
    ("硬通过", "hard_pass"),
    ("JSON抽取", "json_extract_ok"),
    ("Schema合法", "schema_ok"),
    ("城市正确", "city_ok"),
    ("日期范围", "date_range_ok"),
    ("天数", "days_len_ok"),
    ("每日日期", "day_dates_ok"),
    ("天气日期完整", "weather_dates_ok"),
    ("day_index正确", "day_index_ok"),
    ("住宿类型", "accommodation_type_ok"),
    ("餐饮完整", "meal_complete"),
    ("餐饮具体化", "meal_specific_ok"),
    ("餐饮语义合法", "meal_valid_semantics_ok"),
    ("餐饮grounding", "meal_grounding_ok"),
    ("景点数量", "attraction_count_ok"),
    ("景点grounding", "attraction_grounding_ok"),
    ("中间住宿", "middle_hotel_ok"),
    ("无非法酒店名", "invalid_hotel_name_ok"),
    ("酒店grounding", "hotel_grounding_ok"),
    ("酒店距离占位", "hotel_distance_placeholder_ok"),
    ("坐标对象", "location_object_ok"),
    ("交通预算非负", "transportation_budget_nonnegative"),
    ("天气匹配", "weather_match"),
]

SOFTPASS_METRICS = [
    ("软通过", "dpo_soft_pass"),
    ("重算预算软通过", "dpo_soft_recomputed_budget_pass"),
    ("硬通过前置", "hard_pass"),
    ("景点多样性", "attraction_diversity_ok"),
    ("餐饮多样性", "meal_diversity_ok"),
    ("预算偏好贴合", "budget_preference_aligned"),
    ("重算预算贴合", "recomputed_budget_fit_ok"),
]

BUDGET_METRICS = [
    ("预算合计一致", "budget_consistent"),
    ("预算算术一致", "budget_arithmetic_consistent"),
    ("预算关系一致", "budget_relationship_ok"),
    ("预算选品贴合", "budget_selection_ok"),
    ("预算档位贴合", "budget_level_aligned"),
    ("预算偏好贴合（软通过项）", "budget_preference_aligned"),
    ("用户预算约束", "budget_user_constraint_ok"),
    ("声明预算未超", "budget_within_user_budget"),
    ("重算预算硬约束", "recomputed_budget_hard_ok"),
    ("重算预算贴合（重算软通过项）", "recomputed_budget_fit_ok"),
    ("重算预算档位贴合", "recomputed_budget_level_aligned"),
    ("重算预算偏好贴合", "recomputed_budget_preference_aligned"),
    ("重算用户预算约束", "recomputed_budget_user_constraint_ok"),
    ("重算预算未超", "recomputed_budget_within_user_budget"),
    ("酒店预算关系", "hotel_budget_relation_ok"),
    ("酒店覆盖晚数", "hotel_budget_covers_nights"),
    ("景点预算/人数关系", "attraction_budget_party_relation_ok"),
    ("景点预算一致", "attraction_budget_consistent"),
    ("餐饮尺度", "meal_cost_scale_ok"),
    ("餐饮预算一致", "meal_budget_consistent"),
    ("交通预算非负（硬通过项）", "transportation_budget_nonnegative"),
]

COMBINED_NUMERIC_METRICS = [
    ("重算总预算 avg", "recomputed_budget_total", "avg"),
    ("重算人日预算 avg", "recomputed_budget_per_person_day", "avg"),
]

SPLIT_NUMERIC_METRICS = [
    ("重算总预算 avg", "recomputed_budget_total", "avg"),
    ("重算总预算 p50", "recomputed_budget_total", "p50"),
    ("重算总预算 p90", "recomputed_budget_total", "p90"),
    ("重算人日预算 avg", "recomputed_budget_per_person_day", "avg"),
    ("重算人日预算 p50", "recomputed_budget_per_person_day", "p50"),
    ("重算人日预算 p90", "recomputed_budget_per_person_day", "p90"),
]

CHANGE_METRICS = [
    ("预算关系一致", "budget_relationship_ok"),
    ("景点预算/人数关系", "attraction_budget_party_relation_ok"),
    ("餐饮多样性", "meal_diversity_ok"),
    ("预算偏好贴合", "budget_preference_aligned"),
    ("酒店覆盖晚数", "hotel_budget_covers_nights"),
    ("软通过", "dpo_soft_pass"),
    ("酒店预算关系", "hotel_budget_relation_ok"),
    ("餐饮尺度", "meal_cost_scale_ok"),
    ("重算预算软通过", "dpo_soft_recomputed_budget_pass"),
    ("重算预算贴合", "recomputed_budget_fit_ok"),
    ("硬通过", "hard_pass"),
    ("景点多样性", "attraction_diversity_ok"),
    ("餐饮grounding", "meal_grounding_ok"),
    ("景点grounding", "attraction_grounding_ok"),
    ("天气匹配", "weather_match"),
    ("预算合计一致", "budget_consistent"),
    ("预算未超", "budget_within_user_budget"),
]


@dataclass(frozen=True)
class RuleReport:
    label: str
    split: str
    path: Path
    data: dict[str, Any]

    @property
    def summary(self) -> dict[str, Any]:
        return self.data.get("summary") or {}

    @property
    def total(self) -> int:
        return int(self.summary.get("total") or 0)


def parse_report_arg(value: str) -> tuple[str, str, Path]:
    """Parse split/label=rule_eval_report.json."""
    if "=" not in value or "/" not in value.split("=", 1)[0]:
        raise argparse.ArgumentTypeError("report must be split/label=rule_eval_report.json")
    left, path_text = value.split("=", 1)
    split, label = left.split("/", 1)
    if split not in {"standard", "hard"}:
        raise argparse.ArgumentTypeError("split must be standard or hard")
    if not label:
        raise argparse.ArgumentTypeError("label must not be empty")
    return split, label, Path(path_text)


def parse_key_value(value: str) -> tuple[str, str]:
    if "=" not in value:
        raise argparse.ArgumentTypeError("value must be label=text")
    key, text = value.split("=", 1)
    if not key:
        raise argparse.ArgumentTypeError("label must not be empty")
    return key, text


def read_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        raise FileNotFoundError(f"missing report: {path}")
    return json.loads(path.read_text(encoding="utf-8"))


def count_jsonl(path: Path) -> int | None:
    if not path.exists():
        return None
    with path.open("r", encoding="utf-8") as file:
        return sum(1 for line in file if line.strip())


def display_path(path: Path) -> str:
    try:
        return str(path.resolve().relative_to(PROJECT_ROOT))
    except ValueError:
        return str(path)


def normalize_path_for_compare(path: str | Path | None) -> str | None:
    if not path:
        return None
    value = Path(str(path))
    resolved = value.resolve() if value.is_absolute() else (PROJECT_ROOT / value).resolve()
    try:
        return str(resolved.relative_to(PROJECT_ROOT))
    except ValueError:
        return str(resolved)


def validate_report_records_path(report: RuleReport, expected_path: Path, allow_mismatch: bool) -> None:
    actual = normalize_path_for_compare(report.data.get("records_path"))
    expected = normalize_path_for_compare(expected_path)
    if actual == expected:
        return
    message = (
        f"records_path mismatch for {report.split}/{report.label}: "
        f"report has {report.data.get('records_path')!r}, expected {display_path(expected_path)!r}"
    )
    if allow_mismatch:
        print(f"warning: {message}")
        return
    raise ValueError(message)


def strip_date_prefix(name: str) -> str:
    return re.sub(r"^\d{6}_", "", name)


def default_title(current_label: str, labels: list[str]) -> str:
    others = [label for label in labels if label != current_label]
    return f"{current_label} vs {' / '.join(others)} 全量评估报告" if others else f"{current_label} 全量评估报告"


def bool_counts(report: RuleReport, metric: str) -> tuple[int, int] | None:
    item = (report.summary.get("boolean_metrics") or {}).get(metric)
    if not item:
        return None
    return int(item.get("pass") or 0), int(item.get("total") or 0)


def split_bool_counts(model_reports: dict[str, RuleReport], metric: str, split: str) -> tuple[int, int] | None:
    report = model_reports.get(split)
    if not report:
        return None
    return bool_counts(report, metric)


def combined_bool_counts(model_reports: dict[str, RuleReport], metric: str) -> tuple[int, int] | None:
    passed = 0
    total = 0
    found = False
    for split in ("standard", "hard"):
        counts = split_bool_counts(model_reports, metric, split)
        if not counts:
            continue
        found = True
        passed += counts[0]
        total += counts[1]
    return (passed, total) if found else None


def rate_from_counts(counts: tuple[int, int] | None) -> float | None:
    if not counts or counts[1] <= 0:
        return None
    return counts[0] / counts[1]


def format_bool(counts: tuple[int, int] | None) -> str:
    rate = rate_from_counts(counts)
    if rate is None:
        return "-"
    passed, total = counts or (0, 0)
    return f"{rate * 100:.1f}% ({passed}/{total})"


def format_pct(rate: float | None) -> str:
    return "-" if rate is None else f"{rate * 100:.1f}%"


def format_pp(delta: float | None) -> str:
    if delta is None:
        return "-"
    return f"{delta * 100:+.1f}pp"


def format_abs_pp(delta: float) -> str:
    return f"{abs(delta) * 100:.1f}pp"


def format_number(value: float | None) -> str:
    return "-" if value is None else f"{value:.1f}"


def numeric_value(report: RuleReport, metric: str, field: str) -> float | None:
    item = (report.summary.get("numeric_metrics") or {}).get(metric)
    if not item or item.get(field) is None:
        return None
    return float(item[field])


def combined_numeric_avg(model_reports: dict[str, RuleReport], metric: str) -> float | None:
    weighted_sum = 0.0
    weight_sum = 0
    for split in ("standard", "hard"):
        report = model_reports.get(split)
        if not report:
            continue
        value = numeric_value(report, metric, "avg")
        if value is None:
            continue
        weight = report.total or 0
        weighted_sum += value * weight
        weight_sum += weight
    return weighted_sum / weight_sum if weight_sum else None


def model_total(model_reports: dict[str, RuleReport]) -> int:
    return sum((model_reports.get(split).total if model_reports.get(split) else 0) for split in ("standard", "hard"))


def split_target_count(records_path: Path, fallback_report: RuleReport | None) -> int:
    records_count = count_jsonl(records_path)
    if records_count is not None:
        return records_count
    return fallback_report.total if fallback_report else 0


def generation_cell(report: RuleReport | None, target: int) -> str:
    if not report:
        return "-"
    raw = report.data.get("raw_generations")
    unique = report.data.get("unique_generations")
    raw_text = f"{raw}/{target}" if raw is not None and target else str(raw if raw is not None else "-")
    unique_text = str(unique if unique is not None else "-")
    return f"raw={raw_text}, unique={unique_text}"


def append_bool_table(
    lines: list[str],
    title: str,
    rows: list[tuple[str, str]],
    labels: list[str],
    reports_by_label: dict[str, dict[str, RuleReport]],
    split: str | None = None,
) -> None:
    lines.append(f"### {title}\n\n")
    lines.append("| 指标 | " + " | ".join(labels) + " |\n")
    lines.append("|---|" + "|".join("---:" for _ in labels) + "|\n")
    for display_name, metric in rows:
        cells = []
        for label in labels:
            model_reports = reports_by_label[label]
            counts = (
                split_bool_counts(model_reports, metric, split)
                if split
                else combined_bool_counts(model_reports, metric)
            )
            cells.append(format_bool(counts))
        lines.append(f"| {display_name} | " + " | ".join(cells) + " |\n")
    lines.append("\n")


def append_numeric_table(
    lines: list[str],
    title: str,
    rows: list[tuple[str, str, str]],
    labels: list[str],
    reports_by_label: dict[str, dict[str, RuleReport]],
    split: str | None = None,
) -> None:
    lines.append(f"### {title}\n\n")
    lines.append("| 指标 | " + " | ".join(labels) + " |\n")
    lines.append("|---|" + "|".join("---:" for _ in labels) + "|\n")
    for display_name, metric, field in rows:
        cells = []
        for label in labels:
            model_reports = reports_by_label[label]
            if split:
                report = model_reports.get(split)
                value = numeric_value(report, metric, field) if report else None
            else:
                value = combined_numeric_avg(model_reports, metric)
            cells.append(format_number(value))
        lines.append(f"| {display_name} | " + " | ".join(cells) + " |\n")
    lines.append("\n")


def scoped_rate(
    reports_by_label: dict[str, dict[str, RuleReport]],
    label: str,
    metric: str,
    split: str | None = None,
) -> float | None:
    model_reports = reports_by_label[label]
    counts = (
        split_bool_counts(model_reports, metric, split)
        if split
        else combined_bool_counts(model_reports, metric)
    )
    return rate_from_counts(counts)


def append_change_summary(
    lines: list[str],
    title: str,
    current_label: str,
    labels: list[str],
    reports_by_label: dict[str, dict[str, RuleReport]],
    split: str | None,
    limit: int,
) -> None:
    lines.append(f"### {title}\n\n")
    for other_label in labels:
        if other_label == current_label:
            continue
        rows = []
        for display_name, metric in CHANGE_METRICS:
            current_rate = scoped_rate(reports_by_label, current_label, metric, split)
            other_rate = scoped_rate(reports_by_label, other_label, metric, split)
            if current_rate is None or other_rate is None:
                continue
            rows.append((abs(current_rate - other_rate), display_name, current_rate, other_rate))
        rows.sort(key=lambda row: (-row[0], row[1]))

        lines.append(f"相对 {other_label}：\n\n")
        lines.append("| 指标 | 当前 | 对比版本 | 变化 |\n")
        lines.append("|---|---:|---:|---:|\n")
        for _, display_name, current_rate, other_rate in rows[:limit]:
            lines.append(
                f"| {display_name} | {format_pct(current_rate)} | {format_pct(other_rate)} | "
                f"{format_pp(current_rate - other_rate)} |\n"
            )
        lines.append("\n")


def is_baseline_label(label: str) -> bool:
    lowered = label.lower()
    return lowered == "base" or "baseline" in lowered


def comparison_labels(
    labels: list[str],
    current_label: str,
    primary_label: str | None = None,
    baseline_label: str | None = None,
) -> tuple[str | None, str | None]:
    others = [label for label in labels if label != current_label]
    if not others:
        return None, None
    baseline = baseline_label or next((label for label in others if is_baseline_label(label)), None)
    primary = primary_label or next((label for label in others if label != baseline), None) or others[0]
    return primary, baseline or others[-1]


def ordered_labels(
    labels: list[str],
    current_label: str,
    primary_label: str | None = None,
    baseline_label: str | None = None,
) -> list[str]:
    others = [label for label in labels if label != current_label]
    baseline = baseline_label or next((label for label in others if is_baseline_label(label)), None)
    primary = primary_label or next((label for label in others if label != baseline), None)

    ordered = [current_label]
    for label in [primary, *others, baseline]:
        if label and label not in ordered:
            ordered.append(label)
    return ordered


def compare_phrase(
    reports_by_label: dict[str, dict[str, RuleReport]],
    current_label: str,
    other_label: str | None,
    metric: str,
    split: str | None = None,
) -> str:
    if not other_label:
        return ""
    current_rate = scoped_rate(reports_by_label, current_label, metric, split)
    other_rate = scoped_rate(reports_by_label, other_label, metric, split)
    if current_rate is None or other_rate is None:
        return ""
    delta = current_rate - other_rate
    if abs(delta) < 0.0005:
        return f"与 {other_label} 持平"
    if delta > 0:
        return f"高于 {other_label} {format_pp(delta)}"
    return f"低于 {other_label} {format_abs_pp(delta)}"


def split_regression(
    reports_by_label: dict[str, dict[str, RuleReport]],
    labels: list[str],
    current_label: str,
    metric: str,
) -> tuple[str, str, float] | None:
    worst: tuple[str, str, float] | None = None
    for other_label in labels:
        if other_label == current_label:
            continue
        for split in ("standard", "hard"):
            current_rate = scoped_rate(reports_by_label, current_label, metric, split)
            other_rate = scoped_rate(reports_by_label, other_label, metric, split)
            if current_rate is None or other_rate is None:
                continue
            delta = current_rate - other_rate
            if delta >= -0.0005:
                continue
            if worst is None or delta < worst[2]:
                worst = (split, other_label, delta)
    return worst


def auto_recommendation(
    reports_by_label: dict[str, dict[str, RuleReport]],
    labels: list[str],
    current_label: str,
) -> str:
    others = [label for label in labels if label != current_label]
    hard_current = scoped_rate(reports_by_label, current_label, "hard_pass")
    soft_current = scoped_rate(reports_by_label, current_label, "dpo_soft_pass")
    budget_current = scoped_rate(reports_by_label, current_label, "recomputed_budget_fit_ok")
    hard_best = all(
        hard_current is not None
        and (scoped_rate(reports_by_label, label, "hard_pass") is None or hard_current >= scoped_rate(reports_by_label, label, "hard_pass"))
        for label in others
    )
    soft_best = all(
        soft_current is not None
        and (
            scoped_rate(reports_by_label, label, "dpo_soft_pass") is None
            or soft_current >= scoped_rate(reports_by_label, label, "dpo_soft_pass")
        )
        for label in others
    )
    budget_best = all(
        budget_current is not None
        and (
            scoped_rate(reports_by_label, label, "recomputed_budget_fit_ok") is None
            or budget_current >= scoped_rate(reports_by_label, label, "recomputed_budget_fit_ok")
        )
        for label in others
    )
    if hard_best and soft_best and budget_best:
        regression = split_regression(reports_by_label, labels, current_label, "recomputed_budget_fit_ok")
        if regression:
            split, other_label, delta = regression
            split_name = "标准集" if split == "standard" else "困难集"
            return (
                "当前候选在硬约束、软通过和合并重算预算贴合上整体领先；"
                f"但{split_name}的重算预算贴合仍低于 {other_label} {format_abs_pp(delta)}，"
                "下一步应继续补复杂预算目标贴合和选品样本。"
            )
        return "当前候选在硬约束、软通过和重算预算贴合上整体领先；下一步更适合继续补复杂预算样本，确认优势能否稳定外推。"
    if hard_best and soft_best:
        return "当前候选在硬约束和软通过上领先，但预算贴合仍需看分 split 细项；下一步优先补预算目标贴合和选品样本。"
    if hard_best:
        return "当前候选硬约束表现领先，但软通过或预算贴合不是全局最优；下一步应围绕软指标退化点做定向数据或 pairwise 复核。"
    return "当前候选没有在核心指标上全面领先；下一步应先定位退化切片，再决定继续训练、回退 checkpoint 还是补数据。"


def append_summary(
    lines: list[str],
    reports_by_label: dict[str, dict[str, RuleReport]],
    labels: list[str],
    current_label: str,
    summary_notes: list[str],
    primary_label: str | None,
    baseline_label: str | None,
) -> None:
    primary, baseline = comparison_labels(labels, current_label, primary_label, baseline_label)
    combined_n = model_total(reports_by_label[current_label])
    hard_rate = scoped_rate(reports_by_label, current_label, "hard_pass")
    standard_hard = scoped_rate(reports_by_label, current_label, "hard_pass", "standard")
    hard_hard = scoped_rate(reports_by_label, current_label, "hard_pass", "hard")
    soft_rate = scoped_rate(reports_by_label, current_label, "dpo_soft_pass")
    recomputed_soft_rate = scoped_rate(reports_by_label, current_label, "dpo_soft_recomputed_budget_pass")
    budget_relationship = scoped_rate(reports_by_label, current_label, "budget_relationship_ok")
    recomputed_fit = scoped_rate(reports_by_label, current_label, "recomputed_budget_fit_ok")

    lines.append("## 总结\n\n")
    hard_comparisons = "，".join(
        part
        for part in [
            compare_phrase(reports_by_label, current_label, primary, "hard_pass"),
            compare_phrase(reports_by_label, current_label, baseline, "hard_pass") if baseline != primary else "",
        ]
        if part
    )
    lines.append(
        f"当前 {current_label} 在 {combined_n} 条合并口径下，硬通过 {format_pct(hard_rate)}"
        f"{'，' + hard_comparisons if hard_comparisons else ''}。"
        f"standard 硬通过为 {format_pct(standard_hard)}，hard 硬通过为 {format_pct(hard_hard)}。\n\n"
    )

    soft_comparisons = "，".join(
        part
        for part in [
            compare_phrase(reports_by_label, current_label, primary, "dpo_soft_pass"),
            compare_phrase(reports_by_label, current_label, baseline, "dpo_soft_pass") if baseline != primary else "",
        ]
        if part
    )
    lines.append(
        f"软通过为 {format_pct(soft_rate)}，重算预算软通过为 {format_pct(recomputed_soft_rate)}"
        f"{'；软通过' + soft_comparisons if soft_comparisons else ''}。"
        "这两个指标更能反映硬约束之外的多样性和预算偏好收益。\n\n"
    )

    budget_comparisons = "，".join(
        part
        for part in [
            compare_phrase(reports_by_label, current_label, primary, "budget_relationship_ok"),
            compare_phrase(reports_by_label, current_label, baseline, "budget_relationship_ok") if baseline != primary else "",
        ]
        if part
    )
    lines.append(
        f"预算诊断上，预算关系一致为 {format_pct(budget_relationship)}"
        f"{'，' + budget_comparisons if budget_comparisons else ''}；"
        f"重算预算贴合为 {format_pct(recomputed_fit)}。分 split 的预算数值分布和变化摘要见下方表格。\n\n"
    )

    for note in summary_notes:
        lines.append(note.strip() + "\n\n")

    lines.append(f"综合判断：{auto_recommendation(reports_by_label, labels, current_label)}\n\n")


def append_scope(
    lines: list[str],
    heading: str,
    records_path: Path,
    labels: list[str],
    reports_by_label: dict[str, dict[str, RuleReport]],
    current_label: str,
    split: str | None,
    change_limit: int,
) -> None:
    if split:
        current_report = reports_by_label[current_label].get(split)
        count = split_target_count(records_path, current_report)
        lines.append(f"## {heading}\n\n")
        lines.append(f"- 数据：`{display_path(records_path)}`，{count} 条\n\n")
    else:
        count = model_total(reports_by_label[current_label])
        lines.append(f"## {count}条合并视图\n\n")

    append_bool_table(lines, "Hardpass 部分", HARDPASS_METRICS, labels, reports_by_label, split)
    append_bool_table(lines, "Softpass 部分", SOFTPASS_METRICS, labels, reports_by_label, split)
    append_bool_table(lines, "预算部分", BUDGET_METRICS, labels, reports_by_label, split)
    append_numeric_table(
        lines,
        "预算数值分布",
        SPLIT_NUMERIC_METRICS if split else COMBINED_NUMERIC_METRICS,
        labels,
        reports_by_label,
        split,
    )
    change_title = f"{heading} 变化摘要" if split else f"{count}条合并 变化摘要"
    append_change_summary(lines, change_title, current_label, labels, reports_by_label, split, change_limit)


def write_machine_summary(
    path: Path,
    reports_by_label: dict[str, dict[str, RuleReport]],
    labels: list[str],
    current_label: str,
) -> None:
    data = {
        "current_label": current_label,
        "labels": labels,
        "metrics": {},
        "sources": {
            label: {split: display_path(report.path) for split, report in reports.items()}
            for label, reports in reports_by_label.items()
        },
    }
    for label in labels:
        data["metrics"][label] = {
            "combined": {
                display_name: {
                    "pass": counts[0],
                    "total": counts[1],
                    "rate": rate_from_counts(counts),
                }
                for display_name, metric in SOFTPASS_METRICS + BUDGET_METRICS + HARDPASS_METRICS
                if (counts := combined_bool_counts(reports_by_label[label], metric)) is not None
            }
        }
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate a full eval report from rule_eval_report.json files.")
    parser.add_argument("--report", action="append", required=True, type=parse_report_arg, help="格式: split/label=rule_eval_report.json")
    parser.add_argument("--current-label", required=True, help="当前候选 label，必须与 --report 中的 label 一致")
    parser.add_argument("--primary-label", default=None, help="主要对照 label；默认选择第一个非 baseline 对照")
    parser.add_argument("--baseline-label", default=None, help="baseline 对照 label；默认按 base/baseline 名称推断")
    parser.add_argument("--title", default=None)
    parser.add_argument("--updated-date", default=date.today().isoformat())
    parser.add_argument("--standard-records", type=Path, default=DEFAULT_STANDARD_RECORDS)
    parser.add_argument("--hard-records", type=Path, default=DEFAULT_HARD_RECORDS)
    parser.add_argument("--allow-records-mismatch", action="store_true", help="允许 report.records_path 与 split records 不一致，仅用于历史归档核对")
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--output-md", type=Path, default=None)
    parser.add_argument("--output-json", type=Path, default=None)
    parser.add_argument("--comparison-slug", default=None)
    parser.add_argument("--model-note", action="append", default=[], type=parse_key_value, help="格式: label=说明")
    parser.add_argument("--inference-note", default="未提供；本报告只基于已有 rule_eval_report.json 聚合。")
    parser.add_argument(
        "--rule-note",
        default="沿用各 rule_eval_report.json 对应的 eval_rule_metrics.py 产物；具体规则变更以生成该报告时的代码版本为准。",
    )
    parser.add_argument("--summary-note", action="append", default=[], help="追加到总结中的人工说明，可重复")
    parser.add_argument("--change-limit", type=int, default=12)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    reports_by_label: dict[str, dict[str, RuleReport]] = {}
    labels: list[str] = []
    for split, label, path in args.report:
        if label not in reports_by_label:
            reports_by_label[label] = {}
            labels.append(label)
        if split in reports_by_label[label]:
            raise ValueError(f"duplicate report for {split}/{label}")
        reports_by_label[label][split] = RuleReport(label=label, split=split, path=path, data=read_json(path))

    if args.current_label not in reports_by_label:
        raise ValueError(f"--current-label {args.current_label!r} not found in --report")
    for option_name, label in [("--primary-label", args.primary_label), ("--baseline-label", args.baseline_label)]:
        if label and label not in reports_by_label:
            raise ValueError(f"{option_name} {label!r} not found in --report")
        if label and label == args.current_label:
            raise ValueError(f"{option_name} must not equal --current-label")
    if args.primary_label and args.primary_label == args.baseline_label:
        raise ValueError("--primary-label and --baseline-label must be different")
    for label, split_reports in reports_by_label.items():
        missing = {"standard", "hard"} - set(split_reports)
        if missing:
            raise ValueError(f"{label} missing split reports: {', '.join(sorted(missing))}")
        validate_report_records_path(split_reports["standard"], args.standard_records, args.allow_records_mismatch)
        validate_report_records_path(split_reports["hard"], args.hard_records, args.allow_records_mismatch)

    labels = ordered_labels(labels, args.current_label, args.primary_label, args.baseline_label)
    title = args.title or default_title(args.current_label, labels)
    slug = args.comparison_slug or strip_date_prefix(args.output_dir.name)
    output_md = args.output_md or args.output_dir / f"{slug}_full_report.md"
    model_notes = dict(args.model_note)

    lines: list[str] = [f"# {title}\n\n"]
    lines.append(f"- 更新时间：{args.updated_date}\n")
    current_reports = reports_by_label[args.current_label]
    lines.append(
        f"- 当前版本：`{args.current_label}`，评估名 "
        f"`{current_reports['standard'].path.parent.name}` / `{current_reports['hard'].path.parent.name}`\n"
    )
    for label in labels:
        if label == args.current_label:
            continue
        reports = reports_by_label[label]
        note = model_notes.get(
            label,
            f"`{reports['standard'].path.parent.parent.name}/{reports['standard'].path.parent.name}` / "
            f"`{reports['hard'].path.parent.parent.name}/{reports['hard'].path.parent.name}`",
        )
        lines.append(f"- 对照 {label}：{note}\n")

    standard_count = split_target_count(args.standard_records, current_reports["standard"])
    hard_count = split_target_count(args.hard_records, current_reports["hard"])
    lines.append(
        f"- 标准集：`{display_path(args.standard_records)}`，{standard_count} 条；"
        f"困难集：`{display_path(args.hard_records)}`，{hard_count} 条\n"
    )
    lines.append(f"- 推理设置：{args.inference_note}\n")
    lines.append(f"- 规则口径：{args.rule_note}\n")
    lines.append("- 命名说明：本文统一写“硬通过/软通过”，不使用训练阶段前缀命名\n\n")

    lines.append("## 通过口径说明\n\n")
    lines.append("硬通过部分只列 `hard_pass` 当前口径的组成项。预算合计、景点预算一致、餐饮预算一致、酒店覆盖晚数、用户预算约束等诊断项统一放在预算部分。\n\n")
    lines.append("软通过链路：`软通过 = 硬通过 + 景点多样性 + 餐饮多样性 + 预算偏好贴合`；`重算预算软通过 = 硬通过 + 景点多样性 + 餐饮多样性 + 重算预算贴合`。\n\n")
    lines.append("预算部分是诊断区，不等同于硬通过或软通过；其中 `预算偏好贴合` 和 `重算预算贴合` 同时也是软通过链路的预算项。\n\n")

    append_summary(
        lines,
        reports_by_label,
        labels,
        args.current_label,
        args.summary_note,
        args.primary_label,
        args.baseline_label,
    )

    lines.append("## 生成完成情况\n\n")
    lines.append("| 数据集 | " + " | ".join(labels) + " |\n")
    lines.append("|---|" + "|".join("---:" for _ in labels) + "|\n")
    lines.append(
        "| 标准集 | "
        + " | ".join(generation_cell(reports_by_label[label].get("standard"), standard_count) for label in labels)
        + " |\n"
    )
    lines.append(
        "| 困难集 | "
        + " | ".join(generation_cell(reports_by_label[label].get("hard"), hard_count) for label in labels)
        + " |\n\n"
    )

    append_scope(lines, "", args.standard_records, labels, reports_by_label, args.current_label, None, args.change_limit)
    append_scope(lines, "标准集", args.standard_records, labels, reports_by_label, args.current_label, "standard", args.change_limit)
    append_scope(lines, "困难集", args.hard_records, labels, reports_by_label, args.current_label, "hard", args.change_limit)

    lines.append("## 数据源\n\n")
    lines.append("| 版本 | 标准集报告 | 困难集报告 |\n")
    lines.append("|---|---|---|\n")
    for label in labels:
        version = f"当前 {label}" if label == args.current_label else label
        reports = reports_by_label[label]
        lines.append(f"| {version} | `{display_path(reports['standard'].path)}` | `{display_path(reports['hard'].path)}` |\n")
    lines.append("\n")

    lines.append("## 读数建议\n\n")
    lines.append("1. 读硬通过时只看 Hardpass 部分；预算合计类失败不要混进硬通过归因。\n")
    lines.append("2. 读软通过时重点看 Softpass 部分里的景点多样性、餐饮多样性、预算偏好贴合和重算预算贴合。\n")
    lines.append("3. Budget 部分用于解释预算问题，不要把每个预算诊断项都当成 hardpass/softpass 的组成项。\n")
    lines.append("4. 对长期接近 0 或规则口径可疑的指标，优先判断它是不是字段口径或规则口径问题，避免误导选型。\n")
    lines.append(f"5. {auto_recommendation(reports_by_label, labels, args.current_label)}\n")

    output_md.parent.mkdir(parents=True, exist_ok=True)
    output_md.write_text("".join(lines), encoding="utf-8")
    if args.output_json:
        write_machine_summary(args.output_json, reports_by_label, labels, args.current_label)

    print(f"full report md: {output_md}")
    if args.output_json:
        print(f"full report json: {args.output_json}")


if __name__ == "__main__":
    main()
