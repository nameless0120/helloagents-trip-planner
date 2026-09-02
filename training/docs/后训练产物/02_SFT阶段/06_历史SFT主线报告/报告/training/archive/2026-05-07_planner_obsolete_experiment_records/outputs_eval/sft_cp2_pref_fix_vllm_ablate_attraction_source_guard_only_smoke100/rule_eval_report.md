# Rule Eval Report: sft_cp2_pref_fix_vllm_ablate_attraction_source_guard_only_smoke100

- records: 100
- generations: `training/outputs/eval/sft_cp2_pref_fix_vllm_ablate_attraction_source_guard_only_smoke100/generations.jsonl`
- records_path: `training/data/v3/eval_harder_pref_fix_attraction_prompt_ablation_attraction_source_guard_only_no_route/records.jsonl`

## Boolean Metrics

| Metric | Pass | Total | Rate |
| --- | ---: | ---: | ---: |
| accommodation_type_ok | 98 | 98 | 100.00% |
| attraction_budget_consistent | 10 | 98 | 10.20% |
| attraction_budget_party_relation_ok | 40 | 98 | 40.82% |
| attraction_count_ok | 96 | 98 | 97.96% |
| attraction_diversity_ok | 66 | 98 | 67.35% |
| attraction_grounding_ok | 87 | 98 | 88.78% |
| attraction_repeat_limit_ok | 66 | 98 | 67.35% |
| budget_arithmetic_consistent | 68 | 98 | 69.39% |
| budget_consistent | 68 | 98 | 69.39% |
| budget_level_aligned | 60 | 98 | 61.22% |
| budget_preference_aligned | 60 | 98 | 61.22% |
| budget_relationship_ok | 11 | 98 | 11.22% |
| budget_selection_ok | 46 | 98 | 46.94% |
| budget_user_constraint_ok | 89 | 98 | 90.82% |
| budget_within_user_budget | 98 | 98 | 100.00% |
| city_ok | 98 | 98 | 100.00% |
| date_range_ok | 98 | 98 | 100.00% |
| day_dates_ok | 98 | 98 | 100.00% |
| day_index_ok | 98 | 98 | 100.00% |
| days_len_ok | 98 | 98 | 100.00% |
| dpo_soft_pass | 30 | 98 | 30.61% |
| dpo_soft_recomputed_budget_pass | 22 | 98 | 22.45% |
| hard_pass | 84 | 98 | 85.71% |
| hotel_budget_covers_nights | 61 | 98 | 62.24% |
| hotel_budget_relation_ok | 62 | 98 | 63.27% |
| hotel_distance_placeholder_ok | 98 | 98 | 100.00% |
| hotel_grounding_ok | 97 | 98 | 98.98% |
| invalid_hotel_name_ok | 98 | 98 | 100.00% |
| json_extract_ok | 100 | 100 | 100.00% |
| legacy_hard_pass | 28 | 98 | 28.57% |
| location_object_ok | 98 | 98 | 100.00% |
| meal_budget_consistent | 0 | 98 | 0.00% |
| meal_complete | 98 | 98 | 100.00% |
| meal_cost_scale_ok | 32 | 98 | 32.65% |
| meal_diversity_ok | 70 | 98 | 71.43% |
| meal_grounding_ok | 95 | 98 | 96.94% |
| meal_lunch_dinner_same_day_ok | 87 | 98 | 88.78% |
| meal_repeat_limit_ok | 77 | 98 | 78.57% |
| meal_specific_ok | 98 | 98 | 100.00% |
| meal_valid_semantics_ok | 96 | 98 | 97.96% |
| middle_hotel_ok | 98 | 98 | 100.00% |
| recomputed_budget_fit_ok | 46 | 98 | 46.94% |
| recomputed_budget_hard_ok | 85 | 98 | 86.73% |
| recomputed_budget_level_aligned | 46 | 98 | 46.94% |
| recomputed_budget_preference_aligned | 46 | 98 | 46.94% |
| recomputed_budget_user_constraint_ok | 85 | 98 | 86.73% |
| recomputed_budget_within_user_budget | 96 | 98 | 97.96% |
| schema_ok | 98 | 100 | 98.00% |
| sft_budget_semantic_hard_pass | 10 | 98 | 10.20% |
| sft_hard_pass | 84 | 98 | 85.71% |
| sft_no_budget_sum_hard_pass | 84 | 98 | 85.71% |
| sft_strict_hard_pass | 0 | 98 | 0.00% |
| transportation_budget_nonnegative | 98 | 98 | 100.00% |
| weather_dates_ok | 98 | 98 | 100.00% |
| weather_match | 98 | 98 | 100.00% |

