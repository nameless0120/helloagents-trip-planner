# Rule Eval Report: sft_cp2_pref_fix_vllm_ablate_attraction_dedupe_only_smoke100

- records: 100
- generations: `training/outputs/eval/sft_cp2_pref_fix_vllm_ablate_attraction_dedupe_only_smoke100/generations.jsonl`
- records_path: `training/data/v3/eval_harder_pref_fix_attraction_prompt_ablation_attraction_dedupe_only_no_route/records.jsonl`

## Boolean Metrics

| Metric | Pass | Total | Rate |
| --- | ---: | ---: | ---: |
| accommodation_type_ok | 99 | 99 | 100.00% |
| attraction_budget_consistent | 10 | 99 | 10.10% |
| attraction_budget_party_relation_ok | 40 | 99 | 40.40% |
| attraction_count_ok | 97 | 99 | 97.98% |
| attraction_diversity_ok | 55 | 99 | 55.56% |
| attraction_grounding_ok | 94 | 99 | 94.95% |
| attraction_repeat_limit_ok | 55 | 99 | 55.56% |
| budget_arithmetic_consistent | 73 | 99 | 73.74% |
| budget_consistent | 73 | 99 | 73.74% |
| budget_level_aligned | 65 | 99 | 65.66% |
| budget_preference_aligned | 65 | 99 | 65.66% |
| budget_relationship_ok | 17 | 99 | 17.17% |
| budget_selection_ok | 48 | 99 | 48.48% |
| budget_user_constraint_ok | 91 | 99 | 91.92% |
| budget_within_user_budget | 98 | 99 | 98.99% |
| city_ok | 99 | 99 | 100.00% |
| date_range_ok | 99 | 99 | 100.00% |
| day_dates_ok | 99 | 99 | 100.00% |
| day_index_ok | 99 | 99 | 100.00% |
| days_len_ok | 99 | 99 | 100.00% |
| dpo_soft_pass | 27 | 99 | 27.27% |
| dpo_soft_recomputed_budget_pass | 18 | 99 | 18.18% |
| hard_pass | 89 | 99 | 89.90% |
| hotel_budget_covers_nights | 66 | 99 | 66.67% |
| hotel_budget_relation_ok | 67 | 99 | 67.68% |
| hotel_distance_placeholder_ok | 99 | 99 | 100.00% |
| hotel_grounding_ok | 98 | 99 | 98.99% |
| invalid_hotel_name_ok | 99 | 99 | 100.00% |
| json_extract_ok | 100 | 100 | 100.00% |
| legacy_hard_pass | 37 | 99 | 37.37% |
| location_object_ok | 99 | 99 | 100.00% |
| meal_budget_consistent | 0 | 99 | 0.00% |
| meal_complete | 99 | 99 | 100.00% |
| meal_cost_scale_ok | 39 | 99 | 39.39% |
| meal_diversity_ok | 69 | 99 | 69.70% |
| meal_grounding_ok | 97 | 99 | 97.98% |
| meal_lunch_dinner_same_day_ok | 86 | 99 | 86.87% |
| meal_repeat_limit_ok | 74 | 99 | 74.75% |
| meal_specific_ok | 98 | 99 | 98.99% |
| meal_valid_semantics_ok | 97 | 99 | 97.98% |
| middle_hotel_ok | 99 | 99 | 100.00% |
| recomputed_budget_fit_ok | 48 | 99 | 48.48% |
| recomputed_budget_hard_ok | 83 | 99 | 83.84% |
| recomputed_budget_level_aligned | 48 | 99 | 48.48% |
| recomputed_budget_preference_aligned | 48 | 99 | 48.48% |
| recomputed_budget_user_constraint_ok | 83 | 99 | 83.84% |
| recomputed_budget_within_user_budget | 95 | 99 | 95.96% |
| schema_ok | 99 | 100 | 99.00% |
| sft_budget_semantic_hard_pass | 10 | 99 | 10.10% |
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
    "avg": 0.9236,
    "p50": 1.0,
    "p90": 1.0
  },
  "attraction_grounding_rate": {
    "avg": 0.9946,
    "p50": 1.0,
    "p90": 1.0
  },
  "hotel_grounding_rate": {
    "avg": 0.9899,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_diversity_unique_rate": {
    "avg": 0.7534,
    "p50": 0.8,
    "p90": 1.0
  },
  "meal_food_pois_grounding_rate": {
    "avg": 0.9971,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_grounding_rate": {
    "avg": 0.9971,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_semantic_valid_rate": {
    "avg": 0.9971,
    "p50": 1.0,
    "p90": 1.0
  },
  "recomputed_budget_per_person_day": {
    "avg": 596.0589,
    "p50": 571.4,
    "p90": 820.5
  },
  "recomputed_budget_total": {
    "avg": 6535.7879,
    "p50": 6228.0,
    "p90": 11485.0
  }
}
```

## Failure Types

```json
{
  "meal_budget_inconsistent": 99,
  "attraction_budget_inconsistent": 89,
  "budget_relationship_mismatch": 82,
  "meal_cost_scale_too_low": 60,
  "attraction_repeat_too_many": 44,
  "budget_preference_mismatch": 34,
  "hotel_budget_underestimated": 33,
  "budget_arithmetic_inconsistent": 26,
  "meal_repeat_too_many": 25,
  "meal_same_day_lunch_dinner_repeat": 13,
  "budget_hard_constraint_exceeded": 8,
  "meal_invalid_name": 2,
  "too_many_attractions": 2,
  "schema": 1,
  "meal_placeholder": 1
}
```

## Failure Examples

### v3_harder_pref_fix_eval_000004
- request: 张家界 2026-05-10->2026-05-12 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 2000, "total": 1900, "diff": 100, "requested_budget": {"available": true, "amount": 2500, "scope": "total", "party_size": 1, "total": 2500, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "hard"}, "per_person_day": 633.33, "budget_level": "comfortable", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "hard", "amount": 2500, "target_min_ratio": 0.65, "target_max_ratio": 1.0, "target_min_total": 1600, "target_max_total": 2500, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 1, "room_count": 1, "priced_nights": 2, "expected_min_total_hotels": 800, "reported_total_hotels": 800, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 160, "expected_total_attractions": 160, "reported_total_attractions": 240, "meal_per_person_cost_sum": 508, "expected_total_meals": 508, "reported_total_meals": 660, "reported_total_transportation": 300}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 160, "expected_total_attractions": 160, "reported_total_attractions": 240, "meal_per_person_cost_sum": 508, "expected_total_meals": 508, "reported_total_meals": 660, "reported_total_transportation": 300}}]`

