# Rule Eval Report: 260513_rerank_old600final_standard_w10

- records: 200
- generations: `training/outputs/eval/by_model/sft_qwen25_7b_v3_260513_rerank_old600final/260513_rerank_old600final_standard_w10/generations.jsonl`
- records_path: `training/data/v3/eval/records.jsonl`

## Boolean Metrics

| Metric | Pass | Total | Rate |
| --- | ---: | ---: | ---: |
| accommodation_type_ok | 200 | 200 | 100.00% |
| attraction_budget_consistent | 70 | 200 | 35.00% |
| attraction_budget_party_relation_ok | 198 | 200 | 99.00% |
| attraction_count_ok | 200 | 200 | 100.00% |
| attraction_diversity_ok | 195 | 200 | 97.50% |
| attraction_grounding_ok | 200 | 200 | 100.00% |
| attraction_repeat_limit_ok | 195 | 200 | 97.50% |
| budget_arithmetic_consistent | 168 | 200 | 84.00% |
| budget_consistent | 168 | 200 | 84.00% |
| budget_level_aligned | 166 | 200 | 83.00% |
| budget_preference_aligned | 166 | 200 | 83.00% |
| budget_relationship_ok | 175 | 200 | 87.50% |
| budget_selection_ok | 154 | 200 | 77.00% |
| budget_user_constraint_ok | 200 | 200 | 100.00% |
| budget_within_user_budget | 196 | 200 | 98.00% |
| city_ok | 200 | 200 | 100.00% |
| date_range_ok | 200 | 200 | 100.00% |
| day_dates_ok | 200 | 200 | 100.00% |
| day_index_ok | 200 | 200 | 100.00% |
| days_len_ok | 200 | 200 | 100.00% |
| dpo_soft_pass | 153 | 200 | 76.50% |
| dpo_soft_recomputed_budget_pass | 143 | 200 | 71.50% |
| hard_pass | 199 | 200 | 99.50% |
| hotel_budget_covers_nights | 195 | 200 | 97.50% |
| hotel_budget_relation_ok | 198 | 200 | 99.00% |
| hotel_distance_placeholder_ok | 200 | 200 | 100.00% |
| hotel_grounding_ok | 200 | 200 | 100.00% |
| invalid_hotel_name_ok | 200 | 200 | 100.00% |
| json_extract_ok | 200 | 200 | 100.00% |
| legacy_hard_pass | 151 | 200 | 75.50% |
| location_object_ok | 200 | 200 | 100.00% |
| meal_budget_consistent | 1 | 200 | 0.50% |
| meal_complete | 200 | 200 | 100.00% |
| meal_cost_scale_ok | 178 | 200 | 89.00% |
| meal_diversity_ok | 187 | 200 | 93.50% |
| meal_grounding_ok | 199 | 200 | 99.50% |
| meal_lunch_dinner_same_day_ok | 199 | 200 | 99.50% |
| meal_repeat_limit_ok | 188 | 200 | 94.00% |
| meal_specific_ok | 200 | 200 | 100.00% |
| meal_valid_semantics_ok | 199 | 200 | 99.50% |
| middle_hotel_ok | 200 | 200 | 100.00% |
| recomputed_budget_fit_ok | 154 | 200 | 77.00% |
| recomputed_budget_hard_ok | 199 | 200 | 99.50% |
| recomputed_budget_level_aligned | 154 | 200 | 77.00% |
| recomputed_budget_preference_aligned | 154 | 200 | 77.00% |
| recomputed_budget_user_constraint_ok | 199 | 200 | 99.50% |
| recomputed_budget_within_user_budget | 191 | 200 | 95.50% |
| schema_ok | 200 | 200 | 100.00% |
| sft_budget_semantic_hard_pass | 172 | 200 | 86.00% |
| sft_hard_pass | 199 | 200 | 99.50% |
| sft_no_budget_sum_hard_pass | 199 | 200 | 99.50% |
| sft_strict_hard_pass | 0 | 200 | 0.00% |
| transportation_budget_nonnegative | 200 | 200 | 100.00% |
| weather_dates_ok | 200 | 200 | 100.00% |
| weather_match | 200 | 200 | 100.00% |