## Numeric Metrics

```json
{
  "attraction_diversity_unique_rate": {
    "avg": 0.9401,
    "p50": 1.0,
    "p90": 1.0
  },
  "attraction_grounding_rate": {
    "avg": 0.9861,
    "p50": 1.0,
    "p90": 1.0
  },
  "hotel_grounding_rate": {
    "avg": 0.9898,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_diversity_unique_rate": {
    "avg": 0.7624,
    "p50": 0.8,
    "p90": 1.0
  },
  "meal_food_pois_grounding_rate": {
    "avg": 0.9976,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_grounding_rate": {
    "avg": 0.9976,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_semantic_valid_rate": {
    "avg": 0.9985,
    "p50": 1.0,
    "p90": 1.0
  },
  "recomputed_budget_per_person_day": {
    "avg": 580.9185,
    "p50": 556.0,
    "p90": 794.89
  },
  "recomputed_budget_total": {
    "avg": 6352.9796,
    "p50": 5984.0,
    "p90": 10945.0
  }
}
```

## Failure Types

```json
{
  "meal_budget_inconsistent": 98,
  "attraction_budget_inconsistent": 88,
  "budget_relationship_mismatch": 87,
  "meal_cost_scale_too_low": 66,
  "budget_preference_mismatch": 38,
  "hotel_budget_underestimated": 37,
  "attraction_repeat_too_many": 32,
  "budget_arithmetic_inconsistent": 30,
  "meal_repeat_too_many": 21,
  "meal_same_day_lunch_dinner_repeat": 11,
  "budget_hard_constraint_exceeded": 9,
  "schema": 2,
  "too_many_attractions": 2,
  "meal_invalid_name": 2,
  "meal_grounding_miss": 1
}
```

## Failure Examples

### v3_harder_pref_fix_eval_000004
- request: 张家界 2026-05-10->2026-05-12 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 160, "expected_total_attractions": 160, "reported_total_attractions": 240, "meal_per_person_cost_sum": 493, "expected_total_meals": 493, "reported_total_meals": 632, "reported_total_transportation": 300}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 160, "expected_total_attractions": 160, "reported_total_attractions": 240, "meal_per_person_cost_sum": 493, "expected_total_meals": 493, "reported_total_meals": 632, "reported_total_transportation": 300}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": false, "meal_cost_scale_ok": false, "budget_relationship_ok": false, "expected_total_hotels": 800, "reported_total_hotels": 800, "expected_total_attractions": 160, "reported_total_attractions": 240, "meal_scale_eval": {"ok": false, "party_total": 1, "budget_level": "comfortable", "per_person_lunch_dinner_floor": 50, "per_person_breakfast_floor": 20, "meal_count": 9, "checked_count": 9, "failure_count": 1, "failures": [{"date": "2026-05-11", "type": "breakfast", "name": "家旺小吃(解放路店)", "estimated_cost": 13, "min_expected_cost": 20}]}}}]`

