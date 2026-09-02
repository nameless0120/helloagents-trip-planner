# Rule Eval Report: sft_qwen25_7b_v3_260509_main_clean_step104_standard_w10

- records: 200
- generations: `training/outputs/eval/sft_qwen25_7b_v3_260509_main_clean_step104_standard_w10/generations.jsonl`
- records_path: `training/data/v3/eval/records.jsonl`

## Boolean Metrics

| Metric | Pass | Total | Rate |
| --- | ---: | ---: | ---: |
| accommodation_type_ok | 200 | 200 | 100.00% |
| attraction_budget_consistent | 42 | 200 | 21.00% |
| attraction_budget_party_relation_ok | 161 | 200 | 80.50% |
| attraction_count_ok | 199 | 200 | 99.50% |
| attraction_diversity_ok | 186 | 200 | 93.00% |
| attraction_grounding_ok | 199 | 200 | 99.50% |
| attraction_repeat_limit_ok | 186 | 200 | 93.00% |
| budget_arithmetic_consistent | 153 | 200 | 76.50% |
| budget_consistent | 153 | 200 | 76.50% |
| budget_level_aligned | 154 | 200 | 77.00% |
| budget_preference_aligned | 154 | 200 | 77.00% |
| budget_relationship_ok | 108 | 200 | 54.00% |
| budget_selection_ok | 103 | 200 | 51.50% |
| budget_user_constraint_ok | 200 | 200 | 100.00% |
| budget_within_user_budget | 199 | 200 | 99.50% |
| city_ok | 200 | 200 | 100.00% |
| date_range_ok | 200 | 200 | 100.00% |
| day_dates_ok | 200 | 200 | 100.00% |
| day_index_ok | 200 | 200 | 100.00% |
| days_len_ok | 200 | 200 | 100.00% |
| dpo_soft_pass | 117 | 200 | 58.50% |
| dpo_soft_recomputed_budget_pass | 81 | 200 | 40.50% |
| hard_pass | 192 | 200 | 96.00% |
| hotel_budget_covers_nights | 175 | 200 | 87.50% |
| hotel_budget_relation_ok | 177 | 200 | 88.50% |
| hotel_distance_placeholder_ok | 200 | 200 | 100.00% |
| hotel_grounding_ok | 200 | 200 | 100.00% |
| invalid_hotel_name_ok | 200 | 200 | 100.00% |
| json_extract_ok | 200 | 200 | 100.00% |
| legacy_hard_pass | 109 | 200 | 54.50% |
| location_object_ok | 200 | 200 | 100.00% |
| meal_budget_consistent | 0 | 200 | 0.00% |
| meal_complete | 200 | 200 | 100.00% |
| meal_cost_scale_ok | 142 | 200 | 71.00% |
| meal_diversity_ok | 162 | 200 | 81.00% |
| meal_grounding_ok | 194 | 200 | 97.00% |
| meal_lunch_dinner_same_day_ok | 185 | 200 | 92.50% |
| meal_repeat_limit_ok | 170 | 200 | 85.00% |
| meal_specific_ok | 200 | 200 | 100.00% |
| meal_valid_semantics_ok | 195 | 200 | 97.50% |
| middle_hotel_ok | 200 | 200 | 100.00% |
| recomputed_budget_fit_ok | 103 | 200 | 51.50% |
| recomputed_budget_hard_ok | 198 | 200 | 99.00% |
| recomputed_budget_level_aligned | 103 | 200 | 51.50% |
| recomputed_budget_preference_aligned | 103 | 200 | 51.50% |
| recomputed_budget_user_constraint_ok | 198 | 200 | 99.00% |
| recomputed_budget_within_user_budget | 195 | 200 | 97.50% |
| schema_ok | 200 | 200 | 100.00% |
| sft_budget_semantic_hard_pass | 102 | 200 | 51.00% |
| sft_hard_pass | 192 | 200 | 96.00% |
| sft_no_budget_sum_hard_pass | 192 | 200 | 96.00% |
| sft_strict_hard_pass | 0 | 200 | 0.00% |
| transportation_budget_nonnegative | 200 | 200 | 100.00% |
| weather_dates_ok | 200 | 200 | 100.00% |
| weather_match | 200 | 200 | 100.00% |

## Numeric Metrics

