# Rule Eval Report: sft_cp2_pref_fix_vllm_original_smoke100

- records: 100
- generations: `training/outputs/eval/sft_cp2_pref_fix_vllm_original_smoke100/generations.jsonl`
- records_path: `training/data/v3/eval_harder_attraction_pref_fix_20260506/A_C/records.jsonl`

## Boolean Metrics

| Metric | Pass | Total | Rate |
| --- | ---: | ---: | ---: |
| accommodation_type_ok | 99 | 99 | 100.00% |
| attraction_budget_consistent | 10 | 99 | 10.10% |
| attraction_budget_party_relation_ok | 40 | 99 | 40.40% |
| attraction_count_ok | 97 | 99 | 97.98% |
| attraction_diversity_ok | 64 | 99 | 64.65% |
| attraction_grounding_ok | 94 | 99 | 94.95% |
| attraction_repeat_limit_ok | 64 | 99 | 64.65% |
| budget_arithmetic_consistent | 70 | 99 | 70.71% |
| budget_consistent | 70 | 99 | 70.71% |
| budget_level_aligned | 65 | 99 | 65.66% |
| budget_preference_aligned | 65 | 99 | 65.66% |
| budget_relationship_ok | 13 | 99 | 13.13% |
| budget_selection_ok | 49 | 99 | 49.49% |
| budget_user_constraint_ok | 91 | 99 | 91.92% |
| budget_within_user_budget | 98 | 99 | 98.99% |
| city_ok | 99 | 99 | 100.00% |
| date_range_ok | 99 | 99 | 100.00% |
| day_dates_ok | 99 | 99 | 100.00% |
| day_index_ok | 99 | 99 | 100.00% |
| days_len_ok | 99 | 99 | 100.00% |
| dpo_soft_pass | 32 | 99 | 32.32% |
| dpo_soft_recomputed_budget_pass | 25 | 99 | 25.25% |
| hard_pass | 87 | 99 | 87.88% |
| hotel_budget_covers_nights | 64 | 99 | 64.65% |
| hotel_budget_relation_ok | 66 | 99 | 66.67% |
| hotel_distance_placeholder_ok | 99 | 99 | 100.00% |
| hotel_grounding_ok | 98 | 99 | 98.99% |
| invalid_hotel_name_ok | 99 | 99 | 100.00% |
| json_extract_ok | 100 | 100 | 100.00% |
| legacy_hard_pass | 32 | 99 | 32.32% |
| location_object_ok | 99 | 99 | 100.00% |
| meal_budget_consistent | 0 | 99 | 0.00% |
| meal_complete | 99 | 99 | 100.00% |
| meal_cost_scale_ok | 36 | 99 | 36.36% |
| meal_diversity_ok | 63 | 99 | 63.64% |
| meal_grounding_ok | 93 | 99 | 93.94% |
| meal_lunch_dinner_same_day_ok | 84 | 99 | 84.85% |
| meal_repeat_limit_ok | 70 | 99 | 70.71% |
| meal_specific_ok | 98 | 99 | 98.99% |
| meal_valid_semantics_ok | 94 | 99 | 94.95% |
| middle_hotel_ok | 99 | 99 | 100.00% |
| recomputed_budget_fit_ok | 49 | 99 | 49.49% |
| recomputed_budget_hard_ok | 85 | 99 | 85.86% |
| recomputed_budget_level_aligned | 49 | 99 | 49.49% |
| recomputed_budget_preference_aligned | 49 | 99 | 49.49% |
| recomputed_budget_user_constraint_ok | 85 | 99 | 85.86% |
| recomputed_budget_within_user_budget | 97 | 99 | 97.98% |
| schema_ok | 99 | 100 | 99.00% |
| sft_budget_semantic_hard_pass | 9 | 99 | 9.09% |
| sft_hard_pass | 87 | 99 | 87.88% |
| sft_no_budget_sum_hard_pass | 87 | 99 | 87.88% |
| sft_strict_hard_pass | 0 | 99 | 0.00% |
| transportation_budget_nonnegative | 99 | 99 | 100.00% |
| weather_dates_ok | 99 | 99 | 100.00% |
| weather_match | 99 | 99 | 100.00% |

