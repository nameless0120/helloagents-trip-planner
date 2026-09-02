# Rule Eval Report: 260507_realbudget_standard_w10

- records: 200
- generations: `training/outputs/eval/by_model/base_qwen25_7b/260507_realbudget_standard_w10/generations.jsonl`
- records_path: `training/data/v3/eval/records.jsonl`

## Boolean Metrics

| Metric | Pass | Total | Rate |
| --- | ---: | ---: | ---: |
| accommodation_type_ok | 196 | 199 | 98.49% |
| attraction_budget_consistent | 26 | 199 | 13.07% |
| attraction_budget_party_relation_ok | 53 | 199 | 26.63% |
| attraction_count_ok | 199 | 199 | 100.00% |
| attraction_diversity_ok | 188 | 199 | 94.47% |
| attraction_grounding_ok | 198 | 199 | 99.50% |
| attraction_repeat_limit_ok | 188 | 199 | 94.47% |
| budget_arithmetic_consistent | 119 | 199 | 59.80% |
| budget_consistent | 119 | 199 | 59.80% |
| budget_level_aligned | 22 | 199 | 11.06% |
| budget_preference_aligned | 22 | 199 | 11.06% |
| budget_relationship_ok | 5 | 199 | 2.51% |
| budget_selection_ok | 72 | 199 | 36.18% |
| budget_user_constraint_ok | 197 | 199 | 98.99% |
| budget_within_user_budget | 198 | 199 | 99.50% |
| city_ok | 199 | 199 | 100.00% |
| date_range_ok | 199 | 199 | 100.00% |
| day_dates_ok | 199 | 199 | 100.00% |
| day_index_ok | 199 | 199 | 100.00% |
| days_len_ok | 199 | 199 | 100.00% |
| dpo_soft_pass | 12 | 199 | 6.03% |
| dpo_soft_recomputed_budget_pass | 29 | 199 | 14.57% |
| hard_pass | 179 | 199 | 89.95% |
| hotel_budget_covers_nights | 88 | 199 | 44.22% |
| hotel_budget_relation_ok | 91 | 199 | 45.73% |
| hotel_distance_placeholder_ok | 199 | 199 | 100.00% |
| hotel_grounding_ok | 199 | 199 | 100.00% |
| invalid_hotel_name_ok | 199 | 199 | 100.00% |
| json_extract_ok | 200 | 200 | 100.00% |
| legacy_hard_pass | 22 | 199 | 11.06% |
| location_object_ok | 199 | 199 | 100.00% |
| meal_budget_consistent | 0 | 199 | 0.00% |
| meal_complete | 197 | 199 | 98.99% |
| meal_cost_scale_ok | 60 | 199 | 30.15% |
| meal_diversity_ok | 78 | 199 | 39.20% |
| meal_grounding_ok | 184 | 199 | 92.46% |
| meal_lunch_dinner_same_day_ok | 172 | 199 | 86.43% |
| meal_repeat_limit_ok | 83 | 199 | 41.71% |
| meal_specific_ok | 194 | 199 | 97.49% |
| meal_valid_semantics_ok | 184 | 199 | 92.46% |
| middle_hotel_ok | 199 | 199 | 100.00% |
| recomputed_budget_fit_ok | 72 | 199 | 36.18% |
| recomputed_budget_hard_ok | 197 | 199 | 98.99% |
| recomputed_budget_level_aligned | 72 | 199 | 36.18% |
| recomputed_budget_preference_aligned | 72 | 199 | 36.18% |
| recomputed_budget_user_constraint_ok | 197 | 199 | 98.99% |
| recomputed_budget_within_user_budget | 194 | 199 | 97.49% |
| schema_ok | 199 | 200 | 99.50% |
| sft_budget_semantic_hard_pass | 4 | 199 | 2.01% |
| sft_hard_pass | 179 | 199 | 89.95% |
| sft_no_budget_sum_hard_pass | 179 | 199 | 89.95% |
| sft_strict_hard_pass | 0 | 199 | 0.00% |
| transportation_budget_nonnegative | 199 | 199 | 100.00% |
| weather_dates_ok | 199 | 199 | 100.00% |
| weather_match | 199 | 199 | 100.00% |

