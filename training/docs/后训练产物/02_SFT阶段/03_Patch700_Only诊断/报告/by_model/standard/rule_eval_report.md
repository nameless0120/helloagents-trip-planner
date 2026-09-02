# Rule Eval Report: 260511_high_end_context_standard_w10

- records: 200
- generations: `training/outputs/eval/by_model/sft_qwen25_7b_v3_260511_patch700_only_from_lr6e5_lr1e5/260511_high_end_context_standard_w10/generations.jsonl`
- records_path: `training/data/v3/eval/records.jsonl`

## Boolean Metrics

| Metric | Pass | Total | Rate |
| --- | ---: | ---: | ---: |
| accommodation_type_ok | 200 | 200 | 100.00% |
| attraction_budget_consistent | 103 | 200 | 51.50% |
| attraction_budget_party_relation_ok | 192 | 200 | 96.00% |
| attraction_count_ok | 199 | 200 | 99.50% |
| attraction_diversity_ok | 183 | 200 | 91.50% |
| attraction_grounding_ok | 200 | 200 | 100.00% |
| attraction_repeat_limit_ok | 183 | 200 | 91.50% |
| budget_arithmetic_consistent | 166 | 200 | 83.00% |
| budget_consistent | 166 | 200 | 83.00% |
| budget_level_aligned | 90 | 200 | 45.00% |
| budget_preference_aligned | 90 | 200 | 45.00% |
| budget_relationship_ok | 107 | 200 | 53.50% |
| budget_selection_ok | 79 | 200 | 39.50% |
| budget_user_constraint_ok | 197 | 200 | 98.50% |
| budget_within_user_budget | 194 | 200 | 97.00% |
| city_ok | 200 | 200 | 100.00% |
| date_range_ok | 200 | 200 | 100.00% |
| day_dates_ok | 200 | 200 | 100.00% |
| day_index_ok | 200 | 200 | 100.00% |
| days_len_ok | 200 | 200 | 100.00% |
| dpo_soft_pass | 69 | 200 | 34.50% |
| dpo_soft_recomputed_budget_pass | 61 | 200 | 30.50% |
| hard_pass | 195 | 200 | 97.50% |
| hotel_budget_covers_nights | 187 | 200 | 93.50% |
| hotel_budget_relation_ok | 188 | 200 | 94.00% |
| hotel_distance_placeholder_ok | 200 | 200 | 100.00% |
| hotel_grounding_ok | 200 | 200 | 100.00% |
| invalid_hotel_name_ok | 200 | 200 | 100.00% |
| json_extract_ok | 200 | 200 | 100.00% |
| legacy_hard_pass | 123 | 200 | 61.50% |
| location_object_ok | 200 | 200 | 100.00% |
| meal_budget_consistent | 1 | 200 | 0.50% |
| meal_complete | 200 | 200 | 100.00% |
| meal_cost_scale_ok | 121 | 200 | 60.50% |
| meal_diversity_ok | 165 | 200 | 82.50% |
| meal_grounding_ok | 197 | 200 | 98.50% |
| meal_lunch_dinner_same_day_ok | 188 | 200 | 94.00% |
| meal_repeat_limit_ok | 173 | 200 | 86.50% |
| meal_specific_ok | 200 | 200 | 100.00% |
| meal_valid_semantics_ok | 198 | 200 | 99.00% |
| middle_hotel_ok | 200 | 200 | 100.00% |
| recomputed_budget_fit_ok | 79 | 200 | 39.50% |
| recomputed_budget_hard_ok | 198 | 200 | 99.00% |
| recomputed_budget_level_aligned | 79 | 200 | 39.50% |
| recomputed_budget_preference_aligned | 79 | 200 | 39.50% |
| recomputed_budget_user_constraint_ok | 198 | 200 | 99.00% |
| recomputed_budget_within_user_budget | 192 | 200 | 96.00% |
| schema_ok | 200 | 200 | 100.00% |
| sft_budget_semantic_hard_pass | 102 | 200 | 51.00% |
| sft_hard_pass | 195 | 200 | 97.50% |
| sft_no_budget_sum_hard_pass | 195 | 200 | 97.50% |
| sft_strict_hard_pass | 0 | 200 | 0.00% |
| transportation_budget_nonnegative | 200 | 200 | 100.00% |
| weather_dates_ok | 199 | 200 | 99.50% |
| weather_match | 199 | 200 | 99.50% |

