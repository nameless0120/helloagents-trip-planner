# Rule Eval Report: 260507_realbudget_standard_w10

- records: 200
- generations: `training/outputs/eval/by_model/sft_qwen25_7b_v3_1000_cp2_v1/260507_realbudget_standard_w10/generations.jsonl`
- records_path: `training/data/v3/eval/records.jsonl`

## Boolean Metrics

| Metric | Pass | Total | Rate |
| --- | ---: | ---: | ---: |
| accommodation_type_ok | 200 | 200 | 100.00% |
| attraction_budget_consistent | 66 | 200 | 33.00% |
| attraction_budget_party_relation_ok | 174 | 200 | 87.00% |
| attraction_count_ok | 197 | 200 | 98.50% |
| attraction_diversity_ok | 180 | 200 | 90.00% |
| attraction_grounding_ok | 197 | 200 | 98.50% |
| attraction_repeat_limit_ok | 180 | 200 | 90.00% |
| budget_arithmetic_consistent | 161 | 200 | 80.50% |
| budget_consistent | 161 | 200 | 80.50% |
| budget_level_aligned | 151 | 200 | 75.50% |
| budget_preference_aligned | 151 | 200 | 75.50% |
| budget_relationship_ok | 105 | 200 | 52.50% |
| budget_selection_ok | 112 | 200 | 56.00% |
| budget_user_constraint_ok | 200 | 200 | 100.00% |
| budget_within_user_budget | 199 | 200 | 99.50% |
| city_ok | 200 | 200 | 100.00% |
| date_range_ok | 200 | 200 | 100.00% |
| day_dates_ok | 200 | 200 | 100.00% |
| day_index_ok | 200 | 200 | 100.00% |
| days_len_ok | 200 | 200 | 100.00% |
| dpo_soft_pass | 115 | 200 | 57.50% |
| dpo_soft_recomputed_budget_pass | 88 | 200 | 44.00% |
| hard_pass | 189 | 200 | 94.50% |
| hotel_budget_covers_nights | 176 | 200 | 88.00% |
| hotel_budget_relation_ok | 176 | 200 | 88.00% |
| hotel_distance_placeholder_ok | 200 | 200 | 100.00% |
| hotel_grounding_ok | 200 | 200 | 100.00% |
| invalid_hotel_name_ok | 200 | 200 | 100.00% |
| json_extract_ok | 200 | 200 | 100.00% |
| legacy_hard_pass | 117 | 200 | 58.50% |
| location_object_ok | 200 | 200 | 100.00% |
| meal_budget_consistent | 0 | 200 | 0.00% |
| meal_complete | 200 | 200 | 100.00% |
| meal_cost_scale_ok | 139 | 200 | 69.50% |
| meal_diversity_ok | 174 | 200 | 87.00% |
| meal_grounding_ok | 193 | 200 | 96.50% |
| meal_lunch_dinner_same_day_ok | 195 | 200 | 97.50% |
| meal_repeat_limit_ok | 178 | 200 | 89.00% |
| meal_specific_ok | 200 | 200 | 100.00% |
| meal_valid_semantics_ok | 193 | 200 | 96.50% |
| middle_hotel_ok | 200 | 200 | 100.00% |
| recomputed_budget_fit_ok | 112 | 200 | 56.00% |
| recomputed_budget_hard_ok | 198 | 200 | 99.00% |
| recomputed_budget_level_aligned | 112 | 200 | 56.00% |
| recomputed_budget_preference_aligned | 112 | 200 | 56.00% |
| recomputed_budget_user_constraint_ok | 198 | 200 | 99.00% |
| recomputed_budget_within_user_budget | 199 | 200 | 99.50% |
| schema_ok | 200 | 200 | 100.00% |
| sft_budget_semantic_hard_pass | 99 | 200 | 49.50% |
| sft_hard_pass | 189 | 200 | 94.50% |
| sft_no_budget_sum_hard_pass | 189 | 200 | 94.50% |
| sft_strict_hard_pass | 0 | 200 | 0.00% |
| transportation_budget_nonnegative | 200 | 200 | 100.00% |
| weather_dates_ok | 200 | 200 | 100.00% |
| weather_match | 200 | 200 | 100.00% |