## Numeric Metrics

```json
{
  "attraction_diversity_unique_rate": {
    "avg": 0.9454,
    "p50": 1.0,
    "p90": 1.0
  },
  "attraction_grounding_rate": {
    "avg": 0.9951,
    "p50": 1.0,
    "p90": 1.0
  },
  "hotel_grounding_rate": {
    "avg": 0.9899,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_diversity_unique_rate": {
    "avg": 0.7567,
    "p50": 0.8,
    "p90": 1.0
  },
  "meal_food_pois_grounding_rate": {
    "avg": 0.9905,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_grounding_rate": {
    "avg": 0.9905,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_semantic_valid_rate": {
    "avg": 0.9913,
    "p50": 1.0,
    "p90": 1.0
  },
  "recomputed_budget_per_person_day": {
    "avg": 589.7008,
    "p50": 571.0,
    "p90": 791.0
  },
  "recomputed_budget_total": {
    "avg": 6478.6263,
    "p50": 6168.0,
    "p90": 11410.0
  }
}
```

## Failure Types

```json
{
  "meal_budget_inconsistent": 99,
  "attraction_budget_inconsistent": 89,
  "budget_relationship_mismatch": 86,
  "meal_cost_scale_too_low": 63,
  "attraction_repeat_too_many": 35,
  "hotel_budget_underestimated": 35,
  "budget_preference_mismatch": 34,
  "budget_arithmetic_inconsistent": 29,
  "meal_repeat_too_many": 29,
  "meal_same_day_lunch_dinner_repeat": 15,
  "budget_hard_constraint_exceeded": 8,
  "meal_invalid_name": 5,
  "too_many_attractions": 2,
  "schema": 1,
  "meal_placeholder": 1,
  "meal_grounding_miss": 1
}
```

## Failure Examples

### v3_harder_pref_fix_eval_000019
- request: 丽江 2026-05-10->2026-05-13 days=4 transport=打车 hotel=亲子酒店 prefs=['亲子', '老人友好', '博物馆', '城市公园', '特色餐厅']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "黑龙潭", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-05-10", "day_index": 0, "name": "黑龙潭"}, {"date": "2026-05-13", "day_index": 3, "name": "黑龙潭"}]}, {"name_key": "丽江古道藏家博物馆", "count": 3, "max_allowed": 1, "occurrences": [{"date": "2026-05-11", "day_index": 1, "name": "丽江古道藏家博物馆"}, {"date": "2026-05-12", "day_index": 2, "name": "丽江古道藏家博物馆"}, {"date": "2026-05-13", "day_index": 3, "name": "丽江古道藏家博物馆"}]}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 640, "expected_total_attractions": 1280, "reported_total_attractions": 960, "meal_per_person_cost_sum": 596, "expected_total_meals": 1192, "reported_total_meals": 1188, "reported_total_transportation": 1000}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 640, "expected_total_attractions": 1280, "reported_total_attractions": 960, "meal_per_person_cost_sum": 596, "expected_total_meals": 1192, "reported_total_meals": 1188, "reported_total_transportation": 1000}}]`

