# Rule Eval Report: 260511_high_end_context_standard_w10

- records: 200
- generations: `training/outputs/eval/by_model/sft_qwen25_7b_v3_260512_bestofn_replay_final/260511_high_end_context_standard_w10/generations.jsonl`
- records_path: `training/data/v3/eval/records.jsonl`

## Boolean Metrics

| Metric | Pass | Total | Rate |
| --- | ---: | ---: | ---: |
| accommodation_type_ok | 200 | 200 | 100.00% |
| attraction_budget_consistent | 73 | 200 | 36.50% |
| attraction_budget_party_relation_ok | 197 | 200 | 98.50% |
| attraction_count_ok | 200 | 200 | 100.00% |
| attraction_diversity_ok | 185 | 200 | 92.50% |
| attraction_grounding_ok | 200 | 200 | 100.00% |
| attraction_repeat_limit_ok | 185 | 200 | 92.50% |
| budget_arithmetic_consistent | 141 | 200 | 70.50% |
| budget_consistent | 141 | 200 | 70.50% |
| budget_level_aligned | 154 | 200 | 77.00% |
| budget_preference_aligned | 154 | 200 | 77.00% |
| budget_relationship_ok | 168 | 200 | 84.00% |
| budget_selection_ok | 119 | 200 | 59.50% |
| budget_user_constraint_ok | 199 | 200 | 99.50% |
| budget_within_user_budget | 194 | 200 | 97.00% |
| city_ok | 200 | 200 | 100.00% |
| date_range_ok | 200 | 200 | 100.00% |
| day_dates_ok | 200 | 200 | 100.00% |
| day_index_ok | 200 | 200 | 100.00% |
| days_len_ok | 200 | 200 | 100.00% |
| dpo_soft_pass | 131 | 200 | 65.50% |
| dpo_soft_recomputed_budget_pass | 107 | 200 | 53.50% |
| hard_pass | 198 | 200 | 99.00% |
| hotel_budget_covers_nights | 196 | 200 | 98.00% |
| hotel_budget_relation_ok | 197 | 200 | 98.50% |
| hotel_distance_placeholder_ok | 200 | 200 | 100.00% |
| hotel_grounding_ok | 200 | 200 | 100.00% |
| invalid_hotel_name_ok | 200 | 200 | 100.00% |
| json_extract_ok | 200 | 200 | 100.00% |
| legacy_hard_pass | 123 | 200 | 61.50% |
| location_object_ok | 200 | 200 | 100.00% |
| meal_budget_consistent | 0 | 200 | 0.00% |
| meal_complete | 200 | 200 | 100.00% |
| meal_cost_scale_ok | 172 | 200 | 86.00% |
| meal_diversity_ok | 181 | 200 | 90.50% |
| meal_grounding_ok | 198 | 200 | 99.00% |
| meal_lunch_dinner_same_day_ok | 197 | 200 | 98.50% |
| meal_repeat_limit_ok | 184 | 200 | 92.00% |
| meal_specific_ok | 200 | 200 | 100.00% |
| meal_valid_semantics_ok | 198 | 200 | 99.00% |
| middle_hotel_ok | 200 | 200 | 100.00% |
| recomputed_budget_fit_ok | 119 | 200 | 59.50% |
| recomputed_budget_hard_ok | 196 | 200 | 98.00% |
| recomputed_budget_level_aligned | 119 | 200 | 59.50% |
| recomputed_budget_preference_aligned | 119 | 200 | 59.50% |
| recomputed_budget_user_constraint_ok | 196 | 200 | 98.00% |
| recomputed_budget_within_user_budget | 186 | 200 | 93.00% |
| schema_ok | 200 | 200 | 100.00% |
| sft_budget_semantic_hard_pass | 165 | 200 | 82.50% |
| sft_hard_pass | 198 | 200 | 99.00% |
| sft_no_budget_sum_hard_pass | 198 | 200 | 99.00% |
| sft_strict_hard_pass | 0 | 200 | 0.00% |
| transportation_budget_nonnegative | 200 | 200 | 100.00% |
| weather_dates_ok | 200 | 200 | 100.00% |
| weather_match | 200 | 200 | 100.00% |

## Numeric Metrics

