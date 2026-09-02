# Rule Eval Report: sft_qwen25_7b_v3_1000_cp2_v2a_A_C_w10

- records: 300
- generations: `training/outputs/eval/sft_qwen25_7b_v3_1000_cp2_v2a_A_C_w10/generations.jsonl`
- records_path: `training/data/v3/eval_harder_attraction_pref_fix_20260506/A_C/records.jsonl`

## Boolean Metrics

| Metric | Pass | Total | Rate |
| --- | ---: | ---: | ---: |
| accommodation_type_ok | 298 | 298 | 100.00% |
| attraction_budget_consistent | 61 | 298 | 20.47% |
| attraction_budget_party_relation_ok | 217 | 298 | 72.82% |
| attraction_count_ok | 297 | 298 | 99.66% |
| attraction_diversity_ok | 250 | 298 | 83.89% |
| attraction_grounding_ok | 293 | 298 | 98.32% |
| attraction_repeat_limit_ok | 250 | 298 | 83.89% |
| budget_arithmetic_consistent | 236 | 298 | 79.19% |
| budget_consistent | 236 | 298 | 79.19% |
| budget_level_aligned | 195 | 298 | 65.44% |
| budget_preference_aligned | 195 | 298 | 65.44% |
| budget_relationship_ok | 53 | 298 | 17.79% |
| budget_selection_ok | 166 | 298 | 55.70% |
| budget_user_constraint_ok | 283 | 298 | 94.97% |
| budget_within_user_budget | 294 | 298 | 98.66% |
| city_ok | 298 | 298 | 100.00% |
| date_range_ok | 298 | 298 | 100.00% |
| day_dates_ok | 298 | 298 | 100.00% |
| day_index_ok | 298 | 298 | 100.00% |
| days_len_ok | 298 | 298 | 100.00% |
| dpo_soft_pass | 129 | 298 | 43.29% |
| dpo_soft_recomputed_budget_pass | 113 | 298 | 37.92% |
| hard_pass | 277 | 298 | 92.95% |
| hotel_budget_covers_nights | 196 | 298 | 65.77% |
| hotel_budget_relation_ok | 214 | 298 | 71.81% |
| hotel_distance_placeholder_ok | 298 | 298 | 100.00% |
| hotel_grounding_ok | 298 | 298 | 100.00% |
| invalid_hotel_name_ok | 298 | 298 | 100.00% |
| json_extract_ok | 300 | 300 | 100.00% |
| legacy_hard_pass | 116 | 298 | 38.93% |
| location_object_ok | 298 | 298 | 100.00% |
| meal_budget_consistent | 1 | 298 | 0.34% |
| meal_complete | 298 | 298 | 100.00% |
| meal_cost_scale_ok | 92 | 298 | 30.87% |
| meal_diversity_ok | 246 | 298 | 82.55% |
| meal_grounding_ok | 283 | 298 | 94.97% |
| meal_lunch_dinner_same_day_ok | 282 | 298 | 94.63% |
| meal_repeat_limit_ok | 261 | 298 | 87.58% |
| meal_specific_ok | 296 | 298 | 99.33% |
| meal_valid_semantics_ok | 283 | 298 | 94.97% |
| middle_hotel_ok | 298 | 298 | 100.00% |
| recomputed_budget_fit_ok | 166 | 298 | 55.70% |
| recomputed_budget_hard_ok | 263 | 298 | 88.26% |
| recomputed_budget_level_aligned | 166 | 298 | 55.70% |
| recomputed_budget_preference_aligned | 166 | 298 | 55.70% |
| recomputed_budget_user_constraint_ok | 263 | 298 | 88.26% |
| recomputed_budget_within_user_budget | 281 | 298 | 94.30% |
| schema_ok | 298 | 300 | 99.33% |
| sft_budget_semantic_hard_pass | 39 | 298 | 13.09% |
| sft_hard_pass | 277 | 298 | 92.95% |
| sft_no_budget_sum_hard_pass | 277 | 298 | 92.95% |
| sft_strict_hard_pass | 1 | 298 | 0.34% |
| transportation_budget_nonnegative | 298 | 298 | 100.00% |
| weather_dates_ok | 298 | 298 | 100.00% |
| weather_match | 298 | 298 | 100.00% |

## Numeric Metrics

