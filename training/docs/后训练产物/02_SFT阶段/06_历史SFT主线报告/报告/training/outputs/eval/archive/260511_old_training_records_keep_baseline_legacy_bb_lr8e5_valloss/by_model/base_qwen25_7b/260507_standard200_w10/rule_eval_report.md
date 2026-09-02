# Rule Eval Report: base_qwen25_7b_standard200_w10

- records: 200
- generations: `training/outputs/eval/base_qwen25_7b_standard200_w10/generations.jsonl`
- records_path: `training/data/v3/eval/records.jsonl`

## Boolean Metrics

| Metric | Pass | Total | Rate |
| --- | ---: | ---: | ---: |
| accommodation_type_ok | 192 | 197 | 97.46% |
| attraction_budget_consistent | 27 | 197 | 13.71% |
| attraction_budget_party_relation_ok | 55 | 197 | 27.92% |
| attraction_count_ok | 197 | 197 | 100.00% |
| attraction_diversity_ok | 186 | 197 | 94.42% |
| attraction_grounding_ok | 195 | 197 | 98.98% |
| attraction_repeat_limit_ok | 186 | 197 | 94.42% |
| budget_arithmetic_consistent | 116 | 197 | 58.88% |
| budget_consistent | 116 | 197 | 58.88% |
| budget_level_aligned | 50 | 197 | 25.38% |
| budget_preference_aligned | 50 | 197 | 25.38% |
| budget_relationship_ok | 5 | 197 | 2.54% |
| budget_selection_ok | 93 | 197 | 47.21% |
| budget_user_constraint_ok | 194 | 197 | 98.48% |
| budget_within_user_budget | 191 | 197 | 96.95% |
| city_ok | 197 | 197 | 100.00% |
| date_range_ok | 197 | 197 | 100.00% |
| day_dates_ok | 197 | 197 | 100.00% |
| day_index_ok | 197 | 197 | 100.00% |
| days_len_ok | 197 | 197 | 100.00% |
| dpo_soft_pass | 25 | 197 | 12.69% |
| dpo_soft_recomputed_budget_pass | 39 | 197 | 19.80% |
| hard_pass | 172 | 197 | 87.31% |
| hotel_budget_covers_nights | 87 | 197 | 44.16% |
| hotel_budget_relation_ok | 90 | 197 | 45.69% |
| hotel_distance_placeholder_ok | 197 | 197 | 100.00% |
| hotel_grounding_ok | 197 | 197 | 100.00% |
| invalid_hotel_name_ok | 197 | 197 | 100.00% |
| json_extract_ok | 199 | 200 | 99.50% |
| legacy_hard_pass | 22 | 197 | 11.17% |
| location_object_ok | 197 | 197 | 100.00% |
| meal_budget_consistent | 0 | 197 | 0.00% |
| meal_complete | 195 | 197 | 98.98% |
| meal_cost_scale_ok | 37 | 197 | 18.78% |
| meal_diversity_ok | 91 | 197 | 46.19% |
| meal_grounding_ok | 180 | 197 | 91.37% |
| meal_lunch_dinner_same_day_ok | 172 | 197 | 87.31% |
| meal_repeat_limit_ok | 98 | 197 | 49.75% |
| meal_specific_ok | 192 | 197 | 97.46% |
| meal_valid_semantics_ok | 184 | 197 | 93.40% |
| middle_hotel_ok | 197 | 197 | 100.00% |
| recomputed_budget_fit_ok | 93 | 197 | 47.21% |
| recomputed_budget_hard_ok | 194 | 197 | 98.48% |
| recomputed_budget_level_aligned | 93 | 197 | 47.21% |
| recomputed_budget_preference_aligned | 93 | 197 | 47.21% |
| recomputed_budget_user_constraint_ok | 194 | 197 | 98.48% |
| recomputed_budget_within_user_budget | 189 | 197 | 95.94% |
| schema_ok | 197 | 200 | 98.50% |
| sft_budget_semantic_hard_pass | 5 | 197 | 2.54% |
| sft_hard_pass | 172 | 197 | 87.31% |
| sft_no_budget_sum_hard_pass | 172 | 197 | 87.31% |
| sft_strict_hard_pass | 0 | 197 | 0.00% |
| transportation_budget_nonnegative | 197 | 197 | 100.00% |
| weather_dates_ok | 197 | 197 | 100.00% |
| weather_match | 197 | 197 | 100.00% |

