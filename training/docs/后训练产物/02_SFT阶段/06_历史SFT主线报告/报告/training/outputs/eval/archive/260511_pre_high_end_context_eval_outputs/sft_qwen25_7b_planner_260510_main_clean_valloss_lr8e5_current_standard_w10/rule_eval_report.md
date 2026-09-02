# Rule Eval Report: sft_qwen25_7b_v3_260510_main_clean_valloss_lr8e5_current_standard_w10

- records: 200
- generations: `training/outputs/eval/sft_qwen25_7b_v3_260510_main_clean_valloss_lr8e5_current_standard_w10/generations.jsonl`
- records_path: `training/data/v3/eval/records.jsonl`

## Boolean Metrics

| Metric | Pass | Total | Rate |
| --- | ---: | ---: | ---: |
| accommodation_type_ok | 200 | 200 | 100.00% |
| attraction_budget_consistent | 57 | 200 | 28.50% |
| attraction_budget_party_relation_ok | 196 | 200 | 98.00% |
| attraction_count_ok | 200 | 200 | 100.00% |
| attraction_diversity_ok | 189 | 200 | 94.50% |
| attraction_grounding_ok | 199 | 200 | 99.50% |
| attraction_repeat_limit_ok | 189 | 200 | 94.50% |
| budget_arithmetic_consistent | 147 | 200 | 73.50% |
| budget_consistent | 147 | 200 | 73.50% |
| budget_level_aligned | 132 | 200 | 66.00% |
| budget_preference_aligned | 132 | 200 | 66.00% |
| budget_relationship_ok | 143 | 200 | 71.50% |
| budget_selection_ok | 109 | 200 | 54.50% |
| budget_user_constraint_ok | 200 | 200 | 100.00% |
| budget_within_user_budget | 200 | 200 | 100.00% |
| city_ok | 200 | 200 | 100.00% |
| date_range_ok | 200 | 200 | 100.00% |
| day_dates_ok | 200 | 200 | 100.00% |
| day_index_ok | 200 | 200 | 100.00% |
| days_len_ok | 200 | 200 | 100.00% |
| dpo_soft_pass | 106 | 200 | 53.00% |
| dpo_soft_recomputed_budget_pass | 88 | 200 | 44.00% |
| hard_pass | 197 | 200 | 98.50% |
| hotel_budget_covers_nights | 194 | 200 | 97.00% |
| hotel_budget_relation_ok | 194 | 200 | 97.00% |
| hotel_distance_placeholder_ok | 200 | 200 | 100.00% |
| hotel_grounding_ok | 200 | 200 | 100.00% |
| invalid_hotel_name_ok | 200 | 200 | 100.00% |
| json_extract_ok | 200 | 200 | 100.00% |
| legacy_hard_pass | 117 | 200 | 58.50% |
| location_object_ok | 200 | 200 | 100.00% |
| meal_budget_consistent | 1 | 200 | 0.50% |
| meal_complete | 200 | 200 | 100.00% |
| meal_cost_scale_ok | 150 | 200 | 75.00% |
| meal_diversity_ok | 168 | 200 | 84.00% |
| meal_grounding_ok | 198 | 200 | 99.00% |
| meal_lunch_dinner_same_day_ok | 193 | 200 | 96.50% |
| meal_repeat_limit_ok | 172 | 200 | 86.00% |
| meal_specific_ok | 200 | 200 | 100.00% |
| meal_valid_semantics_ok | 198 | 200 | 99.00% |
| middle_hotel_ok | 200 | 200 | 100.00% |
| recomputed_budget_fit_ok | 109 | 200 | 54.50% |
| recomputed_budget_hard_ok | 200 | 200 | 100.00% |
| recomputed_budget_level_aligned | 109 | 200 | 54.50% |
| recomputed_budget_preference_aligned | 109 | 200 | 54.50% |
| recomputed_budget_user_constraint_ok | 200 | 200 | 100.00% |
| recomputed_budget_within_user_budget | 198 | 200 | 99.00% |
| schema_ok | 200 | 200 | 100.00% |
| sft_budget_semantic_hard_pass | 142 | 200 | 71.00% |
| sft_hard_pass | 197 | 200 | 98.50% |
| sft_no_budget_sum_hard_pass | 197 | 200 | 98.50% |
| sft_strict_hard_pass | 1 | 200 | 0.50% |
| transportation_budget_nonnegative | 200 | 200 | 100.00% |
| weather_dates_ok | 200 | 200 | 100.00% |
| weather_match | 200 | 200 | 100.00% |