### v3_harder_pref_fix_eval_000014
- request: 成都 2026-06-05->2026-06-07 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 165, "expected_total_attractions": 165, "reported_total_attractions": 215, "meal_per_person_cost_sum": 638, "expected_total_meals": 638, "reported_total_meals": 1035, "reported_total_transportation": 300}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 165, "expected_total_attractions": 165, "reported_total_attractions": 215, "meal_per_person_cost_sum": 638, "expected_total_meals": 638, "reported_total_meals": 1035, "reported_total_transportation": 300}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": false, "meal_cost_scale_ok": false, "budget_relationship_ok": false, "expected_total_hotels": 900, "reported_total_hotels": 900, "expected_total_attractions": 165, "reported_total_attractions": 215, "meal_scale_eval": {"ok": false, "party_total": 1, "budget_level": "comfortable", "per_person_lunch_dinner_floor": 50, "per_person_breakfast_floor": 20, "meal_count": 9, "checked_count": 9, "failure_count": 2, "failures": [{"date": "2026-06-05", "type": "breakfast", "name": "纯阳馆鱼香排骨面(吉祥街店)", "estimated_cost": 17, "min_expected_cost": 20}, {"date": "2026-06-07", "type": "lunch", "name": "叶婆婆钵钵鸡(太古里店)", "estimated_cost": 42, "min_expected_cost": 50}]}}}]`

### v3_harder_pref_fix_eval_000011
- request: 福州 2026-06-20->2026-06-23 days=4 transport=打车 hotel=高端酒店 prefs=['高端酒店', '艺术', '特色餐厅', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 2, "room_count": 1, "priced_nights": 3, "expected_min_total_hotels": 2250, "reported_total_hotels": 4500, "diff": 2250, "covers_nights": false}}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 8708, "total": 8608, "diff": 100, "requested_budget": {"available": true, "amount": 12100, "scope": "total", "party_size": 2, "total": 12100, "source": "budget_constraint", "budget_level": "premium", "strictness": "soft"}, "per_person_day": 1076.0, "budget_level": "premium", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "premium", "strictness": "soft", "amount": 12100, "target_min_ratio": 0.7, "target_max_ratio": 1.12, "target_min_total": 8500, "target_max_total": 13600, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 2, "room_count": 1, "priced_nights": 3, "expected_min_total_hotels": 2250, "reported_total_hotels": 4500, "diff": 2250, "covers_nights": false}, "hotel_budget_covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 117, "expected_total_attractions": 234, "reported_total_attractions": 160, "meal_per_person_cost_sum": 731, "expected_total_meals": 1462, "reported_total_meals": 2848, "reported_total_transportation": 1200}}]`

