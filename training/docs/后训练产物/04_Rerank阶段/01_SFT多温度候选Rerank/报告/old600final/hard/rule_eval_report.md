# Rule Eval Report: 260513_rerank_old600final_hard_w10

- records: 300
- generations: `training/outputs/eval/by_model/sft_qwen25_7b_v3_260513_rerank_old600final/260513_rerank_old600final_hard_w10/generations.jsonl`
- records_path: `training/data/v3/eval_hard/records.jsonl`

## Boolean Metrics

| Metric | Pass | Total | Rate |
| --- | ---: | ---: | ---: |
| accommodation_type_ok | 300 | 300 | 100.00% |
| attraction_budget_consistent | 74 | 300 | 24.67% |
| attraction_budget_party_relation_ok | 295 | 300 | 98.33% |
| attraction_count_ok | 297 | 300 | 99.00% |
| attraction_diversity_ok | 273 | 300 | 91.00% |
| attraction_grounding_ok | 297 | 300 | 99.00% |
| attraction_repeat_limit_ok | 273 | 300 | 91.00% |
| budget_arithmetic_consistent | 224 | 300 | 74.67% |
| budget_consistent | 224 | 300 | 74.67% |
| budget_level_aligned | 211 | 300 | 70.33% |
| budget_preference_aligned | 211 | 300 | 70.33% |
| budget_relationship_ok | 260 | 300 | 86.67% |
| budget_selection_ok | 185 | 300 | 61.67% |
| budget_user_constraint_ok | 252 | 300 | 84.00% |
| budget_within_user_budget | 275 | 300 | 91.67% |
| city_ok | 300 | 300 | 100.00% |
| date_range_ok | 300 | 300 | 100.00% |
| day_dates_ok | 300 | 300 | 100.00% |
| day_index_ok | 300 | 300 | 100.00% |
| days_len_ok | 300 | 300 | 100.00% |
| dpo_soft_pass | 178 | 300 | 59.33% |
| dpo_soft_recomputed_budget_pass | 153 | 300 | 51.00% |
| hard_pass | 292 | 300 | 97.33% |
| hotel_budget_covers_nights | 287 | 300 | 95.67% |
| hotel_budget_relation_ok | 294 | 300 | 98.00% |
| hotel_distance_placeholder_ok | 300 | 300 | 100.00% |
| hotel_grounding_ok | 299 | 300 | 99.67% |
| invalid_hotel_name_ok | 300 | 300 | 100.00% |
| json_extract_ok | 300 | 300 | 100.00% |
| legacy_hard_pass | 194 | 300 | 64.67% |
| location_object_ok | 300 | 300 | 100.00% |
| meal_budget_consistent | 0 | 300 | 0.00% |
| meal_complete | 300 | 300 | 100.00% |
| meal_cost_scale_ok | 269 | 300 | 89.67% |
| meal_diversity_ok | 269 | 300 | 89.67% |
| meal_grounding_ok | 299 | 300 | 99.67% |
| meal_lunch_dinner_same_day_ok | 299 | 300 | 99.67% |
| meal_repeat_limit_ok | 270 | 300 | 90.00% |
| meal_specific_ok | 300 | 300 | 100.00% |
| meal_valid_semantics_ok | 299 | 300 | 99.67% |
| middle_hotel_ok | 300 | 300 | 100.00% |
| recomputed_budget_fit_ok | 185 | 300 | 61.67% |
| recomputed_budget_hard_ok | 226 | 300 | 75.33% |
| recomputed_budget_level_aligned | 185 | 300 | 61.67% |
| recomputed_budget_preference_aligned | 185 | 300 | 61.67% |
| recomputed_budget_user_constraint_ok | 226 | 300 | 75.33% |
| recomputed_budget_within_user_budget | 260 | 300 | 86.67% |
| schema_ok | 300 | 300 | 100.00% |
| sft_budget_semantic_hard_pass | 208 | 300 | 69.33% |
| sft_hard_pass | 292 | 300 | 97.33% |
| sft_no_budget_sum_hard_pass | 292 | 300 | 97.33% |
| sft_strict_hard_pass | 0 | 300 | 0.00% |
| transportation_budget_nonnegative | 300 | 300 | 100.00% |
| weather_dates_ok | 300 | 300 | 100.00% |
| weather_match | 300 | 300 | 100.00% |

## Numeric Metrics

