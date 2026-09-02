# Rule Eval Report: 260513_rerank_final1200_hard_w10

- records: 300
- generations: `training/outputs/eval/by_model/sft_qwen25_7b_v3_260513_rerank_final1200/260513_rerank_final1200_hard_w10/generations.jsonl`
- records_path: `training/data/v3/eval_hard/records.jsonl`

## Boolean Metrics

| Metric | Pass | Total | Rate |
| --- | ---: | ---: | ---: |
| accommodation_type_ok | 300 | 300 | 100.00% |
| attraction_budget_consistent | 81 | 300 | 27.00% |
| attraction_budget_party_relation_ok | 294 | 300 | 98.00% |
| attraction_count_ok | 298 | 300 | 99.33% |
| attraction_diversity_ok | 279 | 300 | 93.00% |
| attraction_grounding_ok | 299 | 300 | 99.67% |
| attraction_repeat_limit_ok | 279 | 300 | 93.00% |
| budget_arithmetic_consistent | 234 | 300 | 78.00% |
| budget_consistent | 234 | 300 | 78.00% |
| budget_level_aligned | 222 | 300 | 74.00% |
| budget_preference_aligned | 222 | 300 | 74.00% |
| budget_relationship_ok | 248 | 300 | 82.67% |
| budget_selection_ok | 172 | 300 | 57.33% |
| budget_user_constraint_ok | 256 | 300 | 85.33% |
| budget_within_user_budget | 275 | 300 | 91.67% |
| city_ok | 300 | 300 | 100.00% |
| date_range_ok | 300 | 300 | 100.00% |
| day_dates_ok | 300 | 300 | 100.00% |
| day_index_ok | 300 | 300 | 100.00% |
| days_len_ok | 300 | 300 | 100.00% |
| dpo_soft_pass | 182 | 300 | 60.67% |
| dpo_soft_recomputed_budget_pass | 135 | 300 | 45.00% |
| hard_pass | 295 | 300 | 98.33% |
| hotel_budget_covers_nights | 284 | 300 | 94.67% |
| hotel_budget_relation_ok | 291 | 300 | 97.00% |
| hotel_distance_placeholder_ok | 300 | 300 | 100.00% |
| hotel_grounding_ok | 299 | 300 | 99.67% |
| invalid_hotel_name_ok | 300 | 300 | 100.00% |
| json_extract_ok | 300 | 300 | 100.00% |
| legacy_hard_pass | 202 | 300 | 67.33% |
| location_object_ok | 300 | 300 | 100.00% |
| meal_budget_consistent | 1 | 300 | 0.33% |
| meal_complete | 300 | 300 | 100.00% |
| meal_cost_scale_ok | 260 | 300 | 86.67% |
| meal_diversity_ok | 268 | 300 | 89.33% |
| meal_grounding_ok | 299 | 300 | 99.67% |
| meal_lunch_dinner_same_day_ok | 297 | 300 | 99.00% |
| meal_repeat_limit_ok | 270 | 300 | 90.00% |
| meal_specific_ok | 300 | 300 | 100.00% |
| meal_valid_semantics_ok | 299 | 300 | 99.67% |
| middle_hotel_ok | 300 | 300 | 100.00% |
| recomputed_budget_fit_ok | 172 | 300 | 57.33% |
| recomputed_budget_hard_ok | 224 | 300 | 74.67% |
| recomputed_budget_level_aligned | 172 | 300 | 57.33% |
| recomputed_budget_preference_aligned | 172 | 300 | 57.33% |
| recomputed_budget_user_constraint_ok | 224 | 300 | 74.67% |
| recomputed_budget_within_user_budget | 262 | 300 | 87.33% |
| schema_ok | 300 | 300 | 100.00% |
| sft_budget_semantic_hard_pass | 203 | 300 | 67.67% |
| sft_hard_pass | 295 | 300 | 98.33% |
| sft_no_budget_sum_hard_pass | 295 | 300 | 98.33% |
| sft_strict_hard_pass | 1 | 300 | 0.33% |
| transportation_budget_nonnegative | 300 | 300 | 100.00% |
| weather_dates_ok | 300 | 300 | 100.00% |
| weather_match | 300 | 300 | 100.00% |

