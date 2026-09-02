# Rule Eval Report: 260513_bestofn1200_retry_final_standard_w10

- records: 200
- generations: `training/outputs/eval/by_model/sft_qwen25_7b_v3_260513_bestofn1200_retry_final/260513_bestofn1200_retry_final_standard_w10/generations.jsonl`
- records_path: `training/data/v3/eval/records.jsonl`

## Boolean Metrics

| Metric | Pass | Total | Rate |
| --- | ---: | ---: | ---: |
| accommodation_type_ok | 199 | 199 | 100.00% |
| attraction_budget_consistent | 78 | 199 | 39.20% |
| attraction_budget_party_relation_ok | 197 | 199 | 98.99% |
| attraction_count_ok | 199 | 199 | 100.00% |
| attraction_diversity_ok | 181 | 199 | 90.95% |
| attraction_grounding_ok | 199 | 199 | 100.00% |
| attraction_repeat_limit_ok | 181 | 199 | 90.95% |
| budget_arithmetic_consistent | 128 | 199 | 64.32% |
| budget_consistent | 128 | 199 | 64.32% |
| budget_level_aligned | 149 | 199 | 74.87% |
| budget_preference_aligned | 149 | 199 | 74.87% |
| budget_relationship_ok | 166 | 199 | 83.42% |
| budget_selection_ok | 120 | 199 | 60.30% |
| budget_user_constraint_ok | 199 | 199 | 100.00% |
| budget_within_user_budget | 196 | 199 | 98.49% |
| city_ok | 199 | 199 | 100.00% |
| date_range_ok | 199 | 199 | 100.00% |
| day_dates_ok | 199 | 199 | 100.00% |
| day_index_ok | 199 | 199 | 100.00% |
| days_len_ok | 199 | 199 | 100.00% |
| dpo_soft_pass | 123 | 199 | 61.81% |
| dpo_soft_recomputed_budget_pass | 104 | 199 | 52.26% |
| hard_pass | 197 | 199 | 98.99% |
| hotel_budget_covers_nights | 194 | 199 | 97.49% |
| hotel_budget_relation_ok | 195 | 199 | 97.99% |
| hotel_distance_placeholder_ok | 199 | 199 | 100.00% |
| hotel_grounding_ok | 199 | 199 | 100.00% |
| invalid_hotel_name_ok | 199 | 199 | 100.00% |
| json_extract_ok | 199 | 200 | 99.50% |
| legacy_hard_pass | 120 | 199 | 60.30% |
| location_object_ok | 199 | 199 | 100.00% |
| meal_budget_consistent | 2 | 199 | 1.01% |
| meal_complete | 199 | 199 | 100.00% |
| meal_cost_scale_ok | 170 | 199 | 85.43% |
| meal_diversity_ok | 183 | 199 | 91.96% |
| meal_grounding_ok | 197 | 199 | 98.99% |
| meal_lunch_dinner_same_day_ok | 196 | 199 | 98.49% |
| meal_repeat_limit_ok | 185 | 199 | 92.96% |
| meal_specific_ok | 199 | 199 | 100.00% |
| meal_valid_semantics_ok | 197 | 199 | 98.99% |
| middle_hotel_ok | 199 | 199 | 100.00% |
| recomputed_budget_fit_ok | 120 | 199 | 60.30% |
| recomputed_budget_hard_ok | 197 | 199 | 98.99% |
| recomputed_budget_level_aligned | 120 | 199 | 60.30% |
| recomputed_budget_preference_aligned | 120 | 199 | 60.30% |
| recomputed_budget_user_constraint_ok | 197 | 199 | 98.99% |
| recomputed_budget_within_user_budget | 185 | 199 | 92.96% |
| schema_ok | 199 | 200 | 99.50% |
| sft_budget_semantic_hard_pass | 164 | 199 | 82.41% |
| sft_hard_pass | 197 | 199 | 98.99% |
| sft_no_budget_sum_hard_pass | 197 | 199 | 98.99% |
| sft_strict_hard_pass | 1 | 199 | 0.50% |
| transportation_budget_nonnegative | 199 | 199 | 100.00% |
| weather_dates_ok | 199 | 199 | 100.00% |
| weather_match | 199 | 199 | 100.00% |

## Numeric Metrics

