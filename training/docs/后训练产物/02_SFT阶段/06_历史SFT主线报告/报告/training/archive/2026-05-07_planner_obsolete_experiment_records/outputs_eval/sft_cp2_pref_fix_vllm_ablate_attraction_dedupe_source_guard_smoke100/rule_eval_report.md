# Rule Eval Report: sft_cp2_pref_fix_vllm_ablate_attraction_dedupe_source_guard_smoke100

- records: 100
- generations: `training/outputs/eval/sft_cp2_pref_fix_vllm_ablate_attraction_dedupe_source_guard_smoke100/generations.jsonl`
- records_path: `training/data/v3/eval_harder_pref_fix_attraction_prompt_ablation_attraction_dedupe_source_guard_no_route/records.jsonl`

## Boolean Metrics

| Metric | Pass | Total | Rate |
| --- | ---: | ---: | ---: |
| accommodation_type_ok | 99 | 99 | 100.00% |
| attraction_budget_consistent | 12 | 99 | 12.12% |
| attraction_budget_party_relation_ok | 40 | 99 | 40.40% |
| attraction_count_ok | 98 | 99 | 98.99% |
| attraction_diversity_ok | 51 | 99 | 51.52% |
| attraction_grounding_ok | 94 | 99 | 94.95% |
| attraction_repeat_limit_ok | 51 | 99 | 51.52% |
| budget_arithmetic_consistent | 70 | 99 | 70.71% |
| budget_consistent | 70 | 99 | 70.71% |
| budget_level_aligned | 67 | 99 | 67.68% |
| budget_preference_aligned | 67 | 99 | 67.68% |
| budget_relationship_ok | 11 | 99 | 11.11% |
| budget_selection_ok | 51 | 99 | 51.52% |
| budget_user_constraint_ok | 97 | 99 | 97.98% |
| budget_within_user_budget | 99 | 99 | 100.00% |
| city_ok | 99 | 99 | 100.00% |
| date_range_ok | 99 | 99 | 100.00% |
| day_dates_ok | 99 | 99 | 100.00% |
| day_index_ok | 99 | 99 | 100.00% |
| days_len_ok | 99 | 99 | 100.00% |
| dpo_soft_pass | 24 | 99 | 24.24% |
| dpo_soft_recomputed_budget_pass | 18 | 99 | 18.18% |
| hard_pass | 89 | 99 | 89.90% |
| hotel_budget_covers_nights | 60 | 99 | 60.61% |
| hotel_budget_relation_ok | 61 | 99 | 61.62% |
| hotel_distance_placeholder_ok | 99 | 99 | 100.00% |
| hotel_grounding_ok | 98 | 99 | 98.99% |
| invalid_hotel_name_ok | 99 | 99 | 100.00% |
| json_extract_ok | 100 | 100 | 100.00% |
| legacy_hard_pass | 21 | 99 | 21.21% |
| location_object_ok | 99 | 99 | 100.00% |
| meal_budget_consistent | 0 | 99 | 0.00% |
| meal_complete | 99 | 99 | 100.00% |
| meal_cost_scale_ok | 37 | 99 | 37.37% |
| meal_diversity_ok | 61 | 99 | 61.62% |
| meal_grounding_ok | 94 | 99 | 94.95% |
| meal_lunch_dinner_same_day_ok | 81 | 99 | 81.82% |
| meal_repeat_limit_ok | 72 | 99 | 72.73% |
| meal_specific_ok | 98 | 99 | 98.99% |
| meal_valid_semantics_ok | 95 | 99 | 95.96% |
| middle_hotel_ok | 99 | 99 | 100.00% |
| recomputed_budget_fit_ok | 51 | 99 | 51.52% |
| recomputed_budget_hard_ok | 85 | 99 | 85.86% |
| recomputed_budget_level_aligned | 51 | 99 | 51.52% |
| recomputed_budget_preference_aligned | 51 | 99 | 51.52% |
| recomputed_budget_user_constraint_ok | 85 | 99 | 85.86% |
| recomputed_budget_within_user_budget | 94 | 99 | 94.95% |
| schema_ok | 99 | 100 | 99.00% |
| sft_budget_semantic_hard_pass | 11 | 99 | 11.11% |
| sft_hard_pass | 89 | 99 | 89.90% |
| sft_no_budget_sum_hard_pass | 89 | 99 | 89.90% |
| sft_strict_hard_pass | 0 | 99 | 0.00% |
| transportation_budget_nonnegative | 99 | 99 | 100.00% |
| weather_dates_ok | 99 | 99 | 100.00% |
| weather_match | 99 | 99 | 100.00% |