## Numeric Metrics

```json
{
  "attraction_diversity_unique_rate": {
    "avg": 0.9891,
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
    "avg": 0.8979,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_food_pois_grounding_rate": {
    "avg": 0.9988,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_grounding_rate": {
    "avg": 0.9988,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_semantic_valid_rate": {
    "avg": 0.9992,
    "p50": 1.0,
    "p90": 1.0
  },
  "recomputed_budget_per_person_day": {
    "avg": 616.8335,
    "p50": 481.5,
    "p90": 1090.0
  },
  "recomputed_budget_total": {
    "avg": 5759.25,
    "p50": 4691.0,
    "p90": 11670.0
  }
}
```

## Failure Types

```json
{
  "meal_budget_inconsistent": 199,
  "budget_preference_mismatch": 110,
  "attraction_budget_inconsistent": 97,
  "budget_relationship_mismatch": 93,
  "meal_cost_scale_too_low": 79,
  "budget_arithmetic_inconsistent": 34,
  "meal_repeat_too_many": 27,
  "attraction_repeat_too_many": 17,
  "hotel_budget_underestimated": 13,
  "meal_same_day_lunch_dinner_repeat": 12,
  "budget_hard_constraint_exceeded": 3,
  "meal_invalid_name": 2,
  "meal_grounding_miss": 1,
  "weather_mismatch": 1
}
```

## Failure Examples

### v3_standard200_realbudget_eval_000000
- request: 昆明 2026-04-07->2026-04-09 days=3 transport=地铁+步行 hotel=高端酒店 prefs=['休闲慢游', '美食']
- errors: `[{"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 20, "expected_total_attractions": 40, "reported_total_attractions": 40, "meal_per_person_cost_sum": 738, "expected_total_meals": 1476, "reported_total_meals": 2460, "reported_total_transportation": 200}}, {"stage": "rule", "type": "budget_preference_mismatch", "details": {"part_sum": 5300, "total": 5300, "diff": 0, "requested_budget": {"available": true, "amount": 9800, "scope": "total", "party_size": 2, "total": 9800, "source": "budget_constraint", "budget_level": "premium", "strictness": "hard"}, "per_person_day": 883.33, "budget_level": "premium", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "premium", "strictness": "hard", "amount": 9800, "target_min_ratio": 0.75, "target_max_ratio": 1.0, "target_min_total": 7400, "target_max_total": 9800, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": true, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 2, "room_count": 1, "priced_nights": 2, "expected_min_total_hotels": 2600, "reported_total_hotels": 2600, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_standard200_realbudget_eval_000008
- request: 大理 2026-05-11->2026-05-13 days=3 transport=地铁+步行 hotel=舒适型酒店 prefs=['休闲慢游', '城市地标', '历史文化']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 115, "expected_total_attractions": 230, "reported_total_attractions": 270, "meal_per_person_cost_sum": 492, "expected_total_meals": 984, "reported_total_meals": 1008, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 115, "expected_total_attractions": 230, "reported_total_attractions": 270, "meal_per_person_cost_sum": 492, "expected_total_meals": 984, "reported_total_meals": 1008, "reported_total_transportation": 200}}]`