```json
{
  "attraction_diversity_unique_rate": {
    "avg": 0.9898,
    "p50": 1.0,
    "p90": 1.0
  },
  "attraction_grounding_rate": {
    "avg": 0.999,
    "p50": 1.0,
    "p90": 1.0
  },
  "hotel_grounding_rate": {
    "avg": 0.9992,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_diversity_unique_rate": {
    "avg": 0.9011,
    "p50": 0.9333,
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
    "avg": 920.507,
    "p50": 919.8,
    "p90": 1464.8
  },
  "recomputed_budget_total": {
    "avg": 9803.3733,
    "p50": 9202.0,
    "p90": 17735.0
  }
}
```

## Failure Types

```json
{
  "meal_budget_inconsistent": 300,
  "attraction_budget_inconsistent": 226,
  "budget_preference_mismatch": 89,
  "budget_arithmetic_inconsistent": 76,
  "budget_hard_constraint_exceeded": 48,
  "budget_relationship_mismatch": 40,
  "meal_cost_scale_too_low": 31,
  "meal_repeat_too_many": 30,
  "attraction_repeat_too_many": 27,
  "hotel_budget_underestimated": 13,
  "too_many_attractions": 3,
  "meal_same_day_lunch_dinner_repeat": 1,
  "meal_invalid_name": 1
}
```

## Failure Examples

### v3_hard_realbudget_eval_000000
- request: 昆明 2026-04-07->2026-04-11 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 17295, "total": 17300, "diff": -5, "requested_budget": {"available": true, "amount": 24700, "scope": "total", "party_size": 5, "total": 24700, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "hard"}, "per_person_day": 692.0, "budget_level": "comfortable", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "hard", "amount": 24700, "target_min_ratio": 0.7, "target_max_ratio": 1.0, "target_min_total": 17300, "target_max_total": 24700, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 4, "party_total": 5, "room_count": 3, "priced_nights": 4, "expected_min_total_hotels": 7200, "reported_total_hotels": 7200, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 5, "hotel_room_count": 3, "attraction_ticket_sum": 959, "expected_total_attractions": 4795, "reported_total_attractions": 4395, "meal_per_person_cost_sum": 904, "expected_total_meals": 4520, "reported_total_meals": 4600, "reported_total_transportation": 1100}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 5, "hotel_room_count": 3, "attraction_ticket_sum": 959, "expected_total_attractions": 4795, "reported_total_attractions": 4395, "meal_per_person_cost_sum": 904, "expected_total_meals": 4520, "reported_total_meals": 4600, "reported_total_transportation": 1100}}]`

### v3_hard_realbudget_eval_000001
- request: 桂林 2026-09-04->2026-09-07 days=4 transport=打车 hotel=高端酒店 prefs=['高端酒店', '艺术', '特色餐厅', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 10900, "total": 10800, "diff": 100, "requested_budget": {"available": true, "amount": 13100, "scope": "total", "party_size": 2, "total": 13100, "source": "budget_constraint", "budget_level": "premium", "strictness": "soft"}, "per_person_day": 1350.0, "budget_level": "premium", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "premium", "strictness": "soft", "amount": 13100, "target_min_ratio": 0.75, "target_max_ratio": 1.12, "target_min_total": 9800, "target_max_total": 14700, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 2, "room_count": 1, "priced_nights": 3, "expected_min_total_hotels": 3900, "reported_total_hotels": 3900, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 995, "expected_total_attractions": 1990, "reported_total_attractions": 2322, "meal_per_person_cost_sum": 1189, "expected_total_meals": 2378, "reported_total_meals": 2678, "reported_total_transportation": 2000}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 995, "expected_total_attractions": 1990, "reported_total_attractions": 2322, "meal_per_person_cost_sum": 1189, "expected_total_meals": 2378, "reported_total_meals": 2678, "reported_total_transportation": 2000}}]`

### v3_hard_realbudget_eval_000003
- request: 西安 2025-05-07->2025-05-11 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "西安博物院", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2025-05-09", "day_index": 2, "name": "西安博物院"}, {"date": "2025-05-11", "day_index": 4, "name": "西安博物院"}]}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 267, "expected_total_attractions": 534, "reported_total_attractions": 630, "meal_per_person_cost_sum": 859, "expected_total_meals": 1718, "reported_total_meals": 2004, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 267, "expected_total_attractions": 534, "reported_total_attractions": 630, "meal_per_person_cost_sum": 859, "expected_total_meals": 1718, "reported_total_meals": 2004, "reported_total_transportation": 200}}]`

