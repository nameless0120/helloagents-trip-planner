# Rule Eval Report: 260513_rerank_ckpt104_hard_w10

- records: 300
- generations: `training/outputs/eval/by_model/sft_qwen25_7b_v3_260513_rerank_ckpt104/260513_rerank_ckpt104_hard_w10/generations.jsonl`
- records_path: `training/data/v3/eval_hard/records.jsonl`

## Boolean Metrics

| Metric | Pass | Total | Rate |
| --- | ---: | ---: | ---: |
| accommodation_type_ok | 300 | 300 | 100.00% |
| attraction_budget_consistent | 82 | 300 | 27.33% |
| attraction_budget_party_relation_ok | 293 | 300 | 97.67% |
| attraction_count_ok | 297 | 300 | 99.00% |
| attraction_diversity_ok | 281 | 300 | 93.67% |
| attraction_grounding_ok | 298 | 300 | 99.33% |
| attraction_repeat_limit_ok | 281 | 300 | 93.67% |
| budget_arithmetic_consistent | 242 | 300 | 80.67% |
| budget_consistent | 242 | 300 | 80.67% |
| budget_level_aligned | 219 | 300 | 73.00% |
| budget_preference_aligned | 219 | 300 | 73.00% |
| budget_relationship_ok | 256 | 300 | 85.33% |
| budget_selection_ok | 173 | 300 | 57.67% |
| budget_user_constraint_ok | 248 | 300 | 82.67% |
| budget_within_user_budget | 276 | 300 | 92.00% |
| city_ok | 300 | 300 | 100.00% |
| date_range_ok | 300 | 300 | 100.00% |
| day_dates_ok | 300 | 300 | 100.00% |
| day_index_ok | 300 | 300 | 100.00% |
| days_len_ok | 300 | 300 | 100.00% |
| dpo_soft_pass | 182 | 300 | 60.67% |
| dpo_soft_recomputed_budget_pass | 145 | 300 | 48.33% |
| hard_pass | 293 | 300 | 97.67% |
| hotel_budget_covers_nights | 284 | 300 | 94.67% |
| hotel_budget_relation_ok | 291 | 300 | 97.00% |
| hotel_distance_placeholder_ok | 300 | 300 | 100.00% |
| hotel_grounding_ok | 300 | 300 | 100.00% |
| invalid_hotel_name_ok | 300 | 300 | 100.00% |
| json_extract_ok | 300 | 300 | 100.00% |
| legacy_hard_pass | 210 | 300 | 70.00% |
| location_object_ok | 300 | 300 | 100.00% |
| meal_budget_consistent | 1 | 300 | 0.33% |
| meal_complete | 300 | 300 | 100.00% |
| meal_cost_scale_ok | 265 | 300 | 88.33% |
| meal_diversity_ok | 273 | 300 | 91.00% |
| meal_grounding_ok | 298 | 300 | 99.33% |
| meal_lunch_dinner_same_day_ok | 299 | 300 | 99.67% |
| meal_repeat_limit_ok | 273 | 300 | 91.00% |
| meal_specific_ok | 300 | 300 | 100.00% |
| meal_valid_semantics_ok | 298 | 300 | 99.33% |
| middle_hotel_ok | 300 | 300 | 100.00% |
| recomputed_budget_fit_ok | 173 | 300 | 57.67% |
| recomputed_budget_hard_ok | 225 | 300 | 75.00% |
| recomputed_budget_level_aligned | 173 | 300 | 57.67% |
| recomputed_budget_preference_aligned | 173 | 300 | 57.67% |
| recomputed_budget_user_constraint_ok | 225 | 300 | 75.00% |
| recomputed_budget_within_user_budget | 262 | 300 | 87.33% |
| schema_ok | 300 | 300 | 100.00% |
| sft_budget_semantic_hard_pass | 196 | 300 | 65.33% |
| sft_hard_pass | 293 | 300 | 97.67% |
| sft_no_budget_sum_hard_pass | 293 | 300 | 97.67% |
| sft_strict_hard_pass | 0 | 300 | 0.00% |
| transportation_budget_nonnegative | 300 | 300 | 100.00% |
| weather_dates_ok | 300 | 300 | 100.00% |
| weather_match | 300 | 300 | 100.00% |