## Numeric Metrics

```json
{
  "attraction_diversity_unique_rate": {
    "avg": 0.9908,
    "p50": 1.0,
    "p90": 1.0
  },
  "attraction_grounding_rate": {
    "avg": 0.9977,
    "p50": 1.0,
    "p90": 1.0
  },
  "hotel_grounding_rate": {
    "avg": 1.0,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_diversity_unique_rate": {
    "avg": 0.6675,
    "p50": 0.6667,
    "p90": 1.0
  },
  "meal_food_pois_grounding_rate": {
    "avg": 0.9869,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_grounding_rate": {
    "avg": 0.9869,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_semantic_valid_rate": {
    "avg": 0.9909,
    "p50": 1.0,
    "p90": 1.0
  },
  "recomputed_budget_per_person_day": {
    "avg": 497.581,
    "p50": 458.67,
    "p90": 713.25
  },
  "recomputed_budget_total": {
    "avg": 4627.1269,
    "p50": 3974.0,
    "p90": 8676.0
  }
}
```

## Failure Types

```json
{
  "meal_budget_inconsistent": 197,
  "budget_relationship_mismatch": 192,
  "attraction_budget_inconsistent": 170,
  "meal_cost_scale_too_low": 160,
  "budget_preference_mismatch": 147,
  "hotel_budget_underestimated": 110,
  "meal_repeat_too_many": 99,
  "budget_arithmetic_inconsistent": 81,
  "meal_same_day_lunch_dinner_repeat": 25,
  "meal_invalid_name": 13,
  "attraction_repeat_too_many": 11,
  "meal_placeholder": 5,
  "accommodation_type_mismatch": 5,
  "meal_grounding_miss": 4,
  "budget_hard_constraint_exceeded": 3,
  "schema": 2,
  "json_extract": 1
}
```

## Failure Examples

### v3_standard200_eval_000001
- request: 桂林 2026-09-04->2026-09-06 days=3 transport=公共交通 hotel=高端酒店 prefs=['艺术', '美食', '第一次来', '历史文化']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-09-06", "lunch": "阿甘酒家(七星路店)", "dinner": "阿甘酒家(解西店)"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "阿甘酒家", "count": 3, "max_allowed": 2, "occurrences": [{"date": "2026-09-04", "type": "lunch", "name": "阿甘酒家(解西店)"}, {"date": "2026-09-06", "type": "lunch", "name": "阿甘酒家(七星路店)"}, {"date": "2026-09-06", "type": "dinner", "name": "阿甘酒家(解西店)"}]}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 290, "expected_total_attractions": 580, "reported_total_attractions": 1000, "meal_per_person_cost_sum": 418, "expected_total_meals": 836, "reported_total_meals": 1020, "reported_total_transportation": 200}}]`

### v3_standard200_eval_000000
- request: 昆明 2026-04-07->2026-04-09 days=3 transport=地铁+步行 hotel=高端酒店 prefs=['休闲慢游', '美食']
- errors: `[{"stage": "rule", "type": "meal_placeholder", "details": [{"date": "2026-04-07", "type": "breakfast", "name": "BA(翠湖公园店)"}]}, {"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-04-07", "type": "breakfast", "name": "BA(翠湖公园店)", "reason": "non_food_poi_name"}]}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 0, "expected_total_attractions": 0, "reported_total_attractions": 0, "meal_per_person_cost_sum": 317, "expected_total_meals": 634, "reported_total_meals": 1140, "reported_total_transportation": 300}}]`

