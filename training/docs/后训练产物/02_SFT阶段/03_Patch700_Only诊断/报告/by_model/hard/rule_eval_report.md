# Rule Eval Report: 260511_high_end_context_hard_w10

- records: 300
- generations: `training/outputs/eval/by_model/sft_qwen25_7b_v3_260511_patch700_only_from_lr6e5_lr1e5/260511_high_end_context_hard_w10/generations.jsonl`
- records_path: `training/data/v3/eval_hard/records.jsonl`

## Boolean Metrics

| Metric | Pass | Total | Rate |
| --- | ---: | ---: | ---: |
| accommodation_type_ok | 299 | 299 | 100.00% |
| attraction_budget_consistent | 102 | 299 | 34.11% |
| attraction_budget_party_relation_ok | 280 | 299 | 93.65% |
| attraction_count_ok | 299 | 299 | 100.00% |
| attraction_diversity_ok | 244 | 299 | 81.61% |
| attraction_grounding_ok | 298 | 299 | 99.67% |
| attraction_repeat_limit_ok | 244 | 299 | 81.61% |
| budget_arithmetic_consistent | 241 | 299 | 80.60% |
| budget_consistent | 241 | 299 | 80.60% |
| budget_level_aligned | 173 | 299 | 57.86% |
| budget_preference_aligned | 173 | 299 | 57.86% |
| budget_relationship_ok | 173 | 299 | 57.86% |
| budget_selection_ok | 143 | 299 | 47.83% |
| budget_user_constraint_ok | 243 | 299 | 81.27% |
| budget_within_user_budget | 281 | 299 | 93.98% |
| city_ok | 299 | 299 | 100.00% |
| date_range_ok | 299 | 299 | 100.00% |
| day_dates_ok | 298 | 299 | 99.67% |
| day_index_ok | 299 | 299 | 100.00% |
| days_len_ok | 298 | 299 | 99.67% |
| dpo_soft_pass | 107 | 299 | 35.79% |
| dpo_soft_recomputed_budget_pass | 89 | 299 | 29.77% |
| hard_pass | 294 | 299 | 98.33% |
| hotel_budget_covers_nights | 263 | 299 | 87.96% |
| hotel_budget_relation_ok | 269 | 299 | 89.97% |
| hotel_distance_placeholder_ok | 299 | 299 | 100.00% |
| hotel_grounding_ok | 299 | 299 | 100.00% |
| invalid_hotel_name_ok | 299 | 299 | 100.00% |
| json_extract_ok | 300 | 300 | 100.00% |
| legacy_hard_pass | 165 | 299 | 55.18% |
| location_object_ok | 299 | 299 | 100.00% |
| meal_budget_consistent | 2 | 299 | 0.67% |
| meal_complete | 299 | 299 | 100.00% |
| meal_cost_scale_ok | 198 | 299 | 66.22% |
| meal_diversity_ok | 240 | 299 | 80.27% |
| meal_grounding_ok | 297 | 299 | 99.33% |
| meal_lunch_dinner_same_day_ok | 280 | 299 | 93.65% |
| meal_repeat_limit_ok | 251 | 299 | 83.95% |
| meal_specific_ok | 299 | 299 | 100.00% |
| meal_valid_semantics_ok | 299 | 299 | 100.00% |
| middle_hotel_ok | 299 | 299 | 100.00% |
| recomputed_budget_fit_ok | 143 | 299 | 47.83% |
| recomputed_budget_hard_ok | 231 | 299 | 77.26% |
| recomputed_budget_level_aligned | 143 | 299 | 47.83% |
| recomputed_budget_preference_aligned | 143 | 299 | 47.83% |
| recomputed_budget_user_constraint_ok | 231 | 299 | 77.26% |
| recomputed_budget_within_user_budget | 272 | 299 | 90.97% |
| schema_ok | 299 | 300 | 99.67% |
| sft_budget_semantic_hard_pass | 125 | 299 | 41.81% |
| sft_hard_pass | 294 | 299 | 98.33% |
| sft_no_budget_sum_hard_pass | 294 | 299 | 98.33% |
| sft_strict_hard_pass | 1 | 299 | 0.33% |
| transportation_budget_nonnegative | 299 | 299 | 100.00% |
| weather_dates_ok | 298 | 299 | 99.67% |
| weather_match | 297 | 299 | 99.33% |

