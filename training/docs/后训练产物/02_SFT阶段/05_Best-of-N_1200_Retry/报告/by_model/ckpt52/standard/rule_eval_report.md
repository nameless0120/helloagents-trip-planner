# Rule Eval Report: 260513_bestofn1200_retry_ckpt52_standard_w10

- records: 200
- generations: `training/outputs/eval/by_model/sft_qwen25_7b_v3_260513_bestofn1200_retry_ckpt52/260513_bestofn1200_retry_ckpt52_standard_w10/generations.jsonl`
- records_path: `training/data/v3/eval/records.jsonl`

## Boolean Metrics

| Metric | Pass | Total | Rate |
| --- | ---: | ---: | ---: |
| accommodation_type_ok | 198 | 198 | 100.00% |
| attraction_budget_consistent | 75 | 198 | 37.88% |
| attraction_budget_party_relation_ok | 194 | 198 | 97.98% |
| attraction_count_ok | 198 | 198 | 100.00% |
| attraction_diversity_ok | 179 | 198 | 90.40% |
| attraction_grounding_ok | 198 | 198 | 100.00% |
| attraction_repeat_limit_ok | 179 | 198 | 90.40% |
| budget_arithmetic_consistent | 141 | 198 | 71.21% |
| budget_consistent | 141 | 198 | 71.21% |
| budget_level_aligned | 151 | 198 | 76.26% |
| budget_preference_aligned | 151 | 198 | 76.26% |
| budget_relationship_ok | 160 | 198 | 80.81% |
| budget_selection_ok | 118 | 198 | 59.60% |
| budget_user_constraint_ok | 196 | 198 | 98.99% |
| budget_within_user_budget | 193 | 198 | 97.47% |
| city_ok | 198 | 198 | 100.00% |
| date_range_ok | 198 | 198 | 100.00% |
| day_dates_ok | 198 | 198 | 100.00% |
| day_index_ok | 198 | 198 | 100.00% |
| days_len_ok | 198 | 198 | 100.00% |
| dpo_soft_pass | 127 | 198 | 64.14% |
| dpo_soft_recomputed_budget_pass | 103 | 198 | 52.02% |
| hard_pass | 196 | 198 | 98.99% |
| hotel_budget_covers_nights | 192 | 198 | 96.97% |
| hotel_budget_relation_ok | 194 | 198 | 97.98% |
| hotel_distance_placeholder_ok | 198 | 198 | 100.00% |
| hotel_grounding_ok | 198 | 198 | 100.00% |
| invalid_hotel_name_ok | 198 | 198 | 100.00% |
| json_extract_ok | 199 | 200 | 99.50% |
| legacy_hard_pass | 126 | 198 | 63.64% |
| location_object_ok | 198 | 198 | 100.00% |
| meal_budget_consistent | 1 | 198 | 0.51% |
| meal_complete | 198 | 198 | 100.00% |
| meal_cost_scale_ok | 166 | 198 | 83.84% |
| meal_diversity_ok | 177 | 198 | 89.39% |
| meal_grounding_ok | 197 | 198 | 99.49% |
| meal_lunch_dinner_same_day_ok | 194 | 198 | 97.98% |
| meal_repeat_limit_ok | 180 | 198 | 90.91% |
| meal_specific_ok | 198 | 198 | 100.00% |
| meal_valid_semantics_ok | 197 | 198 | 99.49% |
| middle_hotel_ok | 198 | 198 | 100.00% |
| recomputed_budget_fit_ok | 118 | 198 | 59.60% |
| recomputed_budget_hard_ok | 194 | 198 | 97.98% |
| recomputed_budget_level_aligned | 118 | 198 | 59.60% |
| recomputed_budget_preference_aligned | 118 | 198 | 59.60% |
| recomputed_budget_user_constraint_ok | 194 | 198 | 97.98% |
| recomputed_budget_within_user_budget | 183 | 198 | 92.42% |
| schema_ok | 198 | 200 | 99.00% |
| sft_budget_semantic_hard_pass | 157 | 198 | 79.29% |
| sft_hard_pass | 196 | 198 | 98.99% |
| sft_no_budget_sum_hard_pass | 196 | 198 | 98.99% |
| sft_strict_hard_pass | 1 | 198 | 0.51% |
| transportation_budget_nonnegative | 198 | 198 | 100.00% |
| weather_dates_ok | 198 | 198 | 100.00% |
| weather_match | 197 | 198 | 99.49% |

