# Rule Eval Report: 260513_rerank_final1200_standard_w10

- records: 200
- generations: `training/outputs/eval/by_model/sft_qwen25_7b_v3_260513_rerank_final1200/260513_rerank_final1200_standard_w10/generations.jsonl`
- records_path: `training/data/v3/eval/records.jsonl`

## Boolean Metrics

| Metric | Pass | Total | Rate |
| --- | ---: | ---: | ---: |
| accommodation_type_ok | 200 | 200 | 100.00% |
| attraction_budget_consistent | 71 | 200 | 35.50% |
| attraction_budget_party_relation_ok | 197 | 200 | 98.50% |
| attraction_count_ok | 200 | 200 | 100.00% |
| attraction_diversity_ok | 193 | 200 | 96.50% |
| attraction_grounding_ok | 200 | 200 | 100.00% |
| attraction_repeat_limit_ok | 193 | 200 | 96.50% |
| budget_arithmetic_consistent | 156 | 200 | 78.00% |
| budget_consistent | 156 | 200 | 78.00% |
| budget_level_aligned | 170 | 200 | 85.00% |
| budget_preference_aligned | 170 | 200 | 85.00% |
| budget_relationship_ok | 177 | 200 | 88.50% |
| budget_selection_ok | 149 | 200 | 74.50% |
| budget_user_constraint_ok | 199 | 200 | 99.50% |
| budget_within_user_budget | 195 | 200 | 97.50% |
| city_ok | 200 | 200 | 100.00% |
| date_range_ok | 200 | 200 | 100.00% |
| day_dates_ok | 200 | 200 | 100.00% |
| day_index_ok | 200 | 200 | 100.00% |
| days_len_ok | 200 | 200 | 100.00% |
| dpo_soft_pass | 152 | 200 | 76.00% |
| dpo_soft_recomputed_budget_pass | 138 | 200 | 69.00% |
| hard_pass | 196 | 200 | 98.00% |
| hotel_budget_covers_nights | 195 | 200 | 97.50% |
| hotel_budget_relation_ok | 199 | 200 | 99.50% |
| hotel_distance_placeholder_ok | 200 | 200 | 100.00% |
| hotel_grounding_ok | 200 | 200 | 100.00% |
| invalid_hotel_name_ok | 200 | 200 | 100.00% |
| json_extract_ok | 200 | 200 | 100.00% |
| legacy_hard_pass | 138 | 200 | 69.00% |
| location_object_ok | 200 | 200 | 100.00% |
| meal_budget_consistent | 0 | 200 | 0.00% |
| meal_complete | 200 | 200 | 100.00% |
| meal_cost_scale_ok | 180 | 200 | 90.00% |
| meal_diversity_ok | 187 | 200 | 93.50% |
| meal_grounding_ok | 197 | 200 | 98.50% |
| meal_lunch_dinner_same_day_ok | 199 | 200 | 99.50% |
| meal_repeat_limit_ok | 188 | 200 | 94.00% |
| meal_specific_ok | 200 | 200 | 100.00% |
| meal_valid_semantics_ok | 197 | 200 | 98.50% |
| middle_hotel_ok | 200 | 200 | 100.00% |
| recomputed_budget_fit_ok | 149 | 200 | 74.50% |
| recomputed_budget_hard_ok | 197 | 200 | 98.50% |
| recomputed_budget_level_aligned | 149 | 200 | 74.50% |
| recomputed_budget_preference_aligned | 149 | 200 | 74.50% |
| recomputed_budget_user_constraint_ok | 197 | 200 | 98.50% |
| recomputed_budget_within_user_budget | 187 | 200 | 93.50% |
| schema_ok | 200 | 200 | 100.00% |
| sft_budget_semantic_hard_pass | 169 | 200 | 84.50% |
| sft_hard_pass | 196 | 200 | 98.00% |
| sft_no_budget_sum_hard_pass | 196 | 200 | 98.00% |
| sft_strict_hard_pass | 0 | 200 | 0.00% |
| transportation_budget_nonnegative | 200 | 200 | 100.00% |
| weather_dates_ok | 200 | 200 | 100.00% |
| weather_match | 199 | 200 | 99.50% |