### v3_harder_pref_fix_eval_000004
- request: 张家界 2026-05-10->2026-05-12 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 1901, "total": 1801, "diff": 100, "requested_budget": {"available": true, "amount": 2500, "scope": "total", "party_size": 1, "total": 2500, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "hard"}, "per_person_day": 600.33, "budget_level": "comfortable", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "hard", "amount": 2500, "target_min_ratio": 0.65, "target_max_ratio": 1.0, "target_min_total": 1600, "target_max_total": 2500, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 1, "room_count": 1, "priced_nights": 2, "expected_min_total_hotels": 800, "reported_total_hotels": 800, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 160, "expected_total_attractions": 160, "reported_total_attractions": 240, "meal_per_person_cost_sum": 476, "expected_total_meals": 476, "reported_total_meals": 561, "reported_total_transportation": 300}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 160, "expected_total_attractions": 160, "reported_total_attractions": 240, "meal_per_person_cost_sum": 476, "expected_total_meals": 476, "reported_total_meals": 561, "reported_total_transportation": 300}}]`

### v3_harder_pref_fix_eval_000009
- request: 苏州 2026-04-29->2026-05-02 days=4 transport=打车 hotel=亲子酒店 prefs=['亲子', '老人友好', '博物馆', '城市公园', '特色餐厅']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 215, "expected_total_attractions": 860, "reported_total_attractions": 1140, "meal_per_person_cost_sum": 796, "expected_total_meals": 3184, "reported_total_meals": 3352, "reported_total_transportation": 1200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 215, "expected_total_attractions": 860, "reported_total_attractions": 1140, "meal_per_person_cost_sum": 796, "expected_total_meals": 3184, "reported_total_meals": 3352, "reported_total_transportation": 1200}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": false, "meal_cost_scale_ok": true, "budget_relationship_ok": false, "expected_total_hotels": 7500, "reported_total_hotels": 7500, "expected_total_attractions": 860, "reported_total_attractions": 1140, "meal_scale_eval": {"ok": true, "party_total": 4, "budget_level": "comfortable", "per_person_lunch_dinner_floor": 50, "per_person_breakfast_floor": 20, "meal_count": 12, "checked_count": 8, "failure_count": 0, "failures": []}}}]`

### v3_harder_pref_fix_eval_000010
- request: 西安 2026-08-04->2026-08-08 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "西安鼓楼", "count": 3, "max_allowed": 1, "occurrences": [{"date": "2026-08-04", "day_index": 0, "name": "西安鼓楼"}, {"date": "2026-08-06", "day_index": 2, "name": "西安鼓楼"}, {"date": "2026-08-07", "day_index": 3, "name": "西安鼓楼"}]}, {"name_key": "西安博物院", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-08-07", "day_index": 3, "name": "西安博物院"}, {"date": "2026-08-08", "day_index": 4, "name": "西安博物院"}]}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "奔跑吧陕菜·常来长安", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-08-04", "type": "lunch", "name": "奔跑吧陕菜·常来长安(钟楼南大街店)"}, {"date": "2026-08-06", "type": "lunch", "name": "奔跑吧陕菜·常来长安(钟楼南大街店)"}, {"date": "2026-08-07", "type": "lunch", "name": "奔跑吧陕菜·常来长安(钟楼南大街店)"}, {"date": "2026-08-08", "type": "lunch", "name": "奔跑吧陕菜·常来长安(钟楼南大街店)"}]}, {"name_key": "奔跑吧陕菜·雁塔长安", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-08-04", "type": "dinner", "name": "奔跑吧陕菜·雁塔长安(大雁塔店)"}, {"date": "2026-08-05", "type": "lunch", "name": "奔跑吧陕菜·雁塔长安(大雁塔店)"}, {"date": "2026-08-06", "type": "dinner", "name": "奔跑吧陕菜·雁塔长安(大雁塔店)"}, {"date": "2026-08-07", "type": "dinner", "name": "奔跑吧陕菜·雁塔长安(大雁塔店)"}, {"date": "2026-08-08", "type": "dinner", "name": "奔跑吧陕菜·雁塔长安(大雁塔店)"}]}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 4, "party_total": 5, "room_count": 3, "priced_nights": 4, "expected_min_total_hotels": 5400, "reported_total_hotels": 3600, "diff": -1800, "covers_nights": false}}]`

### v3_harder_pref_fix_eval_000001
- request: 桂林 2026-09-03->2026-09-06 days=4 transport=打车 hotel=高端酒店 prefs=['高端酒店', '艺术', '特色餐厅', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-09-04", "lunch": "水云轩(知味餐饮旗下品牌店)", "dinner": "水云轩(知味餐饮旗下品牌店)"}, {"date": "2026-09-05", "lunch": "椿记烧鹅(南溪店)", "dinner": "椿记烧鹅(南溪店)"}, {"date": "2026-09-06", "lunch": "蜜棠升明月江景餐厅", "dinner": "蜜棠升明月江景餐厅"}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 2, "room_count": 1, "priced_nights": 3, "expected_min_total_hotels": 3600, "reported_total_hotels": 7200, "diff": 3600, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 505, "expected_total_attractions": 1010, "reported_total_attractions": 1260, "meal_per_person_cost_sum": 794, "expected_total_meals": 1588, "reported_total_meals": 2480, "reported_total_transportation": 1200}}]`

### v3_harder_pref_fix_eval_000003
- request: 西安 2025-05-06->2025-05-10 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 259, "expected_total_attractions": 518, "reported_total_attractions": 620, "meal_per_person_cost_sum": 761, "expected_total_meals": 1522, "reported_total_meals": 1168, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 259, "expected_total_attractions": 518, "reported_total_attractions": 620, "meal_per_person_cost_sum": 761, "expected_total_meals": 1522, "reported_total_meals": 1168, "reported_total_transportation": 200}}]`

### v3_harder_pref_fix_eval_000013
- request: 武汉 2026-05-08->2026-05-12 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 3800, "total": 3700, "diff": 100, "requested_budget": {"available": true, "amount": 5800, "scope": "total", "party_size": 2, "total": 5800, "source": "budget_constraint", "budget_level": "standard", "strictness": "hard"}, "per_person_day": 370.0, "budget_level": "standard", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "standard", "strictness": "hard", "amount": 5800, "target_min_ratio": 0.55, "target_max_ratio": 1.0, "target_min_total": 3200, "target_max_total": 5800, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 4, "party_total": 2, "room_count": 1, "priced_nights": 4, "expected_min_total_hotels": 1600, "reported_total_hotels": 1600, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 210, "expected_total_attractions": 420, "reported_total_attractions": 340, "meal_per_person_cost_sum": 839, "expected_total_meals": 1678, "reported_total_meals": 1660, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 210, "expected_total_attractions": 420, "reported_total_attractions": 340, "meal_per_person_cost_sum": 839, "expected_total_meals": 1678, "reported_total_meals": 1660, "reported_total_transportation": 200}}]`