## Numeric Metrics

```json
{
  "attraction_diversity_unique_rate": {
    "avg": 0.9869,
    "p50": 1.0,
    "p90": 1.0
  },
  "attraction_grounding_rate": {
    "avg": 1.0,
    "p50": 1.0,
    "p90": 1.0
  },
  "hotel_grounding_rate": {
    "avg": 1.0,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_diversity_unique_rate": {
    "avg": 0.9276,
    "p50": 1.0,
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
    "avg": 718.1912,
    "p50": 588.25,
    "p90": 1321.0
  },
  "recomputed_budget_total": {
    "avg": 6794.1364,
    "p50": 5236.0,
    "p90": 13801.0
  }
}
```

## Failure Types

```json
{
  "meal_budget_inconsistent": 197,
  "attraction_budget_inconsistent": 123,
  "budget_arithmetic_inconsistent": 57,
  "budget_preference_mismatch": 47,
  "budget_relationship_mismatch": 38,
  "meal_cost_scale_too_low": 32,
  "attraction_repeat_too_many": 19,
  "meal_repeat_too_many": 18,
  "hotel_budget_underestimated": 6,
  "meal_same_day_lunch_dinner_repeat": 4,
  "budget_hard_constraint_exceeded": 2,
  "meal_invalid_name": 1,
  "json_extract": 1,
  "schema": 1,
  "weather_mismatch": 1
}
```

## Failure Examples

