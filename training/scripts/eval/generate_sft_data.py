"""生成 legacy SFT 数据。

注意：这是 legacy 兼容脚本，仅用于旧版 SFT/DPO/eval 流程复现，不是当前 SFT 主线入口。
新数据请使用 `training/scripts/planner/data/generate_sft_data.py`。

示例:

1. 先用模板请求做小规模 smoke，不调用强模型生成用户请求:

   cd helloagents-trip-planner
   .venv-training-py311/bin/python3 training/scripts/eval/generate_sft_data.py \
     --count 5 \
     --request-source template \
     --workers 1

2. 正式用强模型模拟真实用户请求，再用强模型蒸馏 TripPlan:

   .venv-training-py311/bin/python3 training/scripts/eval/generate_sft_data.py \
     --count 100 \
     --request-source llm \
     --request-batch-size 20 \
     --workers 4 \
     --resume

输出:

- training/data/legacy/sft/records.jsonl: 完整可审计记录，包含 request、PlannerContext、prompt 和 TripPlan。
- training/data/legacy/sft/errors.jsonl: 失败样本，不进入训练集。
- training/data/llamafactory/trip_legacy_sft_train.json
- training/data/llamafactory/trip_legacy_sft_val.json
"""

from __future__ import annotations

import argparse
import json
import os
import random
import sys
import threading
import time
from collections import Counter
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parents[3]
SCRIPTS_DIR = PROJECT_ROOT / "training" / "scripts"
BACKEND_DIR = PROJECT_ROOT / "backend"
sys.path.insert(0, str(SCRIPTS_DIR))
sys.path.insert(0, str(BACKEND_DIR))

from shared.common import DATA_DIR, LLAMAFACTORY_DIR, load_project_env, read_jsonl, split_train_val, write_json
from shared.llm_client import DataGenLLM


from app.planner.context import PlannerContextBuilder  # noqa: E402
from app.planner.output import validate_trip_plan_shape  # noqa: E402
from app.agents.prompts import PLANNER_AGENT_PROMPT  # noqa: E402
from app.models.schemas import TripPlan, TripRequest  # noqa: E402
from historical_weather import fetch_historical_trip_weather, is_past_trip  # noqa: E402


LEGACY_SFT_DIR = DATA_DIR / "legacy" / "sft"
RAW_RECORDS_PATH = LEGACY_SFT_DIR / "records.jsonl"
ERRORS_PATH = LEGACY_SFT_DIR / "errors.jsonl"
REQUESTS_PATH = LEGACY_SFT_DIR / "requests.jsonl"
LLAMAFACTORY_TRAIN_PATH = LLAMAFACTORY_DIR / "trip_legacy_sft_train.json"
LLAMAFACTORY_VAL_PATH = LLAMAFACTORY_DIR / "trip_legacy_sft_val.json"
DATASET_INFO_PATH = LLAMAFACTORY_DIR / "dataset_info.json"

DEFAULT_CITIES = [
    "北京",
    "上海",
    "广州",
    "深圳",
    "杭州",
    "成都",
    "重庆",
    "西安",
    "南京",
    "苏州",
    "厦门",
    "青岛",
    "长沙",
    "武汉",
    "昆明",
    "大理",
    "丽江",
    "桂林",
    "三亚",
    "哈尔滨",
]

SCENARIOS = [
    {
        "preferences": ["历史文化", "博物馆", "本地美食"],
        "avoid": ["网红排队店", "过度商业化景点"],
        "free_text": "想慢慢看展和逛老街，不想每天赶太多点。",
    },
    {
        "preferences": ["自然风光", "轻徒步", "摄影"],
        "avoid": ["大型商场", "纯购物行程"],
        "free_text": "希望路线别太累，日落和适合拍照的地方可以多一些。",
    },
    {
        "preferences": ["亲子", "动物园", "城市公园"],
        "avoid": ["夜生活", "过长步行"],
        "free_text": "带一个6岁小朋友，午后最好安排轻松一点，餐厅要适合孩子。",
    },
    {
        "preferences": ["艺术", "展览", "咖啡"],
        "avoid": ["跟团游", "打卡式景点"],
        "free_text": "喜欢城市漫步和小众展馆，住宿希望交通方便。",
    },
    {
        "preferences": ["美食", "夜市", "老字号"],
        "avoid": ["高价餐厅", "景区快餐"],
        "free_text": "主要想吃当地特色，预算别太夸张，晚上可以安排夜市。",
    },
    {
        "preferences": ["老人友好", "历史文化", "公园"],
        "avoid": ["爬山", "长时间排队"],
        "free_text": "带父母出行，节奏要慢，景点之间尽量少折腾。",
    },
    {
        "preferences": ["海滨", "休闲", "海鲜"],
        "avoid": ["太早起", "密集行程"],
        "free_text": "想住得舒服一点，上午可以晚点出门，海边散步要安排上。",
    },
    {
        "preferences": ["城市地标", "购物", "特色餐厅"],
        "avoid": ["太偏远的景点"],
        "free_text": "第一次去这个城市，希望经典一点，也想留一些自由活动时间。",
    },
    {
        "preferences": ["清真", "历史街区", "城市公园"],
        "avoid": ["猪肉", "酒吧"],
        "free_text": "有清真饮食要求，餐饮安排一定要注意。",
    },
    {
        "preferences": ["自然风光", "本地菜", "休闲"],
        "avoid": ["海鲜"],
        "free_text": "对海鲜过敏，不要安排海鲜餐厅，整体轻松一点。",
    },
]

ACCOMMODATION_BY_BUDGET = {
    "economy": ("经济型酒店", 350),
    "comfortable": ("舒适型酒店", 800),
    "premium": ("高端酒店", 1800),
}
TRANSPORTATION_OPTIONS = ["公共交通", "打车", "自驾", "地铁+步行"]

CITY_TIERS = {
    "major": ["北京", "上海", "广州", "深圳", "成都", "杭州", "重庆", "西安"],
    "popular": ["南京", "苏州", "厦门", "青岛", "长沙", "武汉", "昆明", "大理", "丽江", "桂林", "三亚", "哈尔滨"],
    "long_tail": ["珠海", "福州", "泉州", "天津", "洛阳", "扬州", "贵阳", "呼和浩特", "沈阳", "大连", "宁波", "济南", "郑州", "黄山", "张家界"],
}

COMPANION_WEIGHTS = [
    ("family_child", 30),
    ("friends", 24),
    ("couple", 18),
    ("solo", 15),
    ("family_elder", 8),
    ("unspecified", 5),
]

