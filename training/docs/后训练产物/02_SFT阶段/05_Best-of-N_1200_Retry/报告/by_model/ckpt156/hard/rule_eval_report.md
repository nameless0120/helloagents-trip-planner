# Rule Eval Report: 260513_bestofn1200_retry_ckpt156_hard_w10

- records: 300
- generations: `training/outputs/eval/by_model/sft_qwen25_7b_v3_260513_bestofn1200_retry_ckpt156/260513_bestofn1200_retry_ckpt156_hard_w10/generations.jsonl`
- records_path: `training/data/v3/eval_hard/records.jsonl`

## Boolean Metrics

| Metric | Pass | Total | Rate |
| --- | ---: | ---: | ---: |
| accommodation_type_ok | 300 | 300 | 100.00% |
| attraction_budget_consistent | 80 | 300 | 26.67% |
| attraction_budget_party_relation_ok | 293 | 300 | 97.67% |
| attraction_count_ok | 297 | 300 | 99.00% |
| attraction_diversity_ok | 255 | 300 | 85.00% |
| attraction_grounding_ok | 296 | 300 | 98.67% |
| attraction_repeat_limit_ok | 255 | 300 | 85.00% |
| budget_arithmetic_consistent | 205 | 300 | 68.33% |
| budget_consistent | 205 | 300 | 68.33% |
| budget_level_aligned | 200 | 300 | 66.67% |
| budget_preference_aligned | 200 | 300 | 66.67% |
| budget_relationship_ok | 226 | 300 | 75.33% |
| budget_selection_ok | 140 | 300 | 46.67% |
| budget_user_constraint_ok | 248 | 300 | 82.67% |
| budget_within_user_budget | 274 | 300 | 91.33% |
| city_ok | 300 | 300 | 100.00% |
| date_range_ok | 300 | 300 | 100.00% |
| day_dates_ok | 300 | 300 | 100.00% |
| day_index_ok | 300 | 300 | 100.00% |
| days_len_ok | 300 | 300 | 100.00% |
| dpo_soft_pass | 138 | 300 | 46.00% |
| dpo_soft_recomputed_budget_pass | 94 | 300 | 31.33% |
| hard_pass | 288 | 300 | 96.00% |
| hotel_budget_covers_nights | 284 | 300 | 94.67% |
| hotel_budget_relation_ok | 290 | 300 | 96.67% |
| hotel_distance_placeholder_ok | 300 | 300 | 100.00% |
| hotel_grounding_ok | 299 | 300 | 99.67% |
| invalid_hotel_name_ok | 300 | 300 | 100.00% |
| json_extract_ok | 300 | 300 | 100.00% |
| legacy_hard_pass | 170 | 300 | 56.67% |
| location_object_ok | 300 | 300 | 100.00% |
| meal_budget_consistent | 0 | 300 | 0.00% |
| meal_complete | 300 | 300 | 100.00% |
| meal_cost_scale_ok | 240 | 300 | 80.00% |
| meal_diversity_ok | 259 | 300 | 86.33% |
| meal_grounding_ok | 297 | 300 | 99.00% |
| meal_lunch_dinner_same_day_ok | 290 | 300 | 96.67% |
| meal_repeat_limit_ok | 267 | 300 | 89.00% |
| meal_specific_ok | 300 | 300 | 100.00% |
| meal_valid_semantics_ok | 297 | 300 | 99.00% |
| middle_hotel_ok | 300 | 300 | 100.00% |
| recomputed_budget_fit_ok | 140 | 300 | 46.67% |
| recomputed_budget_hard_ok | 213 | 300 | 71.00% |
| recomputed_budget_level_aligned | 140 | 300 | 46.67% |
| recomputed_budget_preference_aligned | 140 | 300 | 46.67% |
| recomputed_budget_user_constraint_ok | 213 | 300 | 71.00% |
| recomputed_budget_within_user_budget | 250 | 300 | 83.33% |
| schema_ok | 300 | 300 | 100.00% |
| sft_budget_semantic_hard_pass | 172 | 300 | 57.33% |
| sft_hard_pass | 288 | 300 | 96.00% |
| sft_no_budget_sum_hard_pass | 288 | 300 | 96.00% |
| sft_strict_hard_pass | 0 | 300 | 0.00% |
| transportation_budget_nonnegative | 300 | 300 | 100.00% |
| weather_dates_ok | 300 | 300 | 100.00% |
| weather_match | 299 | 300 | 99.67% |