### v3_standard200_eval_000008
- request: 大理 2026-05-11->2026-05-13 days=3 transport=地铁+步行 hotel=舒适型酒店 prefs=['休闲慢游', '城市地标', '历史文化']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 2021, "total": 1911, "diff": 110, "requested_budget": {"available": true, "amount": 2900, "scope": "total", "party_size": 2, "total": 2900, "source": "budget_constraint", "budget_level": "standard", "strictness": "soft"}, "per_person_day": 318.5, "budget_level": "standard", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "standard", "strictness": "soft", "amount": 2900, "target_min_ratio": 0.55, "target_max_ratio": 1.1, "target_min_total": 1600, "target_max_total": 3200, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 2, "room_count": 1, "priced_nights": 3, "expected_min_total_hotels": 1200, "reported_total_hotels": 1200, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 75, "expected_total_attractions": 150, "reported_total_attractions": 225, "meal_per_person_cost_sum": 452, "expected_total_meals": 904, "reported_total_meals": 396, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 75, "expected_total_attractions": 150, "reported_total_attractions": 225, "meal_per_person_cost_sum": 452, "expected_total_meals": 904, "reported_total_meals": 396, "reported_total_transportation": 200}}]`

### v3_standard200_eval_000007
- request: 成都 2026-05-11->2026-05-13 days=3 transport=地铁+步行 hotel=舒适型酒店 prefs=['美食', '城市公园', '休闲慢游']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 2218, "total": 2118, "diff": 100, "requested_budget": {"available": true, "amount": 3100, "scope": "total", "party_size": 2, "total": 3100, "source": "budget_constraint", "budget_level": "standard", "strictness": "hard"}, "per_person_day": 353.0, "budget_level": "standard", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "standard", "strictness": "hard", "amount": 3100, "target_min_ratio": 0.55, "target_max_ratio": 1.0, "target_min_total": 1700, "target_max_total": 3100, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 2, "room_count": 1, "priced_nights": 3, "expected_min_total_hotels": 1350, "reported_total_hotels": 1350, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 115, "expected_total_attractions": 230, "reported_total_attractions": 230, "meal_per_person_cost_sum": 617, "expected_total_meals": 1234, "reported_total_meals": 438, "reported_total_transportation": 200}}]`

### v3_standard200_eval_000005
- request: 广州 2026-07-06->2026-07-08 days=3 transport=地铁+步行 hotel=经济型酒店 prefs=['博物馆', '城市公园', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-07-08", "type": "breakfast", "name": "广州汉唐商务租房早餐", "reason": "hotel_or_lodging_name"}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 350, "expected_total_attractions": 700, "reported_total_attractions": 150, "meal_per_person_cost_sum": 477, "expected_total_meals": 954, "reported_total_meals": 322, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 350, "expected_total_attractions": 700, "reported_total_attractions": 150, "meal_per_person_cost_sum": 477, "expected_total_meals": 954, "reported_total_meals": 322, "reported_total_transportation": 200}}]`

### v3_standard200_eval_000004
- request: 张家界 2026-05-11->2026-05-15 days=5 transport=地铁+步行 hotel=舒适型酒店 prefs=['亲子', '城市漫步', '历史文化']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 4, "party_total": 4, "room_count": 2, "priced_nights": 4, "expected_min_total_hotels": 3200, "reported_total_hotels": 2000, "diff": -1200, "covers_nights": false}}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 6000, "total": 5000, "diff": 1000, "requested_budget": {"available": true, "amount": 12500, "scope": "total", "party_size": 4, "total": 12500, "source": "budget_constraint", "budget_level": "standard", "strictness": "soft"}, "per_person_day": 250.0, "budget_level": "standard", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "standard", "strictness": "soft", "amount": 12500, "target_min_ratio": 0.55, "target_max_ratio": 1.1, "target_min_total": 6900, "target_max_total": 13800, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 4, "party_total": 4, "room_count": 2, "priced_nights": 4, "expected_min_total_hotels": 3200, "reported_total_hotels": 2000, "diff": -1200, "covers_nights": false}, "hotel_budget_covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 160, "expected_total_attractions": 640, "reported_total_attractions": 1200, "meal_per_person_cost_sum": 467, "expected_total_meals": 1868, "reported_total_meals": 1800, "reported_total_transportation": 1000}}]`

