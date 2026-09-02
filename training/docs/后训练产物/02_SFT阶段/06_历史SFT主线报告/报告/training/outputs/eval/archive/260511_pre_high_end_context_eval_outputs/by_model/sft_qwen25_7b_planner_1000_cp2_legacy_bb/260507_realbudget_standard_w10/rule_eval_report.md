# Rule Eval Report: 260507_realbudget_standard_w10

- records: 200
- generations: `training/outputs/eval/by_model/sft_qwen25_7b_v3_1000_cp2_v2b/260507_realbudget_standard_w10/generations.jsonl`
- records_path: `training/data/v3/eval/records.jsonl`

## Boolean Metrics

| Metric | Pass | Total | Rate |
| --- | ---: | ---: | ---: |
| accommodation_type_ok | 199 | 199 | 100.00% |
| attraction_budget_consistent | 61 | 199 | 30.65% |
| attraction_budget_party_relation_ok | 173 | 199 | 86.93% |
| attraction_count_ok | 198 | 199 | 99.50% |
| attraction_diversity_ok | 189 | 199 | 94.97% |
| attraction_grounding_ok | 196 | 199 | 98.49% |
| attraction_repeat_limit_ok | 189 | 199 | 94.97% |
| budget_arithmetic_consistent | 153 | 199 | 76.88% |
| budget_consistent | 153 | 199 | 76.88% |
| budget_level_aligned | 148 | 199 | 74.37% |
| budget_preference_aligned | 148 | 199 | 74.37% |
| budget_relationship_ok | 113 | 199 | 56.78% |
| budget_selection_ok | 109 | 199 | 54.77% |
| budget_user_constraint_ok | 199 | 199 | 100.00% |
| budget_within_user_budget | 198 | 199 | 99.50% |
| city_ok | 199 | 199 | 100.00% |
| date_range_ok | 199 | 199 | 100.00% |
| day_dates_ok | 199 | 199 | 100.00% |
| day_index_ok | 199 | 199 | 100.00% |
| days_len_ok | 199 | 199 | 100.00% |
| dpo_soft_pass | 115 | 199 | 57.79% |
| dpo_soft_recomputed_budget_pass | 91 | 199 | 45.73% |
| hard_pass | 189 | 199 | 94.97% |
| hotel_budget_covers_nights | 172 | 199 | 86.43% |
| hotel_budget_relation_ok | 174 | 199 | 87.44% |
| hotel_distance_placeholder_ok | 199 | 199 | 100.00% |
| hotel_grounding_ok | 199 | 199 | 100.00% |
| invalid_hotel_name_ok | 199 | 199 | 100.00% |
| json_extract_ok | 199 | 200 | 99.50% |
| legacy_hard_pass | 114 | 199 | 57.29% |
| location_object_ok | 199 | 199 | 100.00% |
| meal_budget_consistent | 1 | 199 | 0.50% |
| meal_complete | 199 | 199 | 100.00% |
| meal_cost_scale_ok | 142 | 199 | 71.36% |
| meal_diversity_ok | 169 | 199 | 84.92% |
| meal_grounding_ok | 193 | 199 | 96.98% |
| meal_lunch_dinner_same_day_ok | 190 | 199 | 95.48% |
| meal_repeat_limit_ok | 177 | 199 | 88.94% |
| meal_specific_ok | 199 | 199 | 100.00% |
| meal_valid_semantics_ok | 193 | 199 | 96.98% |
| middle_hotel_ok | 199 | 199 | 100.00% |
| recomputed_budget_fit_ok | 109 | 199 | 54.77% |
| recomputed_budget_hard_ok | 197 | 199 | 98.99% |
| recomputed_budget_level_aligned | 109 | 199 | 54.77% |
| recomputed_budget_preference_aligned | 109 | 199 | 54.77% |
| recomputed_budget_user_constraint_ok | 197 | 199 | 98.99% |
| recomputed_budget_within_user_budget | 197 | 199 | 98.99% |
| schema_ok | 199 | 200 | 99.50% |
| sft_budget_semantic_hard_pass | 107 | 199 | 53.77% |
| sft_hard_pass | 189 | 199 | 94.97% |
| sft_no_budget_sum_hard_pass | 189 | 199 | 94.97% |
| sft_strict_hard_pass | 1 | 199 | 0.50% |
| transportation_budget_nonnegative | 199 | 199 | 100.00% |
| weather_dates_ok | 199 | 199 | 100.00% |
| weather_match | 199 | 199 | 100.00% |