### v3_harder_pref_fix_eval_000014
- request: 成都 2026-06-05->2026-06-07 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 2670, "total": 2470, "diff": 200, "requested_budget": {"available": true, "amount": 3000, "scope": "total", "party_size": 1, "total": 3000, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "hard"}, "per_person_day": 823.33, "budget_level": "comfortable", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "hard", "amount": 3000, "target_min_ratio": 0.65, "target_max_ratio": 1.0, "target_min_total": 2000, "target_max_total": 3000, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 1, "room_count": 1, "priced_nights": 2, "expected_min_total_hotels": 900, "reported_total_hotels": 900, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 185, "expected_total_attractions": 185, "reported_total_attractions": 235, "meal_per_person_cost_sum": 603, "expected_total_meals": 603, "reported_total_meals": 1335, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 185, "expected_total_attractions": 185, "reported_total_attractions": 235, "meal_per_person_cost_sum": 603, "expected_total_meals": 603, "reported_total_meals": 1335, "reported_total_transportation": 200}}]`

### v3_harder_pref_fix_eval_000019
- request: 丽江 2026-05-10->2026-05-13 days=4 transport=打车 hotel=亲子酒店 prefs=['亲子', '老人友好', '博物馆', '城市公园', '特色餐厅']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "黑龙潭", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-05-10", "day_index": 0, "name": "黑龙潭"}, {"date": "2026-05-13", "day_index": 3, "name": "黑龙潭"}]}, {"name_key": "丽江古道藏家博物馆", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-05-11", "day_index": 1, "name": "丽江古道藏家博物馆"}, {"date": "2026-05-12", "day_index": 2, "name": "丽江古道藏家博物馆"}]}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 560, "expected_total_attractions": 1120, "reported_total_attractions": 960, "meal_per_person_cost_sum": 597, "expected_total_meals": 1194, "reported_total_meals": 1284, "reported_total_transportation": 1000}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 560, "expected_total_attractions": 1120, "reported_total_attractions": 960, "meal_per_person_cost_sum": 597, "expected_total_meals": 1194, "reported_total_meals": 1284, "reported_total_transportation": 1000}}]`

### v3_harder_pref_fix_eval_000009
- request: 苏州 2026-04-29->2026-05-02 days=4 transport=打车 hotel=亲子酒店 prefs=['亲子', '老人友好', '博物馆', '城市公园', '特色餐厅']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 215, "expected_total_attractions": 860, "reported_total_attractions": 1160, "meal_per_person_cost_sum": 768, "expected_total_meals": 3072, "reported_total_meals": 2768, "reported_total_transportation": 1200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 215, "expected_total_attractions": 860, "reported_total_attractions": 1160, "meal_per_person_cost_sum": 768, "expected_total_meals": 3072, "reported_total_meals": 2768, "reported_total_transportation": 1200}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": false, "meal_cost_scale_ok": true, "budget_relationship_ok": false, "expected_total_hotels": 7500, "reported_total_hotels": 7500, "expected_total_attractions": 860, "reported_total_attractions": 1160, "meal_scale_eval": {"ok": true, "party_total": 4, "budget_level": "comfortable", "per_person_lunch_dinner_floor": 50, "per_person_breakfast_floor": 20, "meal_count": 12, "checked_count": 8, "failure_count": 0, "failures": []}}}]`

### v3_harder_pref_fix_eval_000011
- request: 福州 2026-06-20->2026-06-23 days=4 transport=打车 hotel=高端酒店 prefs=['高端酒店', '艺术', '特色餐厅', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 2, "room_count": 1, "priced_nights": 3, "expected_min_total_hotels": 2250, "reported_total_hotels": 4500, "diff": 2250, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 197, "expected_total_attractions": 394, "reported_total_attractions": 320, "meal_per_person_cost_sum": 1058, "expected_total_meals": 2116, "reported_total_meals": 3164, "reported_total_transportation": 1200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 197, "expected_total_attractions": 394, "reported_total_attractions": 320, "meal_per_person_cost_sum": 1058, "expected_total_meals": 2116, "reported_total_meals": 3164, "reported_total_transportation": 1200}}]`

### v3_harder_pref_fix_eval_000001
- request: 桂林 2026-09-03->2026-09-06 days=4 transport=打车 hotel=高端酒店 prefs=['高端酒店', '艺术', '特色餐厅', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "广西省立艺术馆", "count": 5, "max_allowed": 1, "occurrences": [{"date": "2026-09-03", "day_index": 0, "name": "广西省立艺术馆"}, {"date": "2026-09-04", "day_index": 1, "name": "广西省立艺术馆"}, {"date": "2026-09-05", "day_index": 2, "name": "广西省立艺术馆"}, {"date": "2026-09-05", "day_index": 2, "name": "广西省立艺术馆"}, {"date": "2026-09-06", "day_index": 3, "name": "广西省立艺术馆"}]}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "阿甘酒家", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-09-03", "type": "lunch", "name": "阿甘酒家(解西店)"}, {"date": "2026-09-04", "type": "lunch", "name": "阿甘酒家(依仁店)"}, {"date": "2026-09-05", "type": "lunch", "name": "阿甘酒家(依仁店)"}, {"date": "2026-09-06", "type": "lunch", "name": "阿甘酒家(解西店)"}]}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 2, "room_count": 1, "priced_nights": 3, "expected_min_total_hotels": 3600, "reported_total_hotels": 7200, "diff": 3600, "covers_nights": false}}]`