## Numeric Metrics

```json
{
  "attraction_diversity_unique_rate": {
    "avg": 0.9806,
    "p50": 1.0,
    "p90": 1.0
  },
  "attraction_grounding_rate": {
    "avg": 0.9987,
    "p50": 1.0,
    "p90": 1.0
  },
  "hotel_grounding_rate": {
    "avg": 0.9967,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_diversity_unique_rate": {
    "avg": 0.9053,
    "p50": 0.9333,
    "p90": 1.0
  },
  "meal_food_pois_grounding_rate": {
    "avg": 0.9993,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_grounding_rate": {
    "avg": 0.9993,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_semantic_valid_rate": {
    "avg": 0.9993,
    "p50": 1.0,
    "p90": 1.0
  },
  "recomputed_budget_per_person_day": {
    "avg": 916.1689,
    "p50": 920.25,
    "p90": 1448.0
  },
  "recomputed_budget_total": {
    "avg": 9733.8333,
    "p50": 9163.0,
    "p90": 16476.0
  }
}
```

## Failure Types

```json
{
  "meal_budget_inconsistent": 300,
  "attraction_budget_inconsistent": 220,
  "budget_preference_mismatch": 100,
  "budget_arithmetic_inconsistent": 95,
  "budget_relationship_mismatch": 74,
  "meal_cost_scale_too_low": 60,
  "budget_hard_constraint_exceeded": 52,
  "attraction_repeat_too_many": 45,
  "meal_repeat_too_many": 33,
  "hotel_budget_underestimated": 16,
  "meal_same_day_lunch_dinner_repeat": 10,
  "meal_invalid_name": 3,
  "too_many_attractions": 3,
  "weather_mismatch": 1
}
```

## Failure Examples

### v3_hard_realbudget_eval_000004
- request: 张家界 2026-05-11->2026-05-13 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 398, "expected_total_attractions": 398, "reported_total_attractions": 498, "meal_per_person_cost_sum": 690, "expected_total_meals": 690, "reported_total_meals": 658, "reported_total_transportation": 300}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 398, "expected_total_attractions": 398, "reported_total_attractions": 498, "meal_per_person_cost_sum": 690, "expected_total_meals": 690, "reported_total_meals": 658, "reported_total_transportation": 300}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": false, "meal_cost_scale_ok": true, "budget_relationship_ok": false, "expected_total_hotels": 2600, "reported_total_hotels": 2600, "expected_total_attractions": 398, "reported_total_attractions": 498, "meal_scale_eval": {"ok": true, "party_total": 1, "budget_level": "comfortable", "per_person_lunch_dinner_floor": 50, "breakfast_policy": "excluded_from_meal_cost_scale", "meal_count": 9, "checked_count": 6, "failure_count": 0, "failures": []}}}]`