```json
{
  "attraction_diversity_unique_rate": {
    "avg": 0.9903,
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
    "avg": 0.9299,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_food_pois_grounding_rate": {
    "avg": 0.9991,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_grounding_rate": {
    "avg": 0.9991,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_semantic_valid_rate": {
    "avg": 0.9991,
    "p50": 1.0,
    "p90": 1.0
  },
  "recomputed_budget_per_person_day": {
    "avg": 731.0978,
    "p50": 603.0,
    "p90": 1299.67
  },
  "recomputed_budget_total": {
    "avg": 6940.035,
    "p50": 5632.0,
    "p90": 13650.0
  }
}
```

## Failure Types

```json
{
  "meal_budget_inconsistent": 200,
  "attraction_budget_inconsistent": 127,
  "budget_arithmetic_inconsistent": 59,
  "budget_preference_mismatch": 46,
  "budget_relationship_mismatch": 32,
  "meal_cost_scale_too_low": 28,
  "meal_repeat_too_many": 16,
  "attraction_repeat_too_many": 15,
  "hotel_budget_underestimated": 4,
  "meal_same_day_lunch_dinner_repeat": 3,
  "meal_invalid_name": 2,
  "budget_hard_constraint_exceeded": 1
}
```

## Failure Examples

### v3_standard200_realbudget_eval_000000
- request: 昆明 2026-04-07->2026-04-09 days=3 transport=地铁+步行 hotel=高端酒店 prefs=['休闲慢游', '美食']
- errors: `[{"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-04-08", "type": "dinner", "name": "石屏会馆", "reason": "unknown_food_semantics"}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 333, "expected_total_attractions": 666, "reported_total_attractions": 706, "meal_per_person_cost_sum": 773, "expected_total_meals": 1546, "reported_total_meals": 2294, "reported_total_transportation": 1800}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 333, "expected_total_attractions": 666, "reported_total_attractions": 706, "meal_per_person_cost_sum": 773, "expected_total_meals": 1546, "reported_total_meals": 2294, "reported_total_transportation": 1800}}]`

### v3_standard200_realbudget_eval_000001
- request: 桂林 2026-09-04->2026-09-06 days=3 transport=公共交通 hotel=高端酒店 prefs=['艺术', '美食', '第一次来', '历史文化']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 345, "expected_total_attractions": 690, "reported_total_attractions": 790, "meal_per_person_cost_sum": 849, "expected_total_meals": 1698, "reported_total_meals": 2044, "reported_total_transportation": 1000}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 345, "expected_total_attractions": 690, "reported_total_attractions": 790, "meal_per_person_cost_sum": 849, "expected_total_meals": 1698, "reported_total_meals": 2044, "reported_total_transportation": 1000}}]`

### v3_standard200_realbudget_eval_000005
- request: 广州 2026-07-06->2026-07-08 days=3 transport=地铁+步行 hotel=经济型酒店 prefs=['博物馆', '城市公园', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 170, "expected_total_attractions": 340, "reported_total_attractions": 340, "meal_per_person_cost_sum": 637, "expected_total_meals": 1274, "reported_total_meals": 1184, "reported_total_transportation": 200}}]`

