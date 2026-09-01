"""审计宽预算样本的 PlannerContext 候选可达性。

只生成 TripRequest 和 PlannerContext，不调用 Planner LLM，也不写 SFT 数据。
重点检查 comfortable/premium/luxury soft 请求里，高价酒店、餐饮、景点和体验
候选是否足以支撑预算利用型样本。
"""

from __future__ import annotations

import argparse
import json
import math
import os
import statistics
import sys
import time
from collections import Counter, defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

SCRIPTS_DIR = Path(__file__).resolve().parents[2]
DATA_SCRIPT_DIR = SCRIPTS_DIR / "planner" / "data"
if str(DATA_SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(DATA_SCRIPT_DIR))

import generate_sft_data as gen  # noqa: E402


DEFAULT_OUTPUT_DIR = (
    gen.PROJECT_ROOT
    / "training"
    / "outputs"
    / "eval"
    / "budget_utilization_context_audit_100"
)

BUDGET_UTILIZATION_WEIGHTS = [
    (("comfortable", "soft"), 50),
    (("premium", "soft"), 50),
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="生成并审计预算利用型 PlannerContext")
    parser.add_argument("--count", type=int, default=100)
    parser.add_argument("--start-index", type=int, default=3000)
    parser.add_argument("--seed", type=int, default=20260429)
    parser.add_argument("--date-mode", choices=["future", "mixed", "past"], default="mixed")
    parser.add_argument("--workers", type=int, default=8)
    parser.add_argument(
        "--historical-weather-provider",
        choices=["open-meteo", "none"],
        default="open-meteo",
    )
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument("--include-full-context", action="store_true", default=True)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    gen.load_project_env()
    amap_api_key = os.getenv("AMAP_MAPS_API_KEY") or os.getenv("AMAP_API_KEY")
    if not amap_api_key:
        raise RuntimeError("缺少 AMAP_MAPS_API_KEY 或 AMAP_API_KEY")

    monkeypatch_budget_utilization_distribution()

    args.output_dir.mkdir(parents=True, exist_ok=True)
    contexts_path = args.output_dir / "contexts.jsonl"
    errors_path = args.output_dir / "errors.jsonl"
    report_path = args.output_dir / "context_audit_report.md"
    summary_path = args.output_dir / "summary.json"

    started_at = time.perf_counter()
    indices = [args.start_index + offset for offset in range(args.count)]
    results: list[dict[str, Any]] = []
    errors: list[dict[str, Any]] = []

    print(
        f"开始预算利用型 Context 审计: count={args.count}, workers={args.workers}, "
        f"output_dir={args.output_dir}",
        flush=True,
    )
    with ThreadPoolExecutor(max_workers=max(1, args.workers)) as executor:
        futures = {
            executor.submit(collect_one, index, args, amap_api_key): index
            for index in indices
        }
        for progress, future in enumerate(as_completed(futures), start=1):
            index = futures[future]
            try:
                item = future.result()
                results.append(item)
                audit = item["audit"]
                print(
                    f"context progress: {progress}/{len(indices)} ok={len(results)} "
                    f"failed={len(errors)} last={item['record_id']} "
                    f"{audit['budget_level']} ratio_high={audit['high_budget_ratio']:.2f} "
                    f"food_max={audit['food']['max']} exp_max={audit['experience']['max']} "
                    f"scenic_max={audit['scenic']['max']}",
                    flush=True,
                )
            except Exception as exc:  # noqa: BLE001
                error = {
                    "record_id": gen.format_request_id(index),
                    "error": str(exc),
                    "created_at": datetime.now(timezone.utc).isoformat(),
                }
                errors.append(error)
                print(
                    f"context progress: {progress}/{len(indices)} ok={len(results)} "
                    f"failed={len(errors)} error={error['record_id']} {exc}",
                    flush=True,
                )

    write_jsonl(contexts_path, results)
    write_jsonl(errors_path, errors)
    summary = build_summary(results, errors, time.perf_counter() - started_at)
    summary_path.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    report_path.write_text(render_report(summary, results, contexts_path, errors_path), encoding="utf-8")
    print(f"写出: {contexts_path}")
    print(f"写出: {report_path}")
    print(f"写出: {summary_path}")


