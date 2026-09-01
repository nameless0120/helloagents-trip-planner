"""Planner 模型评估公共工具。"""

from __future__ import annotations

import json
import math
import re
import sys
from collections import Counter, defaultdict
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any


_FILE_PATH = Path(__file__).resolve()
_ROOT_CANDIDATES = [
    _FILE_PATH.parents[3],
    _FILE_PATH.parents[4] if len(_FILE_PATH.parents) > 4 else _FILE_PATH.parents[3],
]


def _detect_project_root() -> Path:
    for candidate in _ROOT_CANDIDATES:
        if (candidate / "backend").exists() and (candidate / "training").exists():
            return candidate
    return _ROOT_CANDIDATES[0]


PROJECT_ROOT = _detect_project_root()
SCRIPTS_DIR = PROJECT_ROOT / "training" / "scripts"
BACKEND_DIR = PROJECT_ROOT / "backend"
sys.path.insert(0, str(SCRIPTS_DIR))
sys.path.insert(0, str(BACKEND_DIR))

from app.planner.output import (  # noqa: E402
    extract_json_object,
)
from app.models.schemas import TripPlan  # noqa: E402


DEFAULT_EVAL_RECORDS = PROJECT_ROOT / "training/data/planner/eval/records.jsonl"
DEFAULT_EVAL_OUTPUT_DIR = PROJECT_ROOT / "training/outputs/eval"
WEATHER_KEYS = ["day_weather", "night_weather", "day_temp", "night_temp", "wind_direction", "wind_power"]


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    """读取 JSONL。"""
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8") as file:
        return [json.loads(line) for line in file if line.strip()]


def write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    """覆盖写入 JSONL。"""
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as file:
        for row in rows:
            file.write(json.dumps(row, ensure_ascii=False) + "\n")


def append_jsonl(path: Path, row: dict[str, Any]) -> None:
    """追加一行 JSONL。"""
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as file:
        file.write(json.dumps(row, ensure_ascii=False) + "\n")


def write_json(path: Path, data: Any) -> None:
    """覆盖写入 JSON。"""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


def sanitize_name(value: str) -> str:
    """把模型/实验名转成路径安全名称。"""
    text = re.sub(r"[^0-9a-zA-Z._-]+", "_", value.strip())
    return text.strip("_") or "model"


def model_run_dir(model_name: str, output_dir: Path | None = None) -> Path:
    """返回模型评估输出目录。"""
    base = output_dir or DEFAULT_EVAL_OUTPUT_DIR
    return base / sanitize_name(model_name)


def load_records_by_id(records_path: Path) -> dict[str, dict[str, Any]]:
    """按 record_id 读取 eval records。"""
    return {row["record_id"]: row for row in read_jsonl(records_path)}


def trip_dates(request: dict[str, Any]) -> list[str]:
    """生成请求对应的日期序列。"""
    start = datetime.strptime(request["start_date"], "%Y-%m-%d")
    return [(start + timedelta(days=index)).strftime("%Y-%m-%d") for index in range(int(request["travel_days"]))]


def planner_max_output_tokens(request: dict[str, Any], base: int = 3000, per_day: int = 1800, cap: int = 16000) -> int:
    """按线上逻辑估算生成 token 上限。"""
    return min(base + int(request.get("travel_days", 1)) * per_day, cap)


def context_snapshot(record: dict[str, Any]) -> dict[str, Any]:
    """获取 PlannerContext tool_snapshot。"""
    return ((record.get("planner_context") or {}).get("tool_snapshot") or {})


def candidate_names(record: dict[str, Any], groups: list[str]) -> list[str]:
    """抽取工具候选名称。"""
    snapshot = context_snapshot(record)
    names = []
    for group in groups:
        names.extend(item.get("name", "") for item in snapshot.get(group, []) if item.get("name"))
    return names


def weather_bucket(record: dict[str, Any]) -> str:
    """归纳天气来源类型。"""
    sources = {item.get("source", "unknown") for item in context_snapshot(record).get("trip_weather") or []}
    if "open_meteo_archive" in sources:
        return "historical"
    if "amap_forecast" in sources:
        return "amap_forecast"
    if "unavailable_future_weather" in sources:
        return "future_unavailable"
    return "unknown"


def normalize_weather_value(key: str, value: Any) -> str:
    """天气字段归一化，忽略“级/风”等无害后缀差异。"""
    if value is None:
        return ""
    text = str(value).strip()
    if key == "wind_power" and text.endswith("级"):
        text = text[:-1]
    if key == "wind_direction" and text.endswith("风"):
        text = text[:-1]
    return text


