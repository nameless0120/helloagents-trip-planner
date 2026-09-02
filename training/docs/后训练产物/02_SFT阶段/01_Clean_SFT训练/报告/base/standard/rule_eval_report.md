# Rule Eval Report: 260511_high_end_context_standard_w10

- records: 200
- generations: `training/outputs/eval/by_model/base_qwen25_7b/260511_high_end_context_standard_w10/generations.jsonl`
- records_path: `training/data/v3/eval/records.jsonl`

## Boolean Metrics

| Metric | Pass | Total | Rate |
| --- | ---: | ---: | ---: |
| accommodation_type_ok | 193 | 198 | 97.47% |
| attraction_budget_consistent | 26 | 198 | 13.13% |
| attraction_budget_party_relation_ok | 59 | 198 | 29.80% |
| attraction_count_ok | 198 | 198 | 100.00% |
| attraction_diversity_ok | 180 | 198 | 90.91% |
| attraction_grounding_ok | 197 | 198 | 99.49% |
| attraction_repeat_limit_ok | 180 | 198 | 90.91% |
| budget_arithmetic_consistent | 105 | 198 | 53.03% |
| budget_consistent | 105 | 198 | 53.03% |
| budget_level_aligned | 36 | 198 | 18.18% |
| budget_preference_aligned | 36 | 198 | 18.18% |
| budget_relationship_ok | 12 | 198 | 6.06% |
| budget_selection_ok | 87 | 198 | 43.94% |
| budget_user_constraint_ok | 196 | 198 | 98.99% |
| budget_within_user_budget | 192 | 198 | 96.97% |
| city_ok | 198 | 198 | 100.00% |
| date_range_ok | 198 | 198 | 100.00% |
| day_dates_ok | 198 | 198 | 100.00% |
| day_index_ok | 198 | 198 | 100.00% |
| days_len_ok | 198 | 198 | 100.00% |
| dpo_soft_pass | 11 | 198 | 5.56% |
| dpo_soft_recomputed_budget_pass | 26 | 198 | 13.13% |
| hard_pass | 178 | 198 | 89.90% |
| hotel_budget_covers_nights | 89 | 198 | 44.95% |
| hotel_budget_relation_ok | 92 | 198 | 46.46% |
| hotel_distance_placeholder_ok | 198 | 198 | 100.00% |
| hotel_grounding_ok | 196 | 198 | 98.99% |
| invalid_hotel_name_ok | 198 | 198 | 100.00% |
| json_extract_ok | 200 | 200 | 100.00% |
| legacy_hard_pass | 18 | 198 | 9.09% |
| location_object_ok | 198 | 198 | 100.00% |
| meal_budget_consistent | 0 | 198 | 0.00% |
| meal_complete | 197 | 198 | 99.49% |
| meal_cost_scale_ok | 70 | 198 | 35.35% |
| meal_diversity_ok | 61 | 198 | 30.81% |
| meal_grounding_ok | 188 | 198 | 94.95% |
| meal_lunch_dinner_same_day_ok | 153 | 198 | 77.27% |
| meal_repeat_limit_ok | 66 | 198 | 33.33% |
| meal_specific_ok | 198 | 198 | 100.00% |
| meal_valid_semantics_ok | 191 | 198 | 96.46% |
| middle_hotel_ok | 198 | 198 | 100.00% |
| recomputed_budget_fit_ok | 87 | 198 | 43.94% |
| recomputed_budget_hard_ok | 194 | 198 | 97.98% |
| recomputed_budget_level_aligned | 87 | 198 | 43.94% |
| recomputed_budget_preference_aligned | 87 | 198 | 43.94% |
| recomputed_budget_user_constraint_ok | 194 | 198 | 97.98% |
| recomputed_budget_within_user_budget | 184 | 198 | 92.93% |
| schema_ok | 198 | 200 | 99.00% |
| sft_budget_semantic_hard_pass | 9 | 198 | 4.55% |
| sft_hard_pass | 178 | 198 | 89.90% |
| sft_no_budget_sum_hard_pass | 178 | 198 | 89.90% |
| sft_strict_hard_pass | 0 | 198 | 0.00% |
| transportation_budget_nonnegative | 198 | 198 | 100.00% |
| weather_dates_ok | 198 | 198 | 100.00% |
| weather_match | 197 | 198 | 99.49% |

## Numeric Metrics