## Numeric Metrics

```json
{
  "attraction_diversity_unique_rate": {
    "avg": 0.9944,
    "p50": 1.0,
    "p90": 1.0
  },
  "attraction_grounding_rate": {
    "avg": 0.9986,
    "p50": 1.0,
    "p90": 1.0
  },
  "hotel_grounding_rate": {
    "avg": 1.0,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_diversity_unique_rate": {
    "avg": 0.894,
    "p50": 0.9333,
    "p90": 1.0
  },
  "meal_food_pois_grounding_rate": {
    "avg": 0.9968,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_grounding_rate": {
    "avg": 0.9968,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_semantic_valid_rate": {
    "avg": 0.9968,
    "p50": 1.0,
    "p90": 1.0
  },
  "recomputed_budget_per_person_day": {
    "avg": 590.9014,
    "p50": 507.0,
    "p90": 1001.67
  },
  "recomputed_budget_total": {
    "avg": 5689.4271,
    "p50": 4468.0,
    "p90": 11444.0
  }
}
```

## Failure Types

```json
{
  "meal_budget_inconsistent": 199,
  "attraction_budget_inconsistent": 138,
  "budget_relationship_mismatch": 86,
  "meal_cost_scale_too_low": 57,
  "budget_preference_mismatch": 51,
  "budget_arithmetic_inconsistent": 46,
  "hotel_budget_underestimated": 27,
  "meal_repeat_too_many": 22,
  "attraction_repeat_too_many": 10,
  "meal_same_day_lunch_dinner_repeat": 9,
  "meal_invalid_name": 6,
  "json_extract": 1,
  "too_many_attractions": 1
}
```

## Failure Examples

### v3_standard200_realbudget_eval_000000
- request: 昆明 2026-04-07->2026-04-09 days=3 transport=地铁+步行 hotel=高端酒店 prefs=['休闲慢游', '美食']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 2, "party_total": 2, "room_count": 1, "priced_nights": 2, "expected_min_total_hotels": 1500, "reported_total_hotels": 3000, "diff": 1500, "covers_nights": false}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 50, "expected_total_attractions": 100, "reported_total_attractions": 100, "meal_per_person_cost_sum": 816, "expected_total_meals": 1632, "reported_total_meals": 3400, "reported_total_transportation": 2300}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": false, "attraction_budget_party_relation_ok": true, "meal_cost_scale_ok": false, "budget_relationship_ok": false, "expected_total_hotels": 1500, "reported_total_hotels": 3000, "expected_total_attractions": 100, "reported_total_attractions": 100, "meal_scale_eval": {"ok": false, "party_total": 2, "budget_level": "premium", "per_person_lunch_dinner_floor": 70, "breakfast_policy": "excluded_from_meal_cost_scale", "meal_count": 9, "checked_count": 6, "failure_count": 1, "failures": [{"date": "2026-04-07", "type": "lunch", "name": "湖景坊·经典云南菜·过桥米线(海埂公园店)", "estimated_cost": 57, "min_expected_cost": 70}]}}}]`