### v3_harder_pref_fix_eval_000009
- request: 苏州 2026-04-29->2026-05-02 days=4 transport=打车 hotel=亲子酒店 prefs=['亲子', '老人友好', '博物馆', '城市公园', '特色餐厅']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "苏州博物馆西馆", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-04-30", "day_index": 1, "name": "苏州博物馆西馆"}, {"date": "2026-05-02", "day_index": 3, "name": "苏州博物馆西馆"}]}]}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 11600, "total": 11500, "diff": 100, "requested_budget": {"available": true, "amount": 15700, "scope": "total", "party_size": 4, "total": 15700, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "soft"}, "per_person_day": 718.75, "budget_level": "comfortable", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "soft", "amount": 15700, "target_min_ratio": 0.65, "target_max_ratio": 1.05, "target_min_total": 10200, "target_max_total": 16500, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 4, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 7500, "reported_total_hotels": 7500, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 140, "expected_total_attractions": 560, "reported_total_attractions": 180, "meal_per_person_cost_sum": 894, "expected_total_meals": 3576, "reported_total_meals": 2720, "reported_total_transportation": 1200}}]`

### v3_harder_pref_fix_eval_000001
- request: 桂林 2026-09-03->2026-09-06 days=4 transport=打车 hotel=高端酒店 prefs=['高端酒店', '艺术', '特色餐厅', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "东西巷", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-09-03", "day_index": 0, "name": "东西巷"}, {"date": "2026-09-05", "day_index": 2, "name": "东西巷"}]}, {"name_key": "广西省立艺术馆", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-09-03", "day_index": 0, "name": "广西省立艺术馆"}, {"date": "2026-09-04", "day_index": 1, "name": "广西省立艺术馆"}]}, {"name_key": "桂林博物馆", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-09-05", "day_index": 2, "name": "桂林博物馆"}, {"date": "2026-09-06", "day_index": 3, "name": "桂林博物馆"}]}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "阿甘酒家", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-09-03", "type": "lunch", "name": "阿甘酒家(解西店)"}, {"date": "2026-09-04", "type": "breakfast", "name": "阿甘酒家(依仁店)"}, {"date": "2026-09-04", "type": "lunch", "name": "阿甘酒家(七星路店)"}, {"date": "2026-09-05", "type": "lunch", "name": "阿甘酒家(依仁店)"}, {"date": "2026-09-06", "type": "lunch", "name": "阿甘酒家(七星路店)"}]}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 2, "room_count": 1, "priced_nights": 3, "expected_min_total_hotels": 3600, "reported_total_hotels": 7200, "diff": 3600, "covers_nights": false}}]`

### v3_harder_pref_fix_eval_000019
- request: 丽江 2026-05-10->2026-05-13 days=4 transport=打车 hotel=亲子酒店 prefs=['亲子', '老人友好', '博物馆', '城市公园', '特色餐厅']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "束河古镇", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-05-11", "day_index": 1, "name": "束河古镇"}, {"date": "2026-05-13", "day_index": 3, "name": "束河古镇"}]}, {"name_key": "束河风味美食街", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-05-11", "day_index": 1, "name": "束河风味美食街"}, {"date": "2026-05-13", "day_index": 3, "name": "束河风味美食街"}]}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 668, "expected_total_attractions": 1336, "reported_total_attractions": 1200, "meal_per_person_cost_sum": 590, "expected_total_meals": 1180, "reported_total_meals": 1284, "reported_total_transportation": 1200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 668, "expected_total_attractions": 1336, "reported_total_attractions": 1200, "meal_per_person_cost_sum": 590, "expected_total_meals": 1180, "reported_total_meals": 1284, "reported_total_transportation": 1200}}]`