### v3_standard200_realbudget_eval_000007
- request: 成都 2026-05-11->2026-05-13 days=3 transport=地铁+步行 hotel=舒适型酒店 prefs=['美食', '城市公园', '休闲慢游']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 2964, "total": 3064, "diff": -100, "requested_budget": {"available": true, "amount": 4600, "scope": "total", "party_size": 2, "total": 4600, "source": "budget_constraint", "budget_level": "standard", "strictness": "hard"}, "per_person_day": 510.67, "budget_level": "standard", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "standard", "strictness": "hard", "amount": 4600, "target_min_ratio": 0.6, "target_max_ratio": 1.0, "target_min_total": 2800, "target_max_total": 4600, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 2, "room_count": 1, "priced_nights": 2, "expected_min_total_hotels": 900, "reported_total_hotels": 900, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 165, "expected_total_attractions": 330, "reported_total_attractions": 330, "meal_per_person_cost_sum": 656, "expected_total_meals": 1312, "reported_total_meals": 1434, "reported_total_transportation": 300}}]`

### v3_standard200_realbudget_eval_000008
- request: 大理 2026-05-11->2026-05-13 days=3 transport=地铁+步行 hotel=舒适型酒店 prefs=['休闲慢游', '城市地标', '历史文化']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 115, "expected_total_attractions": 230, "reported_total_attractions": 250, "meal_per_person_cost_sum": 492, "expected_total_meals": 984, "reported_total_meals": 834, "reported_total_transportation": 300}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 115, "expected_total_attractions": 230, "reported_total_attractions": 250, "meal_per_person_cost_sum": 492, "expected_total_meals": 984, "reported_total_meals": 834, "reported_total_transportation": 300}}, {"stage": "rule", "type": "budget_preference_mismatch", "details": {"part_sum": 2184, "total": 2184, "diff": 0, "requested_budget": {"available": true, "amount": 3700, "scope": "total", "party_size": 2, "total": 3700, "source": "budget_constraint", "budget_level": "standard", "strictness": "soft"}, "per_person_day": 364.0, "budget_level": "standard", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "standard", "strictness": "soft", "amount": 3700, "target_min_ratio": 0.6, "target_max_ratio": 1.05, "target_min_total": 2200, "target_max_total": 3900, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": true, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 2, "room_count": 1, "priced_nights": 2, "expected_min_total_hotels": 800, "reported_total_hotels": 800, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_standard200_realbudget_eval_000006
- request: 南京 2026-07-06->2026-07-09 days=4 transport=打车 hotel=经济型酒店 prefs=['老人友好', '美食', '城市公园', '休闲慢游']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 100, "expected_total_attractions": 300, "reported_total_attractions": 330, "meal_per_person_cost_sum": 834, "expected_total_meals": 2502, "reported_total_meals": 2469, "reported_total_transportation": 700}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 100, "expected_total_attractions": 300, "reported_total_attractions": 330, "meal_per_person_cost_sum": 834, "expected_total_meals": 2502, "reported_total_meals": 2469, "reported_total_transportation": 700}}]`

### v3_standard200_realbudget_eval_000004
- request: 张家界 2026-05-11->2026-05-15 days=5 transport=地铁+步行 hotel=舒适型酒店 prefs=['亲子', '城市漫步', '历史文化']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "麦当劳", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-05-11", "type": "breakfast", "name": "麦当劳(泊富国际文化广场店)"}, {"date": "2026-05-12", "type": "breakfast", "name": "麦当劳(天门中心广场店)"}, {"date": "2026-05-13", "type": "breakfast", "name": "麦当劳(天门中心广场店)"}, {"date": "2026-05-14", "type": "breakfast", "name": "麦当劳(泊富国际文化广场店)"}, {"date": "2026-05-15", "type": "breakfast", "name": "麦当劳(泊富国际文化广场店)"}]}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 4, "party_total": 4, "room_count": 2, "priced_nights": 4, "expected_min_total_hotels": 4800, "reported_total_hotels": 7200, "diff": 2400, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 221, "expected_total_attractions": 884, "reported_total_attractions": 1244, "meal_per_person_cost_sum": 682, "expected_total_meals": 2728, "reported_total_meals": 3096, "reported_total_transportation": 1700}}]`

### v3_standard200_realbudget_eval_000010
- request: 西安 2026-08-05->2026-08-08 days=4 transport=公共交通 hotel=经济型酒店 prefs=['城市公园', '美食']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "大唐不夜城", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-08-05", "day_index": 0, "name": "大唐不夜城"}, {"date": "2026-08-07", "day_index": 2, "name": "大唐不夜城"}]}]}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 3064, "total": 2464, "diff": 600, "requested_budget": {"available": true, "amount": 6600, "scope": "total", "party_size": 2, "total": 6600, "source": "budget_constraint", "budget_level": "standard", "strictness": "soft"}, "per_person_day": 308.0, "budget_level": "standard", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "standard", "strictness": "soft", "amount": 6600, "target_min_ratio": 0.6, "target_max_ratio": 1.05, "target_min_total": 4000, "target_max_total": 6900, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 2, "room_count": 1, "priced_nights": 3, "expected_min_total_hotels": 750, "reported_total_hotels": 750, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 319, "expected_total_attractions": 638, "reported_total_attractions": 658, "meal_per_person_cost_sum": 582, "expected_total_meals": 1164, "reported_total_meals": 1356, "reported_total_transportation": 300}}]`

