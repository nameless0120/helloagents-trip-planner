# Rule Eval Report: 260513_bestofn1200_retry_final_hard_w10

- records: 300
- generations: `training/outputs/eval/by_model/sft_qwen25_7b_v3_260513_bestofn1200_retry_final/260513_bestofn1200_retry_final_hard_w10/generations.jsonl`
- records_path: `training/data/v3/eval_hard/records.jsonl`

## Boolean Metrics

| Metric | Pass | Total | Rate |
| --- | ---: | ---: | ---: |
| accommodation_type_ok | 300 | 300 | 100.00% |
| attraction_budget_consistent | 84 | 300 | 28.00% |
| attraction_budget_party_relation_ok | 295 | 300 | 98.33% |
| attraction_count_ok | 298 | 300 | 99.33% |
| attraction_diversity_ok | 257 | 300 | 85.67% |
| attraction_grounding_ok | 295 | 300 | 98.33% |
| attraction_repeat_limit_ok | 257 | 300 | 85.67% |
| budget_arithmetic_consistent | 193 | 300 | 64.33% |
| budget_consistent | 193 | 300 | 64.33% |
| budget_level_aligned | 209 | 300 | 69.67% |
| budget_preference_aligned | 209 | 300 | 69.67% |
| budget_relationship_ok | 231 | 300 | 77.00% |
| budget_selection_ok | 150 | 300 | 50.00% |
| budget_user_constraint_ok | 253 | 300 | 84.33% |
| budget_within_user_budget | 280 | 300 | 93.33% |
| city_ok | 300 | 300 | 100.00% |
| date_range_ok | 300 | 300 | 100.00% |
| day_dates_ok | 300 | 300 | 100.00% |
| day_index_ok | 300 | 300 | 100.00% |
| days_len_ok | 300 | 300 | 100.00% |
| dpo_soft_pass | 151 | 300 | 50.33% |
| dpo_soft_recomputed_budget_pass | 107 | 300 | 35.67% |
| hard_pass | 289 | 300 | 96.33% |
| hotel_budget_covers_nights | 287 | 300 | 95.67% |
| hotel_budget_relation_ok | 291 | 300 | 97.00% |
| hotel_distance_placeholder_ok | 300 | 300 | 100.00% |
| hotel_grounding_ok | 299 | 300 | 99.67% |
| invalid_hotel_name_ok | 300 | 300 | 100.00% |
| json_extract_ok | 300 | 300 | 100.00% |
| legacy_hard_pass | 163 | 300 | 54.33% |
| location_object_ok | 300 | 300 | 100.00% |
| meal_budget_consistent | 0 | 300 | 0.00% |
| meal_complete | 300 | 300 | 100.00% |
| meal_cost_scale_ok | 242 | 300 | 80.67% |
| meal_diversity_ok | 260 | 300 | 86.67% |
| meal_grounding_ok | 297 | 300 | 99.00% |
| meal_lunch_dinner_same_day_ok | 293 | 300 | 97.67% |
| meal_repeat_limit_ok | 267 | 300 | 89.00% |
| meal_specific_ok | 300 | 300 | 100.00% |
| meal_valid_semantics_ok | 298 | 300 | 99.33% |
| middle_hotel_ok | 300 | 300 | 100.00% |
| recomputed_budget_fit_ok | 150 | 300 | 50.00% |
| recomputed_budget_hard_ok | 217 | 300 | 72.33% |
| recomputed_budget_level_aligned | 150 | 300 | 50.00% |
| recomputed_budget_preference_aligned | 150 | 300 | 50.00% |
| recomputed_budget_user_constraint_ok | 217 | 300 | 72.33% |
| recomputed_budget_within_user_budget | 255 | 300 | 85.00% |
| schema_ok | 300 | 300 | 100.00% |
| sft_budget_semantic_hard_pass | 183 | 300 | 61.00% |
| sft_hard_pass | 289 | 300 | 96.33% |
| sft_no_budget_sum_hard_pass | 289 | 300 | 96.33% |
| sft_strict_hard_pass | 0 | 300 | 0.00% |
| transportation_budget_nonnegative | 300 | 300 | 100.00% |
| weather_dates_ok | 300 | 300 | 100.00% |
| weather_match | 300 | 300 | 100.00% |