### v3_standard200_realbudget_eval_000001
- request: 桂林 2026-09-04->2026-09-06 days=3 transport=公共交通 hotel=高端酒店 prefs=['艺术', '美食', '第一次来', '历史文化']
- errors: `[{"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 364, "expected_total_attractions": 728, "reported_total_attractions": 728, "meal_per_person_cost_sum": 811, "expected_total_meals": 1622, "reported_total_meals": 1800, "reported_total_transportation": 200}}, {"stage": "rule", "type": "budget_preference_mismatch", "details": {"part_sum": 3928, "total": 3928, "diff": 0, "requested_budget": {"available": true, "amount": 7100, "scope": "total", "party_size": 2, "total": 7100, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "soft"}, "per_person_day": 654.67, "budget_level": "comfortable", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "soft", "amount": 7100, "target_min_ratio": 0.7, "target_max_ratio": 1.1, "target_min_total": 5000, "target_max_total": 7800, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": true, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 2, "room_count": 1, "priced_nights": 2, "expected_min_total_hotels": 1200, "reported_total_hotels": 1200, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_standard200_realbudget_eval_000007
- request: 成都 2026-05-11->2026-05-13 days=3 transport=地铁+步行 hotel=舒适型酒店 prefs=['美食', '城市公园', '休闲慢游']
- errors: `[{"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 165, "expected_total_attractions": 330, "reported_total_attractions": 330, "meal_per_person_cost_sum": 650, "expected_total_meals": 1300, "reported_total_meals": 1524, "reported_total_transportation": 200}}]`

### v3_standard200_realbudget_eval_000005
- request: 广州 2026-07-06->2026-07-08 days=3 transport=地铁+步行 hotel=经济型酒店 prefs=['博物馆', '城市公园', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 20, "expected_total_attractions": 40, "reported_total_attractions": 40, "meal_per_person_cost_sum": 662, "expected_total_meals": 1324, "reported_total_meals": 1146, "reported_total_transportation": 200}}, {"stage": "rule", "type": "budget_preference_mismatch", "details": {"part_sum": 1886, "total": 1886, "diff": 0, "requested_budget": {"available": true, "amount": 2800, "scope": "total", "party_size": 2, "total": 2800, "source": "budget_constraint", "budget_level": "limited", "strictness": "soft"}, "per_person_day": 314.33, "budget_level": "limited", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "limited", "strictness": "soft", "amount": 2800, "target_min_ratio": 0.72, "target_max_ratio": 1.05, "target_min_total": 2000, "target_max_total": 2900, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": true, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 2, "room_count": 1, "priced_nights": 2, "expected_min_total_hotels": 500, "reported_total_hotels": 500, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_standard200_realbudget_eval_000006
- request: 南京 2026-07-06->2026-07-09 days=4 transport=打车 hotel=经济型酒店 prefs=['老人友好', '美食', '城市公园', '休闲慢游']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 45, "expected_total_attractions": 135, "reported_total_attractions": 120, "meal_per_person_cost_sum": 627, "expected_total_meals": 1881, "reported_total_meals": 1950, "reported_total_transportation": 600}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 45, "expected_total_attractions": 135, "reported_total_attractions": 120, "meal_per_person_cost_sum": 627, "expected_total_meals": 1881, "reported_total_meals": 1950, "reported_total_transportation": 600}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": true, "meal_cost_scale_ok": false, "budget_relationship_ok": false, "expected_total_hotels": 1500, "reported_total_hotels": 1500, "expected_total_attractions": 135, "reported_total_attractions": 120, "meal_scale_eval": {"ok": false, "party_total": 3, "budget_level": "limited", "per_person_lunch_dinner_floor": 25, "breakfast_policy": "excluded_from_meal_cost_scale", "meal_count": 12, "checked_count": 8, "failure_count": 1, "failures": [{"date": "2026-07-09", "type": "lunch", "name": "安庆馄饨董家金牌锅贴(丰富路店)", "estimated_cost": 16, "min_expected_cost": 25}]}}}]`

### v3_standard200_realbudget_eval_000010
- request: 西安 2026-08-05->2026-08-08 days=4 transport=公共交通 hotel=经济型酒店 prefs=['城市公园', '美食']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 319, "expected_total_attractions": 638, "reported_total_attractions": 558, "meal_per_person_cost_sum": 514, "expected_total_meals": 1028, "reported_total_meals": 1302, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 319, "expected_total_attractions": 638, "reported_total_attractions": 558, "meal_per_person_cost_sum": 514, "expected_total_meals": 1028, "reported_total_meals": 1302, "reported_total_transportation": 200}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": true, "meal_cost_scale_ok": false, "budget_relationship_ok": false, "expected_total_hotels": 750, "reported_total_hotels": 750, "expected_total_attractions": 638, "reported_total_attractions": 558, "meal_scale_eval": {"ok": false, "party_total": 2, "budget_level": "standard", "per_person_lunch_dinner_floor": 35, "breakfast_policy": "excluded_from_meal_cost_scale", "meal_count": 12, "checked_count": 8, "failure_count": 3, "failures": [{"date": "2026-08-06", "type": "lunch", "name": "马洪小炒泡馍馆", "estimated_cost": 29, "min_expected_cost": 35}, {"date": "2026-08-07", "type": "lunch", "name": "天发芽何记葫芦头泡馍", "estimated_cost": 34, "min_expected_cost": 35}, {"date": "2026-08-08", "type": "lunch", "name": "邢老三肉丸糊辣汤腊牛肉夹馍总店", "estimated_cost": 18, "min_expected_cost": 35}]}}}]`

