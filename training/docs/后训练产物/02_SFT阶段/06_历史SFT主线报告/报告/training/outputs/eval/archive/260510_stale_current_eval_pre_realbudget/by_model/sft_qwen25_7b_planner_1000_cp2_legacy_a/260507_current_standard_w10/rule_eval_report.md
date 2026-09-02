# Rule Eval Report: sft_qwen25_7b_v3_1000_cp2_v1_current_standard_w10

- records: 200
- generations: `training/outputs/eval/sft_qwen25_7b_v3_1000_cp2_v1_current_standard_w10/generations.jsonl`
- records_path: `training/data/v3/eval/records.jsonl`

## Boolean Metrics

| Metric | Pass | Total | Rate |
| --- | ---: | ---: | ---: |
| accommodation_type_ok | 196 | 196 | 100.00% |
| attraction_budget_consistent | 30 | 196 | 15.31% |
| attraction_budget_party_relation_ok | 89 | 196 | 45.41% |
| attraction_count_ok | 182 | 196 | 92.86% |
| attraction_diversity_ok | 164 | 196 | 83.67% |
| attraction_grounding_ok | 193 | 196 | 98.47% |
| attraction_repeat_limit_ok | 164 | 196 | 83.67% |
| budget_arithmetic_consistent | 143 | 196 | 72.96% |
| budget_consistent | 143 | 196 | 72.96% |
| budget_level_aligned | 154 | 196 | 78.57% |
| budget_preference_aligned | 154 | 196 | 78.57% |
| budget_relationship_ok | 31 | 196 | 15.82% |
| budget_selection_ok | 126 | 196 | 64.29% |
| budget_user_constraint_ok | 194 | 196 | 98.98% |
| budget_within_user_budget | 194 | 196 | 98.98% |
| city_ok | 196 | 196 | 100.00% |
| date_range_ok | 196 | 196 | 100.00% |
| day_dates_ok | 196 | 196 | 100.00% |
| day_index_ok | 196 | 196 | 100.00% |
| days_len_ok | 196 | 196 | 100.00% |
| dpo_soft_pass | 84 | 196 | 42.86% |
| dpo_soft_recomputed_budget_pass | 72 | 196 | 36.73% |
| hard_pass | 171 | 196 | 87.24% |
| hotel_budget_covers_nights | 142 | 196 | 72.45% |
| hotel_budget_relation_ok | 143 | 196 | 72.96% |
| hotel_distance_placeholder_ok | 196 | 196 | 100.00% |
| hotel_grounding_ok | 196 | 196 | 100.00% |
| invalid_hotel_name_ok | 196 | 196 | 100.00% |
| json_extract_ok | 198 | 200 | 99.00% |
| legacy_hard_pass | 68 | 196 | 34.69% |
| location_object_ok | 196 | 196 | 100.00% |
| meal_budget_consistent | 2 | 196 | 1.02% |
| meal_complete | 196 | 196 | 100.00% |
| meal_cost_scale_ok | 94 | 196 | 47.96% |
| meal_diversity_ok | 146 | 196 | 74.49% |
| meal_grounding_ok | 187 | 196 | 95.41% |
| meal_lunch_dinner_same_day_ok | 174 | 196 | 88.78% |
| meal_repeat_limit_ok | 161 | 196 | 82.14% |
| meal_specific_ok | 195 | 196 | 99.49% |
| meal_valid_semantics_ok | 188 | 196 | 95.92% |
| middle_hotel_ok | 196 | 196 | 100.00% |
| recomputed_budget_fit_ok | 126 | 196 | 64.29% |
| recomputed_budget_hard_ok | 192 | 196 | 97.96% |
| recomputed_budget_level_aligned | 126 | 196 | 64.29% |
| recomputed_budget_preference_aligned | 126 | 196 | 64.29% |
| recomputed_budget_user_constraint_ok | 192 | 196 | 97.96% |
| recomputed_budget_within_user_budget | 192 | 196 | 97.96% |
| schema_ok | 196 | 200 | 98.00% |
| sft_budget_semantic_hard_pass | 27 | 196 | 13.78% |
| sft_hard_pass | 171 | 196 | 87.24% |
| sft_no_budget_sum_hard_pass | 171 | 196 | 87.24% |
| sft_strict_hard_pass | 0 | 196 | 0.00% |
| transportation_budget_nonnegative | 196 | 196 | 100.00% |
| weather_dates_ok | 196 | 196 | 100.00% |
| weather_match | 196 | 196 | 100.00% |