## Numeric Metrics

```json
{
  "attraction_diversity_unique_rate": {
    "avg": 0.9815,
    "p50": 1.0,
    "p90": 1.0
  },
  "attraction_grounding_rate": {
    "avg": 0.9984,
    "p50": 1.0,
    "p90": 1.0
  },
  "hotel_grounding_rate": {
    "avg": 0.9967,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_diversity_unique_rate": {
    "avg": 0.9053,
    "p50": 0.9333,
    "p90": 1.0
  },
  "meal_food_pois_grounding_rate": {
    "avg": 0.9991,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_grounding_rate": {
    "avg": 0.9991,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_semantic_valid_rate": {
    "avg": 0.9994,
    "p50": 1.0,
    "p90": 1.0
  },
  "recomputed_budget_per_person_day": {
    "avg": 921.3432,
    "p50": 913.75,
    "p90": 1458.33
  },
  "recomputed_budget_total": {
    "avg": 9844.5767,
    "p50": 9062.0,
    "p90": 17310.0
  }
}
```

## Failure Types

```json
{
  "meal_budget_inconsistent": 300,
  "attraction_budget_inconsistent": 216,
  "budget_arithmetic_inconsistent": 107,
  "budget_preference_mismatch": 91,
  "budget_relationship_mismatch": 69,
  "meal_cost_scale_too_low": 58,
  "budget_hard_constraint_exceeded": 47,
  "attraction_repeat_too_many": 43,
  "meal_repeat_too_many": 33,
  "hotel_budget_underestimated": 13,
  "meal_same_day_lunch_dinner_repeat": 7,
  "meal_invalid_name": 2,
  "too_many_attractions": 2,
  "meal_grounding_miss": 1
}
```

## Failure Examples

### v3_hard_realbudget_eval_000004
- request: 张家界 2026-05-11->2026-05-13 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 597, "expected_total_attractions": 597, "reported_total_attractions": 697, "meal_per_person_cost_sum": 845, "expected_total_meals": 845, "reported_total_meals": 819, "reported_total_transportation": 300}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 597, "expected_total_attractions": 597, "reported_total_attractions": 697, "meal_per_person_cost_sum": 845, "expected_total_meals": 845, "reported_total_meals": 819, "reported_total_transportation": 300}}, {"stage": "rule", "type": "budget_hard_constraint_exceeded", "details": {"part_sum": 4416, "total": 4416, "diff": 0, "requested_budget": {"available": true, "amount": 3200, "scope": "total", "party_size": 1, "total": 3200, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "hard"}, "per_person_day": 1472.0, "budget_level": "comfortable", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "hard", "amount": 3200, "target_min_ratio": 0.7, "target_max_ratio": 1.0, "target_min_total": 2200, "target_max_total": 3200, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": true, "within_user_budget": false, "user_constraint_ok": false, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 1, "room_count": 1, "priced_nights": 2, "expected_min_total_hotels": 2600, "reported_total_hotels": 2600, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_hard_realbudget_eval_000008
- request: 大理 2026-05-11->2026-05-13 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 9099, "total": 6100, "diff": 2999, "requested_budget": {"available": true, "amount": 8700, "scope": "total", "party_size": 3, "total": 8700, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "hard"}, "per_person_day": 677.78, "budget_level": "comfortable", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "hard", "amount": 8700, "target_min_ratio": 0.7, "target_max_ratio": 1.0, "target_min_total": 6100, "target_max_total": 8700, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 3, "room_count": 2, "priced_nights": 2, "expected_min_total_hotels": 5200, "reported_total_hotels": 5200, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 484, "expected_total_attractions": 1452, "reported_total_attractions": 1536, "meal_per_person_cost_sum": 780, "expected_total_meals": 2340, "reported_total_meals": 1563, "reported_total_transportation": 800}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 484, "expected_total_attractions": 1452, "reported_total_attractions": 1536, "meal_per_person_cost_sum": 780, "expected_total_meals": 2340, "reported_total_meals": 1563, "reported_total_transportation": 800}}]`

### v3_hard_realbudget_eval_000006
- request: 南京 2026-07-06->2026-07-09 days=4 transport=自驾 hotel=亲子酒店 prefs=['亲子', '动物园', '海洋馆', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 75, "expected_total_attractions": 225, "reported_total_attractions": 210, "meal_per_person_cost_sum": 902, "expected_total_meals": 2706, "reported_total_meals": 1800, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 75, "expected_total_attractions": 225, "reported_total_attractions": 210, "meal_per_person_cost_sum": 902, "expected_total_meals": 2706, "reported_total_meals": 1800, "reported_total_transportation": 200}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": true, "meal_cost_scale_ok": false, "budget_relationship_ok": false, "expected_total_hotels": 8100, "reported_total_hotels": 8100, "expected_total_attractions": 225, "reported_total_attractions": 210, "meal_scale_eval": {"ok": false, "party_total": 3, "budget_level": "standard", "per_person_lunch_dinner_floor": 35, "breakfast_policy": "excluded_from_meal_cost_scale", "meal_count": 12, "checked_count": 8, "failure_count": 1, "failures": [{"date": "2026-07-07", "type": "lunch", "name": "小潘记鸭血粉丝汤", "estimated_cost": 34, "min_expected_cost": 35}]}}}]`