## Numeric Metrics

```json
{
  "attraction_diversity_unique_rate": {
    "avg": 0.9886,
    "p50": 1.0,
    "p90": 1.0
  },
  "attraction_grounding_rate": {
    "avg": 0.9984,
    "p50": 1.0,
    "p90": 1.0
  },
  "hotel_grounding_rate": {
    "avg": 1.0,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_diversity_unique_rate": {
    "avg": 0.8885,
    "p50": 0.9167,
    "p90": 1.0
  },
  "meal_food_pois_grounding_rate": {
    "avg": 0.9948,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_grounding_rate": {
    "avg": 0.9948,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_semantic_valid_rate": {
    "avg": 0.9952,
    "p50": 1.0,
    "p90": 1.0
  },
  "recomputed_budget_per_person_day": {
    "avg": 595.0327,
    "p50": 509.33,
    "p90": 963.27
  },
  "recomputed_budget_total": {
    "avg": 5698.605,
    "p50": 4456.0,
    "p90": 11400.0
  }
}
```

## Failure Types

```json
{
  "meal_budget_inconsistent": 200,
  "attraction_budget_inconsistent": 134,
  "budget_relationship_mismatch": 95,
  "meal_cost_scale_too_low": 61,
  "budget_preference_mismatch": 49,
  "budget_arithmetic_inconsistent": 39,
  "hotel_budget_underestimated": 24,
  "meal_repeat_too_many": 22,
  "attraction_repeat_too_many": 20,
  "meal_invalid_name": 7,
  "meal_same_day_lunch_dinner_repeat": 5,
  "too_many_attractions": 3
}
```

## Failure Examples

### v3_standard200_realbudget_eval_000000
- request: 昆明 2026-04-07->2026-04-09 days=3 transport=地铁+步行 hotel=高端酒店 prefs=['休闲慢游', '美食']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 2, "party_total": 2, "room_count": 1, "priced_nights": 2, "expected_min_total_hotels": 1500, "reported_total_hotels": 3000, "diff": 1500, "covers_nights": false}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 50, "expected_total_attractions": 100, "reported_total_attractions": 100, "meal_per_person_cost_sum": 810, "expected_total_meals": 1620, "reported_total_meals": 3200, "reported_total_transportation": 2500}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": false, "attraction_budget_party_relation_ok": true, "meal_cost_scale_ok": false, "budget_relationship_ok": false, "expected_total_hotels": 1500, "reported_total_hotels": 3000, "expected_total_attractions": 100, "reported_total_attractions": 100, "meal_scale_eval": {"ok": false, "party_total": 2, "budget_level": "premium", "per_person_lunch_dinner_floor": 70, "breakfast_policy": "excluded_from_meal_cost_scale", "meal_count": 9, "checked_count": 6, "failure_count": 2, "failures": [{"date": "2026-04-07", "type": "lunch", "name": "湖景坊·经典云南菜·过桥米线(海埂公园店)", "estimated_cost": 57, "min_expected_cost": 70}, {"date": "2026-04-08", "type": "lunch", "name": "密芷花园餐厅(西坝店)", "estimated_cost": 64, "min_expected_cost": 70}]}}}]`

### v3_standard200_realbudget_eval_000008
- request: 大理 2026-05-11->2026-05-13 days=3 transport=地铁+步行 hotel=舒适型酒店 prefs=['休闲慢游', '城市地标', '历史文化']
- errors: `[{"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 75, "expected_total_attractions": 150, "reported_total_attractions": 150, "meal_per_person_cost_sum": 464, "expected_total_meals": 928, "reported_total_meals": 1050, "reported_total_transportation": 800}}]`

