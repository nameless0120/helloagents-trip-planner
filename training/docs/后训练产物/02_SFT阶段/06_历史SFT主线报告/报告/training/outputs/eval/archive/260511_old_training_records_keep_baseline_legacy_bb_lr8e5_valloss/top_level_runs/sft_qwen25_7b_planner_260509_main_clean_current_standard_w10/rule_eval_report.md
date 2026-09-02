# Rule Eval Report: sft_qwen25_7b_v3_260509_main_clean_current_standard_w10

- records: 200
- generations: `training/outputs/eval/sft_qwen25_7b_v3_260509_main_clean_current_standard_w10/generations.jsonl`
- records_path: `training/data/v3/eval/records.jsonl`

## Boolean Metrics

| Metric | Pass | Total | Rate |
| --- | ---: | ---: | ---: |
| accommodation_type_ok | 200 | 200 | 100.00% |
| attraction_budget_consistent | 59 | 200 | 29.50% |
| attraction_budget_party_relation_ok | 187 | 200 | 93.50% |
| attraction_count_ok | 200 | 200 | 100.00% |
| attraction_diversity_ok | 185 | 200 | 92.50% |
| attraction_grounding_ok | 198 | 200 | 99.00% |
| attraction_repeat_limit_ok | 185 | 200 | 92.50% |
| budget_arithmetic_consistent | 156 | 200 | 78.00% |
| budget_consistent | 156 | 200 | 78.00% |
| budget_level_aligned | 136 | 200 | 68.00% |
| budget_preference_aligned | 136 | 200 | 68.00% |
| budget_relationship_ok | 140 | 200 | 70.00% |
| budget_selection_ok | 108 | 200 | 54.00% |
| budget_user_constraint_ok | 200 | 200 | 100.00% |
| budget_within_user_budget | 200 | 200 | 100.00% |
| city_ok | 200 | 200 | 100.00% |
| date_range_ok | 200 | 200 | 100.00% |
| day_dates_ok | 200 | 200 | 100.00% |
| day_index_ok | 200 | 200 | 100.00% |
| days_len_ok | 200 | 200 | 100.00% |
| dpo_soft_pass | 101 | 200 | 50.50% |
| dpo_soft_recomputed_budget_pass | 83 | 200 | 41.50% |
| hard_pass | 197 | 200 | 98.50% |
| hotel_budget_covers_nights | 196 | 200 | 98.00% |
| hotel_budget_relation_ok | 196 | 200 | 98.00% |
| hotel_distance_placeholder_ok | 200 | 200 | 100.00% |
| hotel_grounding_ok | 200 | 200 | 100.00% |
| invalid_hotel_name_ok | 200 | 200 | 100.00% |
| json_extract_ok | 200 | 200 | 100.00% |
| legacy_hard_pass | 129 | 200 | 64.50% |
| location_object_ok | 200 | 200 | 100.00% |
| meal_budget_consistent | 1 | 200 | 0.50% |
| meal_complete | 200 | 200 | 100.00% |
| meal_cost_scale_ok | 153 | 200 | 76.50% |
| meal_diversity_ok | 164 | 200 | 82.00% |
| meal_grounding_ok | 198 | 200 | 99.00% |
| meal_lunch_dinner_same_day_ok | 192 | 200 | 96.00% |
| meal_repeat_limit_ok | 169 | 200 | 84.50% |
| meal_specific_ok | 200 | 200 | 100.00% |
| meal_valid_semantics_ok | 198 | 200 | 99.00% |
| middle_hotel_ok | 200 | 200 | 100.00% |
| recomputed_budget_fit_ok | 108 | 200 | 54.00% |
| recomputed_budget_hard_ok | 199 | 200 | 99.50% |
| recomputed_budget_level_aligned | 108 | 200 | 54.00% |
| recomputed_budget_preference_aligned | 108 | 200 | 54.00% |
| recomputed_budget_user_constraint_ok | 199 | 200 | 99.50% |
| recomputed_budget_within_user_budget | 196 | 200 | 98.00% |
| schema_ok | 200 | 200 | 100.00% |
| sft_budget_semantic_hard_pass | 139 | 200 | 69.50% |
| sft_hard_pass | 197 | 200 | 98.50% |
| sft_no_budget_sum_hard_pass | 197 | 200 | 98.50% |
| sft_strict_hard_pass | 0 | 200 | 0.00% |
| transportation_budget_nonnegative | 200 | 200 | 100.00% |
| weather_dates_ok | 200 | 200 | 100.00% |
| weather_match | 200 | 200 | 100.00% |