### v3_standard200_realbudget_eval_000004
- request: 张家界 2026-05-11->2026-05-15 days=5 transport=地铁+步行 hotel=舒适型酒店 prefs=['亲子', '城市漫步', '历史文化']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 4, "party_total": 4, "room_count": 2, "priced_nights": 4, "expected_min_total_hotels": 3200, "reported_total_hotels": 4800, "diff": 1600, "covers_nights": false}}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 9800, "total": 11700, "diff": -1900, "requested_budget": {"available": true, "amount": 13200, "scope": "total", "party_size": 4, "total": 13200, "source": "budget_constraint", "budget_level": "standard", "strictness": "soft"}, "per_person_day": 585.0, "budget_level": "standard", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "standard", "strictness": "soft", "amount": 13200, "target_min_ratio": 0.6, "target_max_ratio": 1.05, "target_min_total": 7900, "target_max_total": 13900, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 4, "party_total": 4, "room_count": 2, "priced_nights": 4, "expected_min_total_hotels": 3200, "reported_total_hotels": 4800, "diff": 1600, "covers_nights": false}, "hotel_budget_covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 407, "expected_total_attractions": 1628, "reported_total_attractions": 1724, "meal_per_person_cost_sum": 668, "expected_total_meals": 2672, "reported_total_meals": 2676, "reported_total_transportation": 600}}]`

### v3_standard200_realbudget_eval_000003
- request: 西安 2025-05-07->2025-05-11 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '历史文化', '购物商圈']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 319, "expected_total_attractions": 957, "reported_total_attractions": 858, "meal_per_person_cost_sum": 627, "expected_total_meals": 1881, "reported_total_meals": 2520, "reported_total_transportation": 1200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 319, "expected_total_attractions": 957, "reported_total_attractions": 858, "meal_per_person_cost_sum": 627, "expected_total_meals": 1881, "reported_total_meals": 2520, "reported_total_transportation": 1200}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": true, "meal_cost_scale_ok": false, "budget_relationship_ok": false, "expected_total_hotels": 3600, "reported_total_hotels": 3600, "expected_total_attractions": 957, "reported_total_attractions": 858, "meal_scale_eval": {"ok": false, "party_total": 3, "budget_level": "standard", "per_person_lunch_dinner_floor": 35, "breakfast_policy": "excluded_from_meal_cost_scale", "meal_count": 15, "checked_count": 10, "failure_count": 3, "failures": [{"date": "2025-05-09", "type": "dinner", "name": "天发芽何记葫芦头泡馍", "estimated_cost": 34, "min_expected_cost": 35}, {"date": "2025-05-10", "type": "dinner", "name": "马洪小炒泡馍馆", "estimated_cost": 29, "min_expected_cost": 35}, {"date": "2025-05-11", "type": "dinner", "name": "邢老三肉丸糊辣汤腊牛肉夹馍总店", "estimated_cost": 18, "min_expected_cost": 35}]}}}]`