CITY_TIER_WEIGHTS = [("major", 35), ("popular", 40), ("long_tail", 25)]
DATE_MODE_WEIGHTS = [("past", 30), ("near_future", 30), ("far_future", 40)]
TRAVEL_DAYS_WEIGHTS = [(2, 18), (3, 42), (4, 28), (5, 12)]
BUDGET_WEIGHTS = [("limited", 28), ("medium", 48), ("upper", 18), ("luxury", 6)]
PACE_WEIGHTS = [("适中节奏", 45), ("慢节奏", 35), ("紧凑高效", 12), ("自由活动多", 8)]

# 真实用户表达预算时通常不会给 14674 这种精确数字。legacy DPO 阶段
# 先统一成“总预算”语义，但底层仍按人均每天粗档位推导总额。
PER_PERSON_DAY_BUDGETS = {
    "limited": [200, 300],
    "medium": [400, 500],
    "upper": [800, 1000],
    "luxury": [1200, 1500, 2000],
}

THEME_POOL = [
    ("美食", 38),
    ("历史文化", 28),
    ("博物馆", 18),
    ("自然风光", 25),
    ("城市公园", 16),
    ("休闲慢游", 30),
    ("城市地标", 22),
    ("第一次来", 18),
    ("摄影", 15),
    ("城市漫步", 15),
    ("购物商圈", 10),
    ("主题乐园", 10),
    ("户外轻徒步", 8),
    ("夜市夜景", 8),
    ("小众展览", 7),
    ("艺术", 7),
    ("海滨度假", 6),
]

DIET_WEIGHTS = [
    ("无", 70),
    ("少辣", 10),
    ("海鲜过敏", 5),
    ("清真", 4),
    ("素食", 4),
    ("清淡饮食", 7),
]


_thread_local = threading.local()
_write_lock = threading.Lock()


class DataGenPlannerContextBuilder(PlannerContextBuilder):
    """训练数据专用 PlannerContextBuilder。

    线上系统不需要历史天气；这里仅在过去完整行程时绕开高德天气，
    直接使用 Open-Meteo Archive，避免浪费高德天气接口额度。
    """

    def __init__(self, amap_api_key: str, historical_weather_provider: str):
        super().__init__(amap_api_key)
        self.historical_weather_provider = historical_weather_provider

    def _collect_weather_snapshot(self, request: TripRequest) -> dict[str, Any]:
        if self.historical_weather_provider == "open-meteo" and is_past_trip(request):
            rows = fetch_historical_trip_weather(request)
            if rows:
                return {
                    "tool_snapshot": {
                        "available_weather": rows,
                        "trip_weather": rows,
                    },
                    "status": self._tool_status(
                        True,
                        f"open_meteo_archive={len(rows)}, covered_trip_days={len(rows)}/{request.travel_days}",
                    ),
                }
        return super()._collect_weather_snapshot(request)


def append_jsonl(path: Path, row: dict[str, Any]) -> None:
    """线程安全追加 JSONL。"""
    path.parent.mkdir(parents=True, exist_ok=True)
    with _write_lock:
        with path.open("a", encoding="utf-8") as f:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")


def get_worker_llm() -> DataGenLLM:
    """每个线程懒加载一个 LLM client，避免共享客户端状态。"""
    if not hasattr(_thread_local, "llm"):
        _thread_local.llm = DataGenLLM()
    return _thread_local.llm


def get_worker_context_builder(amap_api_key: str, historical_weather_provider: str) -> PlannerContextBuilder:
    """每个线程懒加载一个 PlannerContextBuilder。"""
    builder_key = f"{amap_api_key}:{historical_weather_provider}"
    if getattr(_thread_local, "context_builder_key", None) != builder_key:
        _thread_local.context_builder = DataGenPlannerContextBuilder(
            amap_api_key,
            historical_weather_provider,
        )
        _thread_local.context_builder_key = builder_key
    return _thread_local.context_builder


def build_planner_query(builder: PlannerContextBuilder, request: TripRequest, planner_context: dict[str, Any]) -> str:
    """构造与线上 Planner 一致的用户输入。

    这里刻意镜像 `MultiAgentTripPlanner._build_planner_query()`。
    后续如果线上 prompt 协议变化，legacy 数据生成脚本也要同步更新。
    """
    prompt_context = builder.compact_for_planner(planner_context)
    context_json = json.dumps(prompt_context, ensure_ascii=False, indent=2)
    query = f"""请根据下面的 PlannerContext JSON 生成{request.city}的{request.travel_days}天旅行计划。

PlannerContext:
{context_json}

请严格遵守:
1. 只返回一个合法JSON对象，不要输出Markdown代码块、解释、前言、工具调用或<think>内容。
2. 顶层字段必须包含 city/start_date/end_date/days/weather_info/overall_suggestions/budget。
3. days长度必须等于 PlannerContext.request.travel_days，day_index从0开始，date必须逐日对应。
4. weather_info必须逐日对应 PlannerContext.tool_snapshot.trip_weather；远期天气不可用时保留“未知”，不要编造天气。
5. 景点优先使用 classic_pois、preference_pois、scenic_pois 和 experience_pois；酒店必须为null或使用hotel_pois里的真实酒店，不要把“无”“无住宿”“返程”“当天返程”写成hotel.name；餐饮优先使用对应候选，并沿用候选里的name/address/location。
6. 每天安排2-3个景点，每天必须包含breakfast/lunch/dinner三餐。
7. 预算要和住宿、餐饮、景点门票、交通方式大致一致，无法从工具获得价格时用合理估算并保持保守。
"""
    if request.free_text_input:
        query += f"\n额外要求: {request.free_text_input}"
    return query


def planner_max_output_tokens(request: TripRequest, args: argparse.Namespace) -> int:
    """按天数估算强模型输出上限。"""
    if args.max_output_tokens > 0:
        return args.max_output_tokens
    return min(args.output_base_tokens + request.travel_days * args.output_tokens_per_day, args.output_tokens_cap)


def build_legacy_party_info(rng: random.Random, companion_type: str) -> dict[str, Any]:
    """为 legacy 请求补齐当前 TripRequest 要求的同行人数结构。"""
    if companion_type == "solo":
        adults, children, elders = 1, 0, 0
    elif companion_type == "couple":
        adults, children, elders = 2, 0, 0
    elif companion_type == "friends":
        adults, children, elders = rng.choice([2, 3, 4]), 0, 0
    elif companion_type == "family_child":
        adults, children, elders = 2, rng.choice([1, 1, 2]), 0
    elif companion_type == "family_elder":
        adults, children, elders = rng.choice([1, 2]), 0, rng.choice([1, 2])
    else:
        adults, children, elders = rng.choice([1, 2, 3]), 0, 0
    return {
        "adults": adults,
        "children": children,
        "elders": elders,
        "total": adults + children + elders,
        "companion_type": companion_type,
    }


