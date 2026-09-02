"""训练数据生成公共工具。"""

from __future__ import annotations

import json
import random
import re
import sys
from datetime import date, timedelta
from pathlib import Path
from typing import Any

from dotenv import load_dotenv

# 允许直接从仓库根目录执行这个公共模块做导入检查；正式流程仍由具体入口调用。
SCRIPTS_DIR = Path(__file__).resolve().parents[1]
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

from shared.paths import PROJECT_ROOT


def load_project_env() -> None:
    """加载项目和 HelloAgents 的环境变量。"""
    load_dotenv(PROJECT_ROOT / "backend" / ".env", override=False)
    load_dotenv(PROJECT_ROOT / ".env", override=False)
    helloagents_env = PROJECT_ROOT.parent / "HelloAgents" / ".env"
    if helloagents_env.exists():
        load_dotenv(helloagents_env, override=False)


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    """读取 JSONL。"""
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8") as f:
        return [json.loads(line) for line in f if line.strip()]


def write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    """覆盖写入 JSONL。"""
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")


def write_json(path: Path, data: Any) -> None:
    """覆盖写入 JSON。"""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


def split_train_val(rows: list[dict[str, Any]], val_ratio: float = 0.1) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    """固定随机种子切分训练集和验证集。"""
    rows = list(rows)
    rng = random.Random(20260427)
    rng.shuffle(rows)
    val_size = max(1, int(len(rows) * val_ratio)) if len(rows) > 1 else 0
    return rows[val_size:], rows[:val_size]


def format_duration(seconds: float) -> str:
    """把秒数格式化成便于阅读的时间。"""
    seconds = max(0, int(seconds))
    hours, remainder = divmod(seconds, 3600)
    minutes, secs = divmod(remainder, 60)
    if hours:
        return f"{hours}h{minutes:02d}m{secs:02d}s"
    if minutes:
        return f"{minutes}m{secs:02d}s"
    return f"{secs}s"


def estimate_remaining(start_time: float, done: int, total: int) -> str:
    """根据当前速度估算剩余时间。"""
    if done <= 0:
        return "估算中"
    import time

    elapsed = time.monotonic() - start_time
    remaining = elapsed / done * max(total - done, 0)
    return format_duration(remaining)


def date_range(start_date: str, days: int) -> list[str]:
    """生成连续日期。"""
    start = date.fromisoformat(start_date)
    return [(start + timedelta(days=i)).isoformat() for i in range(days)]


def extract_json(text: str) -> Any:
    """从模型输出中严格提取 JSON 对象或数组。"""
    stripped = text.strip()
    fenced = re.search(r"```(?:json)?\s*(.*?)```", stripped, re.DOTALL)
    if fenced:
        stripped = fenced.group(1).strip()

    try:
        return json.loads(stripped)
    except json.JSONDecodeError:
        pass

    starts = [idx for idx in (stripped.find("{"), stripped.find("[")) if idx != -1]
    if not starts:
        raise ValueError("模型输出中没有 JSON 起始符")
    start = min(starts)
    end = max(stripped.rfind("}"), stripped.rfind("]"))
    if end <= start:
        raise ValueError("模型输出中没有完整 JSON")
    return json.loads(stripped[start : end + 1])