```json
{
  "attraction_diversity_unique_rate": {
    "avg": 0.9902,
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
    "avg": 0.9283,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_food_pois_grounding_rate": {
    "avg": 0.9992,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_grounding_rate": {
    "avg": 0.9992,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_semantic_valid_rate": {
    "avg": 0.9992,
    "p50": 1.0,
    "p90": 1.0
  },
  "recomputed_budget_per_person_day": {
    "avg": 720.9595,
    "p50": 570.25,
    "p90": 1269.33
  },
  "recomputed_budget_total": {
    "avg": 6850.3216,
    "p50": 5628.0,
    "p90": 13520.0
  }
}
```

## Failure Types

```json
{
  "meal_budget_inconsistent": 197,
  "attraction_budget_inconsistent": 121,
  "budget_arithmetic_inconsistent": 71,
  "budget_preference_mismatch": 50,
  "budget_relationship_mismatch": 33,
  "meal_cost_scale_too_low": 29,
  "attraction_repeat_too_many": 18,
  "meal_repeat_too_many": 14,
  "hotel_budget_underestimated": 5,
  "meal_same_day_lunch_dinner_repeat": 3,
  "meal_invalid_name": 2,
  "json_extract": 1
}
```

## Failure Examples

### v3_standard200_realbudget_eval_000001
- request: 桂林 2026-09-04->2026-09-06 days=3 transport=公共交通 hotel=高端酒店 prefs=['艺术', '美食', '第一次来', '历史文化']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 4014, "total": 3914, "diff": 100, "requested_budget": {"available": true, "amount": 7100, "scope": "total", "party_size": 2, "total": 7100, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "soft"}, "per_person_day": 652.33, "budget_level": "comfortable", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "soft", "amount": 7100, "target_min_ratio": 0.7, "target_max_ratio": 1.1, "target_min_total": 5000, "target_max_total": 7800, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 2, "room_count": 1, "priced_nights": 2, "expected_min_total_hotels": 1200, "reported_total_hotels": 1200, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 135, "expected_total_attractions": 270, "reported_total_attractions": 270, "meal_per_person_cost_sum": 849, "expected_total_meals": 1698, "reported_total_meals": 2144, "reported_total_transportation": 400}}, {"stage": "rule", "type": "budget_preference_mismatch", "details": {"part_sum": 4014, "total": 3914, "diff": 100, "requested_budget": {"available": true, "amount": 7100, "scope": "total", "party_size": 2, "total": 7100, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "soft"}, "per_person_day": 652.33, "budget_level": "comfortable", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "soft", "amount": 7100, "target_min_ratio": 0.7, "target_max_ratio": 1.1, "target_min_total": 5000, "target_max_total": 7800, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 2, "room_count": 1, "priced_nights": 2, "expected_min_total_hotels": 1200, "reported_total_hotels": 1200, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_standard200_realbudget_eval_000008
- request: 大理 2026-05-11->2026-05-13 days=3 transport=地铁+步行 hotel=舒适型酒店 prefs=['休闲慢游', '城市地标', '历史文化']
- errors: `[{"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 75, "expected_total_attractions": 150, "reported_total_attractions": 150, "meal_per_person_cost_sum": 501, "expected_total_meals": 1002, "reported_total_meals": 834, "reported_total_transportation": 400}}, {"stage": "rule", "type": "budget_preference_mismatch", "details": {"part_sum": 2184, "total": 2184, "diff": 0, "requested_budget": {"available": true, "amount": 3700, "scope": "total", "party_size": 2, "total": 3700, "source": "budget_constraint", "budget_level": "standard", "strictness": "soft"}, "per_person_day": 364.0, "budget_level": "standard", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "standard", "strictness": "soft", "amount": 3700, "target_min_ratio": 0.6, "target_max_ratio": 1.05, "target_min_total": 2200, "target_max_total": 3900, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": true, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 2, "room_count": 1, "priced_nights": 2, "expected_min_total_hotels": 800, "reported_total_hotels": 800, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_standard200_realbudget_eval_000007
- request: 成都 2026-05-11->2026-05-13 days=3 transport=地铁+步行 hotel=舒适型酒店 prefs=['美食', '城市公园', '休闲慢游']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 2964, "total": 3064, "diff": -100, "requested_budget": {"available": true, "amount": 4600, "scope": "total", "party_size": 2, "total": 4600, "source": "budget_constraint", "budget_level": "standard", "strictness": "hard"}, "per_person_day": 510.67, "budget_level": "standard", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "standard", "strictness": "hard", "amount": 4600, "target_min_ratio": 0.6, "target_max_ratio": 1.0, "target_min_total": 2800, "target_max_total": 4600, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 2, "room_count": 1, "priced_nights": 2, "expected_min_total_hotels": 900, "reported_total_hotels": 900, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 165, "expected_total_attractions": 330, "reported_total_attractions": 330, "meal_per_person_cost_sum": 701, "expected_total_meals": 1402, "reported_total_meals": 1634, "reported_total_transportation": 100}}]`

### v3_standard200_realbudget_eval_000005
- request: 广州 2026-07-06->2026-07-08 days=3 transport=地铁+步行 hotel=经济型酒店 prefs=['博物馆', '城市公园', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 170, "expected_total_attractions": 340, "reported_total_attractions": 340, "meal_per_person_cost_sum": 648, "expected_total_meals": 1296, "reported_total_meals": 1184, "reported_total_transportation": 200}}]`

### v3_standard200_realbudget_eval_000000
- request: 昆明 2026-04-07->2026-04-09 days=3 transport=地铁+步行 hotel=高端酒店 prefs=['休闲慢游', '美食']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 6416, "total": 7416, "diff": -1000, "requested_budget": {"available": true, "amount": 9800, "scope": "total", "party_size": 2, "total": 9800, "source": "budget_constraint", "budget_level": "premium", "strictness": "hard"}, "per_person_day": 1236.0, "budget_level": "premium", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "premium", "strictness": "hard", "amount": 9800, "target_min_ratio": 0.75, "target_max_ratio": 1.0, "target_min_total": 7400, "target_max_total": 9800, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 2, "room_count": 1, "priced_nights": 2, "expected_min_total_hotels": 2600, "reported_total_hotels": 2600, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 770, "expected_total_attractions": 1540, "reported_total_attractions": 1874, "meal_per_person_cost_sum": 736, "expected_total_meals": 1472, "reported_total_meals": 1722, "reported_total_transportation": 220}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 770, "expected_total_attractions": 1540, "reported_total_attractions": 1874, "meal_per_person_cost_sum": 736, "expected_total_meals": 1472, "reported_total_meals": 1722, "reported_total_transportation": 220}}]`