## Numeric Metrics

```json
{
  "attraction_diversity_unique_rate": {
    "avg": 0.9959,
    "p50": 1.0,
    "p90": 1.0
  },
  "attraction_grounding_rate": {
    "avg": 1.0,
    "p50": 1.0,
    "p90": 1.0
  },
  "hotel_grounding_rate": {
    "avg": 1.0,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_diversity_unique_rate": {
    "avg": 0.929,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_food_pois_grounding_rate": {
    "avg": 0.9983,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_grounding_rate": {
    "avg": 0.9983,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_semantic_valid_rate": {
    "avg": 0.9983,
    "p50": 1.0,
    "p90": 1.0
  },
  "recomputed_budget_per_person_day": {
    "avg": 747.6768,
    "p50": 616.6,
    "p90": 1315.67
  },
  "recomputed_budget_total": {
    "avg": 7045.91,
    "p50": 5670.0,
    "p90": 13788.0
  }
}
```

## Failure Types

```json
{
  "meal_budget_inconsistent": 200,
  "attraction_budget_inconsistent": 129,
  "budget_arithmetic_inconsistent": 44,
  "budget_preference_mismatch": 30,
  "budget_relationship_mismatch": 23,
  "meal_cost_scale_too_low": 20,
  "meal_repeat_too_many": 12,
  "attraction_repeat_too_many": 7,
  "hotel_budget_underestimated": 5,
  "meal_invalid_name": 3,
  "meal_same_day_lunch_dinner_repeat": 1,
  "weather_mismatch": 1,
  "budget_hard_constraint_exceeded": 1
}
```

## Failure Examples

### v3_standard200_realbudget_eval_000000
- request: 昆明 2026-04-07->2026-04-09 days=3 transport=地铁+步行 hotel=高端酒店 prefs=['休闲慢游', '美食']
- errors: `[{"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-04-07", "type": "dinner", "name": "石屏会馆", "reason": "unknown_food_semantics"}]}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 8400, "total": 7400, "diff": 1000, "requested_budget": {"available": true, "amount": 9800, "scope": "total", "party_size": 2, "total": 9800, "source": "budget_constraint", "budget_level": "premium", "strictness": "hard"}, "per_person_day": 1233.33, "budget_level": "premium", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "premium", "strictness": "hard", "amount": 9800, "target_min_ratio": 0.75, "target_max_ratio": 1.0, "target_min_total": 7400, "target_max_total": 9800, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 2, "room_count": 1, "priced_nights": 2, "expected_min_total_hotels": 2600, "reported_total_hotels": 2600, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 729, "expected_total_attractions": 1458, "reported_total_attractions": 1568, "meal_per_person_cost_sum": 884, "expected_total_meals": 1768, "reported_total_meals": 2032, "reported_total_transportation": 2200}}]`

### v3_standard200_realbudget_eval_000001
- request: 桂林 2026-09-04->2026-09-06 days=3 transport=公共交通 hotel=高端酒店 prefs=['艺术', '美食', '第一次来', '历史文化']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 345, "expected_total_attractions": 690, "reported_total_attractions": 750, "meal_per_person_cost_sum": 849, "expected_total_meals": 1698, "reported_total_meals": 2164, "reported_total_transportation": 900}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 345, "expected_total_attractions": 690, "reported_total_attractions": 750, "meal_per_person_cost_sum": 849, "expected_total_meals": 1698, "reported_total_meals": 2164, "reported_total_transportation": 900}}]`

### v3_standard200_realbudget_eval_000002
- request: 杭州 2026-05-01->2026-05-05 days=5 transport=公共交通 hotel=经济型酒店 prefs=['美食', '休闲慢游', '户外轻徒步', '城市漫步']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 160, "expected_total_attractions": 160, "reported_total_attractions": 170, "meal_per_person_cost_sum": 1126, "expected_total_meals": 1126, "reported_total_meals": 1160, "reported_total_transportation": 150}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 160, "expected_total_attractions": 160, "reported_total_attractions": 170, "meal_per_person_cost_sum": 1126, "expected_total_meals": 1126, "reported_total_meals": 1160, "reported_total_transportation": 150}}]`