### v3_standard200_realbudget_eval_000001
- request: 桂林 2026-09-04->2026-09-06 days=3 transport=公共交通 hotel=高端酒店 prefs=['艺术', '美食', '第一次来', '历史文化']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 4800, "total": 5800, "diff": -1000, "requested_budget": {"available": true, "amount": 7100, "scope": "total", "party_size": 2, "total": 7100, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "soft"}, "per_person_day": 966.67, "budget_level": "comfortable", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "soft", "amount": 7100, "target_min_ratio": 0.7, "target_max_ratio": 1.1, "target_min_total": 5000, "target_max_total": 7800, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 2, "room_count": 1, "priced_nights": 2, "expected_min_total_hotels": 2400, "reported_total_hotels": 2400, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 345, "expected_total_attractions": 690, "reported_total_attractions": 680, "meal_per_person_cost_sum": 521, "expected_total_meals": 1042, "reported_total_meals": 1120, "reported_total_transportation": 600}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 345, "expected_total_attractions": 690, "reported_total_attractions": 680, "meal_per_person_cost_sum": 521, "expected_total_meals": 1042, "reported_total_meals": 1120, "reported_total_transportation": 600}}]`

### v3_standard200_realbudget_eval_000007
- request: 成都 2026-05-11->2026-05-13 days=3 transport=地铁+步行 hotel=舒适型酒店 prefs=['美食', '城市公园', '休闲慢游']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 165, "expected_total_attractions": 330, "reported_total_attractions": 320, "meal_per_person_cost_sum": 720, "expected_total_meals": 1440, "reported_total_meals": 1580, "reported_total_transportation": 600}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 165, "expected_total_attractions": 330, "reported_total_attractions": 320, "meal_per_person_cost_sum": 720, "expected_total_meals": 1440, "reported_total_meals": 1580, "reported_total_transportation": 600}}]`

### v3_standard200_realbudget_eval_000005
- request: 广州 2026-07-06->2026-07-08 days=3 transport=地铁+步行 hotel=经济型酒店 prefs=['博物馆', '城市公园', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 170, "expected_total_attractions": 340, "reported_total_attractions": 340, "meal_per_person_cost_sum": 535, "expected_total_meals": 1070, "reported_total_meals": 1060, "reported_total_transportation": 500}}]`

### v3_standard200_realbudget_eval_000006
- request: 南京 2026-07-06->2026-07-09 days=4 transport=打车 hotel=经济型酒店 prefs=['老人友好', '美食', '城市公园', '休闲慢游']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 100, "expected_total_attractions": 300, "reported_total_attractions": 240, "meal_per_person_cost_sum": 824, "expected_total_meals": 2472, "reported_total_meals": 2060, "reported_total_transportation": 600}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 100, "expected_total_attractions": 300, "reported_total_attractions": 240, "meal_per_person_cost_sum": 824, "expected_total_meals": 2472, "reported_total_meals": 2060, "reported_total_transportation": 600}}]`

### v3_standard200_realbudget_eval_000010
- request: 西安 2026-08-05->2026-08-08 days=4 transport=公共交通 hotel=经济型酒店 prefs=['城市公园', '美食']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "西安碑林博物馆", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-08-05", "day_index": 0, "name": "西安碑林博物馆"}, {"date": "2026-08-08", "day_index": 3, "name": "西安碑林博物馆"}]}]}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 3900, "total": 4800, "diff": -900, "requested_budget": {"available": true, "amount": 6600, "scope": "total", "party_size": 2, "total": 6600, "source": "budget_constraint", "budget_level": "standard", "strictness": "soft"}, "per_person_day": 600.0, "budget_level": "standard", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "standard", "strictness": "soft", "amount": 6600, "target_min_ratio": 0.6, "target_max_ratio": 1.05, "target_min_total": 4000, "target_max_total": 6900, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 2, "room_count": 1, "priced_nights": 3, "expected_min_total_hotels": 750, "reported_total_hotels": 750, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 430, "expected_total_attractions": 860, "reported_total_attractions": 748, "meal_per_person_cost_sum": 511, "expected_total_meals": 1022, "reported_total_meals": 1402, "reported_total_transportation": 1000}}]`