## Numeric Metrics

```json
{
  "attraction_diversity_unique_rate": {
    "avg": 0.9967,
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
    "avg": 0.9307,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_food_pois_grounding_rate": {
    "avg": 0.9997,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_grounding_rate": {
    "avg": 0.9997,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_semantic_valid_rate": {
    "avg": 0.9997,
    "p50": 1.0,
    "p90": 1.0
  },
  "recomputed_budget_per_person_day": {
    "avg": 745.1572,
    "p50": 601.47,
    "p90": 1304.22
  },
  "recomputed_budget_total": {
    "avg": 7019.15,
    "p50": 5946.0,
    "p90": 13645.0
  }
}
```

## Failure Types

```json
{
  "meal_budget_inconsistent": 199,
  "attraction_budget_inconsistent": 130,
  "budget_preference_mismatch": 34,
  "budget_arithmetic_inconsistent": 32,
  "budget_relationship_mismatch": 25,
  "meal_cost_scale_too_low": 22,
  "meal_repeat_too_many": 12,
  "attraction_repeat_too_many": 5,
  "hotel_budget_underestimated": 5,
  "meal_invalid_name": 1,
  "meal_same_day_lunch_dinner_repeat": 1
}
```

## Failure Examples

### v3_standard200_realbudget_eval_000000
- request: 昆明 2026-04-07->2026-04-09 days=3 transport=地铁+步行 hotel=高端酒店 prefs=['休闲慢游', '美食']
- errors: `[{"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 50, "expected_total_attractions": 100, "reported_total_attractions": 100, "meal_per_person_cost_sum": 738, "expected_total_meals": 1476, "reported_total_meals": 2200, "reported_total_transportation": 2500}}]`

### v3_standard200_realbudget_eval_000001
- request: 桂林 2026-09-04->2026-09-06 days=3 transport=公共交通 hotel=高端酒店 prefs=['艺术', '美食', '第一次来', '历史文化']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 345, "expected_total_attractions": 690, "reported_total_attractions": 700, "meal_per_person_cost_sum": 849, "expected_total_meals": 1698, "reported_total_meals": 1600, "reported_total_transportation": 1000}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 345, "expected_total_attractions": 690, "reported_total_attractions": 700, "meal_per_person_cost_sum": 849, "expected_total_meals": 1698, "reported_total_meals": 1600, "reported_total_transportation": 1000}}]`

### v3_standard200_realbudget_eval_000002
- request: 杭州 2026-05-01->2026-05-05 days=5 transport=公共交通 hotel=经济型酒店 prefs=['美食', '休闲慢游', '户外轻徒步', '城市漫步']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 160, "expected_total_attractions": 160, "reported_total_attractions": 170, "meal_per_person_cost_sum": 1163, "expected_total_meals": 1163, "reported_total_meals": 1021, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 160, "expected_total_attractions": 160, "reported_total_attractions": 170, "meal_per_person_cost_sum": 1163, "expected_total_meals": 1163, "reported_total_meals": 1021, "reported_total_transportation": 200}}, {"stage": "rule", "type": "budget_preference_mismatch", "details": {"part_sum": 2391, "total": 2391, "diff": 0, "requested_budget": {"available": true, "amount": 3400, "scope": "total", "party_size": 1, "total": 3400, "source": "budget_constraint", "budget_level": "limited", "strictness": "soft"}, "per_person_day": 478.2, "budget_level": "limited", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "limited", "strictness": "soft", "amount": 3400, "target_min_ratio": 0.72, "target_max_ratio": 1.05, "target_min_total": 2400, "target_max_total": 3600, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": true, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 4, "party_total": 1, "room_count": 1, "priced_nights": 4, "expected_min_total_hotels": 1000, "reported_total_hotels": 1000, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_standard200_realbudget_eval_000004
- request: 张家界 2026-05-11->2026-05-15 days=5 transport=地铁+步行 hotel=舒适型酒店 prefs=['亲子', '城市漫步', '历史文化']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 9900, "total": 7900, "diff": 2000, "requested_budget": {"available": true, "amount": 13200, "scope": "total", "party_size": 4, "total": 13200, "source": "budget_constraint", "budget_level": "standard", "strictness": "soft"}, "per_person_day": 395.0, "budget_level": "standard", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "standard", "strictness": "soft", "amount": 13200, "target_min_ratio": 0.6, "target_max_ratio": 1.05, "target_min_total": 7900, "target_max_total": 13900, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 4, "party_total": 4, "room_count": 2, "priced_nights": 4, "expected_min_total_hotels": 4800, "reported_total_hotels": 4800, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 442, "expected_total_attractions": 1768, "reported_total_attractions": 2044, "meal_per_person_cost_sum": 722, "expected_total_meals": 2888, "reported_total_meals": 2256, "reported_total_transportation": 800}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 442, "expected_total_attractions": 1768, "reported_total_attractions": 2044, "meal_per_person_cost_sum": 722, "expected_total_meals": 2888, "reported_total_meals": 2256, "reported_total_transportation": 800}}]`