def parse_trip_plan_output(output: str) -> tuple[TripPlan | None, dict[str, Any] | None, str | None, str | None]:
    """解析模型输出，返回 (TripPlan, data, error_stage, error_message)。"""
    try:
        data = extract_json_object(output)
    except Exception as exc:  # noqa: BLE001
        return None, None, "json_extract", str(exc)
    try:
        return TripPlan(**data), data, None, None
    except Exception as exc:  # noqa: BLE001
        return None, data, "schema", str(exc)


def summarize_request(record: dict[str, Any]) -> str:
    """短文本描述请求。"""
    request = record.get("request") or {}
    return (
        f"{request.get('city')} {request.get('start_date')}->{request.get('end_date')} "
        f"days={request.get('travel_days')} transport={request.get('transportation')} "
        f"hotel={request.get('accommodation')} prefs={request.get('preferences')}"
    )


def metric_rate(numerator: int, denominator: int) -> float:
    """百分比。"""
    if denominator <= 0:
        return 0.0
    return round(numerator / denominator, 4)


def average(values: list[float | int]) -> float:
    """均值。"""
    return round(sum(values) / len(values), 4) if values else 0.0


def percentile(values: list[float | int], p: float) -> float:
    """简单分位数。"""
    if not values:
        return 0.0
    ordered = sorted(values)
    index = min(len(ordered) - 1, max(0, round((len(ordered) - 1) * p)))
    return round(float(ordered[index]), 4)


def counter_to_dict(counter: Counter, limit: int | None = None) -> dict[str, int]:
    """Counter 转普通 dict。"""
    items = counter.most_common(limit)
    return {str(key): value for key, value in items}


def group_record_ids_by_slice(records: dict[str, dict[str, Any]]) -> dict[str, dict[str, set[str]]]:
    """按 control_spec 和天气来源生成切片 -> record_id 集合。"""
    groups: dict[str, dict[str, set[str]]] = defaultdict(lambda: defaultdict(set))
    for record_id, record in records.items():
        request = record.get("request") or {}
        control = record.get("control_spec") or {}
        slice_values = {
            "companion_type": control.get("companion_type", "unknown"),
            "city_tier": control.get("city_tier", "unknown"),
            "budget_level": control.get("budget_level", "unknown"),
            "diet": control.get("diet", "unknown"),
            "travel_days": str(request.get("travel_days", "unknown")),
            "weather_bucket": weather_bucket(record),
        }
        for slice_name, value in slice_values.items():
            groups[slice_name][str(value)].add(record_id)
    return groups


def sum_budget_parts(budget: dict[str, Any] | None) -> tuple[int, int]:
    """返回预算分项和总额。"""
    if not budget:
        return 0, 0
    part_sum = 0
    for key in ["total_attractions", "total_hotels", "total_meals", "total_transportation"]:
        try:
            part_sum += int(budget.get(key) or 0)
        except Exception:  # noqa: BLE001
            pass
    try:
        total = int(budget.get("total") or 0)
    except Exception:  # noqa: BLE001
        total = 0
    return part_sum, total


def structured_party_size(record: dict[str, Any]) -> int:
    """读取当前记录中的结构化同行人数。"""
    request = record.get("request") or {}
    contexts = [
        request,
        record.get("planner_context") or {},
        record.get("compact_planner_context") or {},
    ]
    for context in contexts:
        party = context.get("party") if isinstance(context, dict) else None
        if not isinstance(party, dict):
            continue
        try:
            total = int(party.get("total") or 0)
        except Exception:  # noqa: BLE001
            total = 0
        if total > 0:
            return total
    return 1


def hotel_room_count(record: dict[str, Any]) -> int:
    """按“两人一间”估算需要的房间数。"""
    return max(1, math.ceil(max(1, structured_party_size(record)) / 2))


def structured_budget_constraint(record: dict[str, Any]) -> dict[str, Any]:
    """读取 planner 结构化预算约束。"""
    request = record.get("request") or {}
    contexts = [
        request,
        record.get("planner_context") or {},
        record.get("compact_planner_context") or {},
    ]
    for context in contexts:
        constraint = context.get("budget_constraint") if isinstance(context, dict) else None
        if isinstance(constraint, dict):
            return constraint
    return {}