## Numeric Metrics

```json
{
  "attraction_diversity_unique_rate": {
    "avg": 0.9211,
    "p50": 1.0,
    "p90": 1.0
  },
  "attraction_grounding_rate": {
    "avg": 0.9942,
    "p50": 1.0,
    "p90": 1.0
  },
  "hotel_grounding_rate": {
    "avg": 0.9899,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_diversity_unique_rate": {
    "avg": 0.7199,
    "p50": 0.75,
    "p90": 1.0
  },
  "meal_food_pois_grounding_rate": {
    "avg": 0.9934,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_grounding_rate": {
    "avg": 0.9934,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_semantic_valid_rate": {
    "avg": 0.9943,
    "p50": 1.0,
    "p90": 1.0
  },
  "recomputed_budget_per_person_day": {
    "avg": 588.7859,
    "p50": 574.5,
    "p90": 786.42
  },
  "recomputed_budget_total": {
    "avg": 6474.7677,
    "p50": 6177.0,
    "p90": 11145.0
  }
}
```

## Failure Types

```json
{
  "meal_budget_inconsistent": 99,
  "budget_relationship_mismatch": 88,
  "attraction_budget_inconsistent": 87,
  "meal_cost_scale_too_low": 62,
  "attraction_repeat_too_many": 48,
  "hotel_budget_underestimated": 39,
  "budget_preference_mismatch": 32,
  "budget_arithmetic_inconsistent": 29,
  "meal_repeat_too_many": 27,
  "meal_same_day_lunch_dinner_repeat": 18,
  "meal_invalid_name": 4,
  "budget_hard_constraint_exceeded": 2,
  "schema": 1,
  "meal_placeholder": 1,
  "meal_grounding_miss": 1,
  "too_many_attractions": 1
}
```

## Failure Examples

### v3_harder_pref_fix_eval_000004
- request: 张家界 2026-05-10->2026-05-12 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 2034, "total": 1934, "diff": 100, "requested_budget": {"available": true, "amount": 2500, "scope": "total", "party_size": 1, "total": 2500, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "hard"}, "per_person_day": 644.67, "budget_level": "comfortable", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "hard", "amount": 2500, "target_min_ratio": 0.65, "target_max_ratio": 1.0, "target_min_total": 1600, "target_max_total": 2500, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 1, "room_count": 1, "priced_nights": 2, "expected_min_total_hotels": 800, "reported_total_hotels": 800, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 160, "expected_total_attractions": 160, "reported_total_attractions": 160, "meal_per_person_cost_sum": 510, "expected_total_meals": 510, "reported_total_meals": 774, "reported_total_transportation": 300}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": true, "meal_cost_scale_ok": false, "budget_relationship_ok": false, "expected_total_hotels": 800, "reported_total_hotels": 800, "expected_total_attractions": 160, "reported_total_attractions": 160, "meal_scale_eval": {"ok": false, "party_total": 1, "budget_level": "comfortable", "per_person_lunch_dinner_floor": 50, "per_person_breakfast_floor": 20, "meal_count": 9, "checked_count": 9, "failure_count": 1, "failures": [{"date": "2026-05-12", "type": "breakfast", "name": "家旺小吃(解放路店)", "estimated_cost": 13, "min_expected_cost": 20}]}}}]`

### v3_harder_pref_fix_eval_000014
- request: 成都 2026-06-05->2026-06-07 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 165, "expected_total_attractions": 165, "reported_total_attractions": 335, "meal_per_person_cost_sum": 679, "expected_total_meals": 679, "reported_total_meals": 1092, "reported_total_transportation": 300}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 165, "expected_total_attractions": 165, "reported_total_attractions": 335, "meal_per_person_cost_sum": 679, "expected_total_meals": 679, "reported_total_meals": 1092, "reported_total_transportation": 300}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": false, "meal_cost_scale_ok": false, "budget_relationship_ok": false, "expected_total_hotels": 900, "reported_total_hotels": 900, "expected_total_attractions": 165, "reported_total_attractions": 335, "meal_scale_eval": {"ok": false, "party_total": 1, "budget_level": "comfortable", "per_person_lunch_dinner_floor": 50, "per_person_breakfast_floor": 20, "meal_count": 9, "checked_count": 9, "failure_count": 1, "failures": [{"date": "2026-06-05", "type": "breakfast", "name": "纯阳馆鱼香排骨面(吉祥街店)", "estimated_cost": 17, "min_expected_cost": 20}]}}}]`