## Numeric Metrics

```json
{
  "attraction_diversity_unique_rate": {
    "avg": 0.991,
    "p50": 1.0,
    "p90": 1.0
  },
  "attraction_grounding_rate": {
    "avg": 0.9989,
    "p50": 1.0,
    "p90": 1.0
  },
  "hotel_grounding_rate": {
    "avg": 1.0,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_diversity_unique_rate": {
    "avg": 0.8696,
    "p50": 0.9,
    "p90": 1.0
  },
  "meal_food_pois_grounding_rate": {
    "avg": 0.9993,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_grounding_rate": {
    "avg": 0.9993,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_semantic_valid_rate": {
    "avg": 0.9993,
    "p50": 1.0,
    "p90": 1.0
  },
  "recomputed_budget_per_person_day": {
    "avg": 608.9699,
    "p50": 498.67,
    "p90": 1027.75
  },
  "recomputed_budget_total": {
    "avg": 5734.24,
    "p50": 4678.0,
    "p90": 11582.0
  }
}
```

## Failure Types

```json
{
  "meal_budget_inconsistent": 200,
  "attraction_budget_inconsistent": 141,
  "budget_preference_mismatch": 64,
  "budget_relationship_mismatch": 60,
  "meal_cost_scale_too_low": 47,
  "budget_arithmetic_inconsistent": 44,
  "meal_repeat_too_many": 31,
  "attraction_repeat_too_many": 15,
  "meal_same_day_lunch_dinner_repeat": 8,
  "hotel_budget_underestimated": 4,
  "meal_invalid_name": 2
}
```

## Failure Examples