### v3_hard_realbudget_eval_000008
- request: 大理 2026-05-11->2026-05-13 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 599, "expected_total_attractions": 1797, "reported_total_attractions": 1695, "meal_per_person_cost_sum": 782, "expected_total_meals": 2346, "reported_total_meals": 2148, "reported_total_transportation": 600}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 599, "expected_total_attractions": 1797, "reported_total_attractions": 1695, "meal_per_person_cost_sum": 782, "expected_total_meals": 2346, "reported_total_meals": 2148, "reported_total_transportation": 600}}, {"stage": "rule", "type": "budget_hard_constraint_exceeded", "details": {"part_sum": 9643, "total": 9643, "diff": 0, "requested_budget": {"available": true, "amount": 8700, "scope": "total", "party_size": 3, "total": 8700, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "hard"}, "per_person_day": 1071.44, "budget_level": "comfortable", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "hard", "amount": 8700, "target_min_ratio": 0.7, "target_max_ratio": 1.0, "target_min_total": 6100, "target_max_total": 8700, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": true, "within_user_budget": true, "user_constraint_ok": false, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 3, "room_count": 2, "priced_nights": 2, "expected_min_total_hotels": 5200, "reported_total_hotels": 5200, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_hard_realbudget_eval_000006
- request: 南京 2026-07-06->2026-07-09 days=4 transport=自驾 hotel=亲子酒店 prefs=['亲子', '动物园', '海洋馆', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 75, "expected_total_attractions": 225, "reported_total_attractions": 195, "meal_per_person_cost_sum": 871, "expected_total_meals": 2613, "reported_total_meals": 1800, "reported_total_transportation": 800}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 75, "expected_total_attractions": 225, "reported_total_attractions": 195, "meal_per_person_cost_sum": 871, "expected_total_meals": 2613, "reported_total_meals": 1800, "reported_total_transportation": 800}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": true, "meal_cost_scale_ok": false, "budget_relationship_ok": false, "expected_total_hotels": 8100, "reported_total_hotels": 8100, "expected_total_attractions": 225, "reported_total_attractions": 195, "meal_scale_eval": {"ok": false, "party_total": 3, "budget_level": "standard", "per_person_lunch_dinner_floor": 35, "breakfast_policy": "excluded_from_meal_cost_scale", "meal_count": 12, "checked_count": 8, "failure_count": 1, "failures": [{"date": "2026-07-07", "type": "lunch", "name": "小潘记鸭血粉丝汤", "estimated_cost": 34, "min_expected_cost": 35}]}}}]`

### v3_hard_realbudget_eval_000001
- request: 桂林 2026-09-04->2026-09-07 days=4 transport=打车 hotel=高端酒店 prefs=['高端酒店', '艺术', '特色餐厅', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "桂林市两江四湖景区", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-09-05", "day_index": 1, "name": "桂林市两江四湖景区"}, {"date": "2026-09-06", "day_index": 2, "name": "桂林市两江四湖景区"}]}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 1021, "expected_total_attractions": 2042, "reported_total_attractions": 2312, "meal_per_person_cost_sum": 917, "expected_total_meals": 1834, "reported_total_meals": 1814, "reported_total_transportation": 800}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 1021, "expected_total_attractions": 2042, "reported_total_attractions": 2312, "meal_per_person_cost_sum": 917, "expected_total_meals": 1834, "reported_total_meals": 1814, "reported_total_transportation": 800}}]`

### v3_hard_realbudget_eval_000002
- request: 杭州 2026-05-01->2026-05-04 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '夜市', '老字号', '城市漫步']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 160, "expected_total_attractions": 640, "reported_total_attractions": 600, "meal_per_person_cost_sum": 636, "expected_total_meals": 2544, "reported_total_meals": 2160, "reported_total_transportation": 300}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 160, "expected_total_attractions": 640, "reported_total_attractions": 600, "meal_per_person_cost_sum": 636, "expected_total_meals": 2544, "reported_total_meals": 2160, "reported_total_transportation": 300}}]`

### v3_hard_realbudget_eval_000005
- request: 广州 2026-07-06->2026-07-10 days=5 transport=公共交通 hotel=民宿 prefs=['摄影', '自然风光', '城市漫步', '本地菜']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-07-08", "lunch": "大鸽饭(体育西店)", "dinner": "大鸽饭(北京路店)"}]}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 3701, "total": 2701, "diff": 1000, "requested_budget": {"available": true, "amount": 4500, "scope": "total", "party_size": 1, "total": 4500, "source": "budget_constraint", "budget_level": "standard", "strictness": "hard"}, "per_person_day": 540.2, "budget_level": "standard", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "standard", "strictness": "hard", "amount": 4500, "target_min_ratio": 0.6, "target_max_ratio": 1.0, "target_min_total": 2700, "target_max_total": 4500, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 4, "party_total": 1, "room_count": 1, "priced_nights": 4, "expected_min_total_hotels": 1200, "reported_total_hotels": 1200, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 185, "expected_total_attractions": 185, "reported_total_attractions": 215, "meal_per_person_cost_sum": 1286, "expected_total_meals": 1286, "reported_total_meals": 1386, "reported_total_transportation": 900}}]`