## Numeric Metrics

```json
{
  "attraction_diversity_unique_rate": {
    "avg": 0.9706,
    "p50": 1.0,
    "p90": 1.0
  },
  "attraction_grounding_rate": {
    "avg": 0.9995,
    "p50": 1.0,
    "p90": 1.0
  },
  "hotel_grounding_rate": {
    "avg": 1.0,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_diversity_unique_rate": {
    "avg": 0.8666,
    "p50": 0.9167,
    "p90": 1.0
  },
  "meal_food_pois_grounding_rate": {
    "avg": 0.9994,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_grounding_rate": {
    "avg": 0.9994,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_semantic_valid_rate": {
    "avg": 1.0,
    "p50": 1.0,
    "p90": 1.0
  },
  "recomputed_budget_per_person_day": {
    "avg": 850.3185,
    "p50": 860.4,
    "p90": 1340.67
  },
  "recomputed_budget_total": {
    "avg": 9068.1405,
    "p50": 8420.0,
    "p90": 15995.0
  }
}
```

## Failure Types

```json
{
  "meal_budget_inconsistent": 297,
  "attraction_budget_inconsistent": 197,
  "budget_preference_mismatch": 126,
  "budget_relationship_mismatch": 126,
  "meal_cost_scale_too_low": 101,
  "budget_arithmetic_inconsistent": 58,
  "budget_hard_constraint_exceeded": 56,
  "attraction_repeat_too_many": 55,
  "meal_repeat_too_many": 48,
  "hotel_budget_underestimated": 36,
  "meal_same_day_lunch_dinner_repeat": 19,
  "weather_mismatch": 2,
  "meal_grounding_miss": 2,
  "schema": 1
}
```

## Failure Examples

### v3_hard_realbudget_eval_000004
- request: 张家界 2026-05-11->2026-05-13 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "张家界市博物馆", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-05-11", "day_index": 0, "name": "张家界市博物馆"}, {"date": "2026-05-13", "day_index": 2, "name": "张家界市博物馆"}]}]}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 346, "expected_total_attractions": 346, "reported_total_attractions": 346, "meal_per_person_cost_sum": 742, "expected_total_meals": 742, "reported_total_meals": 518, "reported_total_transportation": 200}}, {"stage": "rule", "type": "budget_hard_constraint_exceeded", "details": {"part_sum": 3664, "total": 3664, "diff": 0, "requested_budget": {"available": true, "amount": 3200, "scope": "total", "party_size": 1, "total": 3200, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "hard"}, "per_person_day": 1221.33, "budget_level": "comfortable", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "hard", "amount": 3200, "target_min_ratio": 0.7, "target_max_ratio": 1.0, "target_min_total": 2200, "target_max_total": 3200, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": true, "within_user_budget": true, "user_constraint_ok": false, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 1, "room_count": 1, "priced_nights": 2, "expected_min_total_hotels": 2600, "reported_total_hotels": 2600, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_hard_realbudget_eval_000008
- request: 大理 2026-05-11->2026-05-13 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 395, "expected_total_attractions": 1185, "reported_total_attractions": 1245, "meal_per_person_cost_sum": 742, "expected_total_meals": 2226, "reported_total_meals": 1932, "reported_total_transportation": 600}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 395, "expected_total_attractions": 1185, "reported_total_attractions": 1245, "meal_per_person_cost_sum": 742, "expected_total_meals": 2226, "reported_total_meals": 1932, "reported_total_transportation": 600}}, {"stage": "rule", "type": "budget_hard_constraint_exceeded", "details": {"part_sum": 8977, "total": 8977, "diff": 0, "requested_budget": {"available": true, "amount": 8700, "scope": "total", "party_size": 3, "total": 8700, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "hard"}, "per_person_day": 997.44, "budget_level": "comfortable", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "hard", "amount": 8700, "target_min_ratio": 0.7, "target_max_ratio": 1.0, "target_min_total": 6100, "target_max_total": 8700, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": true, "within_user_budget": true, "user_constraint_ok": false, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 3, "room_count": 2, "priced_nights": 2, "expected_min_total_hotels": 5200, "reported_total_hotels": 5200, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_hard_realbudget_eval_000006
- request: 南京 2026-07-06->2026-07-09 days=4 transport=自驾 hotel=亲子酒店 prefs=['亲子', '动物园', '海洋馆', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "weather_mismatch", "details": [{"date": "2026-07-09", "issue": "missing_weather_row"}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 121, "expected_total_attractions": 363, "reported_total_attractions": 408, "meal_per_person_cost_sum": 517, "expected_total_meals": 1551, "reported_total_meals": 1629, "reported_total_transportation": 1000}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 121, "expected_total_attractions": 363, "reported_total_attractions": 408, "meal_per_person_cost_sum": 517, "expected_total_meals": 1551, "reported_total_meals": 1629, "reported_total_transportation": 1000}}]`

### v3_hard_realbudget_eval_000002
- request: 杭州 2026-05-01->2026-05-04 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '夜市', '老字号', '城市漫步']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 189, "expected_total_attractions": 756, "reported_total_attractions": 676, "meal_per_person_cost_sum": 772, "expected_total_meals": 3088, "reported_total_meals": 2324, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 189, "expected_total_attractions": 756, "reported_total_attractions": 676, "meal_per_person_cost_sum": 772, "expected_total_meals": 3088, "reported_total_meals": 2324, "reported_total_transportation": 200}}]`