```json
{
  "attraction_diversity_unique_rate": {
    "avg": 0.9914,
    "p50": 1.0,
    "p90": 1.0
  },
  "attraction_grounding_rate": {
    "avg": 0.9992,
    "p50": 1.0,
    "p90": 1.0
  },
  "hotel_grounding_rate": {
    "avg": 1.0,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_diversity_unique_rate": {
    "avg": 0.8727,
    "p50": 0.9167,
    "p90": 1.0
  },
  "meal_food_pois_grounding_rate": {
    "avg": 0.9962,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_grounding_rate": {
    "avg": 0.9962,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_semantic_valid_rate": {
    "avg": 0.9966,
    "p50": 1.0,
    "p90": 1.0
  },
  "recomputed_budget_per_person_day": {
    "avg": 609.7858,
    "p50": 515.75,
    "p90": 1006.4
  },
  "recomputed_budget_total": {
    "avg": 5768.925,
    "p50": 4847.0,
    "p90": 11010.0
  }
}
```

## Failure Types

```json
{
  "meal_budget_inconsistent": 200,
  "attraction_budget_inconsistent": 158,
  "budget_relationship_mismatch": 92,
  "meal_cost_scale_too_low": 58,
  "budget_arithmetic_inconsistent": 47,
  "budget_preference_mismatch": 46,
  "meal_repeat_too_many": 30,
  "hotel_budget_underestimated": 25,
  "meal_same_day_lunch_dinner_repeat": 15,
  "attraction_repeat_too_many": 14,
  "meal_invalid_name": 5,
  "too_many_attractions": 1,
  "meal_grounding_miss": 1
}
```

## Failure Examples

### v3_standard200_realbudget_eval_000000
- request: 昆明 2026-04-07->2026-04-09 days=3 transport=地铁+步行 hotel=高端酒店 prefs=['休闲慢游', '美食']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 2, "party_total": 2, "room_count": 1, "priced_nights": 2, "expected_min_total_hotels": 1500, "reported_total_hotels": 3000, "diff": 1500, "covers_nights": false}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 50, "expected_total_attractions": 100, "reported_total_attractions": 100, "meal_per_person_cost_sum": 812, "expected_total_meals": 1624, "reported_total_meals": 3700, "reported_total_transportation": 600}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": false, "attraction_budget_party_relation_ok": true, "meal_cost_scale_ok": false, "budget_relationship_ok": false, "expected_total_hotels": 1500, "reported_total_hotels": 3000, "expected_total_attractions": 100, "reported_total_attractions": 100, "meal_scale_eval": {"ok": false, "party_total": 2, "budget_level": "premium", "per_person_lunch_dinner_floor": 70, "breakfast_policy": "excluded_from_meal_cost_scale", "meal_count": 9, "checked_count": 6, "failure_count": 2, "failures": [{"date": "2026-04-08", "type": "lunch", "name": "湖景坊·经典云南菜·过桥米线(海埂公园店)", "estimated_cost": 57, "min_expected_cost": 70}, {"date": "2026-04-09", "type": "lunch", "name": "老滇山寨·云南民族特色菜(官渡广场店)", "estimated_cost": 66, "min_expected_cost": 70}]}}}]`

### v3_standard200_realbudget_eval_000008
- request: 大理 2026-05-11->2026-05-13 days=3 transport=地铁+步行 hotel=舒适型酒店 prefs=['休闲慢游', '城市地标', '历史文化']
- errors: `[{"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 75, "expected_total_attractions": 150, "reported_total_attractions": 150, "meal_per_person_cost_sum": 458, "expected_total_meals": 916, "reported_total_meals": 1032, "reported_total_transportation": 200}}, {"stage": "rule", "type": "budget_preference_mismatch", "details": {"part_sum": 2182, "total": 2182, "diff": 0, "requested_budget": {"available": true, "amount": 3700, "scope": "total", "party_size": 2, "total": 3700, "source": "budget_constraint", "budget_level": "standard", "strictness": "soft"}, "per_person_day": 363.67, "budget_level": "standard", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "standard", "strictness": "soft", "amount": 3700, "target_min_ratio": 0.6, "target_max_ratio": 1.05, "target_min_total": 2200, "target_max_total": 3900, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": true, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 2, "room_count": 1, "priced_nights": 2, "expected_min_total_hotels": 800, "reported_total_hotels": 800, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_standard200_realbudget_eval_000001
- request: 桂林 2026-09-04->2026-09-06 days=3 transport=公共交通 hotel=高端酒店 prefs=['艺术', '美食', '第一次来', '历史文化']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "阿甘酒家", "count": 3, "max_allowed": 2, "occurrences": [{"date": "2026-09-04", "type": "breakfast", "name": "阿甘酒家(解西店)"}, {"date": "2026-09-05", "type": "lunch", "name": "阿甘酒家(中山店)"}, {"date": "2026-09-06", "type": "lunch", "name": "阿甘酒家(依仁店)"}]}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 313, "expected_total_attractions": 626, "reported_total_attractions": 726, "meal_per_person_cost_sum": 524, "expected_total_meals": 1048, "reported_total_meals": 1686, "reported_total_transportation": 600}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 313, "expected_total_attractions": 626, "reported_total_attractions": 726, "meal_per_person_cost_sum": 524, "expected_total_meals": 1048, "reported_total_meals": 1686, "reported_total_transportation": 600}}]`