## Numeric Metrics

```json
{
  "attraction_diversity_unique_rate": {
    "avg": 0.9787,
    "p50": 1.0,
    "p90": 1.0
  },
  "attraction_grounding_rate": {
    "avg": 0.9983,
    "p50": 1.0,
    "p90": 1.0
  },
  "hotel_grounding_rate": {
    "avg": 1.0,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_diversity_unique_rate": {
    "avg": 0.8486,
    "p50": 0.8889,
    "p90": 1.0
  },
  "meal_food_pois_grounding_rate": {
    "avg": 0.9947,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_grounding_rate": {
    "avg": 0.9947,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_semantic_valid_rate": {
    "avg": 0.9953,
    "p50": 1.0,
    "p90": 1.0
  },
  "recomputed_budget_per_person_day": {
    "avg": 507.9057,
    "p50": 463.5,
    "p90": 726.0
  },
  "recomputed_budget_total": {
    "avg": 4845.7959,
    "p50": 4076.0,
    "p90": 8684.0
  }
}
```

## Failure Types

```json
{
  "meal_budget_inconsistent": 196,
  "attraction_budget_inconsistent": 166,
  "budget_relationship_mismatch": 165,
  "meal_cost_scale_too_low": 102,
  "hotel_budget_underestimated": 54,
  "budget_arithmetic_inconsistent": 53,
  "budget_preference_mismatch": 42,
  "meal_repeat_too_many": 35,
  "attraction_repeat_too_many": 32,
  "meal_same_day_lunch_dinner_repeat": 22,
  "too_many_attractions": 14,
  "meal_invalid_name": 8,
  "json_extract": 2,
  "budget_hard_constraint_exceeded": 2,
  "schema": 2,
  "meal_placeholder": 1,
  "meal_grounding_miss": 1
}
```

## Failure Examples

### v3_standard200_eval_000007
- request: 成都 2026-05-11->2026-05-13 days=3 transport=地铁+步行 hotel=舒适型酒店 prefs=['美食', '城市公园', '休闲慢游']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "山面包", "count": 3, "max_allowed": 2, "occurrences": [{"date": "2026-05-11", "type": "breakfast", "name": "山面包(东郊记忆店)"}, {"date": "2026-05-12", "type": "breakfast", "name": "山面包(望平街店)"}, {"date": "2026-05-13", "type": "breakfast", "name": "山面包(东郊记忆店)"}]}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 165, "expected_total_attractions": 330, "reported_total_attractions": 320, "meal_per_person_cost_sum": 663, "expected_total_meals": 1326, "reported_total_meals": 1180, "reported_total_transportation": 400}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 165, "expected_total_attractions": 330, "reported_total_attractions": 320, "meal_per_person_cost_sum": 663, "expected_total_meals": 1326, "reported_total_meals": 1180, "reported_total_transportation": 400}}]`

### v3_standard200_eval_000008
- request: 大理 2026-05-11->2026-05-13 days=3 transport=地铁+步行 hotel=舒适型酒店 prefs=['休闲慢游', '城市地标', '历史文化']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-05-12", "lunch": "海东茄子烧烤(古城店)", "dinner": "海东茄子烧烤(锦生店)"}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 75, "expected_total_attractions": 150, "reported_total_attractions": 300, "meal_per_person_cost_sum": 409, "expected_total_meals": 818, "reported_total_meals": 748, "reported_total_transportation": 150}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 75, "expected_total_attractions": 150, "reported_total_attractions": 300, "meal_per_person_cost_sum": 409, "expected_total_meals": 818, "reported_total_meals": 748, "reported_total_transportation": 150}}]`