def monkeypatch_budget_utilization_distribution() -> None:
    """复用 generate_sft_data 的生成函数，但把分布改成宽预算 soft。"""
    gen.SUPPLEMENT_VERSION = "budget_utilization_context_audit"
    gen.SUPPLEMENT_BUDGET_STRICTNESS_WEIGHTS = list(BUDGET_UTILIZATION_WEIGHTS)
    gen.SUPPLEMENT_TRAVEL_DAYS_WEIGHTS = [(3, 20), (4, 40), (5, 40)]
    gen.SUPPLEMENT_SOFT_BUDGET_POLICY = {
        "target_min_ratio": 0.95,
        "target_max_ratio": 1.05,
        "validation_min_margin": 0.0,
        "validation_max_margin": 0.0,
        "instruction": (
            "预算利用型样本：soft budget 应尽量落在预算的95%-105%之间，"
            "优先升级酒店、品质餐饮和真实付费体验，避免低配省钱方案。"
        ),
    }


def collect_one(index: int, args: argparse.Namespace, amap_api_key: str) -> dict[str, Any]:
    raw_request = gen.generate_budget_supplement_request(index, args)
    request = gen.normalize_request(raw_request, raw_request["request_id"])
    gen.validate_request_date_mode(request, args.date_mode)

    builder = gen.get_worker_context_builder(amap_api_key, args.historical_weather_provider)
    started_at = time.perf_counter()
    planner_context = builder.collect(request)
    gen.apply_budget_fit_policy(planner_context, request, raw_request)
    compact_context = builder.compact_for_planner(planner_context)
    control_spec = gen.record_control_spec(raw_request, request, planner_context)
    audit = audit_context(request.model_dump(), planner_context)

    item = {
        "record_id": raw_request["request_id"],
        "created_at": datetime.now(timezone.utc).isoformat(),
        "request": request.model_dump(),
        "control_spec": control_spec,
        "elapsed_seconds": round(time.perf_counter() - started_at, 3),
        "compact_planner_context": compact_context,
        "audit": audit,
    }
    if args.include_full_context:
        item["planner_context"] = planner_context
    return item


def audit_context(request: dict[str, Any], planner_context: dict[str, Any]) -> dict[str, Any]:
    snapshot = planner_context.get("tool_snapshot") or {}
    party_total = max(int((request.get("party") or {}).get("total") or 1), 1)
    travel_days = max(int(request.get("travel_days") or 1), 1)
    rooms = math.ceil(party_total / 2)
    lodging_nights = int((planner_context.get("lodging_policy") or {}).get("default_lodging_nights") or max(travel_days - 1, 0))
    budget = request.get("budget_constraint") or {}
    amount = int(budget.get("amount") or 0)
    policy = (planner_context.get("planner_constraints") or {}).get("budget_fit_policy") or {}

    hotels = snapshot.get("hotel_pois") or []
    foods = snapshot.get("food_pois") or []
    scenic = snapshot.get("scenic_pois") or []
    experience = snapshot.get("experience_pois") or []
    attraction_candidates = dedupe_named(scenic + experience)

    food_lunch_dinner = [
        row for row in foods
        if not is_breakfast_only(row)
    ]
    breakfast_candidates = [
        row for row in foods
        if "breakfast" in {str(role).lower() for role in (row.get("meal_roles") or [])}
    ]

    hotel_prices = numeric_values(hotels, "estimated_cost_hint")
    lunch_dinner_prices = numeric_values(food_lunch_dinner, "meal_cost_hint")
    breakfast_prices = numeric_values(breakfast_candidates, "meal_cost_hint")
    attraction_prices = numeric_values(attraction_candidates, "ticket_price_hint")

    hotel_high = max(hotel_prices or [0]) * lodging_nights * rooms
    breakfast_high = (max(breakfast_prices or [25]) * travel_days * party_total)
    meal_high = sum_top(lunch_dinner_prices, travel_days * 2) * party_total + breakfast_high
    attraction_high = sum_top(attraction_prices, travel_days * 2) * party_total
    transport_high = estimate_transportation_total(request)
    high_total = hotel_high + meal_high + attraction_high + transport_high

    target_min = int(policy.get("target_min_total") or round(amount * 0.95))
    target_max = int(policy.get("target_max_total") or round(amount * 1.05))
    target_mid = int(round((target_min + target_max) / 2)) if target_min and target_max else amount

    return {
        "city": request.get("city"),
        "travel_days": travel_days,
        "party_total": party_total,
        "rooms": rooms,
        "lodging_nights": lodging_nights,
        "budget_level": budget.get("budget_level"),
        "strictness": budget.get("strictness"),
        "budget_amount": amount,
        "target_min_total": target_min,
        "target_max_total": target_max,
        "target_mid_total": target_mid,
        "tool_counts": {
            key: len(snapshot.get(key) or [])
            for key in ["classic_pois", "preference_pois", "scenic_pois", "experience_pois", "hotel_pois", "food_pois"]
        },
        "bucket_counts": {
            "food": bucket_counts(foods),
            "scenic": bucket_counts(scenic),
            "experience": bucket_counts(experience),
            "hotel": bucket_counts(hotels),
        },
        "hotel": price_summary(hotels, "estimated_cost_hint", [800, 1200, 1800]),
        "food": price_summary(foods, "meal_cost_hint", [120, 180, 260, 380]),
        "lunch_dinner_food": price_summary(food_lunch_dinner, "meal_cost_hint", [120, 180, 260, 380]),
        "scenic": price_summary(scenic, "ticket_price_hint", [120, 180, 280]),
        "experience": price_summary(experience, "ticket_price_hint", [120, 180, 280]),
        "attraction_combined": price_summary(attraction_candidates, "ticket_price_hint", [120, 180, 280]),
        "top_food": top_candidates(foods, "meal_cost_hint", 8),
        "top_scenic": top_candidates(scenic, "ticket_price_hint", 8),
        "top_experience": top_candidates(experience, "ticket_price_hint", 8),
        "top_hotel": top_candidates(hotels, "estimated_cost_hint", 5),
        "estimated_high_budget": {
            "total": high_total,
            "hotels": hotel_high,
            "meals": meal_high,
            "attractions": attraction_high,
            "transportation": transport_high,
        },
        "high_budget_ratio": round(high_total / amount, 4) if amount else 0,
        "can_reach_target_min": high_total >= target_min if target_min else False,
        "can_reach_target_mid": high_total >= target_mid if target_mid else False,
        "has_high_food": any((as_number(row.get("meal_cost_hint")) or 0) >= 180 for row in foods),
        "has_high_experience": any((as_number(row.get("ticket_price_hint")) or 0) >= 180 for row in experience),
        "has_high_scenic": any((as_number(row.get("ticket_price_hint")) or 0) >= 180 for row in scenic),
    }


