"""DPO 数据构造公共工具。"""

from __future__ import annotations

import json
import random
import re
from collections import Counter
from pathlib import Path
from typing import Any

from eval_utils import (
    average,
    percentile,
    read_jsonl,
    weather_bucket,
    write_json,
)
from shared.paths import DPO_DIR, LLAMAFACTORY_DIR, LLAMAFACTORY_GENERATED_DIR

DATASET_INFO_PATH = LLAMAFACTORY_DIR / "dataset_info.json"

DEFAULT_DPO_PROMPTS = DPO_DIR / "prompts.jsonl"
DEFAULT_DPO_CANDIDATES = DPO_DIR / "candidates.jsonl"
DEFAULT_DPO_JUDGEMENTS = DPO_DIR / "judgements.jsonl"
DEFAULT_DPO_PAIRS = DPO_DIR / "pairs.jsonl"
DEFAULT_DPO_PAIRS_TRAIN = DPO_DIR / "pairs_train.jsonl"
DEFAULT_DPO_PAIRS_VAL = DPO_DIR / "pairs_val.jsonl"
DEFAULT_DPO_AUDIT = DPO_DIR / "audit_report.md"

DPO_SCORE_KEYS = [
    "grounding",
    "budget_alignment",
    "preference_alignment",
    "weather_awareness",
    "feasibility",
    "specificity",
]

DPO_SCORE_WEIGHTS = {
    "grounding": 0.20,
    "budget_alignment": 0.25,
    "preference_alignment": 0.25,
    "weather_awareness": 0.10,
    "feasibility": 0.15,
    "specificity": 0.05,
}

SEVERE_FLAG_KEYS = [
    "has_hallucinated_poi",
    "violates_diet",
    "over_budget",
    "too_rushed",
    "bad_hotel",
]


def metadata_from_record(record: dict[str, Any]) -> dict[str, Any]:
    """抽取用于分布审计和 pair tag 的元信息。"""
    request = record.get("request") or {}
    control_spec = record.get("control_spec") or {}
    return {
        "city": request.get("city", "unknown"),
        "travel_days": request.get("travel_days", "unknown"),
        "weather_bucket": weather_bucket(record),
        "budget_level": control_spec.get("budget_level", "unknown"),
        "companion_type": control_spec.get("companion_type", "unknown"),
        "city_tier": control_spec.get("city_tier", "unknown"),
        "diet": control_spec.get("diet", "unknown"),
        "pace": control_spec.get("pace", "unknown"),
    }


def prompt_row_from_record(record: dict[str, Any], *, source: str, system_prompt: str) -> dict[str, Any]:
    """把当前 SFT record 转成 DPO prompt 样本。"""
    return {
        "prompt_id": record["record_id"],
        "record_id": record["record_id"],
        "source": source,
        "request": record.get("request") or {},
        "control_spec": record.get("control_spec") or {},
        "planner_context": record.get("planner_context") or {},
        "compact_planner_context": record.get("compact_planner_context") or {},
        "system_prompt": system_prompt,
        "prompt": record.get("planner_query") or "",
        "metadata": metadata_from_record(record),
    }


def record_from_prompt_row(row: dict[str, Any]) -> dict[str, Any]:
    """把 DPO prompt row 还原成 evaluate_output 可用的 record 形态。"""
    return {
        "record_id": row["record_id"],
        "request": row.get("request") or {},
        "control_spec": row.get("control_spec") or {},
        "planner_context": row.get("planner_context") or {},
        "compact_planner_context": row.get("compact_planner_context") or {},
        "planner_query": row.get("prompt") or "",
    }


def normalize_base_url(base_url: str, auto_openai_path: bool = True) -> str:
    """规范化 OpenAI-compatible base_url。"""
    value = base_url.rstrip("/")
    if auto_openai_path and not value.endswith("/v1"):
        value = f"{value}/v1"
    return value


def candidate_done_prompt_ids(path: Path) -> set[str]:
    """读取已经完成候选生成的 prompt_id。"""
    return {row.get("prompt_id", "") for row in read_jsonl(path) if row.get("prompt_id")}