### v3_standard200_realbudget_eval_000000
- request: 昆明 2026-04-07->2026-04-09 days=3 transport=地铁+步行 hotel=高端酒店 prefs=['休闲慢游', '美食']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 5586, "total": 5686, "diff": -100, "requested_budget": {"available": true, "amount": 9800, "scope": "total", "party_size": 2, "total": 9800, "source": "budget_constraint", "budget_level": "premium", "strictness": "hard"}, "per_person_day": 947.67, "budget_level": "premium", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "premium", "strictness": "hard", "amount": 9800, "target_min_ratio": 0.75, "target_max_ratio": 1.0, "target_min_total": 7400, "target_max_total": 9800, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 2, "room_count": 1, "priced_nights": 2, "expected_min_total_hotels": 1500, "reported_total_hotels": 1500, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 606, "expected_total_attractions": 1212, "reported_total_attractions": 1206, "meal_per_person_cost_sum": 915, "expected_total_meals": 1830, "reported_total_meals": 2580, "reported_total_transportation": 300}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 606, "expected_total_attractions": 1212, "reported_total_attractions": 1206, "meal_per_person_cost_sum": 915, "expected_total_meals": 1830, "reported_total_meals": 2580, "reported_total_transportation": 300}}]`

### v3_standard200_realbudget_eval_000008
- request: 大理 2026-05-11->2026-05-13 days=3 transport=地铁+步行 hotel=舒适型酒店 prefs=['休闲慢游', '城市地标', '历史文化']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 1988, "total": 2088, "diff": -100, "requested_budget": {"available": true, "amount": 3700, "scope": "total", "party_size": 2, "total": 3700, "source": "budget_constraint", "budget_level": "standard", "strictness": "soft"}, "per_person_day": 348.0, "budget_level": "standard", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "standard", "strictness": "soft", "amount": 3700, "target_min_ratio": 0.6, "target_max_ratio": 1.05, "target_min_total": 2200, "target_max_total": 3900, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 2, "room_count": 1, "priced_nights": 2, "expected_min_total_hotels": 800, "reported_total_hotels": 800, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 75, "expected_total_attractions": 150, "reported_total_attractions": 150, "meal_per_person_cost_sum": 462, "expected_total_meals": 924, "reported_total_meals": 838, "reported_total_transportation": 200}}, {"stage": "rule", "type": "budget_preference_mismatch", "details": {"part_sum": 1988, "total": 2088, "diff": -100, "requested_budget": {"available": true, "amount": 3700, "scope": "total", "party_size": 2, "total": 3700, "source": "budget_constraint", "budget_level": "standard", "strictness": "soft"}, "per_person_day": 348.0, "budget_level": "standard", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "standard", "strictness": "soft", "amount": 3700, "target_min_ratio": 0.6, "target_max_ratio": 1.05, "target_min_total": 2200, "target_max_total": 3900, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 2, "room_count": 1, "priced_nights": 2, "expected_min_total_hotels": 800, "reported_total_hotels": 800, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_standard200_realbudget_eval_000001
- request: 桂林 2026-09-04->2026-09-06 days=3 transport=公共交通 hotel=高端酒店 prefs=['艺术', '美食', '第一次来', '历史文化']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 523, "expected_total_attractions": 1046, "reported_total_attractions": 968, "meal_per_person_cost_sum": 427, "expected_total_meals": 854, "reported_total_meals": 1006, "reported_total_transportation": 600}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 523, "expected_total_attractions": 1046, "reported_total_attractions": 968, "meal_per_person_cost_sum": 427, "expected_total_meals": 854, "reported_total_meals": 1006, "reported_total_transportation": 600}}, {"stage": "rule", "type": "budget_preference_mismatch", "details": {"part_sum": 4974, "total": 4974, "diff": 0, "requested_budget": {"available": true, "amount": 7100, "scope": "total", "party_size": 2, "total": 7100, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "soft"}, "per_person_day": 829.0, "budget_level": "comfortable", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "soft", "amount": 7100, "target_min_ratio": 0.7, "target_max_ratio": 1.1, "target_min_total": 5000, "target_max_total": 7800, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": true, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 2, "room_count": 1, "priced_nights": 2, "expected_min_total_hotels": 2400, "reported_total_hotels": 2400, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_standard200_realbudget_eval_000007
- request: 成都 2026-05-11->2026-05-13 days=3 transport=地铁+步行 hotel=舒适型酒店 prefs=['美食', '城市公园', '休闲慢游']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "山面包", "count": 3, "max_allowed": 2, "occurrences": [{"date": "2026-05-11", "type": "breakfast", "name": "山面包(东郊记忆店)"}, {"date": "2026-05-12", "type": "breakfast", "name": "山面包(望平街店)"}, {"date": "2026-05-13", "type": "breakfast", "name": "山面包(东郊记忆店)"}]}]}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 165, "expected_total_attractions": 330, "reported_total_attractions": 330, "meal_per_person_cost_sum": 682, "expected_total_meals": 1364, "reported_total_meals": 1070, "reported_total_transportation": 200}}]`