## Numeric Metrics

```json
{
  "attraction_diversity_unique_rate": {
    "avg": 0.9899,
    "p50": 1.0,
    "p90": 1.0
  },
  "attraction_grounding_rate": {
    "avg": 0.9987,
    "p50": 1.0,
    "p90": 1.0
  },
  "hotel_grounding_rate": {
    "avg": 1.0,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_diversity_unique_rate": {
    "avg": 0.6328,
    "p50": 0.6667,
    "p90": 1.0
  },
  "meal_food_pois_grounding_rate": {
    "avg": 0.9865,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_grounding_rate": {
    "avg": 0.9865,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_semantic_valid_rate": {
    "avg": 0.9874,
    "p50": 1.0,
    "p90": 1.0
  },
  "recomputed_budget_per_person_day": {
    "avg": 510.0258,
    "p50": 475.2,
    "p90": 747.75
  },
  "recomputed_budget_total": {
    "avg": 4728.8744,
    "p50": 3983.0,
    "p90": 8445.0
  }
}
```

## Failure Types

```json
{
  "meal_budget_inconsistent": 199,
  "budget_relationship_mismatch": 194,
  "budget_preference_mismatch": 177,
  "attraction_budget_inconsistent": 173,
  "meal_cost_scale_too_low": 139,
  "meal_repeat_too_many": 116,
  "hotel_budget_underestimated": 111,
  "budget_arithmetic_inconsistent": 80,
  "meal_same_day_lunch_dinner_repeat": 27,
  "meal_invalid_name": 15,
  "attraction_repeat_too_many": 11,
  "meal_placeholder": 5,
  "accommodation_type_mismatch": 3,
  "budget_hard_constraint_exceeded": 2,
  "schema": 1
}
```

## Failure Examples

### v3_standard200_realbudget_eval_000005
- request: 广州 2026-07-06->2026-07-08 days=3 transport=地铁+步行 hotel=经济型酒店 prefs=['博物馆', '城市公园', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "民记煲仔饭", "count": 3, "max_allowed": 2, "occurrences": [{"date": "2026-07-06", "type": "lunch", "name": "民记煲仔饭(北京路店)"}, {"date": "2026-07-07", "type": "lunch", "name": "民记煲仔饭(北京路店)"}, {"date": "2026-07-08", "type": "lunch", "name": "民记煲仔饭(北京路店)"}]}, {"name_key": "大鸽饭", "count": 3, "max_allowed": 2, "occurrences": [{"date": "2026-07-06", "type": "dinner", "name": "大鸽饭(北京路店)"}, {"date": "2026-07-07", "type": "dinner", "name": "大鸽饭(北京路店)"}, {"date": "2026-07-08", "type": "dinner", "name": "大鸽饭(北京路店)"}]}]}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 1736, "total": 1716, "diff": 20, "requested_budget": {"available": true, "amount": 2800, "scope": "total", "party_size": 2, "total": 2800, "source": "budget_constraint", "budget_level": "limited", "strictness": "soft"}, "per_person_day": 286.0, "budget_level": "limited", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "limited", "strictness": "soft", "amount": 2800, "target_min_ratio": 0.72, "target_max_ratio": 1.05, "target_min_total": 2000, "target_max_total": 2900, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 2, "room_count": 1, "priced_nights": 3, "expected_min_total_hotels": 750, "reported_total_hotels": 750, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 150, "expected_total_attractions": 300, "reported_total_attractions": 270, "meal_per_person_cost_sum": 588, "expected_total_meals": 1176, "reported_total_meals": 516, "reported_total_transportation": 200}}]`

### v3_standard200_realbudget_eval_000001
- request: 桂林 2026-09-04->2026-09-06 days=3 transport=公共交通 hotel=高端酒店 prefs=['艺术', '美食', '第一次来', '历史文化']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "阿甘酒家", "count": 3, "max_allowed": 2, "occurrences": [{"date": "2026-09-04", "type": "lunch", "name": "阿甘酒家(解西店)"}, {"date": "2026-09-05", "type": "lunch", "name": "阿甘酒家(解西店)"}, {"date": "2026-09-06", "type": "lunch", "name": "阿甘酒家(解西店)"}]}]}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 3345, "total": 5505, "diff": -2160, "requested_budget": {"available": true, "amount": 7100, "scope": "total", "party_size": 2, "total": 7100, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "soft"}, "per_person_day": 917.5, "budget_level": "comfortable", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "soft", "amount": 7100, "target_min_ratio": 0.7, "target_max_ratio": 1.1, "target_min_total": 5000, "target_max_total": 7800, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 2, "room_count": 1, "priced_nights": 3, "expected_min_total_hotels": 2250, "reported_total_hotels": 2250, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 245, "expected_total_attractions": 490, "reported_total_attractions": 655, "meal_per_person_cost_sum": 405, "expected_total_meals": 810, "reported_total_meals": 240, "reported_total_transportation": 200}}]`

