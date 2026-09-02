# Rule Eval Report: sft_qwen25_7b_v3_1000_cp2_v1_standard200_w10

- records: 200
- generations: `training/outputs/eval/sft_qwen25_7b_v3_1000_cp2_v1_standard200_w10/generations.jsonl`
- records_path: `training/data/v3/eval/records.jsonl`

## Boolean Metrics

| Metric | Pass | Total | Rate |
| --- | ---: | ---: | ---: |
| accommodation_type_ok | 199 | 199 | 100.00% |
| attraction_budget_consistent | 31 | 199 | 15.58% |
| attraction_budget_party_relation_ok | 92 | 199 | 46.23% |
| attraction_count_ok | 192 | 199 | 96.48% |
| attraction_diversity_ok | 163 | 199 | 81.91% |
| attraction_grounding_ok | 192 | 199 | 96.48% |
| attraction_repeat_limit_ok | 163 | 199 | 81.91% |
| budget_arithmetic_consistent | 143 | 199 | 71.86% |
| budget_consistent | 143 | 199 | 71.86% |
| budget_level_aligned | 148 | 199 | 74.37% |
| budget_preference_aligned | 148 | 199 | 74.37% |
| budget_relationship_ok | 30 | 199 | 15.08% |
| budget_selection_ok | 121 | 199 | 60.80% |
| budget_user_constraint_ok | 196 | 199 | 98.49% |
| budget_within_user_budget | 198 | 199 | 99.50% |
| city_ok | 199 | 199 | 100.00% |
| date_range_ok | 199 | 199 | 100.00% |
| day_dates_ok | 199 | 199 | 100.00% |
| day_index_ok | 199 | 199 | 100.00% |
| days_len_ok | 199 | 199 | 100.00% |
| dpo_soft_pass | 92 | 199 | 46.23% |
| dpo_soft_recomputed_budget_pass | 74 | 199 | 37.19% |
| hard_pass | 181 | 199 | 90.95% |
| hotel_budget_covers_nights | 148 | 199 | 74.37% |
| hotel_budget_relation_ok | 150 | 199 | 75.38% |
| hotel_distance_placeholder_ok | 199 | 199 | 100.00% |
| hotel_grounding_ok | 199 | 199 | 100.00% |
| invalid_hotel_name_ok | 199 | 199 | 100.00% |
| json_extract_ok | 200 | 200 | 100.00% |
| legacy_hard_pass | 84 | 199 | 42.21% |
| location_object_ok | 199 | 199 | 100.00% |
| meal_budget_consistent | 1 | 199 | 0.50% |
| meal_complete | 199 | 199 | 100.00% |
| meal_cost_scale_ok | 95 | 199 | 47.74% |
| meal_diversity_ok | 153 | 199 | 76.88% |
| meal_grounding_ok | 195 | 199 | 97.99% |
| meal_lunch_dinner_same_day_ok | 183 | 199 | 91.96% |
| meal_repeat_limit_ok | 162 | 199 | 81.41% |
| meal_specific_ok | 199 | 199 | 100.00% |
| meal_valid_semantics_ok | 195 | 199 | 97.99% |
| middle_hotel_ok | 199 | 199 | 100.00% |
| recomputed_budget_fit_ok | 121 | 199 | 60.80% |
| recomputed_budget_hard_ok | 197 | 199 | 98.99% |
| recomputed_budget_level_aligned | 121 | 199 | 60.80% |
| recomputed_budget_preference_aligned | 121 | 199 | 60.80% |
| recomputed_budget_user_constraint_ok | 197 | 199 | 98.99% |
| recomputed_budget_within_user_budget | 197 | 199 | 98.99% |
| schema_ok | 199 | 200 | 99.50% |
| sft_budget_semantic_hard_pass | 27 | 199 | 13.57% |
| sft_hard_pass | 181 | 199 | 90.95% |
| sft_no_budget_sum_hard_pass | 181 | 199 | 90.95% |
| sft_strict_hard_pass | 0 | 199 | 0.00% |
| transportation_budget_nonnegative | 199 | 199 | 100.00% |
| weather_dates_ok | 199 | 199 | 100.00% |
| weather_match | 199 | 199 | 100.00% |

