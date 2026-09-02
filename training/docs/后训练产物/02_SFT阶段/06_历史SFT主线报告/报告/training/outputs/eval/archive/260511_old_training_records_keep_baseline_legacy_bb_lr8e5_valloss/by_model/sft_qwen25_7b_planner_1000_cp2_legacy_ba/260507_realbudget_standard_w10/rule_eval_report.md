# Rule Eval Report: 260507_realbudget_standard_w10

- records: 200
- generations: `training/outputs/eval/by_model/sft_qwen25_7b_v3_1000_cp2_v2a/260507_realbudget_standard_w10/generations.jsonl`
- records_path: `training/data/v3/eval/records.jsonl`

## Boolean Metrics

| Metric | Pass | Total | Rate |
| --- | ---: | ---: | ---: |
| accommodation_type_ok | 200 | 200 | 100.00% |
| attraction_budget_consistent | 61 | 200 | 30.50% |
| attraction_budget_party_relation_ok | 175 | 200 | 87.50% |
| attraction_count_ok | 200 | 200 | 100.00% |
| attraction_diversity_ok | 186 | 200 | 93.00% |
| attraction_grounding_ok | 197 | 200 | 98.50% |
| attraction_repeat_limit_ok | 186 | 200 | 93.00% |
| budget_arithmetic_consistent | 150 | 200 | 75.00% |
| budget_consistent | 150 | 200 | 75.00% |
| budget_level_aligned | 151 | 200 | 75.50% |
| budget_preference_aligned | 151 | 200 | 75.50% |
| budget_relationship_ok | 116 | 200 | 58.00% |
| budget_selection_ok | 114 | 200 | 57.00% |
| budget_user_constraint_ok | 200 | 200 | 100.00% |
| budget_within_user_budget | 200 | 200 | 100.00% |
| city_ok | 200 | 200 | 100.00% |
| date_range_ok | 200 | 200 | 100.00% |
| day_dates_ok | 200 | 200 | 100.00% |
| day_index_ok | 200 | 200 | 100.00% |
| days_len_ok | 200 | 200 | 100.00% |
| dpo_soft_pass | 112 | 200 | 56.00% |
| dpo_soft_recomputed_budget_pass | 84 | 200 | 42.00% |
| hard_pass | 191 | 200 | 95.50% |
| hotel_budget_covers_nights | 174 | 200 | 87.00% |
| hotel_budget_relation_ok | 177 | 200 | 88.50% |
| hotel_distance_placeholder_ok | 200 | 200 | 100.00% |
| hotel_grounding_ok | 200 | 200 | 100.00% |
| invalid_hotel_name_ok | 200 | 200 | 100.00% |
| json_extract_ok | 200 | 200 | 100.00% |
| legacy_hard_pass | 102 | 200 | 51.00% |
| location_object_ok | 200 | 200 | 100.00% |
| meal_budget_consistent | 2 | 200 | 1.00% |
| meal_complete | 200 | 200 | 100.00% |
| meal_cost_scale_ok | 152 | 200 | 76.00% |
| meal_diversity_ok | 163 | 200 | 81.50% |
| meal_grounding_ok | 194 | 200 | 97.00% |
| meal_lunch_dinner_same_day_ok | 185 | 200 | 92.50% |
| meal_repeat_limit_ok | 173 | 200 | 86.50% |
| meal_specific_ok | 200 | 200 | 100.00% |
| meal_valid_semantics_ok | 196 | 200 | 98.00% |
| middle_hotel_ok | 200 | 200 | 100.00% |
| recomputed_budget_fit_ok | 114 | 200 | 57.00% |
| recomputed_budget_hard_ok | 197 | 200 | 98.50% |
| recomputed_budget_level_aligned | 114 | 200 | 57.00% |
| recomputed_budget_preference_aligned | 114 | 200 | 57.00% |
| recomputed_budget_user_constraint_ok | 197 | 200 | 98.50% |
| recomputed_budget_within_user_budget | 199 | 200 | 99.50% |
| schema_ok | 200 | 200 | 100.00% |
| sft_budget_semantic_hard_pass | 109 | 200 | 54.50% |
| sft_hard_pass | 191 | 200 | 95.50% |
| sft_no_budget_sum_hard_pass | 191 | 200 | 95.50% |
| sft_strict_hard_pass | 0 | 200 | 0.00% |
| transportation_budget_nonnegative | 200 | 200 | 100.00% |
| weather_dates_ok | 200 | 200 | 100.00% |
| weather_match | 200 | 200 | 100.00% |