### v3_standard200_realbudget_eval_000005
- request: 广州 2026-07-06->2026-07-08 days=3 transport=地铁+步行 hotel=经济型酒店 prefs=['博物馆', '城市公园', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 100, "expected_total_attractions": 200, "reported_total_attractions": 200, "meal_per_person_cost_sum": 632, "expected_total_meals": 1264, "reported_total_meals": 1188, "reported_total_transportation": 120}}]`

### v3_standard200_realbudget_eval_000006
- request: 南京 2026-07-06->2026-07-09 days=4 transport=打车 hotel=经济型酒店 prefs=['老人友好', '美食', '城市公园', '休闲慢游']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "许阿姨糕团店", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-07-06", "type": "breakfast", "name": "许阿姨糕团店(南京总店)"}, {"date": "2026-07-07", "type": "breakfast", "name": "许阿姨糕团店(南京总店)"}, {"date": "2026-07-08", "type": "breakfast", "name": "许阿姨糕团店(南京总店)"}, {"date": "2026-07-09", "type": "breakfast", "name": "许阿姨糕团店(南京总店)"}]}]}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 4796, "total": 4896, "diff": -100, "requested_budget": {"available": true, "amount": 5600, "scope": "total", "party_size": 3, "total": 5600, "source": "budget_constraint", "budget_level": "limited", "strictness": "soft"}, "per_person_day": 408.0, "budget_level": "limited", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "limited", "strictness": "soft", "amount": 5600, "target_min_ratio": 0.72, "target_max_ratio": 1.05, "target_min_total": 4000, "target_max_total": 5900, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 3, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 1500, "reported_total_hotels": 1500, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 100, "expected_total_attractions": 300, "reported_total_attractions": 315, "meal_per_person_cost_sum": 764, "expected_total_meals": 2292, "reported_total_meals": 2181, "reported_total_transportation": 800}}]`

### v3_standard200_realbudget_eval_000010
- request: 西安 2026-08-05->2026-08-08 days=4 transport=公共交通 hotel=经济型酒店 prefs=['城市公园', '美食']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 3988, "total": 4088, "diff": -100, "requested_budget": {"available": true, "amount": 6600, "scope": "total", "party_size": 2, "total": 6600, "source": "budget_constraint", "budget_level": "standard", "strictness": "soft"}, "per_person_day": 511.0, "budget_level": "standard", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "standard", "strictness": "soft", "amount": 6600, "target_min_ratio": 0.6, "target_max_ratio": 1.05, "target_min_total": 4000, "target_max_total": 6900, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 2, "room_count": 1, "priced_nights": 3, "expected_min_total_hotels": 750, "reported_total_hotels": 750, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 387, "expected_total_attractions": 774, "reported_total_attractions": 726, "meal_per_person_cost_sum": 699, "expected_total_meals": 1398, "reported_total_meals": 1812, "reported_total_transportation": 700}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 387, "expected_total_attractions": 774, "reported_total_attractions": 726, "meal_per_person_cost_sum": 699, "expected_total_meals": 1398, "reported_total_meals": 1812, "reported_total_transportation": 700}}]`

### v3_standard200_realbudget_eval_000004
- request: 张家界 2026-05-11->2026-05-15 days=5 transport=地铁+步行 hotel=舒适型酒店 prefs=['亲子', '城市漫步', '历史文化']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "麦当劳", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-05-11", "type": "breakfast", "name": "麦当劳(天门中心广场店)"}, {"date": "2026-05-12", "type": "breakfast", "name": "麦当劳(天门中心广场店)"}, {"date": "2026-05-13", "type": "breakfast", "name": "麦当劳(天门中心广场店)"}, {"date": "2026-05-14", "type": "breakfast", "name": "麦当劳(天门中心广场店)"}, {"date": "2026-05-15", "type": "breakfast", "name": "麦当劳(天门中心广场店)"}]}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 301, "expected_total_attractions": 1204, "reported_total_attractions": 1444, "meal_per_person_cost_sum": 713, "expected_total_meals": 2852, "reported_total_meals": 2224, "reported_total_transportation": 400}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 301, "expected_total_attractions": 1204, "reported_total_attractions": 1444, "meal_per_person_cost_sum": 713, "expected_total_meals": 2852, "reported_total_meals": 2224, "reported_total_transportation": 400}}]`