### v3_standard200_eval_000001
- request: 桂林 2026-09-04->2026-09-06 days=3 transport=公共交通 hotel=高端酒店 prefs=['艺术', '美食', '第一次来', '历史文化']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "广西省立艺术馆", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-09-04", "day_index": 0, "name": "广西省立艺术馆"}, {"date": "2026-09-06", "day_index": 2, "name": "广西省立艺术馆"}]}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 2, "party_total": 2, "room_count": 1, "priced_nights": 2, "expected_min_total_hotels": 1500, "reported_total_hotels": 3000, "diff": 1500, "covers_nights": false}}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 4500, "total": 4400, "diff": 100, "requested_budget": {"available": true, "amount": 5600, "scope": "total", "party_size": 2, "total": 5600, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "soft"}, "per_person_day": 733.33, "budget_level": "comfortable", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "soft", "amount": 5600, "target_min_ratio": 0.65, "target_max_ratio": 1.1, "target_min_total": 3600, "target_max_total": 6200, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 2, "room_count": 1, "priced_nights": 2, "expected_min_total_hotels": 1500, "reported_total_hotels": 3000, "diff": 1500, "covers_nights": false}, "hotel_budget_covers_nights": false}}]`

### v3_standard200_eval_000000
- request: 昆明 2026-04-07->2026-04-09 days=3 transport=地铁+步行 hotel=高端酒店 prefs=['休闲慢游', '美食']
- errors: `[{"stage": "rule", "type": "meal_placeholder", "details": [{"date": "2026-04-07", "type": "breakfast", "name": "BA(翠湖公园店)"}]}, {"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-04-07", "type": "breakfast", "name": "BA(翠湖公园店)", "reason": "non_food_poi_name"}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 2, "party_total": 2, "room_count": 1, "priced_nights": 2, "expected_min_total_hotels": 1500, "reported_total_hotels": 3000, "diff": 1500, "covers_nights": false}}]`

### v3_standard200_eval_000005
- request: 广州 2026-07-06->2026-07-08 days=3 transport=地铁+步行 hotel=经济型酒店 prefs=['博物馆', '城市公园', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 1900, "total": 1800, "diff": 100, "requested_budget": {"available": true, "amount": 1900, "scope": "total", "party_size": 2, "total": 1900, "source": "budget_constraint", "budget_level": "limited", "strictness": "soft"}, "per_person_day": 300.0, "budget_level": "limited", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "limited", "strictness": "soft", "amount": 1900, "target_min_ratio": 0.72, "target_max_ratio": 1.05, "target_min_total": 1400, "target_max_total": 2000, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 2, "room_count": 1, "priced_nights": 2, "expected_min_total_hotels": 500, "reported_total_hotels": 500, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 30, "expected_total_attractions": 60, "reported_total_attractions": 120, "meal_per_person_cost_sum": 586, "expected_total_meals": 1172, "reported_total_meals": 1080, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 30, "expected_total_attractions": 60, "reported_total_attractions": 120, "meal_per_person_cost_sum": 586, "expected_total_meals": 1172, "reported_total_meals": 1080, "reported_total_transportation": 200}}]`

### v3_standard200_eval_000010
- request: 西安 2026-08-05->2026-08-08 days=4 transport=公共交通 hotel=经济型酒店 prefs=['城市公园', '美食']
- errors: `[{"stage": "rule", "type": "too_many_attractions", "details": [{"date": "2026-08-05", "count": 4}]}, {"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-08-07", "lunch": "清真刚刚烤肉(芙蓉街店)", "dinner": "清真刚刚烤肉(小南门店)"}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 2, "room_count": 1, "priced_nights": 3, "expected_min_total_hotels": 750, "reported_total_hotels": 1500, "diff": 750, "covers_nights": false}}]`

### v3_standard200_eval_000004
- request: 张家界 2026-05-11->2026-05-15 days=5 transport=地铁+步行 hotel=舒适型酒店 prefs=['亲子', '城市漫步', '历史文化']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 4, "party_total": 4, "room_count": 2, "priced_nights": 4, "expected_min_total_hotels": 3200, "reported_total_hotels": 1600, "diff": -1600, "covers_nights": false}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 400, "expected_total_attractions": 1600, "reported_total_attractions": 1600, "meal_per_person_cost_sum": 721, "expected_total_meals": 2884, "reported_total_meals": 1600, "reported_total_transportation": 1000}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": false, "attraction_budget_party_relation_ok": true, "meal_cost_scale_ok": false, "budget_relationship_ok": false, "expected_total_hotels": 3200, "reported_total_hotels": 1600, "expected_total_attractions": 1600, "reported_total_attractions": 1600, "meal_scale_eval": {"ok": false, "party_total": 4, "budget_level": "standard", "per_person_lunch_dinner_floor": 35, "per_person_breakfast_floor": 14, "meal_count": 15, "checked_count": 15, "failure_count": 1, "failures": [{"date": "2026-05-12", "type": "breakfast", "name": "家旺小吃(解放路店)", "estimated_cost": 13, "min_expected_cost": 14}]}}}]`