### v3_standard200_realbudget_eval_000014
- request: 成都 2026-06-06->2026-06-07 days=2 transport=打车 hotel=经济型酒店 prefs=['小众展览', '美食', '城市地标']
- errors: `[{"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 115, "expected_total_attractions": 460, "reported_total_attractions": 460, "meal_per_person_cost_sum": 315, "expected_total_meals": 1260, "reported_total_meals": 1368, "reported_total_transportation": 400}}, {"stage": "rule", "type": "budget_preference_mismatch", "details": {"part_sum": 2828, "total": 2828, "diff": 0, "requested_budget": {"available": true, "amount": 4100, "scope": "total", "party_size": 4, "total": 4100, "source": "budget_constraint", "budget_level": "limited", "strictness": "soft"}, "per_person_day": 353.5, "budget_level": "limited", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "limited", "strictness": "soft", "amount": 4100, "target_min_ratio": 0.72, "target_max_ratio": 1.05, "target_min_total": 3000, "target_max_total": 4300, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": true, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 1, "party_total": 4, "room_count": 2, "priced_nights": 1, "expected_min_total_hotels": 600, "reported_total_hotels": 600, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_standard200_realbudget_eval_000002
- request: 杭州 2026-05-01->2026-05-05 days=5 transport=公共交通 hotel=经济型酒店 prefs=['美食', '休闲慢游', '户外轻徒步', '城市漫步']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "杭州西湖风景名胜区-断桥残雪", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-05-01", "day_index": 0, "name": "杭州西湖风景名胜区-断桥残雪"}, {"date": "2026-05-04", "day_index": 3, "name": "杭州西湖风景名胜区-断桥残雪"}]}, {"name_key": "杭州西湖风景名胜区-太子湾公园", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-05-01", "day_index": 0, "name": "杭州西湖风景名胜区-太子湾公园"}, {"date": "2026-05-04", "day_index": 3, "name": "杭州西湖风景名胜区-太子湾公园"}]}, {"name_key": "南宋德寿宫遗址博物馆", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-05-02", "day_index": 1, "name": "南宋德寿宫遗址博物馆"}, {"date": "2026-05-03", "day_index": 2, "name": "南宋德寿宫遗址博物馆"}]}, {"name_key": "清河坊步行街", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-05-02", "day_index": 1, "name": "清河坊步行街"}, {"date": "2026-05-03", "day_index": 2, "name": "清河坊步行街"}]}, {"name_key": "南宋御街中山路步行街", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-05-02", "day_index": 1, "name": "南宋御街中山路步行街"}, {"date": "2026-05-03", "day_index": 2, "name": "南宋御街中山路步行街"}]}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "知味观", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-05-01", "type": "breakfast", "name": "知味观(湖滨总店)"}, {"date": "2026-05-03", "type": "breakfast", "name": "知味观(湖滨总店)"}, {"date": "2026-05-04", "type": "breakfast", "name": "知味观(湖滨总店)"}, {"date": "2026-05-05", "type": "breakfast", "name": "知味观(湖滨总店)"}]}, {"name_key": "赵府私厨·老杭帮菜", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-05-01", "type": "lunch", "name": "赵府私厨·老杭帮菜(西湖老店)"}, {"date": "2026-05-03", "type": "lunch", "name": "赵府私厨·老杭帮菜(西湖老店)"}, {"date": "2026-05-04", "type": "lunch", "name": "赵府私厨·老杭帮菜(西湖老店)"}, {"date": "2026-05-05", "type": "lunch", "name": "赵府私厨·老杭帮菜(西湖老店)"}]}, {"name_key": "黄龙海鲜大排档", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-05-01", "type": "dinner", "name": "黄龙海鲜大排档(杭州总店)"}, {"date": "2026-05-03", "type": "dinner", "name": "黄龙海鲜大排档(杭州总店)"}, {"date": "2026-05-04", "type": "dinner", "name": "黄龙海鲜大排档(杭州总店)"}, {"date": "2026-05-05", "type": "dinner", "name": "黄龙海鲜大排档(杭州总店)"}]}]}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 10, "expected_total_attractions": 10, "reported_total_attractions": 10, "meal_per_person_cost_sum": 1428, "expected_total_meals": 1428, "reported_total_meals": 1029, "reported_total_transportation": 200}}]`