### v3_standard200_realbudget_eval_000000
- request: 昆明 2026-04-07->2026-04-09 days=3 transport=地铁+步行 hotel=高端酒店 prefs=['休闲慢游', '美食']
- errors: `[{"stage": "rule", "type": "meal_placeholder", "details": [{"date": "2026-04-07", "type": "breakfast", "name": "BA(翠湖公园店)"}]}, {"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-04-07", "type": "breakfast", "name": "BA(翠湖公园店)", "reason": "non_food_poi_name"}]}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 3720, "total": 4420, "diff": -700, "requested_budget": {"available": true, "amount": 9800, "scope": "total", "party_size": 2, "total": 9800, "source": "budget_constraint", "budget_level": "premium", "strictness": "hard"}, "per_person_day": 736.67, "budget_level": "premium", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "premium", "strictness": "hard", "amount": 9800, "target_min_ratio": 0.75, "target_max_ratio": 1.0, "target_min_total": 7400, "target_max_total": 9800, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 2, "room_count": 1, "priced_nights": 3, "expected_min_total_hotels": 2250, "reported_total_hotels": 2250, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_standard200_realbudget_eval_000008
- request: 大理 2026-05-11->2026-05-13 days=3 transport=地铁+步行 hotel=舒适型酒店 prefs=['休闲慢游', '城市地标', '历史文化']
- errors: `[{"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-05-13", "type": "dinner", "name": "洱海月湿地公园", "reason": "non_food_poi_name"}]}, {"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-05-12", "lunch": "海东茄子烧烤(古城店)", "dinner": "海东茄子烧烤(古城店)"}]}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 2015, "total": 1915, "diff": 100, "requested_budget": {"available": true, "amount": 3700, "scope": "total", "party_size": 2, "total": 3700, "source": "budget_constraint", "budget_level": "standard", "strictness": "soft"}, "per_person_day": 319.17, "budget_level": "standard", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "standard", "strictness": "soft", "amount": 3700, "target_min_ratio": 0.6, "target_max_ratio": 1.05, "target_min_total": 2200, "target_max_total": 3900, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 2, "room_count": 1, "priced_nights": 3, "expected_min_total_hotels": 1200, "reported_total_hotels": 1200, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_standard200_realbudget_eval_000007
- request: 成都 2026-05-11->2026-05-13 days=3 transport=地铁+步行 hotel=舒适型酒店 prefs=['美食', '城市公园', '休闲慢游']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "山面包", "count": 3, "max_allowed": 2, "occurrences": [{"date": "2026-05-11", "type": "breakfast", "name": "山面包(东郊记忆店)"}, {"date": "2026-05-12", "type": "breakfast", "name": "山面包(望平街店)"}, {"date": "2026-05-13", "type": "breakfast", "name": "山面包(东郊记忆店)"}]}]}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 2550, "total": 2500, "diff": 50, "requested_budget": {"available": true, "amount": 4600, "scope": "total", "party_size": 2, "total": 4600, "source": "budget_constraint", "budget_level": "standard", "strictness": "hard"}, "per_person_day": 416.67, "budget_level": "standard", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "standard", "strictness": "hard", "amount": 4600, "target_min_ratio": 0.6, "target_max_ratio": 1.0, "target_min_total": 2800, "target_max_total": 4600, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 2, "room_count": 1, "priced_nights": 3, "expected_min_total_hotels": 1350, "reported_total_hotels": 1350, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 110, "expected_total_attractions": 220, "reported_total_attractions": 160, "meal_per_person_cost_sum": 706, "expected_total_meals": 1412, "reported_total_meals": 840, "reported_total_transportation": 200}}]`

### v3_standard200_realbudget_eval_000004
- request: 张家界 2026-05-11->2026-05-15 days=5 transport=地铁+步行 hotel=舒适型酒店 prefs=['亲子', '城市漫步', '历史文化']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 4, "party_total": 4, "room_count": 2, "priced_nights": 5, "expected_min_total_hotels": 4000, "reported_total_hotels": 2000, "diff": -2000, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 240, "expected_total_attractions": 960, "reported_total_attractions": 1200, "meal_per_person_cost_sum": 584, "expected_total_meals": 2336, "reported_total_meals": 1200, "reported_total_transportation": 500}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 240, "expected_total_attractions": 960, "reported_total_attractions": 1200, "meal_per_person_cost_sum": 584, "expected_total_meals": 2336, "reported_total_meals": 1200, "reported_total_transportation": 500}}]`