## Numeric Metrics

```json
{
  "attraction_diversity_unique_rate": {
    "avg": 0.9914,
    "p50": 1.0,
    "p90": 1.0
  },
  "attraction_grounding_rate": {
    "avg": 0.9997,
    "p50": 1.0,
    "p90": 1.0
  },
  "hotel_grounding_rate": {
    "avg": 0.9992,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_diversity_unique_rate": {
    "avg": 0.8998,
    "p50": 0.9333,
    "p90": 1.0
  },
  "meal_food_pois_grounding_rate": {
    "avg": 0.9996,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_grounding_rate": {
    "avg": 0.9996,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_semantic_valid_rate": {
    "avg": 0.9996,
    "p50": 1.0,
    "p90": 1.0
  },
  "recomputed_budget_per_person_day": {
    "avg": 916.0932,
    "p50": 932.0,
    "p90": 1392.8
  },
  "recomputed_budget_total": {
    "avg": 9850.6433,
    "p50": 9379.0,
    "p90": 17675.0
  }
}
```

## Failure Types

```json
{
  "meal_budget_inconsistent": 299,
  "attraction_budget_inconsistent": 219,
  "budget_preference_mismatch": 78,
  "budget_arithmetic_inconsistent": 66,
  "budget_relationship_mismatch": 52,
  "budget_hard_constraint_exceeded": 44,
  "meal_cost_scale_too_low": 40,
  "meal_repeat_too_many": 30,
  "attraction_repeat_too_many": 21,
  "hotel_budget_underestimated": 16,
  "meal_same_day_lunch_dinner_repeat": 3,
  "too_many_attractions": 2,
  "meal_invalid_name": 1
}
```

## Failure Examples

### v3_hard_realbudget_eval_000000
- request: 昆明 2026-04-07->2026-04-11 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 5, "hotel_room_count": 3, "attraction_ticket_sum": 766, "expected_total_attractions": 3830, "reported_total_attractions": 3165, "meal_per_person_cost_sum": 1079, "expected_total_meals": 5395, "reported_total_meals": 5150, "reported_total_transportation": 2000}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 5, "hotel_room_count": 3, "attraction_ticket_sum": 766, "expected_total_attractions": 3830, "reported_total_attractions": 3165, "meal_per_person_cost_sum": 1079, "expected_total_meals": 5395, "reported_total_meals": 5150, "reported_total_transportation": 2000}}]`

### v3_hard_realbudget_eval_000001
- request: 桂林 2026-09-04->2026-09-07 days=4 transport=打车 hotel=高端酒店 prefs=['高端酒店', '艺术', '特色餐厅', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 625, "expected_total_attractions": 1250, "reported_total_attractions": 1430, "meal_per_person_cost_sum": 1204, "expected_total_meals": 2408, "reported_total_meals": 2664, "reported_total_transportation": 800}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 625, "expected_total_attractions": 1250, "reported_total_attractions": 1430, "meal_per_person_cost_sum": 1204, "expected_total_meals": 2408, "reported_total_meals": 2664, "reported_total_transportation": 800}}, {"stage": "rule", "type": "budget_preference_mismatch", "details": {"part_sum": 8794, "total": 8794, "diff": 0, "requested_budget": {"available": true, "amount": 13100, "scope": "total", "party_size": 2, "total": 13100, "source": "budget_constraint", "budget_level": "premium", "strictness": "soft"}, "per_person_day": 1099.25, "budget_level": "premium", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "premium", "strictness": "soft", "amount": 13100, "target_min_ratio": 0.75, "target_max_ratio": 1.12, "target_min_total": 9800, "target_max_total": 14700, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": true, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 2, "room_count": 1, "priced_nights": 3, "expected_min_total_hotels": 3900, "reported_total_hotels": 3900, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_hard_realbudget_eval_000003
- request: 西安 2025-05-07->2025-05-11 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 319, "expected_total_attractions": 638, "reported_total_attractions": 658, "meal_per_person_cost_sum": 852, "expected_total_meals": 1704, "reported_total_meals": 2044, "reported_total_transportation": 500}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 319, "expected_total_attractions": 638, "reported_total_attractions": 658, "meal_per_person_cost_sum": 852, "expected_total_meals": 1704, "reported_total_meals": 2044, "reported_total_transportation": 500}}]`