### v3_standard200_realbudget_eval_000004
- request: 张家界 2026-05-11->2026-05-15 days=5 transport=地铁+步行 hotel=舒适型酒店 prefs=['亲子', '城市漫步', '历史文化']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "七十二奇楼景区", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-05-11", "day_index": 0, "name": "七十二奇楼景区"}, {"date": "2026-05-14", "day_index": 3, "name": "七十二奇楼景区"}]}]}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 400, "expected_total_attractions": 1600, "reported_total_attractions": 1600, "meal_per_person_cost_sum": 658, "expected_total_meals": 2632, "reported_total_meals": 3496, "reported_total_transportation": 3300}}]`

### v3_standard200_realbudget_eval_000005
- request: 广州 2026-07-06->2026-07-08 days=3 transport=地铁+步行 hotel=经济型酒店 prefs=['博物馆', '城市公园', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 170, "expected_total_attractions": 340, "reported_total_attractions": 340, "meal_per_person_cost_sum": 648, "expected_total_meals": 1296, "reported_total_meals": 1156, "reported_total_transportation": 200}}]`

### v3_standard200_realbudget_eval_000006
- request: 南京 2026-07-06->2026-07-09 days=4 transport=打车 hotel=经济型酒店 prefs=['老人友好', '美食', '城市公园', '休闲慢游']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 100, "expected_total_attractions": 300, "reported_total_attractions": 330, "meal_per_person_cost_sum": 835, "expected_total_meals": 2505, "reported_total_meals": 2469, "reported_total_transportation": 700}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 100, "expected_total_attractions": 300, "reported_total_attractions": 330, "meal_per_person_cost_sum": 835, "expected_total_meals": 2505, "reported_total_meals": 2469, "reported_total_transportation": 700}}]`

### v3_standard200_realbudget_eval_000007
- request: 成都 2026-05-11->2026-05-13 days=3 transport=地铁+步行 hotel=舒适型酒店 prefs=['美食', '城市公园', '休闲慢游']
- errors: `[{"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 165, "expected_total_attractions": 330, "reported_total_attractions": 330, "meal_per_person_cost_sum": 858, "expected_total_meals": 1716, "reported_total_meals": 1830, "reported_total_transportation": 100}}]`

### v3_standard200_realbudget_eval_000008
- request: 大理 2026-05-11->2026-05-13 days=3 transport=地铁+步行 hotel=舒适型酒店 prefs=['休闲慢游', '城市地标', '历史文化']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 115, "expected_total_attractions": 230, "reported_total_attractions": 260, "meal_per_person_cost_sum": 492, "expected_total_meals": 984, "reported_total_meals": 824, "reported_total_transportation": 400}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 115, "expected_total_attractions": 230, "reported_total_attractions": 260, "meal_per_person_cost_sum": 492, "expected_total_meals": 984, "reported_total_meals": 824, "reported_total_transportation": 400}}]`

### v3_standard200_realbudget_eval_000003
- request: 西安 2025-05-07->2025-05-11 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '历史文化', '购物商圈']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 4, "party_total": 3, "room_count": 2, "priced_nights": 4, "expected_min_total_hotels": 3600, "reported_total_hotels": 4500, "diff": 900, "covers_nights": false}}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 11399, "total": 10499, "diff": 900, "requested_budget": {"available": true, "amount": 15700, "scope": "total", "party_size": 3, "total": 15700, "source": "budget_constraint", "budget_level": "standard", "strictness": "soft"}, "per_person_day": 699.93, "budget_level": "standard", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "standard", "strictness": "soft", "amount": 15700, "target_min_ratio": 0.6, "target_max_ratio": 1.05, "target_min_total": 9400, "target_max_total": 16500, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 4, "party_total": 3, "room_count": 2, "priced_nights": 4, "expected_min_total_hotels": 3600, "reported_total_hotels": 4500, "diff": 900, "covers_nights": false}, "hotel_budget_covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 319, "expected_total_attractions": 957, "reported_total_attractions": 948, "meal_per_person_cost_sum": 926, "expected_total_meals": 2778, "reported_total_meals": 3651, "reported_total_transportation": 2300}}]`