### v3_harder_pref_fix_eval_000003
- request: 西安 2025-05-06->2025-05-10 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 4000, "total": 3900, "diff": 100, "requested_budget": {"available": true, "amount": 5400, "scope": "total", "party_size": 2, "total": 5400, "source": "budget_constraint", "budget_level": "standard", "strictness": "hard"}, "per_person_day": 390.0, "budget_level": "standard", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "standard", "strictness": "hard", "amount": 5400, "target_min_ratio": 0.55, "target_max_ratio": 1.0, "target_min_total": 3000, "target_max_total": 5400, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 4, "party_total": 2, "room_count": 1, "priced_nights": 4, "expected_min_total_hotels": 1800, "reported_total_hotels": 1800, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 145, "expected_total_attractions": 290, "reported_total_attractions": 320, "meal_per_person_cost_sum": 826, "expected_total_meals": 1652, "reported_total_meals": 1680, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 145, "expected_total_attractions": 290, "reported_total_attractions": 320, "meal_per_person_cost_sum": 826, "expected_total_meals": 1652, "reported_total_meals": 1680, "reported_total_transportation": 200}}]`

### v3_harder_pref_fix_eval_000013
- request: 武汉 2026-05-08->2026-05-12 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-05-12", "lunch": "刘聋子牛肉粉馆(汉阳龙兴东街店)", "dinner": "刘聋子牛肉粉馆(光谷新竹路店)"}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 130, "expected_total_attractions": 260, "reported_total_attractions": 140, "meal_per_person_cost_sum": 809, "expected_total_meals": 1618, "reported_total_meals": 1060, "reported_total_transportation": 1000}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 130, "expected_total_attractions": 260, "reported_total_attractions": 140, "meal_per_person_cost_sum": 809, "expected_total_meals": 1618, "reported_total_meals": 1060, "reported_total_transportation": 1000}}]`