### v3_standard200_realbudget_eval_000005
- request: 广州 2026-07-06->2026-07-08 days=3 transport=地铁+步行 hotel=经济型酒店 prefs=['博物馆', '城市公园', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 250, "expected_total_attractions": 500, "reported_total_attractions": 420, "meal_per_person_cost_sum": 631, "expected_total_meals": 1262, "reported_total_meals": 1206, "reported_total_transportation": 80}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 250, "expected_total_attractions": 500, "reported_total_attractions": 420, "meal_per_person_cost_sum": 631, "expected_total_meals": 1262, "reported_total_meals": 1206, "reported_total_transportation": 80}}]`

### v3_standard200_realbudget_eval_000006
- request: 南京 2026-07-06->2026-07-09 days=4 transport=打车 hotel=经济型酒店 prefs=['老人友好', '美食', '城市公园', '休闲慢游']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 5019, "total": 4919, "diff": 100, "requested_budget": {"available": true, "amount": 5600, "scope": "total", "party_size": 3, "total": 5600, "source": "budget_constraint", "budget_level": "limited", "strictness": "soft"}, "per_person_day": 409.92, "budget_level": "limited", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "limited", "strictness": "soft", "amount": 5600, "target_min_ratio": 0.72, "target_max_ratio": 1.05, "target_min_total": 4000, "target_max_total": 5900, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 3, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 1500, "reported_total_hotels": 1500, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 70, "expected_total_attractions": 210, "reported_total_attractions": 210, "meal_per_person_cost_sum": 791, "expected_total_meals": 2373, "reported_total_meals": 2109, "reported_total_transportation": 1200}}]`

### v3_standard200_realbudget_eval_000007
- request: 成都 2026-05-11->2026-05-13 days=3 transport=地铁+步行 hotel=舒适型酒店 prefs=['美食', '城市公园', '休闲慢游']
- errors: `[{"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 165, "expected_total_attractions": 330, "reported_total_attractions": 330, "meal_per_person_cost_sum": 880, "expected_total_meals": 1760, "reported_total_meals": 1806, "reported_total_transportation": 100}}]`

### v3_standard200_realbudget_eval_000008
- request: 大理 2026-05-11->2026-05-13 days=3 transport=地铁+步行 hotel=舒适型酒店 prefs=['休闲慢游', '城市地标', '历史文化']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 115, "expected_total_attractions": 230, "reported_total_attractions": 250, "meal_per_person_cost_sum": 492, "expected_total_meals": 984, "reported_total_meals": 854, "reported_total_transportation": 300}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 115, "expected_total_attractions": 230, "reported_total_attractions": 250, "meal_per_person_cost_sum": 492, "expected_total_meals": 984, "reported_total_meals": 854, "reported_total_transportation": 300}}]`

### v3_standard200_realbudget_eval_000003
- request: 西安 2025-05-07->2025-05-11 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '历史文化', '购物商圈']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "西安碑林博物馆", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2025-05-09", "day_index": 2, "name": "西安碑林博物馆"}, {"date": "2025-05-11", "day_index": 4, "name": "西安碑林博物馆"}]}, {"name_key": "西安博物院", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2025-05-10", "day_index": 3, "name": "西安博物院"}, {"date": "2025-05-11", "day_index": 4, "name": "西安博物院"}]}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 4, "party_total": 3, "room_count": 2, "priced_nights": 4, "expected_min_total_hotels": 3600, "reported_total_hotels": 4050, "diff": 450, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 384, "expected_total_attractions": 1152, "reported_total_attractions": 1248, "meal_per_person_cost_sum": 931, "expected_total_meals": 2793, "reported_total_meals": 4200, "reported_total_transportation": 6100}}]`