### v3_standard200_realbudget_eval_000006
- request: 南京 2026-07-06->2026-07-09 days=4 transport=打车 hotel=经济型酒店 prefs=['老人友好', '美食', '城市公园', '休闲慢游']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-07-06", "lunch": "南京大牌档(中山陵紫金坊店)", "dinner": "南京大牌档(1912总统府店)"}, {"date": "2026-07-08", "lunch": "十朝春精菜馆", "dinner": "十朝春精菜馆"}, {"date": "2026-07-09", "lunch": "小潘记鸭血粉丝汤", "dinner": "小潘记鸭血粉丝汤"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "许阿姨糕团店", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-07-06", "type": "breakfast", "name": "许阿姨糕团店(南京总店)"}, {"date": "2026-07-07", "type": "breakfast", "name": "许阿姨糕团店(南京总店)"}, {"date": "2026-07-08", "type": "breakfast", "name": "许阿姨糕团店(南京总店)"}, {"date": "2026-07-09", "type": "breakfast", "name": "许阿姨糕团店(南京总店)"}]}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 3, "room_count": 2, "priced_nights": 4, "expected_min_total_hotels": 2000, "reported_total_hotels": 1000, "diff": -1000, "covers_nights": false}}]`

### v3_standard200_realbudget_eval_000010
- request: 西安 2026-08-05->2026-08-08 days=4 transport=公共交通 hotel=经济型酒店 prefs=['城市公园', '美食']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 2135, "total": 1735, "diff": 400, "requested_budget": {"available": true, "amount": 6600, "scope": "total", "party_size": 2, "total": 6600, "source": "budget_constraint", "budget_level": "standard", "strictness": "soft"}, "per_person_day": 216.88, "budget_level": "standard", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "standard", "strictness": "soft", "amount": 6600, "target_min_ratio": 0.6, "target_max_ratio": 1.05, "target_min_total": 4000, "target_max_total": 6900, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 2, "room_count": 1, "priced_nights": 4, "expected_min_total_hotels": 1000, "reported_total_hotels": 1000, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 289, "expected_total_attractions": 578, "reported_total_attractions": 455, "meal_per_person_cost_sum": 581, "expected_total_meals": 1162, "reported_total_meals": 480, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 289, "expected_total_attractions": 578, "reported_total_attractions": 455, "meal_per_person_cost_sum": 581, "expected_total_meals": 1162, "reported_total_meals": 480, "reported_total_transportation": 200}}]`

### v3_standard200_realbudget_eval_000003
- request: 西安 2025-05-07->2025-05-11 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '历史文化', '购物商圈']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "爱骅裤带面馆", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2025-05-07", "type": "breakfast", "name": "爱骅裤带面馆(钟楼店)"}, {"date": "2025-05-08", "type": "breakfast", "name": "爱骅裤带面馆( 总店 )"}, {"date": "2025-05-09", "type": "breakfast", "name": "爱骅裤带面馆(钟楼店)"}, {"date": "2025-05-10", "type": "breakfast", "name": "爱骅裤带面馆( 总店 )"}, {"date": "2025-05-11", "type": "breakfast", "name": "爱骅裤带面馆(钟楼店)"}]}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 4, "party_total": 3, "room_count": 2, "priced_nights": 5, "expected_min_total_hotels": 4500, "reported_total_hotels": 2250, "diff": -2250, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 254, "expected_total_attractions": 762, "reported_total_attractions": 600, "meal_per_person_cost_sum": 798, "expected_total_meals": 2394, "reported_total_meals": 1080, "reported_total_transportation": 1000}}]`