### v3_standard200_eval_000010
- request: 西安 2026-08-05->2026-08-08 days=4 transport=公共交通 hotel=经济型酒店 prefs=['城市公园', '美食']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 254, "expected_total_attractions": 508, "reported_total_attractions": 480, "meal_per_person_cost_sum": 434, "expected_total_meals": 868, "reported_total_meals": 480, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 254, "expected_total_attractions": 508, "reported_total_attractions": 480, "meal_per_person_cost_sum": 434, "expected_total_meals": 868, "reported_total_meals": 480, "reported_total_transportation": 200}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": true, "meal_cost_scale_ok": false, "budget_relationship_ok": false, "expected_total_hotels": 1000, "reported_total_hotels": 1000, "expected_total_attractions": 508, "reported_total_attractions": 480, "meal_scale_eval": {"ok": false, "party_total": 2, "budget_level": "standard", "per_person_lunch_dinner_floor": 35, "per_person_breakfast_floor": 14, "meal_count": 12, "checked_count": 12, "failure_count": 4, "failures": [{"date": "2026-08-05", "type": "lunch", "name": "魏家凉皮(西大街店)", "estimated_cost": 24, "min_expected_cost": 35}, {"date": "2026-08-05", "type": "dinner", "name": "马洪小炒泡馍馆", "estimated_cost": 31, "min_expected_cost": 35}, {"date": "2026-08-06", "type": "lunch", "name": "蓝田印象", "estimated_cost": 32, "min_expected_cost": 35}, {"date": "2026-08-06", "type": "dinner", "name": "邢老三肉丸糊辣汤腊牛肉夹馍总店", "estimated_cost": 18, "min_expected_cost": 35}]}}}]`

