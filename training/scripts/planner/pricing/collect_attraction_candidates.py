#!/usr/bin/env python3
"""收集 PlannerContext 中的景点候选，用于补本地票价表。

这个脚本只做“景点池审计”，不调用 Planner 强模型，也不写训练数据。
核心用途：

1. 从已有 records.jsonl 聚合 classic/preference/experience POI。
2. 或按受控请求分布直接查询 PlannerContext，观察高德 cost 覆盖情况。
3. 输出缺价景点清单和待补票价表模板。
"""

from __future__ import annotations

import argparse
from collections import Counter
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass, field
from datetime import datetime
import json
import os
from pathlib import Path
import sys
import time
from typing import Any


ROOT = Path(__file__).resolve().parents[4]
BACKEND_DIR = ROOT / "backend"
SCRIPT_DIR = Path(__file__).resolve().parent
DATA_SCRIPT_DIR = ROOT / "training" / "scripts" / "planner" / "data"

for path in [str(ROOT), str(BACKEND_DIR), str(SCRIPT_DIR), str(DATA_SCRIPT_DIR)]:
    if path not in sys.path:
        sys.path.insert(0, path)

from app.planner.pricing import normalize_city, normalize_poi_name, parse_float, poi_name_aliases  # noqa: E402


BASE_BUCKETS = ["classic_pois", "preference_pois", "experience_pois"]
DEFAULT_RECORDS = ROOT / "training/data/planner/eval/records.jsonl"
DEFAULT_OUTPUT_DIR = ROOT / "training/data/planner/attraction_prices"


