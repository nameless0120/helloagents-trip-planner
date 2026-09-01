#!/usr/bin/env python3
"""用强模型为高频景点候选估算成人票价。

注意：输出是预算训练用的强模型估算，不是实时票价/官方票价。
"""

from __future__ import annotations

import argparse
from datetime import datetime
import json
from pathlib import Path
import sys
import time
from typing import Any


ROOT = Path(__file__).resolve().parents[4]
SCRIPTS_DIR = ROOT / "training/scripts"
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

from shared.common import read_jsonl, write_json  # noqa: E402
from shared.llm_client import DataGenLLM  # noqa: E402


DEFAULT_INPUT = ROOT / "training/data/planner/attraction_prices/generated/request_count_ge5_bucketed_candidates.jsonl"
DEFAULT_OUTPUT_DIR = ROOT / "training/data/planner/attraction_prices"


SYSTEM_PROMPT = """你是旅行规划训练数据的景点票价估算助手。

你的任务是给中国旅游景点估算“成人全价门票”，用于旅行预算训练，不是实时售票报价。

必须遵守：
1. 只输出 JSON 对象，不要输出 Markdown。
2. 如果景点本身免费开放，票价填 0。
3. 如果景点免费但内部项目/交通/讲解/游船/索道另收费，只估算景点基础入园票，不包含内部二消。
4. 如果 POI 本身就是索道、游船、演出、主题公园、海洋馆、观光塔等收费项目，则估算该项目成人票。
5. 不要为了显得精确编造小数，价格使用整数人民币。
6. 允许用常识估算，但必须标注 confidence: high/medium/low。
7. source 必须固定为 llm_estimated。
8. 无法判断时仍给一个保守估算，并把 confidence 设为 low。
9. 当前估价以稳定预算训练为主；除非你明确知道该景点淡旺季票价差异，否则 off_season、normal_season、peak_season 填同一个成人基础票价。
"""


def build_user_prompt(items: list[dict[str, Any]]) -> str:
    """构造批量估价 prompt。"""
    payload = []
    for item in items:
        payload.append(
            {
                "city": item.get("city"),
                "name": item.get("name"),
                "category": first_key(item.get("types") or {}) or item.get("review_bucket"),
                "review_bucket": item.get("review_bucket"),
                "review_reason": item.get("review_reason"),
                "source_keywords": item.get("source_keywords") or {},
                "current_rule_hints": item.get("ticket_hints") or {},
                "request_count": item.get("request_count"),
                "count": item.get("count"),
            }
        )

    return f"""请为下面 {len(payload)} 个景点估算成人全价票价。

票价字段定义：
- off_season: 淡季成人全价，人民币元。
- normal_season: 平季成人全价，人民币元。
- peak_season: 旺季/节假日成人全价，人民币元。

返回 JSON 格式必须是：
{{
  "items": [
    {{
      "city": "城市",
      "name": "景点名",
      "ticket_price_profile": {{
        "off_season": 0,
        "normal_season": 0,
        "peak_season": 0
      }},
      "ticket_price_source": "llm_estimated",
      "confidence": "high|medium|low",
      "pricing_note": "一句中文说明，说明为什么这样估价；如果免费，说明免费口径；如果不含内部二消，也要说明。"
    }}
  ]
}}

待估价景点：
{json.dumps(payload, ensure_ascii=False, indent=2)}
"""


def first_key(mapping: dict[str, Any]) -> str:
    """取 dict 第一个 key。"""
    for key in mapping:
        return str(key)
    return ""


def chunked(rows: list[dict[str, Any]], size: int) -> list[list[dict[str, Any]]]:
    """分块。"""
    return [rows[index : index + size] for index in range(0, len(rows), size)]


def load_done_names(path: Path) -> set[tuple[str, str]]:
    """读取已完成估价的城市景点 key。"""
    done = set()
    if not path.exists():
        return done
    for row in read_jsonl(path):
        for item in row.get("items") or []:
            done.add((str(item.get("city") or ""), str(item.get("name") or "")))
    return done


def normalize_price_profile(profile: dict[str, Any]) -> dict[str, int]:
    """规整模型返回的票价。"""
    result = {}
    for key in ["off_season", "normal_season", "peak_season"]:
        value = profile.get(key)
        if value is None:
            value = profile.get("normal_season")
        try:
            value = int(round(float(value)))
        except (TypeError, ValueError):
            value = 0
        result[key] = max(value, 0)

    if result["normal_season"] == 0:
        result["normal_season"] = max(result["off_season"], result["peak_season"])
    if result["off_season"] == 0 and result["normal_season"] > 0:
        result["off_season"] = result["normal_season"]
    if result["peak_season"] == 0 and result["normal_season"] > 0:
        result["peak_season"] = result["normal_season"]
    return result