### v3_standard200_eval_000002
- request: 杭州 2026-05-01->2026-05-05 days=5 transport=公共交通 hotel=经济型酒店 prefs=['美食', '休闲慢游', '户外轻徒步', '城市漫步']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 1990, "total": 2000, "diff": -10, "requested_budget": {"available": true, "amount": 2000, "scope": "total", "party_size": 1, "total": 2000, "source": "budget_constraint", "budget_level": "limited", "strictness": "soft"}, "per_person_day": 400.0, "budget_level": "limited", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "limited", "strictness": "soft", "amount": 2000, "target_min_ratio": 0.72, "target_max_ratio": 1.05, "target_min_total": 1400, "target_max_total": 2100, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 4, "party_total": 1, "room_count": 1, "priced_nights": 5, "expected_min_total_hotels": 1250, "reported_total_hotels": 1250, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 40, "expected_total_attractions": 40, "reported_total_attractions": 150, "meal_per_person_cost_sum": 507, "expected_total_meals": 507, "reported_total_meals": 390, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 40, "expected_total_attractions": 40, "reported_total_attractions": 150, "meal_per_person_cost_sum": 507, "expected_total_meals": 507, "reported_total_meals": 390, "reported_total_transportation": 200}}]`

### v3_standard200_eval_000003
- request: 西安 2025-05-07->2025-05-11 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '历史文化', '购物商圈']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "爱骅裤带面馆", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2025-05-07", "type": "breakfast", "name": "爱骅裤带面馆(钟楼店)"}, {"date": "2025-05-08", "type": "breakfast", "name": "爱骅裤带面馆( 总店 )"}, {"date": "2025-05-09", "type": "breakfast", "name": "爱骅裤带面馆(钟楼店)"}, {"date": "2025-05-10", "type": "breakfast", "name": "爱骅裤带面馆(钟楼店)"}, {"date": "2025-05-11", "type": "breakfast", "name": "爱骅裤带面馆(钟楼店)"}]}, {"name_key": "国人川菜", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2025-05-08", "type": "lunch", "name": "国人川菜(李家村店)"}, {"date": "2025-05-09", "type": "lunch", "name": "国人川菜(李家村店)"}, {"date": "2025-05-10", "type": "lunch", "name": "国人川菜(李家村店)"}, {"date": "2025-05-11", "type": "lunch", "name": "国人川菜(李家村店)"}]}, {"name_key": "乐班le’ban·农场餐厅", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2025-05-08", "type": "dinner", "name": "乐班Le’ban·农场餐厅(米禾农场店)"}, {"date": "2025-05-09", "type": "dinner", "name": "乐班Le’ban·农场餐厅(米禾农场店)"}, {"date": "2025-05-10", "type": "dinner", "name": "乐班Le’ban·农场餐厅(米禾农场店)"}, {"date": "2025-05-11", "type": "dinner", "name": "乐班Le’ban·农场餐厅(米禾农场店)"}]}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 4, "party_total": 3, "room_count": 2, "priced_nights": 5, "expected_min_total_hotels": 4500, "reported_total_hotels": 2250, "diff": -2250, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 254, "expected_total_attractions": 762, "reported_total_attractions": 120, "meal_per_person_cost_sum": 911, "expected_total_meals": 2733, "reported_total_meals": 1080, "reported_total_transportation": 1000}}]`

### v3_standard200_eval_000009
- request: 苏州 2026-04-30->2026-05-04 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['亲子', '城市地标', '第一次来', '城市漫步']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 4, "party_total": 4, "room_count": 2, "priced_nights": 5, "expected_min_total_hotels": 4500, "reported_total_hotels": 2250, "diff": -2250, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 215, "expected_total_attractions": 860, "reported_total_attractions": 1155, "meal_per_person_cost_sum": 871, "expected_total_meals": 3484, "reported_total_meals": 1080, "reported_total_transportation": 1000}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 215, "expected_total_attractions": 860, "reported_total_attractions": 1155, "meal_per_person_cost_sum": 871, "expected_total_meals": 3484, "reported_total_meals": 1080, "reported_total_transportation": 1000}}]`

### v3_standard200_eval_000015
- request: 南京 2026-04-07->2026-04-08 days=2 transport=地铁+步行 hotel=经济型酒店 prefs=['亲子', '休闲慢游', '历史文化']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 1, "party_total": 3, "room_count": 2, "priced_nights": 2, "expected_min_total_hotels": 1000, "reported_total_hotels": 500, "diff": -500, "covers_nights": false}}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 988, "total": 1088, "diff": -100, "requested_budget": {"available": true, "amount": 3600, "scope": "total", "party_size": 3, "total": 3600, "source": "budget_constraint", "budget_level": "standard", "strictness": "soft"}, "per_person_day": 181.33, "budget_level": "standard", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "standard", "strictness": "soft", "amount": 3600, "target_min_ratio": 0.55, "target_max_ratio": 1.1, "target_min_total": 2000, "target_max_total": 4000, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 1, "party_total": 3, "room_count": 2, "priced_nights": 2, "expected_min_total_hotels": 1000, "reported_total_hotels": 500, "diff": -500, "covers_nights": false}, "hotel_budget_covers_nights": false}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 0, "expected_total_attractions": 0, "reported_total_attractions": 0, "meal_per_person_cost_sum": 320, "expected_total_meals": 960, "reported_total_meals": 288, "reported_total_transportation": 200}}]`