```json
{
  "attraction_diversity_unique_rate": {
    "avg": 0.9837,
    "p50": 1.0,
    "p90": 1.0
  },
  "attraction_grounding_rate": {
    "avg": 0.9995,
    "p50": 1.0,
    "p90": 1.0
  },
  "hotel_grounding_rate": {
    "avg": 0.9899,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_diversity_unique_rate": {
    "avg": 0.5917,
    "p50": 0.5556,
    "p90": 0.9167
  },
  "meal_food_pois_grounding_rate": {
    "avg": 0.9908,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_grounding_rate": {
    "avg": 0.9908,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_semantic_valid_rate": {
    "avg": 0.9928,
    "p50": 1.0,
    "p90": 1.0
  },
  "recomputed_budget_per_person_day": {
    "avg": 681.2611,
    "p50": 493.33,
    "p90": 1285.0
  },
  "recomputed_budget_total": {
    "avg": 6236.6061,
    "p50": 4697.0,
    "p90": 12716.0
  }
}
```

## Failure Types

```json
{
  "meal_budget_inconsistent": 198,
  "budget_relationship_mismatch": 186,
  "attraction_budget_inconsistent": 172,
  "budget_preference_mismatch": 162,
  "meal_repeat_too_many": 132,
  "meal_cost_scale_too_low": 128,
  "hotel_budget_underestimated": 109,
  "budget_arithmetic_inconsistent": 93,
  "meal_same_day_lunch_dinner_repeat": 45,
  "attraction_repeat_too_many": 18,
  "meal_invalid_name": 7,
  "accommodation_type_mismatch": 5,
  "meal_grounding_miss": 3,
  "schema": 2,
  "budget_hard_constraint_exceeded": 2,
  "weather_mismatch": 1
}
```

## Failure Examples

### v3_standard200_realbudget_eval_000001
- request: 桂林 2026-09-04->2026-09-06 days=3 transport=公共交通 hotel=高端酒店 prefs=['艺术', '美食', '第一次来', '历史文化']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 2870, "total": 3870, "diff": -1000, "requested_budget": {"available": true, "amount": 7100, "scope": "total", "party_size": 2, "total": 7100, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "soft"}, "per_person_day": 645.0, "budget_level": "comfortable", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "soft", "amount": 7100, "target_min_ratio": 0.7, "target_max_ratio": 1.1, "target_min_total": 5000, "target_max_total": 7800, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 2, "room_count": 1, "priced_nights": 3, "expected_min_total_hotels": 1800, "reported_total_hotels": 1800, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 210, "expected_total_attractions": 420, "reported_total_attractions": 420, "meal_per_person_cost_sum": 498, "expected_total_meals": 996, "reported_total_meals": 450, "reported_total_transportation": 200}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": true, "meal_cost_scale_ok": false, "budget_relationship_ok": false, "expected_total_hotels": 1800, "reported_total_hotels": 1800, "expected_total_attractions": 420, "reported_total_attractions": 420, "meal_scale_eval": {"ok": false, "party_total": 2, "budget_level": "comfortable", "per_person_lunch_dinner_floor": 50, "breakfast_policy": "excluded_from_meal_cost_scale", "meal_count": 9, "checked_count": 6, "failure_count": 1, "failures": [{"date": "2026-09-06", "type": "dinner", "name": "阳朔小渔村.土菜馆(十里画廊戏楼店)", "estimated_cost": 41, "min_expected_cost": 50}]}}}]`

### v3_standard200_realbudget_eval_000000
- request: 昆明 2026-04-07->2026-04-09 days=3 transport=地铁+步行 hotel=高端酒店 prefs=['休闲慢游', '美食']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 189, "expected_total_attractions": 378, "reported_total_attractions": 412, "meal_per_person_cost_sum": 608, "expected_total_meals": 1216, "reported_total_meals": 1080, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 189, "expected_total_attractions": 378, "reported_total_attractions": 412, "meal_per_person_cost_sum": 608, "expected_total_meals": 1216, "reported_total_meals": 1080, "reported_total_transportation": 200}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": true, "meal_cost_scale_ok": false, "budget_relationship_ok": false, "expected_total_hotels": 3900, "reported_total_hotels": 3900, "expected_total_attractions": 378, "reported_total_attractions": 412, "meal_scale_eval": {"ok": false, "party_total": 2, "budget_level": "premium", "per_person_lunch_dinner_floor": 70, "breakfast_policy": "excluded_from_meal_cost_scale", "meal_count": 9, "checked_count": 6, "failure_count": 3, "failures": [{"date": "2026-04-07", "type": "dinner", "name": "菌小厨野生菌火锅(文明街传统老字号商街店)", "estimated_cost": 60, "min_expected_cost": 70}, {"date": "2026-04-08", "type": "dinner", "name": "太小食堂(南强店)", "estimated_cost": 60, "min_expected_cost": 70}, {"date": "2026-04-09", "type": "dinner", "name": "达美乐比萨(顺城购物中心店)", "estimated_cost": 67, "min_expected_cost": 70}]}}}]`