### v3_harder_pref_fix_eval_000013
- request: 武汉 2026-05-08->2026-05-12 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "汉口江滩", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-05-10", "day_index": 2, "name": "汉口江滩"}, {"date": "2026-05-12", "day_index": 4, "name": "汉口江滩"}]}]}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 3300, "total": 3200, "diff": 100, "requested_budget": {"available": true, "amount": 5800, "scope": "total", "party_size": 2, "total": 5800, "source": "budget_constraint", "budget_level": "standard", "strictness": "hard"}, "per_person_day": 320.0, "budget_level": "standard", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "standard", "strictness": "hard", "amount": 5800, "target_min_ratio": 0.55, "target_max_ratio": 1.0, "target_min_total": 3200, "target_max_total": 5800, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 4, "party_total": 2, "room_count": 1, "priced_nights": 4, "expected_min_total_hotels": 1600, "reported_total_hotels": 1600, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 210, "expected_total_attractions": 420, "reported_total_attractions": 340, "meal_per_person_cost_sum": 951, "expected_total_meals": 1902, "reported_total_meals": 1260, "reported_total_transportation": 100}}]`

### v3_harder_pref_fix_eval_000003
- request: 西安 2025-05-06->2025-05-10 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "西安博物院", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2025-05-06", "day_index": 0, "name": "西安博物院"}, {"date": "2025-05-10", "day_index": 4, "name": "西安博物院"}]}, {"name_key": "陕西历史博物馆", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2025-05-07", "day_index": 1, "name": "陕西历史博物馆"}, {"date": "2025-05-09", "day_index": 3, "name": "陕西历史博物馆"}]}]}, {"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2025-05-09", "lunch": "苏福记(高新店)", "dinner": "苏福记(金萨店)"}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 4, "party_total": 2, "room_count": 1, "priced_nights": 4, "expected_min_total_hotels": 1800, "reported_total_hotels": 3600, "diff": 1800, "covers_nights": false}}]`

### v3_harder_pref_fix_eval_000010
- request: 西安 2026-08-04->2026-08-08 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "西安博物院", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-08-07", "day_index": 3, "name": "西安博物院"}, {"date": "2026-08-08", "day_index": 4, "name": "西安博物院"}]}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "奔跑吧陕菜·常来长安", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-08-04", "type": "lunch", "name": "奔跑吧陕菜·常来长安(钟楼南大街店)"}, {"date": "2026-08-06", "type": "lunch", "name": "奔跑吧陕菜·常来长安(钟楼南大街店)"}, {"date": "2026-08-07", "type": "dinner", "name": "奔跑吧陕菜·常来长安(钟楼南大街店)"}, {"date": "2026-08-08", "type": "lunch", "name": "奔跑吧陕菜·常来长安(钟楼南大街店)"}]}, {"name_key": "奔跑吧陕菜·雁塔长安", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-08-04", "type": "dinner", "name": "奔跑吧陕菜·雁塔长安(大雁塔店)"}, {"date": "2026-08-05", "type": "lunch", "name": "奔跑吧陕菜·雁塔长安(大雁塔店)"}, {"date": "2026-08-07", "type": "lunch", "name": "奔跑吧陕菜·雁塔长安(大雁塔店)"}, {"date": "2026-08-08", "type": "dinner", "name": "奔跑吧陕菜·雁塔长安(大雁塔店)"}]}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 4, "party_total": 5, "room_count": 3, "priced_nights": 4, "expected_min_total_hotels": 5400, "reported_total_hotels": 3600, "diff": -1800, "covers_nights": false}}]`

