# Rule Eval Report: sft_qwen25_7b_v3_1000_cp2_v2a_current_standard_w10

- records: 200
- generations: `training/outputs/eval/sft_qwen25_7b_v3_1000_cp2_v2a_current_standard_w10/generations.jsonl`
- records_path: `training/data/v3/eval/records.jsonl`

## Boolean Metrics

| Metric | Pass | Total | Rate |
| --- | ---: | ---: | ---: |
| accommodation_type_ok | 199 | 199 | 100.00% |
| attraction_budget_consistent | 52 | 199 | 26.13% |
| attraction_budget_party_relation_ok | 162 | 199 | 81.41% |
| attraction_count_ok | 198 | 199 | 99.50% |
| attraction_diversity_ok | 181 | 199 | 90.95% |
| attraction_grounding_ok | 196 | 199 | 98.49% |
| attraction_repeat_limit_ok | 181 | 199 | 90.95% |
| budget_arithmetic_consistent | 157 | 199 | 78.89% |
| budget_consistent | 157 | 199 | 78.89% |
| budget_level_aligned | 147 | 199 | 73.87% |
| budget_preference_aligned | 147 | 199 | 73.87% |
| budget_relationship_ok | 65 | 199 | 32.66% |
| budget_selection_ok | 145 | 199 | 72.86% |
| budget_user_constraint_ok | 197 | 199 | 98.99% |
| budget_within_user_budget | 198 | 199 | 99.50% |
| city_ok | 199 | 199 | 100.00% |
| date_range_ok | 199 | 199 | 100.00% |
| day_dates_ok | 199 | 199 | 100.00% |
| day_index_ok | 199 | 199 | 100.00% |
| days_len_ok | 199 | 199 | 100.00% |
| dpo_soft_pass | 113 | 199 | 56.78% |
| dpo_soft_recomputed_budget_pass | 110 | 199 | 55.28% |
| hard_pass | 191 | 199 | 95.98% |
| hotel_budget_covers_nights | 159 | 199 | 79.90% |
| hotel_budget_relation_ok | 161 | 199 | 80.90% |
| hotel_distance_placeholder_ok | 199 | 199 | 100.00% |
| hotel_grounding_ok | 199 | 199 | 100.00% |
| invalid_hotel_name_ok | 199 | 199 | 100.00% |
| json_extract_ok | 200 | 200 | 100.00% |
| legacy_hard_pass | 101 | 199 | 50.75% |
| location_object_ok | 199 | 199 | 100.00% |
| meal_budget_consistent | 0 | 199 | 0.00% |
| meal_complete | 199 | 199 | 100.00% |
| meal_cost_scale_ok | 98 | 199 | 49.25% |
| meal_diversity_ok | 168 | 199 | 84.42% |
| meal_grounding_ok | 195 | 199 | 97.99% |
| meal_lunch_dinner_same_day_ok | 187 | 199 | 93.97% |
| meal_repeat_limit_ok | 179 | 199 | 89.95% |
| meal_specific_ok | 199 | 199 | 100.00% |
| meal_valid_semantics_ok | 195 | 199 | 97.99% |
| middle_hotel_ok | 199 | 199 | 100.00% |
| recomputed_budget_fit_ok | 145 | 199 | 72.86% |
| recomputed_budget_hard_ok | 195 | 199 | 97.99% |
| recomputed_budget_level_aligned | 145 | 199 | 72.86% |
| recomputed_budget_preference_aligned | 145 | 199 | 72.86% |
| recomputed_budget_user_constraint_ok | 195 | 199 | 97.99% |
| recomputed_budget_within_user_budget | 196 | 199 | 98.49% |
| schema_ok | 199 | 200 | 99.50% |
| sft_budget_semantic_hard_pass | 61 | 199 | 30.65% |
| sft_hard_pass | 191 | 199 | 95.98% |
| sft_no_budget_sum_hard_pass | 191 | 199 | 95.98% |
| sft_strict_hard_pass | 0 | 199 | 0.00% |
| transportation_budget_nonnegative | 199 | 199 | 100.00% |
| weather_dates_ok | 199 | 199 | 100.00% |
| weather_match | 199 | 199 | 100.00% |