### v3_hard_realbudget_eval_000004
- request: 张家界 2026-05-11->2026-05-13 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 3952, "total": 2952, "diff": 1000, "requested_budget": {"available": true, "amount": 3200, "scope": "total", "party_size": 1, "total": 3200, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "hard"}, "per_person_day": 984.0, "budget_level": "comfortable", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "hard", "amount": 3200, "target_min_ratio": 0.7, "target_max_ratio": 1.0, "target_min_total": 2200, "target_max_total": 3200, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 1, "room_count": 1, "priced_nights": 2, "expected_min_total_hotels": 2600, "reported_total_hotels": 2600, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 876, "expected_total_attractions": 876, "reported_total_attractions": 856, "meal_per_person_cost_sum": 694, "expected_total_meals": 694, "reported_total_meals": 396, "reported_total_transportation": 100}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 876, "expected_total_attractions": 876, "reported_total_attractions": 856, "meal_per_person_cost_sum": 694, "expected_total_meals": 694, "reported_total_meals": 396, "reported_total_transportation": 100}}]`

### v3_hard_realbudget_eval_000005
- request: 广州 2026-07-06->2026-07-10 days=5 transport=公共交通 hotel=民宿 prefs=['摄影', '自然风光', '城市漫步', '本地菜']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 166, "expected_total_attractions": 166, "reported_total_attractions": 156, "meal_per_person_cost_sum": 1280, "expected_total_meals": 1280, "reported_total_meals": 1345, "reported_total_transportation": 300}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 166, "expected_total_attractions": 166, "reported_total_attractions": 156, "meal_per_person_cost_sum": 1280, "expected_total_meals": 1280, "reported_total_meals": 1345, "reported_total_transportation": 300}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": true, "meal_cost_scale_ok": false, "budget_relationship_ok": false, "expected_total_hotels": 1200, "reported_total_hotels": 1200, "expected_total_attractions": 166, "reported_total_attractions": 156, "meal_scale_eval": {"ok": false, "party_total": 1, "budget_level": "standard", "per_person_lunch_dinner_floor": 35, "breakfast_policy": "excluded_from_meal_cost_scale", "meal_count": 15, "checked_count": 10, "failure_count": 1, "failures": [{"date": "2026-07-10", "type": "dinner", "name": "银记肠粉(北京路店)", "estimated_cost": 23, "min_expected_cost": 35}]}}}]`

### v3_hard_realbudget_eval_000006
- request: 南京 2026-07-06->2026-07-09 days=4 transport=自驾 hotel=亲子酒店 prefs=['亲子', '动物园', '海洋馆', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 45, "expected_total_attractions": 135, "reported_total_attractions": 150, "meal_per_person_cost_sum": 919, "expected_total_meals": 2757, "reported_total_meals": 2232, "reported_total_transportation": 800}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 45, "expected_total_attractions": 135, "reported_total_attractions": 150, "meal_per_person_cost_sum": 919, "expected_total_meals": 2757, "reported_total_meals": 2232, "reported_total_transportation": 800}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": true, "meal_cost_scale_ok": false, "budget_relationship_ok": false, "expected_total_hotels": 8100, "reported_total_hotels": 8100, "expected_total_attractions": 135, "reported_total_attractions": 150, "meal_scale_eval": {"ok": false, "party_total": 3, "budget_level": "standard", "per_person_lunch_dinner_floor": 35, "breakfast_policy": "excluded_from_meal_cost_scale", "meal_count": 12, "checked_count": 8, "failure_count": 1, "failures": [{"date": "2026-07-08", "type": "dinner", "name": "小潘记鸭血粉丝汤", "estimated_cost": 34, "min_expected_cost": 35}]}}}]`

