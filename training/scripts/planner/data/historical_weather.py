"""训练数据专用历史天气补充。

线上系统仍然只使用高德短期天气；这个模块只服务于训练数据生成。
当行程完全发生在过去时，用 Open-Meteo Archive daily 数据改写
PlannerContext.tool_snapshot.trip_weather，训练模型“有天气就遵循”。
"""

from __future__ import annotations

import hashlib
import json
import os
import sys
import time
from datetime import date, datetime
from pathlib import Path
from typing import Any

import httpx


PROJECT_ROOT = Path(__file__).resolve().parents[4]
BACKEND_DIR = PROJECT_ROOT / "backend"
if str(BACKEND_DIR) not in sys.path:
    sys.path.insert(0, str(BACKEND_DIR))

from app.planner.dates import trip_date_strings  # noqa: E402
from app.models.schemas import TripRequest  # noqa: E402


OPEN_METEO_ARCHIVE_URL = "https://archive-api.open-meteo.com/v1/archive"
OPEN_METEO_TIMEOUT = int(os.getenv("OPEN_METEO_TIMEOUT", "30"))
OPEN_METEO_CACHE_DIR = Path(
    os.getenv(
        "OPEN_METEO_CACHE_DIR",
        str(PROJECT_ROOT / "training" / "data" / "cache" / "open_meteo_archive"),
    )
)
OPEN_METEO_CACHE_TTL_SECONDS = int(
    os.getenv("OPEN_METEO_CACHE_TTL_SECONDS", str(60 * 60 * 60))
)


# 常用旅游城市坐标。只用于训练数据历史天气，不影响线上地点/天气逻辑。
TOURISM_CITY_COORDS: dict[str, tuple[float, float]] = {
    "北京": (39.9042, 116.4074),
    "上海": (31.2304, 121.4737),
    "广州": (23.1291, 113.2644),
    "深圳": (22.5431, 114.0579),
    "杭州": (30.2741, 120.1551),
    "成都": (30.5728, 104.0668),
    "重庆": (29.5630, 106.5516),
    "西安": (34.3416, 108.9398),
    "南京": (32.0603, 118.7969),
    "苏州": (31.2989, 120.5853),
    "厦门": (24.4798, 118.0894),
    "青岛": (36.0671, 120.3826),
    "长沙": (28.2282, 112.9388),
    "武汉": (30.5928, 114.3055),
    "昆明": (25.0389, 102.7183),
    "大理": (25.6065, 100.2676),
    "丽江": (26.8565, 100.2271),
    "桂林": (25.2736, 110.2900),
    "三亚": (18.2528, 109.5119),
    "哈尔滨": (45.8038, 126.5349),
    "珠海": (22.2711, 113.5767),
    "福州": (26.0745, 119.2965),
    "泉州": (24.8741, 118.6759),
    "天津": (39.3434, 117.3616),
    "洛阳": (34.6197, 112.4540),
    "扬州": (32.3932, 119.4129),
    "贵阳": (26.6470, 106.6302),
    "呼和浩特": (40.8426, 111.7492),
    "沈阳": (41.8057, 123.4315),
    "大连": (38.9140, 121.6147),
    "宁波": (29.8683, 121.5440),
    "合肥": (31.8206, 117.2272),
    "济南": (36.6512, 117.1201),
    "太原": (37.8706, 112.5489),
    "南昌": (28.6820, 115.8579),
    "郑州": (34.7466, 113.6254),
    "海口": (20.0440, 110.1999),
    "乌鲁木齐": (43.8256, 87.6168),
    "兰州": (36.0611, 103.8343),
    "银川": (38.4872, 106.2309),
    "西宁": (36.6171, 101.7782),
    "拉萨": (29.6520, 91.1721),
    "张家界": (29.1171, 110.4792),
    "黄山": (29.7147, 118.3375),
    "秦皇岛": (39.9354, 119.6005),
    "烟台": (37.4638, 121.4479),
    "威海": (37.5131, 122.1204),
}


WEATHER_CODE_TEXT = {
    0: "晴",
    1: "晴间多云",
    2: "多云",
    3: "阴",
    45: "雾",
    48: "雾",
    51: "小雨",
    53: "小雨",
    55: "中雨",
    56: "冻雨",
    57: "冻雨",
    61: "小雨",
    63: "中雨",
    65: "大雨",
    66: "冻雨",
    67: "冻雨",
    71: "小雪",
    73: "中雪",
    75: "大雪",
    77: "雪",
    80: "阵雨",
    81: "阵雨",
    82: "强阵雨",
    85: "阵雪",
    86: "强阵雪",
    95: "雷雨",
    96: "雷雨伴冰雹",
    99: "雷雨伴冰雹",
}


def apply_open_meteo_history(request: TripRequest, planner_context: dict[str, Any]) -> bool:
    """如果是过去完整行程，用历史天气替换 PlannerContext 天气快照。"""
    if not is_past_trip(request):
        return False

    rows = fetch_historical_trip_weather(request)
    if not rows:
        return False

    snapshot = planner_context.setdefault("tool_snapshot", {})
    snapshot["available_weather"] = rows
    snapshot["trip_weather"] = rows
    snapshot.setdefault("tool_status", {})["weather"] = {
        "ok": True,
        "message": f"open_meteo_archive={len(rows)}, covered_trip_days={len(rows)}/{request.travel_days}",
    }
    return True


def is_past_trip(request: TripRequest) -> bool:
    """行程最后一天早于今天，才视为完整历史行程。"""
    end_date = datetime.strptime(request.end_date, "%Y-%m-%d").date()
    return end_date < date.today()