## Numeric Metrics

```json
{
  "attraction_diversity_unique_rate": {
    "avg": 0.9928,
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
    "avg": 0.8743,
    "p50": 0.9,
    "p90": 1.0
  },
  "meal_food_pois_grounding_rate": {
    "avg": 0.9982,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_grounding_rate": {
    "avg": 0.9982,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_semantic_valid_rate": {
    "avg": 0.9982,
    "p50": 1.0,
    "p90": 1.0
  },
  "recomputed_budget_per_person_day": {
    "avg": 616.7366,
    "p50": 508.25,
    "p90": 1054.75
  },
  "recomputed_budget_total": {
    "avg": 5845.46,
    "p50": 4708.0,
    "p90": 11398.0
  }
}
```

## Failure Types

```json
{
  "meal_budget_inconsistent": 200,
  "attraction_budget_inconsistent": 143,
  "budget_preference_mismatch": 68,
  "budget_relationship_mismatch": 57,
  "budget_arithmetic_inconsistent": 53,
  "meal_cost_scale_too_low": 50,
  "meal_repeat_too_many": 28,
  "attraction_repeat_too_many": 11,
  "meal_same_day_lunch_dinner_repeat": 7,
  "hotel_budget_underestimated": 6,
  "meal_invalid_name": 2
}
```

## Failure Examples