### v3_standard200_realbudget_eval_000007
- request: 成都 2026-05-11->2026-05-13 days=3 transport=地铁+步行 hotel=舒适型酒店 prefs=['美食', '城市公园', '休闲慢游']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 2976, "total": 3076, "diff": -100, "requested_budget": {"available": true, "amount": 4600, "scope": "total", "party_size": 2, "total": 4600, "source": "budget_constraint", "budget_level": "standard", "strictness": "hard"}, "per_person_day": 512.67, "budget_level": "standard", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "standard", "strictness": "hard", "amount": 4600, "target_min_ratio": 0.6, "target_max_ratio": 1.0, "target_min_total": 2800, "target_max_total": 4600, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 2, "room_count": 1, "priced_nights": 2, "expected_min_total_hotels": 900, "reported_total_hotels": 900, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 220, "expected_total_attractions": 440, "reported_total_attractions": 510, "meal_per_person_cost_sum": 737, "expected_total_meals": 1474, "reported_total_meals": 1466, "reported_total_transportation": 100}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 220, "expected_total_attractions": 440, "reported_total_attractions": 510, "meal_per_person_cost_sum": 737, "expected_total_meals": 1474, "reported_total_meals": 1466, "reported_total_transportation": 100}}]`

### v3_standard200_realbudget_eval_000005
- request: 广州 2026-07-06->2026-07-08 days=3 transport=地铁+步行 hotel=经济型酒店 prefs=['博物馆', '城市公园', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 100, "expected_total_attractions": 200, "reported_total_attractions": 340, "meal_per_person_cost_sum": 663, "expected_total_meals": 1326, "reported_total_meals": 1044, "reported_total_transportation": 400}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 100, "expected_total_attractions": 200, "reported_total_attractions": 340, "meal_per_person_cost_sum": 663, "expected_total_meals": 1326, "reported_total_meals": 1044, "reported_total_transportation": 400}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": false, "meal_cost_scale_ok": true, "budget_relationship_ok": false, "expected_total_hotels": 500, "reported_total_hotels": 500, "expected_total_attractions": 200, "reported_total_attractions": 340, "meal_scale_eval": {"ok": true, "party_total": 2, "budget_level": "limited", "per_person_lunch_dinner_floor": 25, "breakfast_policy": "excluded_from_meal_cost_scale", "meal_count": 9, "checked_count": 6, "failure_count": 0, "failures": []}}}]`

### v3_standard200_realbudget_eval_000006
- request: 南京 2026-07-06->2026-07-09 days=4 transport=打车 hotel=经济型酒店 prefs=['老人友好', '美食', '城市公园', '休闲慢游']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 100, "expected_total_attractions": 300, "reported_total_attractions": 255, "meal_per_person_cost_sum": 648, "expected_total_meals": 1944, "reported_total_meals": 2259, "reported_total_transportation": 600}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 100, "expected_total_attractions": 300, "reported_total_attractions": 255, "meal_per_person_cost_sum": 648, "expected_total_meals": 1944, "reported_total_meals": 2259, "reported_total_transportation": 600}}]`

### v3_standard200_realbudget_eval_000010
- request: 西安 2026-08-05->2026-08-08 days=4 transport=公共交通 hotel=经济型酒店 prefs=['城市公园', '美食']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 3644, "total": 4644, "diff": -1000, "requested_budget": {"available": true, "amount": 6600, "scope": "total", "party_size": 2, "total": 6600, "source": "budget_constraint", "budget_level": "standard", "strictness": "soft"}, "per_person_day": 580.5, "budget_level": "standard", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "standard", "strictness": "soft", "amount": 6600, "target_min_ratio": 0.6, "target_max_ratio": 1.05, "target_min_total": 4000, "target_max_total": 6900, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 2, "room_count": 1, "priced_nights": 3, "expected_min_total_hotels": 750, "reported_total_hotels": 750, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 387, "expected_total_attractions": 774, "reported_total_attractions": 846, "meal_per_person_cost_sum": 534, "expected_total_meals": 1068, "reported_total_meals": 1848, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 387, "expected_total_attractions": 774, "reported_total_attractions": 846, "meal_per_person_cost_sum": 534, "expected_total_meals": 1068, "reported_total_meals": 1848, "reported_total_transportation": 200}}]`