### v3_standard200_realbudget_eval_000003
- request: 西安 2025-05-07->2025-05-11 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '历史文化', '购物商圈']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 4, "party_total": 3, "room_count": 2, "priced_nights": 4, "expected_min_total_hotels": 3600, "reported_total_hotels": 5400, "diff": 1800, "covers_nights": false}}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 16600, "total": 16500, "diff": 100, "requested_budget": {"available": true, "amount": 15700, "scope": "total", "party_size": 3, "total": 15700, "source": "budget_constraint", "budget_level": "standard", "strictness": "soft"}, "per_person_day": 1100.0, "budget_level": "standard", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "standard", "strictness": "soft", "amount": 15700, "target_min_ratio": 0.6, "target_max_ratio": 1.05, "target_min_total": 9400, "target_max_total": 16500, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 4, "party_total": 3, "room_count": 2, "priced_nights": 4, "expected_min_total_hotels": 3600, "reported_total_hotels": 5400, "diff": 1800, "covers_nights": false}, "hotel_budget_covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 319, "expected_total_attractions": 957, "reported_total_attractions": 1038, "meal_per_person_cost_sum": 822, "expected_total_meals": 2466, "reported_total_meals": 3762, "reported_total_transportation": 6400}}]`

### v3_standard200_realbudget_eval_000002
- request: 杭州 2026-05-01->2026-05-05 days=5 transport=公共交通 hotel=经济型酒店 prefs=['美食', '休闲慢游', '户外轻徒步', '城市漫步']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 160, "expected_total_attractions": 160, "reported_total_attractions": 150, "meal_per_person_cost_sum": 963, "expected_total_meals": 963, "reported_total_meals": 1098, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 160, "expected_total_attractions": 160, "reported_total_attractions": 150, "meal_per_person_cost_sum": 963, "expected_total_meals": 963, "reported_total_meals": 1098, "reported_total_transportation": 200}}]`

### v3_standard200_realbudget_eval_000014
- request: 成都 2026-06-06->2026-06-07 days=2 transport=打车 hotel=经济型酒店 prefs=['小众展览', '美食', '城市地标']
- errors: `[{"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 165, "expected_total_attractions": 660, "reported_total_attractions": 660, "meal_per_person_cost_sum": 610, "expected_total_meals": 2440, "reported_total_meals": 2248, "reported_total_transportation": 100}}]`

### v3_standard200_realbudget_eval_000013
- request: 武汉 2026-05-09->2026-05-11 days=3 transport=公共交通 hotel=舒适型酒店 prefs=['亲子', '老人友好', '第一次来', '城市公园']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 6, "hotel_room_count": 3, "attraction_ticket_sum": 130, "expected_total_attractions": 780, "reported_total_attractions": 720, "meal_per_person_cost_sum": 551, "expected_total_meals": 3306, "reported_total_meals": 3840, "reported_total_transportation": 400}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 6, "hotel_room_count": 3, "attraction_ticket_sum": 130, "expected_total_attractions": 780, "reported_total_attractions": 720, "meal_per_person_cost_sum": 551, "expected_total_meals": 3306, "reported_total_meals": 3840, "reported_total_transportation": 400}}, {"stage": "rule", "type": "budget_preference_mismatch", "details": {"part_sum": 7360, "total": 7360, "diff": 0, "requested_budget": {"available": true, "amount": 12400, "scope": "total", "party_size": 6, "total": 12400, "source": "budget_constraint", "budget_level": "standard", "strictness": "soft"}, "per_person_day": 408.89, "budget_level": "standard", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "standard", "strictness": "soft", "amount": 12400, "target_min_ratio": 0.6, "target_max_ratio": 1.05, "target_min_total": 7400, "target_max_total": 13000, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": true, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 6, "room_count": 3, "priced_nights": 2, "expected_min_total_hotels": 2400, "reported_total_hotels": 2400, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_standard200_realbudget_eval_000018
- request: 天津 2026-07-06->2026-07-07 days=2 transport=打车 hotel=舒适型酒店 prefs=['老人友好', '夜市夜景', '艺术', '第一次来']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 3001, "total": 2001, "diff": 1000, "requested_budget": {"available": true, "amount": 2700, "scope": "total", "party_size": 3, "total": 2700, "source": "budget_constraint", "budget_level": "limited", "strictness": "hard"}, "per_person_day": 333.5, "budget_level": "limited", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "limited", "strictness": "hard", "amount": 2700, "target_min_ratio": 0.72, "target_max_ratio": 1.0, "target_min_total": 1900, "target_max_total": 2700, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 1, "party_total": 3, "room_count": 2, "priced_nights": 1, "expected_min_total_hotels": 800, "reported_total_hotels": 800, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 130, "expected_total_attractions": 390, "reported_total_attractions": 450, "meal_per_person_cost_sum": 416, "expected_total_meals": 1248, "reported_total_meals": 1251, "reported_total_transportation": 500}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 130, "expected_total_attractions": 390, "reported_total_attractions": 450, "meal_per_person_cost_sum": 416, "expected_total_meals": 1248, "reported_total_meals": 1251, "reported_total_transportation": 500}}]`

### v3_standard200_realbudget_eval_000017
- request: 苏州 2026-05-09->2026-05-11 days=3 transport=地铁+步行 hotel=亲子酒店 prefs=['亲子', '历史文化', '休闲慢游', '户外轻徒步']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 315, "expected_total_attractions": 945, "reported_total_attractions": 1035, "meal_per_person_cost_sum": 520, "expected_total_meals": 1560, "reported_total_meals": 1938, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 315, "expected_total_attractions": 945, "reported_total_attractions": 1035, "meal_per_person_cost_sum": 520, "expected_total_meals": 1560, "reported_total_meals": 1938, "reported_total_transportation": 200}}]`