### v3_hard_realbudget_eval_000001
- request: 桂林 2026-09-04->2026-09-07 days=4 transport=打车 hotel=高端酒店 prefs=['高端酒店', '艺术', '特色餐厅', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 9802, "total": 10702, "diff": -900, "requested_budget": {"available": true, "amount": 13100, "scope": "total", "party_size": 2, "total": 13100, "source": "budget_constraint", "budget_level": "premium", "strictness": "soft"}, "per_person_day": 1337.75, "budget_level": "premium", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "premium", "strictness": "soft", "amount": 13100, "target_min_ratio": 0.75, "target_max_ratio": 1.12, "target_min_total": 9800, "target_max_total": 14700, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 2, "room_count": 1, "priced_nights": 3, "expected_min_total_hotels": 3900, "reported_total_hotels": 3900, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 1214, "expected_total_attractions": 2428, "reported_total_attractions": 2328, "meal_per_person_cost_sum": 1373, "expected_total_meals": 2746, "reported_total_meals": 2874, "reported_total_transportation": 700}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 1214, "expected_total_attractions": 2428, "reported_total_attractions": 2328, "meal_per_person_cost_sum": 1373, "expected_total_meals": 2746, "reported_total_meals": 2874, "reported_total_transportation": 700}}]`

### v3_hard_realbudget_eval_000005
- request: 广州 2026-07-06->2026-07-10 days=5 transport=公共交通 hotel=民宿 prefs=['摄影', '自然风光', '城市漫步', '本地菜']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 3009, "total": 2909, "diff": 100, "requested_budget": {"available": true, "amount": 4500, "scope": "total", "party_size": 1, "total": 4500, "source": "budget_constraint", "budget_level": "standard", "strictness": "hard"}, "per_person_day": 581.8, "budget_level": "standard", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "standard", "strictness": "hard", "amount": 4500, "target_min_ratio": 0.6, "target_max_ratio": 1.0, "target_min_total": 2700, "target_max_total": 4500, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 4, "party_total": 1, "room_count": 1, "priced_nights": 4, "expected_min_total_hotels": 1200, "reported_total_hotels": 1200, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 331, "expected_total_attractions": 331, "reported_total_attractions": 321, "meal_per_person_cost_sum": 1365, "expected_total_meals": 1365, "reported_total_meals": 1288, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 331, "expected_total_attractions": 331, "reported_total_attractions": 321, "meal_per_person_cost_sum": 1365, "expected_total_meals": 1365, "reported_total_meals": 1288, "reported_total_transportation": 200}}]`