def normalize_estimated_item(raw: dict[str, Any], original: dict[str, Any]) -> dict[str, Any]:
    """把模型估价结果合并回候选元信息。"""
    confidence = str(raw.get("confidence") or "low").lower()
    if confidence not in {"high", "medium", "low"}:
        confidence = "low"

    return {
        "city": original.get("city"),
        "name": original.get("name"),
        "aliases": original.get("aliases") or [],
        "category": first_key(original.get("types") or {}) or original.get("review_bucket") or "待确认",
        "ticket_price_profile": normalize_price_profile(raw.get("ticket_price_profile") or {}),
        "ticket_price_source": "llm_estimated",
        "confidence": confidence,
        "pricing_note": str(raw.get("pricing_note") or "").strip(),
        "review_bucket": original.get("review_bucket"),
        "review_reason": original.get("review_reason"),
        "collection_meta": {
            "request_count": original.get("request_count"),
            "count": original.get("count"),
            "buckets": original.get("buckets") or {},
            "ticket_hints": original.get("ticket_hints") or {},
            "source_keywords": original.get("source_keywords") or {},
        },
    }


def estimate_batch(llm: DataGenLLM, batch: list[dict[str, Any]], args: argparse.Namespace) -> list[dict[str, Any]]:
    """调用强模型估算一个 batch。"""
    expected = {(row.get("city"), row.get("name")): row for row in batch}
    last_error: Exception | None = None
    for attempt in range(1, args.retries + 1):
        try:
            result = llm.complete_json(
                SYSTEM_PROMPT,
                build_user_prompt(batch),
                temperature=args.temperature,
                max_tokens=args.max_tokens,
            )
            items = result.get("items") if isinstance(result, dict) else result
            if not isinstance(items, list):
                raise ValueError(f"模型返回 items 不是数组: {type(items).__name__}")

            normalized = []
            seen = set()
            for raw in items:
                key = (raw.get("city"), raw.get("name"))
                original = expected.get(key)
                if original is None:
                    # 按名称找一次，兼容模型轻微改 city 的情况。
                    original = next((row for row in batch if row.get("name") == raw.get("name")), None)
                if original is None:
                    continue
                normalized.append(normalize_estimated_item(raw, original))
                seen.add((original.get("city"), original.get("name")))

            missing = [row for row in batch if (row.get("city"), row.get("name")) not in seen]
            if missing:
                names = "、".join(str(row.get("name")) for row in missing[:5])
                raise ValueError(f"模型漏估 {len(missing)} 条: {names}")
            return normalized
        except Exception as exc:  # noqa: BLE001
            last_error = exc
            print(f"⚠️  batch 第 {attempt}/{args.retries} 次估价失败: {exc}", flush=True)
            time.sleep(1.5 * attempt)
    raise RuntimeError(f"batch 估价失败: {last_error}") from last_error


def build_price_table(items: list[dict[str, Any]]) -> dict[str, Any]:
    """构建可供 Planner 使用的价格表。"""
    return {
        "version": "attraction_price_table_llm_estimated",
        "updated_at": datetime.now().date().isoformat(),
        "currency": "CNY",
        "price_unit": "adult_ticket_cny",
        "note": (
            "本表为 SFT 预算训练使用的强模型估算票价表，不是实时票价或官方核验票价；"
            "票价口径为成人基础入园/参观全价，不包含景区内交通、讲解、餐饮、购物、保险和二次消费。"
        ),
        "items": items,
    }