### v3_standard200_realbudget_eval_000002
- request: 杭州 2026-05-01->2026-05-05 days=5 transport=公共交通 hotel=经济型酒店 prefs=['美食', '休闲慢游', '户外轻徒步', '城市漫步']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "南宋德寿宫遗址博物馆", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-05-03", "day_index": 2, "name": "南宋德寿宫遗址博物馆"}, {"date": "2026-05-05", "day_index": 4, "name": "南宋德寿宫遗址博物馆"}]}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "方老大", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-05-01", "type": "breakfast", "name": "方老大"}, {"date": "2026-05-02", "type": "breakfast", "name": "方老大"}, {"date": "2026-05-03", "type": "breakfast", "name": "方老大"}, {"date": "2026-05-04", "type": "breakfast", "name": "方老大"}, {"date": "2026-05-05", "type": "breakfast", "name": "方老大"}]}, {"name_key": "知味观", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-05-01", "type": "lunch", "name": "知味观(湖滨总店)"}, {"date": "2026-05-02", "type": "lunch", "name": "知味观(湖滨总店)"}, {"date": "2026-05-03", "type": "lunch", "name": "知味观(湖滨总店)"}, {"date": "2026-05-04", "type": "lunch", "name": "知味观(湖滨总店)"}, {"date": "2026-05-05", "type": "lunch", "name": "知味观(湖滨总店)"}]}, {"name_key": "柳来原味螺蛳粉", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-05-01", "type": "dinner", "name": "柳来原味螺蛳粉(枫香路店)"}, {"date": "2026-05-02", "type": "dinner", "name": "柳来原味螺蛳粉(枫香路店)"}, {"date": "2026-05-03", "type": "dinner", "name": "柳来原味螺蛳粉(枫香路店)"}, {"date": "2026-05-04", "type": "dinner", "name": "柳来原味螺蛳粉(枫香路店)"}, {"date": "2026-05-05", "type": "dinner", "name": "柳来原味螺蛳粉(枫香路店)"}]}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 120, "expected_total_attractions": 120, "reported_total_attractions": 1000, "meal_per_person_cost_sum": 765, "expected_total_meals": 765, "reported_total_meals": 1020, "reported_total_transportation": 200}}]`

### v3_standard200_realbudget_eval_000014
- request: 成都 2026-06-06->2026-06-07 days=2 transport=打车 hotel=经济型酒店 prefs=['小众展览', '美食', '城市地标']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 1, "party_total": 4, "room_count": 2, "priced_nights": 2, "expected_min_total_hotels": 1000, "reported_total_hotels": 500, "diff": -500, "covers_nights": false}}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 1120, "total": 1020, "diff": 100, "requested_budget": {"available": true, "amount": 4100, "scope": "total", "party_size": 4, "total": 4100, "source": "budget_constraint", "budget_level": "limited", "strictness": "soft"}, "per_person_day": 127.5, "budget_level": "limited", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "limited", "strictness": "soft", "amount": 4100, "target_min_ratio": 0.72, "target_max_ratio": 1.05, "target_min_total": 3000, "target_max_total": 4300, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 1, "party_total": 4, "room_count": 2, "priced_nights": 2, "expected_min_total_hotels": 1000, "reported_total_hotels": 500, "diff": -500, "covers_nights": false}, "hotel_budget_covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 60, "expected_total_attractions": 240, "reported_total_attractions": 120, "meal_per_person_cost_sum": 420, "expected_total_meals": 1680, "reported_total_meals": 300, "reported_total_transportation": 200}}]`