### v3_harder_pref_fix_eval_000014
- request: 成都 2026-06-05->2026-06-07 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 2680, "total": 2480, "diff": 200, "requested_budget": {"available": true, "amount": 3000, "scope": "total", "party_size": 1, "total": 3000, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "hard"}, "per_person_day": 826.67, "budget_level": "comfortable", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "hard", "amount": 3000, "target_min_ratio": 0.65, "target_max_ratio": 1.0, "target_min_total": 2000, "target_max_total": 3000, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 1, "room_count": 1, "priced_nights": 2, "expected_min_total_hotels": 900, "reported_total_hotels": 900, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 165, "expected_total_attractions": 165, "reported_total_attractions": 215, "meal_per_person_cost_sum": 620, "expected_total_meals": 620, "reported_total_meals": 1365, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 165, "expected_total_attractions": 165, "reported_total_attractions": 215, "meal_per_person_cost_sum": 620, "expected_total_meals": 620, "reported_total_meals": 1365, "reported_total_transportation": 200}}]`

### v3_harder_pref_fix_eval_000011
- request: 福州 2026-06-20->2026-06-23 days=4 transport=打车 hotel=高端酒店 prefs=['高端酒店', '艺术', '特色餐厅', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 2, "room_count": 1, "priced_nights": 3, "expected_min_total_hotels": 2250, "reported_total_hotels": 4500, "diff": 2250, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 117, "expected_total_attractions": 234, "reported_total_attractions": 154, "meal_per_person_cost_sum": 1012, "expected_total_meals": 2024, "reported_total_meals": 3156, "reported_total_transportation": 1200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 117, "expected_total_attractions": 234, "reported_total_attractions": 154, "meal_per_person_cost_sum": 1012, "expected_total_meals": 2024, "reported_total_meals": 3156, "reported_total_transportation": 1200}}]`