### v3_standard200_eval_000014
- request: 成都 2026-06-06->2026-06-07 days=2 transport=打车 hotel=经济型酒店 prefs=['小众展览', '美食', '城市地标']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 1, "party_total": 4, "room_count": 2, "priced_nights": 2, "expected_min_total_hotels": 1000, "reported_total_hotels": 500, "diff": -500, "covers_nights": false}}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 2162, "total": 1962, "diff": 200, "requested_budget": {"available": true, "amount": 3000, "scope": "total", "party_size": 4, "total": 3000, "source": "budget_constraint", "budget_level": "limited", "strictness": "soft"}, "per_person_day": 245.25, "budget_level": "limited", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "limited", "strictness": "soft", "amount": 3000, "target_min_ratio": 0.72, "target_max_ratio": 1.05, "target_min_total": 2200, "target_max_total": 3200, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 1, "party_total": 4, "room_count": 2, "priced_nights": 2, "expected_min_total_hotels": 1000, "reported_total_hotels": 500, "diff": -500, "covers_nights": false}, "hotel_budget_covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 170, "expected_total_attractions": 680, "reported_total_attractions": 1150, "meal_per_person_cost_sum": 375, "expected_total_meals": 1500, "reported_total_meals": 312, "reported_total_transportation": 200}}]`

### v3_standard200_eval_000013
- request: 武汉 2026-05-09->2026-05-11 days=3 transport=公共交通 hotel=舒适型酒店 prefs=['亲子', '老人友好', '第一次来', '城市公园']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "矮子馅饼", "count": 3, "max_allowed": 2, "occurrences": [{"date": "2026-05-09", "type": "lunch", "name": "矮子馅饼(三弓路店)"}, {"date": "2026-05-10", "type": "lunch", "name": "矮子馅饼(武汉总店)"}, {"date": "2026-05-11", "type": "lunch", "name": "矮子馅饼(大成路店)"}]}, {"name_key": "刘聋子牛肉粉馆", "count": 3, "max_allowed": 2, "occurrences": [{"date": "2026-05-09", "type": "dinner", "name": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}, {"date": "2026-05-10", "type": "dinner", "name": "刘聋子牛肉粉馆(汉阳玫瑰街店)"}, {"date": "2026-05-11", "type": "dinner", "name": "刘聋子牛肉粉馆(光谷新竹路店)"}]}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 2, "party_total": 6, "room_count": 3, "priced_nights": 3, "expected_min_total_hotels": 3600, "reported_total_hotels": 1200, "diff": -2400, "covers_nights": false}}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 2120, "total": 1920, "diff": 200, "requested_budget": {"available": true, "amount": 13100, "scope": "total", "party_size": 6, "total": 13100, "source": "budget_constraint", "budget_level": "standard", "strictness": "soft"}, "per_person_day": 106.67, "budget_level": "standard", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "standard", "strictness": "soft", "amount": 13100, "target_min_ratio": 0.55, "target_max_ratio": 1.1, "target_min_total": 7200, "target_max_total": 14400, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 6, "room_count": 3, "priced_nights": 3, "expected_min_total_hotels": 3600, "reported_total_hotels": 1200, "diff": -2400, "covers_nights": false}, "hotel_budget_covers_nights": false}}]`

### v3_standard200_eval_000016
- request: 苏州 2026-06-06->2026-06-08 days=3 transport=公共交通 hotel=民宿 prefs=['海滨度假', '城市公园', '主题乐园', '清真']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "魏家凉皮", "count": 3, "max_allowed": 2, "occurrences": [{"date": "2026-06-06", "type": "breakfast", "name": "魏家凉皮(邵磨针巷店)"}, {"date": "2026-06-07", "type": "breakfast", "name": "魏家凉皮(邵磨针巷店)"}, {"date": "2026-06-08", "type": "breakfast", "name": "魏家凉皮(邵磨针巷店)"}]}]}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 1485, "total": 1385, "diff": 100, "requested_budget": {"available": true, "amount": 2400, "scope": "total", "party_size": 2, "total": 2400, "source": "budget_constraint", "budget_level": "limited", "strictness": "soft"}, "per_person_day": 230.83, "budget_level": "limited", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "limited", "strictness": "soft", "amount": 2400, "target_min_ratio": 0.72, "target_max_ratio": 1.05, "target_min_total": 1700, "target_max_total": 2500, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 2, "room_count": 1, "priced_nights": 3, "expected_min_total_hotels": 900, "reported_total_hotels": 900, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 135, "expected_total_attractions": 270, "reported_total_attractions": 205, "meal_per_person_cost_sum": 330, "expected_total_meals": 660, "reported_total_meals": 180, "reported_total_transportation": 200}}]`

