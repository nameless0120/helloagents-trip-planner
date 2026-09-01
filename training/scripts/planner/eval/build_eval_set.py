"""构建评估集。

评估集只冻结输入侧内容：

- 模拟用户请求
- PlannerContext 工具快照
- 压缩后的 PlannerContext
- 线上同款 Planner prompt

它不调用 Planner 模型生成 TripPlan。后续评估 base/SFT/DPO 时，
都使用同一批 frozen prompt，避免把请求分布和工具快照变化混进模型对比里。
"""

from __future__ import annotations

import argparse
import json
import math
import os
import random
import sys
import time
from collections import Counter
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parents[4]
SCRIPTS_DIR = PROJECT_ROOT / "training" / "scripts"
EVAL_SCRIPTS_DIR = Path(__file__).resolve().parent
DATA_SCRIPTS_DIR = SCRIPTS_DIR / "planner" / "data"
BACKEND_DIR = PROJECT_ROOT / "backend"
sys.path[:0] = [
    str(EVAL_SCRIPTS_DIR),
    str(DATA_SCRIPTS_DIR),
    str(SCRIPTS_DIR),
    str(BACKEND_DIR),
]

from shared.common import DATA_DIR, load_project_env, read_jsonl, write_json  # noqa: E402
from generate_sft_data import (  # noqa: E402
    PLANNER_AGENT_PROMPT,
    append_jsonl,
    apply_budget_fit_policy,
    build_budget_constraint,
    build_party_info,
    build_one_request,
    build_planner_query,
    date_bucket,
    format_request_id,
    get_worker_context_builder,
    infer_city_tier,
    normalize_request,
    record_control_spec,
    summarize_requests,
    validate_request_date_mode,
)


DEFAULT_OUTPUT_DIR = DATA_DIR / "planner" / "eval"

EVAL_PERSON_DAY_BUDGETS = {
    "limited": [220, 270, 320],
    "standard": [380, 470, 560],
    "comfortable": [600, 750, 900],
    "premium": [950, 1200, 1450],
}

EVAL_HOTEL_COST_BY_ACCOMMODATION = {
    "经济型酒店": 300,
    "民宿": 420,
    "舒适型酒店": 520,
    "亲子酒店": 650,
    "高端酒店": 1000,
}

EVAL_SHARED_TRANSPORT_DAY_COST = {
    "公共交通": 80,
    "地铁+步行": 60,
    "打车": 220,
    "自驾": 260,
}

EVAL_CITY_BUDGET_FACTORS = {
    "long_tail": 0.95,
    "popular": 1.05,
    "major": 1.15,
}

HARD_PROFILES = [
    {
        "companion_type": "family_with_children",
        "travel_days": 4,
        "transportation": "打车",
        "accommodation": "亲子酒店",
        "budget_level": "standard",
        "budget_strictness": "hard",
        "preferences": ["亲子", "博物馆", "城市公园", "本地美食"],
        "diet": "无",
        "avoid": ["过长步行", "太偏远的景点", "高价餐厅"],
        "free_text": "带6岁小朋友出行，预算要控制住，午后不要太累，尽量避开过长步行、太偏远景点和高价餐厅。",
    },
    {
        "companion_type": "family_with_elders",
        "travel_days": 5,
        "transportation": "公共交通",
        "accommodation": "舒适型酒店",
        "budget_level": "comfortable",
        "budget_strictness": "soft",
        "preferences": ["历史文化", "公园", "老人友好", "本地美食"],
        "diet": "清淡饮食",
        "avoid": ["爬山", "长时间排队", "过长步行"],
        "free_text": "带父母慢慢玩，餐饮清淡一点，尽量避开爬山、长时间排队和过长步行，预算可以略有弹性但不要乱花。",
    },
    {
        "companion_type": "friends",
        "travel_days": 4,
        "transportation": "地铁+步行",
        "accommodation": "经济型酒店",
        "budget_level": "limited",
        "budget_strictness": "hard",
        "preferences": ["美食", "历史文化", "城市漫步"],
        "diet": "海鲜过敏",
        "avoid": ["海鲜餐厅", "购物团", "太偏远的景点"],
        "free_text": "几个朋友穷游，对海鲜过敏，总预算不能超，想吃本地特色但不要安排海鲜餐厅、购物团和太偏远的景点。",
    },
    {
        "companion_type": "couple",
        "travel_days": 4,
        "transportation": "打车",
        "accommodation": "高端酒店",
        "budget_level": "premium",
        "budget_strictness": "soft",
        "preferences": ["艺术", "特色餐厅", "城市地标", "休闲慢游"],
        "diet": "无",
        "avoid": ["购物团", "打卡式景点"],
        "free_text": "两个人预算比较充足，希望住得舒服、餐饮有品质，不要为了省钱做成低配方案，也避开购物团和打卡式景点。",
    },
    {
        "companion_type": "solo",
        "travel_days": 5,
        "transportation": "公共交通",
        "accommodation": "民宿",
        "budget_level": "standard",
        "budget_strictness": "hard",
        "preferences": ["自然风光", "摄影", "城市漫步", "本地美食"],
        "diet": "少辣",
        "avoid": ["密集行程", "太偏远的景点"],
        "free_text": "一个人旅行，喜欢拍照和城市漫步，少辣，预算需要控制，路线不要太密集，也尽量别去太偏远的景点。",
    },
    {
        "companion_type": "business",
        "travel_days": 3,
        "transportation": "打车",
        "accommodation": "舒适型酒店",
        "budget_level": "comfortable",
        "budget_strictness": "hard",
        "preferences": ["城市地标", "特色餐厅", "自由活动多"],
        "diet": "无",
        "avoid": ["过长步行", "太早起"],
        "free_text": "出差顺便旅行，每天可玩的时间有限，不要太早起，不要安排过长步行，预算要贴合但不能超太多。",
    },
]