### v3_standard200_realbudget_eval_000000
- request: 昆明 2026-04-07->2026-04-09 days=3 transport=地铁+步行 hotel=高端酒店 prefs=['休闲慢游', '美食']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 4934, "total": 7434, "diff": -2500, "requested_budget": {"available": true, "amount": 9800, "scope": "total", "party_size": 2, "total": 9800, "source": "budget_constraint", "budget_level": "premium", "strictness": "hard"}, "per_person_day": 1239.0, "budget_level": "premium", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "premium", "strictness": "hard", "amount": 9800, "target_min_ratio": 0.75, "target_max_ratio": 1.0, "target_min_total": 7400, "target_max_total": 9800, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 2, "room_count": 1, "priced_nights": 2, "expected_min_total_hotels": 2600, "reported_total_hotels": 2600, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 50, "expected_total_attractions": 100, "reported_total_attractions": 100, "meal_per_person_cost_sum": 770, "expected_total_meals": 1540, "reported_total_meals": 1934, "reported_total_transportation": 300}}]`

### v3_standard200_realbudget_eval_000001
- request: 桂林 2026-09-04->2026-09-06 days=3 transport=公共交通 hotel=高端酒店 prefs=['艺术', '美食', '第一次来', '历史文化']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 3974, "total": 4074, "diff": -100, "requested_budget": {"available": true, "amount": 7100, "scope": "total", "party_size": 2, "total": 7100, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "soft"}, "per_person_day": 679.0, "budget_level": "comfortable", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "soft", "amount": 7100, "target_min_ratio": 0.7, "target_max_ratio": 1.1, "target_min_total": 5000, "target_max_total": 7800, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 2, "room_count": 1, "priced_nights": 2, "expected_min_total_hotels": 1200, "reported_total_hotels": 1200, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 135, "expected_total_attractions": 270, "reported_total_attractions": 270, "meal_per_person_cost_sum": 849, "expected_total_meals": 1698, "reported_total_meals": 2004, "reported_total_transportation": 500}}, {"stage": "rule", "type": "budget_preference_mismatch", "details": {"part_sum": 3974, "total": 4074, "diff": -100, "requested_budget": {"available": true, "amount": 7100, "scope": "total", "party_size": 2, "total": 7100, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "soft"}, "per_person_day": 679.0, "budget_level": "comfortable", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "soft", "amount": 7100, "target_min_ratio": 0.7, "target_max_ratio": 1.1, "target_min_total": 5000, "target_max_total": 7800, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 2, "room_count": 1, "priced_nights": 2, "expected_min_total_hotels": 1200, "reported_total_hotels": 1200, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_standard200_realbudget_eval_000008
- request: 大理 2026-05-11->2026-05-13 days=3 transport=地铁+步行 hotel=舒适型酒店 prefs=['休闲慢游', '城市地标', '历史文化']
- errors: `[{"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 75, "expected_total_attractions": 150, "reported_total_attractions": 150, "meal_per_person_cost_sum": 501, "expected_total_meals": 1002, "reported_total_meals": 854, "reported_total_transportation": 400}}]`

### v3_standard200_realbudget_eval_000005
- request: 广州 2026-07-06->2026-07-08 days=3 transport=地铁+步行 hotel=经济型酒店 prefs=['博物馆', '城市公园', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 170, "expected_total_attractions": 340, "reported_total_attractions": 340, "meal_per_person_cost_sum": 637, "expected_total_meals": 1274, "reported_total_meals": 1184, "reported_total_transportation": 200}}]`

### v3_standard200_realbudget_eval_000007
- request: 成都 2026-05-11->2026-05-13 days=3 transport=地铁+步行 hotel=舒适型酒店 prefs=['美食', '城市公园', '休闲慢游']
- errors: `[{"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 223, "expected_total_attractions": 446, "reported_total_attractions": 446, "meal_per_person_cost_sum": 761, "expected_total_meals": 1522, "reported_total_meals": 1638, "reported_total_transportation": 200}}]`

### v3_standard200_realbudget_eval_000006
- request: 南京 2026-07-06->2026-07-09 days=4 transport=打车 hotel=经济型酒店 prefs=['老人友好', '美食', '城市公园', '休闲慢游']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 100, "expected_total_attractions": 300, "reported_total_attractions": 330, "meal_per_person_cost_sum": 835, "expected_total_meals": 2505, "reported_total_meals": 2469, "reported_total_transportation": 700}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 100, "expected_total_attractions": 300, "reported_total_attractions": 330, "meal_per_person_cost_sum": 835, "expected_total_meals": 2505, "reported_total_meals": 2469, "reported_total_transportation": 700}}]`

### v3_standard200_realbudget_eval_000010
- request: 西安 2026-08-05->2026-08-08 days=4 transport=公共交通 hotel=经济型酒店 prefs=['城市公园', '美食']
- errors: `[{"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-08-07", "type": "lunch", "name": "奔跑吧陕菜·钟楼南大街店", "reason": "unknown_food_semantics"}]}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 3910, "total": 4910, "diff": -1000, "requested_budget": {"available": true, "amount": 6600, "scope": "total", "party_size": 2, "total": 6600, "source": "budget_constraint", "budget_level": "standard", "strictness": "soft"}, "per_person_day": 613.75, "budget_level": "standard", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "standard", "strictness": "soft", "amount": 6600, "target_min_ratio": 0.6, "target_max_ratio": 1.05, "target_min_total": 4000, "target_max_total": 6900, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 2, "room_count": 1, "priced_nights": 3, "expected_min_total_hotels": 750, "reported_total_hotels": 750, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 387, "expected_total_attractions": 774, "reported_total_attractions": 756, "meal_per_person_cost_sum": 589, "expected_total_meals": 1178, "reported_total_meals": 1404, "reported_total_transportation": 1000}}]`

### v3_standard200_realbudget_eval_000003
- request: 西安 2025-05-07->2025-05-11 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '历史文化', '购物商圈']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "西安博物院", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2025-05-10", "day_index": 3, "name": "西安博物院"}, {"date": "2025-05-11", "day_index": 4, "name": "西安博物院"}]}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 4, "party_total": 3, "room_count": 2, "priced_nights": 4, "expected_min_total_hotels": 3600, "reported_total_hotels": 4050, "diff": 450, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 319, "expected_total_attractions": 957, "reported_total_attractions": 1098, "meal_per_person_cost_sum": 789, "expected_total_meals": 2367, "reported_total_meals": 3153, "reported_total_transportation": 1100}}]`