## Numeric Metrics

```json
{
  "attraction_diversity_unique_rate": {
    "avg": 0.9741,
    "p50": 1.0,
    "p90": 1.0
  },
  "attraction_grounding_rate": {
    "avg": 0.996,
    "p50": 1.0,
    "p90": 1.0
  },
  "hotel_grounding_rate": {
    "avg": 1.0,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_diversity_unique_rate": {
    "avg": 0.8368,
    "p50": 0.875,
    "p90": 1.0
  },
  "meal_food_pois_grounding_rate": {
    "avg": 0.9981,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_grounding_rate": {
    "avg": 0.9981,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_semantic_valid_rate": {
    "avg": 0.9981,
    "p50": 1.0,
    "p90": 1.0
  },
  "recomputed_budget_per_person_day": {
    "avg": 513.7791,
    "p50": 463.44,
    "p90": 754.75
  },
  "recomputed_budget_total": {
    "avg": 4943.5276,
    "p50": 4072.0,
    "p90": 8858.0
  }
}
```

## Failure Types

```json
{
  "meal_budget_inconsistent": 199,
  "budget_relationship_mismatch": 169,
  "attraction_budget_inconsistent": 168,
  "meal_cost_scale_too_low": 104,
  "budget_arithmetic_inconsistent": 56,
  "hotel_budget_underestimated": 51,
  "budget_preference_mismatch": 51,
  "meal_repeat_too_many": 37,
  "attraction_repeat_too_many": 36,
  "meal_same_day_lunch_dinner_repeat": 16,
  "too_many_attractions": 7,
  "meal_invalid_name": 4,
  "budget_hard_constraint_exceeded": 3,
  "schema": 1
}
```

## Failure Examples

### v3_standard200_eval_000001
- request: 桂林 2026-09-04->2026-09-06 days=3 transport=公共交通 hotel=高端酒店 prefs=['艺术', '美食', '第一次来', '历史文化']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "东西巷", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-09-04", "day_index": 0, "name": "东西巷"}, {"date": "2026-09-06", "day_index": 2, "name": "东西巷"}]}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "阿甘酒家", "count": 3, "max_allowed": 2, "occurrences": [{"date": "2026-09-04", "type": "lunch", "name": "阿甘酒家(解西店)"}, {"date": "2026-09-05", "type": "lunch", "name": "阿甘酒家(七星路店)"}, {"date": "2026-09-06", "type": "lunch", "name": "阿甘酒家(依仁店)"}]}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 2, "party_total": 2, "room_count": 1, "priced_nights": 2, "expected_min_total_hotels": 1500, "reported_total_hotels": 3000, "diff": 1500, "covers_nights": false}}]`

### v3_standard200_eval_000008
- request: 大理 2026-05-11->2026-05-13 days=3 transport=地铁+步行 hotel=舒适型酒店 prefs=['休闲慢游', '城市地标', '历史文化']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 75, "expected_total_attractions": 150, "reported_total_attractions": 300, "meal_per_person_cost_sum": 431, "expected_total_meals": 862, "reported_total_meals": 800, "reported_total_transportation": 300}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 75, "expected_total_attractions": 150, "reported_total_attractions": 300, "meal_per_person_cost_sum": 431, "expected_total_meals": 862, "reported_total_meals": 800, "reported_total_transportation": 300}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": false, "meal_cost_scale_ok": false, "budget_relationship_ok": false, "expected_total_hotels": 800, "reported_total_hotels": 800, "expected_total_attractions": 150, "reported_total_attractions": 300, "meal_scale_eval": {"ok": false, "party_total": 2, "budget_level": "standard", "per_person_lunch_dinner_floor": 35, "per_person_breakfast_floor": 14, "meal_count": 9, "checked_count": 9, "failure_count": 1, "failures": [{"date": "2026-05-12", "type": "breakfast", "name": "九孃豌豆粉店", "estimated_cost": 9, "min_expected_cost": 14}]}}}]`