```json
{
  "attraction_diversity_unique_rate": {
    "avg": 0.9823,
    "p50": 1.0,
    "p90": 1.0
  },
  "attraction_grounding_rate": {
    "avg": 0.9984,
    "p50": 1.0,
    "p90": 1.0
  },
  "hotel_grounding_rate": {
    "avg": 1.0,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_diversity_unique_rate": {
    "avg": 0.8562,
    "p50": 0.8889,
    "p90": 1.0
  },
  "meal_food_pois_grounding_rate": {
    "avg": 0.9949,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_grounding_rate": {
    "avg": 0.9949,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_semantic_valid_rate": {
    "avg": 0.9949,
    "p50": 1.0,
    "p90": 1.0
  },
  "recomputed_budget_per_person_day": {
    "avg": 605.9795,
    "p50": 571.25,
    "p90": 879.83
  },
  "recomputed_budget_total": {
    "avg": 6670.4128,
    "p50": 6192.0,
    "p90": 11945.0
  }
}
```

## Failure Types

```json
{
  "meal_budget_inconsistent": 297,
  "budget_relationship_mismatch": 245,
  "attraction_budget_inconsistent": 237,
  "meal_cost_scale_too_low": 206,
  "budget_preference_mismatch": 103,
  "hotel_budget_underestimated": 102,
  "budget_arithmetic_inconsistent": 62,
  "attraction_repeat_too_many": 48,
  "meal_repeat_too_many": 37,
  "meal_same_day_lunch_dinner_repeat": 16,
  "meal_invalid_name": 15,
  "budget_hard_constraint_exceeded": 15,
  "schema": 2,
  "meal_placeholder": 2,
  "too_many_attractions": 1
}
```

## Failure Examples

### v3_harder_pref_fix_eval_000004
- request: 张家界 2026-05-10->2026-05-12 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆']
- errors: `[{"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-05-12", "type": "dinner", "name": "老妈下饭菜(张家界中天鹭鸶湾一期店)", "reason": "unknown_food_semantics"}]}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 160, "expected_total_attractions": 160, "reported_total_attractions": 160, "meal_per_person_cost_sum": 460, "expected_total_meals": 460, "reported_total_meals": 423, "reported_total_transportation": 300}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": true, "meal_cost_scale_ok": false, "budget_relationship_ok": false, "expected_total_hotels": 800, "reported_total_hotels": 800, "expected_total_attractions": 160, "reported_total_attractions": 160, "meal_scale_eval": {"ok": false, "party_total": 1, "budget_level": "comfortable", "per_person_lunch_dinner_floor": 50, "per_person_breakfast_floor": 20, "meal_count": 9, "checked_count": 9, "failure_count": 2, "failures": [{"date": "2026-05-12", "type": "breakfast", "name": "家旺小吃(解放路店)", "estimated_cost": 13, "min_expected_cost": 20}, {"date": "2026-05-12", "type": "dinner", "name": "老妈下饭菜(张家界中天鹭鸶湾一期店)", "estimated_cost": 45, "min_expected_cost": 50}]}}}]`

### v3_harder_pref_fix_eval_000014
- request: 成都 2026-06-05->2026-06-07 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 165, "expected_total_attractions": 165, "reported_total_attractions": 225, "meal_per_person_cost_sum": 764, "expected_total_meals": 764, "reported_total_meals": 658, "reported_total_transportation": 300}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 165, "expected_total_attractions": 165, "reported_total_attractions": 225, "meal_per_person_cost_sum": 764, "expected_total_meals": 764, "reported_total_meals": 658, "reported_total_transportation": 300}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": false, "meal_cost_scale_ok": false, "budget_relationship_ok": false, "expected_total_hotels": 900, "reported_total_hotels": 900, "expected_total_attractions": 165, "reported_total_attractions": 225, "meal_scale_eval": {"ok": false, "party_total": 1, "budget_level": "comfortable", "per_person_lunch_dinner_floor": 50, "per_person_breakfast_floor": 20, "meal_count": 9, "checked_count": 9, "failure_count": 1, "failures": [{"date": "2026-06-05", "type": "breakfast", "name": "纯阳馆鱼香排骨面(吉祥街店)", "estimated_cost": 17, "min_expected_cost": 20}]}}}]`