### v3_harder_pref_fix_eval_000010
- request: 西安 2026-08-04->2026-08-08 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "西安鼓楼", "count": 3, "max_allowed": 1, "occurrences": [{"date": "2026-08-04", "day_index": 0, "name": "西安鼓楼"}, {"date": "2026-08-06", "day_index": 2, "name": "西安鼓楼"}, {"date": "2026-08-07", "day_index": 3, "name": "西安鼓楼"}]}, {"name_key": "西安博物院", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-08-07", "day_index": 3, "name": "西安博物院"}, {"date": "2026-08-08", "day_index": 4, "name": "西安博物院"}]}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "奔跑吧陕菜·常来长安", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-08-04", "type": "lunch", "name": "奔跑吧陕菜·常来长安(钟楼南大街店)"}, {"date": "2026-08-06", "type": "lunch", "name": "奔跑吧陕菜·常来长安(钟楼南大街店)"}, {"date": "2026-08-07", "type": "lunch", "name": "奔跑吧陕菜·常来长安(钟楼南大街店)"}, {"date": "2026-08-08", "type": "lunch", "name": "奔跑吧陕菜·常来长安(钟楼南大街店)"}]}, {"name_key": "奔跑吧陕菜·雁塔长安", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-08-04", "type": "dinner", "name": "奔跑吧陕菜·雁塔长安(大雁塔店)"}, {"date": "2026-08-05", "type": "dinner", "name": "奔跑吧陕菜·雁塔长安(大雁塔店)"}, {"date": "2026-08-06", "type": "dinner", "name": "奔跑吧陕菜·雁塔长安(大雁塔店)"}, {"date": "2026-08-07", "type": "dinner", "name": "奔跑吧陕菜·雁塔长安(大雁塔店)"}, {"date": "2026-08-08", "type": "dinner", "name": "奔跑吧陕菜·雁塔长安(大雁塔店)"}]}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 4, "party_total": 5, "room_count": 3, "priced_nights": 4, "expected_min_total_hotels": 5400, "reported_total_hotels": 3600, "diff": -1800, "covers_nights": false}}]`

### v3_harder_pref_fix_eval_000017
- request: 苏州 2026-05-08->2026-05-12 days=5 transport=公共交通 hotel=民宿 prefs=['小众展馆', '咖啡', '艺术', '城市漫步', '特色餐厅']
- errors: `[{"stage": "schema", "message": "9 validation errors for TripPlan\ndays.2.attractions.2.address\n  Input should be a valid string [type=string_type, input_value=None, input_type=NoneType]\n    For further information visit https://errors.pydantic.dev/2.12/v/string_type\ndays.2.attractions.2.location\n  Input should be a valid dictionary or instance of Location [type=model_type, input_value=None, input_type=NoneType]\n    For further information visit https://errors.pydantic.dev/2.12/v/model_type\ndays.2.attractions.2.visit_duration\n  Field required [type=missing, input_value={'name': '乾盛兴苏式...None, 'ticket_price': 0}, input_type=dict]\n    For further information visit https://errors.pydantic.dev/2.12/v/missing\ndays.3.attractions.2.address\n  Input should be a valid string [type=string_type, input_value=None, input_type=NoneType]\n    For further information visit https://errors.pydantic.dev/2.12/v/string_type\ndays.3.attractions.2.location\n  Input should be a valid dictionary or instance of Location [type=model_type, input_value=None, input_type=NoneType]\n    For further information visit https://errors.pydantic.dev/2.12/v/model_type\ndays.3.attractions.2.visit_duration\n  Field required [type=missing, input_value={'name': '乾盛兴苏式...None, 'ticket_price': 0}, input_type=dict]\n    For further information visit https://errors.pydantic.dev/2.12/v/missing\ndays.4.attractions.2.address\n  Input should be a valid string [type=string_type, input_value=None, input_type=NoneType]\n    For further information visit https://errors.pydantic.dev/2.12/v/string_type\ndays.4.attractions.2.location\n  Input should be a valid dictionary or instance of Location [type=model_type, input_value=None, input_type=NoneType]\n    For further information visit https://errors.pydantic.dev/2.12/v/model_type\ndays.4.attractions.2.visit_duration\n  Field required [type=missing, input_value={'name': '乾盛兴苏式...None, 'ticket_price': 0}, input_type=dict]\n    For further information visit https://errors.pydantic.dev/2.12/v/missing"}]`

### v3_harder_pref_fix_eval_000018
- request: 天津 2026-07-05->2026-07-07 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 190, "expected_total_attractions": 570, "reported_total_attractions": 1050, "meal_per_person_cost_sum": 681, "expected_total_meals": 2043, "reported_total_meals": 2700, "reported_total_transportation": 1050}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 190, "expected_total_attractions": 570, "reported_total_attractions": 1050, "meal_per_person_cost_sum": 681, "expected_total_meals": 2043, "reported_total_meals": 2700, "reported_total_transportation": 1050}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": false, "meal_cost_scale_ok": false, "budget_relationship_ok": false, "expected_total_hotels": 3000, "reported_total_hotels": 3000, "expected_total_attractions": 570, "reported_total_attractions": 1050, "meal_scale_eval": {"ok": false, "party_total": 3, "budget_level": "comfortable", "per_person_lunch_dinner_floor": 50, "per_person_breakfast_floor": 20, "meal_count": 9, "checked_count": 9, "failure_count": 1, "failures": [{"date": "2026-07-07", "type": "breakfast", "name": "南楼煎饼(滨江道店)", "estimated_cost": 14, "min_expected_cost": 20}]}}}]`

### v3_harder_pref_fix_eval_000008
- request: 大理 2026-05-10->2026-05-12 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物']
- errors: `[{"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 75, "expected_total_attractions": 225, "reported_total_attractions": 225, "meal_per_person_cost_sum": 416, "expected_total_meals": 1248, "reported_total_meals": 1575, "reported_total_transportation": 1200}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": true, "meal_cost_scale_ok": false, "budget_relationship_ok": false, "expected_total_hotels": 3000, "reported_total_hotels": 3000, "expected_total_attractions": 225, "reported_total_attractions": 225, "meal_scale_eval": {"ok": false, "party_total": 3, "budget_level": "comfortable", "per_person_lunch_dinner_floor": 50, "per_person_breakfast_floor": 20, "meal_count": 9, "checked_count": 9, "failure_count": 2, "failures": [{"date": "2026-05-10", "type": "breakfast", "name": "普通面包社", "estimated_cost": 19, "min_expected_cost": 20}, {"date": "2026-05-11", "type": "breakfast", "name": "九孃豌豆粉店", "estimated_cost": 9, "min_expected_cost": 20}]}}}, {"stage": "rule", "type": "meal_cost_scale_too_low", "details": {"ok": false, "party_total": 3, "budget_level": "comfortable", "per_person_lunch_dinner_floor": 50, "per_person_breakfast_floor": 20, "meal_count": 9, "checked_count": 9, "failure_count": 2, "failures": [{"date": "2026-05-10", "type": "breakfast", "name": "普通面包社", "estimated_cost": 19, "min_expected_cost": 20}, {"date": "2026-05-11", "type": "breakfast", "name": "九孃豌豆粉店", "estimated_cost": 9, "min_expected_cost": 20}]}}]`