### v3_standard200_realbudget_eval_000010
- request: 西安 2026-08-05->2026-08-08 days=4 transport=公共交通 hotel=经济型酒店 prefs=['城市公园', '美食']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 3932, "total": 4932, "diff": -1000, "requested_budget": {"available": true, "amount": 6600, "scope": "total", "party_size": 2, "total": 6600, "source": "budget_constraint", "budget_level": "standard", "strictness": "soft"}, "per_person_day": 616.5, "budget_level": "standard", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "standard", "strictness": "soft", "amount": 6600, "target_min_ratio": 0.6, "target_max_ratio": 1.05, "target_min_total": 4000, "target_max_total": 6900, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 2, "room_count": 1, "priced_nights": 3, "expected_min_total_hotels": 750, "reported_total_hotels": 750, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 319, "expected_total_attractions": 638, "reported_total_attractions": 658, "meal_per_person_cost_sum": 715, "expected_total_meals": 1430, "reported_total_meals": 1724, "reported_total_transportation": 800}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 319, "expected_total_attractions": 638, "reported_total_attractions": 658, "meal_per_person_cost_sum": 715, "expected_total_meals": 1430, "reported_total_meals": 1724, "reported_total_transportation": 800}}]`

### v3_standard200_realbudget_eval_000011
- request: 福州 2026-06-21->2026-06-24 days=4 transport=打车 hotel=经济型酒店 prefs=['第一次来', '城市漫步']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 3958, "total": 4058, "diff": -100, "requested_budget": {"available": true, "amount": 5900, "scope": "total", "party_size": 2, "total": 5900, "source": "budget_constraint", "budget_level": "standard", "strictness": "soft"}, "per_person_day": 507.25, "budget_level": "standard", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "standard", "strictness": "soft", "amount": 5900, "target_min_ratio": 0.6, "target_max_ratio": 1.05, "target_min_total": 3500, "target_max_total": 6200, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 2, "room_count": 1, "priced_nights": 3, "expected_min_total_hotels": 600, "reported_total_hotels": 600, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 167, "expected_total_attractions": 334, "reported_total_attractions": 354, "meal_per_person_cost_sum": 844, "expected_total_meals": 1688, "reported_total_meals": 2004, "reported_total_transportation": 1000}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 167, "expected_total_attractions": 334, "reported_total_attractions": 354, "meal_per_person_cost_sum": 844, "expected_total_meals": 1688, "reported_total_meals": 2004, "reported_total_transportation": 1000}}]`