### v3_standard200_realbudget_eval_000000
- request: 昆明 2026-04-07->2026-04-09 days=3 transport=地铁+步行 hotel=高端酒店 prefs=['休闲慢游', '美食']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 4860, "total": 5060, "diff": -200, "requested_budget": {"available": true, "amount": 9800, "scope": "total", "party_size": 2, "total": 9800, "source": "budget_constraint", "budget_level": "premium", "strictness": "hard"}, "per_person_day": 843.33, "budget_level": "premium", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "premium", "strictness": "hard", "amount": 9800, "target_min_ratio": 0.75, "target_max_ratio": 1.0, "target_min_total": 7400, "target_max_total": 9800, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 2, "room_count": 1, "priced_nights": 2, "expected_min_total_hotels": 1500, "reported_total_hotels": 1500, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 323, "expected_total_attractions": 646, "reported_total_attractions": 706, "meal_per_person_cost_sum": 916, "expected_total_meals": 1832, "reported_total_meals": 2454, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 323, "expected_total_attractions": 646, "reported_total_attractions": 706, "meal_per_person_cost_sum": 916, "expected_total_meals": 1832, "reported_total_meals": 2454, "reported_total_transportation": 200}}]`

### v3_standard200_realbudget_eval_000008
- request: 大理 2026-05-11->2026-05-13 days=3 transport=地铁+步行 hotel=舒适型酒店 prefs=['休闲慢游', '城市地标', '历史文化']
- errors: `[{"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 75, "expected_total_attractions": 150, "reported_total_attractions": 150, "meal_per_person_cost_sum": 444, "expected_total_meals": 888, "reported_total_meals": 718, "reported_total_transportation": 200}}, {"stage": "rule", "type": "budget_preference_mismatch", "details": {"part_sum": 1868, "total": 1868, "diff": 0, "requested_budget": {"available": true, "amount": 3700, "scope": "total", "party_size": 2, "total": 3700, "source": "budget_constraint", "budget_level": "standard", "strictness": "soft"}, "per_person_day": 311.33, "budget_level": "standard", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "standard", "strictness": "soft", "amount": 3700, "target_min_ratio": 0.6, "target_max_ratio": 1.05, "target_min_total": 2200, "target_max_total": 3900, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": true, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 2, "room_count": 1, "priced_nights": 2, "expected_min_total_hotels": 800, "reported_total_hotels": 800, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_standard200_realbudget_eval_000007
- request: 成都 2026-05-11->2026-05-13 days=3 transport=地铁+步行 hotel=舒适型酒店 prefs=['美食', '城市公园', '休闲慢游']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "山面包", "count": 3, "max_allowed": 2, "occurrences": [{"date": "2026-05-11", "type": "breakfast", "name": "山面包(望平街店)"}, {"date": "2026-05-12", "type": "breakfast", "name": "山面包(东郊记忆店)"}, {"date": "2026-05-13", "type": "breakfast", "name": "山面包(望平街店)"}]}]}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 165, "expected_total_attractions": 330, "reported_total_attractions": 330, "meal_per_person_cost_sum": 692, "expected_total_meals": 1384, "reported_total_meals": 740, "reported_total_transportation": 100}}]`

### v3_standard200_realbudget_eval_000001
- request: 桂林 2026-09-04->2026-09-06 days=3 transport=公共交通 hotel=高端酒店 prefs=['艺术', '美食', '第一次来', '历史文化']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 345, "expected_total_attractions": 690, "reported_total_attractions": 670, "meal_per_person_cost_sum": 415, "expected_total_meals": 830, "reported_total_meals": 1032, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 345, "expected_total_attractions": 690, "reported_total_attractions": 670, "meal_per_person_cost_sum": 415, "expected_total_meals": 830, "reported_total_meals": 1032, "reported_total_transportation": 200}}, {"stage": "rule", "type": "budget_preference_mismatch", "details": {"part_sum": 4302, "total": 4302, "diff": 0, "requested_budget": {"available": true, "amount": 7100, "scope": "total", "party_size": 2, "total": 7100, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "soft"}, "per_person_day": 717.0, "budget_level": "comfortable", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "soft", "amount": 7100, "target_min_ratio": 0.7, "target_max_ratio": 1.1, "target_min_total": 5000, "target_max_total": 7800, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": true, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 2, "room_count": 1, "priced_nights": 2, "expected_min_total_hotels": 2400, "reported_total_hotels": 2400, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_standard200_realbudget_eval_000005
- request: 广州 2026-07-06->2026-07-08 days=3 transport=地铁+步行 hotel=经济型酒店 prefs=['博物馆', '城市公园', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 20, "expected_total_attractions": 40, "reported_total_attractions": 40, "meal_per_person_cost_sum": 552, "expected_total_meals": 1104, "reported_total_meals": 1014, "reported_total_transportation": 200}}, {"stage": "rule", "type": "budget_preference_mismatch", "details": {"part_sum": 1754, "total": 1754, "diff": 0, "requested_budget": {"available": true, "amount": 2800, "scope": "total", "party_size": 2, "total": 2800, "source": "budget_constraint", "budget_level": "limited", "strictness": "soft"}, "per_person_day": 292.33, "budget_level": "limited", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "limited", "strictness": "soft", "amount": 2800, "target_min_ratio": 0.72, "target_max_ratio": 1.05, "target_min_total": 2000, "target_max_total": 2900, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": true, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 2, "room_count": 1, "priced_nights": 2, "expected_min_total_hotels": 500, "reported_total_hotels": 500, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_standard200_realbudget_eval_000006
- request: 南京 2026-07-06->2026-07-09 days=4 transport=打车 hotel=经济型酒店 prefs=['老人友好', '美食', '城市公园', '休闲慢游']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "许阿姨糕团店", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-07-06", "type": "breakfast", "name": "许阿姨糕团店(南京总店)"}, {"date": "2026-07-07", "type": "breakfast", "name": "许阿姨糕团店(南京总店)"}, {"date": "2026-07-08", "type": "breakfast", "name": "许阿姨糕团店(南京总店)"}, {"date": "2026-07-09", "type": "breakfast", "name": "许阿姨糕团店(南京总店)"}]}]}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 3999, "total": 4000, "diff": -1, "requested_budget": {"available": true, "amount": 5600, "scope": "total", "party_size": 3, "total": 5600, "source": "budget_constraint", "budget_level": "limited", "strictness": "soft"}, "per_person_day": 333.33, "budget_level": "limited", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "limited", "strictness": "soft", "amount": 5600, "target_min_ratio": 0.72, "target_max_ratio": 1.05, "target_min_total": 4000, "target_max_total": 5900, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 3, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 1500, "reported_total_hotels": 1500, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 100, "expected_total_attractions": 300, "reported_total_attractions": 320, "meal_per_person_cost_sum": 738, "expected_total_meals": 2214, "reported_total_meals": 1929, "reported_total_transportation": 250}}]`