### v3_hard_realbudget_eval_000004
- request: 张家界 2026-05-11->2026-05-13 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆']
- errors: `[{"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 610, "expected_total_attractions": 610, "reported_total_attractions": 610, "meal_per_person_cost_sum": 694, "expected_total_meals": 694, "reported_total_meals": 660, "reported_total_transportation": 300}}, {"stage": "rule", "type": "budget_hard_constraint_exceeded", "details": {"part_sum": 4170, "total": 4170, "diff": 0, "requested_budget": {"available": true, "amount": 3200, "scope": "total", "party_size": 1, "total": 3200, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "hard"}, "per_person_day": 1390.0, "budget_level": "comfortable", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "hard", "amount": 3200, "target_min_ratio": 0.7, "target_max_ratio": 1.0, "target_min_total": 2200, "target_max_total": 3200, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": true, "within_user_budget": false, "user_constraint_ok": false, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 1, "room_count": 1, "priced_nights": 2, "expected_min_total_hotels": 2600, "reported_total_hotels": 2600, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "budget_preference_mismatch", "details": {"part_sum": 4170, "total": 4170, "diff": 0, "requested_budget": {"available": true, "amount": 3200, "scope": "total", "party_size": 1, "total": 3200, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "hard"}, "per_person_day": 1390.0, "budget_level": "comfortable", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "hard", "amount": 3200, "target_min_ratio": 0.7, "target_max_ratio": 1.0, "target_min_total": 2200, "target_max_total": 3200, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": true, "within_user_budget": false, "user_constraint_ok": false, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 1, "room_count": 1, "priced_nights": 2, "expected_min_total_hotels": 2600, "reported_total_hotels": 2600, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_hard_realbudget_eval_000005
- request: 广州 2026-07-06->2026-07-10 days=5 transport=公共交通 hotel=民宿 prefs=['摄影', '自然风光', '城市漫步', '本地菜']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 3601, "total": 2701, "diff": 900, "requested_budget": {"available": true, "amount": 4500, "scope": "total", "party_size": 1, "total": 4500, "source": "budget_constraint", "budget_level": "standard", "strictness": "hard"}, "per_person_day": 540.2, "budget_level": "standard", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "standard", "strictness": "hard", "amount": 4500, "target_min_ratio": 0.6, "target_max_ratio": 1.0, "target_min_total": 2700, "target_max_total": 4500, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 4, "party_total": 1, "room_count": 1, "priced_nights": 4, "expected_min_total_hotels": 1200, "reported_total_hotels": 1200, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 186, "expected_total_attractions": 186, "reported_total_attractions": 176, "meal_per_person_cost_sum": 1332, "expected_total_meals": 1332, "reported_total_meals": 1225, "reported_total_transportation": 1000}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 186, "expected_total_attractions": 186, "reported_total_attractions": 176, "meal_per_person_cost_sum": 1332, "expected_total_meals": 1332, "reported_total_meals": 1225, "reported_total_transportation": 1000}}]`

### v3_hard_realbudget_eval_000006
- request: 南京 2026-07-06->2026-07-09 days=4 transport=自驾 hotel=亲子酒店 prefs=['亲子', '动物园', '海洋馆', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 45, "expected_total_attractions": 135, "reported_total_attractions": 105, "meal_per_person_cost_sum": 981, "expected_total_meals": 2943, "reported_total_meals": 2148, "reported_total_transportation": 250}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 45, "expected_total_attractions": 135, "reported_total_attractions": 105, "meal_per_person_cost_sum": 981, "expected_total_meals": 2943, "reported_total_meals": 2148, "reported_total_transportation": 250}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": false, "meal_cost_scale_ok": true, "budget_relationship_ok": false, "expected_total_hotels": 8100, "reported_total_hotels": 8100, "expected_total_attractions": 135, "reported_total_attractions": 105, "meal_scale_eval": {"ok": true, "party_total": 3, "budget_level": "standard", "per_person_lunch_dinner_floor": 35, "breakfast_policy": "excluded_from_meal_cost_scale", "meal_count": 12, "checked_count": 8, "failure_count": 0, "failures": []}}}]`