### v3_hard_realbudget_eval_000007
- request: 成都 2026-05-11->2026-05-15 days=5 transport=公共交通 hotel=民宿 prefs=['小众展馆', '咖啡', '艺术', '城市漫步', '特色餐厅']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 9200, "total": 8200, "diff": 1000, "requested_budget": {"available": true, "amount": 11000, "scope": "total", "party_size": 2, "total": 11000, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "soft"}, "per_person_day": 820.0, "budget_level": "comfortable", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "soft", "amount": 11000, "target_min_ratio": 0.7, "target_max_ratio": 1.1, "target_min_total": 7700, "target_max_total": 12100, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 4, "party_total": 2, "room_count": 1, "priced_nights": 4, "expected_min_total_hotels": 1200, "reported_total_hotels": 1200, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 495, "expected_total_attractions": 990, "reported_total_attractions": 1032, "meal_per_person_cost_sum": 2712, "expected_total_meals": 5424, "reported_total_meals": 5968, "reported_total_transportation": 1000}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 495, "expected_total_attractions": 990, "reported_total_attractions": 1032, "meal_per_person_cost_sum": 2712, "expected_total_meals": 5424, "reported_total_meals": 5968, "reported_total_transportation": 1000}}]`

### v3_hard_realbudget_eval_000003
- request: 西安 2025-05-07->2025-05-11 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 199, "expected_total_attractions": 398, "reported_total_attractions": 348, "meal_per_person_cost_sum": 561, "expected_total_meals": 1122, "reported_total_meals": 1320, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 199, "expected_total_attractions": 398, "reported_total_attractions": 348, "meal_per_person_cost_sum": 561, "expected_total_meals": 1122, "reported_total_meals": 1320, "reported_total_transportation": 200}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": true, "meal_cost_scale_ok": false, "budget_relationship_ok": false, "expected_total_hotels": 1800, "reported_total_hotels": 1800, "expected_total_attractions": 398, "reported_total_attractions": 348, "meal_scale_eval": {"ok": false, "party_total": 2, "budget_level": "standard", "per_person_lunch_dinner_floor": 35, "breakfast_policy": "excluded_from_meal_cost_scale", "meal_count": 15, "checked_count": 10, "failure_count": 4, "failures": [{"date": "2025-05-07", "type": "lunch", "name": "李志贤灌汤包子", "estimated_cost": 20, "min_expected_cost": 35}, {"date": "2025-05-08", "type": "lunch", "name": "崔少野猫耳朵炒面(十里锦绣店)", "estimated_cost": 18, "min_expected_cost": 35}, {"date": "2025-05-09", "type": "lunch", "name": "马洪小炒泡馍馆", "estimated_cost": 31, "min_expected_cost": 35}, {"date": "2025-05-09", "type": "dinner", "name": "天发芽何记葫芦头泡馍", "estimated_cost": 34, "min_expected_cost": 35}]}}}]`

### v3_hard_realbudget_eval_000010
- request: 西安 2026-08-05->2026-08-09 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "西安城市运动公园", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-08-08", "day_index": 3, "name": "西安城市运动公园"}, {"date": "2026-08-09", "day_index": 4, "name": "西安城市运动公园"}]}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 4, "party_total": 5, "room_count": 3, "priced_nights": 4, "expected_min_total_hotels": 16200, "reported_total_hotels": 10800, "diff": -5400, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 5, "hotel_room_count": 3, "attraction_ticket_sum": 199, "expected_total_attractions": 995, "reported_total_attractions": 1225, "meal_per_person_cost_sum": 622, "expected_total_meals": 3110, "reported_total_meals": 3875, "reported_total_transportation": 1000}}]`