def judgement_done_candidate_ids(path: Path) -> set[str]:
    """读取已经 judge 的 candidate_id。"""
    return {row.get("candidate_id", "") for row in read_jsonl(path) if row.get("candidate_id")}


def normalize_score(value: Any) -> float:
    """把 judge 分数归一到 0-5。"""
    try:
        score = float(value)
    except Exception:  # noqa: BLE001
        score = 0.0
    return max(0.0, min(5.0, score))


def normalize_scores(raw: dict[str, Any]) -> dict[str, float]:
    """规范化 DPO judge 多维分数，并重算 overall。"""
    scores = {key: normalize_score(raw.get(key, 0)) for key in DPO_SCORE_KEYS}
    scores["overall"] = round(sum(scores[key] * DPO_SCORE_WEIGHTS[key] for key in DPO_SCORE_KEYS), 4)
    return scores


def normalize_hard_flags(raw: dict[str, Any] | None) -> dict[str, bool]:
    """规范化 hard flags。"""
    raw = raw or {}
    return {key: bool(raw.get(key, False)) for key in SEVERE_FLAG_KEYS}


def severe_flags(flags: dict[str, Any] | None) -> list[str]:
    """返回被置位的严重 flag。"""
    flags = normalize_hard_flags(flags)
    return [key for key, value in flags.items() if value]


def hard_filter_pass(
    candidate: dict[str, Any],
    *,
    min_attraction_grounding: float = 0.7,
    min_hotel_grounding: float = 0.8,
) -> tuple[bool, list[str]]:
    """判断候选是否可以进入 judge / DPO pair。"""
    # 先处理会导致后续规则全部失去意义的根因。
    # 如果 JSON 都没解析出来，schema/date/weather/grounding 等指标自然都会缺失；
    # 这时只保留最根本的失败原因，避免审计报告里出现一串级联假错误。
    generation_meta = candidate.get("generation_meta") or {}
    if generation_meta.get("ok") is False:
        return False, ["generation_failed"]

    metrics = candidate.get("rule_metrics") or {}
    if metrics.get("json_extract_ok") is not True or candidate.get("parsed_ok") is not True:
        return False, ["json_extract_ok"]

    if metrics.get("schema_ok") is not True or candidate.get("schema_ok") is not True:
        return False, ["schema_ok"]

    if not candidate.get("trip_plan"):
        return False, ["schema_ok"]

    reasons = []

    required_true = [
        "city_ok",
        "date_range_ok",
        "days_len_ok",
        "day_dates_ok",
        "weather_dates_ok",
        "day_index_ok",
        "meal_complete",
        "middle_hotel_ok",
        "invalid_hotel_name_ok",
        "location_object_ok",
        "budget_arithmetic_consistent",
        "hotel_budget_covers_nights",
        "weather_match",
    ]
    for key in required_true:
        if metrics.get(key) is not True:
            reasons.append(key)

    try:
        attraction_grounding = float(metrics.get("attraction_grounding_rate", 0))
    except Exception:  # noqa: BLE001
        attraction_grounding = 0.0
    try:
        hotel_grounding = float(metrics.get("hotel_grounding_rate", 0))
    except Exception:  # noqa: BLE001
        hotel_grounding = 0.0

    if attraction_grounding < min_attraction_grounding:
        reasons.append("attraction_grounding_low")
    if hotel_grounding < min_hotel_grounding:
        reasons.append("hotel_grounding_low")

    return not reasons, reasons


def make_training_prompt(system_prompt: str, prompt: str) -> str:
    """DPO 训练时把 system prompt 和 user prompt 合成一个 human message。"""
    return f"{system_prompt.strip()}\n\n{prompt.strip()}".strip()


