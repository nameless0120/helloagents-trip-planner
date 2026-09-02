#!/usr/bin/env python3
"""把高频待补景点按票价处理策略分桶，供人工审核。"""

from __future__ import annotations

import argparse
from collections import Counter
from datetime import datetime
import json
from pathlib import Path
import sys
from typing import Any

ROOT = Path(__file__).resolve().parents[4]
SCRIPTS_DIR = ROOT / "training" / "scripts"
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

from shared.paths import ATTRACTION_PRICES_DIR  # noqa: E402

DEFAULT_INPUT = ATTRACTION_PRICES_DIR / "generated/attraction_candidates.jsonl"
DEFAULT_OUTPUT_DIR = ATTRACTION_PRICES_DIR


HIGH_PRICE_KEYWORDS = [
    "迪士尼",
    "长隆",
    "世界之窗",
    "海洋王国",
    "海洋世界",
    "海洋馆",
    "水族馆",
    "冰雪大世界",
    "千古情",
    "索道",
    "游船",
    "游乐",
    "乐园",
    "大峡谷",
    "峡谷",
    "虎林园",
    "野生动物",
    "动物世界",
    "演艺",
    "东方明珠",
    "广州塔",
    "龙塔",
    "冰雪",
    "波塞冬",
    "海底世界",
]

FREE_KEYWORDS = [
    "广场",
    "步行街",
    "商业街",
    "老街",
    "历史文化街区",
    "街区",
    "古城",
    "古镇",
    "外滩",
    "江滩",
    "海滩",
    "沙滩",
    "码头",
    "水街",
    "城市阳台",
    "中央大街",
    "沙面岛",
    "宽窄巷子",
    "东郊记忆",
    "五四广场",
    "五一广场",
    "天安门广场",
    "大理古城",
    "双廊古镇",
    "喜洲古镇",
    "沙溪古镇",
    "巍山古城",
    "北京路步行街",
    "太平老街",
]

FREE_PARK_KEYWORDS = [
    "人才公园",
    "深圳湾公园",
    "莲花山公园",
    "笔架山公园",
    "大梅沙海滨公园",
    "人民公园",
    "天府艺术公园",
    "钱江世纪公园",
    "太子湾公园",
    "大运河杭钢公园",
    "中山公园",
    "汉口江滩",
    "解放公园",
]

PUBLIC_MUSEUM_KEYWORDS = [
    "省博物馆",
    "市博物馆",
    "博物院",
    "博物馆",
    "美术馆",
    "纪念馆",
    "历史馆",
]

PAID_STANDARD_KEYWORDS = [
    "故宫",
    "长城",
    "城墙",
    "总统府",
    "黄鹤楼",
    "岳麓书院",
    "雷峰塔",
    "日光岩",
    "灵隐寺",
    "天坛",
    "颐和园",
    "都江堰",
    "杜甫草堂",
    "武侯祠",
    "牛首山",
    "总统府",
    "兵马俑",
    "秦始皇",
    "崂山",
    "白云山",
    "象鼻山",
    "独秀峰",
    "王城",
    "三塔",
    "千岛湖",
    "植物园",
    "动物园",
    "寺",
    "书院",
    "园林",
    "风景区",
    "景区",
    "地质公园",
    "森林公园",
]

IGNORE_KEYWORDS = [
    "体验馆",
    "文化馆",
    "培训",
    "校区",
    "生活馆",
    "工作室",
    "摄影",
    "暂停营业",
    "商场",
    "购物中心",
    "广场店",
]