### v3_hard_realbudget_eval_000000
- request: 昆明 2026-04-07->2026-04-11 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 13400, "total": 13300, "diff": 100, "requested_budget": {"available": true, "amount": 24700, "scope": "total", "party_size": 5, "total": 24700, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "hard"}, "per_person_day": 532.0, "budget_level": "comfortable", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "hard", "amount": 24700, "target_min_ratio": 0.7, "target_max_ratio": 1.0, "target_min_total": 17300, "target_max_total": 24700, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 4, "party_total": 5, "room_count": 3, "priced_nights": 4, "expected_min_total_hotels": 7200, "reported_total_hotels": 7200, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 5, "hotel_room_count": 3, "attraction_ticket_sum": 50, "expected_total_attractions": 250, "reported_total_attractions": 250, "meal_per_person_cost_sum": 754, "expected_total_meals": 3770, "reported_total_meals": 4750, "reported_total_transportation": 1200}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": true, "meal_cost_scale_ok": false, "budget_relationship_ok": false, "expected_total_hotels": 7200, "reported_total_hotels": 7200, "expected_total_attractions": 250, "reported_total_attractions": 250, "meal_scale_eval": {"ok": false, "party_total": 5, "budget_level": "comfortable", "per_person_lunch_dinner_floor": 50, "breakfast_policy": "excluded_from_meal_cost_scale", "meal_count": 15, "checked_count": 10, "failure_count": 1, "failures": [{"date": "2026-04-11", "type": "lunch", "name": "嘉华鲜花饼店(南屏步行街店)", "estimated_cost": 31, "min_expected_cost": 50}]}}}]`

### v3_hard_realbudget_eval_000011
- request: 福州 2026-06-21->2026-06-24 days=4 transport=打车 hotel=高端酒店 prefs=['高端酒店', '艺术', '特色餐厅', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 2, "room_count": 1, "priced_nights": 3, "expected_min_total_hotels": 3900, "reported_total_hotels": 7800, "diff": 3900, "covers_nights": false}}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 12962, "total": 13062, "diff": -100, "requested_budget": {"available": true, "amount": 13500, "scope": "total", "party_size": 2, "total": 13500, "source": "budget_constraint", "budget_level": "premium", "strictness": "soft"}, "per_person_day": 1632.75, "budget_level": "premium", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "premium", "strictness": "soft", "amount": 13500, "target_min_ratio": 0.75, "target_max_ratio": 1.12, "target_min_total": 10100, "target_max_total": 15100, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 2, "room_count": 1, "priced_nights": 3, "expected_min_total_hotels": 3900, "reported_total_hotels": 7800, "diff": 3900, "covers_nights": false}, "hotel_budget_covers_nights": false}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 147, "expected_total_attractions": 294, "reported_total_attractions": 294, "meal_per_person_cost_sum": 1501, "expected_total_meals": 3002, "reported_total_meals": 3868, "reported_total_transportation": 1000}}]`

### v3_hard_realbudget_eval_000009
- request: 苏州 2026-04-30->2026-05-03 days=4 transport=打车 hotel=亲子酒店 prefs=['亲子', '老人友好', '博物馆', '城市公园', '特色餐厅']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 135, "expected_total_attractions": 540, "reported_total_attractions": 500, "meal_per_person_cost_sum": 730, "expected_total_meals": 2920, "reported_total_meals": 3192, "reported_total_transportation": 1000}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 135, "expected_total_attractions": 540, "reported_total_attractions": 500, "meal_per_person_cost_sum": 730, "expected_total_meals": 2920, "reported_total_meals": 3192, "reported_total_transportation": 1000}}]`