HARDER_PROFILES = [
    {
        "companion_type": "family_mixed",
        "party_override": {"adults": 2, "children": 1, "elders": 2, "total": 5, "companion_type": "family_mixed"},
        "travel_days": 5,
        "transportation": "打车",
        "accommodation": "舒适型酒店",
        "budget_level": "comfortable",
        "budget_strictness": "hard",
        "budget_amount_factor": 0.9,
        "preferences": ["亲子", "老人友好", "历史文化", "城市公园", "本地美食"],
        "diet": "清淡饮食",
        "avoid": ["爬山", "过长步行", "长时间排队", "高价餐厅"],
        "free_text": "三代同游，有老人也有小朋友，预算要控制住。路线要轻松，不要爬山、过长步行、长时间排队和高价餐厅；如果天气不好，优先室内或轻量活动。",
        "stress_type": "multi_party_constraint",
    },
    {
        "companion_type": "couple",
        "travel_days": 4,
        "transportation": "打车",
        "accommodation": "高端酒店",
        "budget_level": "premium",
        "budget_strictness": "soft",
        "budget_amount_factor": 0.92,
        "preferences": ["高端酒店", "艺术", "特色餐厅", "城市地标", "休闲慢游"],
        "diet": "无",
        "avoid": ["购物团", "打卡式景点", "过度省钱"],
        "free_text": "两个人想住好一点、吃得有品质，但也不想乱花钱。不要做成低配穷游方案，也避开购物团和打卡式景点。",
        "stress_type": "premium_budget_quality",
    },
    {
        "companion_type": "friends",
        "party_override": {"adults": 4, "children": 0, "elders": 0, "total": 4, "companion_type": "friends"},
        "travel_days": 4,
        "transportation": "地铁+步行",
        "accommodation": "经济型酒店",
        "budget_level": "limited",
        "budget_strictness": "hard",
        "budget_amount_factor": 0.86,
        "preferences": ["美食", "夜市", "老字号", "城市漫步"],
        "diet": "海鲜过敏",
        "avoid": ["海鲜餐厅", "购物团", "太偏远的景点", "高价餐厅"],
        "free_text": "四个朋友穷游，其中有人海鲜过敏。想吃本地特色和夜市，但不能安排海鲜餐厅、购物团、太偏远景点和高价餐厅，总预算不要超。",
        "stress_type": "limited_diet_budget",
    },
    {
        "companion_type": "family_with_elders",
        "travel_days": 5,
        "transportation": "公共交通",
        "accommodation": "舒适型酒店",
        "budget_level": "standard",
        "budget_strictness": "hard",
        "budget_amount_factor": 0.9,
        "preferences": ["自然风光", "历史文化", "公园", "本地美食"],
        "diet": "少辣",
        "avoid": ["爬山", "过长步行", "太早起", "太偏远的景点"],
        "free_text": "带父母旅行，喜欢自然和历史，但父母不能爬山，少辣，不要太早起，也不要安排过长步行或太偏远景点。预算比较紧，需要稳住。",
        "stress_type": "elder_nature_conflict",
    },
    {
        "companion_type": "business",
        "party_override": {"adults": 1, "children": 0, "elders": 0, "total": 1, "companion_type": "business"},
        "travel_days": 3,
        "transportation": "打车",
        "accommodation": "舒适型酒店",
        "budget_level": "comfortable",
        "budget_strictness": "hard",
        "budget_amount_factor": 0.85,
        "preferences": ["城市地标", "特色餐厅", "自由活动多", "博物馆"],
        "diet": "无",
        "avoid": ["太早起", "过长步行", "密集行程"],
        "free_text": "出差顺便玩，每天只有半天左右可安排，不能太早起、不能行程太密，也不要过长步行。预算要贴合，不要乱超。",
        "stress_type": "business_time_budget",
    },
    {
        "companion_type": "solo",
        "travel_days": 5,
        "transportation": "公共交通",
        "accommodation": "民宿",
        "budget_level": "standard",
        "budget_strictness": "hard",
        "budget_amount_factor": 0.88,
        "preferences": ["摄影", "自然风光", "城市漫步", "本地菜"],
        "diet": "无",
        "avoid": ["密集行程", "太偏远的景点", "商业化打卡点"],
        "free_text": "一个人拍照旅行，喜欢自然风光和城市漫步，但不要密集赶景点，不要太偏远，也尽量避开商业化打卡点；预算要控制。",
        "stress_type": "solo_route_preference",
    },
    {
        "companion_type": "family_with_children",
        "travel_days": 4,
        "transportation": "自驾",
        "accommodation": "亲子酒店",
        "budget_level": "standard",
        "budget_strictness": "hard",
        "budget_amount_factor": 0.9,
        "preferences": ["亲子", "动物园", "海洋馆", "城市公园", "本地美食"],
        "diet": "无",
        "avoid": ["夜生活", "太晚返程", "过长步行", "排队太久"],
        "free_text": "带5岁孩子自驾，想安排亲子体验，但不要夜生活、太晚返程、过长步行或排队太久。预算是硬约束。",
        "stress_type": "child_queue_budget",
    },
    {
        "companion_type": "couple",
        "travel_days": 5,
        "transportation": "公共交通",
        "accommodation": "民宿",
        "budget_level": "comfortable",
        "budget_strictness": "soft",
        "budget_amount_factor": 1.0,
        "preferences": ["小众展馆", "咖啡", "艺术", "城市漫步", "特色餐厅"],
        "diet": "无",
        "avoid": ["过度商业化景点", "跟团游", "购物团"],
        "free_text": "两个人想要小众、有审美的路线，喜欢展馆、咖啡和特色餐厅，但避开过度商业化景点、跟团游和购物团。预算不需要极省，要符合舒适体验。",
        "stress_type": "soft_preference_quality",
    },
    {
        "companion_type": "friends",
        "party_override": {"adults": 3, "children": 0, "elders": 0, "total": 3, "companion_type": "friends"},
        "travel_days": 3,
        "transportation": "打车",
        "accommodation": "高端酒店",
        "budget_level": "comfortable",
        "budget_strictness": "hard",
        "budget_amount_factor": 0.82,
        "preferences": ["城市地标", "美食", "夜景", "购物"],
        "diet": "不吃猪肉",
        "avoid": ["猪肉餐厅", "太偏远的景点", "低配住宿"],
        "free_text": "三个朋友短途旅行，想住得好一点、吃点好的，但有人不吃猪肉。不要猪肉餐厅、太偏远景点和低配住宿，总预算不能超。",
        "stress_type": "comfort_high_hotel_budget_conflict",
    },
    {
        "companion_type": "family_with_elders",
        "travel_days": 4,
        "transportation": "打车",
        "accommodation": "亲子酒店",
        "budget_level": "comfortable",
        "budget_strictness": "soft",
        "budget_amount_factor": 0.95,
        "preferences": ["亲子", "老人友好", "博物馆", "城市公园", "特色餐厅"],
        "diet": "清淡饮食",
        "avoid": ["爬山", "夜间长距离移动", "排队太久", "重口味餐厅"],
        "free_text": "老人和小朋友一起出行，要求清淡饮食，路线要照顾体力。不要爬山、夜间长距离移动、排队太久和重口味餐厅。",
        "stress_type": "elder_child_mixed_soft",
    },
]