## Numeric Metrics

```json
{
  "attraction_diversity_unique_rate": {
    "avg": 0.9916,
    "p50": 1.0,
    "p90": 1.0
  },
  "attraction_grounding_rate": {
    "avg": 0.9994,
    "p50": 1.0,
    "p90": 1.0
  },
  "hotel_grounding_rate": {
    "avg": 1.0,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_diversity_unique_rate": {
    "avg": 0.9083,
    "p50": 0.9333,
    "p90": 1.0
  },
  "meal_food_pois_grounding_rate": {
    "avg": 0.9995,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_grounding_rate": {
    "avg": 0.9995,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_semantic_valid_rate": {
    "avg": 0.9995,
    "p50": 1.0,
    "p90": 1.0
  },
  "recomputed_budget_per_person_day": {
    "avg": 916.1683,
    "p50": 928.78,
    "p90": 1434.33
  },
  "recomputed_budget_total": {
    "avg": 9789.9433,
    "p50": 8998.0,
    "p90": 17540.0
  }
}
```

## Failure Types

```json
{
  "meal_budget_inconsistent": 299,
  "attraction_budget_inconsistent": 218,
  "budget_preference_mismatch": 81,
  "budget_arithmetic_inconsistent": 58,
  "budget_hard_constraint_exceeded": 52,
  "budget_relationship_mismatch": 44,
  "meal_cost_scale_too_low": 35,
  "meal_repeat_too_many": 27,
  "attraction_repeat_too_many": 19,
  "hotel_budget_underestimated": 16,
  "too_many_attractions": 3,
  "meal_invalid_name": 2,
  "meal_same_day_lunch_dinner_repeat": 1
}
```

## Failure Examples

### v3_hard_realbudget_eval_000000
- request: 昆明 2026-04-07->2026-04-11 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 5, "hotel_room_count": 3, "attraction_ticket_sum": 959, "expected_total_attractions": 4795, "reported_total_attractions": 4695, "meal_per_person_cost_sum": 989, "expected_total_meals": 4945, "reported_total_meals": 4600, "reported_total_transportation": 1800}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 5, "hotel_room_count": 3, "attraction_ticket_sum": 959, "expected_total_attractions": 4795, "reported_total_attractions": 4695, "meal_per_person_cost_sum": 989, "expected_total_meals": 4945, "reported_total_meals": 4600, "reported_total_transportation": 1800}}]`

### v3_hard_realbudget_eval_000001
- request: 桂林 2026-09-04->2026-09-07 days=4 transport=打车 hotel=高端酒店 prefs=['高端酒店', '艺术', '特色餐厅', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 1314, "expected_total_attractions": 2628, "reported_total_attractions": 2628, "meal_per_person_cost_sum": 1071, "expected_total_meals": 2142, "reported_total_meals": 2504, "reported_total_transportation": 1000}}]`