### v3_standard200_realbudget_eval_000012
- request: 洛阳 2025-05-07->2025-05-10 days=4 transport=打车 hotel=高端酒店 prefs=['休闲慢游', '第一次来']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 320, "expected_total_attractions": 960, "reported_total_attractions": 1080, "meal_per_person_cost_sum": 1612, "expected_total_meals": 4836, "reported_total_meals": 6699, "reported_total_transportation": 2000}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 320, "expected_total_attractions": 960, "reported_total_attractions": 1080, "meal_per_person_cost_sum": 1612, "expected_total_meals": 4836, "reported_total_meals": 6699, "reported_total_transportation": 2000}}]`

### v3_standard200_realbudget_eval_000011
- request: 福州 2026-06-21->2026-06-24 days=4 transport=打车 hotel=经济型酒店 prefs=['第一次来', '城市漫步']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 210, "expected_total_attractions": 420, "reported_total_attractions": 400, "meal_per_person_cost_sum": 722, "expected_total_meals": 1444, "reported_total_meals": 1724, "reported_total_transportation": 800}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 210, "expected_total_attractions": 420, "reported_total_attractions": 400, "meal_per_person_cost_sum": 722, "expected_total_meals": 1444, "reported_total_meals": 1724, "reported_total_transportation": 800}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": true, "meal_cost_scale_ok": false, "budget_relationship_ok": false, "expected_total_hotels": 600, "reported_total_hotels": 600, "expected_total_attractions": 420, "reported_total_attractions": 400, "meal_scale_eval": {"ok": false, "party_total": 2, "budget_level": "standard", "per_person_lunch_dinner_floor": 35, "breakfast_policy": "excluded_from_meal_cost_scale", "meal_count": 12, "checked_count": 8, "failure_count": 1, "failures": [{"date": "2026-06-21", "type": "lunch", "name": "后街捞化", "estimated_cost": 27, "min_expected_cost": 35}]}}}]`

### v3_standard200_realbudget_eval_000016
- request: 苏州 2026-06-06->2026-06-08 days=3 transport=公共交通 hotel=民宿 prefs=['海滨度假', '城市公园', '主题乐园', '清真']
- errors: `[{"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 135, "expected_total_attractions": 270, "reported_total_attractions": 270, "meal_per_person_cost_sum": 292, "expected_total_meals": 584, "reported_total_meals": 624, "reported_total_transportation": 200}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": true, "meal_cost_scale_ok": false, "budget_relationship_ok": false, "expected_total_hotels": 600, "reported_total_hotels": 600, "expected_total_attractions": 270, "reported_total_attractions": 270, "meal_scale_eval": {"ok": false, "party_total": 2, "budget_level": "limited", "per_person_lunch_dinner_floor": 25, "breakfast_policy": "excluded_from_meal_cost_scale", "meal_count": 9, "checked_count": 6, "failure_count": 3, "failures": [{"date": "2026-06-06", "type": "dinner", "name": "丝路回乡小吃店(西夏店)", "estimated_cost": 24, "min_expected_cost": 25}, {"date": "2026-06-07", "type": "lunch", "name": "魅之蘭兰州牛肉面(乐嘉汇店)", "estimated_cost": 21, "min_expected_cost": 25}, {"date": "2026-06-08", "type": "lunch", "name": "丝路回乡小吃店(西夏店)", "estimated_cost": 24, "min_expected_cost": 25}]}}}, {"stage": "rule", "type": "meal_cost_scale_too_low", "details": {"ok": false, "party_total": 2, "budget_level": "limited", "per_person_lunch_dinner_floor": 25, "breakfast_policy": "excluded_from_meal_cost_scale", "meal_count": 9, "checked_count": 6, "failure_count": 3, "failures": [{"date": "2026-06-06", "type": "dinner", "name": "丝路回乡小吃店(西夏店)", "estimated_cost": 24, "min_expected_cost": 25}, {"date": "2026-06-07", "type": "lunch", "name": "魅之蘭兰州牛肉面(乐嘉汇店)", "estimated_cost": 21, "min_expected_cost": 25}, {"date": "2026-06-08", "type": "lunch", "name": "丝路回乡小吃店(西夏店)", "estimated_cost": 24, "min_expected_cost": 25}]}}]`