### v3_standard200_eval_000003
- request: 西安 2025-05-07->2025-05-11 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '历史文化', '购物商圈']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "陕西历史博物馆", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2025-05-07", "day_index": 0, "name": "陕西历史博物馆"}, {"date": "2025-05-10", "day_index": 3, "name": "陕西历史博物馆"}]}]}, {"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2025-05-09", "lunch": "东北王酱骨", "dinner": "东北王酱骨"}, {"date": "2025-05-10", "lunch": "国人川菜(李家村店)", "dinner": "国人川菜(李家村店)"}, {"date": "2025-05-11", "lunch": "东北王酱骨", "dinner": "东北王酱骨"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "东北王酱骨", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2025-05-09", "type": "lunch", "name": "东北王酱骨"}, {"date": "2025-05-09", "type": "dinner", "name": "东北王酱骨"}, {"date": "2025-05-11", "type": "lunch", "name": "东北王酱骨"}, {"date": "2025-05-11", "type": "dinner", "name": "东北王酱骨"}]}]}]`

### v3_standard200_eval_000002
- request: 杭州 2026-05-01->2026-05-05 days=5 transport=公共交通 hotel=经济型酒店 prefs=['美食', '休闲慢游', '户外轻徒步', '城市漫步']
- errors: `[{"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-05-05", "type": "lunch", "name": "清河坊历史文化特色街区", "reason": "unknown_food_semantics"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "泮芳春煎饺", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-05-01", "type": "breakfast", "name": "泮芳春煎饺(龙翔桥店)"}, {"date": "2026-05-02", "type": "breakfast", "name": "泮芳春煎饺(龙翔桥店)"}, {"date": "2026-05-03", "type": "breakfast", "name": "泮芳春煎饺(龙翔桥店)"}, {"date": "2026-05-04", "type": "breakfast", "name": "泮芳春煎饺(龙翔桥店)"}, {"date": "2026-05-05", "type": "breakfast", "name": "泮芳春煎饺(龙翔桥店)"}]}]}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 2104, "total": 2004, "diff": 100, "requested_budget": {"available": true, "amount": 2000, "scope": "total", "party_size": 1, "total": 2000, "source": "budget_constraint", "budget_level": "limited", "strictness": "soft"}, "per_person_day": 400.8, "budget_level": "limited", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "limited", "strictness": "soft", "amount": 2000, "target_min_ratio": 0.72, "target_max_ratio": 1.05, "target_min_total": 1400, "target_max_total": 2100, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 4, "party_total": 1, "room_count": 1, "priced_nights": 4, "expected_min_total_hotels": 1000, "reported_total_hotels": 1000, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_standard200_eval_000014
- request: 成都 2026-06-06->2026-06-07 days=2 transport=打车 hotel=经济型酒店 prefs=['小众展览', '美食', '城市地标']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 165, "expected_total_attractions": 660, "reported_total_attractions": 1080, "meal_per_person_cost_sum": 418, "expected_total_meals": 1672, "reported_total_meals": 1040, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 165, "expected_total_attractions": 660, "reported_total_attractions": 1080, "meal_per_person_cost_sum": 418, "expected_total_meals": 1672, "reported_total_meals": 1040, "reported_total_transportation": 200}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": false, "meal_cost_scale_ok": true, "budget_relationship_ok": false, "expected_total_hotels": 500, "reported_total_hotels": 500, "expected_total_attractions": 660, "reported_total_attractions": 1080, "meal_scale_eval": {"ok": true, "party_total": 4, "budget_level": "limited", "per_person_lunch_dinner_floor": 25, "per_person_breakfast_floor": 10, "meal_count": 6, "checked_count": 6, "failure_count": 0, "failures": []}}}]`

### v3_standard200_eval_000009
- request: 苏州 2026-04-30->2026-05-04 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['亲子', '城市地标', '第一次来', '城市漫步']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "拙政园", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-04-30", "day_index": 0, "name": "拙政园"}, {"date": "2026-05-03", "day_index": 3, "name": "拙政园"}]}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 370, "expected_total_attractions": 1480, "reported_total_attractions": 2800, "meal_per_person_cost_sum": 781, "expected_total_meals": 3124, "reported_total_meals": 2900, "reported_total_transportation": 1000}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 370, "expected_total_attractions": 1480, "reported_total_attractions": 2800, "meal_per_person_cost_sum": 781, "expected_total_meals": 3124, "reported_total_meals": 2900, "reported_total_transportation": 1000}}]`

### v3_standard200_eval_000015
- request: 南京 2026-04-07->2026-04-08 days=2 transport=地铁+步行 hotel=经济型酒店 prefs=['亲子', '休闲慢游', '历史文化']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 1, "party_total": 3, "room_count": 2, "priced_nights": 1, "expected_min_total_hotels": 500, "reported_total_hotels": 250, "diff": -250, "covers_nights": false}}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 1687, "total": 1787, "diff": -100, "requested_budget": {"available": true, "amount": 3600, "scope": "total", "party_size": 3, "total": 3600, "source": "budget_constraint", "budget_level": "standard", "strictness": "soft"}, "per_person_day": 297.83, "budget_level": "standard", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "standard", "strictness": "soft", "amount": 3600, "target_min_ratio": 0.55, "target_max_ratio": 1.1, "target_min_total": 2000, "target_max_total": 4000, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 1, "party_total": 3, "room_count": 2, "priced_nights": 1, "expected_min_total_hotels": 500, "reported_total_hotels": 250, "diff": -250, "covers_nights": false}, "hotel_budget_covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 65, "expected_total_attractions": 195, "reported_total_attractions": 215, "meal_per_person_cost_sum": 319, "expected_total_meals": 957, "reported_total_meals": 1122, "reported_total_transportation": 100}}]`