### v3_standard200_eval_000005
- request: 广州 2026-07-06->2026-07-08 days=3 transport=地铁+步行 hotel=经济型酒店 prefs=['博物馆', '城市公园', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 270, "expected_total_attractions": 540, "reported_total_attractions": 450, "meal_per_person_cost_sum": 589, "expected_total_meals": 1178, "reported_total_meals": 550, "reported_total_transportation": 100}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 270, "expected_total_attractions": 540, "reported_total_attractions": 450, "meal_per_person_cost_sum": 589, "expected_total_meals": 1178, "reported_total_meals": 550, "reported_total_transportation": 100}}]`

### v3_standard200_eval_000007
- request: 成都 2026-05-11->2026-05-13 days=3 transport=地铁+步行 hotel=舒适型酒店 prefs=['美食', '城市公园', '休闲慢游']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 2600, "total": 2500, "diff": 100, "requested_budget": {"available": true, "amount": 3100, "scope": "total", "party_size": 2, "total": 3100, "source": "budget_constraint", "budget_level": "standard", "strictness": "hard"}, "per_person_day": 416.67, "budget_level": "standard", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "standard", "strictness": "hard", "amount": 3100, "target_min_ratio": 0.55, "target_max_ratio": 1.0, "target_min_total": 1700, "target_max_total": 3100, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 2, "room_count": 1, "priced_nights": 2, "expected_min_total_hotels": 900, "reported_total_hotels": 900, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 165, "expected_total_attractions": 330, "reported_total_attractions": 360, "meal_per_person_cost_sum": 712, "expected_total_meals": 1424, "reported_total_meals": 1140, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 165, "expected_total_attractions": 330, "reported_total_attractions": 360, "meal_per_person_cost_sum": 712, "expected_total_meals": 1424, "reported_total_meals": 1140, "reported_total_transportation": 200}}]`

### v3_standard200_eval_000000
- request: 昆明 2026-04-07->2026-04-09 days=3 transport=地铁+步行 hotel=高端酒店 prefs=['休闲慢游', '美食']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 2, "party_total": 2, "room_count": 1, "priced_nights": 2, "expected_min_total_hotels": 1500, "reported_total_hotels": 3000, "diff": 1500, "covers_nights": false}}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 6800, "total": 6900, "diff": -100, "requested_budget": {"available": true, "amount": 7200, "scope": "total", "party_size": 2, "total": 7200, "source": "budget_constraint", "budget_level": "premium", "strictness": "hard"}, "per_person_day": 1150.0, "budget_level": "premium", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "premium", "strictness": "hard", "amount": 7200, "target_min_ratio": 0.7, "target_max_ratio": 1.0, "target_min_total": 5000, "target_max_total": 7200, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 2, "room_count": 1, "priced_nights": 2, "expected_min_total_hotels": 1500, "reported_total_hotels": 3000, "diff": 1500, "covers_nights": false}, "hotel_budget_covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 50, "expected_total_attractions": 100, "reported_total_attractions": 120, "meal_per_person_cost_sum": 543, "expected_total_meals": 1086, "reported_total_meals": 2680, "reported_total_transportation": 1000}}]`