### v3_hard_realbudget_eval_000010
- request: 西安 2026-08-05->2026-08-09 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "大唐不夜城", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-08-05", "day_index": 0, "name": "大唐不夜城"}, {"date": "2026-08-06", "day_index": 1, "name": "大唐不夜城"}]}, {"name_key": "西安博物院", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-08-08", "day_index": 3, "name": "西安博物院"}, {"date": "2026-08-09", "day_index": 4, "name": "西安博物院"}]}]}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 23600, "total": 23500, "diff": 100, "requested_budget": {"available": true, "amount": 30900, "scope": "total", "party_size": 5, "total": 30900, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "hard"}, "per_person_day": 940.0, "budget_level": "comfortable", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "hard", "amount": 30900, "target_min_ratio": 0.7, "target_max_ratio": 1.0, "target_min_total": 21600, "target_max_total": 30900, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 4, "party_total": 5, "room_count": 3, "priced_nights": 4, "expected_min_total_hotels": 16200, "reported_total_hotels": 16200, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 5, "hotel_room_count": 3, "attraction_ticket_sum": 199, "expected_total_attractions": 995, "reported_total_attractions": 1225, "meal_per_person_cost_sum": 786, "expected_total_meals": 3930, "reported_total_meals": 5175, "reported_total_transportation": 1000}}]`

### v3_hard_realbudget_eval_000003
- request: 西安 2025-05-07->2025-05-11 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 4, "party_total": 2, "room_count": 1, "priced_nights": 4, "expected_min_total_hotels": 1800, "reported_total_hotels": 3600, "diff": 1800, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 199, "expected_total_attractions": 398, "reported_total_attractions": 438, "meal_per_person_cost_sum": 776, "expected_total_meals": 1552, "reported_total_meals": 2004, "reported_total_transportation": 400}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 199, "expected_total_attractions": 398, "reported_total_attractions": 438, "meal_per_person_cost_sum": 776, "expected_total_meals": 1552, "reported_total_meals": 2004, "reported_total_transportation": 400}}]`

### v3_hard_realbudget_eval_000000
- request: 昆明 2026-04-07->2026-04-11 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 17200, "total": 17100, "diff": 100, "requested_budget": {"available": true, "amount": 24700, "scope": "total", "party_size": 5, "total": 24700, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "hard"}, "per_person_day": 684.0, "budget_level": "comfortable", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "hard", "amount": 24700, "target_min_ratio": 0.7, "target_max_ratio": 1.0, "target_min_total": 17300, "target_max_total": 24700, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 4, "party_total": 5, "room_count": 3, "priced_nights": 4, "expected_min_total_hotels": 7200, "reported_total_hotels": 7200, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 5, "hotel_room_count": 3, "attraction_ticket_sum": 780, "expected_total_attractions": 3900, "reported_total_attractions": 3315, "meal_per_person_cost_sum": 787, "expected_total_meals": 3935, "reported_total_meals": 4685, "reported_total_transportation": 2000}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 5, "hotel_room_count": 3, "attraction_ticket_sum": 780, "expected_total_attractions": 3900, "reported_total_attractions": 3315, "meal_per_person_cost_sum": 787, "expected_total_meals": 3935, "reported_total_meals": 4685, "reported_total_transportation": 2000}}]`

### v3_hard_realbudget_eval_000007
- request: 成都 2026-05-11->2026-05-15 days=5 transport=公共交通 hotel=民宿 prefs=['小众展馆', '咖啡', '艺术', '城市漫步', '特色餐厅']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 10998, "total": 11098, "diff": -100, "requested_budget": {"available": true, "amount": 11000, "scope": "total", "party_size": 2, "total": 11000, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "soft"}, "per_person_day": 1109.8, "budget_level": "comfortable", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "soft", "amount": 11000, "target_min_ratio": 0.7, "target_max_ratio": 1.1, "target_min_total": 7700, "target_max_total": 12100, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 4, "party_total": 2, "room_count": 1, "priced_nights": 4, "expected_min_total_hotels": 1200, "reported_total_hotels": 1200, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 1459, "expected_total_attractions": 2918, "reported_total_attractions": 2854, "meal_per_person_cost_sum": 2601, "expected_total_meals": 5202, "reported_total_meals": 5244, "reported_total_transportation": 1700}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 1459, "expected_total_attractions": 2918, "reported_total_attractions": 2854, "meal_per_person_cost_sum": 2601, "expected_total_meals": 5202, "reported_total_meals": 5244, "reported_total_transportation": 1700}}]`