### v3_standard200_eval_000013
- request: 武汉 2026-05-09->2026-05-11 days=3 transport=公共交通 hotel=舒适型酒店 prefs=['亲子', '老人友好', '第一次来', '城市公园']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 2, "party_total": 6, "room_count": 3, "priced_nights": 2, "expected_min_total_hotels": 2400, "reported_total_hotels": 1600, "diff": -800, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 6, "hotel_room_count": 3, "attraction_ticket_sum": 130, "expected_total_attractions": 780, "reported_total_attractions": 1260, "meal_per_person_cost_sum": 476, "expected_total_meals": 2856, "reported_total_meals": 2520, "reported_total_transportation": 1000}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 6, "hotel_room_count": 3, "attraction_ticket_sum": 130, "expected_total_attractions": 780, "reported_total_attractions": 1260, "meal_per_person_cost_sum": 476, "expected_total_meals": 2856, "reported_total_meals": 2520, "reported_total_transportation": 1000}}]`

### v3_standard200_eval_000021
- request: 上海 2026-06-21->2026-06-22 days=2 transport=地铁+步行 hotel=经济型酒店 prefs=['老人友好', '休闲慢游', '城市漫步', '主题乐园']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 100, "expected_total_attractions": 200, "reported_total_attractions": 220, "meal_per_person_cost_sum": 488, "expected_total_meals": 976, "reported_total_meals": 600, "reported_total_transportation": 130}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 100, "expected_total_attractions": 200, "reported_total_attractions": 220, "meal_per_person_cost_sum": 488, "expected_total_meals": 976, "reported_total_meals": 600, "reported_total_transportation": 130}}]`