### v3_standard200_realbudget_eval_000010
- request: 西安 2026-08-05->2026-08-08 days=4 transport=公共交通 hotel=经济型酒店 prefs=['城市公园', '美食']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 3996, "total": 4096, "diff": -100, "requested_budget": {"available": true, "amount": 6600, "scope": "total", "party_size": 2, "total": 6600, "source": "budget_constraint", "budget_level": "standard", "strictness": "soft"}, "per_person_day": 512.0, "budget_level": "standard", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "standard", "strictness": "soft", "amount": 6600, "target_min_ratio": 0.6, "target_max_ratio": 1.05, "target_min_total": 4000, "target_max_total": 6900, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 2, "room_count": 1, "priced_nights": 3, "expected_min_total_hotels": 750, "reported_total_hotels": 750, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 319, "expected_total_attractions": 638, "reported_total_attractions": 608, "meal_per_person_cost_sum": 688, "expected_total_meals": 1376, "reported_total_meals": 1638, "reported_total_transportation": 1000}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 319, "expected_total_attractions": 638, "reported_total_attractions": 608, "meal_per_person_cost_sum": 688, "expected_total_meals": 1376, "reported_total_meals": 1638, "reported_total_transportation": 1000}}]`

### v3_standard200_realbudget_eval_000004
- request: 张家界 2026-05-11->2026-05-15 days=5 transport=地铁+步行 hotel=舒适型酒店 prefs=['亲子', '城市漫步', '历史文化']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 221, "expected_total_attractions": 884, "reported_total_attractions": 844, "meal_per_person_cost_sum": 603, "expected_total_meals": 2412, "reported_total_meals": 2356, "reported_total_transportation": 1500}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 221, "expected_total_attractions": 884, "reported_total_attractions": 844, "meal_per_person_cost_sum": 603, "expected_total_meals": 2412, "reported_total_meals": 2356, "reported_total_transportation": 1500}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": true, "meal_cost_scale_ok": false, "budget_relationship_ok": false, "expected_total_hotels": 3200, "reported_total_hotels": 3200, "expected_total_attractions": 884, "reported_total_attractions": 844, "meal_scale_eval": {"ok": false, "party_total": 4, "budget_level": "standard", "per_person_lunch_dinner_floor": 35, "breakfast_policy": "excluded_from_meal_cost_scale", "meal_count": 15, "checked_count": 10, "failure_count": 1, "failures": [{"date": "2026-05-15", "type": "dinner", "name": "肯德基(张家界回龙路店)", "estimated_cost": 26, "min_expected_cost": 35}]}}}]`

### v3_standard200_realbudget_eval_000002
- request: 杭州 2026-05-01->2026-05-05 days=5 transport=公共交通 hotel=经济型酒店 prefs=['美食', '休闲慢游', '户外轻徒步', '城市漫步']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 160, "expected_total_attractions": 160, "reported_total_attractions": 150, "meal_per_person_cost_sum": 934, "expected_total_meals": 934, "reported_total_meals": 750, "reported_total_transportation": 500}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 160, "expected_total_attractions": 160, "reported_total_attractions": 150, "meal_per_person_cost_sum": 934, "expected_total_meals": 934, "reported_total_meals": 750, "reported_total_transportation": 500}}]`

### v3_standard200_realbudget_eval_000003
- request: 西安 2025-05-07->2025-05-11 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '历史文化', '购物商圈']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "西安博物院", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2025-05-10", "day_index": 3, "name": "西安博物院"}, {"date": "2025-05-11", "day_index": 4, "name": "西安博物院"}]}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 199, "expected_total_attractions": 597, "reported_total_attractions": 675, "meal_per_person_cost_sum": 740, "expected_total_meals": 2220, "reported_total_meals": 3249, "reported_total_transportation": 1900}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 199, "expected_total_attractions": 597, "reported_total_attractions": 675, "meal_per_person_cost_sum": 740, "expected_total_meals": 2220, "reported_total_meals": 3249, "reported_total_transportation": 1900}}]`