### v3_standard200_realbudget_eval_000003
- request: 西安 2025-05-07->2025-05-11 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '历史文化', '购物商圈']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "西安博物院", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2025-05-09", "day_index": 2, "name": "西安博物院"}, {"date": "2025-05-11", "day_index": 4, "name": "西安博物院"}]}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 199, "expected_total_attractions": 597, "reported_total_attractions": 639, "meal_per_person_cost_sum": 754, "expected_total_meals": 2262, "reported_total_meals": 3661, "reported_total_transportation": 1500}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 199, "expected_total_attractions": 597, "reported_total_attractions": 639, "meal_per_person_cost_sum": 754, "expected_total_meals": 2262, "reported_total_meals": 3661, "reported_total_transportation": 1500}}]`

### v3_standard200_realbudget_eval_000002
- request: 杭州 2026-05-01->2026-05-05 days=5 transport=公共交通 hotel=经济型酒店 prefs=['美食', '休闲慢游', '户外轻徒步', '城市漫步']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 160, "expected_total_attractions": 160, "reported_total_attractions": 150, "meal_per_person_cost_sum": 1103, "expected_total_meals": 1103, "reported_total_meals": 1151, "reported_total_transportation": 100}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 160, "expected_total_attractions": 160, "reported_total_attractions": 150, "meal_per_person_cost_sum": 1103, "expected_total_meals": 1103, "reported_total_meals": 1151, "reported_total_transportation": 100}}]`

### v3_standard200_realbudget_eval_000014
- request: 成都 2026-06-06->2026-06-07 days=2 transport=打车 hotel=经济型酒店 prefs=['小众展览', '美食', '城市地标']
- errors: `[{"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 195, "expected_total_attractions": 780, "reported_total_attractions": 780, "meal_per_person_cost_sum": 566, "expected_total_meals": 2264, "reported_total_meals": 2004, "reported_total_transportation": 200}}]`

### v3_standard200_realbudget_eval_000013
- request: 武汉 2026-05-09->2026-05-11 days=3 transport=公共交通 hotel=舒适型酒店 prefs=['亲子', '老人友好', '第一次来', '城市公园']
- errors: `[{"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 6, "hotel_room_count": 3, "attraction_ticket_sum": 130, "expected_total_attractions": 780, "reported_total_attractions": 780, "meal_per_person_cost_sum": 537, "expected_total_meals": 3222, "reported_total_meals": 3846, "reported_total_transportation": 300}}, {"stage": "rule", "type": "budget_preference_mismatch", "details": {"part_sum": 7326, "total": 7326, "diff": 0, "requested_budget": {"available": true, "amount": 12400, "scope": "total", "party_size": 6, "total": 12400, "source": "budget_constraint", "budget_level": "standard", "strictness": "soft"}, "per_person_day": 407.0, "budget_level": "standard", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "standard", "strictness": "soft", "amount": 12400, "target_min_ratio": 0.6, "target_max_ratio": 1.05, "target_min_total": 7400, "target_max_total": 13000, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": true, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 6, "room_count": 3, "priced_nights": 2, "expected_min_total_hotels": 2400, "reported_total_hotels": 2400, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_standard200_realbudget_eval_000018
- request: 天津 2026-07-06->2026-07-07 days=2 transport=打车 hotel=舒适型酒店 prefs=['老人友好', '夜市夜景', '艺术', '第一次来']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 2101, "total": 1901, "diff": 200, "requested_budget": {"available": true, "amount": 2700, "scope": "total", "party_size": 3, "total": 2700, "source": "budget_constraint", "budget_level": "limited", "strictness": "hard"}, "per_person_day": 316.83, "budget_level": "limited", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "limited", "strictness": "hard", "amount": 2700, "target_min_ratio": 0.72, "target_max_ratio": 1.0, "target_min_total": 1900, "target_max_total": 2700, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 1, "party_total": 3, "room_count": 2, "priced_nights": 1, "expected_min_total_hotels": 800, "reported_total_hotels": 800, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 130, "expected_total_attractions": 390, "reported_total_attractions": 390, "meal_per_person_cost_sum": 369, "expected_total_meals": 1107, "reported_total_meals": 711, "reported_total_transportation": 200}}]`

### v3_standard200_realbudget_eval_000016
- request: 苏州 2026-06-06->2026-06-08 days=3 transport=公共交通 hotel=民宿 prefs=['海滨度假', '城市公园', '主题乐园', '清真']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-06-08", "lunch": "庆乐居[西北民族餐厅]", "dinner": "庆乐居[西北民族餐厅]"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "庆乐居[西北民族餐厅]", "count": 4, "max_allowed": 2, "occurrences": [{"date": "2026-06-06", "type": "lunch", "name": "庆乐居[西北民族餐厅]"}, {"date": "2026-06-07", "type": "dinner", "name": "庆乐居[西北民族餐厅]"}, {"date": "2026-06-08", "type": "lunch", "name": "庆乐居[西北民族餐厅]"}, {"date": "2026-06-08", "type": "dinner", "name": "庆乐居[西北民族餐厅]"}]}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 220, "expected_total_attractions": 440, "reported_total_attractions": 330, "meal_per_person_cost_sum": 258, "expected_total_meals": 516, "reported_total_meals": 402, "reported_total_transportation": 100}}]`

### v3_standard200_realbudget_eval_000011
- request: 福州 2026-06-21->2026-06-24 days=4 transport=打车 hotel=经济型酒店 prefs=['第一次来', '城市漫步']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 167, "expected_total_attractions": 334, "reported_total_attractions": 254, "meal_per_person_cost_sum": 748, "expected_total_meals": 1496, "reported_total_meals": 1602, "reported_total_transportation": 1000}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 167, "expected_total_attractions": 334, "reported_total_attractions": 254, "meal_per_person_cost_sum": 748, "expected_total_meals": 1496, "reported_total_meals": 1602, "reported_total_transportation": 1000}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": false, "meal_cost_scale_ok": false, "budget_relationship_ok": false, "expected_total_hotels": 600, "reported_total_hotels": 600, "expected_total_attractions": 334, "reported_total_attractions": 254, "meal_scale_eval": {"ok": false, "party_total": 2, "budget_level": "standard", "per_person_lunch_dinner_floor": 35, "breakfast_policy": "excluded_from_meal_cost_scale", "meal_count": 12, "checked_count": 8, "failure_count": 1, "failures": [{"date": "2026-06-21", "type": "lunch", "name": "后街捞化", "estimated_cost": 27, "min_expected_cost": 35}]}}}]`