### v3_standard200_realbudget_eval_000013
- request: 武汉 2026-05-09->2026-05-11 days=3 transport=公共交通 hotel=舒适型酒店 prefs=['亲子', '老人友好', '第一次来', '城市公园']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "刘胖子家常菜", "count": 3, "max_allowed": 2, "occurrences": [{"date": "2026-05-09", "type": "lunch", "name": "刘胖子家常菜(总店)"}, {"date": "2026-05-10", "type": "lunch", "name": "刘胖子家常菜(中央花园店)"}, {"date": "2026-05-11", "type": "lunch", "name": "刘胖子家常菜(总店)"}]}, {"name_key": "刘聋子牛肉粉馆", "count": 3, "max_allowed": 2, "occurrences": [{"date": "2026-05-09", "type": "dinner", "name": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}, {"date": "2026-05-10", "type": "dinner", "name": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}, {"date": "2026-05-11", "type": "dinner", "name": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}]}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 2, "party_total": 6, "room_count": 3, "priced_nights": 3, "expected_min_total_hotels": 3600, "reported_total_hotels": 1200, "diff": -2400, "covers_nights": false}}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 2013, "total": 1813, "diff": 200, "requested_budget": {"available": true, "amount": 12400, "scope": "total", "party_size": 6, "total": 12400, "source": "budget_constraint", "budget_level": "standard", "strictness": "soft"}, "per_person_day": 100.72, "budget_level": "standard", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "standard", "strictness": "soft", "amount": 12400, "target_min_ratio": 0.6, "target_max_ratio": 1.05, "target_min_total": 7400, "target_max_total": 13000, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 6, "room_count": 3, "priced_nights": 3, "expected_min_total_hotels": 3600, "reported_total_hotels": 1200, "diff": -2400, "covers_nights": false}, "hotel_budget_covers_nights": false}}]`

### v3_standard200_realbudget_eval_000018
- request: 天津 2026-07-06->2026-07-07 days=2 transport=打车 hotel=舒适型酒店 prefs=['老人友好', '夜市夜景', '艺术', '第一次来']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 1, "party_total": 3, "room_count": 2, "priced_nights": 2, "expected_min_total_hotels": 1600, "reported_total_hotels": 800, "diff": -800, "covers_nights": false}}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 1510, "total": 1410, "diff": 100, "requested_budget": {"available": true, "amount": 2700, "scope": "total", "party_size": 3, "total": 2700, "source": "budget_constraint", "budget_level": "limited", "strictness": "hard"}, "per_person_day": 235.0, "budget_level": "limited", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "limited", "strictness": "hard", "amount": 2700, "target_min_ratio": 0.72, "target_max_ratio": 1.0, "target_min_total": 1900, "target_max_total": 2700, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 1, "party_total": 3, "room_count": 2, "priced_nights": 2, "expected_min_total_hotels": 1600, "reported_total_hotels": 800, "diff": -800, "covers_nights": false}, "hotel_budget_covers_nights": false}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 80, "expected_total_attractions": 240, "reported_total_attractions": 240, "meal_per_person_cost_sum": 214, "expected_total_meals": 642, "reported_total_meals": 270, "reported_total_transportation": 200}}]`

### v3_standard200_realbudget_eval_000011
- request: 福州 2026-06-21->2026-06-24 days=4 transport=打车 hotel=经济型酒店 prefs=['第一次来', '城市漫步']
- errors: `[{"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 0, "expected_total_attractions": 0, "reported_total_attractions": 0, "meal_per_person_cost_sum": 740, "expected_total_meals": 1480, "reported_total_meals": 465, "reported_total_transportation": 800}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": true, "meal_cost_scale_ok": false, "budget_relationship_ok": false, "expected_total_hotels": 800, "reported_total_hotels": 800, "expected_total_attractions": 0, "reported_total_attractions": 0, "meal_scale_eval": {"ok": false, "party_total": 2, "budget_level": "standard", "per_person_lunch_dinner_floor": 35, "breakfast_policy": "excluded_from_meal_cost_scale", "meal_count": 12, "checked_count": 8, "failure_count": 1, "failures": [{"date": "2026-06-21", "type": "lunch", "name": "同利肉燕老铺(三坊七巷店)", "estimated_cost": 23, "min_expected_cost": 35}]}}}, {"stage": "rule", "type": "meal_cost_scale_too_low", "details": {"ok": false, "party_total": 2, "budget_level": "standard", "per_person_lunch_dinner_floor": 35, "breakfast_policy": "excluded_from_meal_cost_scale", "meal_count": 12, "checked_count": 8, "failure_count": 1, "failures": [{"date": "2026-06-21", "type": "lunch", "name": "同利肉燕老铺(三坊七巷店)", "estimated_cost": 23, "min_expected_cost": 35}]}}]`