### v3_hard_realbudget_eval_000002
- request: 杭州 2026-05-01->2026-05-04 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '夜市', '老字号', '城市漫步']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "赵府私厨·老杭帮菜", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-05-01", "type": "lunch", "name": "赵府私厨·老杭帮菜(西湖老店)"}, {"date": "2026-05-02", "type": "dinner", "name": "赵府私厨·老杭帮菜(西湖老店)"}, {"date": "2026-05-03", "type": "lunch", "name": "赵府私厨·老杭帮菜(西湖老店)"}, {"date": "2026-05-04", "type": "lunch", "name": "赵府私厨·老杭帮菜(西湖老店)"}]}]}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 5060, "total": 4860, "diff": 200, "requested_budget": {"available": true, "amount": 6300, "scope": "total", "party_size": 4, "total": 6300, "source": "budget_constraint", "budget_level": "limited", "strictness": "hard"}, "per_person_day": 303.75, "budget_level": "limited", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "limited", "strictness": "hard", "amount": 6300, "target_min_ratio": 0.72, "target_max_ratio": 1.0, "target_min_total": 4500, "target_max_total": 6300, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 4, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 1500, "reported_total_hotels": 1500, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 229, "expected_total_attractions": 916, "reported_total_attractions": 756, "meal_per_person_cost_sum": 761, "expected_total_meals": 3044, "reported_total_meals": 2604, "reported_total_transportation": 200}}]`