def format_eval_id(index: int, prefix: str) -> str:
    """生成 eval record_id。"""
    return f"{prefix}_{index:06d}"


def tool_counts(planner_context: dict[str, Any]) -> dict[str, int]:
    """统计 PlannerContext 中各类工具候选数量。"""
    snapshot = planner_context.get("tool_snapshot") or {}
    return {
        "classic_pois": len(snapshot.get("classic_pois") or []),
        "preference_pois": len(snapshot.get("preference_pois") or []),
        "scenic_pois": len(snapshot.get("scenic_pois") or []),
        "experience_pois": len(snapshot.get("experience_pois") or []),
        "hotel_pois": len(snapshot.get("hotel_pois") or []),
        "food_pois": len(snapshot.get("food_pois") or []),
        "food_query_groups": len(snapshot.get("food_query_groups") or []),
        "route_hints": len(snapshot.get("route_hints") or snapshot.get("route_summary") or []),
        "trip_weather": len(snapshot.get("trip_weather") or []),
    }


def weather_provider(planner_context: dict[str, Any]) -> str:
    """从工具状态中标记天气来源。"""
    weather_status = (planner_context.get("tool_snapshot") or {}).get("tool_status", {}).get("weather", {})
    message = str(weather_status.get("message", ""))
    if "open_meteo_archive" in message:
        return "open_meteo_archive"
    return "amap_or_unknown"