## Numeric Metrics

```json
{
  "attraction_diversity_unique_rate": {
    "avg": 0.9893,
    "p50": 1.0,
    "p90": 1.0
  },
  "attraction_grounding_rate": {
    "avg": 0.9979,
    "p50": 1.0,
    "p90": 1.0
  },
  "hotel_grounding_rate": {
    "avg": 1.0,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_diversity_unique_rate": {
    "avg": 0.8914,
    "p50": 0.9333,
    "p90": 1.0
  },
  "meal_food_pois_grounding_rate": {
    "avg": 0.9977,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_grounding_rate": {
    "avg": 0.9977,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_semantic_valid_rate": {
    "avg": 0.9977,
    "p50": 1.0,
    "p90": 1.0
  },
  "recomputed_budget_per_person_day": {
    "avg": 533.8511,
    "p50": 473.33,
    "p90": 814.89
  },
  "recomputed_budget_total": {
    "avg": 5165.5678,
    "p50": 4311.0,
    "p90": 9694.0
  }
}
```

## Failure Types

```json
{
  "meal_budget_inconsistent": 199,
  "attraction_budget_inconsistent": 147,
  "budget_relationship_mismatch": 134,
  "meal_cost_scale_too_low": 101,
  "budget_preference_mismatch": 52,
  "budget_arithmetic_inconsistent": 42,
  "hotel_budget_underestimated": 40,
  "meal_repeat_too_many": 20,
  "attraction_repeat_too_many": 18,
  "meal_same_day_lunch_dinner_repeat": 12,
  "meal_invalid_name": 4,
  "budget_hard_constraint_exceeded": 2,
  "schema": 1,
  "too_many_attractions": 1
}
```

## Failure Examples

### v3_standard200_eval_000008
- request: 大理 2026-05-11->2026-05-13 days=3 transport=地铁+步行 hotel=舒适型酒店 prefs=['休闲慢游', '城市地标', '历史文化']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 115, "expected_total_attractions": 230, "reported_total_attractions": 260, "meal_per_person_cost_sum": 433, "expected_total_meals": 866, "reported_total_meals": 702, "reported_total_transportation": 100}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 115, "expected_total_attractions": 230, "reported_total_attractions": 260, "meal_per_person_cost_sum": 433, "expected_total_meals": 866, "reported_total_meals": 702, "reported_total_transportation": 100}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": true, "meal_cost_scale_ok": false, "budget_relationship_ok": false, "expected_total_hotels": 800, "reported_total_hotels": 800, "expected_total_attractions": 230, "reported_total_attractions": 260, "meal_scale_eval": {"ok": false, "party_total": 2, "budget_level": "standard", "per_person_lunch_dinner_floor": 35, "per_person_breakfast_floor": 14, "meal_count": 9, "checked_count": 9, "failure_count": 1, "failures": [{"date": "2026-05-12", "type": "breakfast", "name": "九孃豌豆粉店", "estimated_cost": 9, "min_expected_cost": 14}]}}}]`

### v3_standard200_eval_000000
- request: 昆明 2026-04-07->2026-04-09 days=3 transport=地铁+步行 hotel=高端酒店 prefs=['休闲慢游', '美食']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 50, "expected_total_attractions": 100, "reported_total_attractions": 120, "meal_per_person_cost_sum": 485, "expected_total_meals": 970, "reported_total_meals": 1134, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 50, "expected_total_attractions": 100, "reported_total_attractions": 120, "meal_per_person_cost_sum": 485, "expected_total_meals": 970, "reported_total_meals": 1134, "reported_total_transportation": 200}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": true, "meal_cost_scale_ok": false, "budget_relationship_ok": false, "expected_total_hotels": 1500, "reported_total_hotels": 1500, "expected_total_attractions": 100, "reported_total_attractions": 120, "meal_scale_eval": {"ok": false, "party_total": 2, "budget_level": "premium", "per_person_lunch_dinner_floor": 70, "per_person_breakfast_floor": 28, "meal_count": 9, "checked_count": 6, "failure_count": 2, "failures": [{"date": "2026-04-07", "type": "lunch", "name": "湖景坊·经典云南菜·过桥米线(海埂公园店)", "estimated_cost": 57, "min_expected_cost": 70}, {"date": "2026-04-09", "type": "lunch", "name": "芸南道过桥米线(昆明老街旗舰店)", "estimated_cost": 50, "min_expected_cost": 70}]}}}]`