### v3_standard200_realbudget_eval_000005
- request: 广州 2026-07-06->2026-07-08 days=3 transport=地铁+步行 hotel=经济型酒店 prefs=['博物馆', '城市公园', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 160, "expected_total_attractions": 320, "reported_total_attractions": 420, "meal_per_person_cost_sum": 515, "expected_total_meals": 1030, "reported_total_meals": 270, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 160, "expected_total_attractions": 320, "reported_total_attractions": 420, "meal_per_person_cost_sum": 515, "expected_total_meals": 1030, "reported_total_meals": 270, "reported_total_transportation": 200}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": false, "meal_cost_scale_ok": false, "budget_relationship_ok": false, "expected_total_hotels": 750, "reported_total_hotels": 750, "expected_total_attractions": 320, "reported_total_attractions": 420, "meal_scale_eval": {"ok": false, "party_total": 2, "budget_level": "limited", "per_person_lunch_dinner_floor": 25, "breakfast_policy": "excluded_from_meal_cost_scale", "meal_count": 9, "checked_count": 6, "failure_count": 1, "failures": [{"date": "2026-07-06", "type": "lunch", "name": "银记肠粉(北京路店)", "estimated_cost": 23, "min_expected_cost": 25}]}}}]`

### v3_standard200_realbudget_eval_000008
- request: 大理 2026-05-11->2026-05-13 days=3 transport=地铁+步行 hotel=舒适型酒店 prefs=['休闲慢游', '城市地标', '历史文化']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-05-13", "lunch": "海东茄子烧烤(古城店)", "dinner": "海东茄子烧烤(古城店)"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "老爷爷的手工鲜花饼", "count": 3, "max_allowed": 2, "occurrences": [{"date": "2026-05-11", "type": "breakfast", "name": "老爷爷的手工鲜花饼(总店)"}, {"date": "2026-05-12", "type": "breakfast", "name": "老爷爷的手工鲜花饼(总店)"}, {"date": "2026-05-13", "type": "breakfast", "name": "老爷爷的手工鲜花饼(总店)"}]}]}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 2003, "total": 1903, "diff": 100, "requested_budget": {"available": true, "amount": 3700, "scope": "total", "party_size": 2, "total": 3700, "source": "budget_constraint", "budget_level": "standard", "strictness": "soft"}, "per_person_day": 317.17, "budget_level": "standard", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "standard", "strictness": "soft", "amount": 3700, "target_min_ratio": 0.6, "target_max_ratio": 1.05, "target_min_total": 2200, "target_max_total": 3900, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 2, "room_count": 1, "priced_nights": 3, "expected_min_total_hotels": 1200, "reported_total_hotels": 1200, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_standard200_realbudget_eval_000007
- request: 成都 2026-05-11->2026-05-13 days=3 transport=地铁+步行 hotel=舒适型酒店 prefs=['美食', '城市公园', '休闲慢游']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "山面包", "count": 3, "max_allowed": 2, "occurrences": [{"date": "2026-05-11", "type": "breakfast", "name": "山面包(东郊记忆店)"}, {"date": "2026-05-12", "type": "breakfast", "name": "山面包(望平街店)"}, {"date": "2026-05-13", "type": "breakfast", "name": "山面包(东郊记忆店)"}]}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 115, "expected_total_attractions": 230, "reported_total_attractions": 1155, "meal_per_person_cost_sum": 654, "expected_total_meals": 1308, "reported_total_meals": 819, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 115, "expected_total_attractions": 230, "reported_total_attractions": 1155, "meal_per_person_cost_sum": 654, "expected_total_meals": 1308, "reported_total_meals": 819, "reported_total_transportation": 200}}]`

### v3_standard200_realbudget_eval_000004
- request: 张家界 2026-05-11->2026-05-15 days=5 transport=地铁+步行 hotel=舒适型酒店 prefs=['亲子', '城市漫步', '历史文化']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 4, "party_total": 4, "room_count": 2, "priced_nights": 5, "expected_min_total_hotels": 4000, "reported_total_hotels": 1600, "diff": -2400, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 720, "expected_total_attractions": 2880, "reported_total_attractions": 1200, "meal_per_person_cost_sum": 364, "expected_total_meals": 1456, "reported_total_meals": 1020, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 720, "expected_total_attractions": 2880, "reported_total_attractions": 1200, "meal_per_person_cost_sum": 364, "expected_total_meals": 1456, "reported_total_meals": 1020, "reported_total_transportation": 200}}]`