def choose_legacy_budget_amount(
    rng: random.Random,
    budget_level: str,
    party_total: int,
    travel_days: int,
) -> int:
    """按 legacy 预算档位生成整趟总预算，供旧请求兼容当前 schema。"""
    per_person_day = rng.choice(PER_PERSON_DAY_BUDGETS.get(budget_level, PER_PERSON_DAY_BUDGETS["medium"]))
    return per_person_day * max(party_total, 1) * max(travel_days, 1)


def build_legacy_budget_constraint(
    budget_level: str,
    amount: int,
) -> dict[str, Any]:
    return {
        "amount": amount,
        "scope": "total",
        "currency": "CNY",
        "budget_level": budget_level,
        "strictness": "soft",
    }


def normalize_request(data: dict[str, Any], request_id: str) -> TripRequest:
    """把 LLM/模板生成的请求规范成 TripRequest。"""
    item = dict(data)
    control_spec = dict(item.get("control_spec") or {})
    item["city"] = str(item.get("city") or "").strip()
    item["transportation"] = str(item.get("transportation") or "公共交通").strip()
    item["accommodation"] = str(item.get("accommodation") or "经济型酒店").strip()
    item["preferences"] = [str(v).strip() for v in item.get("preferences", []) if str(v).strip()][:5]
    item["free_text_input"] = str(item.get("free_text_input") or "").strip()

    travel_days = int(item.get("travel_days") or 3)
    travel_days = max(1, min(travel_days, 7))
    item["travel_days"] = travel_days

    if not item.get("start_date"):
        item["start_date"] = (date.today() + timedelta(days=14)).isoformat()
    start_date = date.fromisoformat(str(item["start_date"]))
    item["end_date"] = (start_date + timedelta(days=travel_days - 1)).isoformat()

    companion_type = str(control_spec.get("companion_type") or "unspecified")
    rng = random.Random(sum(ord(ch) for ch in request_id))
    if not item.get("party"):
        item["party"] = build_legacy_party_info(rng, companion_type)
    budget_level = str(control_spec.get("budget_level") or "medium")
    if budget_level not in PER_PERSON_DAY_BUDGETS:
        budget_level = "medium"
    if not item.get("budget_constraint"):
        amount = choose_legacy_budget_amount(rng, budget_level, int(item["party"].get("total") or 1), travel_days)
        item["budget_constraint"] = build_legacy_budget_constraint(budget_level, amount)

    request = TripRequest(**item)
    # request_id 不属于后端 schema，放在 metadata 里；这里仅用于错误提示。
    if not request.city:
        raise ValueError(f"{request_id} 缺少 city")
    return request


def choose_start_date(rng: random.Random, travel_days: int, date_mode: str) -> date:
    """按数据生成模式选择出发日期。"""
    if date_mode == "past":
        start_delta = -rng.choice([travel_days + 1, 7, 14, 30, 60, 90, 120, 180, 270, 365])
    elif date_mode == "mixed":
        start_delta = rng.choice([-180, -120, -90, -60, -30, -14, -7, -3, 1, 2, 3, 7, 14, 30, 60, 90, 120])
        if start_delta < 0 and start_delta + travel_days >= 0:
            start_delta = -(travel_days + 1)
    else:
        start_delta = rng.choice([1, 2, 3, 7, 14, 30, 60, 90, 120])
    return date.today() + timedelta(days=start_delta)


def request_date_instruction(date_mode: str) -> str:
    """给强模型的日期约束说明。"""
    if date_mode == "past":
        return "必须早于当前日期，并且整段行程必须已经结束；可以是过去1周到12个月内"
    if date_mode == "mixed":
        return "可以是过去1年内、未来几天或未来1-4个月；请混合历史行程、近期行程和远期行程"
    return "必须是当前日期之后，可以是近几天或未来1-4个月"


def validate_request_date_mode(request: TripRequest, date_mode: str) -> None:
    """确保 LLM 生成的日期符合本轮造数目标。"""
    start_date = date.fromisoformat(request.start_date)
    end_date = date.fromisoformat(request.end_date)
    today = date.today()
    if date_mode == "past" and end_date >= today:
        raise ValueError(f"date_mode=past要求行程已结束: {request.start_date}->{request.end_date}")
    if date_mode == "future" and start_date <= today:
        raise ValueError(f"date_mode=future要求未来出发: {request.start_date}")
    if date_mode == "mixed" and not (today - timedelta(days=366) <= start_date <= today + timedelta(days=180)):
        raise ValueError(f"date_mode=mixed日期超出范围: {request.start_date}")


def weighted_choice(rng: random.Random, weighted_items: list[tuple[Any, int]]) -> Any:
    """按整数权重抽样。"""
    total = sum(weight for _, weight in weighted_items)
    point = rng.uniform(0, total)
    upto = 0.0
    for item, weight in weighted_items:
        upto += weight
        if point <= upto:
            return item
    return weighted_items[-1][0]


def sample_many_weighted(
    rng: random.Random,
    weighted_items: list[tuple[str, int]],
    min_count: int,
    max_count: int,
) -> list[str]:
    """不放回地按权重抽多个主题。"""
    candidates = list(weighted_items)
    results = []
    target = rng.randint(min_count, max_count)
    while candidates and len(results) < target:
        item = weighted_choice(rng, candidates)
        results.append(item)
        candidates = [(name, weight) for name, weight in candidates if name != item]
    return results


def choose_controlled_start_date(rng: random.Random, travel_days: int, date_mode: str) -> date:
    """受控分布下的日期抽样，mixed会覆盖历史/近期/远期三类天气。"""
    if date_mode == "past":
        bucket = "past"
    elif date_mode == "future":
        bucket = weighted_choice(rng, [("near_future", 35), ("far_future", 65)])
    else:
        bucket = weighted_choice(rng, DATE_MODE_WEIGHTS)

    if bucket == "past":
        start_delta = -rng.choice([travel_days + 1, 7, 14, 30, 60, 90, 120, 180, 270, 365])
    elif bucket == "near_future":
        start_delta = rng.choice([1, 2, 3, 4])
    else:
        start_delta = rng.choice([30, 45, 60, 90, 120])
    return date.today() + timedelta(days=start_delta)


def choose_controlled_accommodation(rng: random.Random, companion_type: str, budget_level: str) -> str:
    """住宿分布由预算和同行类型共同决定。"""
    if companion_type == "family_child":
        weights = [("亲子酒店", 32), ("舒适型酒店", 36), ("经济型酒店", 20), ("民宿", 8), ("高端酒店", 4)]
    elif budget_level == "luxury":
        weights = [("高端酒店", 58), ("舒适型酒店", 32), ("民宿", 10)]
    elif budget_level == "limited":
        weights = [("经济型酒店", 62), ("舒适型酒店", 22), ("民宿", 16)]
    else:
        weights = [("舒适型酒店", 48), ("经济型酒店", 28), ("民宿", 16), ("高端酒店", 8)]
    return weighted_choice(rng, weights)


