"""生成 SFT 数据。

对外推荐从 `training/scripts/run_pipeline.py --stage sft` 进入。这个脚本是总入口
调用的 SFT 生成阶段，单独运行主要用于调试请求、上下文和生成本身。

示例:

1. 先 dry-run 看受控请求分布，不调用高德和强模型:

   cd .
   .venv-training-py311/bin/python3 <path-to-generate_sft_data.py> \
     --count 50 \
     --request-source controlled \
     --date-mode mixed \
     --dry-run-requests \
     --dry-run-summary

2. 跑 PlannerContext smoke，只查工具，不调用 Planner 强模型:

   .venv-training-py311/bin/python3 <path-to-generate_sft_data.py> \
     --count 20 \
     --request-source controlled \
     --date-mode mixed \
     --workers 2 \
     --dry-run-context

3. 正式用受控真实分布请求，再用强模型蒸馏 TripPlan:

   .venv-training-py311/bin/python3 <path-to-generate_sft_data.py> \
     --count 100 \
     --request-source controlled \
     --date-mode mixed \
     --workers 4 \
     --teacher-model-provider deepseek \
     --output-dir <output-dir> \
     --resume

输出:

- <output-dir>/records.jsonl: 完整可审计记录，包含 request、PlannerContext、prompt 和 TripPlan。
- <output-dir>/errors.jsonl: 失败样本，不进入训练集。
- 提供 `--output-dir` 时，LLaMA-Factory 临时导出写在 `<output-dir>/llamafactory_train.json` 和 `<output-dir>/llamafactory_val.json`；统一入口会在审计、分类后生成最终带 run 名称的 train/val 文件。
- 不提供 `--output-dir` 时，才会写入 `training/data/llamafactory/generated/trip_sft_train.json` 和 `trip_sft_val.json`。
"""

from __future__ import annotations

import argparse
import json
import math
import os
import random
import re
import sys
import threading
import time
from collections import Counter
from concurrent.futures import FIRST_COMPLETED, ThreadPoolExecutor, as_completed, wait
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parents[4]
SCRIPTS_DIR = PROJECT_ROOT / "training" / "scripts"
LEGACY_SCRIPTS_DIR = SCRIPTS_DIR / "legacy"
EVAL_SCRIPTS_DIR = SCRIPTS_DIR / "eval"
BACKEND_DIR = PROJECT_ROOT / "backend"
sys.path.insert(0, str(SCRIPTS_DIR))
sys.path.insert(0, str(LEGACY_SCRIPTS_DIR))
sys.path.insert(0, str(EVAL_SCRIPTS_DIR))
sys.path.insert(0, str(BACKEND_DIR))

from shared.common import DATA_DIR, LLAMAFACTORY_DIR, load_project_env, read_jsonl, split_train_val, write_json
from shared.llm_client import DataGenLLM


from app.planner.context import PlannerContextBuilder  # noqa: E402
from app.planner.amap import set_amap_qps_limit  # noqa: E402
from app.planner.output import is_lodging_breakfast_meal, name_in_candidates, normalize_poi_name, validate_trip_plan_shape  # noqa: E402
from app.agents.planner_query import build_planner_query as build_backend_planner_query  # noqa: E402
from app.agents.prompts import PLANNER_AGENT_PROMPT  # noqa: E402
from app.models.schemas import Budget, TripPlan, TripRequest  # noqa: E402
from historical_weather import fetch_historical_trip_weather, is_past_trip  # noqa: E402


DEFAULT_SFT_DIR = DATA_DIR / "planner" / "sft_runs" / "default"
RAW_RECORDS_PATH = DEFAULT_SFT_DIR / "records.jsonl"
ERRORS_PATH = DEFAULT_SFT_DIR / "errors.jsonl"
REQUESTS_PATH = DEFAULT_SFT_DIR / "requests.jsonl"
LLAMAFACTORY_GENERATED_DIR = LLAMAFACTORY_DIR / "generated"
LLAMAFACTORY_TRAIN_PATH = LLAMAFACTORY_GENERATED_DIR / "trip_sft_train.json"
LLAMAFACTORY_VAL_PATH = LLAMAFACTORY_GENERATED_DIR / "trip_sft_val.json"
DATASET_INFO_PATH = LLAMAFACTORY_DIR / "dataset_info.json"
REGISTER_LLAMAFACTORY_DATASET = True
REQUEST_ID_PREFIX = "request"


class BudgetContextUnreachableError(ValueError):
    """预算补数上下文候选池不足，不值得重试同一条请求。"""

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
    ("friends", 22),
    ("couple", 20),
    ("solo", 15),
    ("family_with_children", 18),
    ("family_with_elders", 10),
    ("family_mixed", 7),
    ("business", 4),
    ("other", 4),
]

CITY_TIER_WEIGHTS = [("major", 35), ("popular", 40), ("long_tail", 25)]
DATE_MODE_WEIGHTS = [("past", 30), ("near_future", 30), ("far_future", 40)]
TRAVEL_DAYS_WEIGHTS = [(2, 18), (3, 42), (4, 28), (5, 12)]
BUDGET_WEIGHTS = [("limited", 25), ("standard", 40), ("comfortable", 23), ("premium", 9), ("luxury", 3)]
PACE_WEIGHTS = [("适中节奏", 45), ("慢节奏", 35), ("紧凑高效", 12), ("自由活动多", 8)]
SUPPLEMENT_VERSION = "budget_utilization_soft"
SUPPLEMENT_BUDGET_STRICTNESS_WEIGHTS = [
    (("comfortable", "soft"), 250),
    (("premium", "soft"), 250),
]
SUPPLEMENT_TRAVEL_DAYS_WEIGHTS = [(3, 100), (4, 200), (5, 200)]
SUPPLEMENT_COMPANION_WEIGHTS = [
    ("couple", 90),
    ("friends", 90),
    ("family_mixed", 90),
    ("family_with_elders", 75),
    ("family_with_children", 75),
    ("business", 40),
    ("solo", 25),
    ("other", 15),
]
SUPPLEMENT_PACE_WEIGHTS = [("适中节奏", 34), ("慢节奏", 34), ("紧凑高效", 22), ("自由活动多", 10)]
SUPPLEMENT_SOFT_BUDGET_POLICY = {
    "target_min_ratio": 0.95,
    "target_max_ratio": 1.05,
    "validation_min_ratio_margin": 0.02,
    "validation_max_ratio_margin": 0.02,
    "instruction": (
        "这是一条预算利用型SFT补充样本；soft预算应尽量落在用户总预算的95%-105%之间，"
        "不要做成低配省钱方案。预算只能通过选择更高价的真实候选实现，不能修改任何"
        "hotel/attraction/meal单价，不能复用同一家餐厅凑预算。"
    ),
}

# 真实用户表达预算时通常不会给 14674 这种精确数字。这里统一成
# “整趟总预算”语义：住宿按 N-1 晚、两人一间；餐饮/门票/体验按
# 人数线性；市内交通按队伍共享日成本估算。这里必须和 eval realbudget
# 口径保持一致。
PER_PERSON_DAY_BUDGETS = {
    "limited": [220, 270, 320],
    "standard": [380, 470, 560],
    "comfortable": [600, 750, 900],
    "premium": [950, 1200, 1450],
    "luxury": [1600, 2200, 3000],
}
# 预算利用型补数也必须沿用真实预算分档；候选池可达性由 dry-run/context
# smoke/audit 来筛，不通过单独调窄或平移分档边界来“做漂亮”。
SUPPLEMENT_PER_PERSON_DAY_BUDGETS = PER_PERSON_DAY_BUDGETS

REQUEST_HOTEL_COST_BY_ACCOMMODATION = {
    "经济型酒店": 300,
    "民宿": 420,
    "舒适型酒店": 520,
    "亲子酒店": 650,
    "高端酒店": 1000,
}

REQUEST_CITY_BUDGET_FACTORS = {
    "major": 1.15,
    "popular": 1.05,
    "long_tail": 0.95,
}

REQUEST_SHARED_TRANSPORT_DAY_COST = {
    "公共交通": 80,
    "地铁+步行": 60,
    "打车": 220,
    "自驾": 260,
}

REQUEST_COMPANION_BUDGET_FACTORS = {
    "solo": 0.95,
    "couple": 1.0,
    "friends": 1.04,
    "business": 1.08,
    "family_with_children": 1.25,
    "family_with_elders": 1.38,
    "family_mixed": 1.45,
    "other": 1.08,
}

SUPPLEMENT_COMPANION_BUDGET_FACTORS = {
    "solo": 0.95,
    "couple": 1.0,
    "friends": 1.02,
    "business": 1.06,
    "family_with_children": 1.12,
    "family_with_elders": 1.12,
    "family_mixed": 1.16,
    "other": 1.05,
}

BUDGET_USAGE_RATIO_BY_LEVEL = {
    "limited": (0.72, 1.00),
    "standard": (0.60, 1.05),
    "comfortable": (0.70, 1.10),
    "premium": (0.75, 1.12),
    "luxury": (0.75, 1.18),
}
BUDGET_VALIDATION_MIN_RATIO_MARGIN = 0.08
BUDGET_VALIDATION_MAX_RATIO_MARGIN = 0.16
BUDGET_VALIDATION_HARD_MAX_RATIO_MARGIN = 0.05
BUDGET_NARRATIVE_AMOUNT_RE = re.compile(
    r"(?:预算|总预算|总费用|总花费|实际花费|实际费用|实际总费用)"
    r"[^，。；;、\n]{0,18}?"
    r"(?:约|预计|控制在|为|是|共|合计|总计|总额)?"
    r"\s*(\d{3,7})\s*元"
)
LUNCH_DINNER_MEAL_TYPES = {"lunch", "dinner"}

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

DIET_POSITIVE_BY_LABEL = {
    "少辣": ["少辣"],
    "清真": ["清真"],
    "素食": ["素食"],
    "清淡饮食": ["清淡饮食"],
}

DIET_AVOID_BY_LABEL = {
    "海鲜过敏": ["海鲜"],
    "清真": ["猪肉", "酒"],
    "素食": ["荤菜"],
    "少辣": ["重辣"],
    "清淡饮食": ["重口味"],
}

NEGATIVE_TEXT_PHRASES = [
    "人挤人的网红店",
    "网红排队店",
    "过度商业化景点",
    "大型商场",
    "纯购物行程",
    "夜生活",
    "过长步行",
    "长时间排队",
    "打卡式景点",
    "高价餐厅",
    "景区快餐",
    "太早起",
    "密集行程",
    "太偏远的景点",
    "太累的路线",
    "购物团",
    "跟团游",
    "爬山",
    "酒吧",
]


_thread_local = threading.local()
_write_lock = threading.Lock()
_open_meteo_lock = threading.Lock()
_last_open_meteo_call_at = 0.0


def throttle_open_meteo_call() -> None:
    """限制 Open-Meteo 历史天气请求速率，避免高并发造数触发 429。"""
    global _last_open_meteo_call_at
    min_interval = float(os.getenv("OPEN_METEO_MIN_INTERVAL_SECONDS", "0.4"))
    with _open_meteo_lock:
        now = time.monotonic()
        wait_seconds = min_interval - (now - _last_open_meteo_call_at)
        if wait_seconds > 0:
            time.sleep(wait_seconds)
        _last_open_meteo_call_at = time.monotonic()


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
            for attempt in range(1, 4):
                try:
                    throttle_open_meteo_call()
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
                except Exception as exc:  # noqa: BLE001
                    if attempt >= 3:
                        print(f"⚠️  Open-Meteo历史天气失败，回退默认天气链路: {exc}", flush=True)
                        break
                    time.sleep(1.5 * attempt)
        return super()._collect_weather_snapshot(request)