### v3_harder_pref_fix_eval_000019
- request: 丽江 2026-05-10->2026-05-13 days=4 transport=打车 hotel=亲子酒店 prefs=['亲子', '老人友好', '博物馆', '城市公园', '特色餐厅']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "束河古镇", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-05-11", "day_index": 1, "name": "束河古镇"}, {"date": "2026-05-13", "day_index": 3, "name": "束河古镇"}]}, {"name_key": "丽江古道藏家博物馆", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-05-11", "day_index": 1, "name": "丽江古道藏家博物馆"}, {"date": "2026-05-12", "day_index": 2, "name": "丽江古道藏家博物馆"}]}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 640, "expected_total_attractions": 1280, "reported_total_attractions": 960, "meal_per_person_cost_sum": 611, "expected_total_meals": 1222, "reported_total_meals": 1284, "reported_total_transportation": 1200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 640, "expected_total_attractions": 1280, "reported_total_attractions": 960, "meal_per_person_cost_sum": 611, "expected_total_meals": 1222, "reported_total_meals": 1284, "reported_total_transportation": 1200}}]`

### v3_harder_pref_fix_eval_000009
- request: 苏州 2026-04-29->2026-05-02 days=4 transport=打车 hotel=亲子酒店 prefs=['亲子', '老人友好', '博物馆', '城市公园', '特色餐厅']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 11594, "total": 10594, "diff": 1000, "requested_budget": {"available": true, "amount": 15700, "scope": "total", "party_size": 4, "total": 15700, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "soft"}, "per_person_day": 662.12, "budget_level": "comfortable", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "soft", "amount": 15700, "target_min_ratio": 0.65, "target_max_ratio": 1.05, "target_min_total": 10200, "target_max_total": 16500, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 4, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 7500, "reported_total_hotels": 7500, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 140, "expected_total_attractions": 560, "reported_total_attractions": 110, "meal_per_person_cost_sum": 770, "expected_total_meals": 3080, "reported_total_meals": 2784, "reported_total_transportation": 1200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 140, "expected_total_attractions": 560, "reported_total_attractions": 110, "meal_per_person_cost_sum": 770, "expected_total_meals": 3080, "reported_total_meals": 2784, "reported_total_transportation": 1200}}]`

### v3_harder_pref_fix_eval_000001
- request: 桂林 2026-09-03->2026-09-06 days=4 transport=打车 hotel=高端酒店 prefs=['高端酒店', '艺术', '特色餐厅', '城市地标', '休闲慢游']
- errors: `[{"stage": "schema", "message": "6 validation errors for TripPlan\ndays.1.attractions.2.address\n  Input should be a valid string [type=string_type, input_value=None, input_type=NoneType]\n    For further information visit https://errors.pydantic.dev/2.12/v/string_type\ndays.1.attractions.2.location\n  Input should be a valid dictionary or instance of Location [type=model_type, input_value=None, input_type=NoneType]\n    For further information visit https://errors.pydantic.dev/2.12/v/model_type\ndays.1.attractions.2.visit_duration\n  Field required [type=missing, input_value={'name': '水云轩(知...one, 'ticket_price': 82}, input_type=dict]\n    For further information visit https://errors.pydantic.dev/2.12/v/missing\ndays.2.attractions.2.address\n  Input should be a valid string [type=string_type, input_value=None, input_type=NoneType]\n    For further information visit https://errors.pydantic.dev/2.12/v/string_type\ndays.2.attractions.2.location\n  Input should be a valid dictionary or instance of Location [type=model_type, input_value=None, input_type=NoneType]\n    For further information visit https://errors.pydantic.dev/2.12/v/model_type\ndays.2.attractions.2.visit_duration\n  Field required [type=missing, input_value={'name': '椿记烧鹅(...one, 'ticket_price': 56}, input_type=dict]\n    For further information visit https://errors.pydantic.dev/2.12/v/missing"}]`