### v3_standard200_realbudget_eval_000004
- request: 张家界 2026-05-11->2026-05-15 days=5 transport=地铁+步行 hotel=舒适型酒店 prefs=['亲子', '城市漫步', '历史文化']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 400, "expected_total_attractions": 1600, "reported_total_attractions": 1920, "meal_per_person_cost_sum": 766, "expected_total_meals": 3064, "reported_total_meals": 2944, "reported_total_transportation": 400}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 400, "expected_total_attractions": 1600, "reported_total_attractions": 1920, "meal_per_person_cost_sum": 766, "expected_total_meals": 3064, "reported_total_meals": 2944, "reported_total_transportation": 400}}]`

### v3_standard200_realbudget_eval_000002
- request: 杭州 2026-05-01->2026-05-05 days=5 transport=公共交通 hotel=经济型酒店 prefs=['美食', '休闲慢游', '户外轻徒步', '城市漫步']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 230, "expected_total_attractions": 230, "reported_total_attractions": 250, "meal_per_person_cost_sum": 1137, "expected_total_meals": 1137, "reported_total_meals": 1320, "reported_total_transportation": 630}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 230, "expected_total_attractions": 230, "reported_total_attractions": 250, "meal_per_person_cost_sum": 1137, "expected_total_meals": 1137, "reported_total_meals": 1320, "reported_total_transportation": 630}}]`

### v3_standard200_realbudget_eval_000003
- request: 西安 2025-05-07->2025-05-11 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '历史文化', '购物商圈']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "西安博物院", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2025-05-10", "day_index": 3, "name": "西安博物院"}, {"date": "2025-05-11", "day_index": 4, "name": "西安博物院"}]}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 319, "expected_total_attractions": 957, "reported_total_attractions": 1197, "meal_per_person_cost_sum": 802, "expected_total_meals": 2406, "reported_total_meals": 2730, "reported_total_transportation": 1000}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 319, "expected_total_attractions": 957, "reported_total_attractions": 1197, "meal_per_person_cost_sum": 802, "expected_total_meals": 2406, "reported_total_meals": 2730, "reported_total_transportation": 1000}}]`

### v3_standard200_realbudget_eval_000014
- request: 成都 2026-06-06->2026-06-07 days=2 transport=打车 hotel=经济型酒店 prefs=['小众展览', '美食', '城市地标']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 115, "expected_total_attractions": 460, "reported_total_attractions": 520, "meal_per_person_cost_sum": 534, "expected_total_meals": 2136, "reported_total_meals": 1880, "reported_total_transportation": 400}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 115, "expected_total_attractions": 460, "reported_total_attractions": 520, "meal_per_person_cost_sum": 534, "expected_total_meals": 2136, "reported_total_meals": 1880, "reported_total_transportation": 400}}]`

### v3_standard200_realbudget_eval_000013
- request: 武汉 2026-05-09->2026-05-11 days=3 transport=公共交通 hotel=舒适型酒店 prefs=['亲子', '老人友好', '第一次来', '城市公园']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 6, "hotel_room_count": 3, "attraction_ticket_sum": 206, "expected_total_attractions": 1236, "reported_total_attractions": 1296, "meal_per_person_cost_sum": 700, "expected_total_meals": 4200, "reported_total_meals": 3504, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 6, "hotel_room_count": 3, "attraction_ticket_sum": 206, "expected_total_attractions": 1236, "reported_total_attractions": 1296, "meal_per_person_cost_sum": 700, "expected_total_meals": 4200, "reported_total_meals": 3504, "reported_total_transportation": 200}}]`