### v3_standard200_realbudget_eval_000010
- request: 西安 2026-08-05->2026-08-08 days=4 transport=公共交通 hotel=经济型酒店 prefs=['城市公园', '美食']
- errors: `[{"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 319, "expected_total_attractions": 638, "reported_total_attractions": 638, "meal_per_person_cost_sum": 611, "expected_total_meals": 1222, "reported_total_meals": 1424, "reported_total_transportation": 1200}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": true, "meal_cost_scale_ok": false, "budget_relationship_ok": false, "expected_total_hotels": 750, "reported_total_hotels": 750, "expected_total_attractions": 638, "reported_total_attractions": 638, "meal_scale_eval": {"ok": false, "party_total": 2, "budget_level": "standard", "per_person_lunch_dinner_floor": 35, "breakfast_policy": "excluded_from_meal_cost_scale", "meal_count": 12, "checked_count": 8, "failure_count": 1, "failures": [{"date": "2026-08-07", "type": "lunch", "name": "马洪小炒泡馍馆", "estimated_cost": 29, "min_expected_cost": 35}]}}}, {"stage": "rule", "type": "meal_cost_scale_too_low", "details": {"ok": false, "party_total": 2, "budget_level": "standard", "per_person_lunch_dinner_floor": 35, "breakfast_policy": "excluded_from_meal_cost_scale", "meal_count": 12, "checked_count": 8, "failure_count": 1, "failures": [{"date": "2026-08-07", "type": "lunch", "name": "马洪小炒泡馍馆", "estimated_cost": 29, "min_expected_cost": 35}]}}]`

### v3_standard200_realbudget_eval_000011
- request: 福州 2026-06-21->2026-06-24 days=4 transport=打车 hotel=经济型酒店 prefs=['第一次来', '城市漫步']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 117, "expected_total_attractions": 234, "reported_total_attractions": 254, "meal_per_person_cost_sum": 692, "expected_total_meals": 1384, "reported_total_meals": 1536, "reported_total_transportation": 1100}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 117, "expected_total_attractions": 234, "reported_total_attractions": 254, "meal_per_person_cost_sum": 692, "expected_total_meals": 1384, "reported_total_meals": 1536, "reported_total_transportation": 1100}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": true, "meal_cost_scale_ok": false, "budget_relationship_ok": false, "expected_total_hotels": 600, "reported_total_hotels": 600, "expected_total_attractions": 234, "reported_total_attractions": 254, "meal_scale_eval": {"ok": false, "party_total": 2, "budget_level": "standard", "per_person_lunch_dinner_floor": 35, "breakfast_policy": "excluded_from_meal_cost_scale", "meal_count": 12, "checked_count": 8, "failure_count": 1, "failures": [{"date": "2026-06-21", "type": "lunch", "name": "后街捞化", "estimated_cost": 27, "min_expected_cost": 35}]}}}]`