### v3_standard200_eval_000006
- request: 南京 2026-07-06->2026-07-09 days=4 transport=打车 hotel=经济型酒店 prefs=['老人友好', '美食', '城市公园', '休闲慢游']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 3, "room_count": 2, "priced_nights": 4, "expected_min_total_hotels": 2000, "reported_total_hotels": 1000, "diff": -1000, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 90, "expected_total_attractions": 270, "reported_total_attractions": 1080, "meal_per_person_cost_sum": 561, "expected_total_meals": 1683, "reported_total_meals": 450, "reported_total_transportation": 400}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 90, "expected_total_attractions": 270, "reported_total_attractions": 1080, "meal_per_person_cost_sum": 561, "expected_total_meals": 1683, "reported_total_meals": 450, "reported_total_transportation": 400}}]`

### v3_standard200_eval_000017
- request: 苏州 2026-05-09->2026-05-11 days=3 transport=地铁+步行 hotel=亲子酒店 prefs=['亲子', '历史文化', '休闲慢游', '户外轻徒步']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 2, "party_total": 3, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 7500, "reported_total_hotels": 3750, "diff": -3750, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 135, "expected_total_attractions": 405, "reported_total_attractions": 215, "meal_per_person_cost_sum": 452, "expected_total_meals": 1356, "reported_total_meals": 510, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 135, "expected_total_attractions": 405, "reported_total_attractions": 215, "meal_per_person_cost_sum": 452, "expected_total_meals": 1356, "reported_total_meals": 510, "reported_total_transportation": 200}}]`

### v3_standard200_eval_000021
- request: 上海 2026-06-21->2026-06-22 days=2 transport=地铁+步行 hotel=经济型酒店 prefs=['老人友好', '休闲慢游', '城市漫步', '主题乐园']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 535, "expected_total_attractions": 1070, "reported_total_attractions": 535, "meal_per_person_cost_sum": 388, "expected_total_meals": 776, "reported_total_meals": 212, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 535, "expected_total_attractions": 1070, "reported_total_attractions": 535, "meal_per_person_cost_sum": 388, "expected_total_meals": 776, "reported_total_meals": 212, "reported_total_transportation": 200}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": false, "meal_cost_scale_ok": true, "budget_relationship_ok": false, "expected_total_hotels": 500, "reported_total_hotels": 500, "expected_total_attractions": 1070, "reported_total_attractions": 535, "meal_scale_eval": {"ok": true, "party_total": 2, "budget_level": "limited", "per_person_lunch_dinner_floor": 25, "per_person_breakfast_floor": 10, "meal_count": 6, "checked_count": 6, "failure_count": 0, "failures": []}}}]`