## Numeric Metrics

```json
{
  "attraction_diversity_unique_rate": {
    "avg": 0.9907,
    "p50": 1.0,
    "p90": 1.0
  },
  "attraction_grounding_rate": {
    "avg": 0.9985,
    "p50": 1.0,
    "p90": 1.0
  },
  "hotel_grounding_rate": {
    "avg": 1.0,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_diversity_unique_rate": {
    "avg": 0.8842,
    "p50": 0.9333,
    "p90": 1.0
  },
  "meal_food_pois_grounding_rate": {
    "avg": 0.9963,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_grounding_rate": {
    "avg": 0.9963,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_semantic_valid_rate": {
    "avg": 0.9979,
    "p50": 1.0,
    "p90": 1.0
  },
  "recomputed_budget_per_person_day": {
    "avg": 595.0138,
    "p50": 501.0,
    "p90": 956.5
  },
  "recomputed_budget_total": {
    "avg": 5694.865,
    "p50": 4369.0,
    "p90": 10620.0
  }
}
```

## Failure Types

```json
{
  "meal_budget_inconsistent": 200,
  "attraction_budget_inconsistent": 139,
  "budget_relationship_mismatch": 84,
  "budget_arithmetic_inconsistent": 50,
  "budget_preference_mismatch": 49,
  "meal_cost_scale_too_low": 48,
  "meal_repeat_too_many": 27,
  "hotel_budget_underestimated": 26,
  "meal_same_day_lunch_dinner_repeat": 15,
  "attraction_repeat_too_many": 14,
  "meal_invalid_name": 4,
  "meal_grounding_miss": 2
}
```

## Failure Examples

### v3_standard200_realbudget_eval_000008
- request: 大理 2026-05-11->2026-05-13 days=3 transport=地铁+步行 hotel=舒适型酒店 prefs=['休闲慢游', '城市地标', '历史文化']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 115, "expected_total_attractions": 230, "reported_total_attractions": 260, "meal_per_person_cost_sum": 460, "expected_total_meals": 920, "reported_total_meals": 1040, "reported_total_transportation": 600}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 115, "expected_total_attractions": 230, "reported_total_attractions": 260, "meal_per_person_cost_sum": 460, "expected_total_meals": 920, "reported_total_meals": 1040, "reported_total_transportation": 600}}]`

### v3_standard200_realbudget_eval_000001
- request: 桂林 2026-09-04->2026-09-06 days=3 transport=公共交通 hotel=高端酒店 prefs=['艺术', '美食', '第一次来', '历史文化']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 4900, "total": 5900, "diff": -1000, "requested_budget": {"available": true, "amount": 7100, "scope": "total", "party_size": 2, "total": 7100, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "soft"}, "per_person_day": 983.33, "budget_level": "comfortable", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "soft", "amount": 7100, "target_min_ratio": 0.7, "target_max_ratio": 1.1, "target_min_total": 5000, "target_max_total": 7800, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 2, "room_count": 1, "priced_nights": 2, "expected_min_total_hotels": 2400, "reported_total_hotels": 2400, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 345, "expected_total_attractions": 690, "reported_total_attractions": 670, "meal_per_person_cost_sum": 490, "expected_total_meals": 980, "reported_total_meals": 1430, "reported_total_transportation": 400}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 345, "expected_total_attractions": 690, "reported_total_attractions": 670, "meal_per_person_cost_sum": 490, "expected_total_meals": 980, "reported_total_meals": 1430, "reported_total_transportation": 400}}]`