### v3_standard200_eval_000010
- request: 西安 2026-08-05->2026-08-08 days=4 transport=公共交通 hotel=经济型酒店 prefs=['城市公园', '美食']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 2, "room_count": 1, "priced_nights": 3, "expected_min_total_hotels": 750, "reported_total_hotels": 1500, "diff": 750, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 199, "expected_total_attractions": 398, "reported_total_attractions": 584, "meal_per_person_cost_sum": 685, "expected_total_meals": 1370, "reported_total_meals": 1544, "reported_total_transportation": 300}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 199, "expected_total_attractions": 398, "reported_total_attractions": 584, "meal_per_person_cost_sum": 685, "expected_total_meals": 1370, "reported_total_meals": 1544, "reported_total_transportation": 300}}]`

### v3_standard200_eval_000009
- request: 苏州 2026-04-30->2026-05-04 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['亲子', '城市地标', '第一次来', '城市漫步']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 4, "party_total": 4, "room_count": 2, "priced_nights": 4, "expected_min_total_hotels": 10000, "reported_total_hotels": 5000, "diff": -5000, "covers_nights": false}}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 11980, "total": 13980, "diff": -2000, "requested_budget": {"available": true, "amount": 21100, "scope": "total", "party_size": 4, "total": 21100, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "soft"}, "per_person_day": 699.0, "budget_level": "comfortable", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "soft", "amount": 21100, "target_min_ratio": 0.65, "target_max_ratio": 1.1, "target_min_total": 13700, "target_max_total": 23200, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 4, "party_total": 4, "room_count": 2, "priced_nights": 4, "expected_min_total_hotels": 10000, "reported_total_hotels": 5000, "diff": -5000, "covers_nights": false}, "hotel_budget_covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 140, "expected_total_attractions": 560, "reported_total_attractions": 1480, "meal_per_person_cost_sum": 1363, "expected_total_meals": 5452, "reported_total_meals": 4500, "reported_total_transportation": 1000}}]`

### v3_standard200_eval_000003
- request: 西安 2025-05-07->2025-05-11 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '历史文化', '购物商圈']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "西安博物院", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2025-05-07", "day_index": 0, "name": "西安博物院"}, {"date": "2025-05-11", "day_index": 4, "name": "西安博物院"}]}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 319, "expected_total_attractions": 957, "reported_total_attractions": 1143, "meal_per_person_cost_sum": 843, "expected_total_meals": 2529, "reported_total_meals": 3960, "reported_total_transportation": 1500}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 319, "expected_total_attractions": 957, "reported_total_attractions": 1143, "meal_per_person_cost_sum": 843, "expected_total_meals": 2529, "reported_total_meals": 3960, "reported_total_transportation": 1500}}]`

### v3_standard200_eval_000004
- request: 张家界 2026-05-11->2026-05-15 days=5 transport=地铁+步行 hotel=舒适型酒店 prefs=['亲子', '城市漫步', '历史文化']
- errors: `[{"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 400, "expected_total_attractions": 1600, "reported_total_attractions": 1600, "meal_per_person_cost_sum": 709, "expected_total_meals": 2836, "reported_total_meals": 2600, "reported_total_transportation": 1000}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": true, "meal_cost_scale_ok": false, "budget_relationship_ok": false, "expected_total_hotels": 3200, "reported_total_hotels": 3200, "expected_total_attractions": 1600, "reported_total_attractions": 1600, "meal_scale_eval": {"ok": false, "party_total": 4, "budget_level": "standard", "per_person_lunch_dinner_floor": 35, "per_person_breakfast_floor": 14, "meal_count": 15, "checked_count": 15, "failure_count": 1, "failures": [{"date": "2026-05-13", "type": "breakfast", "name": "家旺小吃(解放路店)", "estimated_cost": 13, "min_expected_cost": 14}]}}}, {"stage": "rule", "type": "meal_cost_scale_too_low", "details": {"ok": false, "party_total": 4, "budget_level": "standard", "per_person_lunch_dinner_floor": 35, "per_person_breakfast_floor": 14, "meal_count": 15, "checked_count": 15, "failure_count": 1, "failures": [{"date": "2026-05-13", "type": "breakfast", "name": "家旺小吃(解放路店)", "estimated_cost": 13, "min_expected_cost": 14}]}}]`