### v3_hard_realbudget_eval_000001
- request: 桂林 2026-09-04->2026-09-07 days=4 transport=打车 hotel=高端酒店 prefs=['高端酒店', '艺术', '特色餐厅', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 2, "room_count": 1, "priced_nights": 3, "expected_min_total_hotels": 3900, "reported_total_hotels": 7800, "diff": 3900, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 916, "expected_total_attractions": 1832, "reported_total_attractions": 1892, "meal_per_person_cost_sum": 1054, "expected_total_meals": 2108, "reported_total_meals": 1800, "reported_total_transportation": 500}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 916, "expected_total_attractions": 1832, "reported_total_attractions": 1892, "meal_per_person_cost_sum": 1054, "expected_total_meals": 2108, "reported_total_meals": 1800, "reported_total_transportation": 500}}]`

### v3_hard_realbudget_eval_000005
- request: 广州 2026-07-06->2026-07-10 days=5 transport=公共交通 hotel=民宿 prefs=['摄影', '自然风光', '城市漫步', '本地菜']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "广州动物园", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-07-08", "day_index": 2, "name": "广州动物园"}, {"date": "2026-07-10", "day_index": 4, "name": "广州动物园"}]}]}, {"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-07-09", "lunch": "滋粥楼·顺德菜(番禺广场总店)", "dinner": "滋粥楼·顺德菜(南村万博长隆商圈店)"}]}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 2901, "total": 2701, "diff": 200, "requested_budget": {"available": true, "amount": 4500, "scope": "total", "party_size": 1, "total": 4500, "source": "budget_constraint", "budget_level": "standard", "strictness": "hard"}, "per_person_day": 540.2, "budget_level": "standard", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "standard", "strictness": "hard", "amount": 4500, "target_min_ratio": 0.6, "target_max_ratio": 1.0, "target_min_total": 2700, "target_max_total": 4500, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 4, "party_total": 1, "room_count": 1, "priced_nights": 4, "expected_min_total_hotels": 1200, "reported_total_hotels": 1200, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_hard_realbudget_eval_000000
- request: 昆明 2026-04-07->2026-04-11 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 17300, "total": 17200, "diff": 100, "requested_budget": {"available": true, "amount": 24700, "scope": "total", "party_size": 5, "total": 24700, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "hard"}, "per_person_day": 688.0, "budget_level": "comfortable", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "hard", "amount": 24700, "target_min_ratio": 0.7, "target_max_ratio": 1.0, "target_min_total": 17300, "target_max_total": 24700, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 4, "party_total": 5, "room_count": 3, "priced_nights": 4, "expected_min_total_hotels": 7200, "reported_total_hotels": 7200, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 5, "hotel_room_count": 3, "attraction_ticket_sum": 483, "expected_total_attractions": 2415, "reported_total_attractions": 2165, "meal_per_person_cost_sum": 839, "expected_total_meals": 4195, "reported_total_meals": 4635, "reported_total_transportation": 3300}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 5, "hotel_room_count": 3, "attraction_ticket_sum": 483, "expected_total_attractions": 2415, "reported_total_attractions": 2165, "meal_per_person_cost_sum": 839, "expected_total_meals": 4195, "reported_total_meals": 4635, "reported_total_transportation": 3300}}]`

### v3_hard_realbudget_eval_000003
- request: 西安 2025-05-07->2025-05-11 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "西安碑林博物馆", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2025-05-08", "day_index": 1, "name": "西安碑林博物馆"}, {"date": "2025-05-11", "day_index": 4, "name": "西安碑林博物馆"}]}, {"name_key": "西安博物院", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2025-05-09", "day_index": 2, "name": "西安博物院"}, {"date": "2025-05-10", "day_index": 3, "name": "西安博物院"}]}]}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 6044, "total": 5044, "diff": 1000, "requested_budget": {"available": true, "amount": 8400, "scope": "total", "party_size": 2, "total": 8400, "source": "budget_constraint", "budget_level": "standard", "strictness": "hard"}, "per_person_day": 504.4, "budget_level": "standard", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "standard", "strictness": "hard", "amount": 8400, "target_min_ratio": 0.6, "target_max_ratio": 1.0, "target_min_total": 5000, "target_max_total": 8400, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 4, "party_total": 2, "room_count": 1, "priced_nights": 4, "expected_min_total_hotels": 1800, "reported_total_hotels": 1800, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 332, "expected_total_attractions": 664, "reported_total_attractions": 756, "meal_per_person_cost_sum": 704, "expected_total_meals": 1408, "reported_total_meals": 1988, "reported_total_transportation": 1500}}]`

### v3_hard_realbudget_eval_000007
- request: 成都 2026-05-11->2026-05-15 days=5 transport=公共交通 hotel=民宿 prefs=['小众展馆', '咖啡', '艺术', '城市漫步', '特色餐厅']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 10968, "total": 11000, "diff": -32, "requested_budget": {"available": true, "amount": 11000, "scope": "total", "party_size": 2, "total": 11000, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "soft"}, "per_person_day": 1100.0, "budget_level": "comfortable", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "soft", "amount": 11000, "target_min_ratio": 0.7, "target_max_ratio": 1.1, "target_min_total": 7700, "target_max_total": 12100, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 4, "party_total": 2, "room_count": 1, "priced_nights": 4, "expected_min_total_hotels": 1200, "reported_total_hotels": 1200, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 1294, "expected_total_attractions": 2588, "reported_total_attractions": 2640, "meal_per_person_cost_sum": 2714, "expected_total_meals": 5428, "reported_total_meals": 5928, "reported_total_transportation": 1200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 1294, "expected_total_attractions": 2588, "reported_total_attractions": 2640, "meal_per_person_cost_sum": 2714, "expected_total_meals": 5428, "reported_total_meals": 5928, "reported_total_transportation": 1200}}]`