### v3_standard200_realbudget_eval_000005
- request: 广州 2026-07-06->2026-07-08 days=3 transport=地铁+步行 hotel=经济型酒店 prefs=['博物馆', '城市公园', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 20, "expected_total_attractions": 40, "reported_total_attractions": 40, "meal_per_person_cost_sum": 517, "expected_total_meals": 1034, "reported_total_meals": 1080, "reported_total_transportation": 600}}]`

### v3_standard200_realbudget_eval_000007
- request: 成都 2026-05-11->2026-05-13 days=3 transport=地铁+步行 hotel=舒适型酒店 prefs=['美食', '城市公园', '休闲慢游']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 2800, "total": 3800, "diff": -1000, "requested_budget": {"available": true, "amount": 4600, "scope": "total", "party_size": 2, "total": 4600, "source": "budget_constraint", "budget_level": "standard", "strictness": "hard"}, "per_person_day": 633.33, "budget_level": "standard", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "standard", "strictness": "hard", "amount": 4600, "target_min_ratio": 0.6, "target_max_ratio": 1.0, "target_min_total": 2800, "target_max_total": 4600, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 2, "room_count": 1, "priced_nights": 2, "expected_min_total_hotels": 900, "reported_total_hotels": 900, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 115, "expected_total_attractions": 230, "reported_total_attractions": 260, "meal_per_person_cost_sum": 823, "expected_total_meals": 1646, "reported_total_meals": 1540, "reported_total_transportation": 100}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 115, "expected_total_attractions": 230, "reported_total_attractions": 260, "meal_per_person_cost_sum": 823, "expected_total_meals": 1646, "reported_total_meals": 1540, "reported_total_transportation": 100}}]`

### v3_standard200_realbudget_eval_000000
- request: 昆明 2026-04-07->2026-04-09 days=3 transport=地铁+步行 hotel=高端酒店 prefs=['休闲慢游', '美食']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 2, "party_total": 2, "room_count": 1, "priced_nights": 2, "expected_min_total_hotels": 1500, "reported_total_hotels": 3000, "diff": 1500, "covers_nights": false}}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 6500, "total": 7400, "diff": -900, "requested_budget": {"available": true, "amount": 9800, "scope": "total", "party_size": 2, "total": 9800, "source": "budget_constraint", "budget_level": "premium", "strictness": "hard"}, "per_person_day": 1233.33, "budget_level": "premium", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "premium", "strictness": "hard", "amount": 9800, "target_min_ratio": 0.75, "target_max_ratio": 1.0, "target_min_total": 7400, "target_max_total": 9800, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 2, "room_count": 1, "priced_nights": 2, "expected_min_total_hotels": 1500, "reported_total_hotels": 3000, "diff": 1500, "covers_nights": false}, "hotel_budget_covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 293, "expected_total_attractions": 586, "reported_total_attractions": 646, "meal_per_person_cost_sum": 448, "expected_total_meals": 896, "reported_total_meals": 1854, "reported_total_transportation": 1000}}]`

### v3_standard200_realbudget_eval_000006
- request: 南京 2026-07-06->2026-07-09 days=4 transport=打车 hotel=经济型酒店 prefs=['老人友好', '美食', '城市公园', '休闲慢游']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 4950, "total": 5950, "diff": -1000, "requested_budget": {"available": true, "amount": 5600, "scope": "total", "party_size": 3, "total": 5600, "source": "budget_constraint", "budget_level": "limited", "strictness": "soft"}, "per_person_day": 495.83, "budget_level": "limited", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "limited", "strictness": "soft", "amount": 5600, "target_min_ratio": 0.72, "target_max_ratio": 1.05, "target_min_total": 4000, "target_max_total": 5900, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 3, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 1500, "reported_total_hotels": 1500, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 100, "expected_total_attractions": 300, "reported_total_attractions": 240, "meal_per_person_cost_sum": 729, "expected_total_meals": 2187, "reported_total_meals": 2610, "reported_total_transportation": 600}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 100, "expected_total_attractions": 300, "reported_total_attractions": 240, "meal_per_person_cost_sum": 729, "expected_total_meals": 2187, "reported_total_meals": 2610, "reported_total_transportation": 600}}]`

### v3_standard200_realbudget_eval_000010
- request: 西安 2026-08-05->2026-08-08 days=4 transport=公共交通 hotel=经济型酒店 prefs=['城市公园', '美食']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "西安博物院", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-08-08", "day_index": 3, "name": "西安博物院"}, {"date": "2026-08-08", "day_index": 3, "name": "西安博物院"}]}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 2, "room_count": 1, "priced_nights": 3, "expected_min_total_hotels": 750, "reported_total_hotels": 1500, "diff": 750, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 319, "expected_total_attractions": 638, "reported_total_attractions": 628, "meal_per_person_cost_sum": 661, "expected_total_meals": 1322, "reported_total_meals": 1972, "reported_total_transportation": 700}}]`