def make_eval_request(index: int, args: argparse.Namespace) -> dict[str, Any]:
    """复用 SFT 请求生成逻辑，但使用 eval 专属 record_id。"""
    raw_request = dict(build_one_request(index, args))
    if args.difficulty in {"hard", "harder"}:
        raw_request = harden_request(raw_request, index, args)
    else:
        raw_request = rebalance_eval_budget(raw_request, index, args)
    raw_request["request_id"] = format_eval_id(index, args.id_prefix)
    raw_request.setdefault("source", args.request_source)
    if args.difficulty in {"hard", "harder"}:
        raw_request["source"] = f"{raw_request['source']}_{args.difficulty}_eval"
    raw_request["eval_source_index"] = format_request_id(index)
    return raw_request


def choose_eval_budget_amount(
    rng: random.Random,
    budget_level: str,
    party_total: int,
    travel_days: int,
    accommodation: str,
    transportation: str,
    city_tier: str,
) -> int:
    """按典型旅游预算报告的新口径生成 eval 整趟预算。

    餐饮/门票/体验等非住宿个人消费按人数线性增长；住宿按两人一间；
    打车/自驾等市内交通按队伍共享估算，避免把所有非住宿费用都套
    `group_discount` 压低。
    """
    level = "premium" if budget_level == "luxury" else budget_level
    per_person_day = rng.choice(EVAL_PERSON_DAY_BUDGETS.get(level, EVAL_PERSON_DAY_BUDGETS["standard"]))
    party_total = max(int(party_total), 1)
    travel_days = max(int(travel_days), 1)
    lodging_nights = max(travel_days - 1, 0)
    room_count = max(1, math.ceil(party_total / 2))
    lodging_per_night = EVAL_HOTEL_COST_BY_ACCOMMODATION.get(accommodation, 520)
    shared_transport_day = EVAL_SHARED_TRANSPORT_DAY_COST.get(transportation, 120)
    city_factor = EVAL_CITY_BUDGET_FACTORS.get(city_tier, 1.05)

    lodging_total = lodging_per_night * lodging_nights * room_count
    person_total = per_person_day * party_total * travel_days
    shared_transport_total = shared_transport_day * travel_days
    raw_total = (lodging_total + person_total + shared_transport_total) * city_factor
    return max(500, int(round(raw_total / 100.0) * 100))