PAID_MUSEUM_EXCEPTIONS = [
    "故宫",
    "兵马俑",
    "碑林",
    "啤酒博物馆",
    "自然博物馆",
    "四行仓库",
    "杜甫草堂",
    "武侯祠",
]


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    """读取 JSONL。"""
    rows = []
    with path.open("r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    return rows


def write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    """写 JSONL。"""
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as file:
        for row in rows:
            file.write(json.dumps(row, ensure_ascii=False) + "\n")


def text_of(row: dict[str, Any]) -> str:
    """拼出用于规则判断的文本。"""
    return ";".join(
        [
            str(row.get("name") or ""),
            ";".join(row.get("name_variants") or []),
            ";".join((row.get("types") or {}).keys()),
            ";".join((row.get("source_keywords") or {}).keys()),
        ]
    )


def name_type_text(row: dict[str, Any]) -> str:
    """只拼 POI 名称和类型，避免 source_keyword 干扰免费/收费判断。"""
    return ";".join(
        [
            str(row.get("name") or ""),
            ";".join(row.get("name_variants") or []),
            ";".join((row.get("types") or {}).keys()),
        ]
    )


def name_text(row: dict[str, Any]) -> str:
    """只拼 POI 名称和别名。"""
    return ";".join(
        [
            str(row.get("name") or ""),
            ";".join(row.get("name_variants") or []),
        ]
    )


def has_any(text: str, keywords: list[str]) -> bool:
    return any(keyword in text for keyword in keywords)


def is_experience_only(row: dict[str, Any]) -> bool:
    buckets = row.get("buckets") or {}
    return bool(buckets) and set(buckets) <= {"experience_pois"}


def classify(row: dict[str, Any]) -> tuple[str, str, dict[str, int | None]]:
    """分桶，并给出待审核价格建议。"""
    name = str(row.get("name") or "")
    text = text_of(row)
    poi_name_text = name_text(row)
    poi_text = name_type_text(row)

    if is_experience_only(row) and has_any(text, IGNORE_KEYWORDS):
        return "暂不入表", "仅体验候选且像商业/培训/体验馆，价格不稳定", null_price()

    if has_any(text, IGNORE_KEYWORDS) and row.get("request_count", 0) < 8:
        return "暂不入表", "像商业/体验类POI，且频次不高", null_price()

    if has_any(poi_text, HIGH_PRICE_KEYWORDS):
        return "高价项目", "主题公园/索道/演出/高价场馆，必须单独查价", null_price()

    if has_any(name, PAID_MUSEUM_EXCEPTIONS):
        return "建议收费", "博物馆/纪念馆里的收费例外，需要查价", null_price()

    if has_any(poi_name_text, FREE_KEYWORDS) or has_any(poi_name_text, FREE_PARK_KEYWORDS):
        return "建议免费", "城市公共空间/街区/古镇/广场/公园倾向免费", zero_price()

    if has_any(poi_text, PUBLIC_MUSEUM_KEYWORDS):
        return "建议免费", "公共博物馆/美术馆/纪念馆多数免费，需人工快速确认", zero_price()

    if has_any(poi_text, PAID_STANDARD_KEYWORDS):
        return "建议收费", "景区/寺庙/园林/古迹/植物园等倾向收费，需要查价", null_price()

    if "0" in (row.get("ticket_hints") or {}):
        return "需要人工判断", "当前规则 hint 为 0，但名称/类型不足以确认免费", zero_price()

    return "需要人工判断", "规则无法稳定判断免费或收费", null_price()


def zero_price() -> dict[str, int]:
    return {"off_season": 0, "normal_season": 0, "peak_season": 0}


def null_price() -> dict[str, None]:
    return {"off_season": None, "normal_season": None, "peak_season": None}


def category_from_types(row: dict[str, Any]) -> str:
    types = list((row.get("types") or {}).keys())
    return types[0] if types else "待确认"


def make_bucketed_rows(rows: list[dict[str, Any]], min_request_count: int) -> list[dict[str, Any]]:
    """过滤并分桶。"""
    selected = [
        row
        for row in rows
        if row.get("needs_price_table")
        and not row.get("has_amap_cost")
        and int(row.get("request_count") or 0) >= min_request_count
    ]
    bucketed = []
    for row in selected:
        bucket, reason, price = classify(row)
        bucketed.append(
            {
                **row,
                "review_bucket": bucket,
                "review_reason": reason,
                "suggested_ticket_price_profile": price,
            }
        )
    return sorted(
        bucketed,
        key=lambda row: (
            bucket_order(row["review_bucket"]),
            -int(row.get("request_count") or 0),
            -int(row.get("count") or 0),
            row.get("city") or "",
            row.get("name") or "",
        ),
    )


def bucket_order(bucket: str) -> int:
    order = {
        "建议免费": 0,
        "建议收费": 1,
        "高价项目": 2,
        "需要人工判断": 3,
        "暂不入表": 4,
    }
    return order.get(bucket, 99)


def build_draft_table(rows: list[dict[str, Any]]) -> dict[str, Any]:
    """生成审核草稿，不直接作为线上价格表。"""
    items = []
    for row in rows:
        if row["review_bucket"] == "暂不入表":
            continue
        items.append(
            {
                "city": row["city"],
                "name": row["name"],
                "aliases": row.get("aliases") or [],
                "category": category_from_types(row),
                "ticket_price_profile": row["suggested_ticket_price_profile"],
                "ticket_price_source": "review_pending",
                "confidence": "review_pending",
                "review_bucket": row["review_bucket"],
                "review_reason": row["review_reason"],
                "collection_meta": {
                    "request_count": row["request_count"],
                    "count": row["count"],
                    "buckets": row["buckets"],
                    "ticket_hints": row["ticket_hints"],
                    "source_keywords": row["source_keywords"],
                },
            }
        )
    return {
        "version": "attraction_price_table_review_draft_v1",
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "currency": "CNY",
        "price_unit": "adult_ticket_cny",
        "note": "人工审核草稿，不要直接替换线上价格表。确认票价/source/confidence后再合并。",
        "items": items,
    }


def write_markdown(path: Path, rows: list[dict[str, Any]], min_request_count: int) -> None:
    """写中文审核报告。"""
    path.parent.mkdir(parents=True, exist_ok=True)
    counts = Counter(row["review_bucket"] for row in rows)
    lines = [
        "# request_count >= 5 景点票价分桶审核",
        "",
        f"- 最小出现请求数：{min_request_count}",
        f"- 待审核景点数：{len(rows)}",
        "",
        "## 分桶统计",
        "",
        "| 分桶 | 数量 | 处理建议 |",
        "| --- | ---: | --- |",
    ]
    suggestions = {
        "建议免费": "人工快速扫一遍，确认后可批量写 0。",
        "建议收费": "需要查官网/OTA/强模型估价后填票价。",
        "高价项目": "必须单独查价，不能用规则估价。",
        "需要人工判断": "先看是否为核心景点，再决定免费/收费/忽略。",
        "暂不入表": "默认跳过，优先优化POI召回而不是配价。",
    }
    for bucket in ["建议免费", "建议收费", "高价项目", "需要人工判断", "暂不入表"]:
        lines.append(f"| {bucket} | {counts.get(bucket, 0)} | {suggestions[bucket]} |")

    for bucket in ["建议免费", "建议收费", "高价项目", "需要人工判断", "暂不入表"]:
        lines.extend(["", f"## {bucket}", ""])
        bucket_rows = [row for row in rows if row["review_bucket"] == bucket]
        if not bucket_rows:
            lines.append("无。")
            continue
        lines.extend(
            [
                "| 序号 | 城市 | 景点 | 请求数 | 候选次数 | 当前hint | 来源桶 | 类型 | 分桶原因 |",
                "| --- | --- | --- | ---: | ---: | --- | --- | --- | --- |",
            ]
        )
        for idx, row in enumerate(bucket_rows, start=1):
            lines.append(
                "| {idx} | {city} | {name} | {req} | {count} | {hints} | {buckets} | {types} | {reason} |".format(
                    idx=idx,
                    city=row.get("city") or "",
                    name=row.get("name") or "",
                    req=row.get("request_count") or 0,
                    count=row.get("count") or 0,
                    hints="<br>".join(f"{k}:{v}" for k, v in (row.get("ticket_hints") or {}).items()) or "-",
                    buckets="<br>".join(f"{k}:{v}" for k, v in (row.get("buckets") or {}).items()) or "-",
                    types="<br>".join(list((row.get("types") or {}).keys())[:2]) or "-",
                    reason=row.get("review_reason") or "",
                )
            )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="按 request_count 分桶待补票价景点")
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument("--min-request-count", type=int, default=5)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    rows = read_jsonl(args.input)
    bucketed = make_bucketed_rows(rows, args.min_request_count)
    args.output_dir.mkdir(parents=True, exist_ok=True)
    generated_dir = args.output_dir / "generated"
    reports_dir = args.output_dir / "reports"
    snapshots_dir = args.output_dir / "snapshots"
    for directory in [generated_dir, reports_dir, snapshots_dir]:
        directory.mkdir(parents=True, exist_ok=True)

    jsonl_path = generated_dir / f"request_count_ge{args.min_request_count}_bucketed_candidates.jsonl"
    report_path = reports_dir / f"request_count_ge{args.min_request_count}_景点票价分桶审核.md"
    draft_path = snapshots_dir / f"request_count_ge{args.min_request_count}_price_table_review_draft.json"

    write_jsonl(jsonl_path, bucketed)
    write_markdown(report_path, bucketed, args.min_request_count)
    draft_path.write_text(json.dumps(build_draft_table(bucketed), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    counts = Counter(row["review_bucket"] for row in bucketed)
    print(f"待审核景点数: {len(bucketed)}")
    for bucket in ["建议免费", "建议收费", "高价项目", "需要人工判断", "暂不入表"]:
        print(f"{bucket}: {counts.get(bucket, 0)}")
    print(f"分桶明细: {jsonl_path}")
    print(f"审核报告: {report_path}")
    print(f"价格表草稿: {draft_path}")


if __name__ == "__main__":
    main()