### v3_standard200_realbudget_eval_000008
- request: 大理 2026-05-11->2026-05-13 days=3 transport=地铁+步行 hotel=舒适型酒店 prefs=['休闲慢游', '城市地标', '历史文化']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-05-13", "lunch": "老字号·海东茄子烧烤(大关邑店)", "dinner": "老字号·海东茄子烧烤(大关邑店)"}]}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 75, "expected_total_attractions": 150, "reported_total_attractions": 150, "meal_per_person_cost_sum": 445, "expected_total_meals": 890, "reported_total_meals": 850, "reported_total_transportation": 200}}, {"stage": "rule", "type": "budget_preference_mismatch", "details": {"part_sum": 2000, "total": 2000, "diff": 0, "requested_budget": {"available": true, "amount": 3700, "scope": "total", "party_size": 2, "total": 3700, "source": "budget_constraint", "budget_level": "standard", "strictness": "soft"}, "per_person_day": 333.33, "budget_level": "standard", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "standard", "strictness": "soft", "amount": 3700, "target_min_ratio": 0.6, "target_max_ratio": 1.05, "target_min_total": 2200, "target_max_total": 3900, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": true, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 2, "room_count": 1, "priced_nights": 2, "expected_min_total_hotels": 800, "reported_total_hotels": 800, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_standard200_realbudget_eval_000005
- request: 广州 2026-07-06->2026-07-08 days=3 transport=地铁+步行 hotel=经济型酒店 prefs=['博物馆', '城市公园', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 170, "expected_total_attractions": 340, "reported_total_attractions": 320, "meal_per_person_cost_sum": 537, "expected_total_meals": 1074, "reported_total_meals": 1054, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 170, "expected_total_attractions": 340, "reported_total_attractions": 320, "meal_per_person_cost_sum": 537, "expected_total_meals": 1074, "reported_total_meals": 1054, "reported_total_transportation": 200}}]`

### v3_standard200_realbudget_eval_000001
- request: 桂林 2026-09-04->2026-09-06 days=3 transport=公共交通 hotel=高端酒店 prefs=['艺术', '美食', '第一次来', '历史文化']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 623, "expected_total_attractions": 1246, "reported_total_attractions": 1026, "meal_per_person_cost_sum": 437, "expected_total_meals": 874, "reported_total_meals": 1164, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 623, "expected_total_attractions": 1246, "reported_total_attractions": 1026, "meal_per_person_cost_sum": 437, "expected_total_meals": 874, "reported_total_meals": 1164, "reported_total_transportation": 200}}, {"stage": "rule", "type": "budget_preference_mismatch", "details": {"part_sum": 4790, "total": 4790, "diff": 0, "requested_budget": {"available": true, "amount": 7100, "scope": "total", "party_size": 2, "total": 7100, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "soft"}, "per_person_day": 798.33, "budget_level": "comfortable", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "soft", "amount": 7100, "target_min_ratio": 0.7, "target_max_ratio": 1.1, "target_min_total": 5000, "target_max_total": 7800, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": true, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 2, "room_count": 1, "priced_nights": 2, "expected_min_total_hotels": 2400, "reported_total_hotels": 2400, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_standard200_realbudget_eval_000007
- request: 成都 2026-05-11->2026-05-13 days=3 transport=地铁+步行 hotel=舒适型酒店 prefs=['美食', '城市公园', '休闲慢游']
- errors: `[{"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 170, "expected_total_attractions": 340, "reported_total_attractions": 340, "meal_per_person_cost_sum": 790, "expected_total_meals": 1580, "reported_total_meals": 1460, "reported_total_transportation": 600}}]`

### v3_standard200_realbudget_eval_000006
- request: 南京 2026-07-06->2026-07-09 days=4 transport=打车 hotel=经济型酒店 prefs=['老人友好', '美食', '城市公园', '休闲慢游']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 90, "expected_total_attractions": 270, "reported_total_attractions": 240, "meal_per_person_cost_sum": 809, "expected_total_meals": 2427, "reported_total_meals": 2160, "reported_total_transportation": 400}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 90, "expected_total_attractions": 270, "reported_total_attractions": 240, "meal_per_person_cost_sum": 809, "expected_total_meals": 2427, "reported_total_meals": 2160, "reported_total_transportation": 400}}]`

### v3_standard200_realbudget_eval_000010
- request: 西安 2026-08-05->2026-08-08 days=4 transport=公共交通 hotel=经济型酒店 prefs=['城市公园', '美食']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 365, "expected_total_attractions": 730, "reported_total_attractions": 682, "meal_per_person_cost_sum": 541, "expected_total_meals": 1082, "reported_total_meals": 1238, "reported_total_transportation": 1000}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 365, "expected_total_attractions": 730, "reported_total_attractions": 682, "meal_per_person_cost_sum": 541, "expected_total_meals": 1082, "reported_total_meals": 1238, "reported_total_transportation": 1000}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": true, "meal_cost_scale_ok": false, "budget_relationship_ok": false, "expected_total_hotels": 750, "reported_total_hotels": 750, "expected_total_attractions": 730, "reported_total_attractions": 682, "meal_scale_eval": {"ok": false, "party_total": 2, "budget_level": "standard", "per_person_lunch_dinner_floor": 35, "breakfast_policy": "excluded_from_meal_cost_scale", "meal_count": 12, "checked_count": 8, "failure_count": 2, "failures": [{"date": "2026-08-07", "type": "lunch", "name": "马洪小炒泡馍馆", "estimated_cost": 31, "min_expected_cost": 35}, {"date": "2026-08-08", "type": "lunch", "name": "邢老三肉丸糊辣汤腊牛肉夹馍总店", "estimated_cost": 18, "min_expected_cost": 35}]}}}]`