### v3_standard200_eval_000016
- request: 苏州 2026-06-06->2026-06-08 days=3 transport=公共交通 hotel=民宿 prefs=['海滨度假', '城市公园', '主题乐园', '清真']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 220, "expected_total_attractions": 440, "reported_total_attractions": 355, "meal_per_person_cost_sum": 305, "expected_total_meals": 610, "reported_total_meals": 545, "reported_total_transportation": 100}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 220, "expected_total_attractions": 440, "reported_total_attractions": 355, "meal_per_person_cost_sum": 305, "expected_total_meals": 610, "reported_total_meals": 545, "reported_total_transportation": 100}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": true, "meal_cost_scale_ok": false, "budget_relationship_ok": false, "expected_total_hotels": 600, "reported_total_hotels": 600, "expected_total_attractions": 440, "reported_total_attractions": 355, "meal_scale_eval": {"ok": false, "party_total": 2, "budget_level": "limited", "per_person_lunch_dinner_floor": 25, "per_person_breakfast_floor": 10, "meal_count": 9, "checked_count": 6, "failure_count": 1, "failures": [{"date": "2026-06-08", "type": "lunch", "name": "丝路回乡小吃店(西夏店)", "estimated_cost": 24, "min_expected_cost": 25}]}}}]`

### v3_standard200_eval_000006
- request: 南京 2026-07-06->2026-07-09 days=4 transport=打车 hotel=经济型酒店 prefs=['老人友好', '美食', '城市公园', '休闲慢游']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "玄武湖景区", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-07-06", "day_index": 0, "name": "玄武湖景区"}, {"date": "2026-07-07", "day_index": 1, "name": "玄武湖景区"}]}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 273, "expected_total_attractions": 819, "reported_total_attractions": 1050, "meal_per_person_cost_sum": 856, "expected_total_meals": 2568, "reported_total_meals": 1800, "reported_total_transportation": 500}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 273, "expected_total_attractions": 819, "reported_total_attractions": 1050, "meal_per_person_cost_sum": 856, "expected_total_meals": 2568, "reported_total_meals": 1800, "reported_total_transportation": 500}}]`