### v3_hard_realbudget_eval_000010
- request: 西安 2026-08-05->2026-08-09 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 5, "hotel_room_count": 3, "attraction_ticket_sum": 671, "expected_total_attractions": 3355, "reported_total_attractions": 3390, "meal_per_person_cost_sum": 842, "expected_total_meals": 4210, "reported_total_meals": 3600, "reported_total_transportation": 400}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 5, "hotel_room_count": 3, "attraction_ticket_sum": 671, "expected_total_attractions": 3355, "reported_total_attractions": 3390, "meal_per_person_cost_sum": 842, "expected_total_meals": 4210, "reported_total_meals": 3600, "reported_total_transportation": 400}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": true, "meal_cost_scale_ok": false, "budget_relationship_ok": false, "expected_total_hotels": 16200, "reported_total_hotels": 16200, "expected_total_attractions": 3355, "reported_total_attractions": 3390, "meal_scale_eval": {"ok": false, "party_total": 5, "budget_level": "comfortable", "per_person_lunch_dinner_floor": 50, "breakfast_policy": "excluded_from_meal_cost_scale", "meal_count": 15, "checked_count": 10, "failure_count": 3, "failures": [{"date": "2026-08-08", "type": "lunch", "name": "虎子水盆羊肉(翠华路总店)", "estimated_cost": 43, "min_expected_cost": 50}, {"date": "2026-08-09", "type": "lunch", "name": "马洪小炒泡馍馆", "estimated_cost": 31, "min_expected_cost": 50}, {"date": "2026-08-09", "type": "dinner", "name": "果渊斋老米家泡馍馆(回坊总店)", "estimated_cost": 31, "min_expected_cost": 50}]}}}]`

### v3_hard_realbudget_eval_000011
- request: 福州 2026-06-21->2026-06-24 days=4 transport=打车 hotel=高端酒店 prefs=['高端酒店', '艺术', '特色餐厅', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 407, "expected_total_attractions": 814, "reported_total_attractions": 834, "meal_per_person_cost_sum": 1457, "expected_total_meals": 2914, "reported_total_meals": 3404, "reported_total_transportation": 2000}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 407, "expected_total_attractions": 814, "reported_total_attractions": 834, "meal_per_person_cost_sum": 1457, "expected_total_meals": 2914, "reported_total_meals": 3404, "reported_total_transportation": 2000}}]`

### v3_hard_realbudget_eval_000009
- request: 苏州 2026-04-30->2026-05-03 days=4 transport=打车 hotel=亲子酒店 prefs=['亲子', '老人友好', '博物馆', '城市公园', '特色餐厅']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 320, "expected_total_attractions": 1280, "reported_total_attractions": 1440, "meal_per_person_cost_sum": 699, "expected_total_meals": 2796, "reported_total_meals": 3060, "reported_total_transportation": 150}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 320, "expected_total_attractions": 1280, "reported_total_attractions": 1440, "meal_per_person_cost_sum": 699, "expected_total_meals": 2796, "reported_total_meals": 3060, "reported_total_transportation": 150}}]`