def choose_controlled_transportation(rng: random.Random, companion_type: str, city: str) -> str:
    """交通方式近似真实分布，并根据城市/同行类型微调。"""
    metro_cities = {"北京", "上海", "广州", "深圳", "成都", "杭州", "重庆", "南京", "苏州", "武汉", "西安"}
    if companion_type in {"family_child", "family_elder"}:
        weights = [("地铁+步行", 26), ("公共交通", 18), ("打车", 42), ("自驾", 14)]
    elif city in {"大理", "丽江", "桂林", "三亚", "张家界", "黄山"}:
        weights = [("地铁+步行", 12), ("公共交通", 22), ("打车", 34), ("自驾", 32)]
    elif city in metro_cities:
        weights = [("地铁+步行", 50), ("公共交通", 28), ("打车", 18), ("自驾", 4)]
    else:
        weights = [("地铁+步行", 34), ("公共交通", 30), ("打车", 24), ("自驾", 12)]
    return weighted_choice(rng, weights)


def choose_budget_text(
    rng: random.Random,
    budget_level: str,
    companion_type: str,
    travel_days: int,
    party_total: int | None = None,
    budget_amount: int | None = None,
) -> str:
    """生成自然语言预算描述。"""
    if party_total is None:
        party_total = build_legacy_party_info(rng, companion_type)["total"]
    total = budget_amount or choose_legacy_budget_amount(rng, budget_level, party_total, travel_days)
    # legacy DPO 阶段先统一训练“总预算”语义，避免人均/每日/总额混在一起。
    return f"总预算控制在{total}元左右"


def companion_phrase(rng: random.Random, companion_type: str) -> str:
    """同行类型转自然语气。"""
    if companion_type == "family_child":
        age = rng.choice([3, 4, 5, 6, 7, 8, 9, 10])
        return rng.choice([f"带{age}岁孩子", f"一家三口带{age}岁小朋友", f"带娃出行，孩子{age}岁"])
    if companion_type == "friends":
        return rng.choice(["和朋友一起", "几个朋友出行", "和同学/朋友一起"])
    if companion_type == "couple":
        return rng.choice(["情侣两个人", "和对象一起", "夫妻两个人"])
    if companion_type == "solo":
        return rng.choice(["一个人出行", "独自旅行", "单人自由行"])
    if companion_type == "family_elder":
        return rng.choice(["带父母出行", "陪长辈一起", "和爸妈一起"])
    return rng.choice(["这次想轻松玩几天", "第一次认真规划这个城市", "想安排一个舒服点的短途旅行"])


def build_controlled_free_text(
    rng: random.Random,
    companion_type: str,
    budget_level: str,
    travel_days: int,
    diet: str,
    pace: str,
    avoid: list[str],
    party_total: int | None = None,
    budget_amount: int | None = None,
) -> str:
    """不用强模型，直接生成足够自然的请求补充。"""
    parts = [
        companion_phrase(rng, companion_type),
        choose_budget_text(rng, budget_level, companion_type, travel_days, party_total, budget_amount),
    ]
    if pace == "慢节奏":
        parts.append("希望节奏慢一点，不要每天赶太多景点")
    elif pace == "紧凑高效":
        parts.append("可以紧凑一点，想多看几个经典地方")
    elif pace == "自由活动多":
        parts.append("希望每天留一点自由活动时间")
    else:
        parts.append("节奏适中就行")

    diet_text = {
        "少辣": "吃饭尽量少辣",
        "海鲜过敏": "对海鲜过敏，不要安排海鲜餐厅",
        "清真": "有清真饮食要求",
        "素食": "偏素食，餐饮请注意",
        "清淡饮食": "饮食希望清淡一些",
    }.get(diet)
    if diet_text:
        parts.append(diet_text)
    if avoid:
        parts.append(f"尽量避开{'、'.join(avoid)}")
    return "，".join(parts) + "。"


def generate_controlled_request(index: int, args: argparse.Namespace) -> dict[str, Any]:
    """按近似真实分布生成 TripRequest，不调用强模型。"""
    rng = random.Random(args.seed + index)
    companion_type = weighted_choice(rng, COMPANION_WEIGHTS)
    city_tier = weighted_choice(rng, CITY_TIER_WEIGHTS)
    city = rng.choice(CITY_TIERS[city_tier])
    travel_days = weighted_choice(rng, TRAVEL_DAYS_WEIGHTS)
    budget_level = weighted_choice(rng, BUDGET_WEIGHTS)
    pace = weighted_choice(rng, PACE_WEIGHTS)
    diet = weighted_choice(rng, DIET_WEIGHTS)
    accommodation = choose_controlled_accommodation(rng, companion_type, budget_level)
    transportation = choose_controlled_transportation(rng, companion_type, city)
    start = choose_controlled_start_date(rng, travel_days, args.date_mode)
    party = build_legacy_party_info(rng, companion_type)
    budget_amount = choose_legacy_budget_amount(rng, budget_level, party["total"], travel_days)

    themes = sample_many_weighted(rng, THEME_POOL, 2, 4)
    if companion_type == "family_child" and "亲子" not in themes:
        themes = ["亲子"] + themes[:3]
    if companion_type == "family_elder" and "老人友好" not in themes:
        themes = ["老人友好"] + themes[:3]
    if diet in {"清真", "素食"} and diet not in themes:
        themes = themes[:3] + [diet]

    avoid_pool = ["人挤人的网红店", "过度商业化景点", "太累的路线", "太偏远的景点", "高价餐厅", "购物团"]
    avoid = rng.sample(avoid_pool, k=rng.choice([1, 1, 2, 2, 3])) if rng.random() < 0.68 else []
    free_text = build_controlled_free_text(
        rng,
        companion_type,
        budget_level,
        travel_days,
        diet,
        pace,
        avoid,
        party_total=party["total"],
        budget_amount=budget_amount,
    )

    return {
        "request_id": f"legacy_request_{index:06d}",
        "city": city,
        "start_date": start.isoformat(),
        "end_date": (start + timedelta(days=travel_days - 1)).isoformat(),
        "travel_days": travel_days,
        "transportation": transportation,
        "accommodation": accommodation,
        "preferences": themes[:4],
        "free_text_input": free_text,
        "party": party,
        "budget_constraint": build_legacy_budget_constraint(budget_level, budget_amount),
        "source": "controlled",
        "control_spec": {
            "companion_type": companion_type,
            "city_tier": city_tier,
            "budget_level": budget_level,
            "pace": pace,
            "diet": diet,
            "avoid": avoid,
        },
    }