### v3_standard200_realbudget_eval_000011
- request: 福州 2026-06-21->2026-06-24 days=4 transport=打车 hotel=经济型酒店 prefs=['第一次来', '城市漫步']
- errors: `[{"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 80, "expected_total_attractions": 160, "reported_total_attractions": 160, "meal_per_person_cost_sum": 499, "expected_total_meals": 998, "reported_total_meals": 1026, "reported_total_transportation": 600}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": true, "meal_cost_scale_ok": false, "budget_relationship_ok": false, "expected_total_hotels": 600, "reported_total_hotels": 600, "expected_total_attractions": 160, "reported_total_attractions": 160, "meal_scale_eval": {"ok": false, "party_total": 2, "budget_level": "standard", "per_person_lunch_dinner_floor": 35, "breakfast_policy": "excluded_from_meal_cost_scale", "meal_count": 12, "checked_count": 8, "failure_count": 2, "failures": [{"date": "2026-06-21", "type": "dinner", "name": "后街捞化", "estimated_cost": 27, "min_expected_cost": 35}, {"date": "2026-06-23", "type": "dinner", "name": "没牙伯花生汤店", "estimated_cost": 16, "min_expected_cost": 35}]}}}, {"stage": "rule", "type": "meal_cost_scale_too_low", "details": {"ok": false, "party_total": 2, "budget_level": "standard", "per_person_lunch_dinner_floor": 35, "breakfast_policy": "excluded_from_meal_cost_scale", "meal_count": 12, "checked_count": 8, "failure_count": 2, "failures": [{"date": "2026-06-21", "type": "dinner", "name": "后街捞化", "estimated_cost": 27, "min_expected_cost": 35}, {"date": "2026-06-23", "type": "dinner", "name": "没牙伯花生汤店", "estimated_cost": 16, "min_expected_cost": 35}]}}]`