### v3_standard200_realbudget_eval_000004
- request: 张家界 2026-05-11->2026-05-15 days=5 transport=地铁+步行 hotel=舒适型酒店 prefs=['亲子', '城市漫步', '历史文化']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "七十二奇楼景区", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-05-11", "day_index": 0, "name": "七十二奇楼景区"}, {"date": "2026-05-14", "day_index": 3, "name": "七十二奇楼景区"}]}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "麦当劳", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-05-12", "type": "breakfast", "name": "麦当劳(泊富国际文化广场店)"}, {"date": "2026-05-13", "type": "breakfast", "name": "麦当劳(天门中心广场店)"}, {"date": "2026-05-14", "type": "breakfast", "name": "麦当劳(泊富国际文化广场店)"}, {"date": "2026-05-15", "type": "breakfast", "name": "麦当劳(泊富国际文化广场店)"}]}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 4, "party_total": 4, "room_count": 2, "priced_nights": 4, "expected_min_total_hotels": 3200, "reported_total_hotels": 4800, "diff": 1600, "covers_nights": false}}]`

### v3_standard200_realbudget_eval_000002
- request: 杭州 2026-05-01->2026-05-05 days=5 transport=公共交通 hotel=经济型酒店 prefs=['美食', '休闲慢游', '户外轻徒步', '城市漫步']
- errors: `[{"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 160, "expected_total_attractions": 160, "reported_total_attractions": 160, "meal_per_person_cost_sum": 963, "expected_total_meals": 963, "reported_total_meals": 1032, "reported_total_transportation": 200}}, {"stage": "rule", "type": "budget_preference_mismatch", "details": {"part_sum": 2392, "total": 2392, "diff": 0, "requested_budget": {"available": true, "amount": 3400, "scope": "total", "party_size": 1, "total": 3400, "source": "budget_constraint", "budget_level": "limited", "strictness": "soft"}, "per_person_day": 478.4, "budget_level": "limited", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "limited", "strictness": "soft", "amount": 3400, "target_min_ratio": 0.72, "target_max_ratio": 1.05, "target_min_total": 2400, "target_max_total": 3600, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": true, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 4, "party_total": 1, "room_count": 1, "priced_nights": 4, "expected_min_total_hotels": 1000, "reported_total_hotels": 1000, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_standard200_realbudget_eval_000014
- request: 成都 2026-06-06->2026-06-07 days=2 transport=打车 hotel=经济型酒店 prefs=['小众展览', '美食', '城市地标']
- errors: `[{"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 115, "expected_total_attractions": 460, "reported_total_attractions": 460, "meal_per_person_cost_sum": 612, "expected_total_meals": 2448, "reported_total_meals": 2608, "reported_total_transportation": 400}}]`

### v3_standard200_realbudget_eval_000013
- request: 武汉 2026-05-09->2026-05-11 days=3 transport=公共交通 hotel=舒适型酒店 prefs=['亲子', '老人友好', '第一次来', '城市公园']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 6, "hotel_room_count": 3, "attraction_ticket_sum": 130, "expected_total_attractions": 780, "reported_total_attractions": 840, "meal_per_person_cost_sum": 517, "expected_total_meals": 3102, "reported_total_meals": 4020, "reported_total_transportation": 1140}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 6, "hotel_room_count": 3, "attraction_ticket_sum": 130, "expected_total_attractions": 780, "reported_total_attractions": 840, "meal_per_person_cost_sum": 517, "expected_total_meals": 3102, "reported_total_meals": 4020, "reported_total_transportation": 1140}}]`

### v3_standard200_realbudget_eval_000018
- request: 天津 2026-07-06->2026-07-07 days=2 transport=打车 hotel=舒适型酒店 prefs=['老人友好', '夜市夜景', '艺术', '第一次来']
- errors: `[{"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 130, "expected_total_attractions": 390, "reported_total_attractions": 390, "meal_per_person_cost_sum": 339, "expected_total_meals": 1017, "reported_total_meals": 1011, "reported_total_transportation": 200}}]`

### v3_standard200_realbudget_eval_000016
- request: 苏州 2026-06-06->2026-06-08 days=3 transport=公共交通 hotel=民宿 prefs=['海滨度假', '城市公园', '主题乐园', '清真']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 140, "expected_total_attractions": 280, "reported_total_attractions": 270, "meal_per_person_cost_sum": 292, "expected_total_meals": 584, "reported_total_meals": 608, "reported_total_transportation": 300}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 140, "expected_total_attractions": 280, "reported_total_attractions": 270, "meal_per_person_cost_sum": 292, "expected_total_meals": 584, "reported_total_meals": 608, "reported_total_transportation": 300}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": true, "meal_cost_scale_ok": false, "budget_relationship_ok": false, "expected_total_hotels": 600, "reported_total_hotels": 600, "expected_total_attractions": 280, "reported_total_attractions": 270, "meal_scale_eval": {"ok": false, "party_total": 2, "budget_level": "limited", "per_person_lunch_dinner_floor": 25, "breakfast_policy": "excluded_from_meal_cost_scale", "meal_count": 9, "checked_count": 6, "failure_count": 3, "failures": [{"date": "2026-06-06", "type": "dinner", "name": "丝路回乡小吃店(西夏店)", "estimated_cost": 24, "min_expected_cost": 25}, {"date": "2026-06-07", "type": "lunch", "name": "魅之蘭兰州牛肉面(乐嘉汇店)", "estimated_cost": 21, "min_expected_cost": 25}, {"date": "2026-06-08", "type": "lunch", "name": "丝路回乡小吃店(西夏店)", "estimated_cost": 24, "min_expected_cost": 25}]}}}]`