def budget_fit_policy(record: dict[str, Any]) -> dict[str, Any]:
    """读取 PlannerContext 中冻结的预算贴合策略。"""
    for context_key in ("planner_context", "compact_planner_context"):
        context = record.get(context_key) or {}
        constraints = context.get("planner_constraints") or {}
        policy = constraints.get("budget_fit_policy") or {}
        if isinstance(policy, dict) and policy.get("enabled"):
            return policy
    return {}


def requested_budget_total(record: dict[str, Any]) -> dict[str, Any]:
    """读取结构化用户预算，并换算为整趟总预算。"""
    constraint = structured_budget_constraint(record)
    request = record.get("request") or {}
    try:
        structured_amount = int(constraint.get("amount") or 0)
    except Exception:  # noqa: BLE001
        structured_amount = 0
    if structured_amount > 0:
        days = max(1, int(request.get("travel_days") or 1))
        party_size = structured_party_size(record)
        scope = str(constraint.get("scope") or "total")
        if scope in {"per_person_day", "per_person_per_day"}:
            total = structured_amount * party_size * days
        elif scope in {"per_person_total", "per_person"}:
            total = structured_amount * party_size
        else:
            total = structured_amount
        return {
            "available": True,
            "amount": structured_amount,
            "scope": scope,
            "party_size": party_size,
            "total": total,
            "source": "budget_constraint",
            "budget_level": constraint.get("budget_level", "unknown"),
            "strictness": constraint.get("strictness", "none"),
        }

    return {
        "available": False,
        "amount": 0,
        "scope": "unknown",
        "party_size": structured_party_size(record),
        "total": 0,
        "source": "none",
        "budget_level": constraint.get("budget_level", "unknown"),
        "strictness": constraint.get("strictness", "none"),
    }


def budget_level_aligned(record: dict[str, Any], budget: dict[str, Any] | None) -> bool:
    """预算消费是否匹配 planner 预算档位/预算贴合策略。

    优先使用 PlannerContext.planner_constraints.budget_fit_policy；
    如果记录没有冻结策略，再按结构化预算档位检查人均每天范围。
    """
    _, total = sum_budget_parts(budget)
    if total <= 0:
        return False

    policy = budget_fit_policy(record)
    if policy:
        try:
            target_min = int(policy.get("target_min_total") or 0)
            target_max = int(policy.get("target_max_total") or 0)
        except Exception:  # noqa: BLE001
            target_min = 0
            target_max = 0
        if target_min > 0 and total < target_min:
            return False
        if target_max > 0 and total > target_max:
            return False
        return True

    request = record.get("request") or {}
    control = record.get("control_spec") or {}
    constraint = structured_budget_constraint(record)
    days = max(1, int(request.get("travel_days") or 1))
    party_size = max(1, structured_party_size(record))
    per_person_day = total / days / party_size
    budget_level = str(constraint.get("budget_level") or control.get("budget_level") or "unknown")

    if budget_level == "limited":
        return per_person_day <= 350
    if budget_level in {"standard", "medium"}:
        return 180 <= per_person_day <= 500
    if budget_level in {"comfortable", "upper"}:
        return 300 <= per_person_day <= 850
    if budget_level == "premium":
        return 600 <= per_person_day <= 1500
    if budget_level == "luxury":
        return per_person_day >= 1000
    return True


def budget_within_user_budget(record: dict[str, Any], budget: dict[str, Any] | None, tolerance: float = 0.2) -> bool:
    """预算总额是否没有明显超过用户预算上限。"""
    _, total = sum_budget_parts(budget)
    if total <= 0:
        return False
    requested = requested_budget_total(record)
    if not requested["available"]:
        return True
    return total <= requested["total"] * (1 + tolerance) + 100


def hard_budget_constraint_ok(record: dict[str, Any], budget: dict[str, Any] | None) -> bool:
    """strictness=hard 时必须不超过用户总预算；非 hard 预算不作为硬失败。"""
    _, total = sum_budget_parts(budget)
    if total <= 0:
        return False
    requested = requested_budget_total(record)
    if not requested["available"]:
        return True
    if str(requested.get("strictness") or "none") != "hard":
        return True
    return total <= int(requested["total"])