### v3_hard_realbudget_eval_000014
- request: 成都 2026-06-06->2026-06-08 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 3868, "total": 4068, "diff": -200, "requested_budget": {"available": true, "amount": 4300, "scope": "total", "party_size": 1, "total": 4300, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "hard"}, "per_person_day": 1356.0, "budget_level": "comfortable", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "hard", "amount": 4300, "target_min_ratio": 0.7, "target_max_ratio": 1.0, "target_min_total": 3000, "target_max_total": 4300, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 1, "room_count": 1, "priced_nights": 2, "expected_min_total_hotels": 2700, "reported_total_hotels": 2700, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 110, "expected_total_attractions": 110, "reported_total_attractions": 110, "meal_per_person_cost_sum": 839, "expected_total_meals": 839, "reported_total_meals": 758, "reported_total_transportation": 300}}]`

### v3_hard_realbudget_eval_000012
- request: 洛阳 2025-05-07->2025-05-10 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '夜市', '老字号', '城市漫步']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 347, "expected_total_attractions": 1388, "reported_total_attractions": 1408, "meal_per_person_cost_sum": 561, "expected_total_meals": 2244, "reported_total_meals": 2100, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 347, "expected_total_attractions": 1388, "reported_total_attractions": 1408, "meal_per_person_cost_sum": 561, "expected_total_meals": 2244, "reported_total_meals": 2100, "reported_total_transportation": 200}}]`

### v3_hard_realbudget_eval_000018
- request: 天津 2026-07-06->2026-07-08 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 140, "expected_total_attractions": 420, "reported_total_attractions": 450, "meal_per_person_cost_sum": 4012, "expected_total_meals": 12036, "reported_total_meals": 7659, "reported_total_transportation": 600}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 140, "expected_total_attractions": 420, "reported_total_attractions": 450, "meal_per_person_cost_sum": 4012, "expected_total_meals": 12036, "reported_total_meals": 7659, "reported_total_transportation": 600}}, {"stage": "rule", "type": "budget_hard_constraint_exceeded", "details": {"part_sum": 15909, "total": 15909, "diff": 0, "requested_budget": {"available": true, "amount": 7900, "scope": "total", "party_size": 3, "total": 7900, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "hard"}, "per_person_day": 1767.67, "budget_level": "comfortable", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "hard", "amount": 7900, "target_min_ratio": 0.7, "target_max_ratio": 1.0, "target_min_total": 5500, "target_max_total": 7900, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": true, "within_user_budget": false, "user_constraint_ok": false, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 3, "room_count": 2, "priced_nights": 2, "expected_min_total_hotels": 7200, "reported_total_hotels": 7200, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_hard_realbudget_eval_000016
- request: 苏州 2026-06-06->2026-06-09 days=4 transport=自驾 hotel=亲子酒店 prefs=['亲子', '动物园', '海洋馆', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 409, "expected_total_attractions": 1227, "reported_total_attractions": 1287, "meal_per_person_cost_sum": 683, "expected_total_meals": 2049, "reported_total_meals": 2103, "reported_total_transportation": 1000}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 409, "expected_total_attractions": 1227, "reported_total_attractions": 1287, "meal_per_person_cost_sum": 683, "expected_total_meals": 2049, "reported_total_meals": 2103, "reported_total_transportation": 1000}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": true, "meal_cost_scale_ok": false, "budget_relationship_ok": false, "expected_total_hotels": 8100, "reported_total_hotels": 8100, "expected_total_attractions": 1227, "reported_total_attractions": 1287, "meal_scale_eval": {"ok": false, "party_total": 3, "budget_level": "standard", "per_person_lunch_dinner_floor": 35, "breakfast_policy": "excluded_from_meal_cost_scale", "meal_count": 12, "checked_count": 8, "failure_count": 1, "failures": [{"date": "2026-06-09", "type": "dinner", "name": "万福兴(东中市总店)", "estimated_cost": 20, "min_expected_cost": 35}]}}}]`

### v3_hard_realbudget_eval_000019
- request: 丽江 2026-05-11->2026-05-14 days=4 transport=打车 hotel=亲子酒店 prefs=['亲子', '老人友好', '博物馆', '城市公园', '特色餐厅']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "黑龙潭", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-05-11", "day_index": 0, "name": "黑龙潭"}, {"date": "2026-05-14", "day_index": 3, "name": "黑龙潭"}]}]}, {"stage": "rule", "type": "meal_grounding_miss", "details": [{"date": "2026-05-14", "type": "dinner", "name": "云西小锅饭·云南民俗风味餐厅"}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 500, "expected_total_attractions": 1000, "reported_total_attractions": 840, "meal_per_person_cost_sum": 613, "expected_total_meals": 1226, "reported_total_meals": 1500, "reported_total_transportation": 1300}}]`

### v3_hard_realbudget_eval_000013
- request: 武汉 2026-05-09->2026-05-13 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 210, "expected_total_attractions": 420, "reported_total_attractions": 380, "meal_per_person_cost_sum": 728, "expected_total_meals": 1456, "reported_total_meals": 1724, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 210, "expected_total_attractions": 420, "reported_total_attractions": 380, "meal_per_person_cost_sum": 728, "expected_total_meals": 1456, "reported_total_meals": 1724, "reported_total_transportation": 200}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": true, "meal_cost_scale_ok": false, "budget_relationship_ok": false, "expected_total_hotels": 1600, "reported_total_hotels": 1600, "expected_total_attractions": 420, "reported_total_attractions": 380, "meal_scale_eval": {"ok": false, "party_total": 2, "budget_level": "standard", "per_person_lunch_dinner_floor": 35, "breakfast_policy": "excluded_from_meal_cost_scale", "meal_count": 15, "checked_count": 10, "failure_count": 3, "failures": [{"date": "2026-05-09", "type": "lunch", "name": "刘聋子牛肉粉馆(汉阳龙兴东街店)", "estimated_cost": 27, "min_expected_cost": 35}, {"date": "2026-05-10", "type": "lunch", "name": "小鱼号酸菜鱼(积玉桥店)", "estimated_cost": 25, "min_expected_cost": 35}, {"date": "2026-05-11", "type": "lunch", "name": "川味麻辣香锅.万州烤鱼(武大店)", "estimated_cost": 33, "min_expected_cost": 35}]}}}]`