### v3_standard200_realbudget_eval_000013
- request: 武汉 2026-05-09->2026-05-11 days=3 transport=公共交通 hotel=舒适型酒店 prefs=['亲子', '老人友好', '第一次来', '城市公园']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 6282, "total": 6382, "diff": -100, "requested_budget": {"available": true, "amount": 12400, "scope": "total", "party_size": 6, "total": 12400, "source": "budget_constraint", "budget_level": "standard", "strictness": "soft"}, "per_person_day": 354.56, "budget_level": "standard", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "standard", "strictness": "soft", "amount": 12400, "target_min_ratio": 0.6, "target_max_ratio": 1.05, "target_min_total": 7400, "target_max_total": 13000, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 6, "room_count": 3, "priced_nights": 2, "expected_min_total_hotels": 2400, "reported_total_hotels": 2400, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 6, "hotel_room_count": 3, "attraction_ticket_sum": 70, "expected_total_attractions": 420, "reported_total_attractions": 420, "meal_per_person_cost_sum": 425, "expected_total_meals": 2550, "reported_total_meals": 3162, "reported_total_transportation": 300}}, {"stage": "rule", "type": "budget_preference_mismatch", "details": {"part_sum": 6282, "total": 6382, "diff": -100, "requested_budget": {"available": true, "amount": 12400, "scope": "total", "party_size": 6, "total": 12400, "source": "budget_constraint", "budget_level": "standard", "strictness": "soft"}, "per_person_day": 354.56, "budget_level": "standard", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "standard", "strictness": "soft", "amount": 12400, "target_min_ratio": 0.6, "target_max_ratio": 1.05, "target_min_total": 7400, "target_max_total": 13000, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 6, "room_count": 3, "priced_nights": 2, "expected_min_total_hotels": 2400, "reported_total_hotels": 2400, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_standard200_realbudget_eval_000016
- request: 苏州 2026-06-06->2026-06-08 days=3 transport=公共交通 hotel=民宿 prefs=['海滨度假', '城市公园', '主题乐园', '清真']
- errors: `[{"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 135, "expected_total_attractions": 270, "reported_total_attractions": 270, "meal_per_person_cost_sum": 303, "expected_total_meals": 606, "reported_total_meals": 636, "reported_total_transportation": 100}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": true, "meal_cost_scale_ok": false, "budget_relationship_ok": false, "expected_total_hotels": 600, "reported_total_hotels": 600, "expected_total_attractions": 270, "reported_total_attractions": 270, "meal_scale_eval": {"ok": false, "party_total": 2, "budget_level": "limited", "per_person_lunch_dinner_floor": 25, "breakfast_policy": "excluded_from_meal_cost_scale", "meal_count": 9, "checked_count": 6, "failure_count": 2, "failures": [{"date": "2026-06-07", "type": "lunch", "name": "魅之蘭兰州牛肉面(乐嘉汇店)", "estimated_cost": 21, "min_expected_cost": 25}, {"date": "2026-06-07", "type": "dinner", "name": "丝路回乡小吃店(西夏店)", "estimated_cost": 24, "min_expected_cost": 25}]}}}, {"stage": "rule", "type": "meal_cost_scale_too_low", "details": {"ok": false, "party_total": 2, "budget_level": "limited", "per_person_lunch_dinner_floor": 25, "breakfast_policy": "excluded_from_meal_cost_scale", "meal_count": 9, "checked_count": 6, "failure_count": 2, "failures": [{"date": "2026-06-07", "type": "lunch", "name": "魅之蘭兰州牛肉面(乐嘉汇店)", "estimated_cost": 21, "min_expected_cost": 25}, {"date": "2026-06-07", "type": "dinner", "name": "丝路回乡小吃店(西夏店)", "estimated_cost": 24, "min_expected_cost": 25}]}}]`

### v3_standard200_realbudget_eval_000018
- request: 天津 2026-07-06->2026-07-07 days=2 transport=打车 hotel=舒适型酒店 prefs=['老人友好', '夜市夜景', '艺术', '第一次来']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 182, "expected_total_attractions": 546, "reported_total_attractions": 636, "meal_per_person_cost_sum": 383, "expected_total_meals": 1149, "reported_total_meals": 1182, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 182, "expected_total_attractions": 546, "reported_total_attractions": 636, "meal_per_person_cost_sum": 383, "expected_total_meals": 1149, "reported_total_meals": 1182, "reported_total_transportation": 200}}, {"stage": "rule", "type": "budget_hard_constraint_exceeded", "details": {"part_sum": 2818, "total": 2818, "diff": 0, "requested_budget": {"available": true, "amount": 2700, "scope": "total", "party_size": 3, "total": 2700, "source": "budget_constraint", "budget_level": "limited", "strictness": "hard"}, "per_person_day": 469.67, "budget_level": "limited", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "limited", "strictness": "hard", "amount": 2700, "target_min_ratio": 0.72, "target_max_ratio": 1.0, "target_min_total": 1900, "target_max_total": 2700, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": true, "within_user_budget": true, "user_constraint_ok": false, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 1, "party_total": 3, "room_count": 2, "priced_nights": 1, "expected_min_total_hotels": 800, "reported_total_hotels": 800, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_standard200_realbudget_eval_000017
- request: 苏州 2026-05-09->2026-05-11 days=3 transport=地铁+步行 hotel=亲子酒店 prefs=['亲子', '历史文化', '休闲慢游', '户外轻徒步']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 665, "expected_total_attractions": 1995, "reported_total_attractions": 2190, "meal_per_person_cost_sum": 473, "expected_total_meals": 1419, "reported_total_meals": 2139, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 665, "expected_total_attractions": 1995, "reported_total_attractions": 2190, "meal_per_person_cost_sum": 473, "expected_total_meals": 1419, "reported_total_meals": 2139, "reported_total_transportation": 200}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": true, "meal_cost_scale_ok": false, "budget_relationship_ok": false, "expected_total_hotels": 5400, "reported_total_hotels": 5400, "expected_total_attractions": 1995, "reported_total_attractions": 2190, "meal_scale_eval": {"ok": false, "party_total": 3, "budget_level": "comfortable", "per_person_lunch_dinner_floor": 50, "breakfast_policy": "excluded_from_meal_cost_scale", "meal_count": 9, "checked_count": 6, "failure_count": 1, "failures": [{"date": "2026-05-11", "type": "dinner", "name": "万福兴(东中市总店)", "estimated_cost": 20, "min_expected_cost": 50}]}}}]`

### v3_standard200_realbudget_eval_000012
- request: 洛阳 2025-05-07->2025-05-10 days=4 transport=打车 hotel=高端酒店 prefs=['休闲慢游', '第一次来']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "方中山胡辣汤", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2025-05-07", "type": "breakfast", "name": "方中山胡辣汤(洛阳一店)"}, {"date": "2025-05-08", "type": "breakfast", "name": "方中山胡辣汤(洛阳二店)"}, {"date": "2025-05-09", "type": "breakfast", "name": "方中山胡辣汤(洛阳一店)"}, {"date": "2025-05-10", "type": "breakfast", "name": "方中山胡辣汤(洛阳二店)"}]}]}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 160, "expected_total_attractions": 480, "reported_total_attractions": 480, "meal_per_person_cost_sum": 1573, "expected_total_meals": 4719, "reported_total_meals": 5949, "reported_total_transportation": 1200}}, {"stage": "rule", "type": "budget_preference_mismatch", "details": {"part_sum": 15429, "total": 15429, "diff": 0, "requested_budget": {"available": true, "amount": 23100, "scope": "total", "party_size": 3, "total": 23100, "source": "budget_constraint", "budget_level": "premium", "strictness": "soft"}, "per_person_day": 1285.75, "budget_level": "premium", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "premium", "strictness": "soft", "amount": 23100, "target_min_ratio": 0.75, "target_max_ratio": 1.12, "target_min_total": 17300, "target_max_total": 25900, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": true, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 3, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 7800, "reported_total_hotels": 7800, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_standard200_realbudget_eval_000021
- request: 上海 2026-06-21->2026-06-22 days=2 transport=地铁+步行 hotel=经济型酒店 prefs=['老人友好', '休闲慢游', '城市漫步', '主题乐园']
- errors: `[{"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 60, "expected_total_attractions": 120, "reported_total_attractions": 120, "meal_per_person_cost_sum": 392, "expected_total_meals": 784, "reported_total_meals": 738, "reported_total_transportation": 100}}]`

### v3_standard200_realbudget_eval_000009
- request: 苏州 2026-04-30->2026-05-04 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['亲子', '城市地标', '第一次来', '城市漫步']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "稻山村·苏州菜", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-04-30", "type": "lunch", "name": "稻山村·苏州菜(石路店)"}, {"date": "2026-05-02", "type": "lunch", "name": "稻山村·苏州菜(石路店)"}, {"date": "2026-05-03", "type": "lunch", "name": "稻山村·苏州菜(石路店)"}, {"date": "2026-05-04", "type": "lunch", "name": "稻山村·苏州菜(石路店)"}]}, {"name_key": "苏外婆·苏帮菜·私房菜·松鼠桂鱼", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-04-30", "type": "dinner", "name": "苏外婆·苏帮菜·私房菜·松鼠桂鱼(平江路总店)"}, {"date": "2026-05-02", "type": "dinner", "name": "苏外婆·苏帮菜·私房菜·松鼠桂鱼(平江路总店)"}, {"date": "2026-05-03", "type": "dinner", "name": "苏外婆·苏帮菜·私房菜·松鼠桂鱼(平江路总店)"}, {"date": "2026-05-04", "type": "dinner", "name": "苏外婆·苏帮菜·私房菜·松鼠桂鱼(平江路总店)"}]}]}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 90, "expected_total_attractions": 360, "reported_total_attractions": 360, "meal_per_person_cost_sum": 949, "expected_total_meals": 3796, "reported_total_meals": 3268, "reported_total_transportation": 400}}]`

### v3_standard200_realbudget_eval_000015
- request: 南京 2026-04-07->2026-04-08 days=2 transport=地铁+步行 hotel=经济型酒店 prefs=['亲子', '休闲慢游', '历史文化']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 1, "party_total": 3, "room_count": 2, "priced_nights": 1, "expected_min_total_hotels": 500, "reported_total_hotels": 750, "diff": 250, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 45, "expected_total_attractions": 135, "reported_total_attractions": 150, "meal_per_person_cost_sum": 386, "expected_total_meals": 1158, "reported_total_meals": 1149, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 45, "expected_total_attractions": 135, "reported_total_attractions": 150, "meal_per_person_cost_sum": 386, "expected_total_meals": 1158, "reported_total_meals": 1149, "reported_total_transportation": 200}}]`