### v3_standard200_realbudget_eval_000006
- request: 南京 2026-07-06->2026-07-09 days=4 transport=打车 hotel=经济型酒店 prefs=['老人友好', '美食', '城市公园', '休闲慢游']
- errors: `[{"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 70, "expected_total_attractions": 210, "reported_total_attractions": 210, "meal_per_person_cost_sum": 791, "expected_total_meals": 2373, "reported_total_meals": 2430, "reported_total_transportation": 800}}]`

### v3_standard200_realbudget_eval_000004
- request: 张家界 2026-05-11->2026-05-15 days=5 transport=地铁+步行 hotel=舒适型酒店 prefs=['亲子', '城市漫步', '历史文化']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "七十二奇楼景区", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-05-11", "day_index": 0, "name": "七十二奇楼景区"}, {"date": "2026-05-14", "day_index": 3, "name": "七十二奇楼景区"}]}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 4, "party_total": 4, "room_count": 2, "priced_nights": 4, "expected_min_total_hotels": 3200, "reported_total_hotels": 4800, "diff": 1600, "covers_nights": false}}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 9900, "total": 9800, "diff": 100, "requested_budget": {"available": true, "amount": 13200, "scope": "total", "party_size": 4, "total": 13200, "source": "budget_constraint", "budget_level": "standard", "strictness": "soft"}, "per_person_day": 490.0, "budget_level": "standard", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "standard", "strictness": "soft", "amount": 13200, "target_min_ratio": 0.6, "target_max_ratio": 1.05, "target_min_total": 7900, "target_max_total": 13900, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 4, "party_total": 4, "room_count": 2, "priced_nights": 4, "expected_min_total_hotels": 3200, "reported_total_hotels": 4800, "diff": 1600, "covers_nights": false}, "hotel_budget_covers_nights": false}}]`