def append_jsonl(path: Path, row: dict[str, Any]) -> None:
    """线程安全追加 JSONL。"""
    path.parent.mkdir(parents=True, exist_ok=True)
    with _write_lock:
        with path.open("a", encoding="utf-8") as f:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")


def get_worker_llm(args: argparse.Namespace | None = None) -> DataGenLLM:
    """每个线程懒加载一个 LLM client，避免共享客户端状态。"""
    provider = getattr(args, "data_gen_provider", None)
    model = getattr(args, "data_gen_model", None)
    llm_key = f"{provider or ''}:{model or ''}"
    if getattr(_thread_local, "llm_key", None) != llm_key:
        _thread_local.llm = DataGenLLM(provider=provider, model=model)
        _thread_local.llm_key = llm_key
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


def unique_list(values: list[Any]) -> list[str]:
    """保持顺序去重。"""
    results = []
    seen = set()
    for value in values:
        text = str(value or "").strip()
        if not text or text in seen:
            continue
        seen.add(text)
        results.append(text)
    return results


def positive_preference_tags(preferences: list[str]) -> list[str]:
    """造数侧也保证 preferences 只承载正向偏好。"""
    negative_markers = ["过敏", "不吃", "不要", "避免", "避开", "忌", "不能", "不想", "别"]
    return unique_list(
        [
            item
            for item in preferences
            if not any(marker in str(item) for marker in negative_markers)
        ]
    )


def diet_positive(diet: str) -> list[str]:
    """饮食正向偏好。"""
    return list(DIET_POSITIVE_BY_LABEL.get(diet, []))


def diet_avoid(diet: str) -> list[str]:
    """饮食负向约束。"""
    return list(DIET_AVOID_BY_LABEL.get(diet, []))


def infer_diet_label(preferences: list[str], free_text: str) -> str:
    """从模板/LLM请求里粗略归一化饮食标签。"""
    text = " ".join(preferences + [free_text])
    if "海鲜" in text and any(marker in text for marker in ["过敏", "不吃", "不要", "避免", "忌", "不能"]):
        return "海鲜过敏"
    for diet in ["清真", "素食", "少辣", "清淡饮食"]:
        if diet in text:
            return diet
    return "无"


def build_negative_constraints(avoid: list[str], diet: str, free_text: str) -> list[str]:
    """构造训练用负向约束标签。"""
    results = list(avoid) + diet_avoid(diet)
    for phrase in NEGATIVE_TEXT_PHRASES:
        if phrase in free_text:
            results.append(phrase)
    return unique_list(results)


def build_preference_control_spec(
    preferences: list[str],
    free_text: str,
    party: dict[str, Any],
    pace: str,
    diet: str,
    avoid: list[str],
) -> dict[str, Any]:
    """把正向偏好/负向约束显式写入 control_spec。"""
    traveler_constraints = {
        "needs_child_friendly": int(party.get("children") or 0) > 0 or "孩子" in free_text or "带娃" in free_text,
        "needs_elder_friendly": int(party.get("elders") or 0) > 0 or "老人" in free_text or "长辈" in free_text or "父母" in free_text,
        "avoid_long_walk": any(marker in free_text for marker in ["少走路", "不想太累", "太累", "行动不便", "无障碍", "轮椅"]),
    }
    return {
        "positive_preferences": positive_preference_tags(preferences),
        "negative_constraints": build_negative_constraints(avoid, diet, free_text),
        "diet_positive": diet_positive(diet),
        "diet_avoid": diet_avoid(diet),
        "pace": pace,
        "traveler_constraints": traveler_constraints,
    }


def record_control_spec(raw_request: dict[str, Any], request: TripRequest, planner_context: dict[str, Any]) -> dict[str, Any]:
    """生成记录里最终落盘的 control_spec。

    对规则生成样本，保留生成侧结构；对LLM生成样本，用 PlannerContext
    解析结果补齐结构化偏好，便于后续审计和切片分析。
    """
    spec = dict(raw_request.get("control_spec") or {})
    profile = planner_context.get("preference_profile") or {}
    spec.setdefault("positive_preferences", profile.get("positive_preferences") or positive_preference_tags(request.preferences))
    spec.setdefault("negative_constraints", profile.get("negative_constraints") or [])
    spec.setdefault("diet_positive", profile.get("diet_positive") or [])
    spec.setdefault("diet_avoid", profile.get("diet_avoid") or [])
    spec.setdefault("pace", profile.get("pace") or "未指定")
    spec.setdefault("traveler_constraints", profile.get("traveler_constraints") or {})
    return spec


def build_planner_query(builder: PlannerContextBuilder, request: TripRequest, planner_context: dict[str, Any]) -> str:
    """构造与线上 Planner 一致的用户输入。

    训练数据和线上系统必须共用同一份 Planner query 组装逻辑。
    """
    return build_backend_planner_query(builder, request, planner_context)


def format_request_id(index: int) -> str:
    """生成 request_id。"""
    return f"{REQUEST_ID_PREFIX}_{index:06d}"


def planner_max_output_tokens(request: TripRequest, args: argparse.Namespace, sample_attempt: int = 1) -> int:
    """按天数和重试次数估算强模型输出上限。"""
    if args.max_output_tokens > 0:
        return args.max_output_tokens
    retry_extra = max(sample_attempt - 1, 0) * args.output_retry_tokens
    return min(args.output_base_tokens + request.travel_days * args.output_tokens_per_day + retry_extra, args.output_tokens_cap)


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

    if not item.get("party"):
        companion_type = control_spec.get("companion_type") or "other"
        rng = random.Random(sum(ord(ch) for ch in request_id))
        item["party"] = build_party_info(rng, companion_type)

    if not item.get("budget_constraint"):
        budget_level = control_spec.get("budget_level") or "standard"
        rng = random.Random(sum(ord(ch) for ch in f"{request_id}:{budget_level}"))
        amount = choose_budget_amount(
            rng,
            budget_level,
            int(item["party"].get("total") or 1),
            travel_days,
            item["accommodation"],
            item["transportation"],
            control_spec.get("city_tier") or infer_city_tier(item["city"]),
            control_spec.get("companion_type") or item["party"].get("companion_type") or "other",
        )
        item["budget_constraint"] = build_budget_constraint(rng, budget_level, amount)

    request = TripRequest(**item)
    # request_id 不属于后端 schema，放在 metadata 里；这里仅用于错误提示。
    if not request.city:
        raise ValueError(f"{request_id} 缺少 city")
    return request


def build_party_info(rng: random.Random, companion_type: str) -> dict[str, Any]:
    """按同行类型生成结构化人数。"""
    if companion_type == "solo":
        adults, children, elders = 1, 0, 0
    elif companion_type == "couple":
        adults, children, elders = 2, 0, 0
    elif companion_type == "friends":
        adults, children, elders = rng.choice([2, 3, 4]), 0, 0
    elif companion_type == "family_with_children":
        adults, children, elders = 2, rng.choice([1, 1, 2]), 0
    elif companion_type == "family_with_elders":
        adults, children, elders = rng.choice([1, 2]), 0, rng.choice([1, 2])
    elif companion_type == "family_mixed":
        adults, children, elders = 2, rng.choice([1, 1, 2]), rng.choice([1, 2])
    elif companion_type == "business":
        adults, children, elders = rng.choice([1, 2, 3]), 0, 0
    else:
        adults, children, elders = rng.choice([1, 2, 3]), 0, 0

    return {
        "adults": adults,
        "children": children,
        "elders": elders,
        "total": adults + children + elders,
        "companion_type": companion_type,
    }


def choose_budget_amount(
    rng: random.Random,
    budget_level: str,
    party_total: int,
    travel_days: int,
    accommodation: str,
    transportation: str = "公共交通",
    city_tier: str = "popular",
    companion_type: str = "other",
    per_person_day_budgets: dict[str, list[int]] | None = None,
    companion_budget_factors: dict[str, float] | None = None,
    party_budget_mode: str = "linear",
) -> int:
    """按 eval realbudget 口径推导整趟总预算，并按百元取整。

    `companion_budget_factors` 和 `party_budget_mode` 保留为旧调用兼容参数，
    当前主分布不再用 group_discount 压低多人餐饮/门票预算。
    """
    budget_table = per_person_day_budgets or PER_PERSON_DAY_BUDGETS
    level = "premium" if budget_level == "luxury" else budget_level
    per_person_day = rng.choice(budget_table.get(level, budget_table["standard"]))
    party_total = max(party_total, 1)
    travel_days = max(travel_days, 1)
    lodging_nights = max(travel_days - 1, 0)
    lodging_per_night = REQUEST_HOTEL_COST_BY_ACCOMMODATION.get(accommodation, 300)
    room_count = max(1, math.ceil(party_total / 2))
    city_factor = REQUEST_CITY_BUDGET_FACTORS.get(city_tier, 1.0)
    shared_transport_day = REQUEST_SHARED_TRANSPORT_DAY_COST.get(transportation, 120)

    lodging_total = lodging_per_night * lodging_nights * room_count
    person_total = per_person_day * party_total * travel_days
    shared_transport_total = shared_transport_day * travel_days
    raw_total = (lodging_total + person_total + shared_transport_total) * city_factor
    return max(500, int(round(raw_total / 100.0) * 100))


def budget_party_units(party_total: int, mode: str = "linear") -> float:
    """预算表达的多人折扣；实际评测仍按人头重算餐饮/门票。"""
    party_total = max(party_total, 1)
    if mode == "group_discount":
        return 1.0 + math.log2(party_total)
    return float(party_total)


def infer_city_tier(city: str) -> str:
    """根据城市名回推预算城市层级。"""
    for tier, cities in CITY_TIERS.items():
        if city in cities:
            return tier
    return "popular"


def build_budget_constraint(
    rng: random.Random,
    budget_level: str,
    amount: int | None,
    strictness: str | None = None,
) -> dict[str, Any]:
    """构造预算约束。"""
    if strictness:
        resolved_strictness = strictness
    elif amount is None:
        resolved_strictness = "none"
    elif budget_level == "limited":
        resolved_strictness = weighted_choice(rng, [("soft", 72), ("hard", 20), ("none", 8)])
    else:
        resolved_strictness = weighted_choice(rng, [("soft", 88), ("hard", 4), ("none", 8)])

    if amount is None:
        strictness = "none"
    else:
        strictness = resolved_strictness

    return {
        "amount": amount,
        "scope": "total",
        "currency": "CNY",
        "budget_level": budget_level,
        "strictness": strictness,
    }


def parse_target_budget_mix(value: str | None) -> list[tuple[str, str, int]]:
    """解析形如 standard/soft=520,comfortable/soft=245 的目标预算分布。"""
    if not value:
        return []
    result: list[tuple[str, str, int]] = []
    valid_levels = {"limited", "standard", "comfortable", "premium", "luxury"}
    valid_strictness = {"hard", "soft", "none"}
    for raw_part in value.split(","):
        part = raw_part.strip()
        if not part:
            continue
        if "=" not in part:
            raise ValueError(f"target budget mix 项缺少 '=': {part}")
        key, count_text = part.split("=", 1)
        key = key.strip()
        count = int(count_text.strip())
        if count <= 0:
            continue
        if "/" in key:
            level, strictness = [item.strip() for item in key.split("/", 1)]
        else:
            level, strictness = key, "soft"
        if level not in valid_levels:
            raise ValueError(f"不支持的 budget_level: {level}")
        if strictness not in valid_strictness:
            raise ValueError(f"不支持的 budget strictness: {strictness}")
        result.append((level, strictness, count))
    if not result:
        raise ValueError("target budget mix 不能为空")
    return result