### v3_hard_realbudget_eval_000011
- request: 福州 2026-06-21->2026-06-24 days=4 transport=打车 hotel=高端酒店 prefs=['高端酒店', '艺术', '特色餐厅', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 2, "room_count": 1, "priced_nights": 3, "expected_min_total_hotels": 3900, "reported_total_hotels": 7800, "diff": 3900, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 487, "expected_total_attractions": 974, "reported_total_attractions": 1154, "meal_per_person_cost_sum": 1509, "expected_total_meals": 3018, "reported_total_meals": 3836, "reported_total_transportation": 800}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 487, "expected_total_attractions": 974, "reported_total_attractions": 1154, "meal_per_person_cost_sum": 1509, "expected_total_meals": 3018, "reported_total_meals": 3836, "reported_total_transportation": 800}}]`

### v3_hard_realbudget_eval_000009
- request: 苏州 2026-04-30->2026-05-03 days=4 transport=打车 hotel=亲子酒店 prefs=['亲子', '老人友好', '博物馆', '城市公园', '特色餐厅']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 320, "expected_total_attractions": 1280, "reported_total_attractions": 1440, "meal_per_person_cost_sum": 712, "expected_total_meals": 2848, "reported_total_meals": 3248, "reported_total_transportation": 800}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 320, "expected_total_attractions": 1280, "reported_total_attractions": 1440, "meal_per_person_cost_sum": 712, "expected_total_meals": 2848, "reported_total_meals": 3248, "reported_total_transportation": 800}}]`

### v3_hard_realbudget_eval_000014
- request: 成都 2026-06-06->2026-06-08 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "悦百味·品质川菜", "count": 3, "max_allowed": 2, "occurrences": [{"date": "2026-06-06", "type": "lunch", "name": "悦百味·品质川菜(优品道店)"}, {"date": "2026-06-07", "type": "lunch", "name": "悦百味·品质川菜(悠方店)"}, {"date": "2026-06-08", "type": "lunch", "name": "悦百味·品质川菜(UPARK公园店)"}]}]}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 4334, "total": 3334, "diff": 1000, "requested_budget": {"available": true, "amount": 4300, "scope": "total", "party_size": 1, "total": 4300, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "hard"}, "per_person_day": 1111.33, "budget_level": "comfortable", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "hard", "amount": 4300, "target_min_ratio": 0.7, "target_max_ratio": 1.0, "target_min_total": 3000, "target_max_total": 4300, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 1, "room_count": 1, "priced_nights": 2, "expected_min_total_hotels": 2700, "reported_total_hotels": 2700, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 674, "expected_total_attractions": 674, "reported_total_attractions": 734, "meal_per_person_cost_sum": 942, "expected_total_meals": 942, "reported_total_meals": 700, "reported_total_transportation": 200}}]`

### v3_hard_realbudget_eval_000012
- request: 洛阳 2025-05-07->2025-05-10 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '夜市', '老字号', '城市漫步']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 5140, "total": 4140, "diff": 1000, "requested_budget": {"available": true, "amount": 5800, "scope": "total", "party_size": 4, "total": 5800, "source": "budget_constraint", "budget_level": "limited", "strictness": "hard"}, "per_person_day": 258.75, "budget_level": "limited", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "limited", "strictness": "hard", "amount": 5800, "target_min_ratio": 0.72, "target_max_ratio": 1.0, "target_min_total": 4200, "target_max_total": 5800, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 4, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 1800, "reported_total_hotels": 1800, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 298, "expected_total_attractions": 1192, "reported_total_attractions": 1008, "meal_per_person_cost_sum": 614, "expected_total_meals": 2456, "reported_total_meals": 1632, "reported_total_transportation": 700}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 298, "expected_total_attractions": 1192, "reported_total_attractions": 1008, "meal_per_person_cost_sum": 614, "expected_total_meals": 2456, "reported_total_meals": 1632, "reported_total_transportation": 700}}]`