def generate_template_requests(
    count: int,
    start_index: int,
    seed: int,
    date_mode: str = "future",
) -> list[dict[str, Any]]:
    """用规则模板生成真实感 TripRequest。适合 smoke 和补充边界样本。"""
    rng = random.Random(seed)
    requests = []
    for offset in range(count):
        index = start_index + offset
        scenario = rng.choice(SCENARIOS)
        budget_key = rng.choice(list(ACCOMMODATION_BY_BUDGET))
        accommodation, daily_budget = ACCOMMODATION_BY_BUDGET[budget_key]
        travel_days = rng.choice([2, 3, 3, 4, 4, 5])
        start = choose_start_date(rng, travel_days, date_mode)
        prefs = list(scenario["preferences"])
        rng.shuffle(prefs)
        free_text = (
            f"{scenario['free_text']} 每日预算大概{daily_budget}元，"
            f"尽量避开：{'、'.join(scenario['avoid'])}。"
        )
        requests.append(
            {
                "request_id": f"legacy_request_{index:06d}",
                "city": rng.choice(DEFAULT_CITIES),
                "start_date": start.isoformat(),
                "end_date": (start + timedelta(days=travel_days - 1)).isoformat(),
                "travel_days": travel_days,
                "transportation": rng.choice(TRANSPORTATION_OPTIONS),
                "accommodation": accommodation,
                "preferences": prefs[: rng.choice([2, 3])],
                "free_text_input": free_text,
                "source": "template",
            }
        )
    return requests