### v3_standard200_eval_000001
- request: 桂林 2026-09-04->2026-09-06 days=3 transport=公共交通 hotel=高端酒店 prefs=['艺术', '美食', '第一次来', '历史文化']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 356, "expected_total_attractions": 712, "reported_total_attractions": 671, "meal_per_person_cost_sum": 545, "expected_total_meals": 1090, "reported_total_meals": 1008, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 356, "expected_total_attractions": 712, "reported_total_attractions": 671, "meal_per_person_cost_sum": 545, "expected_total_meals": 1090, "reported_total_meals": 1008, "reported_total_transportation": 200}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": true, "meal_cost_scale_ok": false, "budget_relationship_ok": false, "expected_total_hotels": 2400, "reported_total_hotels": 2400, "expected_total_attractions": 712, "reported_total_attractions": 671, "meal_scale_eval": {"ok": false, "party_total": 2, "budget_level": "comfortable", "per_person_lunch_dinner_floor": 50, "per_person_breakfast_floor": 20, "meal_count": 9, "checked_count": 9, "failure_count": 2, "failures": [{"date": "2026-09-05", "type": "breakfast", "name": "海天肠粉", "estimated_cost": 14, "min_expected_cost": 20}, {"date": "2026-09-06", "type": "breakfast", "name": "老东江米粉(施家园路店)", "estimated_cost": 10, "min_expected_cost": 20}]}}}]`

### v3_standard200_eval_000007
- request: 成都 2026-05-11->2026-05-13 days=3 transport=地铁+步行 hotel=舒适型酒店 prefs=['美食', '城市公园', '休闲慢游']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 165, "expected_total_attractions": 330, "reported_total_attractions": 320, "meal_per_person_cost_sum": 831, "expected_total_meals": 1662, "reported_total_meals": 1080, "reported_total_transportation": 100}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 165, "expected_total_attractions": 330, "reported_total_attractions": 320, "meal_per_person_cost_sum": 831, "expected_total_meals": 1662, "reported_total_meals": 1080, "reported_total_transportation": 100}}]`

### v3_standard200_eval_000005
- request: 广州 2026-07-06->2026-07-08 days=3 transport=地铁+步行 hotel=经济型酒店 prefs=['博物馆', '城市公园', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 30, "expected_total_attractions": 60, "reported_total_attractions": 60, "meal_per_person_cost_sum": 519, "expected_total_meals": 1038, "reported_total_meals": 806, "reported_total_transportation": 100}}]`

### v3_standard200_eval_000010
- request: 西安 2026-08-05->2026-08-08 days=4 transport=公共交通 hotel=经济型酒店 prefs=['城市公园', '美食']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 319, "expected_total_attractions": 638, "reported_total_attractions": 568, "meal_per_person_cost_sum": 603, "expected_total_meals": 1206, "reported_total_meals": 1034, "reported_total_transportation": 100}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 319, "expected_total_attractions": 638, "reported_total_attractions": 568, "meal_per_person_cost_sum": 603, "expected_total_meals": 1206, "reported_total_meals": 1034, "reported_total_transportation": 100}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": true, "meal_cost_scale_ok": false, "budget_relationship_ok": false, "expected_total_hotels": 750, "reported_total_hotels": 750, "expected_total_attractions": 638, "reported_total_attractions": 568, "meal_scale_eval": {"ok": false, "party_total": 2, "budget_level": "standard", "per_person_lunch_dinner_floor": 35, "per_person_breakfast_floor": 14, "meal_count": 12, "checked_count": 12, "failure_count": 1, "failures": [{"date": "2026-08-05", "type": "dinner", "name": "马洪小炒泡馍馆", "estimated_cost": 31, "min_expected_cost": 35}]}}}]`

