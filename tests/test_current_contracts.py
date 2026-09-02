"""当前主线入口的低成本契约测试。

这些测试只加载 schema 和数据处理函数，不请求外部 API，也不初始化 GPU。
"""

from __future__ import annotations

import random
import sys
import unittest
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path[:0] = [
    str(PROJECT_ROOT / "training/scripts"),
    str(PROJECT_ROOT / "training/scripts/planner/data"),
    str(PROJECT_ROOT / "backend"),
]

from app.config import Settings  # noqa: E402
from app.models.schemas import POISearchResponse, TripRequest  # noqa: E402
from planner.data.generate_sft_data import normalize_party_info, normalize_request  # noqa: E402
import run_pipeline  # noqa: E402


class RequestNormalizationTests(unittest.TestCase):
    def _request(self, party: object) -> dict:
        return {
            "city": "北京",
            "start_date": "2026-01-01",
            "travel_days": 2,
            "transportation": "公共交通",
            "accommodation": "经济型酒店",
            "preferences": [],
            "party": party,
            "budget_constraint": {"amount": 1000},
        }

    def test_total_only_party_is_expanded(self) -> None:
        request = normalize_request(self._request({"total": 2}), "test_total_only")
        self.assertEqual(request.party.model_dump(), {
            "adults": 2,
            "children": 0,
            "elders": 0,
            "total": 2,
            "companion_type": "other",
        })

    def test_partial_party_recomputes_total(self) -> None:
        request = normalize_request(
            self._request({"adults": 2, "children": 1, "elders": 0, "total": 99}),
            "test_partial",
        )
        self.assertEqual(request.party.total, 3)

    def test_total_can_fill_missing_adults(self) -> None:
        party = normalize_party_info(
            {"total": 4, "children": 1, "elders": 1},
            rng=random.Random(1),
            companion_type="family_mixed",
        )
        self.assertEqual(party["adults"], 2)
        self.assertEqual(party["total"], 4)


class CurrentContractTests(unittest.TestCase):
    def test_schema_list_defaults_are_independent(self) -> None:
        first = POISearchResponse(success=True)
        first.data.append({
            "id": "1",
            "name": "故宫",
            "type": "景点",
            "address": "北京",
            "location": {"longitude": 116.4, "latitude": 39.9},
        })
        second = POISearchResponse(success=True)
        self.assertEqual(second.data, [])

    def test_amap_alias_is_supported(self) -> None:
        self.assertEqual(Settings(AMAP_MAPS_API_KEY="test-key").amap_api_key, "test-key")

    def test_stage_preflight_only_checks_selected_stage(self) -> None:
        args = run_pipeline.build_parser().parse_args(["--stage", "sft-request"])
        stages = run_pipeline.normalize_stages(args.stage)
        required = run_pipeline.required_files_for_stages(args, stages)
        self.assertEqual(set(required), {"SFT 请求生成入口"})

    def test_pricing_estimate_adds_optional_entry(self) -> None:
        args = run_pipeline.build_parser().parse_args(["--stage", "pricing", "--estimate-prices"])
        stages = run_pipeline.normalize_stages(args.stage)
        required = run_pipeline.required_files_for_stages(args, stages)
        self.assertIn("强模型票价估价", required)


if __name__ == "__main__":
    unittest.main()