### v3_harder_pref_fix_eval_000019
- request: 丽江 2026-05-10->2026-05-13 days=4 transport=打车 hotel=亲子酒店 prefs=['亲子', '老人友好', '博物馆', '城市公园', '特色餐厅']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 2, "room_count": 1, "priced_nights": 3, "expected_min_total_hotels": 3600, "reported_total_hotels": 7200, "diff": 3600, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 480, "expected_total_attractions": 960, "reported_total_attractions": 640, "meal_per_person_cost_sum": 666, "expected_total_meals": 1332, "reported_total_meals": 1034, "reported_total_transportation": 800}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 480, "expected_total_attractions": 960, "reported_total_attractions": 640, "meal_per_person_cost_sum": 666, "expected_total_meals": 1332, "reported_total_meals": 1034, "reported_total_transportation": 800}}]`

### v3_harder_pref_fix_eval_000009
- request: 苏州 2026-04-29->2026-05-02 days=4 transport=打车 hotel=亲子酒店 prefs=['亲子', '老人友好', '博物馆', '城市公园', '特色餐厅']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 140, "expected_total_attractions": 560, "reported_total_attractions": 480, "meal_per_person_cost_sum": 808, "expected_total_meals": 3232, "reported_total_meals": 2264, "reported_total_transportation": 1200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 140, "expected_total_attractions": 560, "reported_total_attractions": 480, "meal_per_person_cost_sum": 808, "expected_total_meals": 3232, "reported_total_meals": 2264, "reported_total_transportation": 1200}}]`

### v3_harder_pref_fix_eval_000001
- request: 桂林 2026-09-03->2026-09-06 days=4 transport=打车 hotel=高端酒店 prefs=['高端酒店', '艺术', '特色餐厅', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 2, "room_count": 1, "priced_nights": 3, "expected_min_total_hotels": 3600, "reported_total_hotels": 7200, "diff": 3600, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 425, "expected_total_attractions": 850, "reported_total_attractions": 820, "meal_per_person_cost_sum": 682, "expected_total_meals": 1364, "reported_total_meals": 1404, "reported_total_transportation": 1000}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 425, "expected_total_attractions": 850, "reported_total_attractions": 820, "meal_per_person_cost_sum": 682, "expected_total_meals": 1364, "reported_total_meals": 1404, "reported_total_transportation": 1000}}]`

### v3_harder_pref_fix_eval_000011
- request: 福州 2026-06-20->2026-06-23 days=4 transport=打车 hotel=高端酒店 prefs=['高端酒店', '艺术', '特色餐厅', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 2, "room_count": 1, "priced_nights": 3, "expected_min_total_hotels": 2250, "reported_total_hotels": 4500, "diff": 2250, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 117, "expected_total_attractions": 234, "reported_total_attractions": 254, "meal_per_person_cost_sum": 1038, "expected_total_meals": 2076, "reported_total_meals": 2658, "reported_total_transportation": 1000}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 117, "expected_total_attractions": 234, "reported_total_attractions": 254, "meal_per_person_cost_sum": 1038, "expected_total_meals": 2076, "reported_total_meals": 2658, "reported_total_transportation": 1000}}]`

### v3_harder_pref_fix_eval_000003
- request: 西安 2025-05-06->2025-05-10 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "西安碑林博物馆", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2025-05-06", "day_index": 0, "name": "西安碑林博物馆"}, {"date": "2025-05-09", "day_index": 3, "name": "西安碑林博物馆"}]}, {"name_key": "西安博物院", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2025-05-08", "day_index": 2, "name": "西安博物院"}, {"date": "2025-05-10", "day_index": 4, "name": "西安博物院"}]}]}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 3700, "total": 3600, "diff": 100, "requested_budget": {"available": true, "amount": 5400, "scope": "total", "party_size": 2, "total": 5400, "source": "budget_constraint", "budget_level": "standard", "strictness": "hard"}, "per_person_day": 360.0, "budget_level": "standard", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "standard", "strictness": "hard", "amount": 5400, "target_min_ratio": 0.55, "target_max_ratio": 1.0, "target_min_total": 3000, "target_max_total": 5400, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 4, "party_total": 2, "room_count": 1, "priced_nights": 4, "expected_min_total_hotels": 1800, "reported_total_hotels": 1800, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 384, "expected_total_attractions": 768, "reported_total_attractions": 668, "meal_per_person_cost_sum": 643, "expected_total_meals": 1286, "reported_total_meals": 1032, "reported_total_transportation": 200}}]`

### v3_harder_pref_fix_eval_000013
- request: 武汉 2026-05-08->2026-05-12 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 3300, "total": 3200, "diff": 100, "requested_budget": {"available": true, "amount": 5800, "scope": "total", "party_size": 2, "total": 5800, "source": "budget_constraint", "budget_level": "standard", "strictness": "hard"}, "per_person_day": 320.0, "budget_level": "standard", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "standard", "strictness": "hard", "amount": 5800, "target_min_ratio": 0.55, "target_max_ratio": 1.0, "target_min_total": 3200, "target_max_total": 5800, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 4, "party_total": 2, "room_count": 1, "priced_nights": 4, "expected_min_total_hotels": 1600, "reported_total_hotels": 1600, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 210, "expected_total_attractions": 420, "reported_total_attractions": 320, "meal_per_person_cost_sum": 1014, "expected_total_meals": 2028, "reported_total_meals": 1280, "reported_total_transportation": 100}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 210, "expected_total_attractions": 420, "reported_total_attractions": 320, "meal_per_person_cost_sum": 1014, "expected_total_meals": 2028, "reported_total_meals": 1280, "reported_total_transportation": 100}}]`