def rebalance_eval_budget(
    raw_request: dict[str, Any],
    index: int,
    args: argparse.Namespace,
    budget_amount_factor: float = 1.0,
) -> dict[str, Any]:
    """按典型旅游预算报告重算 eval 用户“整趟总预算”。"""
    item = dict(raw_request)
    spec = dict(item.get("control_spec") or {})
    budget_constraint = dict(item.get("budget_constraint") or {})
    original_amount = int(budget_constraint.get("amount") or 0)
    original_level = str(budget_constraint.get("budget_level") or spec.get("budget_level") or "standard")
    budget_level = "premium" if original_level == "luxury" else original_level
    party = item.get("party") or {}
    city_tier = spec.get("city_tier") or infer_city_tier(str(item.get("city") or ""))
    rng = random.Random(args.seed * 2017 + index)
    amount = choose_eval_budget_amount(
        rng,
        budget_level,
        int(party.get("total") or 1),
        int(item.get("travel_days") or 1),
        str(item.get("accommodation") or "舒适型酒店"),
        str(item.get("transportation") or "公共交通"),
        str(city_tier),
    )
    amount = max(500, int(round(amount * budget_amount_factor / 100.0) * 100))

    budget_constraint["amount"] = amount
    budget_constraint["budget_level"] = budget_level
    item["budget_constraint"] = budget_constraint
    item["free_text_input"] = replace_budget_amount_text(
        str(item.get("free_text_input") or ""), original_amount, amount
    )

    spec.update(
        {
            "budget_level": budget_level,
            "budget_amount": amount,
            "eval_budget_party_mode": "linear_person_shared_transport",
            "eval_budget_policy_version": "realistic_budget_v1",
        }
    )
    if original_level == "luxury":
        spec["eval_budget_level_rebased_from"] = original_level
    item["control_spec"] = spec
    return item


def replace_budget_amount_text(text: str, original_amount: int, new_amount: int) -> str:
    """替换自由文本中的预算金额；hard profile 通常没有显式金额。"""
    if original_amount > 0 and f"{original_amount}元" in text:
        return text.replace(f"{original_amount}元", f"{new_amount}元")
    return text


def harden_request(raw_request: dict[str, Any], index: int, args: argparse.Namespace) -> dict[str, Any]:
    """把普通受控请求改造成 hard eval 请求。

    hard eval 不是制造不合理需求，而是集中放大真实业务中更容易拉开模型差异的点：
    多人、多天、预算贴合、负向约束、饮食禁忌、老人/亲子/商务时间约束。
    """
    rng = random.Random(args.seed * 1009 + index)
    profiles = HARDER_PROFILES if args.difficulty == "harder" else HARD_PROFILES
    profile = profiles[index % len(profiles)]
    item = dict(raw_request)
    spec = dict(item.get("control_spec") or {})

    companion_type = profile["companion_type"]
    travel_days = int(profile["travel_days"])
    accommodation = str(profile["accommodation"])
    transportation = str(profile["transportation"])
    budget_level = str(profile["budget_level"])
    city_tier = spec.get("city_tier") or infer_city_tier(str(item.get("city") or ""))

    party = dict(profile.get("party_override") or build_party_info(rng, companion_type))
    amount = choose_eval_budget_amount(
        rng,
        budget_level,
        int(party.get("total") or 1),
        travel_days,
        accommodation,
        transportation,
        city_tier,
    )
    amount = max(500, int(round(amount * float(profile.get("budget_amount_factor", 1.0)) / 100.0) * 100))
    budget_constraint = build_budget_constraint(rng, budget_level, amount)
    budget_constraint["strictness"] = profile["budget_strictness"]

    item["travel_days"] = travel_days
    item["transportation"] = transportation
    item["accommodation"] = accommodation
    item["preferences"] = list(profile["preferences"])
    item["free_text_input"] = str(profile["free_text"])
    item["party"] = party
    item["budget_constraint"] = budget_constraint
    item = rebalance_eval_budget(item, index, args, float(profile.get("budget_amount_factor", 1.0)))
    budget_constraint = item["budget_constraint"]
    budget_level = str(budget_constraint.get("budget_level") or budget_level)
    amount = int(budget_constraint.get("amount") or amount)
    spec = dict(item.get("control_spec") or spec)

    spec.update(
        {
            "companion_type": companion_type,
            "city_tier": city_tier,
            "budget_level": budget_level,
            "budget_amount": amount,
            "budget_strictness": budget_constraint["strictness"],
            "pace": "慢节奏" if "慢" in item["free_text_input"] else spec.get("pace", "适中节奏"),
            "diet": profile["diet"],
            "avoid": list(profile["avoid"]),
            "positive_preferences": list(profile["preferences"]),
            "negative_constraints": list(profile["avoid"]),
            "diet_positive": [] if profile["diet"] in {"无", "海鲜过敏"} else [profile["diet"]],
            "diet_avoid": ["海鲜"] if profile["diet"] == "海鲜过敏" else [],
            "traveler_constraints": {
                "needs_child_friendly": int(party.get("children") or 0) > 0,
                "needs_elder_friendly": int(party.get("elders") or 0) > 0,
                "avoid_long_walk": any(
                    value in profile["avoid"]
                    for value in ["过长步行", "爬山", "太累的路线", "密集行程"]
                ),
            },
            "difficulty": args.difficulty,
            "hard_profile": index % len(profiles),
            "stress_type": profile.get("stress_type", args.difficulty),
        }
    )
    item["control_spec"] = spec
    return item