### v3_standard200_realbudget_eval_000017
- request: 苏州 2026-05-09->2026-05-11 days=3 transport=地铁+步行 hotel=亲子酒店 prefs=['亲子', '历史文化', '休闲慢游', '户外轻徒步']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 850, "expected_total_attractions": 2550, "reported_total_attractions": 2385, "meal_per_person_cost_sum": 436, "expected_total_meals": 1308, "reported_total_meals": 1239, "reported_total_transportation": 300}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 850, "expected_total_attractions": 2550, "reported_total_attractions": 2385, "meal_per_person_cost_sum": 436, "expected_total_meals": 1308, "reported_total_meals": 1239, "reported_total_transportation": 300}}]`

### v3_standard200_realbudget_eval_000009
- request: 苏州 2026-04-30->2026-05-04 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['亲子', '城市地标', '第一次来', '城市漫步']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 320, "expected_total_attractions": 1280, "reported_total_attractions": 1530, "meal_per_person_cost_sum": 719, "expected_total_meals": 2876, "reported_total_meals": 2372, "reported_total_transportation": 400}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 320, "expected_total_attractions": 1280, "reported_total_attractions": 1530, "meal_per_person_cost_sum": 719, "expected_total_meals": 2876, "reported_total_meals": 2372, "reported_total_transportation": 400}}]`