### v3_hard_realbudget_eval_000007
- request: 成都 2026-05-11->2026-05-15 days=5 transport=公共交通 hotel=民宿 prefs=['小众展馆', '咖啡', '艺术', '城市漫步', '特色餐厅']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 1473, "expected_total_attractions": 2946, "reported_total_attractions": 3174, "meal_per_person_cost_sum": 2594, "expected_total_meals": 5188, "reported_total_meals": 5808, "reported_total_transportation": 400}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 1473, "expected_total_attractions": 2946, "reported_total_attractions": 3174, "meal_per_person_cost_sum": 2594, "expected_total_meals": 5188, "reported_total_meals": 5808, "reported_total_transportation": 400}}]`

### v3_hard_realbudget_eval_000008
- request: 大理 2026-05-11->2026-05-13 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 8098, "total": 6198, "diff": 1900, "requested_budget": {"available": true, "amount": 8700, "scope": "total", "party_size": 3, "total": 8700, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "hard"}, "per_person_day": 688.67, "budget_level": "comfortable", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "hard", "amount": 8700, "target_min_ratio": 0.7, "target_max_ratio": 1.0, "target_min_total": 6100, "target_max_total": 8700, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 3, "room_count": 2, "priced_nights": 2, "expected_min_total_hotels": 5200, "reported_total_hotels": 5200, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 319, "expected_total_attractions": 957, "reported_total_attractions": 1095, "meal_per_person_cost_sum": 663, "expected_total_meals": 1989, "reported_total_meals": 1203, "reported_total_transportation": 600}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 319, "expected_total_attractions": 957, "reported_total_attractions": 1095, "meal_per_person_cost_sum": 663, "expected_total_meals": 1989, "reported_total_meals": 1203, "reported_total_transportation": 600}}]`

### v3_hard_realbudget_eval_000002
- request: 杭州 2026-05-01->2026-05-04 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '夜市', '老字号', '城市漫步']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 160, "expected_total_attractions": 640, "reported_total_attractions": 600, "meal_per_person_cost_sum": 764, "expected_total_meals": 3056, "reported_total_meals": 2000, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 160, "expected_total_attractions": 640, "reported_total_attractions": 600, "meal_per_person_cost_sum": 764, "expected_total_meals": 3056, "reported_total_meals": 2000, "reported_total_transportation": 200}}, {"stage": "rule", "type": "budget_preference_mismatch", "details": {"part_sum": 4300, "total": 4300, "diff": 0, "requested_budget": {"available": true, "amount": 6300, "scope": "total", "party_size": 4, "total": 6300, "source": "budget_constraint", "budget_level": "limited", "strictness": "hard"}, "per_person_day": 268.75, "budget_level": "limited", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "limited", "strictness": "hard", "amount": 6300, "target_min_ratio": 0.72, "target_max_ratio": 1.0, "target_min_total": 4500, "target_max_total": 6300, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": true, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 4, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 1500, "reported_total_hotels": 1500, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_hard_realbudget_eval_000010
- request: 西安 2026-08-05->2026-08-09 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 22600, "total": 22595, "diff": 5, "requested_budget": {"available": true, "amount": 30900, "scope": "total", "party_size": 5, "total": 30900, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "hard"}, "per_person_day": 903.8, "budget_level": "comfortable", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "hard", "amount": 30900, "target_min_ratio": 0.7, "target_max_ratio": 1.0, "target_min_total": 21600, "target_max_total": 30900, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 4, "party_total": 5, "room_count": 3, "priced_nights": 4, "expected_min_total_hotels": 16200, "reported_total_hotels": 16200, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 5, "hotel_room_count": 3, "attraction_ticket_sum": 199, "expected_total_attractions": 995, "reported_total_attractions": 1175, "meal_per_person_cost_sum": 858, "expected_total_meals": 4290, "reported_total_meals": 4225, "reported_total_transportation": 1000}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 5, "hotel_room_count": 3, "attraction_ticket_sum": 199, "expected_total_attractions": 995, "reported_total_attractions": 1175, "meal_per_person_cost_sum": 858, "expected_total_meals": 4290, "reported_total_meals": 4225, "reported_total_transportation": 1000}}]`

### v3_hard_realbudget_eval_000011
- request: 福州 2026-06-21->2026-06-24 days=4 transport=打车 hotel=高端酒店 prefs=['高端酒店', '艺术', '特色餐厅', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 680, "expected_total_attractions": 1360, "reported_total_attractions": 1698, "meal_per_person_cost_sum": 1482, "expected_total_meals": 2964, "reported_total_meals": 3954, "reported_total_transportation": 4000}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 680, "expected_total_attractions": 1360, "reported_total_attractions": 1698, "meal_per_person_cost_sum": 1482, "expected_total_meals": 2964, "reported_total_meals": 3954, "reported_total_transportation": 4000}}]`