def make_lf_dpo_row(pair: dict[str, Any]) -> dict[str, Any]:
    """转换成当前 LLaMA-Factory DPO sharegpt ranking 格式。"""
    return {
        "conversations": [
            {
                "from": "human",
                "value": make_training_prompt(pair.get("system_prompt", ""), pair["prompt"]),
            }
        ],
        "chosen": {"from": "gpt", "value": pair["chosen"]},
        "rejected": {"from": "gpt", "value": pair["rejected"]},
        "preference_reason": pair.get("preference_reason", ""),
    }


def update_dataset_info(
    train_path: Path,
    val_path: Path,
    *,
    train_dataset_name: str = "trip_dpo_train",
    val_dataset_name: str = "trip_dpo_val",
) -> None:
    """注册 DPO 数据到 central LLaMA-Factory dataset_info。"""
    if DATASET_INFO_PATH.exists():
        data = json.loads(DATASET_INFO_PATH.read_text(encoding="utf-8"))
    else:
        data = {}

    entry = {
        "ranking": True,
        "formatting": "sharegpt",
        "columns": {
            "messages": "conversations",
            "chosen": "chosen",
            "rejected": "rejected",
        },
    }
    data[train_dataset_name] = {"file_name": llamafactory_file_name(train_path), **entry}
    data[val_dataset_name] = {"file_name": llamafactory_file_name(val_path), **entry}
    write_json(DATASET_INFO_PATH, data)


def llamafactory_file_name(path: Path) -> str:
    """返回相对于 LLaMA-Factory 数据目录的文件名。"""
    try:
        return path.resolve().relative_to(LLAMAFACTORY_DIR.resolve()).as_posix()
    except ValueError:
        return path.name


def split_pairs(pairs: list[dict[str, Any]], val_ratio: float, seed: int) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    """固定随机切分 DPO pair。"""
    rows = list(pairs)
    rng = random.Random(seed)
    rng.shuffle(rows)
    val_size = max(1, round(len(rows) * val_ratio)) if len(rows) > 1 else 0
    return rows[val_size:], rows[:val_size]


def safe_counter(rows: list[dict[str, Any]], path: list[str]) -> Counter:
    """按嵌套路径统计分布。"""
    counter: Counter = Counter()
    for row in rows:
        value: Any = row
        for key in path:
            if isinstance(value, dict):
                value = value.get(key)
            else:
                value = None
                break
        counter[str(value if value is not None else "unknown")] += 1
    return counter


def write_lf_files(
    train_path: Path,
    val_path: Path,
    train_pairs: list[dict[str, Any]],
    val_pairs: list[dict[str, Any]],
    *,
    train_dataset_name: str = "trip_dpo_train",
    val_dataset_name: str = "trip_dpo_val",
) -> None:
    """写 LLaMA-Factory DPO JSON 数组并注册 dataset_info。"""
    write_json(train_path, [make_lf_dpo_row(pair) for pair in train_pairs])
    write_json(val_path, [make_lf_dpo_row(pair) for pair in val_pairs])
    update_dataset_info(
        train_path,
        val_path,
        train_dataset_name=train_dataset_name,
        val_dataset_name=val_dataset_name,
    )


def score_summary(rows: list[dict[str, Any]], key: str = "score_gap") -> dict[str, float]:
    """简单数值摘要。"""
    values = [float(row[key]) for row in rows if isinstance(row.get(key), (int, float))]
    if not values:
        return {"avg": 0.0, "p50": 0.0, "p90": 0.0}
    return {
        "avg": average(values),
        "p50": percentile(values, 0.5),
        "p90": percentile(values, 0.9),
    }


def tag_from_score_gap(chosen_scores: dict[str, Any], rejected_scores: dict[str, Any], threshold: float = 0.8) -> list[str]:
    """根据 judge 维度分差生成 pair tags。"""
    tags = []
    for key in DPO_SCORE_KEYS:
        if normalize_score(chosen_scores.get(key)) - normalize_score(rejected_scores.get(key)) >= threshold:
            tags.append(key)
    return tags


def slug_text(value: str) -> str:
    """转成路径/ID 安全文本。"""
    text = re.sub(r"[^0-9a-zA-Z._-]+", "_", value.strip())
    return text.strip("_") or "unknown"