def target_budget_choice(index: int, args: argparse.Namespace) -> tuple[str, str] | None:
    """按 index 稳定映射到目标预算档位/strictness。"""
    mix = parse_target_budget_mix(getattr(args, "target_budget_mix", ""))
    if not mix:
        return None
    total = sum(count for _, _, count in mix)
    offset = (index - int(getattr(args, "start_index", 0))) % total
    cursor = 0
    for level, strictness, count in mix:
        cursor += count
        if offset < cursor:
            return level, strictness
    level, strictness, _ = mix[-1]
    return level, strictness


def normalize_budget_strictness(
    budget_constraint: dict[str, Any],
    args: argparse.Namespace,
) -> dict[str, Any]:
    """训练预算主线里，有 amount 的请求不能关闭预算策略。"""
    if (
        getattr(args, "disallow_budget_strictness_none", False)
        and budget_constraint.get("amount") is not None
        and budget_constraint.get("strictness") == "none"
    ):
        budget_constraint = dict(budget_constraint)
        budget_constraint["strictness"] = "soft"
    return budget_constraint


def budget_fit_policy(
    request: TripRequest,
    policy_override: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """把预算档位转换成强模型可执行、可校验的目标花费区间。"""
    constraint = request.budget_constraint
    amount = int(constraint.amount or 0)
    if amount <= 0 or constraint.strictness == "none":
        return {
            "enabled": False,
            "reason": "budget_amount_unavailable_or_none_strictness",
        }

    min_ratio, max_ratio = BUDGET_USAGE_RATIO_BY_LEVEL.get(
        constraint.budget_level,
        BUDGET_USAGE_RATIO_BY_LEVEL["standard"],
    )
    if constraint.strictness == "hard":
        max_ratio = min(max_ratio, 1.0)
    elif constraint.strictness == "soft":
        max_ratio = max(max_ratio, 1.05)

    if policy_override:
        min_ratio = float(policy_override.get("target_min_ratio", min_ratio))
        max_ratio = float(policy_override.get("target_max_ratio", max_ratio))
        if constraint.strictness == "hard":
            max_ratio = min(max_ratio, 1.0)

    policy = {
        "enabled": True,
        "budget_level": constraint.budget_level,
        "strictness": constraint.strictness,
        "amount": amount,
        "target_min_ratio": min_ratio,
        "target_max_ratio": max_ratio,
        "target_min_total": int(round(amount * min_ratio / 100.0) * 100),
        "target_max_total": int(round(amount * max_ratio / 100.0) * 100),
        "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。",
    }
    if policy_override:
        if policy_override.get("instruction"):
            policy["instruction"] = str(policy_override["instruction"])
        for key in ["validation_min_ratio_margin", "validation_max_ratio_margin", "validation_hard_max_ratio_margin"]:
            if key in policy_override:
                policy[key] = float(policy_override[key])
    return policy


def apply_budget_fit_policy(
    planner_context: dict[str, Any],
    request: TripRequest,
    raw_request: dict[str, Any] | None = None,
) -> None:
    """把预算贴合策略写入 PlannerContext 的约束区。"""
    planner_constraints = planner_context.setdefault("planner_constraints", {})
    control_spec = (raw_request or {}).get("control_spec") or {}
    planner_constraints["budget_fit_policy"] = budget_fit_policy(
        request,
        control_spec.get("budget_fit_policy_override"),
    )


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


def weighted_block_choice(index: int, seed: int, weighted_items: list[tuple[Any, int]], salt: str) -> Any:
    """按权重构造一个可重复的随机排列块，便于补数分布稳定。"""
    pool: list[Any] = []
    for item, weight in weighted_items:
        pool.extend([item] * weight)
    if not pool:
        raise ValueError("weighted_items 不能为空")
    rng = random.Random(f"{seed}:{salt}:{len(pool)}")
    rng.shuffle(pool)
    return pool[index % len(pool)]


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
    if companion_type == "family_with_children":
        if budget_level == "limited":
            weights = [("经济型酒店", 50), ("舒适型酒店", 28), ("亲子酒店", 14), ("民宿", 8)]
        elif budget_level == "standard":
            weights = [("舒适型酒店", 42), ("亲子酒店", 30), ("经济型酒店", 20), ("民宿", 8)]
        elif budget_level == "comfortable":
            weights = [("舒适型酒店", 45), ("亲子酒店", 32), ("高端酒店", 12), ("民宿", 11)]
        else:
            weights = [("亲子酒店", 36), ("高端酒店", 32), ("舒适型酒店", 24), ("民宿", 8)]
    elif companion_type == "family_mixed":
        if budget_level == "limited":
            weights = [("经济型酒店", 48), ("舒适型酒店", 34), ("民宿", 12), ("亲子酒店", 6)]
        elif budget_level == "standard":
            weights = [("舒适型酒店", 50), ("经济型酒店", 22), ("亲子酒店", 18), ("民宿", 10)]
        elif budget_level == "comfortable":
            weights = [("舒适型酒店", 48), ("亲子酒店", 26), ("高端酒店", 14), ("民宿", 12)]
        else:
            weights = [("高端酒店", 36), ("舒适型酒店", 32), ("亲子酒店", 24), ("民宿", 8)]
    elif budget_level == "luxury":
        weights = [("高端酒店", 66), ("舒适型酒店", 24), ("民宿", 10)]
    elif budget_level == "premium":
        weights = [("高端酒店", 45), ("舒适型酒店", 38), ("民宿", 10), ("经济型酒店", 7)]
    elif budget_level == "comfortable":
        weights = [("舒适型酒店", 55), ("高端酒店", 18), ("民宿", 17), ("经济型酒店", 10)]
    elif budget_level == "limited":
        weights = [("经济型酒店", 70), ("民宿", 20), ("舒适型酒店", 10)]
    else:
        weights = [("舒适型酒店", 48), ("经济型酒店", 35), ("民宿", 16), ("高端酒店", 1)]
    return weighted_choice(rng, weights)


def choose_supplement_accommodation(rng: random.Random, companion_type: str, budget_level: str) -> str:
    """预算补数的住宿分布，适度增加高预算可用价格带。"""
    if budget_level == "limited":
        weights = [("经济型酒店", 56), ("舒适型酒店", 28), ("民宿", 10), ("亲子酒店", 6)]
    elif budget_level == "standard":
        weights = [("舒适型酒店", 45), ("经济型酒店", 26), ("民宿", 14), ("亲子酒店", 10), ("高端酒店", 5)]
    elif budget_level == "comfortable":
        weights = [("舒适型酒店", 38), ("高端酒店", 26), ("亲子酒店", 18), ("民宿", 18)]
    elif budget_level == "premium":
        weights = [("高端酒店", 56), ("舒适型酒店", 18), ("民宿", 14), ("亲子酒店", 12)]
    else:
        weights = [("高端酒店", 70), ("民宿", 14), ("亲子酒店", 10), ("舒适型酒店", 6)]

    if companion_type == "family_with_children":
        weights = [(name, weight + (16 if name == "亲子酒店" else 0)) for name, weight in weights]
    elif companion_type == "family_mixed":
        weights = [(name, weight + (10 if name in {"亲子酒店", "舒适型酒店"} else 0)) for name, weight in weights]
    elif companion_type == "business" and budget_level in {"comfortable", "premium", "luxury"}:
        weights = [(name, weight + (12 if name in {"高端酒店", "舒适型酒店"} else 0)) for name, weight in weights]
    return weighted_choice(rng, weights)


def choose_controlled_transportation(rng: random.Random, companion_type: str, city: str) -> str:
    """交通方式近似真实分布，并根据城市/同行类型微调。"""
    metro_cities = {"北京", "上海", "广州", "深圳", "成都", "杭州", "重庆", "南京", "苏州", "武汉", "西安"}
    if companion_type in {"family_with_children", "family_with_elders", "family_mixed"}:
        weights = [("地铁+步行", 26), ("公共交通", 18), ("打车", 42), ("自驾", 14)]
    elif companion_type == "business":
        weights = [("打车", 56), ("地铁+步行", 22), ("公共交通", 12), ("自驾", 10)]
    elif city in {"大理", "丽江", "桂林", "三亚", "张家界", "黄山"}:
        weights = [("地铁+步行", 12), ("公共交通", 22), ("打车", 34), ("自驾", 32)]
    elif city in metro_cities:
        weights = [("地铁+步行", 50), ("公共交通", 28), ("打车", 18), ("自驾", 4)]
    else:
        weights = [("地铁+步行", 34), ("公共交通", 30), ("打车", 24), ("自驾", 12)]
    return weighted_choice(rng, weights)


def choose_budget_text(amount: int | None) -> str:
    """生成自然语言预算描述。"""
    if amount is None:
        return "预算没有特别限制"
    return f"总预算控制在{amount}元左右"


def companion_phrase(rng: random.Random, companion_type: str) -> str:
    """同行类型转自然语气。"""
    if companion_type == "family_with_children":
        age = rng.choice([3, 4, 5, 6, 7, 8, 9, 10])
        return rng.choice([f"带{age}岁孩子", f"一家三口带{age}岁小朋友", f"带娃出行，孩子{age}岁"])
    if companion_type == "friends":
        return rng.choice(["和朋友一起", "几个朋友出行", "和同学/朋友一起"])
    if companion_type == "couple":
        return rng.choice(["情侣两个人", "和对象一起", "夫妻两个人"])
    if companion_type == "solo":
        return rng.choice(["一个人出行", "独自旅行", "单人自由行"])
    if companion_type == "family_with_elders":
        return rng.choice(["带父母出行", "陪长辈一起", "和爸妈一起"])
    if companion_type == "family_mixed":
        return rng.choice(["三代同游", "带父母和孩子一起", "一家老小一起出行"])
    if companion_type == "business":
        return rng.choice(["出差顺便玩一天", "商务行程后想轻松逛逛", "和同事短途出行"])
    return rng.choice(["这次想轻松玩几天", "第一次认真规划这个城市", "想安排一个舒服点的短途旅行"])


def build_controlled_free_text(
    rng: random.Random,
    companion_type: str,
    budget_amount: int | None,
    diet: str,
    pace: str,
    avoid: list[str],
) -> str:
    """不用强模型，直接生成足够自然的请求补充。"""
    parts = [
        companion_phrase(rng, companion_type),
        choose_budget_text(budget_amount),
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
    target_budget = target_budget_choice(index, args)
    if target_budget:
        budget_level, target_strictness = target_budget
    else:
        budget_level = weighted_choice(rng, BUDGET_WEIGHTS)
        target_strictness = None
    pace = weighted_choice(rng, PACE_WEIGHTS)
    diet = weighted_choice(rng, DIET_WEIGHTS)
    party = build_party_info(rng, companion_type)
    accommodation = choose_controlled_accommodation(rng, companion_type, budget_level)
    transportation = choose_controlled_transportation(rng, companion_type, city)
    budget_amount = choose_budget_amount(
        rng,
        budget_level,
        party["total"],
        travel_days,
        accommodation,
        transportation,
        city_tier,
        companion_type,
    )
    budget_constraint = build_budget_constraint(
        rng,
        budget_level,
        budget_amount,
        strictness=target_strictness,
    )
    budget_constraint = normalize_budget_strictness(budget_constraint, args)
    start = choose_controlled_start_date(rng, travel_days, args.date_mode)

    themes = sample_many_weighted(rng, THEME_POOL, 2, 4)
    if companion_type == "family_with_children" and "亲子" not in themes:
        themes = ["亲子"] + themes[:3]
    if companion_type == "family_with_elders" and "老人友好" not in themes:
        themes = ["老人友好"] + themes[:3]
    if companion_type == "family_mixed":
        themes = unique_list(["亲子", "老人友好"] + themes)[:4]
    if diet in {"清真", "素食"} and diet not in themes:
        themes = themes[:3] + [diet]

    avoid_pool = ["人挤人的网红店", "过度商业化景点", "太累的路线", "太偏远的景点", "高价餐厅", "购物团"]
    avoid = rng.sample(avoid_pool, k=rng.choice([1, 1, 2, 2, 3])) if rng.random() < 0.68 else []
    free_text = build_controlled_free_text(rng, companion_type, budget_amount, diet, pace, avoid)

    preferences = themes[:4]
    preference_spec = build_preference_control_spec(preferences, free_text, party, pace, diet, avoid)

    return {
        "request_id": format_request_id(index),
        "city": city,
        "start_date": start.isoformat(),
        "end_date": (start + timedelta(days=travel_days - 1)).isoformat(),
        "travel_days": travel_days,
        "transportation": transportation,
        "accommodation": accommodation,
        "preferences": preferences,
        "free_text_input": free_text,
        "party": party,
        "budget_constraint": budget_constraint,
        "source": "controlled",
        "control_spec": {
            "companion_type": companion_type,
            "city_tier": city_tier,
            "budget_level": budget_level,
            "budget_amount": budget_amount,
            "budget_strictness": budget_constraint["strictness"],
            "pace": pace,
            "diet": diet,
            "avoid": avoid,
            **preference_spec,
        },
    }


def build_budget_supplement_free_text(
    rng: random.Random,
    companion_type: str,
    budget_amount: int,
    diet: str,
    pace: str,
    avoid: list[str],
    budget_level: str,
    strictness: str,
) -> str:
    """预算补数的自然语言表达。"""
    companion = companion_phrase(rng, companion_type)
    pace_text = {
        "慢节奏": "节奏舒服一点，不要赶路",
        "适中节奏": "节奏适中，体验和效率都兼顾",
        "紧凑高效": "可以紧凑一些，但不要牺牲体验质量",
        "自由活动多": "希望留一点自由活动时间",
    }.get(pace, "节奏适中")
    diet_text = "" if diet == "无" else f"，餐饮注意{diet}"
    avoid_text = f"，尽量避开{'、'.join(avoid)}" if avoid else ""
    if strictness == "soft":
        budget_text = (
            f"总预算大约{budget_amount}元，可以在预算上下小幅浮动，"
            "希望尽量用足预算，酒店、餐饮和体验都安排得有品质一些，不要做成低配省钱方案"
        )
    else:
        budget_text = f"总预算控制在{budget_amount}元以内，优先保证不超预算，同时别安排得太寒酸"

    upgrade_text = ""
    if budget_level in {"comfortable", "premium", "luxury"}:
        upgrade_text = "，可以考虑品质餐厅、付费体验或更好的住宿"
    return f"{companion}，{budget_text}，{pace_text}{upgrade_text}{diet_text}{avoid_text}。"


def generate_budget_supplement_request(index: int, args: argparse.Namespace) -> dict[str, Any]:
    """生成预算补充样本请求。"""
    rng = random.Random(args.seed + index)
    target_budget = target_budget_choice(index, args)
    if target_budget:
        budget_level, strictness = target_budget
    else:
        budget_level, strictness = weighted_block_choice(
            index,
            args.seed,
            SUPPLEMENT_BUDGET_STRICTNESS_WEIGHTS,
            "budget_strictness",
        )
    companion_type = weighted_block_choice(index, args.seed, SUPPLEMENT_COMPANION_WEIGHTS, "companion")
    travel_days = weighted_block_choice(index, args.seed, SUPPLEMENT_TRAVEL_DAYS_WEIGHTS, "travel_days")
    city_tier = weighted_choice(rng, CITY_TIER_WEIGHTS)
    city = rng.choice(CITY_TIERS[city_tier])
    pace = weighted_choice(rng, SUPPLEMENT_PACE_WEIGHTS)
    diet = weighted_choice(rng, DIET_WEIGHTS)
    party = build_party_info(rng, companion_type)
    accommodation = choose_supplement_accommodation(rng, companion_type, budget_level)
    transportation = choose_controlled_transportation(rng, companion_type, city)
    budget_amount = choose_budget_amount(
        rng,
        budget_level,
        party["total"],
        travel_days,
        accommodation,
        transportation,
        city_tier,
        companion_type,
        per_person_day_budgets=SUPPLEMENT_PER_PERSON_DAY_BUDGETS,
        companion_budget_factors=SUPPLEMENT_COMPANION_BUDGET_FACTORS,
        party_budget_mode="group_discount",
    )
    budget_constraint = build_budget_constraint(rng, budget_level, budget_amount, strictness=strictness)
    start = choose_controlled_start_date(rng, travel_days, args.date_mode)

    themes = sample_many_weighted(rng, THEME_POOL, 2, 4)
    if budget_level in {"comfortable", "premium", "luxury"} and strictness == "soft":
        themes = unique_list(["美食", "特色餐厅", "休闲慢游"] + themes)[:4]
    if companion_type == "family_with_children" and "亲子" not in themes:
        themes = ["亲子"] + themes[:3]
    if companion_type == "family_with_elders" and "老人友好" not in themes:
        themes = ["老人友好"] + themes[:3]
    if companion_type == "family_mixed":
        themes = unique_list(["亲子", "老人友好"] + themes)[:4]
    if companion_type == "business":
        themes = unique_list(["城市地标", "特色餐厅"] + themes)[:4]
    if diet in {"清真", "素食"} and diet not in themes:
        themes = themes[:3] + [diet]

    avoid_pool = ["人挤人的网红店", "过度商业化景点", "太累的路线", "太偏远的景点", "购物团"]
    if budget_level in {"limited", "standard"} or strictness == "hard":
        avoid_pool.append("高价餐厅")
    avoid = rng.sample(avoid_pool, k=rng.choice([1, 1, 2, 2, 3])) if rng.random() < 0.62 else []
    if strictness == "soft" and budget_level in {"comfortable", "premium", "luxury"}:
        avoid = [item for item in avoid if item != "高价餐厅"]
    free_text = build_budget_supplement_free_text(
        rng,
        companion_type,
        budget_amount,
        diet,
        pace,
        avoid,
        budget_level,
        strictness,
    )

    preferences = themes[:4]
    preference_spec = build_preference_control_spec(preferences, free_text, party, pace, diet, avoid)
    budget_fit_policy_override = dict(SUPPLEMENT_SOFT_BUDGET_POLICY) if strictness == "soft" else None

    control_spec = {
        "companion_type": companion_type,
        "city_tier": city_tier,
        "budget_level": budget_level,
        "budget_amount": budget_amount,
        "budget_strictness": strictness,
        "pace": pace,
        "diet": diet,
        "avoid": avoid,
        "supplement_version": SUPPLEMENT_VERSION,
        "supplement_focus": "budget_selection_fit",
        **preference_spec,
    }
    if budget_fit_policy_override:
        control_spec["budget_fit_policy_override"] = budget_fit_policy_override

    return {
        "request_id": format_request_id(index),
        "city": city,
        "start_date": start.isoformat(),
        "end_date": (start + timedelta(days=travel_days - 1)).isoformat(),
        "travel_days": travel_days,
        "transportation": transportation,
        "accommodation": accommodation,
        "preferences": preferences,
        "free_text_input": free_text,
        "party": party,
        "budget_constraint": budget_constraint,
        "source": "budget_supplement",
        "control_spec": control_spec,
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
        companion_type = weighted_choice(rng, COMPANION_WEIGHTS)
        party = build_party_info(rng, companion_type)
        budget_level = weighted_choice(rng, BUDGET_WEIGHTS)
        travel_days = rng.choice([2, 3, 3, 4, 4, 5])
        accommodation = choose_controlled_accommodation(rng, companion_type, budget_level)
        city = rng.choice(DEFAULT_CITIES)
        transportation = rng.choice(TRANSPORTATION_OPTIONS)
        budget_amount = choose_budget_amount(
            rng,
            budget_level,
            party["total"],
            travel_days,
            accommodation,
            transportation,
            infer_city_tier(city),
            companion_type,
        )
        budget_constraint = build_budget_constraint(rng, budget_level, budget_amount)
        start = choose_start_date(rng, travel_days, date_mode)
        prefs = list(scenario["preferences"])
        rng.shuffle(prefs)
        free_text = (
            f"{companion_phrase(rng, companion_type)}，{scenario['free_text']} "
            f"总预算控制在{budget_amount}元左右，"
            f"尽量避开：{'、'.join(scenario['avoid'])}。"
        )
        diet = infer_diet_label(prefs, free_text)
        pace = "慢节奏" if any(marker in free_text for marker in ["慢", "轻松", "不累", "少折腾"]) else "适中节奏"
        preferences = prefs[: rng.choice([2, 3])]
        preference_spec = build_preference_control_spec(
            preferences,
            free_text,
            party,
            pace,
            diet,
            list(scenario["avoid"]),
        )
        requests.append(
            {
                "request_id": format_request_id(index),
                "city": city,
                "start_date": start.isoformat(),
                "end_date": (start + timedelta(days=travel_days - 1)).isoformat(),
                "travel_days": travel_days,
                "transportation": transportation,
                "accommodation": accommodation,
                "preferences": preferences,
                "free_text_input": free_text,
                "party": party,
                "budget_constraint": budget_constraint,
                "source": "template",
                "control_spec": {
                    "companion_type": companion_type,
                    "budget_level": budget_level,
                    "budget_amount": budget_amount,
                    "budget_strictness": budget_constraint["strictness"],
                    "diet": diet,
                    "avoid": list(scenario["avoid"]),
                    **preference_spec,
                },
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
    data_gen_provider: str | None = None,
    data_gen_model: str | None = None,
) -> list[dict[str, Any]]:
    """用强模型模拟真实用户 TripRequest。"""
    print(
        f"开始用强模型生成模拟用户请求: count={count}, batch_size={batch_size}",
        flush=True,
    )
    llm = DataGenLLM(provider=data_gen_provider, model=data_gen_model)
    rows: list[dict[str, Any]] = []
    current = start_index
    active_batch_size = batch_size
    while len(rows) < count:
        need = min(active_batch_size, count - len(rows))
        batch_no = len(rows) // max(active_batch_size, 1) + 1
        print(
            f"生成用户请求 batch {batch_no}: need={need}, start_id={format_request_id(current)}",
            flush=True,
        )
        system_prompt = """你是旅行产品的真实用户请求模拟器。只能输出 JSON 数组，不要输出 Markdown。"""
        user_prompt = f"""请生成 {need} 条像真实用户填写的旅行规划请求。

当前日期: {date.today().isoformat()}
随机种子: {seed}
request_id 从 {format_request_id(current)} 开始递增。

每条必须包含:
- request_id: 字符串
- city: 中国旅游城市
- start_date: YYYY-MM-DD，必须是当前日期之后，混合近几天和未来1-4个月
- travel_days: 2到5天
- transportation: 公共交通/打车/自驾/地铁+步行 之一
- accommodation: 经济型酒店/舒适型酒店/高端酒店/民宿/亲子酒店 之一
- preferences: 2到4个中文正向偏好标签；不要把过敏、忌口、避雷项放进preferences
- party: 对象，包含 adults/children/elders/total/companion_type，total必须等于分项之和
- budget_constraint: 对象，scope固定为total，currency固定为CNY，amount为整趟总预算或null，budget_level为limited/standard/comfortable/premium/luxury之一，strictness为hard/soft/none之一
- free_text_input: 一句真实口吻的额外要求，可以包含总预算、同行人、饮食忌口、节奏、避雷项

要求:
1. 请求要像真实用户，不要像数据模板。
2. 需要覆盖亲子、老人、独行、情侣、朋友、商务、预算有限、饮食忌口、过敏、休闲、特种兵、摄影、美食等场景。
3. budget_constraint.amount 必须使用整百数，并和 budget_level、人数、天数、住宿类型大致匹配；limited 是预算有限，standard 是普通经济实用，comfortable 是舒适宽裕，premium/luxury 才能给明显高预算。不要给 standard 请求生成明显偏高的总预算。
4. end_date 可以省略，我会按 travel_days 自动计算。
5. 不要输出解释，只输出 JSON 数组。
"""
        batch_items: list[dict[str, Any]] = []
        last_error: Exception | None = None
        for attempt in range(1, retries + 1):
            try:
                result = llm.complete_json(
                    system_prompt,
                    user_prompt,
                    temperature=0.8,
                    max_tokens=max_tokens,
                    metadata={
                        "script": "generate_sft_data.py",
                        "call_type": "request_batch",
                        "batch_no": batch_no,
                        "need": need,
                        "start_request_id": format_request_id(current),
                    },
                )
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
            request_id = format_request_id(current)
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
    request_id = format_request_id(index)
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
- preferences: 2到4个中文正向偏好标签；不要把过敏、忌口、避雷项放进preferences
- party: 对象，包含 adults/children/elders/total/companion_type，total必须等于分项之和；companion_type使用solo/couple/friends/family_with_children/family_with_elders/family_mixed/business/other之一
- budget_constraint: 对象，scope固定为total，currency固定为CNY，amount为整趟总预算或null，budget_level为limited/standard/comfortable/premium/luxury之一，strictness为hard/soft/none之一
- free_text_input: 一句真实口吻的额外要求，可以包含总预算、同行人、饮食忌口、节奏、避雷项

要求:
1. 请求要像真实用户，不要像数据模板。
2. 覆盖亲子、老人、独行、情侣、朋友、商务、预算有限、饮食忌口、过敏、休闲、特种兵、摄影、美食等不同场景。
3. budget_constraint.amount 必须使用整百数，并和 budget_level、人数、天数、住宿类型大致匹配；limited 是预算有限，standard 是普通经济实用，comfortable 是舒适宽裕，premium/luxury 才能给明显高预算。不要给 standard 请求生成明显偏高的总预算。
4. end_date 可以省略，我会按 travel_days 自动计算。
5. 不要输出解释，只输出 JSON 对象。
"""
    llm = get_worker_llm(args)
    last_error: Exception | None = None
    for attempt in range(1, args.request_generation_retries + 1):
        try:
            result = llm.complete_json(
                system_prompt,
                user_prompt,
                temperature=0.8,
                max_tokens=args.request_max_tokens,
                metadata={
                    "script": "generate_sft_data.py",
                    "call_type": "request_single",
                    "request_id": request_id,
                    "attempt": attempt,
                },
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
    if args.request_source == "budget_supplement":
        return generate_budget_supplement_request(index, args)
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
    """把 SFT 数据集注册到 dataset_info.json。"""
    if not REGISTER_LLAMAFACTORY_DATASET:
        return
    if DATASET_INFO_PATH.exists():
        data = json.loads(DATASET_INFO_PATH.read_text(encoding="utf-8"))
    else:
        data = {}

    data["trip_sft_train"] = {"file_name": llamafactory_file_name(LLAMAFACTORY_TRAIN_PATH)}
    data["trip_sft_val"] = {"file_name": llamafactory_file_name(LLAMAFACTORY_VAL_PATH)}
    write_json(DATASET_INFO_PATH, data)


def llamafactory_file_name(path: Path) -> str:
    """Return the dataset_info file_name relative to the LLaMAFactory data root."""
    try:
        return path.relative_to(LLAMAFACTORY_DIR).as_posix()
    except ValueError:
        return path.name


def configure_output_paths(output_dir: Path | None) -> None:
    """可选把本轮输出重定向到明确 run 目录，避免污染旧 SFT 入口。"""
    global RAW_RECORDS_PATH, ERRORS_PATH, REQUESTS_PATH
    global LLAMAFACTORY_TRAIN_PATH, LLAMAFACTORY_VAL_PATH, REGISTER_LLAMAFACTORY_DATASET

    if output_dir is None:
        REGISTER_LLAMAFACTORY_DATASET = True
        return

    output_dir = output_dir.resolve()
    os.environ.setdefault("DATA_GEN_USAGE_LOG", str(output_dir / "llm_usage.jsonl"))
    RAW_RECORDS_PATH = output_dir / "records.jsonl"
    ERRORS_PATH = output_dir / "errors.jsonl"
    REQUESTS_PATH = output_dir / "requests.jsonl"
    LLAMAFACTORY_TRAIN_PATH = output_dir / "llamafactory_train.json"
    LLAMAFACTORY_VAL_PATH = output_dir / "llamafactory_val.json"
    REGISTER_LLAMAFACTORY_DATASET = False


def load_existing_record_ids(path: Path) -> set[str]:
    """读取已成功样本 ID，用于断点续跑。"""
    return {row.get("record_id", "") for row in read_jsonl(path)}


def usable_lunch_dinner_food_names(planner_context: dict[str, Any]) -> list[str]:
    """抽取可用于 lunch/dinner 的 food_pois 名称，排除明显风险候选。"""
    names = []
    for row in planner_context.get("tool_snapshot", {}).get("food_pois") or []:
        name = str(row.get("name") or "").strip()
        if not name:
            continue
        if row.get("avoid_risk_keywords"):
            continue
        roles = {str(role or "").strip().lower() for role in row.get("meal_roles") or []}
        if roles and roles.isdisjoint(LUNCH_DINNER_MEAL_TYPES):
            continue
        names.append(name)
    return names


def validate_meal_structure_and_diversity(
    trip_plan: TripPlan,
    request: TripRequest,
    planner_context: dict[str, Any],
) -> None:
    """训练数据硬拦餐饮占位、未 grounding 和完全同名重复。"""
    food_names = usable_lunch_dinner_food_names(planner_context)
    usable_exact_count = len({name for name in food_names if name})
    required_lunch_dinner_count = max(0, request.travel_days * 2)
    selected_entries = []

    for day_index, day in enumerate(trip_plan.days):
        meal_types = {str(meal.type or "").strip().lower() for meal in day.meals}
        missing = {"breakfast", "lunch", "dinner"} - meal_types
        if missing:
            raise ValueError(f"第{day_index + 1}天缺少餐次: {sorted(missing)}")

        day_lunch_dinner = []
        for meal in day.meals:
            meal_type = str(meal.type or "").strip().lower()
            meal_name = str(meal.name or "").strip()
            if meal_type == "breakfast" and not is_lodging_breakfast_meal(meal_name, meal.type):
                validate_meal_cost_hint(meal_name, int(meal.estimated_cost or 0), planner_context, meal_label="早餐")
            if meal_type not in LUNCH_DINNER_MEAL_TYPES:
                continue
            entry = {
                "day": day_index + 1,
                "type": meal_type,
                "name": meal_name,
                "cost": int(meal.estimated_cost or 0),
            }
            day_lunch_dinner.append(entry)
            selected_entries.append(entry)

        if len(day_lunch_dinner) < 2:
            raise ValueError(f"第{day_index + 1}天必须同时包含lunch和dinner")
        validate_same_day_meal_diversity(day_lunch_dinner)

    exact_unique_required = usable_exact_count >= required_lunch_dinner_count
    for left_index, left in enumerate(selected_entries):
        for right in selected_entries[left_index + 1 :]:
            if exact_unique_required and left["name"] and left["name"] == right["name"]:
                raise ValueError(
                    "food_pois候选充足时lunch/dinner餐厅不能重复: "
                    f"第{left['day']}天{left['type']}={left['name']}, "
                    f"第{right['day']}天{right['type']}={right['name']}"
                )

    for entry in selected_entries:
        validate_meal_cost_hint(str(entry["name"]), int(entry["cost"]), planner_context)


def validate_same_day_meal_diversity(entries: list[dict[str, str | int]]) -> None:
    """同一天午晚餐必须是不同真实餐厅。"""
    for left_index, left in enumerate(entries):
        for right in entries[left_index + 1 :]:
            if left["name"] and left["name"] == right["name"]:
                raise ValueError(
                    "同一天lunch/dinner餐厅不能重复: "
                    f"第{left['day']}天{left['type']}={left['name']}, {right['type']}={right['name']}"
                )


def validate_training_plan(trip_plan: TripPlan, request: TripRequest, planner_context: dict[str, Any]) -> None:
    """SFT 训练样本硬校验。

    线上可以软降级；训练数据不能把预算账本、酒店房间数和候选价格复制错误教给模型。
    """
    if trip_plan.budget is None:
        raise ValueError("缺少budget")

    budget = trip_plan.budget
    if budget.total != (
        budget.total_attractions
        + budget.total_hotels
        + budget.total_meals
        + budget.total_transportation
    ):
        raise ValueError("budget.total与四个分项加总不一致")

    expected_hotel_total = 0
    expected_attraction_total = 0
    expected_meal_total = 0
    lodging_nights = int(planner_context.get("lodging_policy", {}).get("default_lodging_nights") or 0)
    party_total = max(request.party.total, 1)
    room_count = max(1, math.ceil(party_total / 2))
    lodging_hotel_name = ""
    lodging_hotel_display = ""

    for index, day in enumerate(trip_plan.days):
        if day.accommodation != request.accommodation:
            raise ValueError(f"第{index + 1}天accommodation必须固定为用户住宿类型: {day.accommodation}")
        if not (1 <= len(day.attractions) <= 3):
            raise ValueError(f"第{index + 1}天景点数必须为1-3个: {len(day.attractions)}")
        if index < lodging_nights and day.hotel is None:
            raise ValueError(f"第{index + 1}天属于住宿晚数范围，hotel不能为空")
        if day.hotel:
            current_hotel_name = normalize_poi_name(day.hotel.name)
            if not current_hotel_name:
                raise ValueError(f"第{index + 1}天hotel.name不能为空")
            if not lodging_hotel_name:
                lodging_hotel_name = current_hotel_name
                lodging_hotel_display = day.hotel.name
            elif current_hotel_name != lodging_hotel_name:
                raise ValueError(
                    "中间住宿日酒店不能变化: "
                    f"第1晚={lodging_hotel_display}, 第{index + 1}天={day.hotel.name}"
                )
            expected_hotel_total += int(day.hotel.estimated_cost or 0) * room_count
            validate_hotel_cost_hint(day.hotel.name, int(day.hotel.estimated_cost or 0), planner_context)

        for attraction in day.attractions:
            expected_attraction_total += int(attraction.ticket_price or 0) * party_total
            validate_attraction_ticket_hint(attraction.name, int(attraction.ticket_price or 0), planner_context)

        for meal in day.meals:
            expected_meal_total += int(meal.estimated_cost or 0) * party_total

    if budget.total_hotels != expected_hotel_total:
        raise ValueError(
            f"budget.total_hotels未按两人一间汇总酒店费用: rooms={room_count}, expected={expected_hotel_total}, got={budget.total_hotels}"
        )
    if budget.total_attractions != expected_attraction_total:
        raise ValueError(
            f"budget.total_attractions未按party.total汇总门票: expected={expected_attraction_total}, got={budget.total_attractions}"
        )
    if budget.total_meals != expected_meal_total:
        raise ValueError(f"budget.total_meals未按party.total汇总人均餐费: expected={expected_meal_total}, got={budget.total_meals}")
    validate_meal_structure_and_diversity(trip_plan, request, planner_context)
    validate_budget_fit_policy(budget.total, request, planner_context)
    validate_budget_narrative(trip_plan, request)


def recompute_budget(trip_plan: TripPlan, request: TripRequest) -> None:
    """按当前口径重算 budget，避免把强模型算术错误写入 SFT 数据。"""
    party_total = max(request.party.total, 1)
    room_count = max(1, math.ceil(party_total / 2))
    total_hotels = 0
    total_attractions = 0
    total_meals = 0

    for day in trip_plan.days:
        if day.hotel:
            total_hotels += int(day.hotel.estimated_cost or 0) * room_count
        for attraction in day.attractions:
            total_attractions += int(attraction.ticket_price or 0) * party_total
        for meal in day.meals:
            total_meals += int(meal.estimated_cost or 0) * party_total

    original_budget = trip_plan.budget or Budget()
    total_transportation = max(0, int(original_budget.total_transportation or 0))
    trip_plan.budget = Budget(
        total_attractions=total_attractions,
        total_hotels=total_hotels,
        total_meals=total_meals,
        total_transportation=total_transportation,
        total=total_attractions + total_hotels + total_meals + total_transportation,
    )


def validate_budget_fit_policy(total: int, request: TripRequest, planner_context: dict[str, Any]) -> None:
    """训练数据要求预算不仅不超，还要和预算档位匹配。"""
    policy = (
        planner_context.get("planner_constraints", {})
        .get("budget_fit_policy")
        or budget_fit_policy(request)
    )
    if not policy.get("enabled"):
        return

    amount = int(policy.get("amount") or 0)
    min_ratio = float(policy.get("target_min_ratio") or 0)
    max_ratio = float(policy.get("target_max_ratio") or 0)
    strictness = str(policy.get("strictness") or "")

    validation_min_margin = float(policy.get("validation_min_ratio_margin", BUDGET_VALIDATION_MIN_RATIO_MARGIN))
    validation_max_margin = float(policy.get("validation_max_ratio_margin", BUDGET_VALIDATION_MAX_RATIO_MARGIN))
    validation_hard_max_margin = float(
        policy.get("validation_hard_max_ratio_margin", BUDGET_VALIDATION_HARD_MAX_RATIO_MARGIN)
    )
    validation_min_ratio = max(0.0, min_ratio - validation_min_margin)
    validation_max_ratio = max_ratio
    if strictness == "hard":
        validation_max_ratio += validation_hard_max_margin
    else:
        validation_max_ratio += validation_max_margin

    min_total = int(round(amount * validation_min_ratio / 100.0) * 100)
    max_total = int(round(amount * validation_max_ratio / 100.0) * 100)
    if total < min_total:
        raise ValueError(
            "budget.total明显低于预算档位目标区间: "
            f"total={total}, min={min_total}, target_min={policy.get('target_min_total')}, amount={amount}, "
            f"level={policy.get('budget_level')}, strictness={policy.get('strictness')}"
        )
    if max_total > 0 and total > max_total:
        raise ValueError(
            "budget.total超出预算档位目标区间: "
            f"total={total}, max={max_total}, target_max={policy.get('target_max_total')}, amount={amount}, "
            f"level={policy.get('budget_level')}, strictness={policy.get('strictness')}"
        )


def validate_budget_narrative(trip_plan: TripPlan, request: TripRequest) -> None:
    """overall_suggestions 不能口头报一个和 budget.total 冲突的总费用。"""
    if not trip_plan.budget:
        return

    text = str(trip_plan.overall_suggestions or "")
    if not text:
        return

    budget_total = int(trip_plan.budget.total or 0)
    request_amount = int(getattr(request.budget_constraint, "amount", 0) or 0) if request.budget_constraint else 0
    allowed_amounts = [budget_total]
    if request_amount > 0:
        allowed_amounts.append(request_amount)

    for match in BUDGET_NARRATIVE_AMOUNT_RE.finditer(text):
        value = int(match.group(1))
        if any(abs(value - allowed) <= 100 for allowed in allowed_amounts):
            continue
        raise ValueError(
            "overall_suggestions预算金额与budget.total冲突: "
            f"mentioned={value}, budget_total={budget_total}, request_amount={request_amount}"
        )

    if request_amount > 0 and budget_total > request_amount:
        over_budget_ok = re.search(rf"(?:超出|超过)[^，。；;]{{0,12}}{request_amount}\s*元", text)
        says_under_budget = re.search(
            rf"(?:低于|未超过|不超过|控制在|在)[^，。；;]{{0,18}}{request_amount}\s*元|"
            r"低于预算|未超过预算|不超过预算|预算内|低于.*?预算上限",
            text,
        )
        if says_under_budget and not over_budget_ok:
            raise ValueError(
                "overall_suggestions预算超支叙述错误: "
                f"budget_total={budget_total}, request_amount={request_amount}"
            )


def validate_hotel_cost_hint(name: str, value: int, planner_context: dict[str, Any]) -> None:
    """酒店单晚价格必须复制候选 estimated_cost_hint。"""
    hotels = planner_context.get("tool_snapshot", {}).get("hotel_pois") or []
    hint = find_candidate_hint(name, hotels, "estimated_cost_hint")
    if hint is None:
        raise ValueError(f"酒店未命中hotel_pois候选: {name}")
    if value != int(hint):
        raise ValueError(f"酒店价格未复制hint: {name}, expected={int(hint)}, got={value}")


def validate_attraction_ticket_hint(name: str, value: int, planner_context: dict[str, Any]) -> None:
    """景点门票必须复制候选 ticket_price_hint。"""
    snapshot = planner_context.get("tool_snapshot", {})
    candidates = (
        (snapshot.get("classic_pois") or [])
        + (snapshot.get("preference_pois") or [])
        + (snapshot.get("scenic_pois") or [])
        + (snapshot.get("experience_pois") or [])
    )
    hint = find_candidate_hint(name, candidates, "ticket_price_hint")
    if hint is None:
        raise ValueError(f"景点未命中工具候选: {name}")
    if value != int(hint):
        raise ValueError(f"景点门票未复制hint: {name}, expected={int(hint)}, got={value}")


def validate_meal_cost_hint(
    name: str,
    value: int,
    planner_context: dict[str, Any],
    meal_label: str = "午晚餐",
) -> None:
    """餐饮必须来自 food_pois，并复制 meal_cost_hint。"""
    foods = planner_context.get("tool_snapshot", {}).get("food_pois") or []
    hint = find_exact_candidate_hint(name, foods, "meal_cost_hint")
    if hint is None:
        raise ValueError(f"{meal_label}未命中food_pois候选: {name}")
    if value != int(hint):
        raise ValueError(f"{meal_label}价格未复制hint: {name}, expected={int(hint)}, got={value}")


def find_exact_candidate_hint(name: str, candidates: list[dict[str, Any]], hint_key: str) -> Any:
    """餐饮必须按 food_pois.name 原始全名精确匹配。"""
    target = str(name or "").strip()
    for item in candidates:
        if str(item.get("name") or "").strip() == target:
            return item.get(hint_key)
    return None


def find_candidate_hint(name: str, candidates: list[dict[str, Any]], hint_key: str) -> Any:
    """按宽松名称匹配查候选 hint。"""
    named_candidates = [item for item in candidates if item.get("name")]
    names = [item.get("name", "") for item in named_candidates]
    if not name_in_candidates(name, names):
        return None

    normalized_name = normalize_poi_name(name)
    exact_matches = [
        item
        for item in named_candidates
        if normalize_poi_name(item.get("name", "")) == normalized_name
    ]
    if exact_matches:
        return exact_matches[0].get(hint_key)

    # 宽松匹配容易出现“滇池海埂公园”先命中“滇池”的情况；
    # 长名称通常更接近模型实际选择，优先返回更具体的候选。
    for item in sorted(named_candidates, key=lambda row: len(normalize_poi_name(row.get("name", ""))), reverse=True):
        item_name = item.get("name", "")
        if item_name and name_in_candidates(name, [item_name]):
            return item.get(hint_key)
    return None


def budget_context_gate_audit(request: TripRequest, planner_context: dict[str, Any]) -> dict[str, Any]:
    """估算当前候选池的预算上限，用于补数前置过滤。

    这里不评判模型最终输出，只判断“如果模型尽量选高价候选”，上下文是否有
    机会撑到预算利用型样本需要的区间。预算精算仍由后处理/评测逻辑负责。
    """
    snapshot = planner_context.get("tool_snapshot") or {}
    party_total = max(int(request.party.total or 1), 1)
    travel_days = max(int(request.travel_days or 1), 1)
    rooms = math.ceil(party_total / 2)
    lodging_nights = int(
        (planner_context.get("lodging_policy") or {}).get("default_lodging_nights")
        or max(travel_days - 1, 0)
    )
    amount = int((request.budget_constraint.amount or 0) if request.budget_constraint else 0)
    policy = (planner_context.get("planner_constraints") or {}).get("budget_fit_policy") or {}

    hotels = snapshot.get("hotel_pois") or []
    foods = snapshot.get("food_pois") or []
    scenic = snapshot.get("scenic_pois") or []
    experience = snapshot.get("experience_pois") or []
    attraction_candidates = dedupe_context_candidates_by_name(scenic + experience)

    lunch_dinner_foods = [row for row in foods if not is_budget_gate_breakfast_only(row)]
    breakfast_foods = [
        row
        for row in foods
        if "breakfast" in {str(role).strip().lower() for role in (row.get("meal_roles") or [])}
    ]

    hotel_prices = numeric_context_values(hotels, "estimated_cost_hint")
    lunch_dinner_prices = numeric_context_values(lunch_dinner_foods, "meal_cost_hint")
    breakfast_prices = numeric_context_values(breakfast_foods, "meal_cost_hint")
    attraction_prices = numeric_context_values(attraction_candidates, "ticket_price_hint")

    hotel_high = int(max(hotel_prices or [0]) * lodging_nights * rooms)
    breakfast_high = int(max(breakfast_prices or [25]) * travel_days * party_total)
    meals_high = int(sum_top_context_values(lunch_dinner_prices, travel_days * 2) * party_total + breakfast_high)
    attractions_high = int(sum_top_context_values(attraction_prices, travel_days * 2) * party_total)
    transportation_high = estimate_budget_gate_transportation_total(request)
    high_total = hotel_high + meals_high + attractions_high + transportation_high

    target_min = int(policy.get("target_min_total") or round(amount * 0.95))
    target_max = int(policy.get("target_max_total") or round(amount * 1.05))
    target_mid = int(round((target_min + target_max) / 2)) if target_min and target_max else amount

    return {
        "budget_amount": amount,
        "budget_level": request.budget_constraint.budget_level if request.budget_constraint else "",
        "strictness": request.budget_constraint.strictness if request.budget_constraint else "",
        "travel_days": travel_days,
        "party_total": party_total,
        "rooms": rooms,
        "lodging_nights": lodging_nights,
        "target_min_total": target_min,
        "target_max_total": target_max,
        "target_mid_total": target_mid,
        "estimated_high_budget": {
            "total": high_total,
            "hotels": hotel_high,
            "meals": meals_high,
            "attractions": attractions_high,
            "transportation": transportation_high,
        },
        "high_budget_ratio": round(high_total / amount, 4) if amount else 0,
        "can_reach_target_min": high_total >= target_min if target_min else False,
        "can_reach_target_mid": high_total >= target_mid if target_mid else False,
        "tool_counts": {
            "hotel_pois": len(hotels),
            "food_pois": len(foods),
            "scenic_pois": len(scenic),
            "experience_pois": len(experience),
        },
        "max_hint": {
            "hotel": int(max(hotel_prices or [0])),
            "meal": int(max(numeric_context_values(foods, "meal_cost_hint") or [0])),
            "attraction": int(max(attraction_prices or [0])),
        },
    }


def maybe_validate_budget_context_gate(
    request: TripRequest,
    planner_context: dict[str, Any],
    args: argparse.Namespace,
) -> dict[str, Any] | None:
    """强模型前用候选池上限过滤预算不可达样本。"""
    min_ratio = float(getattr(args, "budget_context_min_ratio", 0.0) or 0.0)
    if min_ratio <= 0:
        return None

    policy = (planner_context.get("planner_constraints") or {}).get("budget_fit_policy") or {}
    if not policy.get("enabled"):
        return None

    audit = budget_context_gate_audit(request, planner_context)
    ratio = float(audit["high_budget_ratio"])
    if ratio + 1e-9 < min_ratio:
        high_budget = audit["estimated_high_budget"]
        request_source = str(getattr(args, "request_source", "unknown"))
        raise BudgetContextUnreachableError(
            f"{request_source}上下文预算不可达: "
            f"ratio={ratio:.3f} < {min_ratio:.3f}, "
            f"amount={audit['budget_amount']}, high_total={high_budget['total']}, "
            f"hotel={high_budget['hotels']}, meals={high_budget['meals']}, "
            f"attractions={high_budget['attractions']}, transport={high_budget['transportation']}"
        )
    return audit


def numeric_context_values(rows: list[dict[str, Any]], key: str) -> list[float]:
    values = []
    for row in rows:
        value = as_context_number(row.get(key))
        if value is not None:
            values.append(value)
    return values


def as_context_number(value: Any) -> float | None:
    if value in (None, "", []):
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def sum_top_context_values(values: list[float], count: int) -> int:
    if count <= 0:
        return 0
    return int(sum(sorted(values, reverse=True)[:count]))


def dedupe_context_candidates_by_name(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    seen = set()
    results = []
    for row in rows:
        key = normalize_poi_name(str(row.get("name") or ""))
        if not key or key in seen:
            continue
        seen.add(key)
        results.append(row)
    return results


def is_budget_gate_breakfast_only(row: dict[str, Any]) -> bool:
    roles = {str(role).strip().lower() for role in row.get("meal_roles") or []}
    return roles == {"breakfast"} or str(row.get("source_bucket") or "") == "food_breakfast"


def estimate_budget_gate_transportation_total(request: TripRequest) -> int:
    mode = str(request.transportation or "")
    days = max(int(request.travel_days or 1), 1)
    if any(word in mode for word in ["公共", "公交", "地铁"]):
        per_day = 50
    elif "自驾" in mode:
        per_day = 220
    elif any(word in mode for word in ["打车", "出租"]):
        per_day = 180
    else:
        per_day = 90
    return per_day * days


def generate_one(
    raw_request: dict[str, Any],
    args: argparse.Namespace,
    amap_api_key: str,
    sample_attempt: int = 1,
) -> dict[str, Any]:
    """生成一条 SFT 样本。"""
    request_id = raw_request["request_id"]
    request = normalize_request(raw_request, request_id)
    builder = get_worker_context_builder(amap_api_key, args.historical_weather_provider)

    started_at = time.perf_counter()
    planner_context = builder.collect(request)
    apply_budget_fit_policy(planner_context, request, raw_request)
    budget_context_audit = maybe_validate_budget_context_gate(request, planner_context, args)
    weather_status = planner_context["tool_snapshot"].get("tool_status", {}).get("weather", {})
    weather_provider = "open_meteo_archive" if "open_meteo_archive" in str(weather_status.get("message", "")) else "amap_or_unknown"
    compact_context = builder.compact_for_planner(planner_context)
    planner_query = build_planner_query(builder, request, planner_context)
    control_spec = record_control_spec(raw_request, request, planner_context)

    llm = get_worker_llm(args)
    max_tokens = planner_max_output_tokens(request, args, sample_attempt)
    plan_data = llm.complete_json(
        PLANNER_AGENT_PROMPT,
        planner_query,
        temperature=args.temperature,
        max_tokens=max_tokens,
        metadata={
            "script": "generate_sft_data.py",
            "call_type": "planner",
            "request_id": request_id,
            "sample_attempt": sample_attempt,
            "travel_days": request.travel_days,
            "party_total": request.party.total,
            "budget_amount": getattr(request.budget_constraint, "amount", None),
            "budget_level": getattr(request.budget_constraint, "budget_level", None),
            "city": request.city,
        },
    )
    planner_llm_usage = getattr(llm, "last_usage", None)
    trip_plan = TripPlan(**plan_data)
    recompute_budget(trip_plan, request)
    validate_trip_plan_shape(trip_plan, request, planner_context)
    validate_training_plan(trip_plan, request, planner_context)
    output = json.dumps(trip_plan.model_dump(), ensure_ascii=False)

    elapsed = time.perf_counter() - started_at
    return {
        "record_id": request_id,
        "created_at": datetime.now(timezone.utc).isoformat(),
        "request_source": raw_request.get("source", "unknown"),
        "request": request.model_dump(),
        "control_spec": control_spec,
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
            "max_tokens": max_tokens,
            "teacher_provider": getattr(llm, "provider", None),
            "teacher_model": getattr(llm, "model", None),
            "llm_usage": planner_llm_usage,
            "weather_provider": weather_provider,
            "budget_context_audit": budget_context_audit,
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
    apply_budget_fit_policy(planner_context, request, raw_request)
    budget_context_audit = maybe_validate_budget_context_gate(request, planner_context, args)
    compact_context = builder.compact_for_planner(planner_context)
    control_spec = record_control_spec(raw_request, request, planner_context)
    weather_status = planner_context["tool_snapshot"].get("tool_status", {}).get("weather", {})
    weather_provider = "open_meteo_archive" if "open_meteo_archive" in str(weather_status.get("message", "")) else "amap_or_unknown"
    return {
        "record_id": raw_request["request_id"],
        "request": request.model_dump(),
        "control_spec": control_spec,
        "elapsed_seconds": round(time.perf_counter() - started_at, 3),
        "prompt_chars": len(json.dumps(compact_context, ensure_ascii=False)),
        "weather_provider": weather_provider,
        "budget_context_audit": budget_context_audit,
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
    request_id = format_request_id(index)
    last_error: Exception | None = None
    candidate_index = index
    retry_stride = max(int(getattr(args, "budget_context_retry_stride", 0) or args.count or 1), 1)
    for attempt in range(1, args.sample_retries + 1):
        try:
            raw_request = build_one_request(candidate_index, args)
            record = generate_one(raw_request, args, amap_api_key, sample_attempt=attempt)
            record["metadata"]["sample_attempt"] = attempt
            if candidate_index != index:
                record["metadata"]["base_request_id"] = request_id
            return record
        except BudgetContextUnreachableError as exc:
            last_error = exc
            print(
                f"⚠️  {request_id} 样本生成第 {attempt}/{args.sample_retries} 次失败: {exc}",
                flush=True,
            )
            candidate_index += retry_stride
        except Exception as exc:  # noqa: BLE001
            last_error = exc
            print(
                f"⚠️  {request_id} 样本生成第 {attempt}/{args.sample_retries} 次失败: {exc}",
                flush=True,
            )
            if args.request_source == "budget_supplement":
                candidate_index += retry_stride
    raise RuntimeError(f"{request_id} 样本生成失败: {last_error}") from last_error


def build_requests(args: argparse.Namespace) -> list[dict[str, Any]]:
    """生成本轮 TripRequest 原始输入。"""
    if args.request_source == "budget_supplement":
        print(f"开始用预算补充分布生成模拟用户请求: count={args.count}", flush=True)
        return [generate_budget_supplement_request(args.start_index + index, args) for index in range(args.count)]
    if args.request_source == "controlled":
        print(f"开始用受控分布生成模拟用户请求: count={args.count}", flush=True)
        return [generate_controlled_request(args.start_index + index, args) for index in range(args.count)]
    if args.request_source == "template":
        print(f"开始用模板生成模拟用户请求: count={args.count}", flush=True)
        return generate_template_requests(args.count, args.start_index, args.seed, args.date_mode)
    return generate_llm_requests(
        args.count,
        args.start_index,
        args.request_batch_size,
        args.seed,
        args.request_max_tokens,
        args.request_generation_retries,
        not args.disable_template_request_fallback,
        args.data_gen_provider,
        args.data_gen_model,
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
        "budget_strictness": dict(Counter((item.get("control_spec") or {}).get("budget_strictness", "unknown") for item in requests)),
        "budget_level_strictness": dict(
            Counter(
                f"{(item.get('control_spec') or {}).get('budget_level', 'unknown')}/"
                f"{(item.get('control_spec') or {}).get('budget_strictness', 'unknown')}"
                for item in requests
            )
        ),
        "pace": dict(Counter((item.get("control_spec") or {}).get("pace", "unknown") for item in requests)),
        "diet": dict(Counter((item.get("control_spec") or {}).get("diet", "unknown") for item in requests)),
        "preferences_top20": dict(Counter(pref for item in requests for pref in (item.get("preferences") or [])).most_common(20)),
        "positive_preferences_top20": dict(
            Counter(
                pref
                for item in requests
                for pref in ((item.get("control_spec") or {}).get("positive_preferences") or item.get("preferences") or [])
            ).most_common(20)
        ),
        "negative_constraints_top20": dict(
            Counter(
                constraint
                for item in requests
                for constraint in ((item.get("control_spec") or {}).get("negative_constraints") or [])
            ).most_common(20)
        ),
        "diet_avoid_top20": dict(
            Counter(
                constraint
                for item in requests
                for constraint in ((item.get("control_spec") or {}).get("diet_avoid") or [])
            ).most_common(20)
        ),
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


def summarize_budget_context_audits(audits: list[dict[str, Any]]) -> dict[str, Any]:
    """dry-run 输出里给预算补数 gate 一个轻量汇总。"""
    if not audits:
        return {}
    ratios = [float(item.get("high_budget_ratio") or 0) for item in audits]
    return {
        "count": len(audits),
        "can_reach_target_min_rate": round(
            sum(bool(item.get("can_reach_target_min")) for item in audits) / len(audits),
            4,
        ),
        "can_reach_target_mid_rate": round(
            sum(bool(item.get("can_reach_target_mid")) for item in audits) / len(audits),
            4,
        ),
        "high_budget_ratio_min": round(min(ratios), 3),
        "high_budget_ratio_avg": round(sum(ratios) / len(ratios), 3),
        "high_budget_ratio_max": round(max(ratios), 3),
    }


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
                audit = item.get("budget_context_audit") or {}
                budget_text = (
                    f" budget_ratio={float(audit.get('high_budget_ratio', 0)):.2f}"
                    if audit
                    else ""
                )
                print(
                    f"context progress: {progress_index}/{len(indices)} ok={len(results)} "
                    f"failed={len(failed)} last={item['record_id']} weather={item['weather_provider']}{budget_text}",
                    flush=True,
                )
            except Exception as exc:  # noqa: BLE001
                failed.append({"record_id": format_request_id(index), "error": str(exc)})
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
                "budget_context_gate": summarize_budget_context_audits(
                    [
                        item["budget_context_audit"]
                        for item in results
                        if item.get("budget_context_audit")
                    ]
                ),
                "tool_counts_avg": {
                    key: round(sum(item["tool_counts"].get(key, 0) for item in results) / len(results), 2) if results else 0
                    for key in ["classic_pois", "preference_pois", "scenic_pois", "experience_pois", "hotel_pois", "food_pois", "trip_weather"]
                },
            },
            ensure_ascii=False,
            indent=2,
        )
    )


def save_success_record(record: dict[str, Any]) -> None:
    append_jsonl(RAW_RECORDS_PATH, record)
    append_jsonl(
        REQUESTS_PATH,
        record["request"] | {"request_id": record["record_id"], "control_spec": record.get("control_spec", {})},
    )


def save_failure_record(sample_index: int, exc: Exception) -> None:
    append_jsonl(
        ERRORS_PATH,
        {
            "created_at": datetime.now(timezone.utc).isoformat(),
            "record_id": format_request_id(sample_index),
            "error_type": type(exc).__name__,
            "error": str(exc),
        },
    )


def run_target_success_generation(
    args: argparse.Namespace,
    amap_api_key: str,
    existing_ids: set[str],
) -> tuple[int, int, int]:
    """按目标成功数动态提交任务，适合高失败率补数。"""
    target_successes = max(int(args.target_successes or 0), 0)
    max_launches = max(int(args.count or 0), target_successes)
    if target_successes <= 0:
        raise ValueError("target_successes must be > 0")

    ok = 0
    failed = 0
    launched = 0
    completed = 0
    next_offset = 0
    pending = {}
    max_workers = max(1, int(args.workers or 1))

    def submit_next(executor: ThreadPoolExecutor) -> bool:
        nonlocal launched, next_offset
        while launched < max_launches:
            sample_index = args.start_index + next_offset
            next_offset += 1
            if format_request_id(sample_index) in existing_ids:
                continue
            pending[executor.submit(generate_one_by_index, sample_index, args, amap_api_key)] = sample_index
            launched += 1
            return True
        return False

    print(
        f"开始目标成功数生成: target_successes={target_successes}, max_launches={max_launches}, "
        f"workers={max_workers}, request_source={args.request_source}",
        flush=True,
    )
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        while len(pending) < max_workers and ok + len(pending) < target_successes and submit_next(executor):
            pass

        target_reached_reported = False
        while pending:
            done, _ = wait(pending, return_when=FIRST_COMPLETED)
            for future in done:
                sample_index = pending.pop(future)
                completed += 1
                try:
                    record = future.result()
                    if record["record_id"] in existing_ids:
                        raise ValueError(f"生成结果 record_id 已存在，跳过重复样本: {record['record_id']}")
                    save_success_record(record)
                    existing_ids.add(record["record_id"])
                    ok += 1
                    print(
                        f"progress: completed={completed}/{launched} ok={ok}/{target_successes} "
                        f"failed={failed} last={record['record_id']}",
                        flush=True,
                    )
                except Exception as exc:  # noqa: BLE001
                    failed += 1
                    save_failure_record(sample_index, exc)
                    print(
                        f"progress: completed={completed}/{launched} ok={ok}/{target_successes} "
                        f"failed={failed} error={exc}",
                        flush=True,
                    )

            if ok >= target_successes:
                if pending and not target_reached_reported:
                    print(f"目标成功数已达到，等待{len(pending)}个已提交任务收尾。", flush=True)
                    target_reached_reported = True
                continue

            while len(pending) < max_workers and ok + len(pending) < target_successes and submit_next(executor):
                pass

    return ok, failed, launched


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="生成 SFT 数据")
    parser.add_argument("--count", type=int, default=20, help="本轮尝试生成的样本数")
    parser.add_argument("--start-index", type=int, default=0, help="request_id 起始编号")
    parser.add_argument("--seed", type=int, default=20260429)
    parser.add_argument("--request-source", choices=["template", "llm", "controlled", "budget_supplement"], default="controlled")
    parser.add_argument(
        "--date-mode",
        choices=["future", "mixed", "past"],
        default="mixed",
        help="用户请求日期分布；past/mixed可触发训练专用Open-Meteo历史天气",
    )
    parser.add_argument("--request-batch-size", type=int, default=20, help="兼容旧命令，当前异步流水线不再使用批量请求生成")
    parser.add_argument("--request-max-tokens", type=int, default=8000)
    parser.add_argument("--request-generation-retries", type=int, default=3)
    parser.add_argument("--disable-template-request-fallback", action="store_true")
    parser.add_argument(
        "--target-budget-mix",
        default="",
        help="用于 controlled/budget_supplement 请求，按 index 精确指定预算分布，如 standard/soft=520,comfortable/soft=245,premium/soft=157；省略 strictness 时默认 soft",
    )
    parser.add_argument(
        "--disallow-budget-strictness-none",
        action="store_true",
        help="有 budget amount 时禁止 strictness=none，若随机抽到 none 则改为 soft。",
    )
    parser.add_argument("--workers", type=int, default=1)
    parser.add_argument(
        "--teacher-model-provider",
        "--data-gen-provider",
        dest="data_gen_provider",
        choices=["env", "deepseek", "mimo"],
        default=None,
        help="强模型配置 profile；默认使用 DATA_GEN_* / DeepSeek 环境变量，mimo 使用 MIMO_* 配置。",
    )
    parser.add_argument(
        "--teacher-model",
        "--data-gen-model",
        dest="data_gen_model",
        default=None,
        help="覆盖具体强模型 model id；不传则使用所选 provider 的环境变量默认值。",
    )
    parser.add_argument(
        "--amap-qps-limit",
        type=float,
        default=None,
        help="高德 HTTP API 进程内 QPS 限制；默认使用 AMAP_QPS_LIMIT 环境变量或 3，0 表示关闭限速。",
    )
    parser.add_argument("--sample-retries", type=int, default=3, help="单条样本完整链路失败后的重试次数")
    parser.add_argument(
        "--target-successes",
        type=int,
        default=0,
        help="大于0时动态生成直到达到目标成功数，count作为最多提交的base请求数",
    )
    parser.add_argument(
        "--budget-context-min-ratio",
        type=float,
        default=float(os.getenv("SFT_BUDGET_CONTEXT_MIN_RATIO", "1.0")),
        help="强模型前置过滤候选池高配估算/预算低于该比例的预算请求；0表示关闭",
    )
    parser.add_argument(
        "--budget-context-retry-stride",
        type=int,
        default=0,
        help="上下文预算不可达后换新请求的index步长；0表示使用count",
    )
    parser.add_argument("--temperature", type=float, default=0.2)
    parser.add_argument("--max-output-tokens", type=int, default=0, help="大于0时覆盖动态 token 上限")
    parser.add_argument("--output-base-tokens", type=int, default=int(os.getenv("PLANNER_OUTPUT_BASE_TOKENS", "5000")))
    parser.add_argument("--output-tokens-per-day", type=int, default=int(os.getenv("PLANNER_OUTPUT_TOKENS_PER_DAY", "2600")))
    parser.add_argument("--output-retry-tokens", type=int, default=int(os.getenv("PLANNER_OUTPUT_RETRY_TOKENS", "2000")))
    parser.add_argument("--output-tokens-cap", type=int, default=int(os.getenv("PLANNER_MAX_OUTPUT_TOKENS_CAP", "24000")))
    parser.add_argument(
        "--historical-weather-provider",
        choices=["open-meteo", "none"],
        default="open-meteo",
        help="训练数据专用历史天气来源；只在整段行程早于今天时生效",
    )
    parser.add_argument("--val-ratio", type=float, default=0.1)
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=None,
        help="本轮输出目录；提供后 records/errors/requests/LLaMAFactory 导出都写入该目录，不注册全局 dataset_info",
    )
    parser.add_argument("--resume", action="store_true", help="跳过 records.jsonl 中已存在的 record_id")
    parser.add_argument("--dry-run-requests", action="store_true", help="只生成并打印请求，不调用高德和强模型")
    parser.add_argument("--dry-run-summary", action="store_true", help="dry-run-requests时只打印分布摘要")
    parser.add_argument("--dry-run-context", action="store_true", help="只生成请求并获取PlannerContext，不调用Planner强模型、不写训练数据")
    return parser.parse_args()


def configure_amap_qps_limit(qps_limit: float | None = None) -> None:
    value = qps_limit
    if value is None:
        raw_value = os.getenv("AMAP_QPS_LIMIT")
        if raw_value:
            value = float(raw_value)
    if value is None:
        return
    set_amap_qps_limit(value)


def main() -> None:
    args = parse_args()
    configure_output_paths(args.output_dir)
    load_project_env()
    configure_amap_qps_limit(args.amap_qps_limit)
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
        if format_request_id(args.start_index + offset) not in existing_ids
    ]
    if not indices and args.target_successes <= 0:
        print("没有需要生成的新样本。")
        return

    print(
        f"开始异步生成 SFT: count={len(indices)}, workers={args.workers}, "
        f"request_source={args.request_source}",
        flush=True,
    )

    ok = 0
    failed = 0
    launched = len(indices)
    if args.target_successes > 0:
        ok, failed, launched = run_target_success_generation(args, amap_api_key, existing_ids)
    elif args.workers <= 1:
        for progress_index, sample_index in enumerate(indices, start=1):
            try:
                record = generate_one_by_index(sample_index, args, amap_api_key)
                save_success_record(record)
                ok += 1
                print(f"progress: {progress_index}/{len(indices)} ok={ok} failed={failed} last={record['record_id']}", flush=True)
            except Exception as exc:  # noqa: BLE001
                failed += 1
                save_failure_record(sample_index, exc)
                print(f"progress: {progress_index}/{len(indices)} ok={ok} failed={failed} error={exc}", flush=True)
    else:
        with ThreadPoolExecutor(max_workers=args.workers) as executor:
            futures = {executor.submit(generate_one_by_index, index, args, amap_api_key): index for index in indices}
            for progress_index, future in enumerate(as_completed(futures), start=1):
                sample_index = futures[future]
                try:
                    record = future.result()
                    save_success_record(record)
                    ok += 1
                    print(f"progress: {progress_index}/{len(indices)} ok={ok} failed={failed} last={record['record_id']}", flush=True)
                except Exception as exc:  # noqa: BLE001
                    failed += 1
                    save_failure_record(sample_index, exc)
                    print(f"progress: {progress_index}/{len(indices)} ok={ok} failed={failed} error={exc}", flush=True)

    all_records = read_jsonl(RAW_RECORDS_PATH)
    train_count, val_count = write_llamafactory_files(all_records, val_ratio=args.val_ratio)
    print(
        "完成: "
        f"本轮成功={ok}, 本轮失败={failed}, 本轮提交={launched}, 累计可训练={len(all_records)}, "
        f"train={train_count}, val={val_count}"
    )
    print(f"raw: {RAW_RECORDS_PATH}")
    print(f"errors: {ERRORS_PATH}")
    print(f"llamafactory train: {LLAMAFACTORY_TRAIN_PATH}")
    print(f"llamafactory val: {LLAMAFACTORY_VAL_PATH}")


if __name__ == "__main__":
    main()