### v3_standard200_realbudget_eval_000014
- request: 成都 2026-06-06->2026-06-07 days=2 transport=打车 hotel=经济型酒店 prefs=['小众展览', '美食', '城市地标']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 2960, "total": 3060, "diff": -100, "requested_budget": {"available": true, "amount": 4100, "scope": "total", "party_size": 4, "total": 4100, "source": "budget_constraint", "budget_level": "limited", "strictness": "soft"}, "per_person_day": 382.5, "budget_level": "limited", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "limited", "strictness": "soft", "amount": 4100, "target_min_ratio": 0.72, "target_max_ratio": 1.05, "target_min_total": 3000, "target_max_total": 4300, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 1, "party_total": 4, "room_count": 2, "priced_nights": 1, "expected_min_total_hotels": 500, "reported_total_hotels": 500, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 115, "expected_total_attractions": 460, "reported_total_attractions": 540, "meal_per_person_cost_sum": 433, "expected_total_meals": 1732, "reported_total_meals": 1620, "reported_total_transportation": 300}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 115, "expected_total_attractions": 460, "reported_total_attractions": 540, "meal_per_person_cost_sum": 433, "expected_total_meals": 1732, "reported_total_meals": 1620, "reported_total_transportation": 300}}]`

### v3_standard200_realbudget_eval_000013
- request: 武汉 2026-05-09->2026-05-11 days=3 transport=公共交通 hotel=舒适型酒店 prefs=['亲子', '老人友好', '第一次来', '城市公园']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 6922, "total": 7122, "diff": -200, "requested_budget": {"available": true, "amount": 12400, "scope": "total", "party_size": 6, "total": 12400, "source": "budget_constraint", "budget_level": "standard", "strictness": "soft"}, "per_person_day": 395.67, "budget_level": "standard", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "standard", "strictness": "soft", "amount": 12400, "target_min_ratio": 0.6, "target_max_ratio": 1.05, "target_min_total": 7400, "target_max_total": 13000, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 6, "room_count": 3, "priced_nights": 2, "expected_min_total_hotels": 2400, "reported_total_hotels": 2400, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 6, "hotel_room_count": 3, "attraction_ticket_sum": 130, "expected_total_attractions": 780, "reported_total_attractions": 840, "meal_per_person_cost_sum": 457, "expected_total_meals": 2742, "reported_total_meals": 3282, "reported_total_transportation": 400}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 6, "hotel_room_count": 3, "attraction_ticket_sum": 130, "expected_total_attractions": 780, "reported_total_attractions": 840, "meal_per_person_cost_sum": 457, "expected_total_meals": 2742, "reported_total_meals": 3282, "reported_total_transportation": 400}}]`

### v3_standard200_realbudget_eval_000018
- request: 天津 2026-07-06->2026-07-07 days=2 transport=打车 hotel=舒适型酒店 prefs=['老人友好', '夜市夜景', '艺术', '第一次来']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "天津意大利风情旅游区", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-07-06", "day_index": 0, "name": "天津意大利风情旅游区"}, {"date": "2026-07-07", "day_index": 1, "name": "天津意大利风情旅游区"}]}]}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 2001, "total": 1901, "diff": 100, "requested_budget": {"available": true, "amount": 2700, "scope": "total", "party_size": 3, "total": 2700, "source": "budget_constraint", "budget_level": "limited", "strictness": "hard"}, "per_person_day": 316.83, "budget_level": "limited", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "limited", "strictness": "hard", "amount": 2700, "target_min_ratio": 0.72, "target_max_ratio": 1.0, "target_min_total": 1900, "target_max_total": 2700, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 1, "party_total": 3, "room_count": 2, "priced_nights": 1, "expected_min_total_hotels": 800, "reported_total_hotels": 800, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 130, "expected_total_attractions": 390, "reported_total_attractions": 390, "meal_per_person_cost_sum": 383, "expected_total_meals": 1149, "reported_total_meals": 711, "reported_total_transportation": 100}}]`

### v3_standard200_realbudget_eval_000016
- request: 苏州 2026-06-06->2026-06-08 days=3 transport=公共交通 hotel=民宿 prefs=['海滨度假', '城市公园', '主题乐园', '清真']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-06-06", "lunch": "庆乐居[西北民族餐厅]", "dinner": "庆乐居[西北民族餐厅]"}, {"date": "2026-06-07", "lunch": "庆乐居[西北民族餐厅]", "dinner": "庆乐居[西北民族餐厅]"}, {"date": "2026-06-08", "lunch": "庆乐居[西北民族餐厅]", "dinner": "庆乐居[西北民族餐厅]"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "庆乐居[西北民族餐厅]", "count": 6, "max_allowed": 2, "occurrences": [{"date": "2026-06-06", "type": "lunch", "name": "庆乐居[西北民族餐厅]"}, {"date": "2026-06-06", "type": "dinner", "name": "庆乐居[西北民族餐厅]"}, {"date": "2026-06-07", "type": "lunch", "name": "庆乐居[西北民族餐厅]"}, {"date": "2026-06-07", "type": "dinner", "name": "庆乐居[西北民族餐厅]"}, {"date": "2026-06-08", "type": "lunch", "name": "庆乐居[西北民族餐厅]"}, {"date": "2026-06-08", "type": "dinner", "name": "庆乐居[西北民族餐厅]"}]}]}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 135, "expected_total_attractions": 270, "reported_total_attractions": 270, "meal_per_person_cost_sum": 186, "expected_total_meals": 372, "reported_total_meals": 242, "reported_total_transportation": 200}}]`