### v3_harder_pref_fix_eval_000011
- request: 福州 2026-06-20->2026-06-23 days=4 transport=打车 hotel=高端酒店 prefs=['高端酒店', '艺术', '特色餐厅', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "福州烟台山商业漫步街区", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-06-21", "day_index": 1, "name": "福州烟台山商业漫步街区"}, {"date": "2026-06-23", "day_index": 3, "name": "福州烟台山商业漫步街区"}]}]}, {"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-06-21", "lunch": "紫阳海鲜楼·传承闽味(长乐路总店)", "dinner": "紫阳海鲜楼·传承闽味(华林路店)"}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 2, "room_count": 1, "priced_nights": 3, "expected_min_total_hotels": 2250, "reported_total_hotels": 4500, "diff": 2250, "covers_nights": false}}]`

### v3_harder_pref_fix_eval_000003
- request: 西安 2025-05-06->2025-05-10 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2025-05-08", "lunch": "清真刚刚烤肉(芙蓉街店)", "dinner": "清真刚刚烤肉(小南门店)"}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 319, "expected_total_attractions": 638, "reported_total_attractions": 840, "meal_per_person_cost_sum": 731, "expected_total_meals": 1462, "reported_total_meals": 1140, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 319, "expected_total_attractions": 638, "reported_total_attractions": 840, "meal_per_person_cost_sum": 731, "expected_total_meals": 1462, "reported_total_meals": 1140, "reported_total_transportation": 200}}]`

### v3_harder_pref_fix_eval_000013
- request: 武汉 2026-05-08->2026-05-12 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-05-12", "lunch": "刘聋子牛肉粉馆(汉阳龙兴东街店)", "dinner": "刘聋子牛肉粉馆(光谷新竹路店)"}]}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 3300, "total": 3298, "diff": 2, "requested_budget": {"available": true, "amount": 5800, "scope": "total", "party_size": 2, "total": 5800, "source": "budget_constraint", "budget_level": "standard", "strictness": "hard"}, "per_person_day": 329.8, "budget_level": "standard", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "standard", "strictness": "hard", "amount": 5800, "target_min_ratio": 0.55, "target_max_ratio": 1.0, "target_min_total": 3200, "target_max_total": 5800, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 4, "party_total": 2, "room_count": 1, "priced_nights": 4, "expected_min_total_hotels": 1600, "reported_total_hotels": 1600, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 223, "expected_total_attractions": 446, "reported_total_attractions": 260, "meal_per_person_cost_sum": 896, "expected_total_meals": 1792, "reported_total_meals": 1184, "reported_total_transportation": 256}}]`

### v3_harder_pref_fix_eval_000017
- request: 苏州 2026-05-08->2026-05-12 days=5 transport=公共交通 hotel=民宿 prefs=['小众展馆', '咖啡', '艺术', '城市漫步', '特色餐厅']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-05-10", "lunch": "稻山村·苏州菜(石路店)", "dinner": "稻山村·苏州菜(曼哈顿店)"}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 4, "party_total": 2, "room_count": 1, "priced_nights": 4, "expected_min_total_hotels": 1200, "reported_total_hotels": 2400, "diff": 1200, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 120, "expected_total_attractions": 240, "reported_total_attractions": 125, "meal_per_person_cost_sum": 659, "expected_total_meals": 1318, "reported_total_meals": 2232, "reported_total_transportation": 200}}]`

### v3_harder_pref_fix_eval_000010
- request: 西安 2026-08-04->2026-08-08 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "西安鼓楼", "count": 3, "max_allowed": 1, "occurrences": [{"date": "2026-08-04", "day_index": 0, "name": "西安鼓楼"}, {"date": "2026-08-07", "day_index": 3, "name": "西安鼓楼"}, {"date": "2026-08-08", "day_index": 4, "name": "西安鼓楼"}]}, {"name_key": "西安博物院", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-08-04", "day_index": 0, "name": "西安博物院"}, {"date": "2026-08-07", "day_index": 3, "name": "西安博物院"}]}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "奔跑吧陕菜·常来长安", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-08-04", "type": "lunch", "name": "奔跑吧陕菜·常来长安(钟楼南大街店)"}, {"date": "2026-08-06", "type": "lunch", "name": "奔跑吧陕菜·常来长安(钟楼南大街店)"}, {"date": "2026-08-07", "type": "dinner", "name": "奔跑吧陕菜·常来长安(钟楼南大街店)"}, {"date": "2026-08-08", "type": "lunch", "name": "奔跑吧陕菜·常来长安(钟楼南大街店)"}]}, {"name_key": "奔跑吧陕菜·雁塔长安", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-08-04", "type": "dinner", "name": "奔跑吧陕菜·雁塔长安(大雁塔店)"}, {"date": "2026-08-05", "type": "lunch", "name": "奔跑吧陕菜·雁塔长安(大雁塔店)"}, {"date": "2026-08-07", "type": "lunch", "name": "奔跑吧陕菜·雁塔长安(大雁塔店)"}, {"date": "2026-08-08", "type": "dinner", "name": "奔跑吧陕菜·雁塔长安(大雁塔店)"}]}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 4, "party_total": 5, "room_count": 3, "priced_nights": 4, "expected_min_total_hotels": 5400, "reported_total_hotels": 3600, "diff": -1800, "covers_nights": false}}]`

### v3_harder_pref_fix_eval_000018
- request: 天津 2026-07-05->2026-07-07 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "汉巴味德", "count": 3, "max_allowed": 2, "occurrences": [{"date": "2026-07-05", "type": "lunch", "name": "汉巴味德(乐宾百货店)"}, {"date": "2026-07-06", "type": "lunch", "name": "汉巴味德(乐宾百货店)"}, {"date": "2026-07-07", "type": "lunch", "name": "汉巴味德(乐宾百货店)"}]}]}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 80, "expected_total_attractions": 240, "reported_total_attractions": 240, "meal_per_person_cost_sum": 652, "expected_total_meals": 1956, "reported_total_meals": 1899, "reported_total_transportation": 1000}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": true, "meal_cost_scale_ok": false, "budget_relationship_ok": false, "expected_total_hotels": 3000, "reported_total_hotels": 3000, "expected_total_attractions": 240, "reported_total_attractions": 240, "meal_scale_eval": {"ok": false, "party_total": 3, "budget_level": "comfortable", "per_person_lunch_dinner_floor": 50, "per_person_breakfast_floor": 20, "meal_count": 9, "checked_count": 9, "failure_count": 1, "failures": [{"date": "2026-07-07", "type": "breakfast", "name": "南楼煎饼(滨江道店)", "estimated_cost": 14, "min_expected_cost": 20}]}}}]`