### v3_standard200_realbudget_eval_000002
- request: 杭州 2026-05-01->2026-05-05 days=5 transport=公共交通 hotel=经济型酒店 prefs=['美食', '休闲慢游', '户外轻徒步', '城市漫步']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 160, "expected_total_attractions": 160, "reported_total_attractions": 120, "meal_per_person_cost_sum": 1063, "expected_total_meals": 1063, "reported_total_meals": 1034, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 160, "expected_total_attractions": 160, "reported_total_attractions": 120, "meal_per_person_cost_sum": 1063, "expected_total_meals": 1063, "reported_total_meals": 1034, "reported_total_transportation": 200}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": false, "meal_cost_scale_ok": true, "budget_relationship_ok": false, "expected_total_hotels": 1000, "reported_total_hotels": 1000, "expected_total_attractions": 160, "reported_total_attractions": 120, "meal_scale_eval": {"ok": true, "party_total": 1, "budget_level": "limited", "per_person_lunch_dinner_floor": 25, "breakfast_policy": "excluded_from_meal_cost_scale", "meal_count": 15, "checked_count": 10, "failure_count": 0, "failures": []}}}]`

### v3_standard200_realbudget_eval_000004
- request: 张家界 2026-05-11->2026-05-15 days=5 transport=地铁+步行 hotel=舒适型酒店 prefs=['亲子', '城市漫步', '历史文化']
- errors: `[{"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-05-13", "type": "dinner", "name": "老妈妈下饭菜.家常菜三下锅(南庄坪)", "reason": "unknown_food_semantics"}, {"date": "2026-05-14", "type": "dinner", "name": "老妈妈下饭菜.家常菜三下锅(南庄坪)", "reason": "unknown_food_semantics"}, {"date": "2026-05-15", "type": "lunch", "name": "老妈妈下饭菜.家常菜三下锅(南庄坪)", "reason": "unknown_food_semantics"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "麦当劳", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-05-11", "type": "breakfast", "name": "麦当劳(天门中心广场店)"}, {"date": "2026-05-13", "type": "breakfast", "name": "麦当劳(泊富国际文化广场店)"}, {"date": "2026-05-14", "type": "breakfast", "name": "麦当劳(泊富国际文化广场店)"}, {"date": "2026-05-15", "type": "breakfast", "name": "麦当劳(泊富国际文化广场店)"}]}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 301, "expected_total_attractions": 1204, "reported_total_attractions": 1444, "meal_per_person_cost_sum": 623, "expected_total_meals": 2492, "reported_total_meals": 2824, "reported_total_transportation": 400}}]`

### v3_standard200_realbudget_eval_000003
- request: 西安 2025-05-07->2025-05-11 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '历史文化', '购物商圈']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 10500, "total": 9499, "diff": 1001, "requested_budget": {"available": true, "amount": 15700, "scope": "total", "party_size": 3, "total": 15700, "source": "budget_constraint", "budget_level": "standard", "strictness": "soft"}, "per_person_day": 633.27, "budget_level": "standard", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "standard", "strictness": "soft", "amount": 15700, "target_min_ratio": 0.6, "target_max_ratio": 1.05, "target_min_total": 9400, "target_max_total": 16500, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 4, "party_total": 3, "room_count": 2, "priced_nights": 4, "expected_min_total_hotels": 3600, "reported_total_hotels": 3600, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 319, "expected_total_attractions": 957, "reported_total_attractions": 1065, "meal_per_person_cost_sum": 830, "expected_total_meals": 2490, "reported_total_meals": 3852, "reported_total_transportation": 1983}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 319, "expected_total_attractions": 957, "reported_total_attractions": 1065, "meal_per_person_cost_sum": 830, "expected_total_meals": 2490, "reported_total_meals": 3852, "reported_total_transportation": 1983}}]`

### v3_standard200_realbudget_eval_000014
- request: 成都 2026-06-06->2026-06-07 days=2 transport=打车 hotel=经济型酒店 prefs=['小众展览', '美食', '城市地标']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 204, "expected_total_attractions": 816, "reported_total_attractions": 836, "meal_per_person_cost_sum": 504, "expected_total_meals": 2016, "reported_total_meals": 1552, "reported_total_transportation": 400}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 204, "expected_total_attractions": 816, "reported_total_attractions": 836, "meal_per_person_cost_sum": 504, "expected_total_meals": 2016, "reported_total_meals": 1552, "reported_total_transportation": 400}}]`