### v3_harder_pref_fix_eval_000017
- request: 苏州 2026-05-08->2026-05-12 days=5 transport=公共交通 hotel=民宿 prefs=['小众展馆', '咖啡', '艺术', '城市漫步', '特色餐厅']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "稻山村·苏州菜", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-05-09", "type": "dinner", "name": "稻山村·苏州菜(石路店)"}, {"date": "2026-05-10", "type": "lunch", "name": "稻山村·苏州菜(石路店)"}, {"date": "2026-05-11", "type": "lunch", "name": "稻山村·苏州菜(石路店)"}, {"date": "2026-05-12", "type": "lunch", "name": "稻山村·苏州菜(石路店)"}]}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 4, "party_total": 2, "room_count": 1, "priced_nights": 4, "expected_min_total_hotels": 1200, "reported_total_hotels": 2400, "diff": 1200, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 207, "expected_total_attractions": 414, "reported_total_attractions": 360, "meal_per_person_cost_sum": 718, "expected_total_meals": 1436, "reported_total_meals": 2172, "reported_total_transportation": 400}}]`

### v3_harder_pref_fix_eval_000018
- request: 天津 2026-07-05->2026-07-07 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物']
- errors: `[{"stage": "schema", "message": "3 validation errors for TripPlan\ndays.2.attractions.2.address\n  Input should be a valid string [type=string_type, input_value=None, input_type=NoneType]\n    For further information visit https://errors.pydantic.dev/2.12/v/string_type\ndays.2.attractions.2.location\n  Input should be a valid dictionary or instance of Location [type=model_type, input_value=None, input_type=NoneType]\n    For further information visit https://errors.pydantic.dev/2.12/v/model_type\ndays.2.attractions.2.visit_duration\n  Field required [type=missing, input_value={'name': '南楼煎饼(...one, 'ticket_price': 18}, input_type=dict]\n    For further information visit https://errors.pydantic.dev/2.12/v/missing"}]`

### v3_harder_pref_fix_eval_000008
- request: 大理 2026-05-10->2026-05-12 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 7149, "total": 6149, "diff": 1000, "requested_budget": {"available": true, "amount": 9800, "scope": "total", "party_size": 3, "total": 9800, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "hard"}, "per_person_day": 683.22, "budget_level": "comfortable", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "hard", "amount": 9800, "target_min_ratio": 0.65, "target_max_ratio": 1.0, "target_min_total": 6400, "target_max_total": 9800, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 3, "room_count": 2, "priced_nights": 2, "expected_min_total_hotels": 3000, "reported_total_hotels": 3000, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 75, "expected_total_attractions": 225, "reported_total_attractions": 750, "meal_per_person_cost_sum": 432, "expected_total_meals": 1296, "reported_total_meals": 1899, "reported_total_transportation": 1500}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 75, "expected_total_attractions": 225, "reported_total_attractions": 750, "meal_per_person_cost_sum": 432, "expected_total_meals": 1296, "reported_total_meals": 1899, "reported_total_transportation": 1500}}]`

### v3_harder_pref_fix_eval_000000
- request: 昆明 2026-04-06->2026-04-10 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 4, "party_total": 5, "room_count": 3, "priced_nights": 4, "expected_min_total_hotels": 4800, "reported_total_hotels": 3200, "diff": -1600, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 5, "hotel_room_count": 3, "attraction_ticket_sum": 285, "expected_total_attractions": 1425, "reported_total_attractions": 1700, "meal_per_person_cost_sum": 867, "expected_total_meals": 4335, "reported_total_meals": 3950, "reported_total_transportation": 1000}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 5, "hotel_room_count": 3, "attraction_ticket_sum": 285, "expected_total_attractions": 1425, "reported_total_attractions": 1700, "meal_per_person_cost_sum": 867, "expected_total_meals": 4335, "reported_total_meals": 3950, "reported_total_transportation": 1000}}]`