### v3_hard_realbudget_eval_000007
- request: 成都 2026-05-11->2026-05-15 days=5 transport=公共交通 hotel=民宿 prefs=['小众展馆', '咖啡', '艺术', '城市漫步', '特色餐厅']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 1428, "expected_total_attractions": 2856, "reported_total_attractions": 3154, "meal_per_person_cost_sum": 2799, "expected_total_meals": 5598, "reported_total_meals": 4848, "reported_total_transportation": 500}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 1428, "expected_total_attractions": 2856, "reported_total_attractions": 3154, "meal_per_person_cost_sum": 2799, "expected_total_meals": 5598, "reported_total_meals": 4848, "reported_total_transportation": 500}}]`

### v3_hard_realbudget_eval_000008
- request: 大理 2026-05-11->2026-05-13 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物']
- errors: `[{"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-05-13", "type": "dinner", "name": "洱海大游船", "reason": "unknown_food_semantics"}]}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 8097, "total": 7197, "diff": 900, "requested_budget": {"available": true, "amount": 8700, "scope": "total", "party_size": 3, "total": 8700, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "hard"}, "per_person_day": 799.67, "budget_level": "comfortable", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "hard", "amount": 8700, "target_min_ratio": 0.7, "target_max_ratio": 1.0, "target_min_total": 6100, "target_max_total": 8700, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 3, "room_count": 2, "priced_nights": 2, "expected_min_total_hotels": 5200, "reported_total_hotels": 5200, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 319, "expected_total_attractions": 957, "reported_total_attractions": 1095, "meal_per_person_cost_sum": 659, "expected_total_meals": 1977, "reported_total_meals": 1302, "reported_total_transportation": 500}}]`

### v3_hard_realbudget_eval_000002
- request: 杭州 2026-05-01->2026-05-04 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '夜市', '老字号', '城市漫步']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 160, "expected_total_attractions": 640, "reported_total_attractions": 600, "meal_per_person_cost_sum": 708, "expected_total_meals": 2832, "reported_total_meals": 2160, "reported_total_transportation": 300}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 160, "expected_total_attractions": 640, "reported_total_attractions": 600, "meal_per_person_cost_sum": 708, "expected_total_meals": 2832, "reported_total_meals": 2160, "reported_total_transportation": 300}}]`

### v3_hard_realbudget_eval_000010
- request: 西安 2026-08-05->2026-08-09 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 4, "party_total": 5, "room_count": 3, "priced_nights": 4, "expected_min_total_hotels": 16200, "reported_total_hotels": 17100, "diff": 900, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 5, "hotel_room_count": 3, "attraction_ticket_sum": 487, "expected_total_attractions": 2435, "reported_total_attractions": 2590, "meal_per_person_cost_sum": 812, "expected_total_meals": 4060, "reported_total_meals": 2910, "reported_total_transportation": 1500}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 5, "hotel_room_count": 3, "attraction_ticket_sum": 487, "expected_total_attractions": 2435, "reported_total_attractions": 2590, "meal_per_person_cost_sum": 812, "expected_total_meals": 4060, "reported_total_meals": 2910, "reported_total_transportation": 1500}}]`

### v3_hard_realbudget_eval_000011
- request: 福州 2026-06-21->2026-06-24 days=4 transport=打车 hotel=高端酒店 prefs=['高端酒店', '艺术', '特色餐厅', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 680, "expected_total_attractions": 1360, "reported_total_attractions": 1698, "meal_per_person_cost_sum": 1466, "expected_total_meals": 2932, "reported_total_meals": 3856, "reported_total_transportation": 4000}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 680, "expected_total_attractions": 1360, "reported_total_attractions": 1698, "meal_per_person_cost_sum": 1466, "expected_total_meals": 2932, "reported_total_meals": 3856, "reported_total_transportation": 4000}}]`