### v3_harder_pref_fix_eval_000008
- request: 大理 2026-05-10->2026-05-12 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物']
- errors: `[{"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 75, "expected_total_attractions": 225, "reported_total_attractions": 225, "meal_per_person_cost_sum": 385, "expected_total_meals": 1155, "reported_total_meals": 1665, "reported_total_transportation": 1200}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": true, "meal_cost_scale_ok": false, "budget_relationship_ok": false, "expected_total_hotels": 3000, "reported_total_hotels": 3000, "expected_total_attractions": 225, "reported_total_attractions": 225, "meal_scale_eval": {"ok": false, "party_total": 3, "budget_level": "comfortable", "per_person_lunch_dinner_floor": 50, "per_person_breakfast_floor": 20, "meal_count": 9, "checked_count": 9, "failure_count": 3, "failures": [{"date": "2026-05-10", "type": "breakfast", "name": "普通面包社", "estimated_cost": 19, "min_expected_cost": 20}, {"date": "2026-05-12", "type": "breakfast", "name": "九孃豌豆粉店", "estimated_cost": 9, "min_expected_cost": 20}, {"date": "2026-05-12", "type": "dinner", "name": "蒙自小黄牛米线(S湾海景店)", "estimated_cost": 19, "min_expected_cost": 50}]}}}, {"stage": "rule", "type": "meal_cost_scale_too_low", "details": {"ok": false, "party_total": 3, "budget_level": "comfortable", "per_person_lunch_dinner_floor": 50, "per_person_breakfast_floor": 20, "meal_count": 9, "checked_count": 9, "failure_count": 3, "failures": [{"date": "2026-05-10", "type": "breakfast", "name": "普通面包社", "estimated_cost": 19, "min_expected_cost": 20}, {"date": "2026-05-12", "type": "breakfast", "name": "九孃豌豆粉店", "estimated_cost": 9, "min_expected_cost": 20}, {"date": "2026-05-12", "type": "dinner", "name": "蒙自小黄牛米线(S湾海景店)", "estimated_cost": 19, "min_expected_cost": 50}]}}]`