### v3_standard200_realbudget_eval_000004
- request: 张家界 2026-05-11->2026-05-15 days=5 transport=地铁+步行 hotel=舒适型酒店 prefs=['亲子', '城市漫步', '历史文化']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 442, "expected_total_attractions": 1768, "reported_total_attractions": 2244, "meal_per_person_cost_sum": 758, "expected_total_meals": 3032, "reported_total_meals": 2356, "reported_total_transportation": 1000}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 442, "expected_total_attractions": 1768, "reported_total_attractions": 2244, "meal_per_person_cost_sum": 758, "expected_total_meals": 3032, "reported_total_meals": 2356, "reported_total_transportation": 1000}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": false, "meal_cost_scale_ok": true, "budget_relationship_ok": false, "expected_total_hotels": 3200, "reported_total_hotels": 3200, "expected_total_attractions": 1768, "reported_total_attractions": 2244, "meal_scale_eval": {"ok": true, "party_total": 4, "budget_level": "standard", "per_person_lunch_dinner_floor": 35, "breakfast_policy": "excluded_from_meal_cost_scale", "meal_count": 15, "checked_count": 10, "failure_count": 0, "failures": []}}}]`

### v3_standard200_realbudget_eval_000003
- request: 西安 2025-05-07->2025-05-11 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '历史文化', '购物商圈']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "西安博物院", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2025-05-10", "day_index": 3, "name": "西安博物院"}, {"date": "2025-05-11", "day_index": 4, "name": "西安博物院"}]}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 4, "party_total": 3, "room_count": 2, "priced_nights": 4, "expected_min_total_hotels": 3600, "reported_total_hotels": 4500, "diff": 900, "covers_nights": false}}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 9990, "total": 10090, "diff": -100, "requested_budget": {"available": true, "amount": 15700, "scope": "total", "party_size": 3, "total": 15700, "source": "budget_constraint", "budget_level": "standard", "strictness": "soft"}, "per_person_day": 672.67, "budget_level": "standard", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "standard", "strictness": "soft", "amount": 15700, "target_min_ratio": 0.6, "target_max_ratio": 1.05, "target_min_total": 9400, "target_max_total": 16500, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 4, "party_total": 3, "room_count": 2, "priced_nights": 4, "expected_min_total_hotels": 3600, "reported_total_hotels": 4500, "diff": 900, "covers_nights": false}, "hotel_budget_covers_nights": false}}]`

### v3_standard200_realbudget_eval_000002
- request: 杭州 2026-05-01->2026-05-05 days=5 transport=公共交通 hotel=经济型酒店 prefs=['美食', '休闲慢游', '户外轻徒步', '城市漫步']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "南宋德寿宫遗址博物馆", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-05-01", "day_index": 0, "name": "南宋德寿宫遗址博物馆"}, {"date": "2026-05-04", "day_index": 3, "name": "南宋德寿宫遗址博物馆"}]}]}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 2900, "total": 3000, "diff": -100, "requested_budget": {"available": true, "amount": 3400, "scope": "total", "party_size": 1, "total": 3400, "source": "budget_constraint", "budget_level": "limited", "strictness": "soft"}, "per_person_day": 600.0, "budget_level": "limited", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "limited", "strictness": "soft", "amount": 3400, "target_min_ratio": 0.72, "target_max_ratio": 1.05, "target_min_total": 2400, "target_max_total": 3600, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 4, "party_total": 1, "room_count": 1, "priced_nights": 4, "expected_min_total_hotels": 1000, "reported_total_hotels": 1000, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 160, "expected_total_attractions": 160, "reported_total_attractions": 150, "meal_per_person_cost_sum": 1023, "expected_total_meals": 1023, "reported_total_meals": 1450, "reported_total_transportation": 300}}]`

### v3_standard200_realbudget_eval_000014
- request: 成都 2026-06-06->2026-06-07 days=2 transport=打车 hotel=经济型酒店 prefs=['小众展览', '美食', '城市地标']
- errors: `[{"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 110, "expected_total_attractions": 440, "reported_total_attractions": 440, "meal_per_person_cost_sum": 500, "expected_total_meals": 2000, "reported_total_meals": 1660, "reported_total_transportation": 800}}]`