### v3_standard200_realbudget_eval_000018
- request: 天津 2026-07-06->2026-07-07 days=2 transport=打车 hotel=舒适型酒店 prefs=['老人友好', '夜市夜景', '艺术', '第一次来']
- errors: `[{"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 130, "expected_total_attractions": 390, "reported_total_attractions": 390, "meal_per_person_cost_sum": 325, "expected_total_meals": 975, "reported_total_meals": 819, "reported_total_transportation": 100}}]`

### v3_standard200_realbudget_eval_000011
- request: 福州 2026-06-21->2026-06-24 days=4 transport=打车 hotel=经济型酒店 prefs=['第一次来', '城市漫步']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 156, "expected_total_attractions": 312, "reported_total_attractions": 306, "meal_per_person_cost_sum": 639, "expected_total_meals": 1278, "reported_total_meals": 1894, "reported_total_transportation": 1400}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 156, "expected_total_attractions": 312, "reported_total_attractions": 306, "meal_per_person_cost_sum": 639, "expected_total_meals": 1278, "reported_total_meals": 1894, "reported_total_transportation": 1400}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": true, "meal_cost_scale_ok": false, "budget_relationship_ok": false, "expected_total_hotels": 600, "reported_total_hotels": 600, "expected_total_attractions": 312, "reported_total_attractions": 306, "meal_scale_eval": {"ok": false, "party_total": 2, "budget_level": "standard", "per_person_lunch_dinner_floor": 35, "breakfast_policy": "excluded_from_meal_cost_scale", "meal_count": 12, "checked_count": 8, "failure_count": 1, "failures": [{"date": "2026-06-21", "type": "lunch", "name": "后街捞化", "estimated_cost": 27, "min_expected_cost": 35}]}}}]`

### v3_standard200_realbudget_eval_000012
- request: 洛阳 2025-05-07->2025-05-10 days=4 transport=打车 hotel=高端酒店 prefs=['休闲慢游', '第一次来']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "隋唐城遗址植物园", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2025-05-07", "day_index": 0, "name": "隋唐城遗址植物园"}, {"date": "2025-05-10", "day_index": 3, "name": "隋唐城遗址植物园"}]}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 320, "expected_total_attractions": 960, "reported_total_attractions": 1200, "meal_per_person_cost_sum": 648, "expected_total_meals": 1944, "reported_total_meals": 3690, "reported_total_transportation": 8700}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 320, "expected_total_attractions": 960, "reported_total_attractions": 1200, "meal_per_person_cost_sum": 648, "expected_total_meals": 1944, "reported_total_meals": 3690, "reported_total_transportation": 8700}}]`

### v3_standard200_realbudget_eval_000017
- request: 苏州 2026-05-09->2026-05-11 days=3 transport=地铁+步行 hotel=亲子酒店 prefs=['亲子', '历史文化', '休闲慢游', '户外轻徒步']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 7801, "total": 8801, "diff": -1000, "requested_budget": {"available": true, "amount": 10000, "scope": "total", "party_size": 3, "total": 10000, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "soft"}, "per_person_day": 977.89, "budget_level": "comfortable", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "soft", "amount": 10000, "target_min_ratio": 0.7, "target_max_ratio": 1.1, "target_min_total": 7000, "target_max_total": 11000, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 3, "room_count": 2, "priced_nights": 2, "expected_min_total_hotels": 5000, "reported_total_hotels": 5000, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 140, "expected_total_attractions": 420, "reported_total_attractions": 435, "meal_per_person_cost_sum": 449, "expected_total_meals": 1347, "reported_total_meals": 1866, "reported_total_transportation": 500}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 140, "expected_total_attractions": 420, "reported_total_attractions": 435, "meal_per_person_cost_sum": 449, "expected_total_meals": 1347, "reported_total_meals": 1866, "reported_total_transportation": 500}}]`

### v3_standard200_realbudget_eval_000016
- request: 苏州 2026-06-06->2026-06-08 days=3 transport=公共交通 hotel=民宿 prefs=['海滨度假', '城市公园', '主题乐园', '清真']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 1598, "total": 1698, "diff": -100, "requested_budget": {"available": true, "amount": 2800, "scope": "total", "party_size": 2, "total": 2800, "source": "budget_constraint", "budget_level": "limited", "strictness": "soft"}, "per_person_day": 283.0, "budget_level": "limited", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "limited", "strictness": "soft", "amount": 2800, "target_min_ratio": 0.72, "target_max_ratio": 1.05, "target_min_total": 2000, "target_max_total": 2900, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 2, "room_count": 1, "priced_nights": 2, "expected_min_total_hotels": 600, "reported_total_hotels": 600, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 151, "expected_total_attractions": 302, "reported_total_attractions": 270, "meal_per_person_cost_sum": 201, "expected_total_meals": 402, "reported_total_meals": 628, "reported_total_transportation": 100}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 151, "expected_total_attractions": 302, "reported_total_attractions": 270, "meal_per_person_cost_sum": 201, "expected_total_meals": 402, "reported_total_meals": 628, "reported_total_transportation": 100}}]`