### v3_standard200_realbudget_eval_000011
- request: 福州 2026-06-21->2026-06-24 days=4 transport=打车 hotel=经济型酒店 prefs=['第一次来', '城市漫步']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 167, "expected_total_attractions": 334, "reported_total_attractions": 314, "meal_per_person_cost_sum": 831, "expected_total_meals": 1662, "reported_total_meals": 1700, "reported_total_transportation": 1000}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 167, "expected_total_attractions": 334, "reported_total_attractions": 314, "meal_per_person_cost_sum": 831, "expected_total_meals": 1662, "reported_total_meals": 1700, "reported_total_transportation": 1000}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": true, "meal_cost_scale_ok": false, "budget_relationship_ok": false, "expected_total_hotels": 600, "reported_total_hotels": 600, "expected_total_attractions": 334, "reported_total_attractions": 314, "meal_scale_eval": {"ok": false, "party_total": 2, "budget_level": "standard", "per_person_lunch_dinner_floor": 35, "breakfast_policy": "excluded_from_meal_cost_scale", "meal_count": 12, "checked_count": 8, "failure_count": 1, "failures": [{"date": "2026-06-21", "type": "lunch", "name": "后街捞化", "estimated_cost": 27, "min_expected_cost": 35}]}}}]`

### v3_standard200_realbudget_eval_000012
- request: 洛阳 2025-05-07->2025-05-10 days=4 transport=打车 hotel=高端酒店 prefs=['休闲慢游', '第一次来']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 780, "expected_total_attractions": 2340, "reported_total_attractions": 2160, "meal_per_person_cost_sum": 679, "expected_total_meals": 2037, "reported_total_meals": 3429, "reported_total_transportation": 7200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 780, "expected_total_attractions": 2340, "reported_total_attractions": 2160, "meal_per_person_cost_sum": 679, "expected_total_meals": 2037, "reported_total_meals": 3429, "reported_total_transportation": 7200}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": true, "meal_cost_scale_ok": false, "budget_relationship_ok": false, "expected_total_hotels": 4500, "reported_total_hotels": 4500, "expected_total_attractions": 2340, "reported_total_attractions": 2160, "meal_scale_eval": {"ok": false, "party_total": 3, "budget_level": "premium", "per_person_lunch_dinner_floor": 70, "breakfast_policy": "excluded_from_meal_cost_scale", "meal_count": 12, "checked_count": 8, "failure_count": 2, "failures": [{"date": "2025-05-08", "type": "lunch", "name": "武哥跑马汤(龙门高铁站店)", "estimated_cost": 67, "min_expected_cost": 70}, {"date": "2025-05-08", "type": "dinner", "name": "宴愉餐茶艺术餐厅", "estimated_cost": 67, "min_expected_cost": 70}]}}}]`