### v3_harder_pref_fix_eval_000000
- request: 昆明 2026-04-06->2026-04-10 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "国立西南联合大学旧址", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-04-06", "day_index": 0, "name": "国立西南联合大学旧址"}, {"date": "2026-04-09", "day_index": 3, "name": "国立西南联合大学旧址"}]}, {"name_key": "昆明老街·美食天街", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-04-06", "day_index": 0, "name": "昆明老街·美食天街(正义坊购物中心店)"}, {"date": "2026-04-10", "day_index": 4, "name": "昆明老街·美食天街(正义坊购物中心店)"}]}, {"name_key": "昆明老街钱王街", "count": 3, "max_allowed": 1, "occurrences": [{"date": "2026-04-07", "day_index": 1, "name": "昆明老街钱王街"}, {"date": "2026-04-09", "day_index": 3, "name": "昆明老街钱王街"}, {"date": "2026-04-10", "day_index": 4, "name": "昆明老街钱王街"}]}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "从水居餐厅.特色云南菜", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-04-06", "type": "lunch", "name": "从水居餐厅.特色云南菜(滇池海鸥岛店)"}, {"date": "2026-04-08", "type": "lunch", "name": "从水居餐厅.特色云南菜(滇池海鸥岛店)"}, {"date": "2026-04-09", "type": "lunch", "name": "从水居餐厅.特色云南菜(滇池海鸥岛店)"}, {"date": "2026-04-10", "type": "lunch", "name": "从水居餐厅.特色云南菜(滇池海鸥岛店)"}]}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 4, "party_total": 5, "room_count": 3, "priced_nights": 4, "expected_min_total_hotels": 4800, "reported_total_hotels": 3200, "diff": -1600, "covers_nights": false}}]`

### v3_harder_pref_fix_eval_000031
- request: 成都 2026-05-10->2026-05-13 days=4 transport=打车 hotel=高端酒店 prefs=['高端酒店', '艺术', '特色餐厅', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 2, "room_count": 1, "priced_nights": 3, "expected_min_total_hotels": 2400, "reported_total_hotels": 4800, "diff": 2400, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 190, "expected_total_attractions": 380, "reported_total_attractions": 460, "meal_per_person_cost_sum": 1124, "expected_total_meals": 2248, "reported_total_meals": 3864, "reported_total_transportation": 1200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 190, "expected_total_attractions": 380, "reported_total_attractions": 460, "meal_per_person_cost_sum": 1124, "expected_total_meals": 2248, "reported_total_meals": 3864, "reported_total_transportation": 1200}}]`

### v3_harder_pref_fix_eval_000002
- request: 杭州 2026-04-30->2026-05-03 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '夜市', '老字号', '城市漫步']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 219, "expected_total_attractions": 876, "reported_total_attractions": 440, "meal_per_person_cost_sum": 777, "expected_total_meals": 3108, "reported_total_meals": 1432, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 219, "expected_total_attractions": 876, "reported_total_attractions": 440, "meal_per_person_cost_sum": 777, "expected_total_meals": 3108, "reported_total_meals": 1432, "reported_total_transportation": 200}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": false, "meal_cost_scale_ok": true, "budget_relationship_ok": false, "expected_total_hotels": 1500, "reported_total_hotels": 1500, "expected_total_attractions": 876, "reported_total_attractions": 440, "meal_scale_eval": {"ok": true, "party_total": 4, "budget_level": "limited", "per_person_lunch_dinner_floor": 25, "per_person_breakfast_floor": 10, "meal_count": 12, "checked_count": 12, "failure_count": 0, "failures": []}}}]`