### v3_hard_realbudget_eval_000009
- request: 苏州 2026-04-30->2026-05-03 days=4 transport=打车 hotel=亲子酒店 prefs=['亲子', '老人友好', '博物馆', '城市公园', '特色餐厅']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 320, "expected_total_attractions": 1280, "reported_total_attractions": 1420, "meal_per_person_cost_sum": 771, "expected_total_meals": 3084, "reported_total_meals": 3812, "reported_total_transportation": 1000}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 320, "expected_total_attractions": 1280, "reported_total_attractions": 1420, "meal_per_person_cost_sum": 771, "expected_total_meals": 3084, "reported_total_meals": 3812, "reported_total_transportation": 1000}}]`

### v3_hard_realbudget_eval_000012
- request: 洛阳 2025-05-07->2025-05-10 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '夜市', '老字号', '城市漫步']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 298, "expected_total_attractions": 1192, "reported_total_attractions": 1208, "meal_per_person_cost_sum": 614, "expected_total_meals": 2456, "reported_total_meals": 2004, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 298, "expected_total_attractions": 1192, "reported_total_attractions": 1208, "meal_per_person_cost_sum": 614, "expected_total_meals": 2456, "reported_total_meals": 2004, "reported_total_transportation": 200}}]`

### v3_hard_realbudget_eval_000014
- request: 成都 2026-06-06->2026-06-08 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 3466, "total": 3066, "diff": 400, "requested_budget": {"available": true, "amount": 4300, "scope": "total", "party_size": 1, "total": 4300, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "hard"}, "per_person_day": 1022.0, "budget_level": "comfortable", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "hard", "amount": 4300, "target_min_ratio": 0.7, "target_max_ratio": 1.0, "target_min_total": 3000, "target_max_total": 4300, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 1, "room_count": 1, "priced_nights": 2, "expected_min_total_hotels": 2700, "reported_total_hotels": 2700, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 130, "expected_total_attractions": 130, "reported_total_attractions": 130, "meal_per_person_cost_sum": 775, "expected_total_meals": 775, "reported_total_meals": 546, "reported_total_transportation": 90}}]`

### v3_hard_realbudget_eval_000013
- request: 武汉 2026-05-09->2026-05-13 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 163, "expected_total_attractions": 326, "reported_total_attractions": 306, "meal_per_person_cost_sum": 1004, "expected_total_meals": 2008, "reported_total_meals": 2184, "reported_total_transportation": 400}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 163, "expected_total_attractions": 326, "reported_total_attractions": 306, "meal_per_person_cost_sum": 1004, "expected_total_meals": 2008, "reported_total_meals": 2184, "reported_total_transportation": 400}}]`