### v3_hard_realbudget_eval_000014
- request: 成都 2026-06-06->2026-06-08 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 4103, "total": 3003, "diff": 1100, "requested_budget": {"available": true, "amount": 4300, "scope": "total", "party_size": 1, "total": 4300, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "hard"}, "per_person_day": 1001.0, "budget_level": "comfortable", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "hard", "amount": 4300, "target_min_ratio": 0.7, "target_max_ratio": 1.0, "target_min_total": 3000, "target_max_total": 4300, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 1, "room_count": 1, "priced_nights": 2, "expected_min_total_hotels": 2700, "reported_total_hotels": 2700, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 165, "expected_total_attractions": 165, "reported_total_attractions": 165, "meal_per_person_cost_sum": 1338, "expected_total_meals": 1338, "reported_total_meals": 1138, "reported_total_transportation": 100}}]`

### v3_hard_realbudget_eval_000012
- request: 洛阳 2025-05-07->2025-05-10 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '夜市', '老字号', '城市漫步']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 378, "expected_total_attractions": 1512, "reported_total_attractions": 1552, "meal_per_person_cost_sum": 610, "expected_total_meals": 2440, "reported_total_meals": 2000, "reported_total_transportation": 400}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 378, "expected_total_attractions": 1512, "reported_total_attractions": 1552, "meal_per_person_cost_sum": 610, "expected_total_meals": 2440, "reported_total_meals": 2000, "reported_total_transportation": 400}}]`

### v3_hard_realbudget_eval_000016
- request: 苏州 2026-06-06->2026-06-09 days=4 transport=自驾 hotel=亲子酒店 prefs=['亲子', '动物园', '海洋馆', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 10557, "total": 9657, "diff": 900, "requested_budget": {"available": true, "amount": 10000, "scope": "total", "party_size": 3, "total": 10000, "source": "budget_constraint", "budget_level": "standard", "strictness": "hard"}, "per_person_day": 804.75, "budget_level": "standard", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "standard", "strictness": "hard", "amount": 10000, "target_min_ratio": 0.6, "target_max_ratio": 1.0, "target_min_total": 6000, "target_max_total": 10000, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 3, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 8100, "reported_total_hotels": 8100, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 120, "expected_total_attractions": 360, "reported_total_attractions": 345, "meal_per_person_cost_sum": 585, "expected_total_meals": 1755, "reported_total_meals": 1512, "reported_total_transportation": 600}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 120, "expected_total_attractions": 360, "reported_total_attractions": 345, "meal_per_person_cost_sum": 585, "expected_total_meals": 1755, "reported_total_meals": 1512, "reported_total_transportation": 600}}]`

### v3_hard_realbudget_eval_000018
- request: 天津 2026-07-06->2026-07-08 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 16190, "total": 7890, "diff": 8300, "requested_budget": {"available": true, "amount": 7900, "scope": "total", "party_size": 3, "total": 7900, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "hard"}, "per_person_day": 876.67, "budget_level": "comfortable", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "hard", "amount": 7900, "target_min_ratio": 0.7, "target_max_ratio": 1.0, "target_min_total": 5500, "target_max_total": 7900, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 3, "room_count": 2, "priced_nights": 2, "expected_min_total_hotels": 7200, "reported_total_hotels": 7200, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 851, "expected_total_attractions": 2553, "reported_total_attractions": 2583, "meal_per_person_cost_sum": 3341, "expected_total_meals": 10023, "reported_total_meals": 5807, "reported_total_transportation": 600}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 851, "expected_total_attractions": 2553, "reported_total_attractions": 2583, "meal_per_person_cost_sum": 3341, "expected_total_meals": 10023, "reported_total_meals": 5807, "reported_total_transportation": 600}}]`