### v3_standard200_eval_000017
- request: 苏州 2026-05-09->2026-05-11 days=3 transport=地铁+步行 hotel=亲子酒店 prefs=['亲子', '历史文化', '休闲慢游', '户外轻徒步']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-05-10", "lunch": "稻山村·苏州菜(石路店)", "dinner": "稻山村·苏州菜(曼哈顿店)"}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 2, "party_total": 3, "room_count": 2, "priced_nights": 2, "expected_min_total_hotels": 5000, "reported_total_hotels": 2500, "diff": -2500, "covers_nights": false}}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 5850, "total": 7850, "diff": -2000, "requested_budget": {"available": true, "amount": 9900, "scope": "total", "party_size": 3, "total": 9900, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "soft"}, "per_person_day": 872.22, "budget_level": "comfortable", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "soft", "amount": 9900, "target_min_ratio": 0.65, "target_max_ratio": 1.1, "target_min_total": 6400, "target_max_total": 10900, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 3, "room_count": 2, "priced_nights": 2, "expected_min_total_hotels": 5000, "reported_total_hotels": 2500, "diff": -2500, "covers_nights": false}, "hotel_budget_covers_nights": false}}]`

### v3_standard200_eval_000018
- request: 天津 2026-07-06->2026-07-07 days=2 transport=打车 hotel=舒适型酒店 prefs=['老人友好', '夜市夜景', '艺术', '第一次来']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 1, "party_total": 3, "room_count": 2, "priced_nights": 1, "expected_min_total_hotels": 800, "reported_total_hotels": 400, "diff": -400, "covers_nights": false}}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 2900, "total": 2850, "diff": 50, "requested_budget": {"available": true, "amount": 3100, "scope": "total", "party_size": 3, "total": 3100, "source": "budget_constraint", "budget_level": "limited", "strictness": "hard"}, "per_person_day": 475.0, "budget_level": "limited", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "limited", "strictness": "hard", "amount": 3100, "target_min_ratio": 0.72, "target_max_ratio": 1.0, "target_min_total": 2200, "target_max_total": 3100, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 1, "party_total": 3, "room_count": 2, "priced_nights": 1, "expected_min_total_hotels": 800, "reported_total_hotels": 400, "diff": -400, "covers_nights": false}, "hotel_budget_covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 130, "expected_total_attractions": 390, "reported_total_attractions": 450, "meal_per_person_cost_sum": 343, "expected_total_meals": 1029, "reported_total_meals": 1050, "reported_total_transportation": 1000}}]`

### v3_standard200_eval_000022
- request: 桂林 2026-04-07->2026-04-10 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['亲子', '自然风光', '休闲慢游']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 4000, "total": 3900, "diff": 100, "requested_budget": {"available": true, "amount": 4800, "scope": "total", "party_size": 3, "total": 4800, "source": "budget_constraint", "budget_level": "limited", "strictness": "soft"}, "per_person_day": 325.0, "budget_level": "limited", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "limited", "strictness": "soft", "amount": 4800, "target_min_ratio": 0.72, "target_max_ratio": 1.05, "target_min_total": 3500, "target_max_total": 5000, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 3, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 1200, "reported_total_hotels": 1200, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 575, "expected_total_attractions": 1725, "reported_total_attractions": 1410, "meal_per_person_cost_sum": 484, "expected_total_meals": 1452, "reported_total_meals": 1190, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 575, "expected_total_attractions": 1725, "reported_total_attractions": 1410, "meal_per_person_cost_sum": 484, "expected_total_meals": 1452, "reported_total_meals": 1190, "reported_total_transportation": 200}}]`

### v3_standard200_eval_000019
- request: 丽江 2026-05-11->2026-05-15 days=5 transport=打车 hotel=经济型酒店 prefs=['亲子', '老人友好', '海滨度假', '美食']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "黑龙潭", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-05-11", "day_index": 0, "name": "黑龙潭"}, {"date": "2026-05-15", "day_index": 4, "name": "黑龙潭"}]}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 4, "party_total": 5, "room_count": 3, "priced_nights": 4, "expected_min_total_hotels": 3600, "reported_total_hotels": 2400, "diff": -1200, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 5, "hotel_room_count": 3, "attraction_ticket_sum": 560, "expected_total_attractions": 2800, "reported_total_attractions": 4000, "meal_per_person_cost_sum": 825, "expected_total_meals": 4125, "reported_total_meals": 3700, "reported_total_transportation": 1000}}]`