### v3_standard200_realbudget_eval_000004
- request: 张家界 2026-05-11->2026-05-15 days=5 transport=地铁+步行 hotel=舒适型酒店 prefs=['亲子', '城市漫步', '历史文化']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 442, "expected_total_attractions": 1768, "reported_total_attractions": 2044, "meal_per_person_cost_sum": 710, "expected_total_meals": 2840, "reported_total_meals": 2356, "reported_total_transportation": 1000}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 442, "expected_total_attractions": 1768, "reported_total_attractions": 2044, "meal_per_person_cost_sum": 710, "expected_total_meals": 2840, "reported_total_meals": 2356, "reported_total_transportation": 1000}}]`

### v3_standard200_realbudget_eval_000002
- request: 杭州 2026-05-01->2026-05-05 days=5 transport=公共交通 hotel=经济型酒店 prefs=['美食', '休闲慢游', '户外轻徒步', '城市漫步']
- errors: `[{"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 160, "expected_total_attractions": 160, "reported_total_attractions": 160, "meal_per_person_cost_sum": 1016, "expected_total_meals": 1016, "reported_total_meals": 1140, "reported_total_transportation": 600}}]`

### v3_standard200_realbudget_eval_000014
- request: 成都 2026-06-06->2026-06-07 days=2 transport=打车 hotel=经济型酒店 prefs=['小众展览', '美食', '城市地标']
- errors: `[{"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 115, "expected_total_attractions": 460, "reported_total_attractions": 460, "meal_per_person_cost_sum": 496, "expected_total_meals": 1984, "reported_total_meals": 1704, "reported_total_transportation": 800}}]`

### v3_standard200_realbudget_eval_000003
- request: 西安 2025-05-07->2025-05-11 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '历史文化', '购物商圈']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "西安鼓楼", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2025-05-07", "day_index": 0, "name": "西安鼓楼"}, {"date": "2025-05-11", "day_index": 4, "name": "西安鼓楼"}]}, {"name_key": "西安博物院", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2025-05-10", "day_index": 3, "name": "西安博物院"}, {"date": "2025-05-11", "day_index": 4, "name": "西安博物院"}]}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 4, "party_total": 3, "room_count": 2, "priced_nights": 4, "expected_min_total_hotels": 3600, "reported_total_hotels": 4500, "diff": 900, "covers_nights": false}}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 10500, "total": 10400, "diff": 100, "requested_budget": {"available": true, "amount": 15700, "scope": "total", "party_size": 3, "total": 15700, "source": "budget_constraint", "budget_level": "standard", "strictness": "soft"}, "per_person_day": 693.33, "budget_level": "standard", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "standard", "strictness": "soft", "amount": 15700, "target_min_ratio": 0.6, "target_max_ratio": 1.05, "target_min_total": 9400, "target_max_total": 16500, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 4, "party_total": 3, "room_count": 2, "priced_nights": 4, "expected_min_total_hotels": 3600, "reported_total_hotels": 4500, "diff": 900, "covers_nights": false}, "hotel_budget_covers_nights": false}}]`

### v3_standard200_realbudget_eval_000013
- request: 武汉 2026-05-09->2026-05-11 days=3 transport=公共交通 hotel=舒适型酒店 prefs=['亲子', '老人友好', '第一次来', '城市公园']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 7956, "total": 8056, "diff": -100, "requested_budget": {"available": true, "amount": 12400, "scope": "total", "party_size": 6, "total": 12400, "source": "budget_constraint", "budget_level": "standard", "strictness": "soft"}, "per_person_day": 447.56, "budget_level": "standard", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "standard", "strictness": "soft", "amount": 12400, "target_min_ratio": 0.6, "target_max_ratio": 1.05, "target_min_total": 7400, "target_max_total": 13000, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 6, "room_count": 3, "priced_nights": 2, "expected_min_total_hotels": 2400, "reported_total_hotels": 2400, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 6, "hotel_room_count": 3, "attraction_ticket_sum": 83, "expected_total_attractions": 498, "reported_total_attractions": 558, "meal_per_person_cost_sum": 700, "expected_total_meals": 4200, "reported_total_meals": 4698, "reported_total_transportation": 300}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 6, "hotel_room_count": 3, "attraction_ticket_sum": 83, "expected_total_attractions": 498, "reported_total_attractions": 558, "meal_per_person_cost_sum": 700, "expected_total_meals": 4200, "reported_total_meals": 4698, "reported_total_transportation": 300}}]`