### v3_hard_realbudget_eval_000013
- request: 武汉 2026-05-09->2026-05-13 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 223, "expected_total_attractions": 446, "reported_total_attractions": 416, "meal_per_person_cost_sum": 940, "expected_total_meals": 1880, "reported_total_meals": 2004, "reported_total_transportation": 400}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 223, "expected_total_attractions": 446, "reported_total_attractions": 416, "meal_per_person_cost_sum": 940, "expected_total_meals": 1880, "reported_total_meals": 2004, "reported_total_transportation": 400}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": true, "meal_cost_scale_ok": false, "budget_relationship_ok": false, "expected_total_hotels": 1600, "reported_total_hotels": 1600, "expected_total_attractions": 446, "reported_total_attractions": 416, "meal_scale_eval": {"ok": false, "party_total": 2, "budget_level": "standard", "per_person_lunch_dinner_floor": 35, "breakfast_policy": "excluded_from_meal_cost_scale", "meal_count": 15, "checked_count": 10, "failure_count": 1, "failures": [{"date": "2026-05-13", "type": "lunch", "name": "刘聋子牛肉粉馆(汉阳龙兴东街店)", "estimated_cost": 27, "min_expected_cost": 35}]}}}]`

### v3_hard_realbudget_eval_000017
- request: 苏州 2026-05-09->2026-05-13 days=5 transport=公共交通 hotel=民宿 prefs=['小众展馆', '咖啡', '艺术', '城市漫步', '特色餐厅']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 6494, "total": 7494, "diff": -1000, "requested_budget": {"available": true, "amount": 10100, "scope": "total", "party_size": 2, "total": 10100, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "soft"}, "per_person_day": 749.4, "budget_level": "comfortable", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "soft", "amount": 10100, "target_min_ratio": 0.7, "target_max_ratio": 1.1, "target_min_total": 7100, "target_max_total": 11100, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 4, "party_total": 2, "room_count": 1, "priced_nights": 4, "expected_min_total_hotels": 1200, "reported_total_hotels": 1200, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 320, "expected_total_attractions": 640, "reported_total_attractions": 690, "meal_per_person_cost_sum": 921, "expected_total_meals": 1842, "reported_total_meals": 2604, "reported_total_transportation": 2000}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 320, "expected_total_attractions": 640, "reported_total_attractions": 690, "meal_per_person_cost_sum": 921, "expected_total_meals": 1842, "reported_total_meals": 2604, "reported_total_transportation": 2000}}]`

### v3_hard_realbudget_eval_000019
- request: 丽江 2026-05-11->2026-05-14 days=4 transport=打车 hotel=亲子酒店 prefs=['亲子', '老人友好', '博物馆', '城市公园', '特色餐厅']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 1164, "expected_total_attractions": 2328, "reported_total_attractions": 2674, "meal_per_person_cost_sum": 812, "expected_total_meals": 1624, "reported_total_meals": 1338, "reported_total_transportation": 800}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 1164, "expected_total_attractions": 2328, "reported_total_attractions": 2674, "meal_per_person_cost_sum": 812, "expected_total_meals": 1624, "reported_total_meals": 1338, "reported_total_transportation": 800}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": true, "meal_cost_scale_ok": false, "budget_relationship_ok": false, "expected_total_hotels": 3900, "reported_total_hotels": 3900, "expected_total_attractions": 2328, "reported_total_attractions": 2674, "meal_scale_eval": {"ok": false, "party_total": 2, "budget_level": "comfortable", "per_person_lunch_dinner_floor": 50, "breakfast_policy": "excluded_from_meal_cost_scale", "meal_count": 12, "checked_count": 8, "failure_count": 1, "failures": [{"date": "2026-05-12", "type": "dinner", "name": "云老官保山火塘牛肉(丽江总店)", "estimated_cost": 34, "min_expected_cost": 50}]}}}]`

### v3_hard_realbudget_eval_000020
- request: 杭州 2026-06-21->2026-06-25 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 5, "hotel_room_count": 3, "attraction_ticket_sum": 160, "expected_total_attractions": 800, "reported_total_attractions": 750, "meal_per_person_cost_sum": 1111, "expected_total_meals": 5555, "reported_total_meals": 5950, "reported_total_transportation": 1000}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 5, "hotel_room_count": 3, "attraction_ticket_sum": 160, "expected_total_attractions": 800, "reported_total_attractions": 750, "meal_per_person_cost_sum": 1111, "expected_total_meals": 5555, "reported_total_meals": 5950, "reported_total_transportation": 1000}}]`