### v3_standard200_eval_000002
- request: 杭州 2026-05-01->2026-05-05 days=5 transport=公共交通 hotel=经济型酒店 prefs=['美食', '休闲慢游', '户外轻徒步', '城市漫步']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "泮芳春煎饺", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-05-01", "type": "breakfast", "name": "泮芳春煎饺(龙翔桥店)"}, {"date": "2026-05-02", "type": "breakfast", "name": "泮芳春煎饺(龙翔桥店)"}, {"date": "2026-05-03", "type": "breakfast", "name": "泮芳春煎饺(龙翔桥店)"}, {"date": "2026-05-04", "type": "breakfast", "name": "泮芳春煎饺(龙翔桥店)"}, {"date": "2026-05-05", "type": "breakfast", "name": "泮芳春煎饺(龙翔桥店)"}]}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 160, "expected_total_attractions": 160, "reported_total_attractions": 220, "meal_per_person_cost_sum": 897, "expected_total_meals": 897, "reported_total_meals": 430, "reported_total_transportation": 100}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 160, "expected_total_attractions": 160, "reported_total_attractions": 220, "meal_per_person_cost_sum": 897, "expected_total_meals": 897, "reported_total_meals": 430, "reported_total_transportation": 100}}]`

### v3_standard200_eval_000014
- request: 成都 2026-06-06->2026-06-07 days=2 transport=打车 hotel=经济型酒店 prefs=['小众展览', '美食', '城市地标']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 115, "expected_total_attractions": 460, "reported_total_attractions": 620, "meal_per_person_cost_sum": 445, "expected_total_meals": 1780, "reported_total_meals": 1232, "reported_total_transportation": 400}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 115, "expected_total_attractions": 460, "reported_total_attractions": 620, "meal_per_person_cost_sum": 445, "expected_total_meals": 1780, "reported_total_meals": 1232, "reported_total_transportation": 400}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": false, "meal_cost_scale_ok": true, "budget_relationship_ok": false, "expected_total_hotels": 500, "reported_total_hotels": 500, "expected_total_attractions": 460, "reported_total_attractions": 620, "meal_scale_eval": {"ok": true, "party_total": 4, "budget_level": "limited", "per_person_lunch_dinner_floor": 25, "per_person_breakfast_floor": 10, "meal_count": 6, "checked_count": 4, "failure_count": 0, "failures": []}}}]`

### v3_standard200_eval_000015
- request: 南京 2026-04-07->2026-04-08 days=2 transport=地铁+步行 hotel=经济型酒店 prefs=['亲子', '休闲慢游', '历史文化']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 45, "expected_total_attractions": 135, "reported_total_attractions": 210, "meal_per_person_cost_sum": 388, "expected_total_meals": 1164, "reported_total_meals": 1575, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 45, "expected_total_attractions": 135, "reported_total_attractions": 210, "meal_per_person_cost_sum": 388, "expected_total_meals": 1164, "reported_total_meals": 1575, "reported_total_transportation": 200}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": false, "meal_cost_scale_ok": false, "budget_relationship_ok": false, "expected_total_hotels": 500, "reported_total_hotels": 500, "expected_total_attractions": 135, "reported_total_attractions": 210, "meal_scale_eval": {"ok": false, "party_total": 3, "budget_level": "standard", "per_person_lunch_dinner_floor": 35, "per_person_breakfast_floor": 14, "meal_count": 6, "checked_count": 6, "failure_count": 1, "failures": [{"date": "2026-04-08", "type": "lunch", "name": "小潘记鸭血粉丝汤", "estimated_cost": 34, "min_expected_cost": 35}]}}}]`