def build_one_eval_record(index: int, args: argparse.Namespace, amap_api_key: str) -> dict[str, Any]:
    """构建一条 frozen eval 输入记录。"""
    raw_request = make_eval_request(index, args)
    request_id = raw_request["request_id"]
    request = normalize_request(raw_request, request_id)
    validate_request_date_mode(request, args.date_mode)

    builder = get_worker_context_builder(amap_api_key, args.historical_weather_provider)
    started_at = time.perf_counter()
    planner_context = builder.collect(request)
    apply_budget_fit_policy(planner_context, request)
    compact_context = builder.compact_for_planner(planner_context)
    planner_query = build_planner_query(builder, request, planner_context)
    control_spec = record_control_spec(raw_request, request, planner_context)
    elapsed = time.perf_counter() - started_at

    compact_context_text = json.dumps(compact_context, ensure_ascii=False)
    raw_context_text = json.dumps(planner_context, ensure_ascii=False)
    return {
        "record_id": request_id,
        "created_at": datetime.now(timezone.utc).isoformat(),
        "split": "eval",
        "request_source": raw_request.get("source", "unknown"),
        "eval_source_index": raw_request.get("eval_source_index"),
        "request": request.model_dump(),
        "control_spec": control_spec,
        "system_prompt": PLANNER_AGENT_PROMPT,
        "planner_query": planner_query,
        "compact_planner_context": compact_context,
        "planner_context": planner_context,
        "metadata": {
            "elapsed_seconds": round(elapsed, 3),
            "prompt_chars": len(planner_query),
            "compact_context_chars": len(compact_context_text),
            "raw_context_chars": len(raw_context_text),
            "weather_provider": weather_provider(planner_context),
            "date_bucket": date_bucket(request.model_dump()),
            "tool_counts": tool_counts(planner_context),
            "tool_status": (planner_context.get("tool_snapshot") or {}).get("tool_status", {}),
            "eval_metrics_version": "current",
            "expected_output_schema": "TripPlan",
        },
    }


def load_existing_ids(path: Path) -> set[str]:
    """读取已构建的 eval record_id。"""
    if not path.exists():
        return set()
    return {str(row.get("record_id") or "") for row in read_jsonl(path)}


def write_request_row(path: Path, record: dict[str, Any]) -> None:
    """单独落一份轻量 requests.jsonl，方便抽样审计分布。"""
    row = dict(record["request"])
    row["request_id"] = record["record_id"]
    row["control_spec"] = record.get("control_spec") or {}
    row["request_source"] = record.get("request_source")
    row["date_bucket"] = record.get("metadata", {}).get("date_bucket")
    append_jsonl(path, row)