### v3_standard200_realbudget_eval_000003
- request: 西安 2025-05-07->2025-05-11 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '历史文化', '购物商圈']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "西安博物院", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2025-05-10", "day_index": 3, "name": "西安博物院"}, {"date": "2025-05-11", "day_index": 4, "name": "西安博物院"}]}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 4, "party_total": 3, "room_count": 2, "priced_nights": 4, "expected_min_total_hotels": 3600, "reported_total_hotels": 5400, "diff": 1800, "covers_nights": false}}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 10398, "total": 9398, "diff": 1000, "requested_budget": {"available": true, "amount": 15700, "scope": "total", "party_size": 3, "total": 15700, "source": "budget_constraint", "budget_level": "standard", "strictness": "soft"}, "per_person_day": 626.53, "budget_level": "standard", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "standard", "strictness": "soft", "amount": 15700, "target_min_ratio": 0.6, "target_max_ratio": 1.05, "target_min_total": 9400, "target_max_total": 16500, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 4, "party_total": 3, "room_count": 2, "priced_nights": 4, "expected_min_total_hotels": 3600, "reported_total_hotels": 5400, "diff": 1800, "covers_nights": false}, "hotel_budget_covers_nights": false}}]`

### v3_standard200_realbudget_eval_000010
- request: 西安 2026-08-05->2026-08-08 days=4 transport=公共交通 hotel=经济型酒店 prefs=['城市公园', '美食']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 2980, "total": 3080, "diff": -100, "requested_budget": {"available": true, "amount": 6600, "scope": "total", "party_size": 2, "total": 6600, "source": "budget_constraint", "budget_level": "standard", "strictness": "soft"}, "per_person_day": 385.0, "budget_level": "standard", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "standard", "strictness": "soft", "amount": 6600, "target_min_ratio": 0.6, "target_max_ratio": 1.05, "target_min_total": 4000, "target_max_total": 6900, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 2, "room_count": 1, "priced_nights": 3, "expected_min_total_hotels": 750, "reported_total_hotels": 750, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 387, "expected_total_attractions": 774, "reported_total_attractions": 726, "meal_per_person_cost_sum": 570, "expected_total_meals": 1140, "reported_total_meals": 1304, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 387, "expected_total_attractions": 774, "reported_total_attractions": 726, "meal_per_person_cost_sum": 570, "expected_total_meals": 1140, "reported_total_meals": 1304, "reported_total_transportation": 200}}]`

### v3_standard200_realbudget_eval_000002
- request: 杭州 2026-05-01->2026-05-05 days=5 transport=公共交通 hotel=经济型酒店 prefs=['美食', '休闲慢游', '户外轻徒步', '城市漫步']
- errors: `[{"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 160, "expected_total_attractions": 160, "reported_total_attractions": 160, "meal_per_person_cost_sum": 957, "expected_total_meals": 957, "reported_total_meals": 1032, "reported_total_transportation": 200}}, {"stage": "rule", "type": "budget_preference_mismatch", "details": {"part_sum": 2392, "total": 2392, "diff": 0, "requested_budget": {"available": true, "amount": 3400, "scope": "total", "party_size": 1, "total": 3400, "source": "budget_constraint", "budget_level": "limited", "strictness": "soft"}, "per_person_day": 478.4, "budget_level": "limited", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "limited", "strictness": "soft", "amount": 3400, "target_min_ratio": 0.72, "target_max_ratio": 1.05, "target_min_total": 2400, "target_max_total": 3600, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": true, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 4, "party_total": 1, "room_count": 1, "priced_nights": 4, "expected_min_total_hotels": 1000, "reported_total_hotels": 1000, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_standard200_realbudget_eval_000014
- request: 成都 2026-06-06->2026-06-07 days=2 transport=打车 hotel=经济型酒店 prefs=['小众展览', '美食', '城市地标']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 4008, "total": 3908, "diff": 100, "requested_budget": {"available": true, "amount": 4100, "scope": "total", "party_size": 4, "total": 4100, "source": "budget_constraint", "budget_level": "limited", "strictness": "soft"}, "per_person_day": 488.5, "budget_level": "limited", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "limited", "strictness": "soft", "amount": 4100, "target_min_ratio": 0.72, "target_max_ratio": 1.05, "target_min_total": 3000, "target_max_total": 4300, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 1, "party_total": 4, "room_count": 2, "priced_nights": 1, "expected_min_total_hotels": 600, "reported_total_hotels": 600, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 115, "expected_total_attractions": 460, "reported_total_attractions": 460, "meal_per_person_cost_sum": 641, "expected_total_meals": 2564, "reported_total_meals": 2248, "reported_total_transportation": 700}}]`

### v3_standard200_realbudget_eval_000013
- request: 武汉 2026-05-09->2026-05-11 days=3 transport=公共交通 hotel=舒适型酒店 prefs=['亲子', '老人友好', '第一次来', '城市公园']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 8380, "total": 7380, "diff": 1000, "requested_budget": {"available": true, "amount": 12400, "scope": "total", "party_size": 6, "total": 12400, "source": "budget_constraint", "budget_level": "standard", "strictness": "soft"}, "per_person_day": 410.0, "budget_level": "standard", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "standard", "strictness": "soft", "amount": 12400, "target_min_ratio": 0.6, "target_max_ratio": 1.05, "target_min_total": 7400, "target_max_total": 13000, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 6, "room_count": 3, "priced_nights": 2, "expected_min_total_hotels": 2400, "reported_total_hotels": 2400, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 6, "hotel_room_count": 3, "attraction_ticket_sum": 130, "expected_total_attractions": 780, "reported_total_attractions": 840, "meal_per_person_cost_sum": 489, "expected_total_meals": 2934, "reported_total_meals": 3840, "reported_total_transportation": 1300}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 6, "hotel_room_count": 3, "attraction_ticket_sum": 130, "expected_total_attractions": 780, "reported_total_attractions": 840, "meal_per_person_cost_sum": 489, "expected_total_meals": 2934, "reported_total_meals": 3840, "reported_total_transportation": 1300}}]`