### v3_hard_realbudget_eval_000003
- request: 西安 2025-05-07->2025-05-11 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 319, "expected_total_attractions": 638, "reported_total_attractions": 658, "meal_per_person_cost_sum": 836, "expected_total_meals": 1672, "reported_total_meals": 2046, "reported_total_transportation": 500}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 319, "expected_total_attractions": 638, "reported_total_attractions": 658, "meal_per_person_cost_sum": 836, "expected_total_meals": 1672, "reported_total_meals": 2046, "reported_total_transportation": 500}}]`

### v3_hard_realbudget_eval_000004
- request: 张家界 2026-05-11->2026-05-13 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 3498, "total": 3598, "diff": -100, "requested_budget": {"available": true, "amount": 3200, "scope": "total", "party_size": 1, "total": 3200, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "hard"}, "per_person_day": 1199.33, "budget_level": "comfortable", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "hard", "amount": 3200, "target_min_ratio": 0.7, "target_max_ratio": 1.0, "target_min_total": 2200, "target_max_total": 3200, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": false, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 1, "room_count": 1, "priced_nights": 2, "expected_min_total_hotels": 2600, "reported_total_hotels": 2600, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 160, "expected_total_attractions": 160, "reported_total_attractions": 160, "meal_per_person_cost_sum": 683, "expected_total_meals": 683, "reported_total_meals": 538, "reported_total_transportation": 200}}, {"stage": "rule", "type": "budget_hard_constraint_exceeded", "details": {"part_sum": 3498, "total": 3598, "diff": -100, "requested_budget": {"available": true, "amount": 3200, "scope": "total", "party_size": 1, "total": 3200, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "hard"}, "per_person_day": 1199.33, "budget_level": "comfortable", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "hard", "amount": 3200, "target_min_ratio": 0.7, "target_max_ratio": 1.0, "target_min_total": 2200, "target_max_total": 3200, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": false, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 1, "room_count": 1, "priced_nights": 2, "expected_min_total_hotels": 2600, "reported_total_hotels": 2600, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_hard_realbudget_eval_000005
- request: 广州 2026-07-06->2026-07-10 days=5 transport=公共交通 hotel=民宿 prefs=['摄影', '自然风光', '城市漫步', '本地菜']
- errors: `[{"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 186, "expected_total_attractions": 186, "reported_total_attractions": 186, "meal_per_person_cost_sum": 1157, "expected_total_meals": 1157, "reported_total_meals": 1119, "reported_total_transportation": 500}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": true, "meal_cost_scale_ok": false, "budget_relationship_ok": false, "expected_total_hotels": 1200, "reported_total_hotels": 1200, "expected_total_attractions": 186, "reported_total_attractions": 186, "meal_scale_eval": {"ok": false, "party_total": 1, "budget_level": "standard", "per_person_lunch_dinner_floor": 35, "breakfast_policy": "excluded_from_meal_cost_scale", "meal_count": 15, "checked_count": 10, "failure_count": 1, "failures": [{"date": "2026-07-08", "type": "lunch", "name": "银记肠粉(北京路店)", "estimated_cost": 23, "min_expected_cost": 35}]}}}, {"stage": "rule", "type": "meal_cost_scale_too_low", "details": {"ok": false, "party_total": 1, "budget_level": "standard", "per_person_lunch_dinner_floor": 35, "breakfast_policy": "excluded_from_meal_cost_scale", "meal_count": 15, "checked_count": 10, "failure_count": 1, "failures": [{"date": "2026-07-08", "type": "lunch", "name": "银记肠粉(北京路店)", "estimated_cost": 23, "min_expected_cost": 35}]}}]`

### v3_hard_realbudget_eval_000006
- request: 南京 2026-07-06->2026-07-09 days=4 transport=自驾 hotel=亲子酒店 prefs=['亲子', '动物园', '海洋馆', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 75, "expected_total_attractions": 225, "reported_total_attractions": 210, "meal_per_person_cost_sum": 859, "expected_total_meals": 2577, "reported_total_meals": 1800, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 75, "expected_total_attractions": 225, "reported_total_attractions": 210, "meal_per_person_cost_sum": 859, "expected_total_meals": 2577, "reported_total_meals": 1800, "reported_total_transportation": 200}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": true, "meal_cost_scale_ok": false, "budget_relationship_ok": false, "expected_total_hotels": 8100, "reported_total_hotels": 8100, "expected_total_attractions": 225, "reported_total_attractions": 210, "meal_scale_eval": {"ok": false, "party_total": 3, "budget_level": "standard", "per_person_lunch_dinner_floor": 35, "breakfast_policy": "excluded_from_meal_cost_scale", "meal_count": 12, "checked_count": 8, "failure_count": 1, "failures": [{"date": "2026-07-08", "type": "lunch", "name": "小潘记鸭血粉丝汤", "estimated_cost": 34, "min_expected_cost": 35}]}}}]`