### v3_standard200_realbudget_eval_000016
- request: 苏州 2026-06-06->2026-06-08 days=3 transport=公共交通 hotel=民宿 prefs=['海滨度假', '城市公园', '主题乐园', '清真']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "丝路回乡小吃店", "count": 3, "max_allowed": 2, "occurrences": [{"date": "2026-06-06", "type": "lunch", "name": "丝路回乡小吃店(西夏店)"}, {"date": "2026-06-07", "type": "dinner", "name": "丝路回乡小吃店(西夏店)"}, {"date": "2026-06-08", "type": "dinner", "name": "丝路回乡小吃店(西夏店)"}]}, {"name_key": "庆乐居[西北民族餐厅]", "count": 3, "max_allowed": 2, "occurrences": [{"date": "2026-06-06", "type": "dinner", "name": "庆乐居[西北民族餐厅]"}, {"date": "2026-06-07", "type": "lunch", "name": "庆乐居[西北民族餐厅]"}, {"date": "2026-06-08", "type": "lunch", "name": "庆乐居[西北民族餐厅]"}]}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 140, "expected_total_attractions": 280, "reported_total_attractions": 235, "meal_per_person_cost_sum": 165, "expected_total_meals": 330, "reported_total_meals": 418, "reported_total_transportation": 100}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 140, "expected_total_attractions": 280, "reported_total_attractions": 235, "meal_per_person_cost_sum": 165, "expected_total_meals": 330, "reported_total_meals": 418, "reported_total_transportation": 100}}]`

### v3_standard200_realbudget_eval_000011
- request: 福州 2026-06-21->2026-06-24 days=4 transport=打车 hotel=经济型酒店 prefs=['第一次来', '城市漫步']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 117, "expected_total_attractions": 234, "reported_total_attractions": 254, "meal_per_person_cost_sum": 705, "expected_total_meals": 1410, "reported_total_meals": 1674, "reported_total_transportation": 1000}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 117, "expected_total_attractions": 234, "reported_total_attractions": 254, "meal_per_person_cost_sum": 705, "expected_total_meals": 1410, "reported_total_meals": 1674, "reported_total_transportation": 1000}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": true, "meal_cost_scale_ok": false, "budget_relationship_ok": false, "expected_total_hotels": 600, "reported_total_hotels": 600, "expected_total_attractions": 234, "reported_total_attractions": 254, "meal_scale_eval": {"ok": false, "party_total": 2, "budget_level": "standard", "per_person_lunch_dinner_floor": 35, "breakfast_policy": "excluded_from_meal_cost_scale", "meal_count": 12, "checked_count": 8, "failure_count": 1, "failures": [{"date": "2026-06-21", "type": "lunch", "name": "后街捞化", "estimated_cost": 27, "min_expected_cost": 35}]}}}]`