### v3_standard200_realbudget_eval_000011
- request: 福州 2026-06-21->2026-06-24 days=4 transport=打车 hotel=经济型酒店 prefs=['第一次来', '城市漫步']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 117, "expected_total_attractions": 234, "reported_total_attractions": 254, "meal_per_person_cost_sum": 694, "expected_total_meals": 1388, "reported_total_meals": 1424, "reported_total_transportation": 1200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 117, "expected_total_attractions": 234, "reported_total_attractions": 254, "meal_per_person_cost_sum": 694, "expected_total_meals": 1388, "reported_total_meals": 1424, "reported_total_transportation": 1200}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": true, "meal_cost_scale_ok": false, "budget_relationship_ok": false, "expected_total_hotels": 600, "reported_total_hotels": 600, "expected_total_attractions": 234, "reported_total_attractions": 254, "meal_scale_eval": {"ok": false, "party_total": 2, "budget_level": "standard", "per_person_lunch_dinner_floor": 35, "breakfast_policy": "excluded_from_meal_cost_scale", "meal_count": 12, "checked_count": 8, "failure_count": 1, "failures": [{"date": "2026-06-21", "type": "lunch", "name": "后街捞化", "estimated_cost": 27, "min_expected_cost": 35}]}}}]`

### v3_standard200_realbudget_eval_000017
- request: 苏州 2026-05-09->2026-05-11 days=3 transport=地铁+步行 hotel=亲子酒店 prefs=['亲子', '历史文化', '休闲慢游', '户外轻徒步']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 320, "expected_total_attractions": 960, "reported_total_attractions": 1035, "meal_per_person_cost_sum": 510, "expected_total_meals": 1530, "reported_total_meals": 1350, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 320, "expected_total_attractions": 960, "reported_total_attractions": 1035, "meal_per_person_cost_sum": 510, "expected_total_meals": 1530, "reported_total_meals": 1350, "reported_total_transportation": 200}}]`

### v3_standard200_realbudget_eval_000021
- request: 上海 2026-06-21->2026-06-22 days=2 transport=地铁+步行 hotel=经济型酒店 prefs=['老人友好', '休闲慢游', '城市漫步', '主题乐园']
- errors: `[{"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 70, "expected_total_attractions": 140, "reported_total_attractions": 140, "meal_per_person_cost_sum": 596, "expected_total_meals": 1192, "reported_total_meals": 1090, "reported_total_transportation": 100}}]`

### v3_standard200_realbudget_eval_000009
- request: 苏州 2026-04-30->2026-05-04 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['亲子', '城市地标', '第一次来', '城市漫步']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 17300, "total": 14300, "diff": 3000, "requested_budget": {"available": true, "amount": 20500, "scope": "total", "party_size": 4, "total": 20500, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "soft"}, "per_person_day": 715.0, "budget_level": "comfortable", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "soft", "amount": 20500, "target_min_ratio": 0.7, "target_max_ratio": 1.1, "target_min_total": 14300, "target_max_total": 22600, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 4, "party_total": 4, "room_count": 2, "priced_nights": 4, "expected_min_total_hotels": 10800, "reported_total_hotels": 10800, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 400, "expected_total_attractions": 1600, "reported_total_attractions": 2120, "meal_per_person_cost_sum": 975, "expected_total_meals": 3900, "reported_total_meals": 3380, "reported_total_transportation": 1000}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 400, "expected_total_attractions": 1600, "reported_total_attractions": 2120, "meal_per_person_cost_sum": 975, "expected_total_meals": 3900, "reported_total_meals": 3380, "reported_total_transportation": 1000}}]`

### v3_standard200_realbudget_eval_000012
- request: 洛阳 2025-05-07->2025-05-10 days=4 transport=打车 hotel=高端酒店 prefs=['休闲慢游', '第一次来']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "洛阳凤舞神都实景演出", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2025-05-07", "day_index": 0, "name": "洛阳凤舞神都实景演出"}, {"date": "2025-05-09", "day_index": 2, "name": "洛阳凤舞神都实景演出"}]}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 1154, "expected_total_attractions": 3462, "reported_total_attractions": 3600, "meal_per_person_cost_sum": 2319, "expected_total_meals": 6957, "reported_total_meals": 7299, "reported_total_transportation": 5000}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 1154, "expected_total_attractions": 3462, "reported_total_attractions": 3600, "meal_per_person_cost_sum": 2319, "expected_total_meals": 6957, "reported_total_meals": 7299, "reported_total_transportation": 5000}}]`

### v3_standard200_realbudget_eval_000020
- request: 杭州 2026-06-21->2026-06-24 days=4 transport=地铁+步行 hotel=高端酒店 prefs=['历史文化', '海滨度假']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 8980, "total": 9980, "diff": -1000, "requested_budget": {"available": true, "amount": 10600, "scope": "total", "party_size": 2, "total": 10600, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "soft"}, "per_person_day": 1247.5, "budget_level": "comfortable", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "soft", "amount": 10600, "target_min_ratio": 0.7, "target_max_ratio": 1.1, "target_min_total": 7400, "target_max_total": 11700, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 2, "room_count": 1, "priced_nights": 3, "expected_min_total_hotels": 4500, "reported_total_hotels": 4500, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 432, "expected_total_attractions": 864, "reported_total_attractions": 804, "meal_per_person_cost_sum": 992, "expected_total_meals": 1984, "reported_total_meals": 2576, "reported_total_transportation": 1100}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 432, "expected_total_attractions": 864, "reported_total_attractions": 804, "meal_per_person_cost_sum": 992, "expected_total_meals": 1984, "reported_total_meals": 2576, "reported_total_transportation": 1100}}]`