### v3_hard_realbudget_eval_000007
- request: 成都 2026-05-11->2026-05-15 days=5 transport=公共交通 hotel=民宿 prefs=['小众展馆', '咖啡', '艺术', '城市漫步', '特色餐厅']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 1243, "expected_total_attractions": 2486, "reported_total_attractions": 2674, "meal_per_person_cost_sum": 2659, "expected_total_meals": 5318, "reported_total_meals": 5826, "reported_total_transportation": 1100}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 1243, "expected_total_attractions": 2486, "reported_total_attractions": 2674, "meal_per_person_cost_sum": 2659, "expected_total_meals": 5318, "reported_total_meals": 5826, "reported_total_transportation": 1100}}]`

### v3_hard_realbudget_eval_000008
- request: 大理 2026-05-11->2026-05-13 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 7795, "total": 7895, "diff": -100, "requested_budget": {"available": true, "amount": 8700, "scope": "total", "party_size": 3, "total": 8700, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "hard"}, "per_person_day": 877.22, "budget_level": "comfortable", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "hard", "amount": 8700, "target_min_ratio": 0.7, "target_max_ratio": 1.0, "target_min_total": 6100, "target_max_total": 8700, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 3, "room_count": 2, "priced_nights": 2, "expected_min_total_hotels": 5200, "reported_total_hotels": 5200, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 279, "expected_total_attractions": 837, "reported_total_attractions": 945, "meal_per_person_cost_sum": 769, "expected_total_meals": 2307, "reported_total_meals": 1350, "reported_total_transportation": 300}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 279, "expected_total_attractions": 837, "reported_total_attractions": 945, "meal_per_person_cost_sum": 769, "expected_total_meals": 2307, "reported_total_meals": 1350, "reported_total_transportation": 300}}]`

### v3_hard_realbudget_eval_000002
- request: 杭州 2026-05-01->2026-05-04 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '夜市', '老字号', '城市漫步']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 229, "expected_total_attractions": 916, "reported_total_attractions": 816, "meal_per_person_cost_sum": 641, "expected_total_meals": 2564, "reported_total_meals": 2088, "reported_total_transportation": 100}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 229, "expected_total_attractions": 916, "reported_total_attractions": 816, "meal_per_person_cost_sum": 641, "expected_total_meals": 2564, "reported_total_meals": 2088, "reported_total_transportation": 100}}]`

### v3_hard_realbudget_eval_000010
- request: 西安 2026-08-05->2026-08-09 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 4, "party_total": 5, "room_count": 3, "priced_nights": 4, "expected_min_total_hotels": 16200, "reported_total_hotels": 10800, "diff": -5400, "covers_nights": false}}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 22500, "total": 22400, "diff": 100, "requested_budget": {"available": true, "amount": 30900, "scope": "total", "party_size": 5, "total": 30900, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "hard"}, "per_person_day": 896.0, "budget_level": "comfortable", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "hard", "amount": 30900, "target_min_ratio": 0.7, "target_max_ratio": 1.0, "target_min_total": 21600, "target_max_total": 30900, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 4, "party_total": 5, "room_count": 3, "priced_nights": 4, "expected_min_total_hotels": 16200, "reported_total_hotels": 10800, "diff": -5400, "covers_nights": false}, "hotel_budget_covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 5, "hotel_room_count": 3, "attraction_ticket_sum": 914, "expected_total_attractions": 4570, "reported_total_attractions": 5855, "meal_per_person_cost_sum": 808, "expected_total_meals": 4040, "reported_total_meals": 4845, "reported_total_transportation": 1000}}]`