def hotel_budget_details(
    record: dict[str, Any],
    plan: dict[str, Any] | None,
    budget: dict[str, Any] | None,
    tolerance: float = 0.2,
) -> dict[str, Any]:
    """检查酒店预算是否覆盖住宿晚数。

    TripPlan 里的 hotel.estimated_cost 是“单间每晚价格”，而 budget.total_hotels
    是酒店总费用。按“两人一间”估算房间数，所以每个住宿日的酒店预算
    应为 `hotel.estimated_cost * ceil(party.total / 2)`。
    """
    if not plan or not budget:
        return {
            "available": False,
            "lodging_nights": 0,
            "party_total": structured_party_size(record),
            "room_count": hotel_room_count(record),
            "priced_nights": 0,
            "expected_min_total_hotels": 0,
            "reported_total_hotels": 0,
            "diff": 0,
            "covers_nights": False,
        }

    days = plan.get("days") or []
    party_total = structured_party_size(record)
    room_count = hotel_room_count(record)
    lodging_policy = {}
    for context_key in ("planner_context", "compact_planner_context"):
        context = record.get(context_key) or {}
        if isinstance(context.get("lodging_policy"), dict):
            lodging_policy = context["lodging_policy"]
            break
    try:
        lodging_nights = int(lodging_policy.get("default_lodging_nights"))
    except Exception:  # noqa: BLE001
        request = record.get("request") or {}
        try:
            travel_days = int(request.get("travel_days") or len(days) or 1)
        except Exception:  # noqa: BLE001
            travel_days = len(days) or 1
        lodging_nights = max(0, travel_days - 1)

    expected_total = 0
    priced_nights = 0
    for day in days:
        if not isinstance(day, dict):
            continue
        hotel = day.get("hotel")
        if not isinstance(hotel, dict):
            continue
        try:
            cost = int(hotel.get("estimated_cost") or 0)
        except Exception:  # noqa: BLE001
            cost = 0
        if cost > 0:
            expected_total += cost * room_count
            priced_nights += 1

    try:
        reported_total = int(budget.get("total_hotels") or 0)
    except Exception:  # noqa: BLE001
        reported_total = 0

    if lodging_nights <= 0 and priced_nights == 0:
        covers_nights = reported_total == 0
    elif expected_total <= 0:
        covers_nights = False
    else:
        covers_nights = reported_total == expected_total

    return {
        "available": True,
        "lodging_nights": lodging_nights,
        "party_total": party_total,
        "room_count": room_count,
        "priced_nights": priced_nights,
        "expected_min_total_hotels": expected_total,
        "reported_total_hotels": reported_total,
        "diff": reported_total - expected_total,
        "covers_nights": covers_nights,
    }


def budget_alignment_details(
    record: dict[str, Any],
    budget: dict[str, Any] | None,
    plan: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """同时返回预算算术一致性和偏好对齐结果。"""
    part_sum, total = sum_budget_parts(budget)
    requested = requested_budget_total(record)
    request = record.get("request") or {}
    days = max(1, int(request.get("travel_days") or 1))
    party_size = max(1, structured_party_size(record))
    per_person_day = round(total / days / party_size, 2) if total > 0 else 0
    arithmetic_ok = budget_consistent(budget)
    within_user_budget = budget_within_user_budget(record, budget)
    user_constraint_ok = hard_budget_constraint_ok(record, budget)
    level_ok = budget_level_aligned(record, budget)
    hotel_budget = hotel_budget_details(record, plan, budget)
    policy = budget_fit_policy(record)
    constraint = structured_budget_constraint(record)
    return {
        "part_sum": part_sum,
        "total": total,
        "diff": part_sum - total,
        "requested_budget": requested,
        "per_person_day": per_person_day,
        "budget_level": constraint.get("budget_level") or (record.get("control_spec") or {}).get("budget_level", "unknown"),
        "strictness": constraint.get("strictness", requested.get("strictness", "none")),
        "budget_fit_policy": policy,
        "arithmetic_consistent": arithmetic_ok,
        "within_user_budget": within_user_budget,
        "user_constraint_ok": user_constraint_ok,
        "level_aligned": level_ok,
        "preference_aligned": user_constraint_ok and level_ok,
        "hotel_budget": hotel_budget,
        "hotel_budget_covers_nights": hotel_budget["covers_nights"],
    }


def budget_consistent(budget: dict[str, Any] | None, tolerance: float = 0.0) -> bool:
    """预算总额是否和分项精确一致。"""
    part_sum, total = sum_budget_parts(budget)
    if total <= 0:
        return False
    if tolerance <= 0:
        return part_sum == total
    return math.isclose(part_sum, total, rel_tol=tolerance, abs_tol=100)