### v3_standard200_realbudget_eval_000021
- request: 上海 2026-06-21->2026-06-22 days=2 transport=地铁+步行 hotel=经济型酒店 prefs=['老人友好', '休闲慢游', '城市漫步', '主题乐园']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-06-21", "lunch": "外滩家宴·上海菜(外滩·南京路店)", "dinner": "外滩家宴·上海菜(外滩豫园店)"}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 80, "expected_total_attractions": 160, "reported_total_attractions": 140, "meal_per_person_cost_sum": 492, "expected_total_meals": 984, "reported_total_meals": 834, "reported_total_transportation": 100}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 80, "expected_total_attractions": 160, "reported_total_attractions": 140, "meal_per_person_cost_sum": 492, "expected_total_meals": 984, "reported_total_meals": 834, "reported_total_transportation": 100}}]`

### v3_standard200_realbudget_eval_000012
- request: 洛阳 2025-05-07->2025-05-10 days=4 transport=打车 hotel=高端酒店 prefs=['休闲慢游', '第一次来']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 621, "expected_total_attractions": 1863, "reported_total_attractions": 1893, "meal_per_person_cost_sum": 632, "expected_total_meals": 1896, "reported_total_meals": 4209, "reported_total_transportation": 9800}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 621, "expected_total_attractions": 1863, "reported_total_attractions": 1893, "meal_per_person_cost_sum": 632, "expected_total_meals": 1896, "reported_total_meals": 4209, "reported_total_transportation": 9800}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": true, "meal_cost_scale_ok": false, "budget_relationship_ok": false, "expected_total_hotels": 4500, "reported_total_hotels": 4500, "expected_total_attractions": 1863, "reported_total_attractions": 1893, "meal_scale_eval": {"ok": false, "party_total": 3, "budget_level": "premium", "per_person_lunch_dinner_floor": 70, "breakfast_policy": "excluded_from_meal_cost_scale", "meal_count": 12, "checked_count": 8, "failure_count": 2, "failures": [{"date": "2025-05-08", "type": "lunch", "name": "武哥跑马汤(龙门高铁站店)", "estimated_cost": 67, "min_expected_cost": 70}, {"date": "2025-05-10", "type": "dinner", "name": "洛阳十字街小吃一条街", "estimated_cost": 27, "min_expected_cost": 70}]}}}]`

### v3_standard200_realbudget_eval_000015
- request: 南京 2026-04-07->2026-04-08 days=2 transport=地铁+步行 hotel=经济型酒店 prefs=['亲子', '休闲慢游', '历史文化']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 75, "expected_total_attractions": 225, "reported_total_attractions": 210, "meal_per_person_cost_sum": 351, "expected_total_meals": 1053, "reported_total_meals": 1038, "reported_total_transportation": 100}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 75, "expected_total_attractions": 225, "reported_total_attractions": 210, "meal_per_person_cost_sum": 351, "expected_total_meals": 1053, "reported_total_meals": 1038, "reported_total_transportation": 100}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": true, "meal_cost_scale_ok": false, "budget_relationship_ok": false, "expected_total_hotels": 500, "reported_total_hotels": 500, "expected_total_attractions": 225, "reported_total_attractions": 210, "meal_scale_eval": {"ok": false, "party_total": 3, "budget_level": "standard", "per_person_lunch_dinner_floor": 35, "breakfast_policy": "excluded_from_meal_cost_scale", "meal_count": 6, "checked_count": 4, "failure_count": 1, "failures": [{"date": "2026-04-08", "type": "lunch", "name": "小潘记鸭血粉丝汤", "estimated_cost": 34, "min_expected_cost": 35}]}}}]`