### v3_harder_pref_fix_eval_000023
- request: 大理 2026-09-03->2026-09-07 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食']
- errors: `[{"stage": "schema", "message": "3 validation errors for TripPlan\ndays.3.attractions.1.address\n  Input should be a valid string [type=string_type, input_value=None, input_type=NoneType]\n    For further information visit https://errors.pydantic.dev/2.12/v/string_type\ndays.3.attractions.1.location\n  Input should be a valid dictionary or instance of Location [type=model_type, input_value=None, input_type=NoneType]\n    For further information visit https://errors.pydantic.dev/2.12/v/model_type\ndays.3.attractions.1.visit_duration\n  Field required [type=missing, input_value={'name': '白族民居', ...None, 'ticket_price': 0}, input_type=dict]\n    For further information visit https://errors.pydantic.dev/2.12/v/missing"}]`

### v3_harder_pref_fix_eval_000002
- request: 杭州 2026-04-30->2026-05-03 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '夜市', '老字号', '城市漫步']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 250, "expected_total_attractions": 1000, "reported_total_attractions": 632, "meal_per_person_cost_sum": 821, "expected_total_meals": 3284, "reported_total_meals": 1848, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 250, "expected_total_attractions": 1000, "reported_total_attractions": 632, "meal_per_person_cost_sum": 821, "expected_total_meals": 3284, "reported_total_meals": 1848, "reported_total_transportation": 200}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": false, "meal_cost_scale_ok": true, "budget_relationship_ok": false, "expected_total_hotels": 1500, "reported_total_hotels": 1500, "expected_total_attractions": 1000, "reported_total_attractions": 632, "meal_scale_eval": {"ok": true, "party_total": 4, "budget_level": "limited", "per_person_lunch_dinner_floor": 25, "per_person_breakfast_floor": 10, "meal_count": 12, "checked_count": 12, "failure_count": 0, "failures": []}}}]`