### v3_standard200_realbudget_eval_000021
- request: 上海 2026-06-21->2026-06-22 days=2 transport=地铁+步行 hotel=经济型酒店 prefs=['老人友好', '休闲慢游', '城市漫步', '主题乐园']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 505, "expected_total_attractions": 1010, "reported_total_attractions": 535, "meal_per_person_cost_sum": 408, "expected_total_meals": 816, "reported_total_meals": 302, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 505, "expected_total_attractions": 1010, "reported_total_attractions": 535, "meal_per_person_cost_sum": 408, "expected_total_meals": 816, "reported_total_meals": 302, "reported_total_transportation": 200}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": false, "meal_cost_scale_ok": true, "budget_relationship_ok": false, "expected_total_hotels": 500, "reported_total_hotels": 500, "expected_total_attractions": 1010, "reported_total_attractions": 535, "meal_scale_eval": {"ok": true, "party_total": 2, "budget_level": "limited", "per_person_lunch_dinner_floor": 25, "breakfast_policy": "excluded_from_meal_cost_scale", "meal_count": 6, "checked_count": 4, "failure_count": 0, "failures": []}}}]`

### v3_standard200_realbudget_eval_000017
- request: 苏州 2026-05-09->2026-05-11 days=3 transport=地铁+步行 hotel=亲子酒店 prefs=['亲子', '历史文化', '休闲慢游', '户外轻徒步']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 2, "party_total": 3, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 7500, "reported_total_hotels": 3750, "diff": -3750, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 135, "expected_total_attractions": 405, "reported_total_attractions": 255, "meal_per_person_cost_sum": 453, "expected_total_meals": 1359, "reported_total_meals": 1140, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 135, "expected_total_attractions": 405, "reported_total_attractions": 255, "meal_per_person_cost_sum": 453, "expected_total_meals": 1359, "reported_total_meals": 1140, "reported_total_transportation": 200}}]`

### v3_standard200_realbudget_eval_000016
- request: 苏州 2026-06-06->2026-06-08 days=3 transport=公共交通 hotel=民宿 prefs=['海滨度假', '城市公园', '主题乐园', '清真']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "魏家凉皮", "count": 3, "max_allowed": 2, "occurrences": [{"date": "2026-06-06", "type": "breakfast", "name": "魏家凉皮(邵磨针巷店)"}, {"date": "2026-06-07", "type": "breakfast", "name": "魏家凉皮(邵磨针巷店)"}, {"date": "2026-06-08", "type": "breakfast", "name": "魏家凉皮(邵磨针巷店)"}]}]}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 1556, "total": 1456, "diff": 100, "requested_budget": {"available": true, "amount": 2800, "scope": "total", "party_size": 2, "total": 2800, "source": "budget_constraint", "budget_level": "limited", "strictness": "soft"}, "per_person_day": 242.67, "budget_level": "limited", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "limited", "strictness": "soft", "amount": 2800, "target_min_ratio": 0.72, "target_max_ratio": 1.05, "target_min_total": 2000, "target_max_total": 2900, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 2, "room_count": 1, "priced_nights": 3, "expected_min_total_hotels": 900, "reported_total_hotels": 900, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 135, "expected_total_attractions": 270, "reported_total_attractions": 186, "meal_per_person_cost_sum": 330, "expected_total_meals": 660, "reported_total_meals": 270, "reported_total_transportation": 200}}]`