@dataclass
class AttractionStats:
    """单个城市景点的聚合统计。"""

    city: str
    normalized_name: str
    count: int = 0
    record_ids: set[str] = field(default_factory=set)
    names: Counter[str] = field(default_factory=Counter)
    buckets: Counter[str] = field(default_factory=Counter)
    keywords: Counter[str] = field(default_factory=Counter)
    types: Counter[str] = field(default_factory=Counter)
    adnames: Counter[str] = field(default_factory=Counter)
    locations: Counter[str] = field(default_factory=Counter)
    ratings: Counter[str] = field(default_factory=Counter)
    amap_cost_values: Counter[str] = field(default_factory=Counter)
    ticket_hints: Counter[str] = field(default_factory=Counter)
    ticket_sources: Counter[str] = field(default_factory=Counter)
    ticket_seasons: Counter[str] = field(default_factory=Counter)
    table_names: Counter[str] = field(default_factory=Counter)
    confidences: Counter[str] = field(default_factory=Counter)

    def add(self, record_id: str, bucket: str, row: dict[str, Any]) -> None:
        """添加一次 POI 出现。"""
        self.count += 1
        if record_id:
            self.record_ids.add(record_id)

        self.buckets[bucket] += 1
        for field_name, counter in [
            ("name", self.names),
            ("source_keyword", self.keywords),
            ("type", self.types),
            ("adname", self.adnames),
            ("location", self.locations),
            ("rating", self.ratings),
            ("ticket_price_source", self.ticket_sources),
            ("ticket_price_season", self.ticket_seasons),
            ("ticket_price_table_name", self.table_names),
            ("ticket_price_confidence", self.confidences),
        ]:
            value = str(row.get(field_name) or "").strip()
            if value:
                counter[value] += 1

        amap_cost = parse_float(row.get("cost"))
        if amap_cost is not None and amap_cost >= 0:
            self.amap_cost_values[str(int(round(amap_cost)))] += 1

        hint = row.get("ticket_price_hint")
        if hint not in (None, ""):
            self.ticket_hints[str(hint)] += 1

    @property
    def request_count(self) -> int:
        return len(self.record_ids)

    @property
    def has_amap_cost(self) -> bool:
        return bool(self.amap_cost_values)

    @property
    def has_price_table_match(self) -> bool:
        # 当前价格表项可能把 source 写成 llm_estimated/manual_verified，
        # 所以 table_name 比 source 更能说明“命中了本地表”。
        return bool(self.table_names)

    @property
    def uses_rule_estimate(self) -> bool:
        return self.ticket_sources.get("rule_estimated", 0) > 0

    @property
    def needs_price_table(self) -> bool:
        return (not self.has_amap_cost) and (not self.has_price_table_match)

    @property
    def primary_name(self) -> str:
        return self.names.most_common(1)[0][0] if self.names else self.normalized_name

    def top(self, counter: Counter[str], n: int = 3) -> list[str]:
        return [value for value, _ in counter.most_common(n)]

    def priority_score(self) -> int:
        """给人工补价排序：经典、高频、缺价、非免费 hint 优先。"""
        score = self.request_count * 10 + self.count
        score += self.buckets.get("classic_pois", 0) * 8
        score += self.buckets.get("preference_pois", 0) * 4
        score += self.buckets.get("experience_pois", 0) * 2
        if self.needs_price_table:
            score += 50
        if self.uses_rule_estimate:
            score += 20
        if any(int(float(value)) > 0 for value in self.ticket_hints if str(value).replace(".", "", 1).isdigit()):
            score += 10
        return score

    def as_json(self) -> dict[str, Any]:
        return {
            "city": self.city,
            "name": self.primary_name,
            "normalized_name": self.normalized_name,
            "count": self.count,
            "request_count": self.request_count,
            "needs_price_table": self.needs_price_table,
            "has_amap_cost": self.has_amap_cost,
            "has_price_table_match": self.has_price_table_match,
            "uses_rule_estimate": self.uses_rule_estimate,
            "buckets": dict(self.buckets),
            "aliases": sorted(set(poi_name_aliases(self.primary_name)) - {self.normalized_name}),
            "name_variants": self.top(self.names, 8),
            "source_keywords": dict(self.keywords.most_common(8)),
            "types": dict(self.types.most_common(5)),
            "adnames": dict(self.adnames.most_common(5)),
            "locations": dict(self.locations.most_common(3)),
            "ratings": dict(self.ratings.most_common(3)),
            "amap_cost_values": dict(self.amap_cost_values.most_common(5)),
            "ticket_hints": dict(self.ticket_hints.most_common(5)),
            "ticket_sources": dict(self.ticket_sources.most_common(5)),
            "ticket_seasons": dict(self.ticket_seasons.most_common(5)),
            "ticket_price_table_names": dict(self.table_names.most_common(5)),
            "ticket_price_confidences": dict(self.confidences.most_common(5)),
            "priority_score": self.priority_score(),
        }


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    """读取 JSONL。"""
    if not path.exists():
        return []
    rows = []
    with path.open("r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            rows.append(json.loads(line))
    return rows


def write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    """写 JSONL。"""
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as file:
        for row in rows:
            file.write(json.dumps(row, ensure_ascii=False) + "\n")


def get_context_rows_from_records(paths: list[Path]) -> list[dict[str, Any]]:
    """从 records.jsonl 读取 planner_context。"""
    rows = []
    for path in paths:
        for record in read_jsonl(path):
            context = record.get("planner_context") or {}
            if not context:
                continue
            rows.append(
                {
                    "record_id": record.get("record_id", ""),
                    "request": record.get("request") or {},
                    "planner_context": context,
                    "source": str(path),
                }
            )
    return rows


def get_context_rows_live(args: argparse.Namespace) -> list[dict[str, Any]]:
    """按请求分布直接查询 PlannerContext。"""
    import generate_sft_data as gen  # noqa: PLC0415

    gen.load_project_env()
    amap_api_key = os.getenv("AMAP_MAPS_API_KEY") or os.getenv("AMAP_API_KEY")
    if not amap_api_key:
        raise RuntimeError("缺少 AMAP_MAPS_API_KEY 或 AMAP_API_KEY")

    indices = [args.start_index + offset for offset in range(args.count)]
    results = []
    failed = []
    started = time.perf_counter()

    print(
        f"开始收集景点候选: count={len(indices)}, workers={args.workers}, "
        f"request_source={args.request_source}, date_mode={args.date_mode}",
        flush=True,
    )

    def collect_one(index: int) -> dict[str, Any]:
        raw_request = gen.build_one_request(index, args)
        request = gen.normalize_request(raw_request, raw_request["request_id"])
        gen.validate_request_date_mode(request, args.date_mode)
        builder = gen.get_worker_context_builder(amap_api_key, args.historical_weather_provider)
        planner_context = builder.collect(request)
        return {
            "record_id": raw_request["request_id"],
            "request": request.model_dump(),
            "control_spec": raw_request.get("control_spec", {}),
            "planner_context": planner_context,
            "source": "live_context",
        }

    with ThreadPoolExecutor(max_workers=max(1, args.workers)) as executor:
        futures = {executor.submit(collect_one, index): index for index in indices}
        for progress, future in enumerate(as_completed(futures), start=1):
            index = futures[future]
            try:
                row = future.result()
                results.append(row)
                print(
                    f"collect progress: {progress}/{len(indices)} ok={len(results)} "
                    f"failed={len(failed)} last={row['record_id']}",
                    flush=True,
                )
            except Exception as exc:  # noqa: BLE001
                failed.append({"record_id": f"request_{index:06d}", "error": str(exc)})
                print(
                    f"collect progress: {progress}/{len(indices)} ok={len(results)} "
                    f"failed={len(failed)} error={exc}",
                    flush=True,
                )

    print(
        f"收集完成: ok={len(results)}, failed={len(failed)}, elapsed={time.perf_counter() - started:.1f}s",
        flush=True,
    )
    if failed:
        print("失败样例:")
        print(json.dumps(failed[:10], ensure_ascii=False, indent=2), flush=True)
    return results


def aggregate_attractions(context_rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """聚合 PlannerContext 里的候选景点。"""
    stats: dict[tuple[str, str], AttractionStats] = {}

    for context_row in context_rows:
        record_id = str(context_row.get("record_id") or "")
        request = context_row.get("request") or {}
        request_city = normalize_city(request.get("city") or "")
        snapshot = (context_row.get("planner_context") or {}).get("tool_snapshot") or {}

        for bucket in BASE_BUCKETS:
            for item in snapshot.get(bucket) or []:
                name = str(item.get("name") or "").strip()
                normalized_name = normalize_poi_name(name)
                if not normalized_name:
                    continue
                city = normalize_city(item.get("cityname") or request_city)
                key = (city, normalized_name)
                if key not in stats:
                    stats[key] = AttractionStats(city=city, normalized_name=normalized_name)
                stats[key].add(record_id, bucket, item)

    rows = [value.as_json() for value in stats.values()]
    return sorted(rows, key=lambda row: (-row["priority_score"], row["city"], row["name"]))


def build_price_table_template(rows: list[dict[str, Any]], limit: int) -> dict[str, Any]:
    """生成待补票价表模板。"""
    candidates = [row for row in rows if row["needs_price_table"]]
    candidates = sorted(candidates, key=lambda row: (-row["priority_score"], row["city"], row["name"]))[:limit]

    items = []
    for row in candidates:
        items.append(
            {
                "city": row["city"],
                "name": row["name"],
                "aliases": row["aliases"],
                "category": next(iter(row["types"]), "待确认"),
                "ticket_price_profile": {
                    "off_season": None,
                    "normal_season": None,
                    "peak_season": None,
                },
                "ticket_price_source": "todo",
                "confidence": "todo",
                "collection_meta": {
                    "count": row["count"],
                    "request_count": row["request_count"],
                    "buckets": row["buckets"],
                    "source_keywords": row["source_keywords"],
                    "ticket_hints": row["ticket_hints"],
                },
            }
        )

    return {
        "version": "attraction_price_table_template",
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "currency": "CNY",
        "price_unit": "adult_ticket_cny",
        "note": "待补价格模板，不要直接作为线上价格表使用；补完 source/confidence/票价后再合并到 backend/app/planner/attraction_price_table.json。",
        "items": items,
    }


def write_markdown_report(path: Path, rows: list[dict[str, Any]], source_count: int, limit: int) -> None:
    """写中文审查报告。"""
    path.parent.mkdir(parents=True, exist_ok=True)
    total = len(rows)
    no_amap = sum(1 for row in rows if not row["has_amap_cost"])
    needs_table = sum(1 for row in rows if row["needs_price_table"])
    table_hit = sum(1 for row in rows if row["has_price_table_match"])
    amap_hit = sum(1 for row in rows if row["has_amap_cost"])

    lines = [
        "# 景点票价候选收集报告",
        "",
        f"- 统计 PlannerContext 数量：{source_count}",
        f"- 去重景点数：{total}",
        f"- 高德已有 cost：{amap_hit}",
        f"- 命中本地价格表：{table_hit}",
        f"- 高德无 cost：{no_amap}",
        f"- 建议补入价格表：{needs_table}",
        "",
        "## 优先补价清单",
        "",
        "| 序号 | 城市 | 景点 | 出现请求数 | 候选次数 | 来源桶 | 当前价格来源 | 当前hint | 高德cost | 关键词 | 类型 |",
        "| --- | --- | --- | ---: | ---: | --- | --- | --- | --- | --- | --- |",
    ]

    selected = [row for row in rows if row["needs_price_table"]][:limit]
    for idx, row in enumerate(selected, start=1):
        lines.append(
            "| {idx} | {city} | {name} | {request_count} | {count} | {buckets} | {sources} | {hints} | {amap_cost} | {keywords} | {types} |".format(
                idx=idx,
                city=row["city"],
                name=row["name"],
                request_count=row["request_count"],
                count=row["count"],
                buckets="<br>".join(f"{k}:{v}" for k, v in row["buckets"].items()),
                sources="<br>".join(f"{k}:{v}" for k, v in row["ticket_sources"].items()) or "-",
                hints="<br>".join(f"{k}:{v}" for k, v in row["ticket_hints"].items()) or "-",
                amap_cost="<br>".join(f"{k}:{v}" for k, v in row["amap_cost_values"].items()) or "-",
                keywords="<br>".join(f"{k}:{v}" for k, v in row["source_keywords"].items()) or "-",
                types="<br>".join(list(row["types"].keys())[:2]) or "-",
            )
        )

    lines.extend(
        [
            "",
            "## 说明",
            "",
            "- `建议补入价格表` 指：高德没有 `cost`，也没有命中本地价格表，目前只能走规则估价。",
            "- `当前hint` 是后端规则暂时给 Planner 的票价 hint，不代表真实票价。",
            "- 后续优先处理城市经典、出现频次高、主题公园/景区/演出类这几类，因为它们最影响预算训练。",
            "",
        ]
    )

    path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="收集 PlannerContext 景点候选，辅助补本地票价表")
    parser.add_argument("--records", nargs="*", type=Path, default=[DEFAULT_RECORDS], help="已有 records.jsonl，可传多个")
    parser.add_argument("--collect-context", action="store_true", help="不读records，直接生成请求并查询PlannerContext")
    parser.add_argument("--count", type=int, default=100, help="collect-context模式下的请求数")
    parser.add_argument("--start-index", type=int, default=0)
    parser.add_argument("--seed", type=int, default=20260429)
    parser.add_argument("--request-source", choices=["template", "controlled"], default="controlled")
    parser.add_argument("--date-mode", choices=["future", "mixed", "past"], default="mixed")
    parser.add_argument("--workers", type=int, default=1)
    parser.add_argument(
        "--historical-weather-provider",
        choices=["open-meteo", "none"],
        default="open-meteo",
        help="和 SFT 生成脚本保持一致；本脚本只关心POI，天气失败通常不影响景点统计。",
    )
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument("--report-limit", type=int, default=120)
    parser.add_argument("--template-limit", type=int, default=300)
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    if args.collect_context:
        context_rows = get_context_rows_live(args)
    else:
        context_rows = get_context_rows_from_records(args.records)

    rows = aggregate_attractions(context_rows)
    args.output_dir.mkdir(parents=True, exist_ok=True)
    generated_dir = args.output_dir / "generated"
    reports_dir = args.output_dir / "reports"
    snapshots_dir = args.output_dir / "snapshots"
    for directory in [generated_dir, reports_dir, snapshots_dir]:
        directory.mkdir(parents=True, exist_ok=True)

    candidates_path = generated_dir / "attraction_candidates.jsonl"
    report_path = reports_dir / "景点票价候选收集报告.md"
    template_path = snapshots_dir / "attraction_price_table_todo.json"

    write_jsonl(candidates_path, rows)
    write_markdown_report(report_path, rows, len(context_rows), args.report_limit)
    template = build_price_table_template(rows, args.template_limit)
    template_path.write_text(json.dumps(template, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"PlannerContext数量: {len(context_rows)}")
    print(f"去重景点数: {len(rows)}")
    print(f"建议补价景点数: {sum(1 for row in rows if row['needs_price_table'])}")
    print(f"候选明细: {candidates_path}")
    print(f"审查报告: {report_path}")
    print(f"待补模板: {template_path}")


if __name__ == "__main__":
    main()