### v3_standard200_realbudget_eval_000021
- request: 上海 2026-06-21->2026-06-22 days=2 transport=地铁+步行 hotel=经济型酒店 prefs=['老人友好', '休闲慢游', '城市漫步', '主题乐园']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 1180, "total": 1380, "diff": -200, "requested_budget": {"available": true, "amount": 1700, "scope": "total", "party_size": 2, "total": 1700, "source": "budget_constraint", "budget_level": "limited", "strictness": "soft"}, "per_person_day": 345.0, "budget_level": "limited", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "limited", "strictness": "soft", "amount": 1700, "target_min_ratio": 0.72, "target_max_ratio": 1.05, "target_min_total": 1200, "target_max_total": 1800, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 1, "party_total": 2, "room_count": 1, "priced_nights": 1, "expected_min_total_hotels": 250, "reported_total_hotels": 250, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 70, "expected_total_attractions": 140, "reported_total_attractions": 140, "meal_per_person_cost_sum": 279, "expected_total_meals": 558, "reported_total_meals": 550, "reported_total_transportation": 240}}]`

### v3_standard200_realbudget_eval_000009
- request: 苏州 2026-04-30->2026-05-04 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['亲子', '城市地标', '第一次来', '城市漫步']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "留园", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-05-01", "day_index": 1, "name": "留园"}, {"date": "2026-05-04", "day_index": 4, "name": "留园"}]}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 185, "expected_total_attractions": 740, "reported_total_attractions": 1040, "meal_per_person_cost_sum": 1150, "expected_total_meals": 4600, "reported_total_meals": 4260, "reported_total_transportation": 1000}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 185, "expected_total_attractions": 740, "reported_total_attractions": 1040, "meal_per_person_cost_sum": 1150, "expected_total_meals": 4600, "reported_total_meals": 4260, "reported_total_transportation": 1000}}]`

### v3_standard200_realbudget_eval_000015
- request: 南京 2026-04-07->2026-04-08 days=2 transport=地铁+步行 hotel=经济型酒店 prefs=['亲子', '休闲慢游', '历史文化']
- errors: `[{"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 65, "expected_total_attractions": 195, "reported_total_attractions": 195, "meal_per_person_cost_sum": 369, "expected_total_meals": 1107, "reported_total_meals": 1437, "reported_total_transportation": 100}}, {"stage": "rule", "type": "budget_preference_mismatch", "details": {"part_sum": 2232, "total": 2232, "diff": 0, "requested_budget": {"available": true, "amount": 4300, "scope": "total", "party_size": 3, "total": 4300, "source": "budget_constraint", "budget_level": "standard", "strictness": "soft"}, "per_person_day": 372.0, "budget_level": "standard", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "standard", "strictness": "soft", "amount": 4300, "target_min_ratio": 0.6, "target_max_ratio": 1.05, "target_min_total": 2600, "target_max_total": 4500, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": true, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 1, "party_total": 3, "room_count": 2, "priced_nights": 1, "expected_min_total_hotels": 500, "reported_total_hotels": 500, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`