### v3_harder_pref_fix_eval_000017
- request: 苏州 2026-05-08->2026-05-12 days=5 transport=公共交通 hotel=民宿 prefs=['小众展馆', '咖啡', '艺术', '城市漫步', '特色餐厅']
- errors: `[{"stage": "schema", "message": "3 validation errors for TripPlan\ndays.2.attractions.2.address\n  Input should be a valid string [type=string_type, input_value=None, input_type=NoneType]\n    For further information visit https://errors.pydantic.dev/2.12/v/string_type\ndays.2.attractions.2.location\n  Input should be a valid dictionary or instance of Location [type=model_type, input_value=None, input_type=NoneType]\n    For further information visit https://errors.pydantic.dev/2.12/v/model_type\ndays.2.attractions.2.visit_duration\n  Field required [type=missing, input_value={'name': '西园寺素食...one, 'ticket_price': 16}, input_type=dict]\n    For further information visit https://errors.pydantic.dev/2.12/v/missing"}]`

### v3_harder_pref_fix_eval_000000
- request: 昆明 2026-04-06->2026-04-10 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "云南美术馆", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-04-08", "day_index": 2, "name": "云南美术馆(五一路)"}, {"date": "2026-04-10", "day_index": 4, "name": "云南美术馆(五一路)"}]}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "从水居餐厅.特色云南菜", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-04-06", "type": "lunch", "name": "从水居餐厅.特色云南菜(滇池海鸥岛店)"}, {"date": "2026-04-08", "type": "dinner", "name": "从水居餐厅.特色云南菜(滇池海鸥岛店)"}, {"date": "2026-04-09", "type": "dinner", "name": "从水居餐厅.特色云南菜(滇池海鸥岛店)"}, {"date": "2026-04-10", "type": "dinner", "name": "从水居餐厅.特色云南菜(滇池海鸥岛店)"}]}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 4, "party_total": 5, "room_count": 3, "priced_nights": 4, "expected_min_total_hotels": 4800, "reported_total_hotels": 4000, "diff": -800, "covers_nights": false}}]`

### v3_harder_pref_fix_eval_000018
- request: 天津 2026-07-05->2026-07-07 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "天津博物馆", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-07-06", "day_index": 1, "name": "天津博物馆"}, {"date": "2026-07-07", "day_index": 2, "name": "天津博物馆"}]}, {"name_key": "滨江道步行街", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-07-06", "day_index": 1, "name": "滨江道步行街(天津·金街店)"}, {"date": "2026-07-07", "day_index": 2, "name": "滨江道步行街(天津·金街店)"}]}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "汉巴味德", "count": 3, "max_allowed": 2, "occurrences": [{"date": "2026-07-05", "type": "lunch", "name": "汉巴味德(乐宾百货店)"}, {"date": "2026-07-06", "type": "dinner", "name": "汉巴味德(乐宾百货店)"}, {"date": "2026-07-07", "type": "lunch", "name": "汉巴味德(乐宾百货店)"}]}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 190, "expected_total_attractions": 570, "reported_total_attractions": 1140, "meal_per_person_cost_sum": 682, "expected_total_meals": 2046, "reported_total_meals": 2649, "reported_total_transportation": 1200}}]`

### v3_harder_pref_fix_eval_000008
- request: 大理 2026-05-10->2026-05-12 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-05-11", "lunch": "海东茄子烧烤(古城店)", "dinner": "海东茄子烧烤(滇纺店)"}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 75, "expected_total_attractions": 225, "reported_total_attractions": 675, "meal_per_person_cost_sum": 429, "expected_total_meals": 1287, "reported_total_meals": 1869, "reported_total_transportation": 1200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 75, "expected_total_attractions": 225, "reported_total_attractions": 675, "meal_per_person_cost_sum": 429, "expected_total_meals": 1287, "reported_total_meals": 1869, "reported_total_transportation": 1200}}]`