def summarize_records(records: list[dict[str, Any]], errors: list[dict[str, Any]]) -> dict[str, Any]:
    """生成评估集分布摘要。"""
    requests = []
    for record in records:
        item = dict(record.get("request") or {})
        item["control_spec"] = record.get("control_spec") or {}
        requests.append(item)

    metadata_rows = [record.get("metadata") or {} for record in records]
    tool_keys = [
        "classic_pois",
        "preference_pois",
        "scenic_pois",
        "experience_pois",
        "hotel_pois",
        "food_pois",
        "food_query_groups",
        "route_hints",
        "trip_weather",
    ]
    return {
        "count": len(records),
        "failed": len(errors),
        "request_distribution": summarize_requests(requests),
        "weather_provider": dict(Counter(row.get("weather_provider", "unknown") for row in metadata_rows)),
        "difficulty": dict(
            Counter((record.get("control_spec") or {}).get("difficulty", "standard") for record in records)
        ),
        "avg_elapsed_seconds": round(sum(row.get("elapsed_seconds", 0) for row in metadata_rows) / len(metadata_rows), 3)
        if metadata_rows
        else 0,
        "avg_prompt_chars": int(sum(row.get("prompt_chars", 0) for row in metadata_rows) / len(metadata_rows))
        if metadata_rows
        else 0,
        "avg_compact_context_chars": int(
            sum(row.get("compact_context_chars", 0) for row in metadata_rows) / len(metadata_rows)
        )
        if metadata_rows
        else 0,
        "avg_raw_context_chars": int(sum(row.get("raw_context_chars", 0) for row in metadata_rows) / len(metadata_rows))
        if metadata_rows
        else 0,
        "tool_counts_avg": {
            key: round(
                sum((row.get("tool_counts") or {}).get(key, 0) for row in metadata_rows) / len(metadata_rows),
                2,
            )
            if metadata_rows
            else 0
            for key in tool_keys
        },
        "first_errors": errors[:10],
    }