### v3_standard200_realbudget_eval_000009
- request: 苏州 2026-04-30->2026-05-04 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['亲子', '城市地标', '第一次来', '城市漫步']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 16300, "total": 14300, "diff": 2000, "requested_budget": {"available": true, "amount": 20500, "scope": "total", "party_size": 4, "total": 20500, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "soft"}, "per_person_day": 715.0, "budget_level": "comfortable", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "soft", "amount": 20500, "target_min_ratio": 0.7, "target_max_ratio": 1.1, "target_min_total": 14300, "target_max_total": 22600, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 4, "party_total": 4, "room_count": 2, "priced_nights": 4, "expected_min_total_hotels": 10800, "reported_total_hotels": 10800, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 500, "expected_total_attractions": 2000, "reported_total_attractions": 2160, "meal_per_person_cost_sum": 925, "expected_total_meals": 3700, "reported_total_meals": 2880, "reported_total_transportation": 460}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 500, "expected_total_attractions": 2000, "reported_total_attractions": 2160, "meal_per_person_cost_sum": 925, "expected_total_meals": 3700, "reported_total_meals": 2880, "reported_total_transportation": 460}}]`

### v3_standard200_realbudget_eval_000013
- request: 武汉 2026-05-09->2026-05-11 days=3 transport=公共交通 hotel=舒适型酒店 prefs=['亲子', '老人友好', '第一次来', '城市公园']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 6, "hotel_room_count": 3, "attraction_ticket_sum": 206, "expected_total_attractions": 1236, "reported_total_attractions": 1296, "meal_per_person_cost_sum": 497, "expected_total_meals": 2982, "reported_total_meals": 3600, "reported_total_transportation": 1000}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 6, "hotel_room_count": 3, "attraction_ticket_sum": 206, "expected_total_attractions": 1236, "reported_total_attractions": 1296, "meal_per_person_cost_sum": 497, "expected_total_meals": 2982, "reported_total_meals": 3600, "reported_total_transportation": 1000}}]`

### v3_standard200_realbudget_eval_000014
- request: 成都 2026-06-06->2026-06-07 days=2 transport=打车 hotel=经济型酒店 prefs=['小众展览', '美食', '城市地标']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 115, "expected_total_attractions": 460, "reported_total_attractions": 500, "meal_per_person_cost_sum": 587, "expected_total_meals": 2348, "reported_total_meals": 2148, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 115, "expected_total_attractions": 460, "reported_total_attractions": 500, "meal_per_person_cost_sum": 587, "expected_total_meals": 2348, "reported_total_meals": 2148, "reported_total_transportation": 200}}]`

### v3_standard200_realbudget_eval_000012
- request: 洛阳 2025-05-07->2025-05-10 days=4 transport=打车 hotel=高端酒店 prefs=['休闲慢游', '第一次来']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 974, "expected_total_attractions": 2922, "reported_total_attractions": 2970, "meal_per_person_cost_sum": 2148, "expected_total_meals": 6444, "reported_total_meals": 6882, "reported_total_transportation": 4500}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 974, "expected_total_attractions": 2922, "reported_total_attractions": 2970, "meal_per_person_cost_sum": 2148, "expected_total_meals": 6444, "reported_total_meals": 6882, "reported_total_transportation": 4500}}]`

### v3_standard200_realbudget_eval_000016
- request: 苏州 2026-06-06->2026-06-08 days=3 transport=公共交通 hotel=民宿 prefs=['海滨度假', '城市公园', '主题乐园', '清真']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 135, "expected_total_attractions": 270, "reported_total_attractions": 250, "meal_per_person_cost_sum": 259, "expected_total_meals": 518, "reported_total_meals": 610, "reported_total_transportation": 500}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 135, "expected_total_attractions": 270, "reported_total_attractions": 250, "meal_per_person_cost_sum": 259, "expected_total_meals": 518, "reported_total_meals": 610, "reported_total_transportation": 500}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": true, "meal_cost_scale_ok": false, "budget_relationship_ok": false, "expected_total_hotels": 600, "reported_total_hotels": 600, "expected_total_attractions": 270, "reported_total_attractions": 250, "meal_scale_eval": {"ok": false, "party_total": 2, "budget_level": "limited", "per_person_lunch_dinner_floor": 25, "breakfast_policy": "excluded_from_meal_cost_scale", "meal_count": 9, "checked_count": 6, "failure_count": 4, "failures": [{"date": "2026-06-06", "type": "dinner", "name": "丝路回乡小吃店(西夏店)", "estimated_cost": 24, "min_expected_cost": 25}, {"date": "2026-06-07", "type": "lunch", "name": "魅之蘭兰州牛肉面(乐嘉汇店)", "estimated_cost": 21, "min_expected_cost": 25}, {"date": "2026-06-07", "type": "dinner", "name": "秋娟馄饨店", "estimated_cost": 14, "min_expected_cost": 25}, {"date": "2026-06-08", "type": "lunch", "name": "丝路回乡小吃店(西夏店)", "estimated_cost": 24, "min_expected_cost": 25}]}}}]`