### v3_harder_pref_fix_eval_000017
- request: 苏州 2026-05-08->2026-05-12 days=5 transport=公共交通 hotel=民宿 prefs=['小众展馆', '咖啡', '艺术', '城市漫步', '特色餐厅']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 220, "expected_total_attractions": 440, "reported_total_attractions": 390, "meal_per_person_cost_sum": 846, "expected_total_meals": 1692, "reported_total_meals": 1464, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 220, "expected_total_attractions": 440, "reported_total_attractions": 390, "meal_per_person_cost_sum": 846, "expected_total_meals": 1692, "reported_total_meals": 1464, "reported_total_transportation": 200}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": true, "meal_cost_scale_ok": false, "budget_relationship_ok": false, "expected_total_hotels": 1200, "reported_total_hotels": 1200, "expected_total_attractions": 440, "reported_total_attractions": 390, "meal_scale_eval": {"ok": false, "party_total": 2, "budget_level": "comfortable", "per_person_lunch_dinner_floor": 50, "per_person_breakfast_floor": 20, "meal_count": 15, "checked_count": 15, "failure_count": 2, "failures": [{"date": "2026-05-10", "type": "breakfast", "name": "西园寺素食-面馆", "estimated_cost": 16, "min_expected_cost": 20}, {"date": "2026-05-12", "type": "breakfast", "name": "秋娟馄饨店", "estimated_cost": 14, "min_expected_cost": 20}]}}}]`

### v3_harder_pref_fix_eval_000010
- request: 西安 2026-08-04->2026-08-08 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "西安碑林博物馆", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-08-05", "day_index": 1, "name": "西安碑林博物馆"}, {"date": "2026-08-07", "day_index": 3, "name": "西安碑林博物馆"}]}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 4, "party_total": 5, "room_count": 3, "priced_nights": 4, "expected_min_total_hotels": 5400, "reported_total_hotels": 4500, "diff": -900, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 5, "hotel_room_count": 3, "attraction_ticket_sum": 264, "expected_total_attractions": 1320, "reported_total_attractions": 1325, "meal_per_person_cost_sum": 752, "expected_total_meals": 3760, "reported_total_meals": 3245, "reported_total_transportation": 1000}}]`

### v3_harder_pref_fix_eval_000008
- request: 大理 2026-05-10->2026-05-12 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 5503, "total": 5403, "diff": 100, "requested_budget": {"available": true, "amount": 9800, "scope": "total", "party_size": 3, "total": 9800, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "hard"}, "per_person_day": 600.33, "budget_level": "comfortable", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "hard", "amount": 9800, "target_min_ratio": 0.65, "target_max_ratio": 1.0, "target_min_total": 6400, "target_max_total": 9800, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 3, "room_count": 2, "priced_nights": 2, "expected_min_total_hotels": 3000, "reported_total_hotels": 3000, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 115, "expected_total_attractions": 345, "reported_total_attractions": 345, "meal_per_person_cost_sum": 465, "expected_total_meals": 1395, "reported_total_meals": 1158, "reported_total_transportation": 1000}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": true, "meal_cost_scale_ok": false, "budget_relationship_ok": false, "expected_total_hotels": 3000, "reported_total_hotels": 3000, "expected_total_attractions": 345, "reported_total_attractions": 345, "meal_scale_eval": {"ok": false, "party_total": 3, "budget_level": "comfortable", "per_person_lunch_dinner_floor": 50, "per_person_breakfast_floor": 20, "meal_count": 9, "checked_count": 9, "failure_count": 1, "failures": [{"date": "2026-05-12", "type": "breakfast", "name": "九孃豌豆粉店", "estimated_cost": 9, "min_expected_cost": 20}]}}}]`