### v3_standard200_realbudget_eval_000010
- request: 西安 2026-08-05->2026-08-08 days=4 transport=公共交通 hotel=经济型酒店 prefs=['城市公园', '美食']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-08-05", "lunch": "魏家凉皮(西大街店)", "dinner": "魏家凉皮(秦飞大厦店)"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "爱骅裤带面馆", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-08-05", "type": "breakfast", "name": "爱骅裤带面馆(钟楼店)"}, {"date": "2026-08-06", "type": "breakfast", "name": "爱骅裤带面馆(钟楼店)"}, {"date": "2026-08-07", "type": "breakfast", "name": "爱骅裤带面馆(钟楼店)"}, {"date": "2026-08-08", "type": "breakfast", "name": "爱骅裤带面馆(钟楼店)"}]}, {"name_key": "魏家凉皮", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-08-05", "type": "lunch", "name": "魏家凉皮(西大街店)"}, {"date": "2026-08-05", "type": "dinner", "name": "魏家凉皮(秦飞大厦店)"}, {"date": "2026-08-06", "type": "lunch", "name": "魏家凉皮(秦飞大厦店)"}, {"date": "2026-08-07", "type": "lunch", "name": "魏家凉皮(秦飞大厦店)"}, {"date": "2026-08-08", "type": "lunch", "name": "魏家凉皮(秦飞大厦店)"}]}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 2, "room_count": 1, "priced_nights": 4, "expected_min_total_hotels": 1000, "reported_total_hotels": 750, "diff": -250, "covers_nights": false}}]`

### v3_standard200_realbudget_eval_000006
- request: 南京 2026-07-06->2026-07-09 days=4 transport=打车 hotel=经济型酒店 prefs=['老人友好', '美食', '城市公园', '休闲慢游']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-07-06", "lunch": "南京大牌档(中山陵紫金坊店)", "dinner": "南京大牌档(1912总统府店)"}, {"date": "2026-07-07", "lunch": "清真·西北桥头拉面大王(丁家桥店)", "dinner": "清真·西北桥头拉面大王(丁家桥店)"}, {"date": "2026-07-08", "lunch": "无名老卤面(中华门总店)", "dinner": "无名老卤面(中华门总店)"}, {"date": "2026-07-09", "lunch": "小潘记鸭血粉丝汤", "dinner": "小潘记鸭血粉丝汤"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "许阿姨糕团店", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-07-06", "type": "breakfast", "name": "许阿姨糕团店(南京总店)"}, {"date": "2026-07-07", "type": "breakfast", "name": "许阿姨糕团店(南京总店)"}, {"date": "2026-07-08", "type": "breakfast", "name": "许阿姨糕团店(南京总店)"}, {"date": "2026-07-09", "type": "breakfast", "name": "许阿姨糕团店(南京总店)"}]}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 3, "room_count": 2, "priced_nights": 4, "expected_min_total_hotels": 2000, "reported_total_hotels": 1000, "diff": -1000, "covers_nights": false}}]`

### v3_standard200_realbudget_eval_000003
- request: 西安 2025-05-07->2025-05-11 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '历史文化', '购物商圈']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "爱骅裤带面馆", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2025-05-07", "type": "breakfast", "name": "爱骅裤带面馆(钟楼店)"}, {"date": "2025-05-08", "type": "breakfast", "name": "爱骅裤带面馆( 总店 )"}, {"date": "2025-05-09", "type": "breakfast", "name": "爱骅裤带面馆(钟楼店)"}, {"date": "2025-05-10", "type": "breakfast", "name": "爱骅裤带面馆(钟楼店)"}, {"date": "2025-05-11", "type": "breakfast", "name": "爱骅裤带面馆(钟楼店)"}]}, {"name_key": "奔跑吧陕菜·雁塔长安", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2025-05-08", "type": "dinner", "name": "奔跑吧陕菜·雁塔长安(大雁塔店)"}, {"date": "2025-05-09", "type": "dinner", "name": "奔跑吧陕菜·雁塔长安(大雁塔店)"}, {"date": "2025-05-10", "type": "dinner", "name": "奔跑吧陕菜·雁塔长安(大雁塔店)"}, {"date": "2025-05-11", "type": "dinner", "name": "奔跑吧陕菜·雁塔长安(大雁塔店)"}]}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 4, "party_total": 3, "room_count": 2, "priced_nights": 5, "expected_min_total_hotels": 4500, "reported_total_hotels": 2250, "diff": -2250, "covers_nights": false}}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 4678, "total": 4778, "diff": -100, "requested_budget": {"available": true, "amount": 15700, "scope": "total", "party_size": 3, "total": 15700, "source": "budget_constraint", "budget_level": "standard", "strictness": "soft"}, "per_person_day": 318.53, "budget_level": "standard", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "standard", "strictness": "soft", "amount": 15700, "target_min_ratio": 0.6, "target_max_ratio": 1.05, "target_min_total": 9400, "target_max_total": 16500, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 4, "party_total": 3, "room_count": 2, "priced_nights": 5, "expected_min_total_hotels": 4500, "reported_total_hotels": 2250, "diff": -2250, "covers_nights": false}, "hotel_budget_covers_nights": false}}]`