def fetch_historical_trip_weather(request: TripRequest) -> list[dict[str, Any]]:
    """按城市坐标和行程日期获取 Open-Meteo daily 历史天气。"""
    coords = TOURISM_CITY_COORDS.get(request.city)
    if not coords:
        print(f"⚠️  Open-Meteo历史天气缺少城市坐标: {request.city}", flush=True)
        return []

    start_date = request.start_date
    end_date = request.end_date
    raw = fetch_open_meteo_archive(request.city, coords[0], coords[1], start_date, end_date)
    return normalize_open_meteo_daily(raw, request)


def fetch_open_meteo_archive(city: str, latitude: float, longitude: float, start_date: str, end_date: str) -> dict[str, Any]:
    """调用 Open-Meteo Archive API，并做本地缓存。"""
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "start_date": start_date,
        "end_date": end_date,
        "daily": ",".join(
            [
                "weather_code",
                "temperature_2m_max",
                "temperature_2m_min",
                "wind_speed_10m_max",
                "wind_direction_10m_dominant",
            ]
        ),
        "timezone": "Asia/Shanghai",
        "wind_speed_unit": "kmh",
    }
    cache_path = open_meteo_cache_path(city, params)
    cached = read_cache(cache_path)
    if cached is not None:
        return cached

    response = httpx.get(OPEN_METEO_ARCHIVE_URL, params=params, timeout=OPEN_METEO_TIMEOUT)
    response.raise_for_status()
    data = response.json()
    if data.get("error"):
        raise RuntimeError(f"Open-Meteo历史天气错误: {data.get('reason')}")
    write_cache(cache_path, data)
    return data


def normalize_open_meteo_daily(raw: dict[str, Any], request: TripRequest) -> list[dict[str, Any]]:
    """把 Open-Meteo daily 字段转成 PlannerContext trip_weather 协议。"""
    daily = raw.get("daily") or {}
    dates = daily.get("time") or []
    codes = daily.get("weather_code") or []
    temp_max = daily.get("temperature_2m_max") or []
    temp_min = daily.get("temperature_2m_min") or []
    wind_speed = daily.get("wind_speed_10m_max") or []
    wind_degree = daily.get("wind_direction_10m_dominant") or []

    by_date = {}
    for index, date_text in enumerate(dates):
        code = safe_int(value_at(codes, index))
        weather_text = WEATHER_CODE_TEXT.get(code, "天气未知")
        by_date[date_text] = {
            "date": date_text,
            "day_weather": weather_text,
            "night_weather": weather_text,
            "day_temp": safe_int(value_at(temp_max, index), default="未知"),
            "night_temp": safe_int(value_at(temp_min, index), default="未知"),
            "wind_direction": wind_direction_text(value_at(wind_degree, index)),
            "wind_power": wind_power_text(value_at(wind_speed, index)),
            "source": "open_meteo_archive",
        }

    return [by_date[date_text] for date_text in trip_date_strings(request) if date_text in by_date]


def value_at(values: list[Any], index: int) -> Any:
    """安全取 daily 数组。"""
    return values[index] if index < len(values) else None


def safe_int(value: Any, default: Any = None) -> Any:
    """温度/天气代码转整数；空值保留默认值。"""
    try:
        if value is None:
            return default
        return int(round(float(value)))
    except (TypeError, ValueError):
        return default


def wind_direction_text(degree: Any) -> str:
    """角度转中文风向。"""
    try:
        value = float(degree)
    except (TypeError, ValueError):
        return "未知"
    directions = ["北", "东北", "东", "东南", "南", "西南", "西", "西北"]
    return directions[int((value + 22.5) // 45) % 8]


def wind_power_text(speed_kmh: Any) -> str:
    """Open-Meteo km/h 风速粗略转成高德风力表达。"""
    try:
        speed = float(speed_kmh)
    except (TypeError, ValueError):
        return "未知"
    if speed < 6:
        return "0-1"
    if speed < 20:
        return "1-3"
    if speed < 29:
        return "3-4"
    if speed < 39:
        return "4-5"
    if speed < 50:
        return "5-6"
    return "6+"


def open_meteo_cache_path(city: str, params: dict[str, Any]) -> Path:
    """生成历史天气缓存路径。"""
    payload = {"city": city, "params": {key: str(params[key]) for key in sorted(params)}}
    digest = hashlib.sha256(
        json.dumps(payload, ensure_ascii=False, sort_keys=True).encode("utf-8")
    ).hexdigest()[:24]
    safe_city = "".join(ch for ch in city if ch.isalnum() or ch in ("-", "_")) or "unknown"
    return OPEN_METEO_CACHE_DIR / f"{safe_city}_{params['start_date']}_{params['end_date']}_{digest}.json"


def read_cache(path: Path) -> dict[str, Any] | None:
    """读取未过期历史天气缓存。"""
    if not path.exists():
        return None
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
        created_at = float(payload.get("created_at", 0))
        if time.time() - created_at > OPEN_METEO_CACHE_TTL_SECONDS:
            return None
        data = payload.get("data")
        return data if isinstance(data, dict) else None
    except Exception:
        return None


def write_cache(path: Path, data: dict[str, Any]) -> None:
    """写入历史天气缓存。"""
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        payload = {
            "created_at": time.time(),
            "ttl_seconds": OPEN_METEO_CACHE_TTL_SECONDS,
            "data": data,
        }
        tmp_path = path.with_suffix(f".tmp.{os.getpid()}.{time.time_ns()}")
        tmp_path.write_text(json.dumps(payload, ensure_ascii=False), encoding="utf-8")
        tmp_path.replace(path)
    except Exception as exc:
        print(f"⚠️  Open-Meteo历史天气缓存写入失败: {exc}", flush=True)