### v3_standard200_realbudget_eval_000017
- request: 苏州 2026-05-09->2026-05-11 days=3 transport=地铁+步行 hotel=亲子酒店 prefs=['亲子', '历史文化', '休闲慢游', '户外轻徒步']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 200, "expected_total_attractions": 600, "reported_total_attractions": 690, "meal_per_person_cost_sum": 428, "expected_total_meals": 1284, "reported_total_meals": 1890, "reported_total_transportation": 1120}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 200, "expected_total_attractions": 600, "reported_total_attractions": 690, "meal_per_person_cost_sum": 428, "expected_total_meals": 1284, "reported_total_meals": 1890, "reported_total_transportation": 1120}}]`

### v3_standard200_realbudget_eval_000012
- request: 洛阳 2025-05-07->2025-05-10 days=4 transport=打车 hotel=高端酒店 prefs=['休闲慢游', '第一次来']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "隋唐城遗址植物园", "count": 3, "max_allowed": 1, "occurrences": [{"date": "2025-05-07", "day_index": 0, "name": "隋唐城遗址植物园"}, {"date": "2025-05-10", "day_index": 3, "name": "隋唐城遗址植物园"}, {"date": "2025-05-10", "day_index": 3, "name": "隋唐城遗址植物园"}]}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 621, "expected_total_attractions": 1863, "reported_total_attractions": 1893, "meal_per_person_cost_sum": 657, "expected_total_meals": 1971, "reported_total_meals": 2838, "reported_total_transportation": 4000}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 621, "expected_total_attractions": 1863, "reported_total_attractions": 1893, "meal_per_person_cost_sum": 657, "expected_total_meals": 1971, "reported_total_meals": 2838, "reported_total_transportation": 4000}}]`

### v3_standard200_realbudget_eval_000018
- request: 天津 2026-07-06->2026-07-07 days=2 transport=打车 hotel=舒适型酒店 prefs=['老人友好', '夜市夜景', '艺术', '第一次来']
- errors: `[{"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 130, "expected_total_attractions": 390, "reported_total_attractions": 390, "meal_per_person_cost_sum": 325, "expected_total_meals": 975, "reported_total_meals": 810, "reported_total_transportation": 100}}]`

### v3_standard200_realbudget_eval_000021
- request: 上海 2026-06-21->2026-06-22 days=2 transport=地铁+步行 hotel=经济型酒店 prefs=['老人友好', '休闲慢游', '城市漫步', '主题乐园']
- errors: `[{"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 70, "expected_total_attractions": 140, "reported_total_attractions": 140, "meal_per_person_cost_sum": 370, "expected_total_meals": 740, "reported_total_meals": 760, "reported_total_transportation": 200}}]`

### v3_standard200_realbudget_eval_000015
- request: 南京 2026-04-07->2026-04-08 days=2 transport=地铁+步行 hotel=经济型酒店 prefs=['亲子', '休闲慢游', '历史文化']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 65, "expected_total_attractions": 195, "reported_total_attractions": 165, "meal_per_person_cost_sum": 348, "expected_total_meals": 1044, "reported_total_meals": 1350, "reported_total_transportation": 800}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 65, "expected_total_attractions": 195, "reported_total_attractions": 165, "meal_per_person_cost_sum": 348, "expected_total_meals": 1044, "reported_total_meals": 1350, "reported_total_transportation": 800}}]`

### v3_standard200_realbudget_eval_000009
- request: 苏州 2026-04-30->2026-05-04 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['亲子', '城市地标', '第一次来', '城市漫步']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "七里山塘景区", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-05-02", "day_index": 2, "name": "七里山塘景区"}, {"date": "2026-05-04", "day_index": 4, "name": "七里山塘景区"}]}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 680, "expected_total_attractions": 2720, "reported_total_attractions": 3160, "meal_per_person_cost_sum": 1111, "expected_total_meals": 4444, "reported_total_meals": 3144, "reported_total_transportation": 1000}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 680, "expected_total_attractions": 2720, "reported_total_attractions": 3160, "meal_per_person_cost_sum": 1111, "expected_total_meals": 4444, "reported_total_meals": 3144, "reported_total_transportation": 1000}}]`