### v3_standard200_realbudget_eval_000002
- request: 杭州 2026-05-01->2026-05-05 days=5 transport=公共交通 hotel=经济型酒店 prefs=['美食', '休闲慢游', '户外轻徒步', '城市漫步']
- errors: `[{"stage": "rule", "type": "accommodation_type_mismatch", "details": [{"date": "2026-05-05", "day_index": 4, "expected": "经济型酒店", "got": "无住宿"}]}, {"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-05-05", "lunch": "肯德基(市民中心1号店)", "dinner": "肯德基(市民中心1号店)"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "肯德基", "count": 6, "max_allowed": 3, "occurrences": [{"date": "2026-05-01", "type": "dinner", "name": "肯德基(杭州灵隐店)"}, {"date": "2026-05-02", "type": "dinner", "name": "肯德基(市民中心1号店)"}, {"date": "2026-05-03", "type": "dinner", "name": "肯德基(市民中心1号店)"}, {"date": "2026-05-04", "type": "dinner", "name": "肯德基(市民中心1号店)"}, {"date": "2026-05-05", "type": "lunch", "name": "肯德基(市民中心1号店)"}, {"date": "2026-05-05", "type": "dinner", "name": "肯德基(市民中心1号店)"}]}]}]`

### v3_standard200_realbudget_eval_000014
- request: 成都 2026-06-06->2026-06-07 days=2 transport=打车 hotel=经济型酒店 prefs=['小众展览', '美食', '城市地标']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 1, "party_total": 4, "room_count": 2, "priced_nights": 2, "expected_min_total_hotels": 1000, "reported_total_hotels": 500, "diff": -500, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 115, "expected_total_attractions": 460, "reported_total_attractions": 600, "meal_per_person_cost_sum": 464, "expected_total_meals": 1856, "reported_total_meals": 320, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 115, "expected_total_attractions": 460, "reported_total_attractions": 600, "meal_per_person_cost_sum": 464, "expected_total_meals": 1856, "reported_total_meals": 320, "reported_total_transportation": 200}}]`

### v3_standard200_realbudget_eval_000013
- request: 武汉 2026-05-09->2026-05-11 days=3 transport=公共交通 hotel=舒适型酒店 prefs=['亲子', '老人友好', '第一次来', '城市公园']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-05-10", "lunch": "刘聋子牛肉粉馆(汉阳龙兴东街店)", "dinner": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}, {"date": "2026-05-11", "lunch": "刘聋子牛肉粉馆(汉阳龙兴东街店)", "dinner": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "刘聋子牛肉粉馆", "count": 5, "max_allowed": 2, "occurrences": [{"date": "2026-05-09", "type": "dinner", "name": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}, {"date": "2026-05-10", "type": "lunch", "name": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}, {"date": "2026-05-10", "type": "dinner", "name": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}, {"date": "2026-05-11", "type": "lunch", "name": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}, {"date": "2026-05-11", "type": "dinner", "name": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}]}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 2, "party_total": 6, "room_count": 3, "priced_nights": 3, "expected_min_total_hotels": 3600, "reported_total_hotels": 1200, "diff": -2400, "covers_nights": false}}]`