### v3_harder_pref_fix_eval_000018
- request: 天津 2026-07-05->2026-07-07 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 2, "party_total": 3, "room_count": 2, "priced_nights": 2, "expected_min_total_hotels": 3000, "reported_total_hotels": 1500, "diff": -1500, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 140, "expected_total_attractions": 420, "reported_total_attractions": 490, "meal_per_person_cost_sum": 603, "expected_total_meals": 1809, "reported_total_meals": 1566, "reported_total_transportation": 1000}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 140, "expected_total_attractions": 420, "reported_total_attractions": 490, "meal_per_person_cost_sum": 603, "expected_total_meals": 1809, "reported_total_meals": 1566, "reported_total_transportation": 1000}}]`

### v3_harder_pref_fix_eval_000000
- request: 昆明 2026-04-06->2026-04-10 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 4, "party_total": 5, "room_count": 3, "priced_nights": 4, "expected_min_total_hotels": 4800, "reported_total_hotels": 3200, "diff": -1600, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 5, "hotel_room_count": 3, "attraction_ticket_sum": 448, "expected_total_attractions": 2240, "reported_total_attractions": 2485, "meal_per_person_cost_sum": 781, "expected_total_meals": 3905, "reported_total_meals": 3735, "reported_total_transportation": 1000}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 5, "hotel_room_count": 3, "attraction_ticket_sum": 448, "expected_total_attractions": 2240, "reported_total_attractions": 2485, "meal_per_person_cost_sum": 781, "expected_total_meals": 3905, "reported_total_meals": 3735, "reported_total_transportation": 1000}}]`

### v3_harder_pref_fix_eval_000023
- request: 大理 2026-09-03->2026-09-07 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-09-03", "type": "dinner", "name": "随园食单(善德居店)", "reason": "unknown_food_semantics"}, {"date": "2026-09-06", "type": "dinner", "name": "随园食单(善德居店)", "reason": "unknown_food_semantics"}, {"date": "2026-09-07", "type": "dinner", "name": "随园食单(善德居店)", "reason": "unknown_food_semantics"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "蒙自小黄牛米线", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-09-03", "type": "breakfast", "name": "蒙自小黄牛米线"}, {"date": "2026-09-05", "type": "breakfast", "name": "蒙自小黄牛米线(S湾海景店)"}, {"date": "2026-09-06", "type": "breakfast", "name": "蒙自小黄牛米线"}, {"date": "2026-09-07", "type": "breakfast", "name": "蒙自小黄牛米线"}]}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 195, "expected_total_attractions": 780, "reported_total_attractions": 680, "meal_per_person_cost_sum": 686, "expected_total_meals": 2744, "reported_total_meals": 1920, "reported_total_transportation": 100}}]`

### v3_harder_pref_fix_eval_000006
- request: 南京 2026-07-05->2026-07-08 days=4 transport=自驾 hotel=亲子酒店 prefs=['亲子', '动物园', '海洋馆', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 10045, "total": 9645, "diff": 400, "requested_budget": {"available": true, "amount": 7600, "scope": "total", "party_size": 3, "total": 7600, "source": "budget_constraint", "budget_level": "standard", "strictness": "hard"}, "per_person_day": 803.75, "budget_level": "standard", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "standard", "strictness": "hard", "amount": 7600, "target_min_ratio": 0.55, "target_max_ratio": 1.0, "target_min_total": 4200, "target_max_total": 7600, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": false, "user_constraint_ok": false, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 3, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 7500, "reported_total_hotels": 7500, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 163, "expected_total_attractions": 489, "reported_total_attractions": 525, "meal_per_person_cost_sum": 981, "expected_total_meals": 2943, "reported_total_meals": 1620, "reported_total_transportation": 400}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 163, "expected_total_attractions": 489, "reported_total_attractions": 525, "meal_per_person_cost_sum": 981, "expected_total_meals": 2943, "reported_total_meals": 1620, "reported_total_transportation": 400}}]`