### v3_standard200_eval_000004
- request: 张家界 2026-05-11->2026-05-15 days=5 transport=地铁+步行 hotel=舒适型酒店 prefs=['亲子', '城市漫步', '历史文化']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 301, "expected_total_attractions": 1204, "reported_total_attractions": 1044, "meal_per_person_cost_sum": 737, "expected_total_meals": 2948, "reported_total_meals": 1680, "reported_total_transportation": 580}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 301, "expected_total_attractions": 1204, "reported_total_attractions": 1044, "meal_per_person_cost_sum": 737, "expected_total_meals": 2948, "reported_total_meals": 1680, "reported_total_transportation": 580}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": true, "meal_cost_scale_ok": false, "budget_relationship_ok": false, "expected_total_hotels": 3200, "reported_total_hotels": 3200, "expected_total_attractions": 1204, "reported_total_attractions": 1044, "meal_scale_eval": {"ok": false, "party_total": 4, "budget_level": "standard", "per_person_lunch_dinner_floor": 35, "per_person_breakfast_floor": 14, "meal_count": 15, "checked_count": 15, "failure_count": 1, "failures": [{"date": "2026-05-14", "type": "breakfast", "name": "家旺小吃(解放路店)", "estimated_cost": 13, "min_expected_cost": 14}]}}}]`

### v3_standard200_eval_000002
- request: 杭州 2026-05-01->2026-05-05 days=5 transport=公共交通 hotel=经济型酒店 prefs=['美食', '休闲慢游', '户外轻徒步', '城市漫步']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "泮芳春煎饺", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-05-01", "type": "breakfast", "name": "泮芳春煎饺(龙翔桥店)"}, {"date": "2026-05-03", "type": "breakfast", "name": "泮芳春煎饺(龙翔桥店)"}, {"date": "2026-05-04", "type": "breakfast", "name": "泮芳春煎饺(龙翔桥店)"}, {"date": "2026-05-05", "type": "breakfast", "name": "泮芳春煎饺(龙翔桥店)"}]}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 160, "expected_total_attractions": 160, "reported_total_attractions": 180, "meal_per_person_cost_sum": 896, "expected_total_meals": 896, "reported_total_meals": 685, "reported_total_transportation": 100}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 160, "expected_total_attractions": 160, "reported_total_attractions": 180, "meal_per_person_cost_sum": 896, "expected_total_meals": 896, "reported_total_meals": 685, "reported_total_transportation": 100}}]`

### v3_standard200_eval_000015
- request: 南京 2026-04-07->2026-04-08 days=2 transport=地铁+步行 hotel=经济型酒店 prefs=['亲子', '休闲慢游', '历史文化']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 1, "party_total": 3, "room_count": 2, "priced_nights": 1, "expected_min_total_hotels": 500, "reported_total_hotels": 250, "diff": -250, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 65, "expected_total_attractions": 195, "reported_total_attractions": 180, "meal_per_person_cost_sum": 651, "expected_total_meals": 1953, "reported_total_meals": 1260, "reported_total_transportation": 550}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 65, "expected_total_attractions": 195, "reported_total_attractions": 180, "meal_per_person_cost_sum": 651, "expected_total_meals": 1953, "reported_total_meals": 1260, "reported_total_transportation": 550}}]`

### v3_standard200_eval_000009
- request: 苏州 2026-04-30->2026-05-04 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['亲子', '城市地标', '第一次来', '城市漫步']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 14700, "total": 13700, "diff": 1000, "requested_budget": {"available": true, "amount": 21100, "scope": "total", "party_size": 4, "total": 21100, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "soft"}, "per_person_day": 685.0, "budget_level": "comfortable", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "soft", "amount": 21100, "target_min_ratio": 0.65, "target_max_ratio": 1.1, "target_min_total": 13700, "target_max_total": 23200, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 4, "party_total": 4, "room_count": 2, "priced_nights": 4, "expected_min_total_hotels": 10000, "reported_total_hotels": 10000, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 220, "expected_total_attractions": 880, "reported_total_attractions": 880, "meal_per_person_cost_sum": 780, "expected_total_meals": 3120, "reported_total_meals": 2820, "reported_total_transportation": 1000}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": true, "meal_cost_scale_ok": false, "budget_relationship_ok": false, "expected_total_hotels": 10000, "reported_total_hotels": 10000, "expected_total_attractions": 880, "reported_total_attractions": 880, "meal_scale_eval": {"ok": false, "party_total": 4, "budget_level": "comfortable", "per_person_lunch_dinner_floor": 50, "per_person_breakfast_floor": 20, "meal_count": 15, "checked_count": 15, "failure_count": 3, "failures": [{"date": "2026-05-02", "type": "breakfast", "name": "西园寺素食-面馆", "estimated_cost": 16, "min_expected_cost": 20}, {"date": "2026-05-03", "type": "breakfast", "name": "秋娟馄饨店", "estimated_cost": 14, "min_expected_cost": 20}, {"date": "2026-05-03", "type": "dinner", "name": "万福兴(东中市总店)", "estimated_cost": 20, "min_expected_cost": 50}]}}}]`