### v3_standard200_realbudget_eval_000018
- request: 天津 2026-07-06->2026-07-07 days=2 transport=打车 hotel=舒适型酒店 prefs=['老人友好', '夜市夜景', '艺术', '第一次来']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 1, "party_total": 3, "room_count": 2, "priced_nights": 2, "expected_min_total_hotels": 1600, "reported_total_hotels": 800, "diff": -800, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 130, "expected_total_attractions": 390, "reported_total_attractions": 310, "meal_per_person_cost_sum": 257, "expected_total_meals": 771, "reported_total_meals": 252, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 130, "expected_total_attractions": 390, "reported_total_attractions": 310, "meal_per_person_cost_sum": 257, "expected_total_meals": 771, "reported_total_meals": 252, "reported_total_transportation": 200}}]`

### v3_standard200_realbudget_eval_000011
- request: 福州 2026-06-21->2026-06-24 days=4 transport=打车 hotel=经济型酒店 prefs=['第一次来', '城市漫步']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "麦当劳", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-06-21", "type": "lunch", "name": "麦当劳(烟台山店)"}, {"date": "2026-06-22", "type": "breakfast", "name": "麦当劳(烟台山店)"}, {"date": "2026-06-23", "type": "breakfast", "name": "麦当劳(烟台山店)"}, {"date": "2026-06-24", "type": "breakfast", "name": "麦当劳(烟台山店)"}]}]}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 0, "expected_total_attractions": 0, "reported_total_attractions": 0, "meal_per_person_cost_sum": 574, "expected_total_meals": 1148, "reported_total_meals": 480, "reported_total_transportation": 800}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": true, "meal_cost_scale_ok": false, "budget_relationship_ok": false, "expected_total_hotels": 800, "reported_total_hotels": 800, "expected_total_attractions": 0, "reported_total_attractions": 0, "meal_scale_eval": {"ok": false, "party_total": 2, "budget_level": "standard", "per_person_lunch_dinner_floor": 35, "breakfast_policy": "excluded_from_meal_cost_scale", "meal_count": 12, "checked_count": 8, "failure_count": 4, "failures": [{"date": "2026-06-21", "type": "lunch", "name": "麦当劳(烟台山店)", "estimated_cost": 28, "min_expected_cost": 35}, {"date": "2026-06-21", "type": "dinner", "name": "古街依强稀饭(古街商厦店)", "estimated_cost": 17, "min_expected_cost": 35}, {"date": "2026-06-23", "type": "dinner", "name": "后街捞化", "estimated_cost": 27, "min_expected_cost": 35}, {"date": "2026-06-24", "type": "dinner", "name": "没牙伯花生汤店", "estimated_cost": 16, "min_expected_cost": 35}]}}}]`