### v3_standard200_eval_000013
- request: 武汉 2026-05-09->2026-05-11 days=3 transport=公共交通 hotel=舒适型酒店 prefs=['亲子', '老人友好', '第一次来', '城市公园']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 2, "party_total": 6, "room_count": 3, "priced_nights": 2, "expected_min_total_hotels": 2400, "reported_total_hotels": 1600, "diff": -800, "covers_nights": false}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 6, "hotel_room_count": 3, "attraction_ticket_sum": 146, "expected_total_attractions": 876, "reported_total_attractions": 876, "meal_per_person_cost_sum": 488, "expected_total_meals": 2928, "reported_total_meals": 4680, "reported_total_transportation": 600}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": false, "attraction_budget_party_relation_ok": true, "meal_cost_scale_ok": false, "budget_relationship_ok": false, "expected_total_hotels": 2400, "reported_total_hotels": 1600, "expected_total_attractions": 876, "reported_total_attractions": 876, "meal_scale_eval": {"ok": false, "party_total": 6, "budget_level": "standard", "per_person_lunch_dinner_floor": 35, "per_person_breakfast_floor": 14, "meal_count": 9, "checked_count": 9, "failure_count": 1, "failures": [{"date": "2026-05-09", "type": "breakfast", "name": "矮子馅饼(大成路店)", "estimated_cost": 13, "min_expected_cost": 14}]}}}]`

### v3_standard200_eval_000016
- request: 苏州 2026-06-06->2026-06-08 days=3 transport=公共交通 hotel=民宿 prefs=['海滨度假', '城市公园', '主题乐园', '清真']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 215, "expected_total_attractions": 430, "reported_total_attractions": 390, "meal_per_person_cost_sum": 372, "expected_total_meals": 744, "reported_total_meals": 684, "reported_total_transportation": 100}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 215, "expected_total_attractions": 430, "reported_total_attractions": 390, "meal_per_person_cost_sum": 372, "expected_total_meals": 744, "reported_total_meals": 684, "reported_total_transportation": 100}}]`

### v3_standard200_eval_000017
- request: 苏州 2026-05-09->2026-05-11 days=3 transport=地铁+步行 hotel=亲子酒店 prefs=['亲子', '历史文化', '休闲慢游', '户外轻徒步']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 2, "party_total": 3, "room_count": 2, "priced_nights": 2, "expected_min_total_hotels": 5000, "reported_total_hotels": 2500, "diff": -2500, "covers_nights": false}}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 5800, "total": 7800, "diff": -2000, "requested_budget": {"available": true, "amount": 9900, "scope": "total", "party_size": 3, "total": 9900, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "soft"}, "per_person_day": 866.67, "budget_level": "comfortable", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "soft", "amount": 9900, "target_min_ratio": 0.65, "target_max_ratio": 1.1, "target_min_total": 6400, "target_max_total": 10900, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 3, "room_count": 2, "priced_nights": 2, "expected_min_total_hotels": 5000, "reported_total_hotels": 2500, "diff": -2500, "covers_nights": false}, "hotel_budget_covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 195, "expected_total_attractions": 585, "reported_total_attractions": 1135, "meal_per_person_cost_sum": 373, "expected_total_meals": 1119, "reported_total_meals": 1965, "reported_total_transportation": 200}}]`