### v3_hard_realbudget_eval_000011
- request: 福州 2026-06-21->2026-06-24 days=4 transport=打车 hotel=高端酒店 prefs=['高端酒店', '艺术', '特色餐厅', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 14470, "total": 13470, "diff": 1000, "requested_budget": {"available": true, "amount": 13500, "scope": "total", "party_size": 2, "total": 13500, "source": "budget_constraint", "budget_level": "premium", "strictness": "soft"}, "per_person_day": 1683.75, "budget_level": "premium", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "premium", "strictness": "soft", "amount": 13500, "target_min_ratio": 0.75, "target_max_ratio": 1.12, "target_min_total": 10100, "target_max_total": 15100, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 2, "room_count": 1, "priced_nights": 3, "expected_min_total_hotels": 3900, "reported_total_hotels": 3900, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 548, "expected_total_attractions": 1096, "reported_total_attractions": 1378, "meal_per_person_cost_sum": 1485, "expected_total_meals": 2970, "reported_total_meals": 3692, "reported_total_transportation": 5500}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 548, "expected_total_attractions": 1096, "reported_total_attractions": 1378, "meal_per_person_cost_sum": 1485, "expected_total_meals": 2970, "reported_total_meals": 3692, "reported_total_transportation": 5500}}]`

### v3_hard_realbudget_eval_000009
- request: 苏州 2026-04-30->2026-05-03 days=4 transport=打车 hotel=亲子酒店 prefs=['亲子', '老人友好', '博物馆', '城市公园', '特色餐厅']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 320, "expected_total_attractions": 1280, "reported_total_attractions": 1440, "meal_per_person_cost_sum": 766, "expected_total_meals": 3064, "reported_total_meals": 4008, "reported_total_transportation": 1000}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 320, "expected_total_attractions": 1280, "reported_total_attractions": 1440, "meal_per_person_cost_sum": 766, "expected_total_meals": 3064, "reported_total_meals": 4008, "reported_total_transportation": 1000}}]`

### v3_hard_realbudget_eval_000012
- request: 洛阳 2025-05-07->2025-05-10 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '夜市', '老字号', '城市漫步']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 267, "expected_total_attractions": 1068, "reported_total_attractions": 908, "meal_per_person_cost_sum": 585, "expected_total_meals": 2340, "reported_total_meals": 2004, "reported_total_transportation": 500}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 267, "expected_total_attractions": 1068, "reported_total_attractions": 908, "meal_per_person_cost_sum": 585, "expected_total_meals": 2340, "reported_total_meals": 2004, "reported_total_transportation": 500}}]`

### v3_hard_realbudget_eval_000014
- request: 成都 2026-06-06->2026-06-08 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆']
- errors: `[{"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 130, "expected_total_attractions": 130, "reported_total_attractions": 130, "meal_per_person_cost_sum": 887, "expected_total_meals": 887, "reported_total_meals": 891, "reported_total_transportation": 300}}]`

### v3_hard_realbudget_eval_000013
- request: 武汉 2026-05-09->2026-05-13 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 163, "expected_total_attractions": 326, "reported_total_attractions": 286, "meal_per_person_cost_sum": 1004, "expected_total_meals": 2008, "reported_total_meals": 2200, "reported_total_transportation": 400}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 163, "expected_total_attractions": 326, "reported_total_attractions": 286, "meal_per_person_cost_sum": 1004, "expected_total_meals": 2008, "reported_total_meals": 2200, "reported_total_transportation": 400}}]`

### v3_hard_realbudget_eval_000016
- request: 苏州 2026-06-06->2026-06-09 days=4 transport=自驾 hotel=亲子酒店 prefs=['亲子', '动物园', '海洋馆', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 140, "expected_total_attractions": 420, "reported_total_attractions": 435, "meal_per_person_cost_sum": 581, "expected_total_meals": 1743, "reported_total_meals": 1650, "reported_total_transportation": 600}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 140, "expected_total_attractions": 420, "reported_total_attractions": 435, "meal_per_person_cost_sum": 581, "expected_total_meals": 1743, "reported_total_meals": 1650, "reported_total_transportation": 600}}, {"stage": "rule", "type": "budget_hard_constraint_exceeded", "details": {"part_sum": 10785, "total": 10785, "diff": 0, "requested_budget": {"available": true, "amount": 10000, "scope": "total", "party_size": 3, "total": 10000, "source": "budget_constraint", "budget_level": "standard", "strictness": "hard"}, "per_person_day": 898.75, "budget_level": "standard", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "standard", "strictness": "hard", "amount": 10000, "target_min_ratio": 0.6, "target_max_ratio": 1.0, "target_min_total": 6000, "target_max_total": 10000, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": true, "within_user_budget": true, "user_constraint_ok": false, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 3, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 8100, "reported_total_hotels": 8100, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_hard_realbudget_eval_000017
- request: 苏州 2026-05-09->2026-05-13 days=5 transport=公共交通 hotel=民宿 prefs=['小众展馆', '咖啡', '艺术', '城市漫步', '特色餐厅']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 320, "expected_total_attractions": 640, "reported_total_attractions": 750, "meal_per_person_cost_sum": 1123, "expected_total_meals": 2246, "reported_total_meals": 3400, "reported_total_transportation": 1800}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 320, "expected_total_attractions": 640, "reported_total_attractions": 750, "meal_per_person_cost_sum": 1123, "expected_total_meals": 2246, "reported_total_meals": 3400, "reported_total_transportation": 1800}}]`