### v3_standard200_realbudget_eval_000021
- request: 上海 2026-06-21->2026-06-22 days=2 transport=地铁+步行 hotel=经济型酒店 prefs=['老人友好', '休闲慢游', '城市漫步', '主题乐园']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 1614, "total": 1594, "diff": 20, "requested_budget": {"available": true, "amount": 1700, "scope": "total", "party_size": 2, "total": 1700, "source": "budget_constraint", "budget_level": "limited", "strictness": "soft"}, "per_person_day": 398.5, "budget_level": "limited", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "limited", "strictness": "soft", "amount": 1700, "target_min_ratio": 0.72, "target_max_ratio": 1.05, "target_min_total": 1200, "target_max_total": 1800, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 1, "party_total": 2, "room_count": 1, "priced_nights": 1, "expected_min_total_hotels": 250, "reported_total_hotels": 250, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 60, "expected_total_attractions": 120, "reported_total_attractions": 120, "meal_per_person_cost_sum": 596, "expected_total_meals": 1192, "reported_total_meals": 1164, "reported_total_transportation": 80}}]`

### v3_standard200_realbudget_eval_000009
- request: 苏州 2026-04-30->2026-05-04 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['亲子', '城市地标', '第一次来', '城市漫步']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "苏州博物馆西馆", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-05-01", "day_index": 1, "name": "苏州博物馆西馆"}, {"date": "2026-05-03", "day_index": 3, "name": "苏州博物馆西馆"}]}, {"name_key": "苏州丝绸博物馆", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-05-02", "day_index": 2, "name": "苏州丝绸博物馆"}, {"date": "2026-05-04", "day_index": 4, "name": "苏州丝绸博物馆"}]}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 495, "expected_total_attractions": 1980, "reported_total_attractions": 2160, "meal_per_person_cost_sum": 1271, "expected_total_meals": 5084, "reported_total_meals": 3640, "reported_total_transportation": 700}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 495, "expected_total_attractions": 1980, "reported_total_attractions": 2160, "meal_per_person_cost_sum": 1271, "expected_total_meals": 5084, "reported_total_meals": 3640, "reported_total_transportation": 700}}]`

### v3_standard200_realbudget_eval_000015
- request: 南京 2026-04-07->2026-04-08 days=2 transport=地铁+步行 hotel=经济型酒店 prefs=['亲子', '休闲慢游', '历史文化']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 125, "expected_total_attractions": 375, "reported_total_attractions": 405, "meal_per_person_cost_sum": 415, "expected_total_meals": 1245, "reported_total_meals": 1413, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 125, "expected_total_attractions": 375, "reported_total_attractions": 405, "meal_per_person_cost_sum": 415, "expected_total_meals": 1245, "reported_total_meals": 1413, "reported_total_transportation": 200}}, {"stage": "rule", "type": "budget_preference_mismatch", "details": {"part_sum": 2518, "total": 2518, "diff": 0, "requested_budget": {"available": true, "amount": 4300, "scope": "total", "party_size": 3, "total": 4300, "source": "budget_constraint", "budget_level": "standard", "strictness": "soft"}, "per_person_day": 419.67, "budget_level": "standard", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "standard", "strictness": "soft", "amount": 4300, "target_min_ratio": 0.6, "target_max_ratio": 1.05, "target_min_total": 2600, "target_max_total": 4500, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": true, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 1, "party_total": 3, "room_count": 2, "priced_nights": 1, "expected_min_total_hotels": 500, "reported_total_hotels": 500, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`