### v3_standard200_realbudget_eval_000009
- request: 苏州 2026-04-30->2026-05-04 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['亲子', '城市地标', '第一次来', '城市漫步']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 16300, "total": 14300, "diff": 2000, "requested_budget": {"available": true, "amount": 20500, "scope": "total", "party_size": 4, "total": 20500, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "soft"}, "per_person_day": 715.0, "budget_level": "comfortable", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "soft", "amount": 20500, "target_min_ratio": 0.7, "target_max_ratio": 1.1, "target_min_total": 14300, "target_max_total": 22600, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 4, "party_total": 4, "room_count": 2, "priced_nights": 4, "expected_min_total_hotels": 10800, "reported_total_hotels": 10800, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 509, "expected_total_attractions": 2036, "reported_total_attractions": 2296, "meal_per_person_cost_sum": 1188, "expected_total_meals": 4752, "reported_total_meals": 3004, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 509, "expected_total_attractions": 2036, "reported_total_attractions": 2296, "meal_per_person_cost_sum": 1188, "expected_total_meals": 4752, "reported_total_meals": 3004, "reported_total_transportation": 200}}]`

### v3_standard200_realbudget_eval_000013
- request: 武汉 2026-05-09->2026-05-11 days=3 transport=公共交通 hotel=舒适型酒店 prefs=['亲子', '老人友好', '第一次来', '城市公园']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 8296, "total": 7296, "diff": 1000, "requested_budget": {"available": true, "amount": 12400, "scope": "total", "party_size": 6, "total": 12400, "source": "budget_constraint", "budget_level": "standard", "strictness": "soft"}, "per_person_day": 405.33, "budget_level": "standard", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "standard", "strictness": "soft", "amount": 12400, "target_min_ratio": 0.6, "target_max_ratio": 1.05, "target_min_total": 7400, "target_max_total": 13000, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 6, "room_count": 3, "priced_nights": 2, "expected_min_total_hotels": 2400, "reported_total_hotels": 2400, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 6, "hotel_room_count": 3, "attraction_ticket_sum": 206, "expected_total_attractions": 1236, "reported_total_attractions": 1296, "meal_per_person_cost_sum": 505, "expected_total_meals": 3030, "reported_total_meals": 3600, "reported_total_transportation": 1000}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 6, "hotel_room_count": 3, "attraction_ticket_sum": 206, "expected_total_attractions": 1236, "reported_total_attractions": 1296, "meal_per_person_cost_sum": 505, "expected_total_meals": 3030, "reported_total_meals": 3600, "reported_total_transportation": 1000}}]`

### v3_standard200_realbudget_eval_000014
- request: 成都 2026-06-06->2026-06-07 days=2 transport=打车 hotel=经济型酒店 prefs=['小众展览', '美食', '城市地标']
- errors: `[{"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 115, "expected_total_attractions": 460, "reported_total_attractions": 460, "meal_per_person_cost_sum": 581, "expected_total_meals": 2324, "reported_total_meals": 2128, "reported_total_transportation": 200}}]`

### v3_standard200_realbudget_eval_000012
- request: 洛阳 2025-05-07->2025-05-10 days=4 transport=打车 hotel=高端酒店 prefs=['休闲慢游', '第一次来']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 20600, "total": 20500, "diff": 100, "requested_budget": {"available": true, "amount": 23100, "scope": "total", "party_size": 3, "total": 23100, "source": "budget_constraint", "budget_level": "premium", "strictness": "soft"}, "per_person_day": 1708.33, "budget_level": "premium", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "premium", "strictness": "soft", "amount": 23100, "target_min_ratio": 0.75, "target_max_ratio": 1.12, "target_min_total": 17300, "target_max_total": 25900, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 3, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 7800, "reported_total_hotels": 7800, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 701, "expected_total_attractions": 2103, "reported_total_attractions": 2103, "meal_per_person_cost_sum": 1602, "expected_total_meals": 4806, "reported_total_meals": 6697, "reported_total_transportation": 4000}}]`

### v3_standard200_realbudget_eval_000016
- request: 苏州 2026-06-06->2026-06-08 days=3 transport=公共交通 hotel=民宿 prefs=['海滨度假', '城市公园', '主题乐园', '清真']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 1978, "total": 2078, "diff": -100, "requested_budget": {"available": true, "amount": 2800, "scope": "total", "party_size": 2, "total": 2800, "source": "budget_constraint", "budget_level": "limited", "strictness": "soft"}, "per_person_day": 346.33, "budget_level": "limited", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "limited", "strictness": "soft", "amount": 2800, "target_min_ratio": 0.72, "target_max_ratio": 1.05, "target_min_total": 2000, "target_max_total": 2900, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 2, "room_count": 1, "priced_nights": 2, "expected_min_total_hotels": 600, "reported_total_hotels": 600, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 135, "expected_total_attractions": 270, "reported_total_attractions": 250, "meal_per_person_cost_sum": 292, "expected_total_meals": 584, "reported_total_meals": 628, "reported_total_transportation": 500}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 135, "expected_total_attractions": 270, "reported_total_attractions": 250, "meal_per_person_cost_sum": 292, "expected_total_meals": 584, "reported_total_meals": 628, "reported_total_transportation": 500}}]`