### v3_hard_realbudget_eval_000018
- request: 天津 2026-07-06->2026-07-08 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 16187, "total": 7897, "diff": 8290, "requested_budget": {"available": true, "amount": 7900, "scope": "total", "party_size": 3, "total": 7900, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "hard"}, "per_person_day": 877.44, "budget_level": "comfortable", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "hard", "amount": 7900, "target_min_ratio": 0.7, "target_max_ratio": 1.0, "target_min_total": 5500, "target_max_total": 7900, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 3, "room_count": 2, "priced_nights": 2, "expected_min_total_hotels": 7200, "reported_total_hotels": 7200, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 851, "expected_total_attractions": 2553, "reported_total_attractions": 2493, "meal_per_person_cost_sum": 3341, "expected_total_meals": 10023, "reported_total_meals": 5894, "reported_total_transportation": 600}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 851, "expected_total_attractions": 2553, "reported_total_attractions": 2493, "meal_per_person_cost_sum": 3341, "expected_total_meals": 10023, "reported_total_meals": 5894, "reported_total_transportation": 600}}]`

### v3_hard_realbudget_eval_000016
- request: 苏州 2026-06-06->2026-06-09 days=4 transport=自驾 hotel=亲子酒店 prefs=['亲子', '动物园', '海洋馆', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "苏州丝绸博物馆", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-06-08", "day_index": 2, "name": "苏州丝绸博物馆"}, {"date": "2026-06-09", "day_index": 3, "name": "苏州丝绸博物馆"}]}]}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 11183, "total": 11283, "diff": -100, "requested_budget": {"available": true, "amount": 10000, "scope": "total", "party_size": 3, "total": 10000, "source": "budget_constraint", "budget_level": "standard", "strictness": "hard"}, "per_person_day": 940.25, "budget_level": "standard", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "standard", "strictness": "hard", "amount": 10000, "target_min_ratio": 0.6, "target_max_ratio": 1.0, "target_min_total": 6000, "target_max_total": 10000, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": false, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 3, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 8100, "reported_total_hotels": 8100, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 120, "expected_total_attractions": 360, "reported_total_attractions": 345, "meal_per_person_cost_sum": 581, "expected_total_meals": 1743, "reported_total_meals": 1938, "reported_total_transportation": 800}}]`