### v3_standard200_realbudget_eval_000013
- request: 武汉 2026-05-09->2026-05-11 days=3 transport=公共交通 hotel=舒适型酒店 prefs=['亲子', '老人友好', '第一次来', '城市公园']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 7400, "total": 7300, "diff": 100, "requested_budget": {"available": true, "amount": 12400, "scope": "total", "party_size": 6, "total": 12400, "source": "budget_constraint", "budget_level": "standard", "strictness": "soft"}, "per_person_day": 405.56, "budget_level": "standard", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "standard", "strictness": "soft", "amount": 12400, "target_min_ratio": 0.6, "target_max_ratio": 1.05, "target_min_total": 7400, "target_max_total": 13000, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 6, "room_count": 3, "priced_nights": 2, "expected_min_total_hotels": 2400, "reported_total_hotels": 2400, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 6, "hotel_room_count": 3, "attraction_ticket_sum": 83, "expected_total_attractions": 498, "reported_total_attractions": 558, "meal_per_person_cost_sum": 539, "expected_total_meals": 3234, "reported_total_meals": 3442, "reported_total_transportation": 1000}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 6, "hotel_room_count": 3, "attraction_ticket_sum": 83, "expected_total_attractions": 498, "reported_total_attractions": 558, "meal_per_person_cost_sum": 539, "expected_total_meals": 3234, "reported_total_meals": 3442, "reported_total_transportation": 1000}}]`

### v3_standard200_realbudget_eval_000012
- request: 洛阳 2025-05-07->2025-05-10 days=4 transport=打车 hotel=高端酒店 prefs=['休闲慢游', '第一次来']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "隋唐城遗址植物园", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2025-05-07", "day_index": 0, "name": "隋唐城遗址植物园"}, {"date": "2025-05-10", "day_index": 3, "name": "隋唐城遗址植物园"}]}]}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 18289, "total": 17300, "diff": 989, "requested_budget": {"available": true, "amount": 23100, "scope": "total", "party_size": 3, "total": 23100, "source": "budget_constraint", "budget_level": "premium", "strictness": "soft"}, "per_person_day": 1441.67, "budget_level": "premium", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "premium", "strictness": "soft", "amount": 23100, "target_min_ratio": 0.75, "target_max_ratio": 1.12, "target_min_total": 17300, "target_max_total": 25900, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 3, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 4500, "reported_total_hotels": 4500, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 240, "expected_total_attractions": 720, "reported_total_attractions": 720, "meal_per_person_cost_sum": 620, "expected_total_meals": 1860, "reported_total_meals": 2769, "reported_total_transportation": 10300}}]`

### v3_standard200_realbudget_eval_000011
- request: 福州 2026-06-21->2026-06-24 days=4 transport=打车 hotel=经济型酒店 prefs=['第一次来', '城市漫步']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 117, "expected_total_attractions": 234, "reported_total_attractions": 254, "meal_per_person_cost_sum": 869, "expected_total_meals": 1738, "reported_total_meals": 1686, "reported_total_transportation": 1660}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 117, "expected_total_attractions": 234, "reported_total_attractions": 254, "meal_per_person_cost_sum": 869, "expected_total_meals": 1738, "reported_total_meals": 1686, "reported_total_transportation": 1660}}]`

### v3_standard200_realbudget_eval_000017
- request: 苏州 2026-05-09->2026-05-11 days=3 transport=地铁+步行 hotel=亲子酒店 prefs=['亲子', '历史文化', '休闲慢游', '户外轻徒步']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 7802, "total": 8802, "diff": -1000, "requested_budget": {"available": true, "amount": 10000, "scope": "total", "party_size": 3, "total": 10000, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "soft"}, "per_person_day": 978.0, "budget_level": "comfortable", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "soft", "amount": 10000, "target_min_ratio": 0.7, "target_max_ratio": 1.1, "target_min_total": 7000, "target_max_total": 11000, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 3, "room_count": 2, "priced_nights": 2, "expected_min_total_hotels": 5000, "reported_total_hotels": 5000, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 135, "expected_total_attractions": 405, "reported_total_attractions": 405, "meal_per_person_cost_sum": 399, "expected_total_meals": 1197, "reported_total_meals": 1797, "reported_total_transportation": 600}}]`