def write_explanation(path: Path, table_path: Path, raw_path: Path, input_path: Path, item_count: int) -> None:
    """写估价说明。"""
    path.write_text(
        "\n".join(
            [
                "# 景点票价强模型估算说明",
                "",
                "## 定位",
                "",
                "这批景点票价用于 SFT 的预算账本训练，不是实时票价、官方票价或售票依据。",
                "",
                "## 票价口径",
                "",
                "- 成人基础入园/参观全价，单位 CNY。",
                "- 免费开放景点填 0。",
                "- 若景点本体免费但内部游船、索道、讲解、展陈或体验项目另收费，本表只记录基础入园价。",
                "- 若 POI 本身就是索道、游船、演出、主题公园、海洋馆、观光塔等收费项目，则记录该项目成人票估算。",
                "- 不区分学生、儿童、老人、军人等优惠票。",
                "",
                "## 数据来源",
                "",
                "- 输入候选来自 PlannerContext 高频命中景点。",
                "- 票价由强模型基于常识估算，字段统一标记为 `ticket_price_source = llm_estimated`。",
                "- `confidence` 表示强模型对估算的自评置信度，不代表人工核验。",
                "",
                "## 输出文件",
                "",
                f"- 输入候选：`{input_path}`",
                f"- 原始批次估价：`{raw_path}`",
                f"- 可用价格表：`{table_path}`",
                f"- 景点数量：{item_count}",
                "",
                "## 后续 TODO",
                "",
                "- 高频 TOP 景点逐步升级为 `manual_verified`。",
                "- 高价项目接入官网/OTA/官方小程序票价核验。",
                "- 增加儿童、老人、学生、军人等优惠票口径。",
                "- 增加景区内游船、索道、观光车等二消项目的独立预算字段。",
                "",
            ]
        ),
        encoding="utf-8",
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="用强模型估算高频景点成人票价")
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument("--min-request-count", type=int, default=5)
    parser.add_argument("--batch-size", type=int, default=20)
    parser.add_argument("--limit", type=int, default=0, help="调试用，0 表示不限制")
    parser.add_argument("--include-ignored", action="store_true", help="是否包含暂不入表候选")
    parser.add_argument("--resume", action="store_true")
    parser.add_argument("--dry-run-prompt", action="store_true", help="只打印第一个 batch 的 prompt，不调用模型")
    parser.add_argument("--temperature", type=float, default=0.1)
    parser.add_argument("--max-tokens", type=int, default=12000)
    parser.add_argument("--retries", type=int, default=3)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    rows = read_jsonl(args.input)
    rows = [
        row
        for row in rows
        if int(row.get("request_count") or 0) >= args.min_request_count
        and (args.include_ignored or row.get("review_bucket") != "暂不入表")
    ]
    if args.limit > 0:
        rows = rows[: args.limit]

    args.output_dir.mkdir(parents=True, exist_ok=True)
    generated_dir = args.output_dir / "generated"
    reports_dir = args.output_dir / "reports"
    snapshots_dir = args.output_dir / "snapshots"
    for directory in [generated_dir, reports_dir, snapshots_dir]:
        directory.mkdir(parents=True, exist_ok=True)

    raw_path = generated_dir / f"request_count_ge{args.min_request_count}_llm_price_estimates.jsonl"
    table_path = snapshots_dir / f"request_count_ge{args.min_request_count}_attraction_price_table_llm_estimated.json"
    explanation_path = reports_dir / "景点票价强模型估算说明.md"

    done = load_done_names(raw_path) if args.resume else set()
    todo = [row for row in rows if (row.get("city"), row.get("name")) not in done]

    if args.dry_run_prompt:
        first_batch = todo[: args.batch_size] or rows[: args.batch_size]
        print("===== SYSTEM PROMPT =====")
        print(SYSTEM_PROMPT)
        print("\n===== USER PROMPT =====")
        print(build_user_prompt(first_batch))
        return

    print(f"开始强模型景点估价: total={len(rows)}, todo={len(todo)}, batch_size={args.batch_size}", flush=True)
    llm = DataGenLLM()
    for index, batch in enumerate(chunked(todo, args.batch_size), start=1):
        estimated = estimate_batch(llm, batch, args)
        payload = {
            "created_at": datetime.now().isoformat(timespec="seconds"),
            "batch_index": index,
            "items": estimated,
        }
        with raw_path.open("a", encoding="utf-8") as file:
            file.write(json.dumps(payload, ensure_ascii=False) + "\n")
        print(
            f"progress batch={index} done={min(index * args.batch_size, len(todo))}/{len(todo)}",
            flush=True,
        )

    all_items = []
    seen = set()
    for row in read_jsonl(raw_path):
        for item in row.get("items") or []:
            key = (item.get("city"), item.get("name"))
            if key in seen:
                continue
            seen.add(key)
            all_items.append(item)

    write_json(table_path, build_price_table(all_items))
    write_explanation(explanation_path, table_path, raw_path, args.input, len(all_items))
    print(f"估价原始结果: {raw_path}")
    print(f"强模型估价价格表: {table_path}")
    print(f"估价说明: {explanation_path}")


if __name__ == "__main__":
    main()