### v3_hard_realbudget_eval_000013
- request: 武汉 2026-05-09->2026-05-13 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 4200, "total": 4100, "diff": 100, "requested_budget": {"available": true, "amount": 6800, "scope": "total", "party_size": 2, "total": 6800, "source": "budget_constraint", "budget_level": "standard", "strictness": "hard"}, "per_person_day": 410.0, "budget_level": "standard", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "standard", "strictness": "hard", "amount": 6800, "target_min_ratio": 0.6, "target_max_ratio": 1.0, "target_min_total": 4100, "target_max_total": 6800, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 4, "party_total": 2, "room_count": 1, "priced_nights": 4, "expected_min_total_hotels": 1600, "reported_total_hotels": 1600, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 223, "expected_total_attractions": 446, "reported_total_attractions": 416, "meal_per_person_cost_sum": 940, "expected_total_meals": 1880, "reported_total_meals": 2084, "reported_total_transportation": 100}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 223, "expected_total_attractions": 446, "reported_total_attractions": 416, "meal_per_person_cost_sum": 940, "expected_total_meals": 1880, "reported_total_meals": 2084, "reported_total_transportation": 100}}]`

### v3_hard_realbudget_eval_000019
- request: 丽江 2026-05-11->2026-05-14 days=4 transport=打车 hotel=亲子酒店 prefs=['亲子', '老人友好', '博物馆', '城市公园', '特色餐厅']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 780, "expected_total_attractions": 1560, "reported_total_attractions": 1680, "meal_per_person_cost_sum": 760, "expected_total_meals": 1520, "reported_total_meals": 1306, "reported_total_transportation": 800}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 780, "expected_total_attractions": 1560, "reported_total_attractions": 1680, "meal_per_person_cost_sum": 760, "expected_total_meals": 1520, "reported_total_meals": 1306, "reported_total_transportation": 800}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": true, "meal_cost_scale_ok": false, "budget_relationship_ok": false, "expected_total_hotels": 3900, "reported_total_hotels": 3900, "expected_total_attractions": 1560, "reported_total_attractions": 1680, "meal_scale_eval": {"ok": false, "party_total": 2, "budget_level": "comfortable", "per_person_lunch_dinner_floor": 50, "breakfast_policy": "excluded_from_meal_cost_scale", "meal_count": 12, "checked_count": 8, "failure_count": 2, "failures": [{"date": "2026-05-13", "type": "lunch", "name": "鲜云集野生菌腊排骨云南菜", "estimated_cost": 41, "min_expected_cost": 50}, {"date": "2026-05-14", "type": "lunch", "name": "云老官保山火塘牛肉(丽江总店)", "estimated_cost": 34, "min_expected_cost": 50}]}}}]`

### v3_hard_realbudget_eval_000020
- request: 杭州 2026-06-21->2026-06-25 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "杭州植物园", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-06-24", "day_index": 3, "name": "杭州植物园"}, {"date": "2026-06-25", "day_index": 4, "name": "杭州植物园"}]}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 5, "hotel_room_count": 3, "attraction_ticket_sum": 170, "expected_total_attractions": 850, "reported_total_attractions": 800, "meal_per_person_cost_sum": 1140, "expected_total_meals": 5700, "reported_total_meals": 5950, "reported_total_transportation": 1000}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 5, "hotel_room_count": 3, "attraction_ticket_sum": 170, "expected_total_attractions": 850, "reported_total_attractions": 800, "meal_per_person_cost_sum": 1140, "expected_total_meals": 5700, "reported_total_meals": 5950, "reported_total_transportation": 1000}}]`

### v3_hard_realbudget_eval_000017
- request: 苏州 2026-05-09->2026-05-13 days=5 transport=公共交通 hotel=民宿 prefs=['小众展馆', '咖啡', '艺术', '城市漫步', '特色餐厅']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 6034, "total": 7034, "diff": -1000, "requested_budget": {"available": true, "amount": 10100, "scope": "total", "party_size": 2, "total": 10100, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "soft"}, "per_person_day": 703.4, "budget_level": "comfortable", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "soft", "amount": 10100, "target_min_ratio": 0.7, "target_max_ratio": 1.1, "target_min_total": 7100, "target_max_total": 11100, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 4, "party_total": 2, "room_count": 1, "priced_nights": 4, "expected_min_total_hotels": 1200, "reported_total_hotels": 1200, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 320, "expected_total_attractions": 640, "reported_total_attractions": 730, "meal_per_person_cost_sum": 927, "expected_total_meals": 1854, "reported_total_meals": 2604, "reported_total_transportation": 1500}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 320, "expected_total_attractions": 640, "reported_total_attractions": 730, "meal_per_person_cost_sum": 927, "expected_total_meals": 1854, "reported_total_meals": 2604, "reported_total_transportation": 1500}}]`