def generate_llm_requests(
    count: int,
    start_index: int,
    batch_size: int,
    seed: int,
    max_tokens: int,
    retries: int,
    fallback_to_template: bool,
) -> list[dict[str, Any]]:
    """用强模型模拟真实用户 TripRequest。"""
    print(
        f"开始用强模型生成模拟用户请求: count={count}, batch_size={batch_size}",
        flush=True,
    )
    llm = DataGenLLM()
    rows: list[dict[str, Any]] = []
    current = start_index
    active_batch_size = batch_size
    while len(rows) < count:
        need = min(active_batch_size, count - len(rows))
        batch_no = len(rows) // max(active_batch_size, 1) + 1
        print(
            f"生成用户请求 batch {batch_no}: need={need}, start_id=legacy_request_{current:06d}",
            flush=True,
        )
        system_prompt = """你是旅行产品的真实用户请求模拟器。只能输出 JSON 数组，不要输出 Markdown。"""
        user_prompt = f"""请生成 {need} 条像真实用户填写的旅行规划请求。

当前日期: {date.today().isoformat()}
随机种子: {seed}
request_id 从 legacy_request_{current:06d} 开始递增。

每条必须包含:
- request_id: 字符串
- city: 中国旅游城市
- start_date: YYYY-MM-DD，必须是当前日期之后，混合近几天和未来1-4个月
- travel_days: 2到5天
- transportation: 公共交通/打车/自驾/地铁+步行 之一
- accommodation: 经济型酒店/舒适型酒店/高端酒店/民宿/亲子酒店 之一
- preferences: 2到4个中文偏好标签
- free_text_input: 一句真实口吻的额外要求，可以包含预算、同行人、饮食忌口、节奏、避雷项

要求:
1. 请求要像真实用户，不要像数据模板。
2. 需要覆盖亲子、老人、独行、情侣、朋友、预算有限、饮食忌口、过敏、休闲、特种兵、摄影、美食等场景。
3. end_date 可以省略，我会按 travel_days 自动计算。
4. 不要输出解释，只输出 JSON 数组。
"""
        batch_items: list[dict[str, Any]] = []
        last_error: Exception | None = None
        for attempt in range(1, retries + 1):
            try:
                result = llm.complete_json(system_prompt, user_prompt, temperature=0.8, max_tokens=max_tokens)
                if isinstance(result, dict):
                    result = result.get("requests") or result.get("data") or []
                if not isinstance(result, list):
                    raise ValueError(f"LLM 用户请求生成结果不是数组: {type(result).__name__}")
                batch_items = [dict(item) for item in result[:need]]
                if not batch_items:
                    raise ValueError("LLM 用户请求生成结果为空")
                break
            except Exception as exc:  # noqa: BLE001
                last_error = exc
                print(
                    f"⚠️  用户请求 batch {batch_no} 第 {attempt}/{retries} 次解析失败: {exc}",
                    flush=True,
                )

        if not batch_items:
            if active_batch_size > 5:
                active_batch_size = max(5, active_batch_size // 2)
                print(
                    f"⚠️  batch {batch_no} 多次失败，自动缩小 request_batch_size 到 {active_batch_size} 后重试",
                    flush=True,
                )
                continue

            if not fallback_to_template:
                raise RuntimeError(f"用户请求 batch {batch_no} 生成失败: {last_error}") from last_error

            print(
                f"⚠️  batch {batch_no} 多次失败，使用模板请求补齐 need={need}",
                flush=True,
            )
            batch_items = generate_template_requests(need, current, seed + current)

        batch_added = 0
        for item in batch_items:
            if len(rows) >= count:
                break
            request_id = f"legacy_request_{current:06d}"
            item = dict(item)
            item["request_id"] = request_id
            item["source"] = item.get("source") or "llm"
            rows.append(item)
            current += 1
            batch_added += 1
        print(
            f"用户请求 batch {batch_no} 完成: added={batch_added}, total={len(rows)}/{count}",
            flush=True,
        )
    return rows


def generate_llm_request(index: int, args: argparse.Namespace) -> dict[str, Any]:
    """用强模型生成单条真实感 TripRequest。

    正式数据生成采用单样本请求，而不是批量 JSON 数组。
    这样 32 个 worker 可以独立推进；某个 JSON 坏了只重试这个样本，
    不会让整批请求生成阶段失败。
    """
    request_id = f"legacy_request_{index:06d}"
    system_prompt = """你是旅行产品的真实用户请求模拟器。只能输出一个 JSON 对象，不要输出 Markdown。"""
    user_prompt = f"""请生成 1 条像真实用户填写的旅行规划请求。

当前日期: {date.today().isoformat()}
随机种子: {args.seed + index}
request_id 必须是: {request_id}

必须包含:
- request_id: "{request_id}"
- city: 中国旅游城市
- start_date: YYYY-MM-DD，{request_date_instruction(args.date_mode)}
- travel_days: 2到5天
- transportation: 公共交通/打车/自驾/地铁+步行 之一
- accommodation: 经济型酒店/舒适型酒店/高端酒店/民宿/亲子酒店 之一
- preferences: 2到4个中文偏好标签
- free_text_input: 一句真实口吻的额外要求，可以包含预算、同行人、饮食忌口、节奏、避雷项

要求:
1. 请求要像真实用户，不要像数据模板。
2. 覆盖亲子、老人、独行、情侣、朋友、预算有限、饮食忌口、过敏、休闲、特种兵、摄影、美食等不同场景。
3. end_date 可以省略，我会按 travel_days 自动计算。
4. 不要输出解释，只输出 JSON 对象。
"""
    llm = get_worker_llm()
    last_error: Exception | None = None
    for attempt in range(1, args.request_generation_retries + 1):
        try:
            result = llm.complete_json(
                system_prompt,
                user_prompt,
                temperature=0.8,
                max_tokens=args.request_max_tokens,
            )
            if isinstance(result, list):
                if not result:
                    raise ValueError("LLM 用户请求生成结果为空数组")
                result = result[0]
            if not isinstance(result, dict):
                raise ValueError(f"LLM 用户请求生成结果不是对象: {type(result).__name__}")
            result = dict(result)
            result["request_id"] = request_id
            result["source"] = "llm"
            # 这里提前跑一次 schema 规范化，尽早发现脏请求。
            request = normalize_request(result, request_id)
            validate_request_date_mode(request, args.date_mode)
            return result
        except Exception as exc:  # noqa: BLE001
            last_error = exc
            print(
                f"⚠️  {request_id} 用户请求生成第 {attempt}/{args.request_generation_retries} 次失败: {exc}",
                flush=True,
            )

    if args.disable_template_request_fallback:
        raise RuntimeError(f"{request_id} 用户请求生成失败: {last_error}") from last_error

    print(f"⚠️  {request_id} 用户请求生成失败，使用模板请求兜底", flush=True)
    row = generate_template_requests(1, index, args.seed + index, args.date_mode)[0]
    row["source"] = "template_fallback"
    return row


def build_one_request(index: int, args: argparse.Namespace) -> dict[str, Any]:
    """生成单条原始 TripRequest。"""
    if args.request_source == "controlled":
        return generate_controlled_request(index, args)
    if args.request_source == "template":
        return generate_template_requests(1, index, args.seed + index, args.date_mode)[0]
    return generate_llm_request(index, args)


def make_lf_row(record: dict[str, Any]) -> dict[str, Any]:
    """转换成 LLaMA-Factory alpaca 格式。"""
    return {
        "instruction": PLANNER_AGENT_PROMPT,
        "input": record["planner_query"],
        "output": record["output"],
    }


def write_llamafactory_files(records: list[dict[str, Any]], val_ratio: float) -> tuple[int, int]:
    """写入 LLaMA-Factory JSON 数组文件。"""
    lf_rows = [make_lf_row(row) for row in records]
    train_rows, val_rows = split_train_val(lf_rows, val_ratio=val_ratio)
    write_json(LLAMAFACTORY_TRAIN_PATH, train_rows)
    write_json(LLAMAFACTORY_VAL_PATH, val_rows)
    update_dataset_info()
    return len(train_rows), len(val_rows)


def update_dataset_info() -> None:
    """把 legacy SFT 数据集注册到 dataset_info.json。"""
    if DATASET_INFO_PATH.exists():
        data = json.loads(DATASET_INFO_PATH.read_text(encoding="utf-8"))
    else:
        data = {}

    data["trip_legacy_sft_train"] = {"file_name": LLAMAFACTORY_TRAIN_PATH.name}
    data["trip_legacy_sft_val"] = {"file_name": LLAMAFACTORY_VAL_PATH.name}
    write_json(DATASET_INFO_PATH, data)


def load_existing_record_ids(path: Path) -> set[str]:
    """读取已成功样本 ID，用于断点续跑。"""
    return {row.get("record_id", "") for row in read_jsonl(path)}


def generate_one(raw_request: dict[str, Any], args: argparse.Namespace, amap_api_key: str) -> dict[str, Any]:
    """生成一条 legacy SFT 样本。"""
    request_id = raw_request["request_id"]
    request = normalize_request(raw_request, request_id)
    builder = get_worker_context_builder(amap_api_key, args.historical_weather_provider)

    started_at = time.perf_counter()
    planner_context = builder.collect(request)
    weather_status = planner_context["tool_snapshot"].get("tool_status", {}).get("weather", {})
    weather_provider = "open_meteo_archive" if "open_meteo_archive" in str(weather_status.get("message", "")) else "amap_or_unknown"
    compact_context = builder.compact_for_planner(planner_context)
    planner_query = build_planner_query(builder, request, planner_context)

    llm = get_worker_llm()
    plan_data = llm.complete_json(
        PLANNER_AGENT_PROMPT,
        planner_query,
        temperature=args.temperature,
        max_tokens=planner_max_output_tokens(request, args),
    )
    trip_plan = TripPlan(**plan_data)
    validate_trip_plan_shape(trip_plan, request, planner_context)
    output = json.dumps(trip_plan.model_dump(), ensure_ascii=False)

    elapsed = time.perf_counter() - started_at
    return {
        "record_id": request_id,
        "created_at": datetime.now(timezone.utc).isoformat(),
        "request_source": raw_request.get("source", "unknown"),
        "request": request.model_dump(),
        "control_spec": raw_request.get("control_spec", {}),
        "system_prompt": PLANNER_AGENT_PROMPT,
        "planner_query": planner_query,
        "output": output,
        "trip_plan": trip_plan.model_dump(),
        "compact_planner_context": compact_context,
        "planner_context": planner_context,
        "metadata": {
            "elapsed_seconds": round(elapsed, 3),
            "prompt_chars": len(planner_query),
            "output_chars": len(output),
            "weather_provider": weather_provider,
            "tool_counts": {
                "classic_pois": len(planner_context["tool_snapshot"].get("classic_pois") or []),
                "preference_pois": len(planner_context["tool_snapshot"].get("preference_pois") or []),
                "scenic_pois": len(planner_context["tool_snapshot"].get("scenic_pois") or []),
                "experience_pois": len(planner_context["tool_snapshot"].get("experience_pois") or []),
                "hotel_pois": len(planner_context["tool_snapshot"].get("hotel_pois") or []),
                "food_pois": len(planner_context["tool_snapshot"].get("food_pois") or []),
                "trip_weather": len(planner_context["tool_snapshot"].get("trip_weather") or []),
            },
        },
    }


def collect_context_dry_run(index: int, args: argparse.Namespace, amap_api_key: str) -> dict[str, Any]:
    """只生成请求并获取 PlannerContext，不调用 Planner LLM。"""
    raw_request = build_one_request(index, args)
    request = normalize_request(raw_request, raw_request["request_id"])
    validate_request_date_mode(request, args.date_mode)
    builder = get_worker_context_builder(amap_api_key, args.historical_weather_provider)
    started_at = time.perf_counter()
    planner_context = builder.collect(request)
    compact_context = builder.compact_for_planner(planner_context)
    weather_status = planner_context["tool_snapshot"].get("tool_status", {}).get("weather", {})
    weather_provider = "open_meteo_archive" if "open_meteo_archive" in str(weather_status.get("message", "")) else "amap_or_unknown"
    return {
        "record_id": raw_request["request_id"],
        "request": request.model_dump(),
        "control_spec": raw_request.get("control_spec", {}),
        "elapsed_seconds": round(time.perf_counter() - started_at, 3),
        "prompt_chars": len(json.dumps(compact_context, ensure_ascii=False)),
        "weather_provider": weather_provider,
        "tool_status": planner_context["tool_snapshot"].get("tool_status", {}),
        "tool_counts": {
            "classic_pois": len(planner_context["tool_snapshot"].get("classic_pois") or []),
            "preference_pois": len(planner_context["tool_snapshot"].get("preference_pois") or []),
            "scenic_pois": len(planner_context["tool_snapshot"].get("scenic_pois") or []),
            "experience_pois": len(planner_context["tool_snapshot"].get("experience_pois") or []),
            "hotel_pois": len(planner_context["tool_snapshot"].get("hotel_pois") or []),
            "food_pois": len(planner_context["tool_snapshot"].get("food_pois") or []),
            "trip_weather": len(planner_context["tool_snapshot"].get("trip_weather") or []),
        },
    }


def generate_one_by_index(index: int, args: argparse.Namespace, amap_api_key: str) -> dict[str, Any]:
    """异步 worker 单元：生成请求、查工具、蒸馏答案、校验，全部成功才返回。"""
    request_id = f"legacy_request_{index:06d}"
    last_error: Exception | None = None
    for attempt in range(1, args.sample_retries + 1):
        try:
            raw_request = build_one_request(index, args)
            record = generate_one(raw_request, args, amap_api_key)
            record["metadata"]["sample_attempt"] = attempt
            return record
        except Exception as exc:  # noqa: BLE001
            last_error = exc
            print(
                f"⚠️  {request_id} 样本生成第 {attempt}/{args.sample_retries} 次失败: {exc}",
                flush=True,
            )
    raise RuntimeError(f"{request_id} 样本生成失败: {last_error}") from last_error


def build_requests(args: argparse.Namespace) -> list[dict[str, Any]]:
    """生成本轮 TripRequest 原始输入。"""
    if args.request_source == "controlled":
        print(f"开始用受控分布生成模拟用户请求: count={args.count}", flush=True)
        return [generate_controlled_request(args.start_index + index, args) for index in range(args.count)]
    if args.request_source == "template":
        print(f"开始用模板生成模拟用户请求: count={args.count}", flush=True)
        return generate_template_requests(args.count, args.start_index, args.seed)
    return generate_llm_requests(
        args.count,
        args.start_index,
        args.request_batch_size,
        args.seed,
        args.request_max_tokens,
        args.request_generation_retries,
        not args.disable_template_request_fallback,
    )


def summarize_requests(requests: list[dict[str, Any]]) -> dict[str, Any]:
    """汇总请求分布，给dry-run用。"""
    return {
        "count": len(requests),
        "companion_type": dict(Counter((item.get("control_spec") or {}).get("companion_type", "unknown") for item in requests)),
        "city": dict(Counter(item.get("city") for item in requests).most_common(20)),
        "city_tier": dict(Counter((item.get("control_spec") or {}).get("city_tier", "unknown") for item in requests)),
        "travel_days": dict(Counter(item.get("travel_days") for item in requests)),
        "transportation": dict(Counter(item.get("transportation") for item in requests)),
        "accommodation": dict(Counter(item.get("accommodation") for item in requests)),
        "budget_level": dict(Counter((item.get("control_spec") or {}).get("budget_level", "unknown") for item in requests)),
        "pace": dict(Counter((item.get("control_spec") or {}).get("pace", "unknown") for item in requests)),
        "diet": dict(Counter((item.get("control_spec") or {}).get("diet", "unknown") for item in requests)),
        "preferences_top20": dict(Counter(pref for item in requests for pref in (item.get("preferences") or [])).most_common(20)),
        "date_bucket": dict(Counter(date_bucket(item) for item in requests)),
    }


def date_bucket(item: dict[str, Any]) -> str:
    """请求日期桶。"""
    start_date = date.fromisoformat(item["start_date"])
    end_date = date.fromisoformat(item["end_date"])
    today = date.today()
    if end_date < today:
        return "past"
    if start_date <= today + timedelta(days=4):
        return "near_future"
    return "far_future"


def print_request_summary(requests: list[dict[str, Any]]) -> None:
    """打印请求分布摘要。"""
    summary = summarize_requests(requests)
    print(json.dumps(summary, ensure_ascii=False, indent=2))


def run_context_dry_run(args: argparse.Namespace, amap_api_key: str) -> None:
    """只跑工具快照，不调用强模型，不写训练数据。"""
    indices = [args.start_index + offset for offset in range(args.count)]
    results = []
    failed = []
    print(
        f"开始PlannerContext dry-run: count={len(indices)}, workers={args.workers}, "
        f"request_source={args.request_source}, date_mode={args.date_mode}",
        flush=True,
    )
    with ThreadPoolExecutor(max_workers=max(1, args.workers)) as executor:
        futures = {executor.submit(collect_context_dry_run, index, args, amap_api_key): index for index in indices}
        for progress_index, future in enumerate(as_completed(futures), start=1):
            index = futures[future]
            try:
                item = future.result()
                results.append(item)
                print(
                    f"context progress: {progress_index}/{len(indices)} ok={len(results)} "
                    f"failed={len(failed)} last={item['record_id']} weather={item['weather_provider']}",
                    flush=True,
                )
            except Exception as exc:  # noqa: BLE001
                failed.append({"record_id": f"legacy_request_{index:06d}", "error": str(exc)})
                print(
                    f"context progress: {progress_index}/{len(indices)} ok={len(results)} "
                    f"failed={len(failed)} error={exc}",
                    flush=True,
                )

    requests = [item["request"] | {"control_spec": item.get("control_spec", {})} for item in results]
    print("\n请求分布:")
    print_request_summary(requests)
    print("\n工具状态:")
    print(
        json.dumps(
            {
                "count": len(results),
                "failed": failed[:10],
                "weather_provider": dict(Counter(item["weather_provider"] for item in results)),
                "tool_failures": [
                    {
                        "record_id": item["record_id"],
                        "tool_status": item["tool_status"],
                    }
                    for item in results
                    if any(not status.get("ok") for status in item["tool_status"].values())
                ][:10],
                "avg_elapsed_seconds": round(sum(item["elapsed_seconds"] for item in results) / len(results), 3) if results else 0,
                "avg_prompt_chars": int(sum(item["prompt_chars"] for item in results) / len(results)) if results else 0,
                "tool_counts_avg": {
                    key: round(sum(item["tool_counts"].get(key, 0) for item in results) / len(results), 2) if results else 0
                    for key in ["classic_pois", "preference_pois", "scenic_pois", "experience_pois", "hotel_pois", "food_pois", "trip_weather"]
                },
            },
            ensure_ascii=False,
            indent=2,
        )
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="生成 legacy SFT 数据")
    parser.add_argument("--count", type=int, default=20, help="本轮尝试生成的样本数")
    parser.add_argument("--start-index", type=int, default=0, help="request_id 起始编号")
    parser.add_argument("--seed", type=int, default=20260429)
    parser.add_argument("--request-source", choices=["template", "llm", "controlled"], default="template")
    parser.add_argument(
        "--date-mode",
        choices=["future", "mixed", "past"],
        default="future",
        help="用户请求日期分布；past/mixed可触发训练专用Open-Meteo历史天气",
    )
    parser.add_argument("--request-batch-size", type=int, default=20, help="兼容旧命令，当前异步流水线不再使用批量请求生成")
    parser.add_argument("--request-max-tokens", type=int, default=8000)
    parser.add_argument("--request-generation-retries", type=int, default=3)
    parser.add_argument("--disable-template-request-fallback", action="store_true")
    parser.add_argument("--workers", type=int, default=1)
    parser.add_argument("--sample-retries", type=int, default=3, help="单条样本完整链路失败后的重试次数")
    parser.add_argument("--temperature", type=float, default=0.2)
    parser.add_argument("--max-output-tokens", type=int, default=0, help="大于0时覆盖动态 token 上限")
    parser.add_argument("--output-base-tokens", type=int, default=int(os.getenv("PLANNER_OUTPUT_BASE_TOKENS", "3000")))
    parser.add_argument("--output-tokens-per-day", type=int, default=int(os.getenv("PLANNER_OUTPUT_TOKENS_PER_DAY", "1800")))
    parser.add_argument("--output-tokens-cap", type=int, default=int(os.getenv("PLANNER_MAX_OUTPUT_TOKENS_CAP", "16000")))
    parser.add_argument(
        "--historical-weather-provider",
        choices=["open-meteo", "none"],
        default="open-meteo",
        help="训练数据专用历史天气来源；只在整段行程早于今天时生效",
    )
    parser.add_argument("--val-ratio", type=float, default=0.1)
    parser.add_argument("--resume", action="store_true", help="跳过 records.jsonl 中已存在的 record_id")
    parser.add_argument("--dry-run-requests", action="store_true", help="只生成并打印请求，不调用高德和强模型")
    parser.add_argument("--dry-run-summary", action="store_true", help="dry-run-requests时只打印分布摘要")
    parser.add_argument("--dry-run-context", action="store_true", help="只生成请求并获取PlannerContext，不调用Planner强模型、不写训练数据")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    load_project_env()
    amap_api_key = os.getenv("AMAP_MAPS_API_KEY") or os.getenv("AMAP_API_KEY")
    if not amap_api_key and not args.dry_run_requests:
        raise RuntimeError("缺少 AMAP_MAPS_API_KEY 或 AMAP_API_KEY")

    if args.dry_run_requests:
        requests = [build_one_request(args.start_index + i, args) for i in range(args.count)]
        if args.dry_run_summary:
            print_request_summary(requests)
        else:
            print(json.dumps(requests, ensure_ascii=False, indent=2))
        return

    if args.dry_run_context:
        run_context_dry_run(args, amap_api_key)
        return

    existing_ids = load_existing_record_ids(RAW_RECORDS_PATH) if args.resume else set()
    indices = [
        args.start_index + offset
        for offset in range(args.count)
        if f"legacy_request_{args.start_index + offset:06d}" not in existing_ids
    ]
    if not indices:
        print("没有需要生成的新样本。")
        return

    print(
        f"开始异步生成 legacy SFT: count={len(indices)}, workers={args.workers}, "
        f"request_source={args.request_source}",
        flush=True,
    )

    ok = 0
    failed = 0
    if args.workers <= 1:
        for progress_index, sample_index in enumerate(indices, start=1):
            try:
                record = generate_one_by_index(sample_index, args, amap_api_key)
                append_jsonl(RAW_RECORDS_PATH, record)
                append_jsonl(REQUESTS_PATH, record["request"] | {"control_spec": record.get("control_spec", {})})
                ok += 1
                print(f"progress: {progress_index}/{len(indices)} ok={ok} failed={failed} last={record['record_id']}", flush=True)
            except Exception as exc:  # noqa: BLE001
                failed += 1
                append_jsonl(
                    ERRORS_PATH,
                    {
                        "created_at": datetime.now(timezone.utc).isoformat(),
                        "record_id": f"legacy_request_{sample_index:06d}",
                        "error_type": type(exc).__name__,
                        "error": str(exc),
                    },
                )
                print(f"progress: {progress_index}/{len(indices)} ok={ok} failed={failed} error={exc}", flush=True)
    else:
        with ThreadPoolExecutor(max_workers=args.workers) as executor:
            futures = {executor.submit(generate_one_by_index, index, args, amap_api_key): index for index in indices}
            for progress_index, future in enumerate(as_completed(futures), start=1):
                sample_index = futures[future]
                try:
                    record = future.result()
                    append_jsonl(RAW_RECORDS_PATH, record)
                    append_jsonl(REQUESTS_PATH, record["request"] | {"control_spec": record.get("control_spec", {})})
                    ok += 1
                    print(f"progress: {progress_index}/{len(indices)} ok={ok} failed={failed} last={record['record_id']}", flush=True)
                except Exception as exc:  # noqa: BLE001
                    failed += 1
                    append_jsonl(
                        ERRORS_PATH,
                        {
                            "created_at": datetime.now(timezone.utc).isoformat(),
                            "record_id": f"legacy_request_{sample_index:06d}",
                            "error_type": type(exc).__name__,
                            "error": str(exc),
                        },
                    )
                    print(f"progress: {progress_index}/{len(indices)} ok={ok} failed={failed} error={exc}", flush=True)

    all_records = read_jsonl(RAW_RECORDS_PATH)
    train_count, val_count = write_llamafactory_files(all_records, val_ratio=args.val_ratio)
    print(
        "完成: "
        f"本轮成功={ok}, 本轮失败={failed}, 累计可训练={len(all_records)}, "
        f"train={train_count}, val={val_count}"
    )
    print(f"raw: {RAW_RECORDS_PATH}")
    print(f"errors: {ERRORS_PATH}")
    print(f"llamafactory train: {LLAMAFACTORY_TRAIN_PATH}")
    print(f"llamafactory val: {LLAMAFACTORY_VAL_PATH}")


if __name__ == "__main__":
    main()