### v3_standard200_eval_000003
- request: 西安 2025-05-07->2025-05-11 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '历史文化', '购物商圈']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 7100, "total": 6000, "diff": 1100, "requested_budget": {"available": true, "amount": 11000, "scope": "total", "party_size": 3, "total": 11000, "source": "budget_constraint", "budget_level": "standard", "strictness": "soft"}, "per_person_day": 400.0, "budget_level": "standard", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "standard", "strictness": "soft", "amount": 11000, "target_min_ratio": 0.55, "target_max_ratio": 1.1, "target_min_total": 6100, "target_max_total": 12100, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 4, "party_total": 3, "room_count": 2, "priced_nights": 4, "expected_min_total_hotels": 3600, "reported_total_hotels": 3600, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 419, "expected_total_attractions": 1257, "reported_total_attractions": 1179, "meal_per_person_cost_sum": 759, "expected_total_meals": 2277, "reported_total_meals": 1921, "reported_total_transportation": 400}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 419, "expected_total_attractions": 1257, "reported_total_attractions": 1179, "meal_per_person_cost_sum": 759, "expected_total_meals": 2277, "reported_total_meals": 1921, "reported_total_transportation": 400}}]`

### v3_standard200_eval_000014
- request: 成都 2026-06-06->2026-06-07 days=2 transport=打车 hotel=经济型酒店 prefs=['小众展览', '美食', '城市地标']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 1, "party_total": 4, "room_count": 2, "priced_nights": 1, "expected_min_total_hotels": 500, "reported_total_hotels": 250, "diff": -250, "covers_nights": false}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 115, "expected_total_attractions": 460, "reported_total_attractions": 460, "meal_per_person_cost_sum": 476, "expected_total_meals": 1904, "reported_total_meals": 1168, "reported_total_transportation": 400}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": false, "attraction_budget_party_relation_ok": true, "meal_cost_scale_ok": true, "budget_relationship_ok": false, "expected_total_hotels": 500, "reported_total_hotels": 250, "expected_total_attractions": 460, "reported_total_attractions": 460, "meal_scale_eval": {"ok": true, "party_total": 4, "budget_level": "limited", "per_person_lunch_dinner_floor": 25, "per_person_breakfast_floor": 10, "meal_count": 6, "checked_count": 6, "failure_count": 0, "failures": []}}}]`