### v3_hard_realbudget_eval_000009
- request: 苏州 2026-04-30->2026-05-03 days=4 transport=打车 hotel=亲子酒店 prefs=['亲子', '老人友好', '博物馆', '城市公园', '特色餐厅']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 320, "expected_total_attractions": 1280, "reported_total_attractions": 1440, "meal_per_person_cost_sum": 995, "expected_total_meals": 3980, "reported_total_meals": 5048, "reported_total_transportation": 1000}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 320, "expected_total_attractions": 1280, "reported_total_attractions": 1440, "meal_per_person_cost_sum": 995, "expected_total_meals": 3980, "reported_total_meals": 5048, "reported_total_transportation": 1000}}]`

### v3_hard_realbudget_eval_000012
- request: 洛阳 2025-05-07->2025-05-10 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '夜市', '老字号', '城市漫步']
- errors: `[{"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 240, "expected_total_attractions": 960, "reported_total_attractions": 960, "meal_per_person_cost_sum": 627, "expected_total_meals": 2508, "reported_total_meals": 2004, "reported_total_transportation": 1000}}]`

### v3_hard_realbudget_eval_000014
- request: 成都 2026-06-06->2026-06-08 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 4000, "total": 3000, "diff": 1000, "requested_budget": {"available": true, "amount": 4300, "scope": "total", "party_size": 1, "total": 4300, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "hard"}, "per_person_day": 1000.0, "budget_level": "comfortable", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "hard", "amount": 4300, "target_min_ratio": 0.7, "target_max_ratio": 1.0, "target_min_total": 3000, "target_max_total": 4300, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 1, "room_count": 1, "priced_nights": 2, "expected_min_total_hotels": 2700, "reported_total_hotels": 2700, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 130, "expected_total_attractions": 130, "reported_total_attractions": 130, "meal_per_person_cost_sum": 904, "expected_total_meals": 904, "reported_total_meals": 840, "reported_total_transportation": 330}}]`

### v3_hard_realbudget_eval_000013
- request: 武汉 2026-05-09->2026-05-13 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 253, "expected_total_attractions": 506, "reported_total_attractions": 516, "meal_per_person_cost_sum": 922, "expected_total_meals": 1844, "reported_total_meals": 2044, "reported_total_transportation": 400}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 253, "expected_total_attractions": 506, "reported_total_attractions": 516, "meal_per_person_cost_sum": 922, "expected_total_meals": 1844, "reported_total_meals": 2044, "reported_total_transportation": 400}}]`