### v3_standard200_eval_000011
- request: 福州 2026-06-21->2026-06-24 days=4 transport=打车 hotel=经济型酒店 prefs=['第一次来', '城市漫步']
- errors: `[{"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 0, "expected_total_attractions": 0, "reported_total_attractions": 0, "meal_per_person_cost_sum": 602, "expected_total_meals": 1204, "reported_total_meals": 1200, "reported_total_transportation": 400}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": true, "meal_cost_scale_ok": false, "budget_relationship_ok": false, "expected_total_hotels": 800, "reported_total_hotels": 800, "expected_total_attractions": 0, "reported_total_attractions": 0, "meal_scale_eval": {"ok": false, "party_total": 2, "budget_level": "standard", "per_person_lunch_dinner_floor": 35, "per_person_breakfast_floor": 14, "meal_count": 12, "checked_count": 12, "failure_count": 1, "failures": [{"date": "2026-06-21", "type": "lunch", "name": "同利肉燕老铺(三坊七巷店)", "estimated_cost": 23, "min_expected_cost": 35}]}}}, {"stage": "rule", "type": "meal_cost_scale_too_low", "details": {"ok": false, "party_total": 2, "budget_level": "standard", "per_person_lunch_dinner_floor": 35, "per_person_breakfast_floor": 14, "meal_count": 12, "checked_count": 12, "failure_count": 1, "failures": [{"date": "2026-06-21", "type": "lunch", "name": "同利肉燕老铺(三坊七巷店)", "estimated_cost": 23, "min_expected_cost": 35}]}}]`

### v3_standard200_eval_000019
- request: 丽江 2026-05-11->2026-05-15 days=5 transport=打车 hotel=经济型酒店 prefs=['亲子', '老人友好', '海滨度假', '美食']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "丽江古城", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-05-11", "day_index": 0, "name": "丽江古城"}, {"date": "2026-05-15", "day_index": 4, "name": "丽江古城"}]}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "沈记土鸡米线", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-05-11", "type": "lunch", "name": "沈记土鸡米线(七星街店)"}, {"date": "2026-05-12", "type": "breakfast", "name": "沈记土鸡米线(七星街店)"}, {"date": "2026-05-13", "type": "breakfast", "name": "沈记土鸡米线(七星街店)"}, {"date": "2026-05-14", "type": "breakfast", "name": "沈记土鸡米线(七星街店)"}, {"date": "2026-05-15", "type": "breakfast", "name": "沈记土鸡米线(七星街店)"}]}, {"name_key": "大师的面", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-05-11", "type": "dinner", "name": "大师的面"}, {"date": "2026-05-12", "type": "lunch", "name": "大师的面"}, {"date": "2026-05-13", "type": "lunch", "name": "大师的面"}, {"date": "2026-05-14", "type": "lunch", "name": "大师的面"}, {"date": "2026-05-15", "type": "lunch", "name": "大师的面"}]}, {"name_key": "久哥·猪圈咖啡", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-05-12", "type": "dinner", "name": "久哥·猪圈咖啡"}, {"date": "2026-05-13", "type": "dinner", "name": "久哥·猪圈咖啡"}, {"date": "2026-05-14", "type": "dinner", "name": "久哥·猪圈咖啡"}, {"date": "2026-05-15", "type": "dinner", "name": "久哥·猪圈咖啡"}]}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 4, "party_total": 5, "room_count": 3, "priced_nights": 5, "expected_min_total_hotels": 4500, "reported_total_hotels": 1200, "diff": -3300, "covers_nights": false}}]`

### v3_standard200_eval_000018
- request: 天津 2026-07-06->2026-07-07 days=2 transport=打车 hotel=舒适型酒店 prefs=['老人友好', '夜市夜景', '艺术', '第一次来']
- errors: `[{"stage": "rule", "type": "meal_grounding_miss", "details": [{"date": "2026-07-06", "type": "dinner", "name": "王庄夜市"}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 1, "party_total": 3, "room_count": 2, "priced_nights": 2, "expected_min_total_hotels": 1600, "reported_total_hotels": 800, "diff": -800, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 80, "expected_total_attractions": 240, "reported_total_attractions": 480, "meal_per_person_cost_sum": 146, "expected_total_meals": 438, "reported_total_meals": 210, "reported_total_transportation": 200}}]`