### v3_standard200_realbudget_eval_000017
- request: 苏州 2026-05-09->2026-05-11 days=3 transport=地铁+步行 hotel=亲子酒店 prefs=['亲子', '历史文化', '休闲慢游', '户外轻徒步']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 315, "expected_total_attractions": 945, "reported_total_attractions": 1035, "meal_per_person_cost_sum": 507, "expected_total_meals": 1521, "reported_total_meals": 1809, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 315, "expected_total_attractions": 945, "reported_total_attractions": 1035, "meal_per_person_cost_sum": 507, "expected_total_meals": 1521, "reported_total_meals": 1809, "reported_total_transportation": 200}}]`

### v3_standard200_realbudget_eval_000018
- request: 天津 2026-07-06->2026-07-07 days=2 transport=打车 hotel=舒适型酒店 prefs=['老人友好', '夜市夜景', '艺术', '第一次来']
- errors: `[{"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 130, "expected_total_attractions": 390, "reported_total_attractions": 390, "meal_per_person_cost_sum": 339, "expected_total_meals": 1017, "reported_total_meals": 1011, "reported_total_transportation": 200}}]`

### v3_standard200_realbudget_eval_000019
- request: 丽江 2026-05-11->2026-05-15 days=5 transport=打车 hotel=经济型酒店 prefs=['亲子', '老人友好', '海滨度假', '美食']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 9700, "total": 7700, "diff": 2000, "requested_budget": {"available": true, "amount": 10700, "scope": "total", "party_size": 5, "total": 10700, "source": "budget_constraint", "budget_level": "limited", "strictness": "hard"}, "per_person_day": 308.0, "budget_level": "limited", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "limited", "strictness": "hard", "amount": 10700, "target_min_ratio": 0.72, "target_max_ratio": 1.0, "target_min_total": 7700, "target_max_total": 10700, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 4, "party_total": 5, "room_count": 3, "priced_nights": 4, "expected_min_total_hotels": 3600, "reported_total_hotels": 3600, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 5, "hotel_room_count": 3, "attraction_ticket_sum": 740, "expected_total_attractions": 3700, "reported_total_attractions": 3400, "meal_per_person_cost_sum": 928, "expected_total_meals": 4640, "reported_total_meals": 1800, "reported_total_transportation": 900}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 5, "hotel_room_count": 3, "attraction_ticket_sum": 740, "expected_total_attractions": 3700, "reported_total_attractions": 3400, "meal_per_person_cost_sum": 928, "expected_total_meals": 4640, "reported_total_meals": 1800, "reported_total_transportation": 900}}]`

### v3_standard200_realbudget_eval_000020
- request: 杭州 2026-06-21->2026-06-24 days=4 transport=地铁+步行 hotel=高端酒店 prefs=['历史文化', '海滨度假']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 9584, "total": 10584, "diff": -1000, "requested_budget": {"available": true, "amount": 10600, "scope": "total", "party_size": 2, "total": 10600, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "soft"}, "per_person_day": 1323.0, "budget_level": "comfortable", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "soft", "amount": 10600, "target_min_ratio": 0.7, "target_max_ratio": 1.1, "target_min_total": 7400, "target_max_total": 11700, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 2, "room_count": 1, "priced_nights": 3, "expected_min_total_hotels": 4500, "reported_total_hotels": 4500, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 150, "expected_total_attractions": 300, "reported_total_attractions": 280, "meal_per_person_cost_sum": 1421, "expected_total_meals": 2842, "reported_total_meals": 3904, "reported_total_transportation": 900}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 150, "expected_total_attractions": 300, "reported_total_attractions": 280, "meal_per_person_cost_sum": 1421, "expected_total_meals": 2842, "reported_total_meals": 3904, "reported_total_transportation": 900}}]`