### v3_standard200_realbudget_eval_000013
- request: 武汉 2026-05-09->2026-05-11 days=3 transport=公共交通 hotel=舒适型酒店 prefs=['亲子', '老人友好', '第一次来', '城市公园']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 6, "hotel_room_count": 3, "attraction_ticket_sum": 146, "expected_total_attractions": 876, "reported_total_attractions": 1056, "meal_per_person_cost_sum": 476, "expected_total_meals": 2856, "reported_total_meals": 3600, "reported_total_transportation": 400}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 6, "hotel_room_count": 3, "attraction_ticket_sum": 146, "expected_total_attractions": 876, "reported_total_attractions": 1056, "meal_per_person_cost_sum": 476, "expected_total_meals": 2856, "reported_total_meals": 3600, "reported_total_transportation": 400}}]`

### v3_standard200_realbudget_eval_000018
- request: 天津 2026-07-06->2026-07-07 days=2 transport=打车 hotel=舒适型酒店 prefs=['老人友好', '夜市夜景', '艺术', '第一次来']
- errors: `[{"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 160, "expected_total_attractions": 480, "reported_total_attractions": 480, "meal_per_person_cost_sum": 383, "expected_total_meals": 1149, "reported_total_meals": 1053, "reported_total_transportation": 200}}]`

### v3_standard200_realbudget_eval_000011
- request: 福州 2026-06-21->2026-06-24 days=4 transport=打车 hotel=经济型酒店 prefs=['第一次来', '城市漫步']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-06-23", "lunch": "紫阳海鲜楼·传承闽味(长乐路总店)", "dinner": "紫阳海鲜楼·传承闽味(华林路店)"}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 2, "room_count": 1, "priced_nights": 3, "expected_min_total_hotels": 600, "reported_total_hotels": 1200, "diff": 600, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 117, "expected_total_attractions": 234, "reported_total_attractions": 304, "meal_per_person_cost_sum": 736, "expected_total_meals": 1472, "reported_total_meals": 2484, "reported_total_transportation": 800}}]`

### v3_standard200_realbudget_eval_000016
- request: 苏州 2026-06-06->2026-06-08 days=3 transport=公共交通 hotel=民宿 prefs=['海滨度假', '城市公园', '主题乐园', '清真']
- errors: `[{"stage": "rule", "type": "too_many_attractions", "details": [{"date": "2026-06-07", "count": 4}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "庆乐居[西北民族餐厅]", "count": 3, "max_allowed": 2, "occurrences": [{"date": "2026-06-06", "type": "lunch", "name": "庆乐居[西北民族餐厅]"}, {"date": "2026-06-07", "type": "lunch", "name": "庆乐居[西北民族餐厅]"}, {"date": "2026-06-08", "type": "lunch", "name": "庆乐居[西北民族餐厅]"}]}, {"name_key": "丝路回乡小吃店", "count": 3, "max_allowed": 2, "occurrences": [{"date": "2026-06-06", "type": "dinner", "name": "丝路回乡小吃店(西夏店)"}, {"date": "2026-06-07", "type": "dinner", "name": "丝路回乡小吃店(西夏店)"}, {"date": "2026-06-08", "type": "dinner", "name": "丝路回乡小吃店(西夏店)"}]}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 140, "expected_total_attractions": 280, "reported_total_attractions": 310, "meal_per_person_cost_sum": 216, "expected_total_meals": 432, "reported_total_meals": 412, "reported_total_transportation": 100}}]`

### v3_standard200_realbudget_eval_000017
- request: 苏州 2026-05-09->2026-05-11 days=3 transport=地铁+步行 hotel=亲子酒店 prefs=['亲子', '历史文化', '休闲慢游', '户外轻徒步']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 8891, "total": 9991, "diff": -1100, "requested_budget": {"available": true, "amount": 10000, "scope": "total", "party_size": 3, "total": 10000, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "soft"}, "per_person_day": 1110.11, "budget_level": "comfortable", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "soft", "amount": 10000, "target_min_ratio": 0.7, "target_max_ratio": 1.1, "target_min_total": 7000, "target_max_total": 11000, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 3, "room_count": 2, "priced_nights": 2, "expected_min_total_hotels": 5000, "reported_total_hotels": 5000, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 380, "expected_total_attractions": 1140, "reported_total_attractions": 1635, "meal_per_person_cost_sum": 436, "expected_total_meals": 1308, "reported_total_meals": 1956, "reported_total_transportation": 300}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 380, "expected_total_attractions": 1140, "reported_total_attractions": 1635, "meal_per_person_cost_sum": 436, "expected_total_meals": 1308, "reported_total_meals": 1956, "reported_total_transportation": 300}}]`

### v3_standard200_realbudget_eval_000021
- request: 上海 2026-06-21->2026-06-22 days=2 transport=地铁+步行 hotel=经济型酒店 prefs=['老人友好', '休闲慢游', '城市漫步', '主题乐园']
- errors: `[{"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 70, "expected_total_attractions": 140, "reported_total_attractions": 140, "meal_per_person_cost_sum": 503, "expected_total_meals": 1006, "reported_total_meals": 822, "reported_total_transportation": 100}}]`

### v3_standard200_realbudget_eval_000009
- request: 苏州 2026-04-30->2026-05-04 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['亲子', '城市地标', '第一次来', '城市漫步']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 16300, "total": 16200, "diff": 100, "requested_budget": {"available": true, "amount": 20500, "scope": "total", "party_size": 4, "total": 20500, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "soft"}, "per_person_day": 810.0, "budget_level": "comfortable", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "soft", "amount": 20500, "target_min_ratio": 0.7, "target_max_ratio": 1.1, "target_min_total": 14300, "target_max_total": 22600, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 4, "party_total": 4, "room_count": 2, "priced_nights": 4, "expected_min_total_hotels": 10000, "reported_total_hotels": 10000, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 682, "expected_total_attractions": 2728, "reported_total_attractions": 2928, "meal_per_person_cost_sum": 805, "expected_total_meals": 3220, "reported_total_meals": 2772, "reported_total_transportation": 600}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 682, "expected_total_attractions": 2728, "reported_total_attractions": 2928, "meal_per_person_cost_sum": 805, "expected_total_meals": 3220, "reported_total_meals": 2772, "reported_total_transportation": 600}}]`

### v3_standard200_realbudget_eval_000012
- request: 洛阳 2025-05-07->2025-05-10 days=4 transport=打车 hotel=高端酒店 prefs=['休闲慢游', '第一次来']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "洛阳博物馆", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2025-05-07", "day_index": 0, "name": "洛阳博物馆"}, {"date": "2025-05-08", "day_index": 1, "name": "洛阳博物馆"}]}, {"name_key": "洛阳古墓博物馆", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2025-05-07", "day_index": 0, "name": "洛阳古墓博物馆"}, {"date": "2025-05-09", "day_index": 2, "name": "洛阳古墓博物馆"}]}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 980, "expected_total_attractions": 2940, "reported_total_attractions": 2880, "meal_per_person_cost_sum": 757, "expected_total_meals": 2271, "reported_total_meals": 4869, "reported_total_transportation": 5000}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 980, "expected_total_attractions": 2940, "reported_total_attractions": 2880, "meal_per_person_cost_sum": 757, "expected_total_meals": 2271, "reported_total_meals": 4869, "reported_total_transportation": 5000}}]`

### v3_standard200_realbudget_eval_000020
- request: 杭州 2026-06-21->2026-06-24 days=4 transport=地铁+步行 hotel=高端酒店 prefs=['历史文化', '海滨度假']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 432, "expected_total_attractions": 864, "reported_total_attractions": 1004, "meal_per_person_cost_sum": 1217, "expected_total_meals": 2434, "reported_total_meals": 3496, "reported_total_transportation": 1100}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 432, "expected_total_attractions": 864, "reported_total_attractions": 1004, "meal_per_person_cost_sum": 1217, "expected_total_meals": 2434, "reported_total_meals": 3496, "reported_total_transportation": 1100}}]`