def is_breakfast_only(row: dict[str, Any]) -> bool:
    roles = {str(role).strip().lower() for role in row.get("meal_roles") or []}
    return roles == {"breakfast"} or str(row.get("source_bucket") or "") == "food_breakfast"


def estimate_transportation_total(request: dict[str, Any]) -> int:
    mode = str(request.get("transportation") or "")
    days = max(int(request.get("travel_days") or 1), 1)
    if any(word in mode for word in ["公共", "公交", "地铁"]):
        per_day = 50
    elif any(word in mode for word in ["自驾"]):
        per_day = 220
    elif any(word in mode for word in ["打车", "出租"]):
        per_day = 180
    else:
        per_day = 90
    return per_day * days


def price_summary(rows: list[dict[str, Any]], key: str, thresholds: list[int]) -> dict[str, Any]:
    values = numeric_values(rows, key)
    return {
        "count": len(rows),
        "priced_count": len(values),
        "min": int(min(values)) if values else 0,
        "p50": int(percentile(values, 0.50)) if values else 0,
        "p75": int(percentile(values, 0.75)) if values else 0,
        "p90": int(percentile(values, 0.90)) if values else 0,
        "max": int(max(values)) if values else 0,
        "avg": round(statistics.mean(values), 1) if values else 0,
        "threshold_counts": {f"ge_{threshold}": sum(value >= threshold for value in values) for threshold in thresholds},
    }


def numeric_values(rows: list[dict[str, Any]], key: str) -> list[float]:
    values = []
    for row in rows:
        value = as_number(row.get(key))
        if value is not None:
            values.append(value)
    return values


def as_number(value: Any) -> float | None:
    if value in (None, "", []):
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def percentile(values: list[float], q: float) -> float:
    if not values:
        return 0
    ordered = sorted(values)
    return ordered[round((len(ordered) - 1) * q)]


def sum_top(values: list[float], count: int) -> int:
    if count <= 0:
        return 0
    return int(sum(sorted(values, reverse=True)[:count]))


def bucket_counts(rows: list[dict[str, Any]]) -> dict[str, int]:
    return dict(Counter(str(row.get("source_bucket") or "unknown") for row in rows))