### v3_standard200_realbudget_eval_000016
- request: 苏州 2026-06-06->2026-06-08 days=3 transport=公共交通 hotel=民宿 prefs=['海滨度假', '城市公园', '主题乐园', '清真']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "丝路回乡小吃店", "count": 3, "max_allowed": 2, "occurrences": [{"date": "2026-06-06", "type": "lunch", "name": "丝路回乡小吃店(西夏店)"}, {"date": "2026-06-07", "type": "dinner", "name": "丝路回乡小吃店(西夏店)"}, {"date": "2026-06-08", "type": "dinner", "name": "丝路回乡小吃店(西夏店)"}]}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 140, "expected_total_attractions": 280, "reported_total_attractions": 250, "meal_per_person_cost_sum": 208, "expected_total_meals": 416, "reported_total_meals": 540, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 140, "expected_total_attractions": 280, "reported_total_attractions": 250, "meal_per_person_cost_sum": 208, "expected_total_meals": 416, "reported_total_meals": 540, "reported_total_transportation": 200}}]`

### v3_standard200_realbudget_eval_000018
- request: 天津 2026-07-06->2026-07-07 days=2 transport=打车 hotel=舒适型酒店 prefs=['老人友好', '夜市夜景', '艺术', '第一次来']
- errors: `[{"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 130, "expected_total_attractions": 390, "reported_total_attractions": 390, "meal_per_person_cost_sum": 376, "expected_total_meals": 1128, "reported_total_meals": 1182, "reported_total_transportation": 300}}]`

### v3_standard200_realbudget_eval_000021
- request: 上海 2026-06-21->2026-06-22 days=2 transport=地铁+步行 hotel=经济型酒店 prefs=['老人友好', '休闲慢游', '城市漫步', '主题乐园']
- errors: `[{"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 70, "expected_total_attractions": 140, "reported_total_attractions": 140, "meal_per_person_cost_sum": 279, "expected_total_meals": 558, "reported_total_meals": 566, "reported_total_transportation": 200}}, {"stage": "rule", "type": "budget_preference_mismatch", "details": {"part_sum": 1156, "total": 1156, "diff": 0, "requested_budget": {"available": true, "amount": 1700, "scope": "total", "party_size": 2, "total": 1700, "source": "budget_constraint", "budget_level": "limited", "strictness": "soft"}, "per_person_day": 289.0, "budget_level": "limited", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "limited", "strictness": "soft", "amount": 1700, "target_min_ratio": 0.72, "target_max_ratio": 1.05, "target_min_total": 1200, "target_max_total": 1800, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": true, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 1, "party_total": 2, "room_count": 1, "priced_nights": 1, "expected_min_total_hotels": 250, "reported_total_hotels": 250, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_standard200_realbudget_eval_000009
- request: 苏州 2026-04-30->2026-05-04 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['亲子', '城市地标', '第一次来', '城市漫步']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "留园", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-05-01", "day_index": 1, "name": "留园"}, {"date": "2026-05-04", "day_index": 4, "name": "留园"}]}]}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 15400, "total": 15300, "diff": 100, "requested_budget": {"available": true, "amount": 20500, "scope": "total", "party_size": 4, "total": 20500, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "soft"}, "per_person_day": 765.0, "budget_level": "comfortable", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "soft", "amount": 20500, "target_min_ratio": 0.7, "target_max_ratio": 1.1, "target_min_total": 14300, "target_max_total": 22600, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 4, "party_total": 4, "room_count": 2, "priced_nights": 4, "expected_min_total_hotels": 10000, "reported_total_hotels": 10000, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 376, "expected_total_attractions": 1504, "reported_total_attractions": 2260, "meal_per_person_cost_sum": 1236, "expected_total_meals": 4944, "reported_total_meals": 3040, "reported_total_transportation": 100}}]`

### v3_standard200_realbudget_eval_000015
- request: 南京 2026-04-07->2026-04-08 days=2 transport=地铁+步行 hotel=经济型酒店 prefs=['亲子', '休闲慢游', '历史文化']
- errors: `[{"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 140, "expected_total_attractions": 420, "reported_total_attractions": 420, "meal_per_person_cost_sum": 396, "expected_total_meals": 1188, "reported_total_meals": 1413, "reported_total_transportation": 800}}]`