### v3_harder_pref_fix_eval_000000
- request: 昆明 2026-04-06->2026-04-10 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "云南美术馆", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-04-06", "day_index": 0, "name": "云南美术馆(五一路)"}, {"date": "2026-04-10", "day_index": 4, "name": "云南美术馆(五一路)"}]}, {"name_key": "云南民族博物馆", "count": 3, "max_allowed": 1, "occurrences": [{"date": "2026-04-08", "day_index": 2, "name": "云南民族博物馆"}, {"date": "2026-04-09", "day_index": 3, "name": "云南民族博物馆"}, {"date": "2026-04-10", "day_index": 4, "name": "云南民族博物馆"}]}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 4, "party_total": 5, "room_count": 3, "priced_nights": 4, "expected_min_total_hotels": 4800, "reported_total_hotels": 3200, "diff": -1600, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 5, "hotel_room_count": 3, "attraction_ticket_sum": 210, "expected_total_attractions": 1050, "reported_total_attractions": 1200, "meal_per_person_cost_sum": 849, "expected_total_meals": 4245, "reported_total_meals": 3400, "reported_total_transportation": 1600}}]`

### v3_harder_pref_fix_eval_000023
- request: 大理 2026-09-03->2026-09-07 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "大理白族自治州博物馆", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-09-05", "day_index": 2, "name": "大理白族自治州博物馆"}, {"date": "2026-09-06", "day_index": 3, "name": "大理白族自治州博物馆"}]}]}, {"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-09-03", "type": "dinner", "name": "随园食单(善德居店)", "reason": "unknown_food_semantics"}, {"date": "2026-09-05", "type": "dinner", "name": "随园食单(善德居店)", "reason": "unknown_food_semantics"}, {"date": "2026-09-06", "type": "dinner", "name": "随园食单(善德居店)", "reason": "unknown_food_semantics"}, {"date": "2026-09-07", "type": "lunch", "name": "随园食单(善德居店)", "reason": "unknown_food_semantics"}, {"date": "2026-09-07", "type": "dinner", "name": "随园食单(善德居店)", "reason": "unknown_food_semantics"}]}, {"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-09-07", "lunch": "随园食单(善德居店)", "dinner": "随园食单(善德居店)"}]}]`

### v3_harder_pref_fix_eval_000002
- request: 杭州 2026-04-30->2026-05-03 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '夜市', '老字号', '城市漫步']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "泮芳春煎饺", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-04-30", "type": "breakfast", "name": "泮芳春煎饺(龙翔桥店)"}, {"date": "2026-05-01", "type": "breakfast", "name": "泮芳春煎饺(龙翔桥店)"}, {"date": "2026-05-02", "type": "breakfast", "name": "泮芳春煎饺(龙翔桥店)"}, {"date": "2026-05-03", "type": "breakfast", "name": "泮芳春煎饺(龙翔桥店)"}]}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 313, "expected_total_attractions": 1252, "reported_total_attractions": 436, "meal_per_person_cost_sum": 766, "expected_total_meals": 3064, "reported_total_meals": 1832, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 313, "expected_total_attractions": 1252, "reported_total_attractions": 436, "meal_per_person_cost_sum": 766, "expected_total_meals": 3064, "reported_total_meals": 1832, "reported_total_transportation": 200}}]`