### v3_hard_realbudget_eval_000017
- request: 苏州 2026-05-09->2026-05-13 days=5 transport=公共交通 hotel=民宿 prefs=['小众展馆', '咖啡', '艺术', '城市漫步', '特色餐厅']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 315, "expected_total_attractions": 630, "reported_total_attractions": 690, "meal_per_person_cost_sum": 858, "expected_total_meals": 1716, "reported_total_meals": 2480, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 315, "expected_total_attractions": 630, "reported_total_attractions": 690, "meal_per_person_cost_sum": 858, "expected_total_meals": 1716, "reported_total_meals": 2480, "reported_total_transportation": 200}}, {"stage": "rule", "type": "budget_preference_mismatch", "details": {"part_sum": 4570, "total": 4570, "diff": 0, "requested_budget": {"available": true, "amount": 10100, "scope": "total", "party_size": 2, "total": 10100, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "soft"}, "per_person_day": 457.0, "budget_level": "comfortable", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "soft", "amount": 10100, "target_min_ratio": 0.7, "target_max_ratio": 1.1, "target_min_total": 7100, "target_max_total": 11100, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": true, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 4, "party_total": 2, "room_count": 1, "priced_nights": 4, "expected_min_total_hotels": 1200, "reported_total_hotels": 1200, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_hard_realbudget_eval_000020
- request: 杭州 2026-06-21->2026-06-25 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "杭州植物园", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-06-23", "day_index": 2, "name": "杭州植物园"}, {"date": "2026-06-25", "day_index": 4, "name": "杭州植物园"}]}]}, {"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-06-24", "lunch": "杨记肴·精致浙菜(东站店)", "dinner": "杨记肴·精致浙菜(西湖文化广场店)"}, {"date": "2026-06-25", "lunch": "老姑东北人(立涛园店)", "dinner": "老姑东北人(立涛园店)"}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 5, "hotel_room_count": 3, "attraction_ticket_sum": 95, "expected_total_attractions": 475, "reported_total_attractions": 425, "meal_per_person_cost_sum": 1094, "expected_total_meals": 5470, "reported_total_meals": 4830, "reported_total_transportation": 1000}}]`