### v3_standard200_eval_000013
- request: 武汉 2026-05-09->2026-05-11 days=3 transport=公共交通 hotel=舒适型酒店 prefs=['亲子', '老人友好', '第一次来', '城市公园']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 6, "hotel_room_count": 3, "attraction_ticket_sum": 83, "expected_total_attractions": 498, "reported_total_attractions": 558, "meal_per_person_cost_sum": 663, "expected_total_meals": 3978, "reported_total_meals": 3258, "reported_total_transportation": 400}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 6, "hotel_room_count": 3, "attraction_ticket_sum": 83, "expected_total_attractions": 498, "reported_total_attractions": 558, "meal_per_person_cost_sum": 663, "expected_total_meals": 3978, "reported_total_meals": 3258, "reported_total_transportation": 400}}]`

### v3_standard200_eval_000016
- request: 苏州 2026-06-06->2026-06-08 days=3 transport=公共交通 hotel=民宿 prefs=['海滨度假', '城市公园', '主题乐园', '清真']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 140, "expected_total_attractions": 280, "reported_total_attractions": 250, "meal_per_person_cost_sum": 270, "expected_total_meals": 540, "reported_total_meals": 440, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 140, "expected_total_attractions": 280, "reported_total_attractions": 250, "meal_per_person_cost_sum": 270, "expected_total_meals": 540, "reported_total_meals": 440, "reported_total_transportation": 200}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": true, "meal_cost_scale_ok": false, "budget_relationship_ok": false, "expected_total_hotels": 600, "reported_total_hotels": 600, "expected_total_attractions": 280, "reported_total_attractions": 250, "meal_scale_eval": {"ok": false, "party_total": 2, "budget_level": "limited", "per_person_lunch_dinner_floor": 25, "per_person_breakfast_floor": 10, "meal_count": 9, "checked_count": 6, "failure_count": 2, "failures": [{"date": "2026-06-06", "type": "lunch", "name": "丝路回乡小吃店(西夏店)", "estimated_cost": 24, "min_expected_cost": 25}, {"date": "2026-06-08", "type": "dinner", "name": "丝路回乡小吃店(西夏店)", "estimated_cost": 24, "min_expected_cost": 25}]}}}]`

### v3_standard200_eval_000006
- request: 南京 2026-07-06->2026-07-09 days=4 transport=打车 hotel=经济型酒店 prefs=['老人友好', '美食', '城市公园', '休闲慢游']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 100, "expected_total_attractions": 300, "reported_total_attractions": 240, "meal_per_person_cost_sum": 666, "expected_total_meals": 1998, "reported_total_meals": 1836, "reported_total_transportation": 424}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 100, "expected_total_attractions": 300, "reported_total_attractions": 240, "meal_per_person_cost_sum": 666, "expected_total_meals": 1998, "reported_total_meals": 1836, "reported_total_transportation": 424}}, {"stage": "rule", "type": "budget_preference_mismatch", "details": {"part_sum": 4000, "total": 4000, "diff": 0, "requested_budget": {"available": true, "amount": 6700, "scope": "total", "party_size": 3, "total": 6700, "source": "budget_constraint", "budget_level": "limited", "strictness": "soft"}, "per_person_day": 333.33, "budget_level": "limited", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "limited", "strictness": "soft", "amount": 6700, "target_min_ratio": 0.72, "target_max_ratio": 1.05, "target_min_total": 4800, "target_max_total": 7000, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": true, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 3, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 1500, "reported_total_hotels": 1500, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_standard200_eval_000017
- request: 苏州 2026-05-09->2026-05-11 days=3 transport=地铁+步行 hotel=亲子酒店 prefs=['亲子', '历史文化', '休闲慢游', '户外轻徒步']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 140, "expected_total_attractions": 420, "reported_total_attractions": 390, "meal_per_person_cost_sum": 426, "expected_total_meals": 1278, "reported_total_meals": 1326, "reported_total_transportation": 300}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 140, "expected_total_attractions": 420, "reported_total_attractions": 390, "meal_per_person_cost_sum": 426, "expected_total_meals": 1278, "reported_total_meals": 1326, "reported_total_transportation": 300}}]`

### v3_standard200_eval_000021
- request: 上海 2026-06-21->2026-06-22 days=2 transport=地铁+步行 hotel=经济型酒店 prefs=['老人友好', '休闲慢游', '城市漫步', '主题乐园']
- errors: `[{"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 100, "expected_total_attractions": 200, "reported_total_attractions": 200, "meal_per_person_cost_sum": 304, "expected_total_meals": 608, "reported_total_meals": 574, "reported_total_transportation": 200}}]`

### v3_standard200_eval_000018
- request: 天津 2026-07-06->2026-07-07 days=2 transport=打车 hotel=舒适型酒店 prefs=['老人友好', '夜市夜景', '艺术', '第一次来']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 1, "party_total": 3, "room_count": 2, "priced_nights": 1, "expected_min_total_hotels": 800, "reported_total_hotels": 400, "diff": -400, "covers_nights": false}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 80, "expected_total_attractions": 240, "reported_total_attractions": 240, "meal_per_person_cost_sum": 326, "expected_total_meals": 978, "reported_total_meals": 807, "reported_total_transportation": 753}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": false, "attraction_budget_party_relation_ok": true, "meal_cost_scale_ok": true, "budget_relationship_ok": false, "expected_total_hotels": 800, "reported_total_hotels": 400, "expected_total_attractions": 240, "reported_total_attractions": 240, "meal_scale_eval": {"ok": true, "party_total": 3, "budget_level": "limited", "per_person_lunch_dinner_floor": 25, "per_person_breakfast_floor": 10, "meal_count": 6, "checked_count": 6, "failure_count": 0, "failures": []}}}]`