### v3_standard200_eval_000021
- request: 上海 2026-06-21->2026-06-22 days=2 transport=地铁+步行 hotel=经济型酒店 prefs=['老人友好', '休闲慢游', '城市漫步', '主题乐园']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 100, "expected_total_attractions": 200, "reported_total_attractions": 220, "meal_per_person_cost_sum": 518, "expected_total_meals": 1036, "reported_total_meals": 690, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 100, "expected_total_attractions": 200, "reported_total_attractions": 220, "meal_per_person_cost_sum": 518, "expected_total_meals": 1036, "reported_total_meals": 690, "reported_total_transportation": 200}}]`

### v3_standard200_eval_000006
- request: 南京 2026-07-06->2026-07-09 days=4 transport=打车 hotel=经济型酒店 prefs=['老人友好', '美食', '城市公园', '休闲慢游']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 255, "expected_total_attractions": 765, "reported_total_attractions": 1050, "meal_per_person_cost_sum": 795, "expected_total_meals": 2385, "reported_total_meals": 1650, "reported_total_transportation": 600}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 255, "expected_total_attractions": 765, "reported_total_attractions": 1050, "meal_per_person_cost_sum": 795, "expected_total_meals": 2385, "reported_total_meals": 1650, "reported_total_transportation": 600}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": false, "meal_cost_scale_ok": true, "budget_relationship_ok": false, "expected_total_hotels": 1500, "reported_total_hotels": 1500, "expected_total_attractions": 765, "reported_total_attractions": 1050, "meal_scale_eval": {"ok": true, "party_total": 3, "budget_level": "limited", "per_person_lunch_dinner_floor": 25, "per_person_breakfast_floor": 10, "meal_count": 12, "checked_count": 12, "failure_count": 0, "failures": []}}}]`

### v3_standard200_eval_000018
- request: 天津 2026-07-06->2026-07-07 days=2 transport=打车 hotel=舒适型酒店 prefs=['老人友好', '夜市夜景', '艺术', '第一次来']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 1, "party_total": 3, "room_count": 2, "priced_nights": 1, "expected_min_total_hotels": 800, "reported_total_hotels": 400, "diff": -400, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 130, "expected_total_attractions": 390, "reported_total_attractions": 450, "meal_per_person_cost_sum": 380, "expected_total_meals": 1140, "reported_total_meals": 675, "reported_total_transportation": 400}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 130, "expected_total_attractions": 390, "reported_total_attractions": 450, "meal_per_person_cost_sum": 380, "expected_total_meals": 1140, "reported_total_meals": 675, "reported_total_transportation": 400}}]`

### v3_standard200_eval_000020
- request: 杭州 2026-06-21->2026-06-24 days=4 transport=地铁+步行 hotel=高端酒店 prefs=['历史文化', '海滨度假']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "灵隐寺", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-06-22", "day_index": 1, "name": "灵隐寺"}, {"date": "2026-06-24", "day_index": 3, "name": "灵隐寺"}]}]}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 5940, "total": 6040, "diff": -100, "requested_budget": {"available": true, "amount": 6900, "scope": "total", "party_size": 2, "total": 6900, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "soft"}, "per_person_day": 755.0, "budget_level": "comfortable", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "soft", "amount": 6900, "target_min_ratio": 0.65, "target_max_ratio": 1.1, "target_min_total": 4500, "target_max_total": 7600, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 2, "room_count": 1, "priced_nights": 3, "expected_min_total_hotels": 4200, "reported_total_hotels": 4200, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 110, "expected_total_attractions": 220, "reported_total_attractions": 120, "meal_per_person_cost_sum": 659, "expected_total_meals": 1318, "reported_total_meals": 1320, "reported_total_transportation": 300}}]`

### v3_standard200_eval_000022
- request: 桂林 2026-04-07->2026-04-10 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['亲子', '自然风光', '休闲慢游']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 295, "expected_total_attractions": 885, "reported_total_attractions": 1170, "meal_per_person_cost_sum": 577, "expected_total_meals": 1731, "reported_total_meals": 1482, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 295, "expected_total_attractions": 885, "reported_total_attractions": 1170, "meal_per_person_cost_sum": 577, "expected_total_meals": 1731, "reported_total_meals": 1482, "reported_total_transportation": 200}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": false, "meal_cost_scale_ok": true, "budget_relationship_ok": false, "expected_total_hotels": 1200, "reported_total_hotels": 1200, "expected_total_attractions": 885, "reported_total_attractions": 1170, "meal_scale_eval": {"ok": true, "party_total": 3, "budget_level": "limited", "per_person_lunch_dinner_floor": 25, "per_person_breakfast_floor": 10, "meal_count": 12, "checked_count": 12, "failure_count": 0, "failures": []}}}]`