def write_summary_markdown(path: Path, summary: dict[str, Any]) -> None:
    """写中文 Markdown 摘要。"""
    dist = summary.get("request_distribution") or {}
    lines = [
        "# 评估集摘要",
        "",
        f"- 样本数：{summary.get('count', 0)}",
        f"- 失败数：{summary.get('failed', 0)}",
        f"- 平均 prompt 字符数：{summary.get('avg_prompt_chars', 0)}",
        f"- 平均压缩上下文字符数：{summary.get('avg_compact_context_chars', 0)}",
        f"- 平均原始上下文字符数：{summary.get('avg_raw_context_chars', 0)}",
        f"- 平均构建耗时：{summary.get('avg_elapsed_seconds', 0)}s",
        "",
        "## 请求分布",
        "",
    ]
    for key in [
        "companion_type",
        "city_tier",
        "date_bucket",
        "travel_days",
        "transportation",
        "accommodation",
        "budget_level",
        "pace",
        "diet",
    ]:
        lines.append(f"### {key}")
        lines.append("")
        values = dist.get(key) or {}
        if values:
            for name, count in values.items():
                lines.append(f"- {name}: {count}")
        else:
            lines.append("- 无")
        lines.append("")

    lines.extend(
        [
            "## 工具候选均值",
            "",
        ]
    )
    for name, value in (summary.get("tool_counts_avg") or {}).items():
        lines.append(f"- {name}: {value}")

    lines.extend(["", "## 天气来源", ""])
    for name, count in (summary.get("weather_provider") or {}).items():
        lines.append(f"- {name}: {count}")

    lines.extend(["", "## 难度分布", ""])
    for name, count in (summary.get("difficulty") or {}).items():
        lines.append(f"- {name}: {count}")

    if summary.get("first_errors"):
        lines.extend(["", "## 前 10 个错误", ""])
        for item in summary["first_errors"]:
            lines.append(f"- {item.get('record_id')}: {item.get('error_type')} - {item.get('error')}")

    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="构建 frozen 评估集")
    parser.add_argument("--count", type=int, default=200, help="本轮构建的样本数")
    parser.add_argument("--start-index", type=int, default=0)
    parser.add_argument("--seed", type=int, default=20260429)
    parser.add_argument("--id-prefix", default="standard200_eval")
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument("--request-source", choices=["template", "llm", "controlled"], default="controlled")
    parser.add_argument("--date-mode", choices=["future", "mixed", "past"], default="mixed")
    parser.add_argument(
        "--difficulty",
        choices=["standard", "hard", "harder"],
        default="standard",
        help="hard/harder 会放大多人、多天、预算、负向约束、天气和路线压力样本占比",
    )
    parser.add_argument("--request-batch-size", type=int, default=20)
    parser.add_argument("--request-max-tokens", type=int, default=8000)
    parser.add_argument("--request-generation-retries", type=int, default=3)
    parser.add_argument("--disable-template-request-fallback", action="store_true")
    parser.add_argument("--workers", type=int, default=2)
    parser.add_argument(
        "--historical-weather-provider",
        choices=["open-meteo", "none"],
        default="open-meteo",
    )
    parser.add_argument("--resume", action="store_true")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    load_project_env()
    amap_api_key = os.getenv("AMAP_MAPS_API_KEY") or os.getenv("AMAP_API_KEY")
    if not amap_api_key:
        raise RuntimeError("缺少 AMAP_MAPS_API_KEY 或 AMAP_API_KEY")

    output_dir: Path = args.output_dir
    records_path = output_dir / "records.jsonl"
    requests_path = output_dir / "requests.jsonl"
    errors_path = output_dir / "errors.jsonl"
    summary_json_path = output_dir / "summary.json"
    summary_md_path = output_dir / "评估集摘要.md"

    existing_ids = load_existing_ids(records_path) if args.resume else set()
    indices = [
        args.start_index + offset
        for offset in range(args.count)
        if format_eval_id(args.start_index + offset, args.id_prefix) not in existing_ids
    ]
    if not indices:
        print("没有需要构建的新评估样本。")
        return

    print(
        f"开始构建评估集: count={len(indices)}, workers={args.workers}, "
        f"request_source={args.request_source}, date_mode={args.date_mode}",
        flush=True,
    )

    ok = 0
    failed = 0
    errors: list[dict[str, Any]] = []

    if args.workers <= 1:
        for progress_index, index in enumerate(indices, start=1):
            try:
                record = build_one_eval_record(index, args, amap_api_key)
                append_jsonl(records_path, record)
                write_request_row(requests_path, record)
                ok += 1
                print(f"progress: {progress_index}/{len(indices)} ok={ok} failed={failed} last={record['record_id']}", flush=True)
            except Exception as exc:  # noqa: BLE001
                failed += 1
                error = {
                    "created_at": datetime.now(timezone.utc).isoformat(),
                    "record_id": format_eval_id(index, args.id_prefix),
                    "error_type": type(exc).__name__,
                    "error": str(exc),
                }
                errors.append(error)
                append_jsonl(errors_path, error)
                print(f"progress: {progress_index}/{len(indices)} ok={ok} failed={failed} error={exc}", flush=True)
    else:
        with ThreadPoolExecutor(max_workers=max(1, args.workers)) as executor:
            futures = {executor.submit(build_one_eval_record, index, args, amap_api_key): index for index in indices}
            for progress_index, future in enumerate(as_completed(futures), start=1):
                index = futures[future]
                try:
                    record = future.result()
                    append_jsonl(records_path, record)
                    write_request_row(requests_path, record)
                    ok += 1
                    print(
                        f"progress: {progress_index}/{len(indices)} ok={ok} failed={failed} last={record['record_id']}",
                        flush=True,
                    )
                except Exception as exc:  # noqa: BLE001
                    failed += 1
                    error = {
                        "created_at": datetime.now(timezone.utc).isoformat(),
                        "record_id": format_eval_id(index, args.id_prefix),
                        "error_type": type(exc).__name__,
                        "error": str(exc),
                    }
                    errors.append(error)
                    append_jsonl(errors_path, error)
                    print(f"progress: {progress_index}/{len(indices)} ok={ok} failed={failed} error={exc}", flush=True)

    errors_path.parent.mkdir(parents=True, exist_ok=True)
    errors_path.touch(exist_ok=True)
    all_records = read_jsonl(records_path)
    all_errors = read_jsonl(errors_path)
    summary = summarize_records(all_records, all_errors)
    write_json(summary_json_path, summary)
    write_summary_markdown(summary_md_path, summary)

    print(f"完成: 本轮成功={ok}, 本轮失败={failed}, 累计评估样本={len(all_records)}")
    print(f"records: {records_path}")
    print(f"requests: {requests_path}")
    print(f"errors: {errors_path}")
    print(f"summary: {summary_md_path}")


if __name__ == "__main__":
    main()