### v3_standard200_realbudget_eval_000016
- request: 苏州 2026-06-06->2026-06-08 days=3 transport=公共交通 hotel=民宿 prefs=['海滨度假', '城市公园', '主题乐园', '清真']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "魏家凉皮", "count": 3, "max_allowed": 2, "occurrences": [{"date": "2026-06-06", "type": "breakfast", "name": "魏家凉皮(邵磨针巷店)"}, {"date": "2026-06-07", "type": "breakfast", "name": "魏家凉皮(邵磨针巷店)"}, {"date": "2026-06-08", "type": "breakfast", "name": "魏家凉皮(邵磨针巷店)"}]}, {"name_key": "阿萨中东料理·清真", "count": 3, "max_allowed": 2, "occurrences": [{"date": "2026-06-06", "type": "lunch", "name": "阿萨中东料理·清真(苏州万象天地店)"}, {"date": "2026-06-07", "type": "lunch", "name": "阿萨中东料理·清真(苏州万象天地店)"}, {"date": "2026-06-08", "type": "lunch", "name": "阿萨中东料理·清真(苏州万象天地店)"}]}, {"name_key": "庆乐居[西北民族餐厅]", "count": 3, "max_allowed": 2, "occurrences": [{"date": "2026-06-06", "type": "dinner", "name": "庆乐居[西北民族餐厅]"}, {"date": "2026-06-07", "type": "dinner", "name": "庆乐居[西北民族餐厅]"}, {"date": "2026-06-08", "type": "dinner", "name": "庆乐居[西北民族餐厅]"}]}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 135, "expected_total_attractions": 270, "reported_total_attractions": 276, "meal_per_person_cost_sum": 498, "expected_total_meals": 996, "reported_total_meals": 180, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 135, "expected_total_attractions": 270, "reported_total_attractions": 276, "meal_per_person_cost_sum": 498, "expected_total_meals": 996, "reported_total_meals": 180, "reported_total_transportation": 200}}]`

### v3_standard200_realbudget_eval_000012
- request: 洛阳 2025-05-07->2025-05-10 days=4 transport=打车 hotel=高端酒店 prefs=['休闲慢游', '第一次来']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "方中山胡辣汤", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2025-05-07", "type": "breakfast", "name": "方中山胡辣汤(洛阳一店)"}, {"date": "2025-05-08", "type": "breakfast", "name": "方中山胡辣汤(洛阳二店)"}, {"date": "2025-05-09", "type": "breakfast", "name": "方中山胡辣汤(洛阳一店)"}, {"date": "2025-05-10", "type": "breakfast", "name": "方中山胡辣汤(洛阳一店)"}]}, {"name_key": "唐宫乐宴", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2025-05-07", "type": "lunch", "name": "唐宫乐宴"}, {"date": "2025-05-08", "type": "lunch", "name": "唐宫乐宴"}, {"date": "2025-05-09", "type": "lunch", "name": "唐宫乐宴"}, {"date": "2025-05-10", "type": "lunch", "name": "唐宫乐宴"}]}, {"name_key": "武皇盛宴", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2025-05-07", "type": "dinner", "name": "武皇盛宴(西工店)"}, {"date": "2025-05-08", "type": "dinner", "name": "武皇盛宴(老城十字街店)"}, {"date": "2025-05-09", "type": "dinner", "name": "武皇盛宴(老城十字街店)"}, {"date": "2025-05-10", "type": "dinner", "name": "武皇盛宴(西工店)"}]}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 3, "room_count": 2, "priced_nights": 4, "expected_min_total_hotels": 10400, "reported_total_hotels": 5200, "diff": -5200, "covers_nights": false}}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 9200, "total": 8200, "diff": 1000, "requested_budget": {"available": true, "amount": 23100, "scope": "total", "party_size": 3, "total": 23100, "source": "budget_constraint", "budget_level": "premium", "strictness": "soft"}, "per_person_day": 683.33, "budget_level": "premium", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "premium", "strictness": "soft", "amount": 23100, "target_min_ratio": 0.75, "target_max_ratio": 1.12, "target_min_total": 17300, "target_max_total": 25900, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 3, "room_count": 2, "priced_nights": 4, "expected_min_total_hotels": 10400, "reported_total_hotels": 5200, "diff": -5200, "covers_nights": false}, "hotel_budget_covers_nights": false}}]`

### v3_standard200_realbudget_eval_000017
- request: 苏州 2026-05-09->2026-05-11 days=3 transport=地铁+步行 hotel=亲子酒店 prefs=['亲子', '历史文化', '休闲慢游', '户外轻徒步']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "老横泾面馆", "count": 3, "max_allowed": 2, "occurrences": [{"date": "2026-05-09", "type": "breakfast", "name": "老横泾面馆(吴中横泾总店)"}, {"date": "2026-05-10", "type": "breakfast", "name": "老横泾面馆(吴中横泾总店)"}, {"date": "2026-05-11", "type": "breakfast", "name": "老横泾面馆(吴中横泾总店)"}]}, {"name_key": "苏州太太精致苏帮菜", "count": 3, "max_allowed": 2, "occurrences": [{"date": "2026-05-09", "type": "dinner", "name": "苏州太太精致苏帮菜(苏州总店)"}, {"date": "2026-05-10", "type": "dinner", "name": "苏州太太精致苏帮菜(苏州总店)"}, {"date": "2026-05-11", "type": "dinner", "name": "苏州太太精致苏帮菜(苏州总店)"}]}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 2, "party_total": 3, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 8100, "reported_total_hotels": 4050, "diff": -4050, "covers_nights": false}}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 6055, "total": 6820, "diff": -765, "requested_budget": {"available": true, "amount": 10000, "scope": "total", "party_size": 3, "total": 10000, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "soft"}, "per_person_day": 757.78, "budget_level": "comfortable", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "soft", "amount": 10000, "target_min_ratio": 0.7, "target_max_ratio": 1.1, "target_min_total": 7000, "target_max_total": 11000, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 3, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 8100, "reported_total_hotels": 4050, "diff": -4050, "covers_nights": false}, "hotel_budget_covers_nights": false}}]`

### v3_standard200_realbudget_eval_000021
- request: 上海 2026-06-21->2026-06-22 days=2 transport=地铁+步行 hotel=经济型酒店 prefs=['老人友好', '休闲慢游', '城市漫步', '主题乐园']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 2017, "total": 1717, "diff": 300, "requested_budget": {"available": true, "amount": 1700, "scope": "total", "party_size": 2, "total": 1700, "source": "budget_constraint", "budget_level": "limited", "strictness": "soft"}, "per_person_day": 429.25, "budget_level": "limited", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "limited", "strictness": "soft", "amount": 1700, "target_min_ratio": 0.72, "target_max_ratio": 1.05, "target_min_total": 1200, "target_max_total": 1800, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 1, "party_total": 2, "room_count": 1, "priced_nights": 2, "expected_min_total_hotels": 500, "reported_total_hotels": 500, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 535, "expected_total_attractions": 1070, "reported_total_attractions": 1075, "meal_per_person_cost_sum": 408, "expected_total_meals": 816, "reported_total_meals": 242, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 535, "expected_total_attractions": 1070, "reported_total_attractions": 1075, "meal_per_person_cost_sum": 408, "expected_total_meals": 816, "reported_total_meals": 242, "reported_total_transportation": 200}}]`