### v3_harder_pref_fix_eval_000006
- request: 南京 2026-07-05->2026-07-08 days=4 transport=自驾 hotel=亲子酒店 prefs=['亲子', '动物园', '海洋馆', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "南京博物院", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-07-06", "day_index": 1, "name": "南京博物院"}, {"date": "2026-07-08", "day_index": 3, "name": "南京博物院"}]}]}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 5709, "total": 6609, "diff": -900, "requested_budget": {"available": true, "amount": 7600, "scope": "total", "party_size": 3, "total": 7600, "source": "budget_constraint", "budget_level": "standard", "strictness": "hard"}, "per_person_day": 550.75, "budget_level": "standard", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "standard", "strictness": "hard", "amount": 7600, "target_min_ratio": 0.55, "target_max_ratio": 1.0, "target_min_total": 4200, "target_max_total": 7600, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 3, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 3300, "reported_total_hotels": 3300, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 65, "expected_total_attractions": 195, "reported_total_attractions": 255, "meal_per_person_cost_sum": 752, "expected_total_meals": 2256, "reported_total_meals": 1854, "reported_total_transportation": 300}}]`

### v3_harder_pref_fix_eval_000015
- request: 南京 2026-04-06->2026-04-10 days=5 transport=公共交通 hotel=民宿 prefs=['摄影', '自然风光', '城市漫步', '本地菜']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "玄武湖景区", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-04-06", "day_index": 0, "name": "玄武湖景区"}, {"date": "2026-04-10", "day_index": 4, "name": "玄武湖景区"}]}, {"name_key": "古鸡鸣寺", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-04-06", "day_index": 0, "name": "古鸡鸣寺"}, {"date": "2026-04-10", "day_index": 4, "name": "古鸡鸣寺"}]}]}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 2706, "total": 2606, "diff": 100, "requested_budget": {"available": true, "amount": 3400, "scope": "total", "party_size": 1, "total": 3400, "source": "budget_constraint", "budget_level": "standard", "strictness": "hard"}, "per_person_day": 521.2, "budget_level": "standard", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "standard", "strictness": "hard", "amount": 3400, "target_min_ratio": 0.55, "target_max_ratio": 1.0, "target_min_total": 1900, "target_max_total": 3400, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 4, "party_total": 1, "room_count": 1, "priced_nights": 4, "expected_min_total_hotels": 1200, "reported_total_hotels": 1200, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 85, "expected_total_attractions": 85, "reported_total_attractions": 115, "meal_per_person_cost_sum": 1053, "expected_total_meals": 1053, "reported_total_meals": 1191, "reported_total_transportation": 200}}]`

### v3_harder_pref_fix_eval_000031
- request: 成都 2026-05-10->2026-05-13 days=4 transport=打车 hotel=高端酒店 prefs=['高端酒店', '艺术', '特色餐厅', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 2, "room_count": 1, "priced_nights": 3, "expected_min_total_hotels": 2400, "reported_total_hotels": 4800, "diff": 2400, "covers_nights": false}}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 10984, "total": 11984, "diff": -1000, "requested_budget": {"available": true, "amount": 13100, "scope": "total", "party_size": 2, "total": 13100, "source": "budget_constraint", "budget_level": "premium", "strictness": "soft"}, "per_person_day": 1498.0, "budget_level": "premium", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "premium", "strictness": "soft", "amount": 13100, "target_min_ratio": 0.7, "target_max_ratio": 1.12, "target_min_total": 9200, "target_max_total": 14700, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 2, "room_count": 1, "priced_nights": 3, "expected_min_total_hotels": 2400, "reported_total_hotels": 4800, "diff": 2400, "covers_nights": false}, "hotel_budget_covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 190, "expected_total_attractions": 380, "reported_total_attractions": 320, "meal_per_person_cost_sum": 1536, "expected_total_meals": 3072, "reported_total_meals": 4664, "reported_total_transportation": 1200}}]`

### v3_harder_pref_fix_eval_000016
- request: 苏州 2026-06-05->2026-06-08 days=4 transport=自驾 hotel=亲子酒店 prefs=['亲子', '动物园', '海洋馆', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 3, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 7500, "reported_total_hotels": 3750, "diff": -3750, "covers_nights": false}}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 6800, "total": 7700, "diff": -900, "requested_budget": {"available": true, "amount": 7600, "scope": "total", "party_size": 3, "total": 7600, "source": "budget_constraint", "budget_level": "standard", "strictness": "hard"}, "per_person_day": 641.67, "budget_level": "standard", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "standard", "strictness": "hard", "amount": 7600, "target_min_ratio": 0.55, "target_max_ratio": 1.0, "target_min_total": 4200, "target_max_total": 7600, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": false, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 3, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 7500, "reported_total_hotels": 3750, "diff": -3750, "covers_nights": false}, "hotel_budget_covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 70, "expected_total_attractions": 210, "reported_total_attractions": 315, "meal_per_person_cost_sum": 661, "expected_total_meals": 1983, "reported_total_meals": 1735, "reported_total_transportation": 1000}}]`

### v3_harder_pref_fix_eval_000020
- request: 杭州 2026-06-20->2026-06-24 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 4, "party_total": 5, "room_count": 3, "priced_nights": 4, "expected_min_total_hotels": 6000, "reported_total_hotels": 4000, "diff": -2000, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 5, "hotel_room_count": 3, "attraction_ticket_sum": 160, "expected_total_attractions": 800, "reported_total_attractions": 150, "meal_per_person_cost_sum": 1155, "expected_total_meals": 5775, "reported_total_meals": 3275, "reported_total_transportation": 1000}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 5, "hotel_room_count": 3, "attraction_ticket_sum": 160, "expected_total_attractions": 800, "reported_total_attractions": 150, "meal_per_person_cost_sum": 1155, "expected_total_meals": 5775, "reported_total_meals": 3275, "reported_total_transportation": 1000}}]`