### v3_harder_pref_fix_eval_000023
- request: 大理 2026-09-03->2026-09-07 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "大理古城-玉洱园", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-09-03", "day_index": 0, "name": "大理古城-玉洱园"}, {"date": "2026-09-06", "day_index": 3, "name": "大理古城-玉洱园"}]}]}, {"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-09-03", "type": "lunch", "name": "随园食单(善德居店)", "reason": "unknown_food_semantics"}, {"date": "2026-09-06", "type": "lunch", "name": "随园食单(善德居店)", "reason": "unknown_food_semantics"}, {"date": "2026-09-07", "type": "lunch", "name": "随园食单(善德居店)", "reason": "unknown_food_semantics"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "蒙自小黄牛米线", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-09-04", "type": "breakfast", "name": "蒙自小黄牛米线"}, {"date": "2026-09-05", "type": "breakfast", "name": "蒙自小黄牛米线(S湾海景店)"}, {"date": "2026-09-06", "type": "breakfast", "name": "蒙自小黄牛米线"}, {"date": "2026-09-07", "type": "breakfast", "name": "蒙自小黄牛米线"}]}]}]`

### v3_harder_pref_fix_eval_000015
- request: 南京 2026-04-06->2026-04-10 days=5 transport=公共交通 hotel=民宿 prefs=['摄影', '自然风光', '城市漫步', '本地菜']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "玄武湖景区", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-04-06", "day_index": 0, "name": "玄武湖景区"}, {"date": "2026-04-08", "day_index": 2, "name": "玄武湖景区"}]}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 190, "expected_total_attractions": 190, "reported_total_attractions": 265, "meal_per_person_cost_sum": 1325, "expected_total_meals": 1325, "reported_total_meals": 1282, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 190, "expected_total_attractions": 190, "reported_total_attractions": 265, "meal_per_person_cost_sum": 1325, "expected_total_meals": 1325, "reported_total_meals": 1282, "reported_total_transportation": 200}}]`

### v3_harder_pref_fix_eval_000020
- request: 杭州 2026-06-20->2026-06-24 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "杭州西湖风景名胜区-太子湾公园", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-06-20", "day_index": 0, "name": "杭州西湖风景名胜区-太子湾公园"}, {"date": "2026-06-24", "day_index": 4, "name": "杭州西湖风景名胜区-太子湾公园"}]}, {"name_key": "中国湿地博物馆", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-06-22", "day_index": 2, "name": "中国湿地博物馆"}, {"date": "2026-06-24", "day_index": 4, "name": "中国湿地博物馆"}]}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 4, "party_total": 5, "room_count": 3, "priced_nights": 4, "expected_min_total_hotels": 6000, "reported_total_hotels": 4000, "diff": -2000, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 5, "hotel_room_count": 3, "attraction_ticket_sum": 80, "expected_total_attractions": 400, "reported_total_attractions": 150, "meal_per_person_cost_sum": 1120, "expected_total_meals": 5600, "reported_total_meals": 3475, "reported_total_transportation": 1000}}]`

### v3_harder_pref_fix_eval_000016
- request: 苏州 2026-06-05->2026-06-08 days=4 transport=自驾 hotel=亲子酒店 prefs=['亲子', '动物园', '海洋馆', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 11050, "total": 10050, "diff": 1000, "requested_budget": {"available": true, "amount": 7600, "scope": "total", "party_size": 3, "total": 7600, "source": "budget_constraint", "budget_level": "standard", "strictness": "hard"}, "per_person_day": 837.5, "budget_level": "standard", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "standard", "strictness": "hard", "amount": 7600, "target_min_ratio": 0.55, "target_max_ratio": 1.0, "target_min_total": 4200, "target_max_total": 7600, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": false, "user_constraint_ok": false, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 3, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 7500, "reported_total_hotels": 7500, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 195, "expected_total_attractions": 585, "reported_total_attractions": 555, "meal_per_person_cost_sum": 811, "expected_total_meals": 2433, "reported_total_meals": 1995, "reported_total_transportation": 1000}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 195, "expected_total_attractions": 585, "reported_total_attractions": 555, "meal_per_person_cost_sum": 811, "expected_total_meals": 2433, "reported_total_meals": 1995, "reported_total_transportation": 1000}}]`

### v3_harder_pref_fix_eval_000006
- request: 南京 2026-07-05->2026-07-08 days=4 transport=自驾 hotel=亲子酒店 prefs=['亲子', '动物园', '海洋馆', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "南京海底世界", "count": 3, "max_allowed": 1, "occurrences": [{"date": "2026-07-05", "day_index": 0, "name": "南京海底世界"}, {"date": "2026-07-07", "day_index": 2, "name": "南京海底世界"}, {"date": "2026-07-08", "day_index": 3, "name": "南京海底世界"}]}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 3, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 3300, "reported_total_hotels": 1650, "diff": -1650, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 228, "expected_total_attractions": 684, "reported_total_attractions": 105, "meal_per_person_cost_sum": 721, "expected_total_meals": 2163, "reported_total_meals": 1692, "reported_total_transportation": 1000}}]`