### v3_standard200_realbudget_eval_000009
- request: 苏州 2026-04-30->2026-05-04 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['亲子', '城市地标', '第一次来', '城市漫步']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "秋娟馄饨店", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-04-30", "type": "breakfast", "name": "秋娟馄饨店"}, {"date": "2026-05-01", "type": "breakfast", "name": "秋娟馄饨店"}, {"date": "2026-05-02", "type": "breakfast", "name": "秋娟馄饨店"}, {"date": "2026-05-03", "type": "breakfast", "name": "秋娟馄饨店"}, {"date": "2026-05-04", "type": "breakfast", "name": "秋娟馄饨店"}]}, {"name_key": "老横泾面馆", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-04-30", "type": "lunch", "name": "老横泾面馆(吴中横泾总店)"}, {"date": "2026-05-02", "type": "lunch", "name": "老横泾面馆(吴中横泾总店)"}, {"date": "2026-05-03", "type": "lunch", "name": "老横泾面馆(吴中横泾总店)"}, {"date": "2026-05-04", "type": "lunch", "name": "老横泾面馆(吴中横泾总店)"}]}, {"name_key": "瓦当下·茶馆私房菜", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-04-30", "type": "dinner", "name": "瓦当下·茶馆私房菜(星悦汇店)"}, {"date": "2026-05-01", "type": "dinner", "name": "瓦当下·茶馆私房菜(星悦汇店)"}, {"date": "2026-05-02", "type": "dinner", "name": "瓦当下·茶馆私房菜(星悦汇店)"}, {"date": "2026-05-03", "type": "dinner", "name": "瓦当下·茶馆私房菜(星悦汇店)"}, {"date": "2026-05-04", "type": "dinner", "name": "瓦当下·茶馆私房菜(星悦汇店)"}]}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 4, "party_total": 4, "room_count": 2, "priced_nights": 5, "expected_min_total_hotels": 14000, "reported_total_hotels": 7000, "diff": -7000, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 215, "expected_total_attractions": 860, "reported_total_attractions": 1000, "meal_per_person_cost_sum": 1022, "expected_total_meals": 4088, "reported_total_meals": 2400, "reported_total_transportation": 1000}}]`

### v3_standard200_realbudget_eval_000015
- request: 南京 2026-04-07->2026-04-08 days=2 transport=地铁+步行 hotel=经济型酒店 prefs=['亲子', '休闲慢游', '历史文化']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 1, "party_total": 3, "room_count": 2, "priced_nights": 2, "expected_min_total_hotels": 1000, "reported_total_hotels": 500, "diff": -500, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 35, "expected_total_attractions": 105, "reported_total_attractions": 398, "meal_per_person_cost_sum": 292, "expected_total_meals": 876, "reported_total_meals": 254, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 35, "expected_total_attractions": 105, "reported_total_attractions": 398, "meal_per_person_cost_sum": 292, "expected_total_meals": 876, "reported_total_meals": 254, "reported_total_transportation": 200}}]`