### v3_hard_realbudget_eval_000018
- request: 天津 2026-07-06->2026-07-08 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 1001, "expected_total_attractions": 3003, "reported_total_attractions": 2859, "meal_per_person_cost_sum": 3341, "expected_total_meals": 10023, "reported_total_meals": 7245, "reported_total_transportation": 1200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 1001, "expected_total_attractions": 3003, "reported_total_attractions": 2859, "meal_per_person_cost_sum": 3341, "expected_total_meals": 10023, "reported_total_meals": 7245, "reported_total_transportation": 1200}}, {"stage": "rule", "type": "budget_hard_constraint_exceeded", "details": {"part_sum": 18504, "total": 18504, "diff": 0, "requested_budget": {"available": true, "amount": 7900, "scope": "total", "party_size": 3, "total": 7900, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "hard"}, "per_person_day": 2056.0, "budget_level": "comfortable", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "hard", "amount": 7900, "target_min_ratio": 0.7, "target_max_ratio": 1.0, "target_min_total": 5500, "target_max_total": 7900, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": true, "within_user_budget": false, "user_constraint_ok": false, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 3, "room_count": 2, "priced_nights": 2, "expected_min_total_hotels": 7200, "reported_total_hotels": 7200, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_hard_realbudget_eval_000019
- request: 丽江 2026-05-11->2026-05-14 days=4 transport=打车 hotel=亲子酒店 prefs=['亲子', '老人友好', '博物馆', '城市公园', '特色餐厅']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 500, "expected_total_attractions": 1000, "reported_total_attractions": 1040, "meal_per_person_cost_sum": 893, "expected_total_meals": 1786, "reported_total_meals": 1728, "reported_total_transportation": 800}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 500, "expected_total_attractions": 1000, "reported_total_attractions": 1040, "meal_per_person_cost_sum": 893, "expected_total_meals": 1786, "reported_total_meals": 1728, "reported_total_transportation": 800}}]`

### v3_hard_realbudget_eval_000020
- request: 杭州 2026-06-21->2026-06-25 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 5, "hotel_room_count": 3, "attraction_ticket_sum": 160, "expected_total_attractions": 800, "reported_total_attractions": 700, "meal_per_person_cost_sum": 1133, "expected_total_meals": 5665, "reported_total_meals": 5950, "reported_total_transportation": 1000}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 5, "hotel_room_count": 3, "attraction_ticket_sum": 160, "expected_total_attractions": 800, "reported_total_attractions": 700, "meal_per_person_cost_sum": 1133, "expected_total_meals": 5665, "reported_total_meals": 5950, "reported_total_transportation": 1000}}]`
