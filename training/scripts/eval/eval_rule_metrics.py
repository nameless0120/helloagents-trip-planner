"""对模型生成结果做规则评估。"""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path
from typing import Any

from eval_utils import (
    DEFAULT_EVAL_RECORDS,
    DEFAULT_EVAL_OUTPUT_DIR,
    WEATHER_KEYS,
    average,
    budget_alignment_details,
    candidate_names,
    context_snapshot,
    counter_to_dict,
    hotel_room_count,
    load_records_by_id,
    metric_rate,
    normalize_weather_value,
    parse_trip_plan_output,
    percentile,
    read_jsonl,
    structured_party_size,
    summarize_request,
    trip_dates,
    weather_bucket,
    write_json,
)
from app.planner.output import (  # noqa: E402
    is_lodging_breakfast_meal,
    is_placeholder_hotel_distance,
    is_placeholder_meal_name,
    name_in_candidates,
)


def evaluate_output(record: dict[str, Any], generation: dict[str, Any]) -> dict[str, Any]:
    """评估单条输出。"""
    output = generation.get("output", "")
    result: dict[str, Any] = {
        "record_id": record["record_id"],
        "request_summary": summarize_request(record),
        "control_spec": record.get("control_spec", {}),
        "weather_bucket": weather_bucket(record),
        "call_ok": bool(generation.get("ok")),
        "latency_seconds": generation.get("latency_seconds"),
        "output_chars": generation.get("output_chars", len(output)),
        "errors": [],
        "metrics": {},
    }
    metrics = result["metrics"]

    if not generation.get("ok"):
        result["errors"].append({"stage": "call", "message": generation.get("error", "call failed")})
        return result

    trip_plan, data, error_stage, error = parse_trip_plan_output(output)
    metrics["json_extract_ok"] = error_stage != "json_extract"
    metrics["schema_ok"] = trip_plan is not None
    if error_stage:
        result["errors"].append({"stage": error_stage, "message": error})
        return result

    assert trip_plan is not None
    plan = trip_plan.model_dump()
    request = record.get("request") or {}
    expected_dates = trip_dates(request)

    metrics["city_ok"] = plan.get("city") == request.get("city")
    metrics["date_range_ok"] = plan.get("start_date") == request.get("start_date") and plan.get("end_date") == request.get("end_date")
    metrics["days_len_ok"] = len(plan.get("days") or []) == int(request.get("travel_days", 0))
    metrics["day_dates_ok"] = [day.get("date") for day in plan.get("days") or []] == expected_dates
    metrics["weather_dates_ok"] = [item.get("date") for item in plan.get("weather_info") or []] == expected_dates

    day_index_ok = True
    meal_complete = True
    attraction_count_ok = True
    middle_hotel_ok = True
    invalid_hotel_name_ok = True
    hotel_distance_placeholder_ok = True
    location_object_ok = True
    attraction_total = 0
    attraction_hit = 0
    hotel_total = 0
    hotel_hit = 0
    meal_total = 0
    meal_hit = 0
    meal_semantic_hit = 0
    attraction_ticket_sum = 0
    meal_cost_sum = 0
    accommodation_type_ok = True
    meal_specific_ok = True
    meal_valid_semantics_ok = True
    meal_lunch_dinner_same_day_ok = True
    meal_repeat_limit_ok = True
    too_many_attractions = []
    repeated_attractions = []
    middle_hotel_null = []
    placeholder_hotel_distances = []
    placeholder_meals = []
    ungrounded_meals = []
    invalid_meals = []
    accommodation_mismatches = []
    same_day_repeated_meals = []
    repeated_meals = []
    meal_diversity_counts: Counter[str] = Counter()
    meal_diversity_details: dict[str, list[dict[str, Any]]] = {}
    attraction_diversity_counts: Counter[str] = Counter()
    attraction_diversity_details: dict[str, list[dict[str, Any]]] = {}

    attraction_candidates = candidate_names(record, ["classic_pois", "preference_pois", "scenic_pois", "experience_pois"])
    hotel_candidates = candidate_names(record, ["hotel_pois"])
    food_candidates = candidate_names(record, ["food_pois"])
    food_candidate_keys = {key for name in food_candidates if (key := meal_diversity_key(name))}
    food_candidate_count = len(food_candidate_keys)

    days = plan.get("days") or []
    for index, day in enumerate(days):
        if day.get("day_index") != index:
            day_index_ok = False
        if day.get("accommodation") != request.get("accommodation"):
            accommodation_type_ok = False
            accommodation_mismatches.append(
                {
                    "date": day.get("date"),
                    "day_index": day.get("day_index"),
                    "expected": request.get("accommodation"),
                    "got": day.get("accommodation"),
                }
            )

        meal_types = {str(item.get("type", "")).lower() for item in day.get("meals") or []}
        if not {"breakfast", "lunch", "dinner"}.issubset(meal_types):
            meal_complete = False

        attractions = day.get("attractions") or []
        if not (1 <= len(attractions) <= 3):
            attraction_count_ok = False
            if len(attractions) > 3:
                too_many_attractions.append({"date": day.get("date"), "count": len(attractions)})

        for attraction in attractions:
            name = attraction.get("name", "")
            attraction_total += 1
            attraction_ticket_sum += _safe_int(attraction.get("ticket_price"))
            if name_in_candidates(name, attraction_candidates):
                attraction_hit += 1
            diversity_key = attraction_diversity_key(name)
            if diversity_key:
                attraction_diversity_counts[diversity_key] += 1
                attraction_diversity_details.setdefault(diversity_key, []).append(
                    {
                        "date": day.get("date"),
                        "day_index": day.get("day_index"),
                        "name": name,
                    }
                )
            location = attraction.get("location")
            if not isinstance(location, dict) or "longitude" not in location or "latitude" not in location:
                location_object_ok = False

        hotel = day.get("hotel")
        if hotel is None:
            if index < len(days) - 1:
                middle_hotel_ok = False
                middle_hotel_null.append({"date": day.get("date"), "day_index": day.get("day_index")})
        else:
            hotel_total += 1
            name = hotel.get("name", "")
            if not name or name_in_candidates(name, hotel_candidates):
                hotel_hit += int(bool(name))
            if not name or _invalid_hotel_name(name):
                invalid_hotel_name_ok = False
            distance = str(hotel.get("distance") or "")
            if is_placeholder_hotel_distance(distance):
                hotel_distance_placeholder_ok = False
                placeholder_hotel_distances.append({"date": day.get("date"), "day_index": day.get("day_index"), "name": name, "distance": distance})
            location = hotel.get("location")
            if location is not None and (not isinstance(location, dict) or "longitude" not in location or "latitude" not in location):
                location_object_ok = False

        day_lunch_dinner_keys: dict[str, dict[str, Any]] = {}
        for meal in day.get("meals") or []:
            meal_name = str(meal.get("name") or "")
            meal_type = str(meal.get("type") or "").lower()
            meal_total += 1
            meal_cost_sum += _safe_int(meal.get("estimated_cost"))
            if is_placeholder_meal_name(meal_name):
                meal_specific_ok = False
                placeholder_meals.append({"date": day.get("date"), "type": meal.get("type"), "name": meal_name})
            diversity_key = meal_diversity_key(meal_name)
            lodging_breakfast = is_lodging_breakfast_meal(meal_name, meal_type)
            if diversity_key and not lodging_breakfast:
                meal_diversity_counts[diversity_key] += 1
                meal_diversity_details.setdefault(diversity_key, []).append(
                    {
                        "date": day.get("date"),
                        "type": meal.get("type"),
                        "name": meal_name,
                    }
                )
                if meal_type in {"lunch", "dinner"}:
                    day_lunch_dinner_keys[meal_type] = {
                        "key": diversity_key,
                        "name": meal_name,
                    }
            if lodging_breakfast or name_in_candidates(meal_name, food_candidates):
                meal_hit += 1
                meal_semantic_hit += 1
            else:
                ungrounded_meals.append({"date": day.get("date"), "type": meal.get("type"), "name": meal_name})
                validity = meal_semantic_validity(meal_name, meal_type, hotel_candidates)
                if validity["valid"]:
                    meal_semantic_hit += 1
                else:
                    meal_valid_semantics_ok = False
                    invalid_meals.append(
                        {
                            "date": day.get("date"),
                            "type": meal.get("type"),
                            "name": meal_name,
                            "reason": validity["reason"],
                        }
                    )
            location = meal.get("location")
            if location is not None and (not isinstance(location, dict) or "longitude" not in location or "latitude" not in location):
                location_object_ok = False
        lunch_row = day_lunch_dinner_keys.get("lunch")
        dinner_row = day_lunch_dinner_keys.get("dinner")
        if food_candidate_count >= 2 and lunch_row and dinner_row and lunch_row["key"] == dinner_row["key"]:
            meal_lunch_dinner_same_day_ok = False
            same_day_repeated_meals.append(
                {
                    "date": day.get("date"),
                    "lunch": lunch_row["name"],
                    "dinner": dinner_row["name"],
                }
            )

    if food_candidate_count >= 3:
        # 旅行餐饮应有变化，但偶尔复用真实餐厅可以接受。
        # 3天最多2次，4-5天最多3次；酒店/民宿/客栈早餐已在上面排除。
        max_allowed_repeat = max(2, (len(days) * 3 + 4) // 5)
    else:
        max_allowed_repeat = None
    if max_allowed_repeat is not None:
        for key, count in meal_diversity_counts.items():
            if count > max_allowed_repeat:
                meal_repeat_limit_ok = False
                repeated_meals.append(
                    {
                        "name_key": key,
                        "count": count,
                        "max_allowed": max_allowed_repeat,
                        "occurrences": meal_diversity_details.get(key, [])[:10],
                    }
                )

    attraction_repeat_limit_ok = True
    for key, count in attraction_diversity_counts.items():
        if count > 1:
            attraction_repeat_limit_ok = False
            repeated_attractions.append(
                {
                    "name_key": key,
                    "count": count,
                    "max_allowed": 1,
                    "occurrences": attraction_diversity_details.get(key, [])[:10],
                }
            )

    metrics["day_index_ok"] = day_index_ok
    metrics["accommodation_type_ok"] = accommodation_type_ok
    metrics["meal_complete"] = meal_complete
    metrics["attraction_count_ok"] = attraction_count_ok
    metrics["attraction_repeat_limit_ok"] = attraction_repeat_limit_ok
    metrics["attraction_diversity_ok"] = attraction_repeat_limit_ok
    metrics["middle_hotel_ok"] = middle_hotel_ok
    metrics["invalid_hotel_name_ok"] = invalid_hotel_name_ok
    metrics["hotel_distance_placeholder_ok"] = hotel_distance_placeholder_ok
    metrics["meal_specific_ok"] = meal_specific_ok
    metrics["meal_valid_semantics_ok"] = meal_valid_semantics_ok
    metrics["meal_lunch_dinner_same_day_ok"] = meal_lunch_dinner_same_day_ok
    metrics["meal_repeat_limit_ok"] = meal_repeat_limit_ok
    metrics["meal_diversity_ok"] = meal_lunch_dinner_same_day_ok and meal_repeat_limit_ok
    metrics["location_object_ok"] = location_object_ok
    metrics["attraction_grounding_rate"] = metric_rate(attraction_hit, attraction_total)
    metrics["attraction_grounding_ok"] = attraction_hit == attraction_total
    metrics["attraction_diversity_unique_rate"] = metric_rate(len(attraction_diversity_counts), sum(attraction_diversity_counts.values()))
    metrics["hotel_grounding_rate"] = metric_rate(hotel_hit, hotel_total)
    metrics["hotel_grounding_ok"] = hotel_hit == hotel_total
    metrics["meal_food_pois_grounding_rate"] = metric_rate(meal_hit, meal_total)
    metrics["meal_semantic_valid_rate"] = metric_rate(meal_semantic_hit, meal_total)
    metrics["meal_grounding_rate"] = metric_rate(meal_hit, meal_total)
    metrics["meal_grounding_ok"] = meal_hit == meal_total
    metrics["meal_diversity_unique_rate"] = metric_rate(len(meal_diversity_counts), sum(meal_diversity_counts.values()))
    budget_eval = budget_alignment_details(record, plan.get("budget"), plan)
    result["budget_eval"] = budget_eval
    budget = plan.get("budget") or {}
    party_total = max(1, structured_party_size(record))
    expected_attraction_budget = attraction_ticket_sum * party_total
    reported_attraction_budget = _safe_int(budget.get("total_attractions"))
    reported_meal_budget = _safe_int(budget.get("total_meals"))
    reported_transportation_budget = _safe_int(budget.get("total_transportation"))
    expected_meal_budget = meal_cost_sum * party_total
    budget_component_eval = {
        "party_total": party_total,
        "hotel_room_count": hotel_room_count(record),
        "attraction_ticket_sum": attraction_ticket_sum,
        "expected_total_attractions": expected_attraction_budget,
        "reported_total_attractions": reported_attraction_budget,
        "meal_per_person_cost_sum": meal_cost_sum,
        "expected_total_meals": expected_meal_budget,
        "reported_total_meals": reported_meal_budget,
        "reported_total_transportation": reported_transportation_budget,
    }
    meal_scale_eval = meal_cost_scale_details(record, plan)
    budget_relationship_eval = budget_relationship_details(
        budget_eval=budget_eval,
        expected_attraction_budget=expected_attraction_budget,
        reported_attraction_budget=reported_attraction_budget,
        meal_scale_eval=meal_scale_eval,
    )
    recomputed_budget = recompute_budget_from_selected_items(record, plan, budget)
    recomputed_budget_eval = budget_alignment_details(record, recomputed_budget, plan)
    result["budget_component_eval"] = budget_component_eval
    result["meal_scale_eval"] = meal_scale_eval
    result["budget_relationship_eval"] = budget_relationship_eval
    result["recomputed_budget"] = recomputed_budget
    result["recomputed_budget_eval"] = recomputed_budget_eval
    metrics["budget_consistent"] = budget_eval["arithmetic_consistent"]
    metrics["budget_arithmetic_consistent"] = budget_eval["arithmetic_consistent"]
    metrics["attraction_budget_consistent"] = reported_attraction_budget == expected_attraction_budget
    metrics["meal_budget_consistent"] = reported_meal_budget == expected_meal_budget
    metrics["hotel_budget_relation_ok"] = budget_relationship_eval["hotel_budget_relation_ok"]
    metrics["attraction_budget_party_relation_ok"] = budget_relationship_eval["attraction_budget_party_relation_ok"]
    metrics["meal_cost_scale_ok"] = meal_scale_eval["ok"]
    metrics["budget_relationship_ok"] = budget_relationship_eval["budget_relationship_ok"]
    metrics["transportation_budget_nonnegative"] = reported_transportation_budget >= 0
    metrics["budget_within_user_budget"] = budget_eval["within_user_budget"]
    metrics["budget_user_constraint_ok"] = budget_eval["user_constraint_ok"]
    metrics["budget_level_aligned"] = budget_eval["level_aligned"]
    metrics["budget_preference_aligned"] = budget_eval["preference_aligned"]
    metrics["hotel_budget_covers_nights"] = budget_eval["hotel_budget_covers_nights"]
    metrics["recomputed_budget_total"] = recomputed_budget_eval["total"]
    metrics["recomputed_budget_per_person_day"] = recomputed_budget_eval["per_person_day"]
    metrics["recomputed_budget_within_user_budget"] = recomputed_budget_eval["within_user_budget"]
    metrics["recomputed_budget_user_constraint_ok"] = recomputed_budget_eval["user_constraint_ok"]
    metrics["recomputed_budget_level_aligned"] = recomputed_budget_eval["level_aligned"]
    metrics["recomputed_budget_preference_aligned"] = recomputed_budget_eval["preference_aligned"]
    metrics["recomputed_budget_hard_ok"] = recomputed_budget_eval["user_constraint_ok"]
    metrics["recomputed_budget_fit_ok"] = recomputed_budget_eval["preference_aligned"]
    metrics["budget_selection_ok"] = recomputed_budget_eval["preference_aligned"]

    weather_match = True
    context_weather = {item.get("date"): item for item in context_snapshot(record).get("trip_weather") or []}
    plan_weather = {item.get("date"): item for item in plan.get("weather_info") or []}
    weather_diffs = []
    for date_text in expected_dates:
        context_row = context_weather.get(date_text)
        plan_row = plan_weather.get(date_text)
        if not context_row or not plan_row:
            weather_match = False
            weather_diffs.append({"date": date_text, "issue": "missing_weather_row"})
            continue
        for key in WEATHER_KEYS:
            if normalize_weather_value(key, context_row.get(key)) != normalize_weather_value(key, plan_row.get(key)):
                weather_match = False
                weather_diffs.append({"date": date_text, "field": key, "expected": context_row.get(key), "got": plan_row.get(key)})
    metrics["weather_match"] = weather_match

    sft_hard_keys = [
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
        "budget_arithmetic_consistent",
        "attraction_budget_consistent",
        "meal_budget_consistent",
        "transportation_budget_nonnegative",
        "budget_user_constraint_ok",
        "hotel_budget_covers_nights",
        "weather_match",
    ]
    dpo_soft_keys = [
        "attraction_diversity_ok",
        "meal_diversity_ok",
        "budget_preference_aligned",
    ]
    dpo_soft_recomputed_budget_keys = [
        "attraction_diversity_ok",
        "meal_diversity_ok",
        "recomputed_budget_fit_ok",
    ]
    planner_soft_keys = [
        "attraction_diversity_ok",
        "meal_diversity_ok",
        "meal_cost_scale_ok",
        "recomputed_budget_user_constraint_ok",
        "recomputed_budget_fit_ok",
    ]
    budget_sum_hard_excluded_keys = {
        # Reported budget ledger math is diagnostic for now. Production can
        # recompute these deterministic fields from selected POIs and party.
        "budget_arithmetic_consistent",
        "attraction_budget_consistent",
        "meal_budget_consistent",
        "hotel_budget_covers_nights",
        "budget_user_constraint_ok",
    }
    sft_no_budget_sum_hard_keys = [
        key for key in sft_hard_keys if key not in budget_sum_hard_excluded_keys
    ]
    metrics["sft_strict_hard_pass"] = all(metrics.get(key) for key in sft_hard_keys)
    metrics["sft_no_budget_sum_hard_pass"] = all(metrics.get(key) for key in sft_no_budget_sum_hard_keys)
    metrics["sft_hard_pass"] = metrics["sft_no_budget_sum_hard_pass"]
    metrics["dpo_soft_pass"] = metrics["sft_hard_pass"] and all(metrics.get(key) for key in dpo_soft_keys)
    metrics["dpo_soft_recomputed_budget_pass"] = metrics["sft_hard_pass"] and all(
        metrics.get(key) for key in dpo_soft_recomputed_budget_keys
    )
    metrics["planner_soft_pass"] = metrics["sft_hard_pass"] and all(metrics.get(key) for key in planner_soft_keys)
    semantic_budget_hard_keys = [
        key
        for key in sft_hard_keys
        if key not in {"budget_arithmetic_consistent", "attraction_budget_consistent", "meal_budget_consistent"}
    ] + [
        "budget_relationship_ok",
    ]
    metrics["sft_budget_semantic_hard_pass"] = all(metrics.get(key) for key in semantic_budget_hard_keys)
    # 从 planner 后续评估开始，hard_pass 默认指 SFT 可训练/可过滤的硬约束；
    # 餐饮多样性、预算偏好等质量项进入 dpo_soft_pass。
    metrics["hard_pass"] = metrics["sft_hard_pass"]

    if too_many_attractions:
        result["errors"].append({"stage": "rule", "type": "too_many_attractions", "details": too_many_attractions})
    if repeated_attractions:
        result["errors"].append({"stage": "rule", "type": "attraction_repeat_too_many", "details": repeated_attractions[:10]})
    if accommodation_mismatches:
        result["errors"].append({"stage": "rule", "type": "accommodation_type_mismatch", "details": accommodation_mismatches[:10]})
    if middle_hotel_null:
        result["errors"].append({"stage": "rule", "type": "middle_hotel_null", "details": middle_hotel_null})
    if placeholder_hotel_distances:
        result["errors"].append({"stage": "rule", "type": "hotel_distance_placeholder", "details": placeholder_hotel_distances[:10]})
    if placeholder_meals:
        result["errors"].append({"stage": "rule", "type": "meal_placeholder", "details": placeholder_meals[:10]})
    if invalid_meals:
        result["errors"].append({"stage": "rule", "type": "meal_invalid_name", "details": invalid_meals[:10]})
    elif ungrounded_meals:
        result["errors"].append({"stage": "rule", "type": "meal_grounding_miss", "details": ungrounded_meals[:10]})
    if same_day_repeated_meals:
        result["errors"].append({"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": same_day_repeated_meals[:10]})
    if repeated_meals:
        result["errors"].append({"stage": "rule", "type": "meal_repeat_too_many", "details": repeated_meals[:10]})
    if not budget_eval["hotel_budget_covers_nights"]:
        result["errors"].append(
            {
                "stage": "rule",
                "type": "hotel_budget_underestimated",
                "details": budget_eval["hotel_budget"],
            }
        )
    if weather_diffs:
        result["errors"].append({"stage": "rule", "type": "weather_mismatch", "details": weather_diffs[:5]})
    if not budget_eval["arithmetic_consistent"]:
        result["errors"].append({"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": budget_eval})
    if reported_attraction_budget != expected_attraction_budget:
        result["errors"].append({"stage": "rule", "type": "attraction_budget_inconsistent", "details": budget_component_eval})
    if reported_meal_budget != expected_meal_budget:
        result["errors"].append({"stage": "rule", "type": "meal_budget_inconsistent", "details": budget_component_eval})
    if reported_transportation_budget < 0:
        result["errors"].append({"stage": "rule", "type": "transportation_budget_negative", "details": budget_component_eval})
    if not budget_relationship_eval["budget_relationship_ok"]:
        result["errors"].append({"stage": "rule", "type": "budget_relationship_mismatch", "details": budget_relationship_eval})
    if not meal_scale_eval["ok"]:
        result["errors"].append({"stage": "rule", "type": "meal_cost_scale_too_low", "details": meal_scale_eval})
    if not budget_eval["user_constraint_ok"]:
        result["errors"].append({"stage": "rule", "type": "budget_hard_constraint_exceeded", "details": budget_eval})
    if not budget_eval["preference_aligned"]:
        result["errors"].append({"stage": "rule", "type": "budget_preference_mismatch", "details": budget_eval})

    return result


def recompute_budget_from_selected_items(
    record: dict[str, Any],
    plan: dict[str, Any],
    reported_budget: dict[str, Any] | None,
) -> dict[str, int]:
    """按模型已选 item 的分项价格重算预算。

    这里不信模型输出的 budget.total 和各类乘法结果，只使用：
    - hotel.estimated_cost: 单间每晚价
    - attraction.ticket_price: 单人票价
    - meal.estimated_cost: 人均单餐价
    - budget.total_transportation: 本地交通整体估算
    """
    party_total = max(1, structured_party_size(record))
    room_count = hotel_room_count(record)
    total_hotels = 0
    total_attractions = 0
    total_meals = 0
    for day in plan.get("days") or []:
        hotel = day.get("hotel")
        if isinstance(hotel, dict):
            total_hotels += max(0, _safe_int(hotel.get("estimated_cost"))) * room_count
        for attraction in day.get("attractions") or []:
            if isinstance(attraction, dict):
                total_attractions += max(0, _safe_int(attraction.get("ticket_price"))) * party_total
        for meal in day.get("meals") or []:
            if isinstance(meal, dict):
                total_meals += max(0, _safe_int(meal.get("estimated_cost"))) * party_total

    total_transportation = max(0, _safe_int((reported_budget or {}).get("total_transportation")))
    total = total_attractions + total_hotels + total_meals + total_transportation
    return {
        "total_attractions": total_attractions,
        "total_hotels": total_hotels,
        "total_meals": total_meals,
        "total_transportation": total_transportation,
        "total": total,
    }


def _invalid_hotel_name(name: str) -> bool:
    from app.planner.output import is_invalid_hotel_name

    return is_invalid_hotel_name(name)


def _safe_int(value: Any) -> int:
    try:
        return int(value or 0)
    except Exception:  # noqa: BLE001
        return 0


def _ratio_close(reported: int, expected: int, low: float = 0.75, high: float = 1.35) -> bool:
    """判断预算分项是否大致体现了正确口径，而不是要求精确加总。"""
    if expected <= 0:
        return reported == 0
    return expected * low <= reported <= expected * high


def budget_relationship_details(
    *,
    budget_eval: dict[str, Any],
    expected_attraction_budget: int,
    reported_attraction_budget: int,
    meal_scale_eval: dict[str, Any],
) -> dict[str, Any]:
    """检查预算是否体现天数/人数关系，而不是检查所有分项精确加和。"""
    hotel_budget = budget_eval.get("hotel_budget") or {}
    expected_hotels = _safe_int(hotel_budget.get("expected_min_total_hotels"))
    reported_hotels = _safe_int(hotel_budget.get("reported_total_hotels"))
    hotel_ok = _ratio_close(reported_hotels, expected_hotels, low=0.8, high=1.25)
    attraction_ok = _ratio_close(reported_attraction_budget, expected_attraction_budget, low=0.8, high=1.25)
    ok = hotel_ok and attraction_ok and bool(meal_scale_eval.get("ok"))
    return {
        "hotel_budget_relation_ok": hotel_ok,
        "attraction_budget_party_relation_ok": attraction_ok,
        "meal_cost_scale_ok": bool(meal_scale_eval.get("ok")),
        "budget_relationship_ok": ok,
        "expected_total_hotels": expected_hotels,
        "reported_total_hotels": reported_hotels,
        "expected_total_attractions": expected_attraction_budget,
        "reported_total_attractions": reported_attraction_budget,
        "meal_scale_eval": meal_scale_eval,
    }


def meal_cost_scale_details(record: dict[str, Any], plan: dict[str, Any]) -> dict[str, Any]:
    """检查餐饮人均费用是否体现预算档位。

    新口径下 meal.estimated_cost 是“人均单餐费用”，不是整组费用。早餐价格受
    城市、品类、酒店权益影响太大，不参与该尺度检查。

    这个指标只约束 premium/luxury：高预算不是不能吃当地小吃，而是整趟午晚餐
    不能全部低价。低价的正餐型当地小吃/夜市/大排档可以作为例外，但至少一半
    午晚餐仍需达到该预算档位的人均价格尺度。甜品、咖啡、奶茶等轻食饮品不作为
    lunch/dinner 的低价例外。
    """
    party_total = max(1, structured_party_size(record))
    constraint = (record.get("request") or {}).get("budget_constraint") or {}
    control = record.get("control_spec") or {}
    budget_level = str(constraint.get("budget_level") or control.get("budget_level") or "standard")
    floor_by_level = {
        "premium": 70,
        "luxury": 100,
    }
    per_person_floor = floor_by_level.get(budget_level, 0)
    failures = []
    low_cost_exceptions = []
    floor_hit_count = 0
    meal_count = 0
    checked_count = 0
    for day in plan.get("days") or []:
        for meal in day.get("meals") or []:
            meal_count += 1
            meal_name = str(meal.get("name") or "")
            meal_type = str(meal.get("type") or "").lower()
            cost = _safe_int(meal.get("estimated_cost"))
            if meal_type not in {"lunch", "dinner"}:
                continue
            checked_count += 1
            if per_person_floor <= 0:
                continue
            if cost >= per_person_floor:
                floor_hit_count += 1
                continue
            if is_local_snack_meal(meal_name):
                low_cost_exceptions.append(
                    {
                        "date": day.get("date"),
                        "type": meal.get("type"),
                        "name": meal_name,
                        "estimated_cost": cost,
                        "min_expected_cost": per_person_floor,
                    }
                )
                continue
            failures.append(
                {
                    "date": day.get("date"),
                    "type": meal.get("type"),
                    "name": meal_name,
                    "estimated_cost": cost,
                    "min_expected_cost": per_person_floor,
                    "reason": "low_cost_non_local_snack",
                }
            )
    required_floor_hits = (checked_count + 1) // 2 if per_person_floor > 0 else 0
    enough_floor_hits = per_person_floor <= 0 or floor_hit_count >= required_floor_hits
    if per_person_floor > 0 and checked_count > 0 and not enough_floor_hits:
        failures.append(
            {
                "reason": "not_enough_full_scale_meals",
                "floor_hit_count": floor_hit_count,
                "required_floor_hits": required_floor_hits,
                "checked_count": checked_count,
                "low_cost_exception_count": len(low_cost_exceptions),
            }
        )
    return {
        "ok": not failures,
        "party_total": party_total,
        "budget_level": budget_level,
        "per_person_lunch_dinner_floor": per_person_floor,
        "breakfast_policy": "excluded_from_meal_cost_scale",
        "enforced_levels": sorted(floor_by_level),
        "local_snack_policy": "low-cost local snacks/night markets are allowed, but at least half of premium/luxury lunch/dinner meals must meet the floor",
        "meal_count": meal_count,
        "checked_count": checked_count,
        "floor_hit_count": floor_hit_count,
        "required_floor_hits": required_floor_hits,
        "low_cost_exception_count": len(low_cost_exceptions),
        "low_cost_exceptions": low_cost_exceptions[:20],
        "failure_count": len(failures),
        "failures": failures[:20],
    }


LOCAL_SNACK_MEAL_MARKERS = [
    "小吃",
    "名小吃",
    "老字号",
    "地道",
    "本地",
    "风味",
    "苍蝇馆",
    "面馆",
    "拉面",
    "牛肉面",
    "刀削面",
    "热干面",
    "烩面",
    "臊子面",
    "炸酱面",
    "小面",
    "拌面",
    "炒面",
    "汤面",
    "海鲜面",
    "莜面",
    "饸饹面",
    "粉店",
    "米粉",
    "螺蛳粉",
    "牛肉粉",
    "羊肉粉",
    "粉馆",
    "肠粉",
    "河粉",
    "米线",
    "过桥米线",
    "酸辣粉",
    "馄饨",
    "云吞",
    "抄手",
    "饺子",
    "水饺",
    "小笼包",
    "生煎",
    "锅贴",
    "包子",
    "烧饼",
    "锅盔",
    "肉夹馍",
    "煎饼",
    "凉皮",
    "凉面",
    "砂锅",
    "麻辣烫",
    "冒菜",
    "串串",
    "炸串",
    "卤味",
    "卤煮",
    "鸭血粉丝",
    "粥",
    "粿条",
    "饵丝",
    "饵块",
    "豆花",
    "大排档",
    "排档",
]
LOCAL_SNACK_SCENE_MARKERS = [
    "夜市",
    "美食街",
    "小吃街",
    "老街",
    "古城",
    "步行街",
    "市集",
    "集市",
    "早市",
    "菜市场",
    "农贸市场",
    "档口",
    "摊",
]
LIGHT_MEAL_MARKERS = [
    "甜品",
    "糖水",
    "糕点",
    "点心",
    "奶茶",
    "茶饮",
    "咖啡",
    "冰粉",
    "饮品",
    "面包",
    "蛋糕",
    "下午茶",
    "饼屋",
    "鲜花饼",
]


def is_local_snack_meal(name: str) -> bool:
    """判断低价 lunch/dinner 是否像数据里的当地小吃或夜市/摊档体验。"""
    text = str(name or "").strip()
    if not text:
        return False
    if any(marker in text for marker in LIGHT_MEAL_MARKERS):
        return False
    return any(marker in text for marker in LOCAL_SNACK_MEAL_MARKERS) or any(
        marker in text for marker in LOCAL_SNACK_SCENE_MARKERS
    )


MEAL_EMPTY_NAMES = {"", "无", "无安排", "不安排", "无需", "暂无"}
MEAL_LODGING_MARKERS = ["酒店", "宾馆", "旅馆", "民宿", "客栈", "旅舍", "公寓", "住宿"]
MEAL_LODGING_GENERIC = ["酒店晚餐", "酒店午餐", "民宿晚餐", "民宿午餐", "客栈晚餐", "客栈午餐", "酒店餐厅"]
MEAL_NON_FOOD_MARKERS = [
    "电子游艺",
    "游艺厅",
    "电玩城",
    "博物馆",
    "博物院",
    "美术馆",
    "艺术馆",
    "科技馆",
    "纪念馆",
    "公园",
    "景区",
    "景点",
    "风景区",
    "商场",
    "购物中心",
    "培训",
    "学校",
]
MEAL_FOOD_SEMANTIC_MARKERS = [
    "小吃",
    "夜市",
    "美食",
    "餐厅",
    "饭店",
    "酒家",
    "茶社",
    "茶楼",
    "面馆",
    "粉店",
    "米粉",
    "火锅",
    "烧烤",
    "烤肉",
    "咖啡",
    "甜品",
    "菜馆",
    "食堂",
    "食府",
    "厨房",
    "私房菜",
    "大排档",
    "水饺",
    "饺子",
    "包子",
    "馄饨",
    "凉皮",
    "泡馍",
]


def meal_semantic_validity(name: str, meal_type: str, hotel_candidates: list[str]) -> dict[str, Any]:
    """判断未命中 food_pois 的 meal.name 是否仍是可接受的餐饮语义 fallback。"""
    text = str(name or "").strip()
    if text in MEAL_EMPTY_NAMES:
        return {"valid": False, "reason": "empty_or_none"}
    if meal_type in {"lunch", "dinner"} and any(marker in text for marker in MEAL_LODGING_GENERIC):
        return {"valid": False, "reason": "generic_lodging_meal"}
    if name_in_candidates(text, hotel_candidates) or any(marker in text for marker in MEAL_LODGING_MARKERS):
        return {"valid": False, "reason": "hotel_or_lodging_name"}
    if any(marker in text for marker in MEAL_NON_FOOD_MARKERS):
        return {"valid": False, "reason": "non_food_poi_name"}
    if any(marker in text for marker in MEAL_FOOD_SEMANTIC_MARKERS):
        return {"valid": True, "reason": "food_semantic_fallback"}
    return {"valid": False, "reason": "unknown_food_semantics"}


def meal_diversity_key(name: str) -> str:
    """餐饮多样性去重 key。

    分店名不应让同一品牌看起来像不同餐厅，例如
    “方砖厂69号炸酱面(崇文门店)”和“方砖厂69号炸酱面(王府井喜悦店)”
    在多样性上都按“方砖厂69号炸酱面”统计。
    """
    text = str(name or "").strip()
    if not text:
        return ""
    for marker in ("(", "（"):
        if marker in text:
            text = text.split(marker, 1)[0]
    return "".join(text.split()).lower()


def attraction_diversity_key(name: str) -> str:
    """景点多样性去重 key。

    先使用保守规则，只判断同一个景点名是否被跨天/多次重复安排；
    不按景点类别做强制多样化，避免误伤历史文化游、博物馆游等垂直偏好。
    """
    text = str(name or "").strip()
    if not text:
        return ""
    for marker in ("(", "（"):
        if marker in text:
            text = text.split(marker, 1)[0]
    return "".join(text.split()).lower()


def summarize_results(results: list[dict[str, Any]]) -> dict[str, Any]:
    """汇总规则评估结果。"""
    total = len(results)
    metric_keys = set()
    for row in results:
        metric_keys.update(row.get("metrics", {}).keys())

    boolean_summary = {}
    numeric_values: dict[str, list[float]] = {}
    for key in sorted(metric_keys):
        values = [row.get("metrics", {}).get(key) for row in results if key in row.get("metrics", {})]
        if values and all(isinstance(value, bool) for value in values):
            boolean_summary[key] = {
                "pass": sum(1 for value in values if value),
                "total": len(values),
                "rate": metric_rate(sum(1 for value in values if value), len(values)),
            }
        elif values and all(isinstance(value, (int, float)) for value in values):
            numeric_values[key] = [float(value) for value in values]

    failure_stages = Counter()
    error_types = Counter()
    latencies = []
    output_chars = []
    for row in results:
        if row.get("latency_seconds") is not None:
            latencies.append(float(row["latency_seconds"]))
        if row.get("output_chars") is not None:
            output_chars.append(float(row["output_chars"]))
        for error in row.get("errors") or []:
            failure_stages[error.get("stage", "unknown")] += 1
            error_types[error.get("type") or error.get("stage", "unknown")] += 1

    numeric_summary = {
        key: {
            "avg": average(values),
            "p50": percentile(values, 0.5),
            "p90": percentile(values, 0.9),
        }
        for key, values in numeric_values.items()
    }
    return {
        "total": total,
        "boolean_metrics": boolean_summary,
        "numeric_metrics": numeric_summary,
        "latency": {
            "avg": average(latencies),
            "p50": percentile(latencies, 0.5),
            "p90": percentile(latencies, 0.9),
            "p99": percentile(latencies, 0.99),
        },
        "output_chars": {
            "avg": average(output_chars),
            "p50": percentile(output_chars, 0.5),
            "p90": percentile(output_chars, 0.9),
        },
        "failure_stages": counter_to_dict(failure_stages),
        "error_types": counter_to_dict(error_types),
    }


def write_markdown(path: Path, report: dict[str, Any], results: list[dict[str, Any]]) -> None:
    """写规则评估 Markdown 报告。"""
    lines = [
        f"# Rule Eval Report: {report['model_name']}\n\n",
        f"- records: {report['summary']['total']}\n",
        f"- generations: `{report['generations_path']}`\n",
        f"- records_path: `{report['records_path']}`\n\n",
        "## Boolean Metrics\n\n",
        "| Metric | Pass | Total | Rate |\n",
        "| --- | ---: | ---: | ---: |\n",
    ]
    for key, item in report["summary"]["boolean_metrics"].items():
        lines.append(f"| {key} | {item['pass']} | {item['total']} | {item['rate']:.2%} |\n")

    lines.extend(["\n## Numeric Metrics\n\n", "```json\n", json.dumps(report["summary"]["numeric_metrics"], ensure_ascii=False, indent=2), "\n```\n"])
    lines.extend(["\n## Failure Types\n\n", "```json\n", json.dumps(report["summary"]["error_types"], ensure_ascii=False, indent=2), "\n```\n"])
    lines.append("\n## Failure Examples\n\n")
    failures = [row for row in results if row.get("errors")]
    for row in failures[:20]:
        lines.append(f"### {row['record_id']}\n")
        lines.append(f"- request: {row['request_summary']}\n")
        lines.append(f"- errors: `{json.dumps(row['errors'][:3], ensure_ascii=False)}`\n\n")

    path.write_text("".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="评估 Planner 生成结果。")
    parser.add_argument("--records", type=Path, default=DEFAULT_EVAL_RECORDS)
    parser.add_argument("--generations", type=Path, default=None)
    parser.add_argument("--model-name", required=True)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_EVAL_OUTPUT_DIR)
    parser.add_argument("--use-reference-output", action="store_true", help="用 records_eval 里的 teacher output 做规则评估 smoke")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    records_by_id = load_records_by_id(args.records)
    run_dir = args.output_dir / args.model_name
    generations_path = args.generations or (run_dir / "generations.jsonl")

    if args.use_reference_output:
        generations = [
            {
                "record_id": record_id,
                "ok": True,
                "output": record["output"],
                "output_chars": len(record["output"]),
                "latency_seconds": 0,
            }
            for record_id, record in records_by_id.items()
        ]
    else:
        raw_generations = read_jsonl(generations_path)
        generations_by_id = {}
        for generation in raw_generations:
            record_id = generation.get("record_id")
            if record_id:
                # eval_generate 在 --resume 时会重试失败样本，因此同一个 record_id
                # 可能有旧失败行和新成功行。规则评估只看最后一次生成结果。
                generations_by_id[record_id] = generation
        generations = list(generations_by_id.values())

    results = []
    for generation in generations:
        record = records_by_id.get(generation.get("record_id"))
        if not record:
            continue
        results.append(evaluate_output(record, generation))

    summary = summarize_results(results)
    report = {
        "model_name": args.model_name,
        "records_path": str(args.records),
        "generations_path": str(generations_path),
        "raw_generations": 0 if args.use_reference_output else len(raw_generations),
        "unique_generations": len(generations),
        "summary": summary,
        "results": results,
    }
    run_dir.mkdir(parents=True, exist_ok=True)
    report_json = run_dir / "rule_eval_report.json"
    report_md = run_dir / "rule_eval_report.md"
    write_json(report_json, report)
    write_markdown(report_md, report, results)
    print(f"rule report: {report_json}")
    print(f"rule markdown: {report_md}")
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