### v3_harder_pref_fix_eval_000023
- request: 大理 2026-09-03->2026-09-07 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-09-03", "type": "dinner", "name": "随园食单(善德居店)", "reason": "unknown_food_semantics"}, {"date": "2026-09-05", "type": "dinner", "name": "随园食单(善德居店)", "reason": "unknown_food_semantics"}, {"date": "2026-09-06", "type": "dinner", "name": "随园食单(善德居店)", "reason": "unknown_food_semantics"}, {"date": "2026-09-07", "type": "lunch", "name": "随园食单(善德居店)", "reason": "unknown_food_semantics"}, {"date": "2026-09-07", "type": "dinner", "name": "随园食单(善德居店)", "reason": "unknown_food_semantics"}]}, {"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-09-07", "lunch": "随园食单(善德居店)", "dinner": "随园食单(善德居店)"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "随园食单", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-09-03", "type": "dinner", "name": "随园食单(善德居店)"}, {"date": "2026-09-05", "type": "dinner", "name": "随园食单(善德居店)"}, {"date": "2026-09-06", "type": "dinner", "name": "随园食单(善德居店)"}, {"date": "2026-09-07", "type": "lunch", "name": "随园食单(善德居店)"}, {"date": "2026-09-07", "type": "dinner", "name": "随园食单(善德居店)"}]}, {"name_key": "蒙自小黄牛米线", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-09-04", "type": "breakfast", "name": "蒙自小黄牛米线"}, {"date": "2026-09-05", "type": "breakfast", "name": "蒙自小黄牛米线(S湾海景店)"}, {"date": "2026-09-06", "type": "breakfast", "name": "蒙自小黄牛米线"}, {"date": "2026-09-07", "type": "breakfast", "name": "蒙自小黄牛米线"}]}]}]`

### v3_harder_pref_fix_eval_000015
- request: 南京 2026-04-06->2026-04-10 days=5 transport=公共交通 hotel=民宿 prefs=['摄影', '自然风光', '城市漫步', '本地菜']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "玄武湖景区", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-04-06", "day_index": 0, "name": "玄武湖景区"}, {"date": "2026-04-08", "day_index": 2, "name": "玄武湖景区"}]}, {"name_key": "总统府", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-04-07", "day_index": 1, "name": "总统府"}, {"date": "2026-04-10", "day_index": 4, "name": "总统府"}]}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "南京大牌档", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-04-06", "type": "breakfast", "name": "南京大牌档(中山陵紫金坊店)"}, {"date": "2026-04-07", "type": "breakfast", "name": "南京大牌档(1912总统府店)"}, {"date": "2026-04-08", "type": "breakfast", "name": "南京大牌档(中山陵紫金坊店)"}, {"date": "2026-04-10", "type": "breakfast", "name": "南京大牌档(1912总统府店)"}]}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 110, "expected_total_attractions": 110, "reported_total_attractions": 115, "meal_per_person_cost_sum": 1118, "expected_total_meals": 1118, "reported_total_meals": 1082, "reported_total_transportation": 200}}]`

### v3_harder_pref_fix_eval_000002
- request: 杭州 2026-04-30->2026-05-03 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '夜市', '老字号', '城市漫步']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "泮芳春煎饺", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-04-30", "type": "breakfast", "name": "泮芳春煎饺(龙翔桥店)"}, {"date": "2026-05-01", "type": "breakfast", "name": "泮芳春煎饺(龙翔桥店)"}, {"date": "2026-05-02", "type": "breakfast", "name": "泮芳春煎饺(龙翔桥店)"}, {"date": "2026-05-03", "type": "breakfast", "name": "泮芳春煎饺(龙翔桥店)"}]}]}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 4044, "total": 3844, "diff": 200, "requested_budget": {"available": true, "amount": 5200, "scope": "total", "party_size": 4, "total": 5200, "source": "budget_constraint", "budget_level": "limited", "strictness": "hard"}, "per_person_day": 240.25, "budget_level": "limited", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "limited", "strictness": "hard", "amount": 5200, "target_min_ratio": 0.72, "target_max_ratio": 1.0, "target_min_total": 3700, "target_max_total": 5200, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 4, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 1500, "reported_total_hotels": 1500, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 344, "expected_total_attractions": 1376, "reported_total_attractions": 408, "meal_per_person_cost_sum": 751, "expected_total_meals": 3004, "reported_total_meals": 1736, "reported_total_transportation": 400}}]`