### v3_standard200_realbudget_eval_000016
- request: 苏州 2026-06-06->2026-06-08 days=3 transport=公共交通 hotel=民宿 prefs=['海滨度假', '城市公园', '主题乐园', '清真']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 1908, "total": 2008, "diff": -100, "requested_budget": {"available": true, "amount": 2800, "scope": "total", "party_size": 2, "total": 2800, "source": "budget_constraint", "budget_level": "limited", "strictness": "soft"}, "per_person_day": 334.67, "budget_level": "limited", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "limited", "strictness": "soft", "amount": 2800, "target_min_ratio": 0.72, "target_max_ratio": 1.05, "target_min_total": 2000, "target_max_total": 2900, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 2, "room_count": 1, "priced_nights": 2, "expected_min_total_hotels": 600, "reported_total_hotels": 600, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 140, "expected_total_attractions": 280, "reported_total_attractions": 270, "meal_per_person_cost_sum": 349, "expected_total_meals": 698, "reported_total_meals": 838, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 140, "expected_total_attractions": 280, "reported_total_attractions": 270, "meal_per_person_cost_sum": 349, "expected_total_meals": 698, "reported_total_meals": 838, "reported_total_transportation": 200}}]`

### v3_standard200_realbudget_eval_000018
- request: 天津 2026-07-06->2026-07-07 days=2 transport=打车 hotel=舒适型酒店 prefs=['老人友好', '夜市夜景', '艺术', '第一次来']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 130, "expected_total_attractions": 390, "reported_total_attractions": 450, "meal_per_person_cost_sum": 313, "expected_total_meals": 939, "reported_total_meals": 951, "reported_total_transportation": 100}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 130, "expected_total_attractions": 390, "reported_total_attractions": 450, "meal_per_person_cost_sum": 313, "expected_total_meals": 939, "reported_total_meals": 951, "reported_total_transportation": 100}}]`

### v3_standard200_realbudget_eval_000011
- request: 福州 2026-06-21->2026-06-24 days=4 transport=打车 hotel=经济型酒店 prefs=['第一次来', '城市漫步']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 210, "expected_total_attractions": 420, "reported_total_attractions": 404, "meal_per_person_cost_sum": 694, "expected_total_meals": 1388, "reported_total_meals": 1338, "reported_total_transportation": 1200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 210, "expected_total_attractions": 420, "reported_total_attractions": 404, "meal_per_person_cost_sum": 694, "expected_total_meals": 1388, "reported_total_meals": 1338, "reported_total_transportation": 1200}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": true, "meal_cost_scale_ok": false, "budget_relationship_ok": false, "expected_total_hotels": 600, "reported_total_hotels": 600, "expected_total_attractions": 420, "reported_total_attractions": 404, "meal_scale_eval": {"ok": false, "party_total": 2, "budget_level": "standard", "per_person_lunch_dinner_floor": 35, "breakfast_policy": "excluded_from_meal_cost_scale", "meal_count": 12, "checked_count": 8, "failure_count": 1, "failures": [{"date": "2026-06-21", "type": "lunch", "name": "后街捞化", "estimated_cost": 27, "min_expected_cost": 35}]}}}]`