### v3_standard200_realbudget_eval_000017
- request: 苏州 2026-05-09->2026-05-11 days=3 transport=地铁+步行 hotel=亲子酒店 prefs=['亲子', '历史文化', '休闲慢游', '户外轻徒步']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 7763, "total": 8763, "diff": -1000, "requested_budget": {"available": true, "amount": 10000, "scope": "total", "party_size": 3, "total": 10000, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "soft"}, "per_person_day": 973.67, "budget_level": "comfortable", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "soft", "amount": 10000, "target_min_ratio": 0.7, "target_max_ratio": 1.1, "target_min_total": 7000, "target_max_total": 11000, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 3, "room_count": 2, "priced_nights": 2, "expected_min_total_hotels": 5000, "reported_total_hotels": 5000, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 320, "expected_total_attractions": 960, "reported_total_attractions": 1050, "meal_per_person_cost_sum": 369, "expected_total_meals": 1107, "reported_total_meals": 1413, "reported_total_transportation": 300}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 320, "expected_total_attractions": 960, "reported_total_attractions": 1050, "meal_per_person_cost_sum": 369, "expected_total_meals": 1107, "reported_total_meals": 1413, "reported_total_transportation": 300}}]`

### v3_standard200_realbudget_eval_000009
- request: 苏州 2026-04-30->2026-05-04 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['亲子', '城市地标', '第一次来', '城市漫步']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 15300, "total": 14300, "diff": 1000, "requested_budget": {"available": true, "amount": 20500, "scope": "total", "party_size": 4, "total": 20500, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "soft"}, "per_person_day": 715.0, "budget_level": "comfortable", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "soft", "amount": 20500, "target_min_ratio": 0.7, "target_max_ratio": 1.1, "target_min_total": 14300, "target_max_total": 22600, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 4, "party_total": 4, "room_count": 2, "priced_nights": 4, "expected_min_total_hotels": 10000, "reported_total_hotels": 10000, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 871, "expected_total_attractions": 3484, "reported_total_attractions": 3300, "meal_per_person_cost_sum": 698, "expected_total_meals": 2792, "reported_total_meals": 1000, "reported_total_transportation": 1000}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 871, "expected_total_attractions": 3484, "reported_total_attractions": 3300, "meal_per_person_cost_sum": 698, "expected_total_meals": 2792, "reported_total_meals": 1000, "reported_total_transportation": 1000}}]`

### v3_standard200_realbudget_eval_000021
- request: 上海 2026-06-21->2026-06-22 days=2 transport=地铁+步行 hotel=经济型酒店 prefs=['老人友好', '休闲慢游', '城市漫步', '主题乐园']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 1396, "total": 1400, "diff": -4, "requested_budget": {"available": true, "amount": 1700, "scope": "total", "party_size": 2, "total": 1700, "source": "budget_constraint", "budget_level": "limited", "strictness": "soft"}, "per_person_day": 350.0, "budget_level": "limited", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "limited", "strictness": "soft", "amount": 1700, "target_min_ratio": 0.72, "target_max_ratio": 1.05, "target_min_total": 1200, "target_max_total": 1800, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 1, "party_total": 2, "room_count": 1, "priced_nights": 1, "expected_min_total_hotels": 250, "reported_total_hotels": 250, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 80, "expected_total_attractions": 160, "reported_total_attractions": 180, "meal_per_person_cost_sum": 541, "expected_total_meals": 1082, "reported_total_meals": 916, "reported_total_transportation": 50}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 80, "expected_total_attractions": 160, "reported_total_attractions": 180, "meal_per_person_cost_sum": 541, "expected_total_meals": 1082, "reported_total_meals": 916, "reported_total_transportation": 50}}]`

### v3_standard200_realbudget_eval_000015
- request: 南京 2026-04-07->2026-04-08 days=2 transport=地铁+步行 hotel=经济型酒店 prefs=['亲子', '休闲慢游', '历史文化']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 1974, "total": 2074, "diff": -100, "requested_budget": {"available": true, "amount": 4300, "scope": "total", "party_size": 3, "total": 4300, "source": "budget_constraint", "budget_level": "standard", "strictness": "soft"}, "per_person_day": 345.67, "budget_level": "standard", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "standard", "strictness": "soft", "amount": 4300, "target_min_ratio": 0.6, "target_max_ratio": 1.05, "target_min_total": 2600, "target_max_total": 4500, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 1, "party_total": 3, "room_count": 2, "priced_nights": 1, "expected_min_total_hotels": 500, "reported_total_hotels": 500, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 65, "expected_total_attractions": 195, "reported_total_attractions": 195, "meal_per_person_cost_sum": 395, "expected_total_meals": 1185, "reported_total_meals": 1179, "reported_total_transportation": 100}}, {"stage": "rule", "type": "budget_preference_mismatch", "details": {"part_sum": 1974, "total": 2074, "diff": -100, "requested_budget": {"available": true, "amount": 4300, "scope": "total", "party_size": 3, "total": 4300, "source": "budget_constraint", "budget_level": "standard", "strictness": "soft"}, "per_person_day": 345.67, "budget_level": "standard", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "standard", "strictness": "soft", "amount": 4300, "target_min_ratio": 0.6, "target_max_ratio": 1.05, "target_min_total": 2600, "target_max_total": 4500, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 1, "party_total": 3, "room_count": 2, "priced_nights": 1, "expected_min_total_hotels": 500, "reported_total_hotels": 500, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`