### v3_standard200_realbudget_eval_000012
- request: 洛阳 2025-05-07->2025-05-10 days=4 transport=打车 hotel=高端酒店 prefs=['休闲慢游', '第一次来']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "方中山胡辣汤", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2025-05-07", "type": "breakfast", "name": "方中山胡辣汤(洛阳一店)"}, {"date": "2025-05-08", "type": "breakfast", "name": "方中山胡辣汤(洛阳二店)"}, {"date": "2025-05-09", "type": "breakfast", "name": "方中山胡辣汤(洛阳二店)"}, {"date": "2025-05-10", "type": "breakfast", "name": "方中山胡辣汤(洛阳二店)"}]}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 3, "room_count": 2, "priced_nights": 4, "expected_min_total_hotels": 6000, "reported_total_hotels": 2250, "diff": -3750, "covers_nights": false}}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 3800, "total": 3200, "diff": 600, "requested_budget": {"available": true, "amount": 23100, "scope": "total", "party_size": 3, "total": 23100, "source": "budget_constraint", "budget_level": "premium", "strictness": "soft"}, "per_person_day": 266.67, "budget_level": "premium", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "premium", "strictness": "soft", "amount": 23100, "target_min_ratio": 0.75, "target_max_ratio": 1.12, "target_min_total": 17300, "target_max_total": 25900, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 3, "room_count": 2, "priced_nights": 4, "expected_min_total_hotels": 6000, "reported_total_hotels": 2250, "diff": -3750, "covers_nights": false}, "hotel_budget_covers_nights": false}}]`

### v3_standard200_realbudget_eval_000009
- request: 苏州 2026-04-30->2026-05-04 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['亲子', '城市地标', '第一次来', '城市漫步']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "魏家凉皮", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-04-30", "type": "breakfast", "name": "魏家凉皮(邵磨针巷店)"}, {"date": "2026-05-01", "type": "breakfast", "name": "魏家凉皮(邵磨针巷店)"}, {"date": "2026-05-02", "type": "breakfast", "name": "魏家凉皮(邵磨针巷店)"}, {"date": "2026-05-03", "type": "breakfast", "name": "魏家凉皮(邵磨针巷店)"}, {"date": "2026-05-04", "type": "breakfast", "name": "魏家凉皮(邵磨针巷店)"}]}, {"name_key": "老横泾面馆", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-04-30", "type": "lunch", "name": "老横泾面馆(吴中横泾总店)"}, {"date": "2026-05-01", "type": "lunch", "name": "老横泾面馆(吴中横泾总店)"}, {"date": "2026-05-02", "type": "lunch", "name": "老横泾面馆(吴中横泾总店)"}, {"date": "2026-05-03", "type": "lunch", "name": "老横泾面馆(吴中横泾总店)"}, {"date": "2026-05-04", "type": "lunch", "name": "老横泾面馆(吴中横泾总店)"}]}, {"name_key": "万福兴", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-04-30", "type": "dinner", "name": "万福兴(东中市总店)"}, {"date": "2026-05-01", "type": "dinner", "name": "万福兴(东中市总店)"}, {"date": "2026-05-02", "type": "dinner", "name": "万福兴(东中市总店)"}, {"date": "2026-05-03", "type": "dinner", "name": "万福兴(东中市总店)"}, {"date": "2026-05-04", "type": "dinner", "name": "万福兴(东中市总店)"}]}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 4, "party_total": 4, "room_count": 2, "priced_nights": 5, "expected_min_total_hotels": 4500, "reported_total_hotels": 2250, "diff": -2250, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 135, "expected_total_attractions": 540, "reported_total_attractions": 1050, "meal_per_person_cost_sum": 415, "expected_total_meals": 1660, "reported_total_meals": 1080, "reported_total_transportation": 1000}}]`

### v3_standard200_realbudget_eval_000015
- request: 南京 2026-04-07->2026-04-08 days=2 transport=地铁+步行 hotel=经济型酒店 prefs=['亲子', '休闲慢游', '历史文化']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 1, "party_total": 3, "room_count": 2, "priced_nights": 2, "expected_min_total_hotels": 1000, "reported_total_hotels": 500, "diff": -500, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 35, "expected_total_attractions": 105, "reported_total_attractions": 35, "meal_per_person_cost_sum": 277, "expected_total_meals": 831, "reported_total_meals": 214, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 35, "expected_total_attractions": 105, "reported_total_attractions": 35, "meal_per_person_cost_sum": 277, "expected_total_meals": 831, "reported_total_meals": 214, "reported_total_transportation": 200}}]`