### v3_harder_pref_fix_eval_000031
- request: 成都 2026-05-10->2026-05-13 days=4 transport=打车 hotel=高端酒店 prefs=['高端酒店', '艺术', '特色餐厅', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 2, "room_count": 1, "priced_nights": 3, "expected_min_total_hotels": 2400, "reported_total_hotels": 4800, "diff": 2400, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 245, "expected_total_attractions": 490, "reported_total_attractions": 480, "meal_per_person_cost_sum": 1598, "expected_total_meals": 3196, "reported_total_meals": 3876, "reported_total_transportation": 1000}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 245, "expected_total_attractions": 490, "reported_total_attractions": 480, "meal_per_person_cost_sum": 1598, "expected_total_meals": 3196, "reported_total_meals": 3876, "reported_total_transportation": 1000}}]`

### v3_harder_pref_fix_eval_000002
- request: 杭州 2026-04-30->2026-05-03 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '夜市', '老字号', '城市漫步']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 160, "expected_total_attractions": 640, "reported_total_attractions": 600, "meal_per_person_cost_sum": 828, "expected_total_meals": 3312, "reported_total_meals": 2448, "reported_total_transportation": 252}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 160, "expected_total_attractions": 640, "reported_total_attractions": 600, "meal_per_person_cost_sum": 828, "expected_total_meals": 3312, "reported_total_meals": 2448, "reported_total_transportation": 252}}]`

### v3_harder_pref_fix_eval_000015
- request: 南京 2026-04-06->2026-04-10 days=5 transport=公共交通 hotel=民宿 prefs=['摄影', '自然风光', '城市漫步', '本地菜']
- errors: `[{"stage": "schema", "message": "3 validation errors for TripPlan\ndays.3.attractions.1.address\n  Input should be a valid string [type=string_type, input_value=None, input_type=NoneType]\n    For further information visit https://errors.pydantic.dev/2.12/v/string_type\ndays.3.attractions.1.location\n  Input should be a valid dictionary or instance of Location [type=model_type, input_value=None, input_type=NoneType]\n    For further information visit https://errors.pydantic.dev/2.12/v/model_type\ndays.3.attractions.1.visit_duration\n  Field required [type=missing, input_value={'name': '小厨娘淮扬...ne, 'ticket_price': 105}, input_type=dict]\n    For further information visit https://errors.pydantic.dev/2.12/v/missing"}]`

### v3_harder_pref_fix_eval_000016
- request: 苏州 2026-06-05->2026-06-08 days=4 transport=自驾 hotel=亲子酒店 prefs=['亲子', '动物园', '海洋馆', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 3, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 7500, "reported_total_hotels": 3750, "diff": -3750, "covers_nights": false}}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 6300, "total": 6200, "diff": 100, "requested_budget": {"available": true, "amount": 7600, "scope": "total", "party_size": 3, "total": 7600, "source": "budget_constraint", "budget_level": "standard", "strictness": "hard"}, "per_person_day": 516.67, "budget_level": "standard", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "standard", "strictness": "hard", "amount": 7600, "target_min_ratio": 0.55, "target_max_ratio": 1.0, "target_min_total": 4200, "target_max_total": 7600, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 3, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 7500, "reported_total_hotels": 3750, "diff": -3750, "covers_nights": false}, "hotel_budget_covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 275, "expected_total_attractions": 825, "reported_total_attractions": 630, "meal_per_person_cost_sum": 657, "expected_total_meals": 1971, "reported_total_meals": 1440, "reported_total_transportation": 480}}]`

### v3_harder_pref_fix_eval_000020
- request: 杭州 2026-06-20->2026-06-24 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 4, "party_total": 5, "room_count": 3, "priced_nights": 4, "expected_min_total_hotels": 6000, "reported_total_hotels": 4000, "diff": -2000, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 5, "hotel_room_count": 3, "attraction_ticket_sum": 160, "expected_total_attractions": 800, "reported_total_attractions": 650, "meal_per_person_cost_sum": 1025, "expected_total_meals": 5125, "reported_total_meals": 4500, "reported_total_transportation": 9000}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 5, "hotel_room_count": 3, "attraction_ticket_sum": 160, "expected_total_attractions": 800, "reported_total_attractions": 650, "meal_per_person_cost_sum": 1025, "expected_total_meals": 5125, "reported_total_meals": 4500, "reported_total_transportation": 9000}}]`