### v3_standard200_realbudget_eval_000017
- request: 苏州 2026-05-09->2026-05-11 days=3 transport=地铁+步行 hotel=亲子酒店 prefs=['亲子', '历史文化', '休闲慢游', '户外轻徒步']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 8165, "total": 7165, "diff": 1000, "requested_budget": {"available": true, "amount": 10000, "scope": "total", "party_size": 3, "total": 10000, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "soft"}, "per_person_day": 796.11, "budget_level": "comfortable", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "soft", "amount": 10000, "target_min_ratio": 0.7, "target_max_ratio": 1.1, "target_min_total": 7000, "target_max_total": 11000, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 3, "room_count": 2, "priced_nights": 2, "expected_min_total_hotels": 5400, "reported_total_hotels": 5400, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 320, "expected_total_attractions": 960, "reported_total_attractions": 1035, "meal_per_person_cost_sum": 510, "expected_total_meals": 1530, "reported_total_meals": 1530, "reported_total_transportation": 200}}]`

### v3_standard200_realbudget_eval_000021
- request: 上海 2026-06-21->2026-06-22 days=2 transport=地铁+步行 hotel=经济型酒店 prefs=['老人友好', '休闲慢游', '城市漫步', '主题乐园']
- errors: `[{"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 70, "expected_total_attractions": 140, "reported_total_attractions": 140, "meal_per_person_cost_sum": 604, "expected_total_meals": 1208, "reported_total_meals": 1104, "reported_total_transportation": 90}}]`

### v3_standard200_realbudget_eval_000012
- request: 洛阳 2025-05-07->2025-05-10 days=4 transport=打车 hotel=高端酒店 prefs=['休闲慢游', '第一次来']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 990, "expected_total_attractions": 2970, "reported_total_attractions": 3198, "meal_per_person_cost_sum": 2318, "expected_total_meals": 6954, "reported_total_meals": 7200, "reported_total_transportation": 4000}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 990, "expected_total_attractions": 2970, "reported_total_attractions": 3198, "meal_per_person_cost_sum": 2318, "expected_total_meals": 6954, "reported_total_meals": 7200, "reported_total_transportation": 4000}}]`

### v3_standard200_realbudget_eval_000020
- request: 杭州 2026-06-21->2026-06-24 days=4 transport=地铁+步行 hotel=高端酒店 prefs=['历史文化', '海滨度假']
- errors: `[{"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 150, "expected_total_attractions": 300, "reported_total_attractions": 300, "meal_per_person_cost_sum": 977, "expected_total_meals": 1954, "reported_total_meals": 2104, "reported_total_transportation": 400}}, {"stage": "rule", "type": "budget_preference_mismatch", "details": {"part_sum": 7304, "total": 7304, "diff": 0, "requested_budget": {"available": true, "amount": 10600, "scope": "total", "party_size": 2, "total": 10600, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "soft"}, "per_person_day": 913.0, "budget_level": "comfortable", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "soft", "amount": 10600, "target_min_ratio": 0.7, "target_max_ratio": 1.1, "target_min_total": 7400, "target_max_total": 11700, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": true, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 2, "room_count": 1, "priced_nights": 3, "expected_min_total_hotels": 4500, "reported_total_hotels": 4500, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_standard200_realbudget_eval_000015
- request: 南京 2026-04-07->2026-04-08 days=2 transport=地铁+步行 hotel=经济型酒店 prefs=['亲子', '休闲慢游', '历史文化']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 145, "expected_total_attractions": 435, "reported_total_attractions": 495, "meal_per_person_cost_sum": 396, "expected_total_meals": 1188, "reported_total_meals": 1353, "reported_total_transportation": 300}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 145, "expected_total_attractions": 435, "reported_total_attractions": 495, "meal_per_person_cost_sum": 396, "expected_total_meals": 1188, "reported_total_meals": 1353, "reported_total_transportation": 300}}]`