### v3_harder_pref_fix_eval_000020
- request: 杭州 2026-06-20->2026-06-24 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "杭州西湖风景名胜区-太子湾公园", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-06-21", "day_index": 1, "name": "杭州西湖风景名胜区-太子湾公园"}, {"date": "2026-06-24", "day_index": 4, "name": "杭州西湖风景名胜区-太子湾公园"}]}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 4, "party_total": 5, "room_count": 3, "priced_nights": 4, "expected_min_total_hotels": 6000, "reported_total_hotels": 10000, "diff": 4000, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 5, "hotel_room_count": 3, "attraction_ticket_sum": 160, "expected_total_attractions": 800, "reported_total_attractions": 1000, "meal_per_person_cost_sum": 1096, "expected_total_meals": 5480, "reported_total_meals": 4400, "reported_total_transportation": 2000}}]`

### v3_harder_pref_fix_eval_000031
- request: 成都 2026-05-10->2026-05-13 days=4 transport=打车 hotel=高端酒店 prefs=['高端酒店', '艺术', '特色餐厅', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "山面包", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-05-10", "type": "breakfast", "name": "山面包(东郊记忆店)"}, {"date": "2026-05-11", "type": "breakfast", "name": "山面包(望平街店)"}, {"date": "2026-05-12", "type": "breakfast", "name": "山面包(东郊记忆店)"}, {"date": "2026-05-13", "type": "breakfast", "name": "山面包(东郊记忆店)"}]}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 2, "room_count": 1, "priced_nights": 3, "expected_min_total_hotels": 2400, "reported_total_hotels": 4800, "diff": 2400, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 245, "expected_total_attractions": 490, "reported_total_attractions": 1000, "meal_per_person_cost_sum": 1079, "expected_total_meals": 2158, "reported_total_meals": 3544, "reported_total_transportation": 1200}}]`

### v3_harder_pref_fix_eval_000006
- request: 南京 2026-07-05->2026-07-08 days=4 transport=自驾 hotel=亲子酒店 prefs=['亲子', '动物园', '海洋馆', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "南京博物院", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-07-06", "day_index": 1, "name": "南京博物院"}, {"date": "2026-07-08", "day_index": 3, "name": "南京博物院"}]}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 65, "expected_total_attractions": 195, "reported_total_attractions": 105, "meal_per_person_cost_sum": 729, "expected_total_meals": 2187, "reported_total_meals": 1719, "reported_total_transportation": 500}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 65, "expected_total_attractions": 195, "reported_total_attractions": 105, "meal_per_person_cost_sum": 729, "expected_total_meals": 2187, "reported_total_meals": 1719, "reported_total_transportation": 500}}]`

### v3_harder_pref_fix_eval_000016
- request: 苏州 2026-06-05->2026-06-08 days=4 transport=自驾 hotel=亲子酒店 prefs=['亲子', '动物园', '海洋馆', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 3, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 7500, "reported_total_hotels": 3750, "diff": -3750, "covers_nights": false}}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 7400, "total": 7390, "diff": 10, "requested_budget": {"available": true, "amount": 7600, "scope": "total", "party_size": 3, "total": 7600, "source": "budget_constraint", "budget_level": "standard", "strictness": "hard"}, "per_person_day": 615.83, "budget_level": "standard", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "standard", "strictness": "hard", "amount": 7600, "target_min_ratio": 0.55, "target_max_ratio": 1.0, "target_min_total": 4200, "target_max_total": 7600, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 3, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 7500, "reported_total_hotels": 3750, "diff": -3750, "covers_nights": false}, "hotel_budget_covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 195, "expected_total_attractions": 585, "reported_total_attractions": 1035, "meal_per_person_cost_sum": 733, "expected_total_meals": 2199, "reported_total_meals": 1615, "reported_total_transportation": 1000}}]`