### v3_standard200_eval_000011
- request: 福州 2026-06-21->2026-06-24 days=4 transport=打车 hotel=经济型酒店 prefs=['第一次来', '城市漫步']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 2400, "total": 2300, "diff": 100, "requested_budget": {"available": true, "amount": 3800, "scope": "total", "party_size": 2, "total": 3800, "source": "budget_constraint", "budget_level": "standard", "strictness": "soft"}, "per_person_day": 287.5, "budget_level": "standard", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "standard", "strictness": "soft", "amount": 3800, "target_min_ratio": 0.55, "target_max_ratio": 1.1, "target_min_total": 2100, "target_max_total": 4200, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 2, "room_count": 1, "priced_nights": 3, "expected_min_total_hotels": 600, "reported_total_hotels": 600, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 117, "expected_total_attractions": 234, "reported_total_attractions": 254, "meal_per_person_cost_sum": 619, "expected_total_meals": 1238, "reported_total_meals": 1046, "reported_total_transportation": 500}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 117, "expected_total_attractions": 234, "reported_total_attractions": 254, "meal_per_person_cost_sum": 619, "expected_total_meals": 1238, "reported_total_meals": 1046, "reported_total_transportation": 500}}]`

### v3_standard200_eval_000012
- request: 洛阳 2025-05-07->2025-05-10 days=4 transport=打车 hotel=高端酒店 prefs=['休闲慢游', '第一次来']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 521, "expected_total_attractions": 1563, "reported_total_attractions": 1443, "meal_per_person_cost_sum": 618, "expected_total_meals": 1854, "reported_total_meals": 2676, "reported_total_transportation": 2000}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 521, "expected_total_attractions": 1563, "reported_total_attractions": 1443, "meal_per_person_cost_sum": 618, "expected_total_meals": 1854, "reported_total_meals": 2676, "reported_total_transportation": 2000}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": true, "meal_cost_scale_ok": false, "budget_relationship_ok": false, "expected_total_hotels": 4500, "reported_total_hotels": 4500, "expected_total_attractions": 1563, "reported_total_attractions": 1443, "meal_scale_eval": {"ok": false, "party_total": 3, "budget_level": "premium", "per_person_lunch_dinner_floor": 70, "per_person_breakfast_floor": 28, "meal_count": 12, "checked_count": 8, "failure_count": 3, "failures": [{"date": "2025-05-07", "type": "lunch", "name": "菜先生私厨", "estimated_cost": 56, "min_expected_cost": 70}, {"date": "2025-05-08", "type": "lunch", "name": "豪享来(政和店)", "estimated_cost": 67, "min_expected_cost": 70}, {"date": "2025-05-10", "type": "lunch", "name": "宴愉餐茶艺术餐厅", "estimated_cost": 67, "min_expected_cost": 70}]}}}]`