### v3_hard_realbudget_eval_000016
- request: 苏州 2026-06-06->2026-06-09 days=4 transport=自驾 hotel=亲子酒店 prefs=['亲子', '动物园', '海洋馆', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 140, "expected_total_attractions": 420, "reported_total_attractions": 450, "meal_per_person_cost_sum": 689, "expected_total_meals": 2067, "reported_total_meals": 1659, "reported_total_transportation": 600}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 140, "expected_total_attractions": 420, "reported_total_attractions": 450, "meal_per_person_cost_sum": 689, "expected_total_meals": 2067, "reported_total_meals": 1659, "reported_total_transportation": 600}}, {"stage": "rule", "type": "budget_hard_constraint_exceeded", "details": {"part_sum": 10809, "total": 10809, "diff": 0, "requested_budget": {"available": true, "amount": 10000, "scope": "total", "party_size": 3, "total": 10000, "source": "budget_constraint", "budget_level": "standard", "strictness": "hard"}, "per_person_day": 900.75, "budget_level": "standard", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "standard", "strictness": "hard", "amount": 10000, "target_min_ratio": 0.6, "target_max_ratio": 1.0, "target_min_total": 6000, "target_max_total": 10000, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": true, "within_user_budget": true, "user_constraint_ok": false, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 3, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 8100, "reported_total_hotels": 8100, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_hard_realbudget_eval_000017
- request: 苏州 2026-05-09->2026-05-13 days=5 transport=公共交通 hotel=民宿 prefs=['小众展馆', '咖啡', '艺术', '城市漫步', '特色餐厅']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 6174, "total": 7174, "diff": -1000, "requested_budget": {"available": true, "amount": 10100, "scope": "total", "party_size": 2, "total": 10100, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "soft"}, "per_person_day": 717.4, "budget_level": "comfortable", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "soft", "amount": 10100, "target_min_ratio": 0.7, "target_max_ratio": 1.1, "target_min_total": 7100, "target_max_total": 11100, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 4, "party_total": 2, "room_count": 1, "priced_nights": 4, "expected_min_total_hotels": 1200, "reported_total_hotels": 1200, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 320, "expected_total_attractions": 640, "reported_total_attractions": 690, "meal_per_person_cost_sum": 734, "expected_total_meals": 1468, "reported_total_meals": 2284, "reported_total_transportation": 2000}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 320, "expected_total_attractions": 640, "reported_total_attractions": 690, "meal_per_person_cost_sum": 734, "expected_total_meals": 1468, "reported_total_meals": 2284, "reported_total_transportation": 2000}}]`

### v3_hard_realbudget_eval_000018
- request: 天津 2026-07-06->2026-07-08 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 897, "expected_total_attractions": 2691, "reported_total_attractions": 2838, "meal_per_person_cost_sum": 2288, "expected_total_meals": 6864, "reported_total_meals": 4152, "reported_total_transportation": 600}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 897, "expected_total_attractions": 2691, "reported_total_attractions": 2838, "meal_per_person_cost_sum": 2288, "expected_total_meals": 6864, "reported_total_meals": 4152, "reported_total_transportation": 600}}, {"stage": "rule", "type": "budget_hard_constraint_exceeded", "details": {"part_sum": 14790, "total": 14790, "diff": 0, "requested_budget": {"available": true, "amount": 7900, "scope": "total", "party_size": 3, "total": 7900, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "hard"}, "per_person_day": 1643.33, "budget_level": "comfortable", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "hard", "amount": 7900, "target_min_ratio": 0.7, "target_max_ratio": 1.0, "target_min_total": 5500, "target_max_total": 7900, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": true, "within_user_budget": false, "user_constraint_ok": false, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 3, "room_count": 2, "priced_nights": 2, "expected_min_total_hotels": 7200, "reported_total_hotels": 7200, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_hard_realbudget_eval_000019
- request: 丽江 2026-05-11->2026-05-14 days=4 transport=打车 hotel=亲子酒店 prefs=['亲子', '老人友好', '博物馆', '城市公园', '特色餐厅']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 8022, "total": 7022, "diff": 1000, "requested_budget": {"available": true, "amount": 7600, "scope": "total", "party_size": 2, "total": 7600, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "soft"}, "per_person_day": 877.75, "budget_level": "comfortable", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "soft", "amount": 7600, "target_min_ratio": 0.7, "target_max_ratio": 1.1, "target_min_total": 5300, "target_max_total": 8400, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 2, "room_count": 1, "priced_nights": 3, "expected_min_total_hotels": 3900, "reported_total_hotels": 3900, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 867, "expected_total_attractions": 1734, "reported_total_attractions": 1614, "meal_per_person_cost_sum": 921, "expected_total_meals": 1842, "reported_total_meals": 1708, "reported_total_transportation": 800}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 867, "expected_total_attractions": 1734, "reported_total_attractions": 1614, "meal_per_person_cost_sum": 921, "expected_total_meals": 1842, "reported_total_meals": 1708, "reported_total_transportation": 800}}]`

### v3_hard_realbudget_eval_000020
- request: 杭州 2026-06-21->2026-06-25 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 5, "hotel_room_count": 3, "attraction_ticket_sum": 160, "expected_total_attractions": 800, "reported_total_attractions": 750, "meal_per_person_cost_sum": 1102, "expected_total_meals": 5510, "reported_total_meals": 5950, "reported_total_transportation": 1000}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 5, "hotel_room_count": 3, "attraction_ticket_sum": 160, "expected_total_attractions": 800, "reported_total_attractions": 750, "meal_per_person_cost_sum": 1102, "expected_total_meals": 5510, "reported_total_meals": 5950, "reported_total_transportation": 1000}}]`