### v3_standard200_realbudget_eval_000017
- request: 苏州 2026-05-09->2026-05-11 days=3 transport=地铁+步行 hotel=亲子酒店 prefs=['亲子', '历史文化', '休闲慢游', '户外轻徒步']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 375, "expected_total_attractions": 1125, "reported_total_attractions": 1245, "meal_per_person_cost_sum": 594, "expected_total_meals": 1782, "reported_total_meals": 1938, "reported_total_transportation": 400}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 375, "expected_total_attractions": 1125, "reported_total_attractions": 1245, "meal_per_person_cost_sum": 594, "expected_total_meals": 1782, "reported_total_meals": 1938, "reported_total_transportation": 400}}]`

### v3_standard200_realbudget_eval_000018
- request: 天津 2026-07-06->2026-07-07 days=2 transport=打车 hotel=舒适型酒店 prefs=['老人友好', '夜市夜景', '艺术', '第一次来']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 130, "expected_total_attractions": 390, "reported_total_attractions": 450, "meal_per_person_cost_sum": 313, "expected_total_meals": 939, "reported_total_meals": 951, "reported_total_transportation": 100}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 130, "expected_total_attractions": 390, "reported_total_attractions": 450, "meal_per_person_cost_sum": 313, "expected_total_meals": 939, "reported_total_meals": 951, "reported_total_transportation": 100}}]`

### v3_standard200_realbudget_eval_000019
- request: 丽江 2026-05-11->2026-05-15 days=5 transport=打车 hotel=经济型酒店 prefs=['亲子', '老人友好', '海滨度假', '美食']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 9700, "total": 7700, "diff": 2000, "requested_budget": {"available": true, "amount": 10700, "scope": "total", "party_size": 5, "total": 10700, "source": "budget_constraint", "budget_level": "limited", "strictness": "hard"}, "per_person_day": 308.0, "budget_level": "limited", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "limited", "strictness": "hard", "amount": 10700, "target_min_ratio": 0.72, "target_max_ratio": 1.0, "target_min_total": 7700, "target_max_total": 10700, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 4, "party_total": 5, "room_count": 3, "priced_nights": 4, "expected_min_total_hotels": 3600, "reported_total_hotels": 3600, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 5, "hotel_room_count": 3, "attraction_ticket_sum": 820, "expected_total_attractions": 4100, "reported_total_attractions": 3200, "meal_per_person_cost_sum": 923, "expected_total_meals": 4615, "reported_total_meals": 2100, "reported_total_transportation": 800}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 5, "hotel_room_count": 3, "attraction_ticket_sum": 820, "expected_total_attractions": 4100, "reported_total_attractions": 3200, "meal_per_person_cost_sum": 923, "expected_total_meals": 4615, "reported_total_meals": 2100, "reported_total_transportation": 800}}]`

### v3_standard200_realbudget_eval_000020
- request: 杭州 2026-06-21->2026-06-24 days=4 transport=地铁+步行 hotel=高端酒店 prefs=['历史文化', '海滨度假']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 9600, "total": 10600, "diff": -1000, "requested_budget": {"available": true, "amount": 10600, "scope": "total", "party_size": 2, "total": 10600, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "soft"}, "per_person_day": 1325.0, "budget_level": "comfortable", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "soft", "amount": 10600, "target_min_ratio": 0.7, "target_max_ratio": 1.1, "target_min_total": 7400, "target_max_total": 11700, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 2, "room_count": 1, "priced_nights": 3, "expected_min_total_hotels": 4500, "reported_total_hotels": 4500, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 432, "expected_total_attractions": 864, "reported_total_attractions": 924, "meal_per_person_cost_sum": 991, "expected_total_meals": 1982, "reported_total_meals": 2436, "reported_total_transportation": 1740}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 432, "expected_total_attractions": 864, "reported_total_attractions": 924, "meal_per_person_cost_sum": 991, "expected_total_meals": 1982, "reported_total_meals": 2436, "reported_total_transportation": 1740}}]`