def dedupe_named(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    seen = set()
    results = []
    for row in rows:
        key = gen.normalize_poi_name(str(row.get("name") or ""))
        if not key or key in seen:
            continue
        seen.add(key)
        results.append(row)
    return results


def top_candidates(rows: list[dict[str, Any]], key: str, limit: int) -> list[dict[str, Any]]:
    ranked = sorted(
        rows,
        key=lambda row: as_number(row.get(key)) or 0,
        reverse=True,
    )
    results = []
    for row in ranked[:limit]:
        results.append(
            {
                "name": row.get("name", ""),
                "price": int(as_number(row.get(key)) or 0),
                "source_bucket": row.get("source_bucket", ""),
                "source_keyword": row.get("source_keyword", ""),
                "cost_source": row.get("cost_source") or row.get("ticket_price_source") or "",
                "type": row.get("type", ""),
            }
        )
    return results


def build_summary(results: list[dict[str, Any]], errors: list[dict[str, Any]], elapsed: float) -> dict[str, Any]:
    audits = [item["audit"] for item in results]
    by_level: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for audit in audits:
        by_level[str(audit.get("budget_level") or "unknown")].append(audit)

    return {
        "created_at": datetime.now(timezone.utc).isoformat(),
        "count": len(results),
        "failed": len(errors),
        "elapsed_seconds": round(elapsed, 3),
        "budget_level": dict(Counter(audit["budget_level"] for audit in audits)),
        "city_top20": dict(Counter(audit["city"] for audit in audits).most_common(20)),
        "travel_days": dict(Counter(audit["travel_days"] for audit in audits)),
        "overall": aggregate_audits(audits),
        "by_budget_level": {
            level: aggregate_audits(items)
            for level, items in sorted(by_level.items())
        },
        "weak_cases": weakest_cases(audits, 20),
    }


def aggregate_audits(audits: list[dict[str, Any]]) -> dict[str, Any]:
    if not audits:
        return {}
    ratios = [audit["high_budget_ratio"] for audit in audits]
    return {
        "count": len(audits),
        "can_reach_target_min_rate": round(sum(audit["can_reach_target_min"] for audit in audits) / len(audits), 4),
        "can_reach_target_mid_rate": round(sum(audit["can_reach_target_mid"] for audit in audits) / len(audits), 4),
        "has_high_food_rate": round(sum(audit["has_high_food"] for audit in audits) / len(audits), 4),
        "has_high_experience_rate": round(sum(audit["has_high_experience"] for audit in audits) / len(audits), 4),
        "has_high_scenic_rate": round(sum(audit["has_high_scenic"] for audit in audits) / len(audits), 4),
        "high_budget_ratio_avg": round(statistics.mean(ratios), 3),
        "high_budget_ratio_p25": round(percentile(ratios, 0.25), 3),
        "high_budget_ratio_p50": round(percentile(ratios, 0.50), 3),
        "high_budget_ratio_p75": round(percentile(ratios, 0.75), 3),
        "food_max_avg": round(statistics.mean(audit["food"]["max"] for audit in audits), 1),
        "food_ge_180_rate": round(sum(audit["food"]["threshold_counts"].get("ge_180", 0) > 0 for audit in audits) / len(audits), 4),
        "experience_max_avg": round(statistics.mean(audit["experience"]["max"] for audit in audits), 1),
        "experience_ge_180_rate": round(sum(audit["experience"]["threshold_counts"].get("ge_180", 0) > 0 for audit in audits) / len(audits), 4),
        "scenic_max_avg": round(statistics.mean(audit["scenic"]["max"] for audit in audits), 1),
        "scenic_ge_180_rate": round(sum(audit["scenic"]["threshold_counts"].get("ge_180", 0) > 0 for audit in audits) / len(audits), 4),
        "hotel_max_avg": round(statistics.mean(audit["hotel"]["max"] for audit in audits), 1),
    }


def weakest_cases(audits: list[dict[str, Any]], limit: int) -> list[dict[str, Any]]:
    weak = sorted(audits, key=lambda item: (item["can_reach_target_min"], item["high_budget_ratio"]))[:limit]
    return [
        {
            "city": item["city"],
            "budget_level": item["budget_level"],
            "budget_amount": item["budget_amount"],
            "travel_days": item["travel_days"],
            "party_total": item["party_total"],
            "high_budget_ratio": item["high_budget_ratio"],
            "can_reach_target_min": item["can_reach_target_min"],
            "food_max": item["food"]["max"],
            "experience_max": item["experience"]["max"],
            "scenic_max": item["scenic"]["max"],
            "hotel_max": item["hotel"]["max"],
            "top_food": item["top_food"][:3],
            "top_experience": item["top_experience"][:3],
            "top_scenic": item["top_scenic"][:3],
        }
        for item in weak
    ]


def render_report(
    summary: dict[str, Any],
    results: list[dict[str, Any]],
    contexts_path: Path,
    errors_path: Path,
) -> str:
    lines = [
        "# 预算利用型 Context 审计",
        "",
        f"- 样本数：{summary['count']}",
        f"- 失败数：{summary['failed']}",
        f"- 耗时：{summary['elapsed_seconds']} 秒",
        f"- contexts：`{contexts_path}`",
        f"- errors：`{errors_path}`",
        "",
        "## 分布",
        "",
        f"- budget_level：`{json.dumps(summary['budget_level'], ensure_ascii=False)}`",
        f"- travel_days：`{json.dumps(summary['travel_days'], ensure_ascii=False)}`",
        "",
        "## 核心可达性",
        "",
        render_aggregate_table({"overall": summary["overall"], **summary["by_budget_level"]}),
        "",
        "说明：`high_budget_ratio` 是用当前候选池做粗上限估算，不是模型输出预算；用于判断候选是否足以支撑 95%-105% 的预算利用型样本。",
        "",
        "## 最弱样本 Top20",
        "",
        "| 城市 | 档位 | 预算 | 天数 | 人数 | 高配估算/预算 | 可达target_min | food max | exp max | scenic max | hotel max |",
        "| --- | --- | ---: | ---: | ---: | ---: | --- | ---: | ---: | ---: | ---: |",
    ]
    for item in summary["weak_cases"]:
        lines.append(
            f"| {item['city']} | {item['budget_level']} | {item['budget_amount']} | "
            f"{item['travel_days']} | {item['party_total']} | {item['high_budget_ratio']:.2f} | "
            f"{'是' if item['can_reach_target_min'] else '否'} | {item['food_max']} | "
            f"{item['experience_max']} | {item['scenic_max']} | {item['hotel_max']} |"
        )

    lines.extend(["", "## 高价候选示例", ""])
    for item in results[:12]:
        audit = item["audit"]
        lines.append(
            f"### {item['record_id']} {audit['city']} {audit['budget_level']} "
            f"{audit['budget_amount']}元 ratio_high={audit['high_budget_ratio']:.2f}"
        )
        lines.append("")
        lines.append("- 餐饮：" + format_top(audit["top_food"][:5]))
        lines.append("- 体验：" + format_top(audit["top_experience"][:5]))
        lines.append("- 景点：" + format_top(audit["top_scenic"][:5]))
        lines.append("- 酒店：" + format_top(audit["top_hotel"][:3]))
        lines.append("")

    return "\n".join(lines) + "\n"


def render_aggregate_table(groups: dict[str, dict[str, Any]]) -> str:
    lines = [
        "| 分组 | 数量 | 可达target_min | 可达target_mid | 高价餐饮覆盖 | 高价体验覆盖 | 高价景点覆盖 | high ratio p50 | food max均值 | exp max均值 | scenic max均值 | hotel max均值 |",
        "| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for name, item in groups.items():
        lines.append(
            f"| {name} | {item.get('count', 0)} | {pct_text(item.get('can_reach_target_min_rate', 0))} | "
            f"{pct_text(item.get('can_reach_target_mid_rate', 0))} | {pct_text(item.get('has_high_food_rate', 0))} | "
            f"{pct_text(item.get('has_high_experience_rate', 0))} | {pct_text(item.get('has_high_scenic_rate', 0))} | "
            f"{item.get('high_budget_ratio_p50', 0):.2f} | {item.get('food_max_avg', 0):.1f} | "
            f"{item.get('experience_max_avg', 0):.1f} | {item.get('scenic_max_avg', 0):.1f} | {item.get('hotel_max_avg', 0):.1f} |"
        )
    return "\n".join(lines)


def pct_text(value: float) -> str:
    return f"{value * 100:.1f}%"


def format_top(items: list[dict[str, Any]]) -> str:
    if not items:
        return "无"
    return " / ".join(
        f"{item['name']}({item['price']}元,{item['source_bucket']}/{item['source_keyword']})"
        for item in items
    )


def write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    with path.open("w", encoding="utf-8") as fh:
        for row in rows:
            fh.write(json.dumps(row, ensure_ascii=False) + "\n")


if __name__ == "__main__":
    main()