### v3_hard_realbudget_eval_000016
- request: 苏州 2026-06-06->2026-06-09 days=4 transport=自驾 hotel=亲子酒店 prefs=['亲子', '动物园', '海洋馆', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 140, "expected_total_attractions": 420, "reported_total_attractions": 420, "meal_per_person_cost_sum": 583, "expected_total_meals": 1749, "reported_total_meals": 1980, "reported_total_transportation": 800}}, {"stage": "rule", "type": "budget_hard_constraint_exceeded", "details": {"part_sum": 11300, "total": 11300, "diff": 0, "requested_budget": {"available": true, "amount": 10000, "scope": "total", "party_size": 3, "total": 10000, "source": "budget_constraint", "budget_level": "standard", "strictness": "hard"}, "per_person_day": 941.67, "budget_level": "standard", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "standard", "strictness": "hard", "amount": 10000, "target_min_ratio": 0.6, "target_max_ratio": 1.0, "target_min_total": 6000, "target_max_total": 10000, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": true, "within_user_budget": true, "user_constraint_ok": false, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 3, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 8100, "reported_total_hotels": 8100, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "budget_preference_mismatch", "details": {"part_sum": 11300, "total": 11300, "diff": 0, "requested_budget": {"available": true, "amount": 10000, "scope": "total", "party_size": 3, "total": 10000, "source": "budget_constraint", "budget_level": "standard", "strictness": "hard"}, "per_person_day": 941.67, "budget_level": "standard", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "standard", "strictness": "hard", "amount": 10000, "target_min_ratio": 0.6, "target_max_ratio": 1.0, "target_min_total": 6000, "target_max_total": 10000, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": true, "within_user_budget": true, "user_constraint_ok": false, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 3, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 8100, "reported_total_hotels": 8100, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_hard_realbudget_eval_000017
- request: 苏州 2026-05-09->2026-05-13 days=5 transport=公共交通 hotel=民宿 prefs=['小众展馆', '咖啡', '艺术', '城市漫步', '特色餐厅']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 5938, "total": 7138, "diff": -1200, "requested_budget": {"available": true, "amount": 10100, "scope": "total", "party_size": 2, "total": 10100, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "soft"}, "per_person_day": 713.8, "budget_level": "comfortable", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "soft", "amount": 10100, "target_min_ratio": 0.7, "target_max_ratio": 1.1, "target_min_total": 7100, "target_max_total": 11100, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 4, "party_total": 2, "room_count": 1, "priced_nights": 4, "expected_min_total_hotels": 1200, "reported_total_hotels": 1200, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 502, "expected_total_attractions": 1004, "reported_total_attractions": 1034, "meal_per_person_cost_sum": 1094, "expected_total_meals": 2188, "reported_total_meals": 2704, "reported_total_transportation": 1000}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 502, "expected_total_attractions": 1004, "reported_total_attractions": 1034, "meal_per_person_cost_sum": 1094, "expected_total_meals": 2188, "reported_total_meals": 2704, "reported_total_transportation": 1000}}]`

### v3_hard_realbudget_eval_000018
- request: 天津 2026-07-06->2026-07-08 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 2, "party_total": 3, "room_count": 2, "priced_nights": 2, "expected_min_total_hotels": 7200, "reported_total_hotels": 3600, "diff": -3600, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 955, "expected_total_attractions": 2865, "reported_total_attractions": 2697, "meal_per_person_cost_sum": 3189, "expected_total_meals": 9567, "reported_total_meals": 5970, "reported_total_transportation": 600}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 955, "expected_total_attractions": 2865, "reported_total_attractions": 2697, "meal_per_person_cost_sum": 3189, "expected_total_meals": 9567, "reported_total_meals": 5970, "reported_total_transportation": 600}}]`

### v3_hard_realbudget_eval_000019
- request: 丽江 2026-05-11->2026-05-14 days=4 transport=打车 hotel=亲子酒店 prefs=['亲子', '老人友好', '博物馆', '城市公园', '特色餐厅']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 500, "expected_total_attractions": 1000, "reported_total_attractions": 1040, "meal_per_person_cost_sum": 862, "expected_total_meals": 1724, "reported_total_meals": 1604, "reported_total_transportation": 800}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 500, "expected_total_attractions": 1000, "reported_total_attractions": 1040, "meal_per_person_cost_sum": 862, "expected_total_meals": 1724, "reported_total_meals": 1604, "reported_total_transportation": 800}}]`

### v3_hard_realbudget_eval_000020
- request: 杭州 2026-06-21->2026-06-25 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 25950, "total": 26450, "diff": -500, "requested_budget": {"available": true, "amount": 27000, "scope": "total", "party_size": 5, "total": 27000, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "hard"}, "per_person_day": 1058.0, "budget_level": "comfortable", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "hard", "amount": 27000, "target_min_ratio": 0.7, "target_max_ratio": 1.0, "target_min_total": 18900, "target_max_total": 27000, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 4, "party_total": 5, "room_count": 3, "priced_nights": 4, "expected_min_total_hotels": 18000, "reported_total_hotels": 18000, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 5, "hotel_room_count": 3, "attraction_ticket_sum": 120, "expected_total_attractions": 600, "reported_total_attractions": 500, "meal_per_person_cost_sum": 1168, "expected_total_meals": 5840, "reported_total_meals": 5950, "reported_total_transportation": 1500}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 5, "hotel_room_count": 3, "attraction_ticket_sum": 120, "expected_total_attractions": 600, "reported_total_attractions": 500, "meal_per_person_cost_sum": 1168, "expected_total_meals": 5840, "reported_total_meals": 5950, "reported_total_transportation": 1500}}]`