### v3_harder_pref_fix_eval_000006
- request: 南京 2026-07-05->2026-07-08 days=4 transport=自驾 hotel=亲子酒店 prefs=['亲子', '动物园', '海洋馆', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "南京博物院", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-07-06", "day_index": 1, "name": "南京博物院"}, {"date": "2026-07-08", "day_index": 3, "name": "南京博物院"}]}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 175, "expected_total_attractions": 525, "reported_total_attractions": 370, "meal_per_person_cost_sum": 774, "expected_total_meals": 2322, "reported_total_meals": 1845, "reported_total_transportation": 500}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 175, "expected_total_attractions": 525, "reported_total_attractions": 370, "meal_per_person_cost_sum": 774, "expected_total_meals": 2322, "reported_total_meals": 1845, "reported_total_transportation": 500}}]`

### v3_harder_pref_fix_eval_000031
- request: 成都 2026-05-10->2026-05-13 days=4 transport=打车 hotel=高端酒店 prefs=['高端酒店', '艺术', '特色餐厅', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 2, "room_count": 1, "priced_nights": 3, "expected_min_total_hotels": 2400, "reported_total_hotels": 4800, "diff": 2400, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 240, "expected_total_attractions": 480, "reported_total_attractions": 1050, "meal_per_person_cost_sum": 1162, "expected_total_meals": 2324, "reported_total_meals": 3424, "reported_total_transportation": 1000}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 240, "expected_total_attractions": 480, "reported_total_attractions": 1050, "meal_per_person_cost_sum": 1162, "expected_total_meals": 2324, "reported_total_meals": 3424, "reported_total_transportation": 1000}}]`

### v3_harder_pref_fix_eval_000020
- request: 杭州 2026-06-20->2026-06-24 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 4, "party_total": 5, "room_count": 3, "priced_nights": 4, "expected_min_total_hotels": 6000, "reported_total_hotels": 4000, "diff": -2000, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 5, "hotel_room_count": 3, "attraction_ticket_sum": 110, "expected_total_attractions": 550, "reported_total_attractions": 150, "meal_per_person_cost_sum": 1182, "expected_total_meals": 5910, "reported_total_meals": 3295, "reported_total_transportation": 1000}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 5, "hotel_room_count": 3, "attraction_ticket_sum": 110, "expected_total_attractions": 550, "reported_total_attractions": 150, "meal_per_person_cost_sum": 1182, "expected_total_meals": 5910, "reported_total_meals": 3295, "reported_total_transportation": 1000}}]`

### v3_harder_pref_fix_eval_000015
- request: 南京 2026-04-06->2026-04-10 days=5 transport=公共交通 hotel=民宿 prefs=['摄影', '自然风光', '城市漫步', '本地菜']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "玄武湖景区", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-04-06", "day_index": 0, "name": "玄武湖景区"}, {"date": "2026-04-10", "day_index": 4, "name": "玄武湖景区"}]}]}, {"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-04-10", "lunch": "南京大牌档(1912总统府店)", "dinner": "南京大牌档(中山陵紫金坊店)"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "南京大牌档", "count": 6, "max_allowed": 3, "occurrences": [{"date": "2026-04-06", "type": "breakfast", "name": "南京大牌档(中山陵紫金坊店)"}, {"date": "2026-04-09", "type": "breakfast", "name": "南京大牌档(中山陵紫金坊店)"}, {"date": "2026-04-09", "type": "dinner", "name": "南京大牌档(中山陵紫金坊店)"}, {"date": "2026-04-10", "type": "breakfast", "name": "南京大牌档(中山陵紫金坊店)"}, {"date": "2026-04-10", "type": "lunch", "name": "南京大牌档(1912总统府店)"}, {"date": "2026-04-10", "type": "dinner", "name": "南京大牌档(中山陵紫金坊店)"}]}]}]`

### v3_harder_pref_fix_eval_000016
- request: 苏州 2026-06-05->2026-06-08 days=4 transport=自驾 hotel=亲子酒店 prefs=['亲子', '动物园', '海洋馆', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "稻山村·苏州菜", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-06-05", "type": "dinner", "name": "稻山村·苏州菜(石路店)"}, {"date": "2026-06-06", "type": "lunch", "name": "稻山村·苏州菜(曼哈顿店)"}, {"date": "2026-06-07", "type": "lunch", "name": "稻山村·苏州菜(石路店)"}, {"date": "2026-06-08", "type": "lunch", "name": "稻山村·苏州菜(曼哈顿店)"}]}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 3, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 7500, "reported_total_hotels": 3750, "diff": -3750, "covers_nights": false}}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 7700, "total": 7690, "diff": 10, "requested_budget": {"available": true, "amount": 7600, "scope": "total", "party_size": 3, "total": 7600, "source": "budget_constraint", "budget_level": "standard", "strictness": "hard"}, "per_person_day": 640.83, "budget_level": "standard", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "standard", "strictness": "hard", "amount": 7600, "target_min_ratio": 0.55, "target_max_ratio": 1.0, "target_min_total": 4200, "target_max_total": 7600, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": false, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 3, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 7500, "reported_total_hotels": 3750, "diff": -3750, "covers_nights": false}, "hotel_budget_covers_nights": false}}]`
