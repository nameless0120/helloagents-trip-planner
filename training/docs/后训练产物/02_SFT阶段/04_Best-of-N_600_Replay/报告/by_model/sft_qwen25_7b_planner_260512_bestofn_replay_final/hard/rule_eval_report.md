# Rule Eval Report: 260511_high_end_context_hard_w10

- records: 300
- generations: `training/outputs/eval/by_model/sft_qwen25_7b_v3_260512_bestofn_replay_final/260511_high_end_context_hard_w10/generations.jsonl`
- records_path: `training/data/v3/eval_hard/records.jsonl`

## Boolean Metrics

| Metric | Pass | Total | Rate |
| --- | ---: | ---: | ---: |
| accommodation_type_ok | 299 | 299 | 100.00% |
| attraction_budget_consistent | 88 | 299 | 29.43% |
| attraction_budget_party_relation_ok | 291 | 299 | 97.32% |
| attraction_count_ok | 298 | 299 | 99.67% |
| attraction_diversity_ok | 258 | 299 | 86.29% |
| attraction_grounding_ok | 297 | 299 | 99.33% |
| attraction_repeat_limit_ok | 258 | 299 | 86.29% |
| budget_arithmetic_consistent | 195 | 299 | 65.22% |
| budget_consistent | 195 | 299 | 65.22% |
| budget_level_aligned | 198 | 299 | 66.22% |
| budget_preference_aligned | 198 | 299 | 66.22% |
| budget_relationship_ok | 229 | 299 | 76.59% |
| budget_selection_ok | 137 | 299 | 45.82% |
| budget_user_constraint_ok | 251 | 299 | 83.95% |
| budget_within_user_budget | 273 | 299 | 91.30% |
| city_ok | 299 | 299 | 100.00% |
| date_range_ok | 299 | 299 | 100.00% |
| day_dates_ok | 299 | 299 | 100.00% |
| day_index_ok | 299 | 299 | 100.00% |
| days_len_ok | 299 | 299 | 100.00% |
| dpo_soft_pass | 148 | 299 | 49.50% |
| dpo_soft_recomputed_budget_pass | 95 | 299 | 31.77% |
| hard_pass | 294 | 299 | 98.33% |
| hotel_budget_covers_nights | 284 | 299 | 94.98% |
| hotel_budget_relation_ok | 290 | 299 | 96.99% |
| hotel_distance_placeholder_ok | 299 | 299 | 100.00% |
| hotel_grounding_ok | 299 | 299 | 100.00% |
| invalid_hotel_name_ok | 299 | 299 | 100.00% |
| json_extract_ok | 300 | 300 | 100.00% |
| legacy_hard_pass | 157 | 299 | 52.51% |
| location_object_ok | 299 | 299 | 100.00% |
| meal_budget_consistent | 1 | 299 | 0.33% |
| meal_complete | 299 | 299 | 100.00% |
| meal_cost_scale_ok | 243 | 299 | 81.27% |
| meal_diversity_ok | 258 | 299 | 86.29% |
| meal_grounding_ok | 297 | 299 | 99.33% |
| meal_lunch_dinner_same_day_ok | 295 | 299 | 98.66% |
| meal_repeat_limit_ok | 262 | 299 | 87.63% |
| meal_specific_ok | 299 | 299 | 100.00% |
| meal_valid_semantics_ok | 297 | 299 | 99.33% |
| middle_hotel_ok | 299 | 299 | 100.00% |
| recomputed_budget_fit_ok | 137 | 299 | 45.82% |
| recomputed_budget_hard_ok | 212 | 299 | 70.90% |
| recomputed_budget_level_aligned | 137 | 299 | 45.82% |
| recomputed_budget_preference_aligned | 137 | 299 | 45.82% |
| recomputed_budget_user_constraint_ok | 212 | 299 | 70.90% |
| recomputed_budget_within_user_budget | 255 | 299 | 85.28% |
| schema_ok | 299 | 300 | 99.67% |
| sft_budget_semantic_hard_pass | 185 | 299 | 61.87% |
| sft_hard_pass | 294 | 299 | 98.33% |
| sft_no_budget_sum_hard_pass | 294 | 299 | 98.33% |
| sft_strict_hard_pass | 0 | 299 | 0.00% |
| transportation_budget_nonnegative | 299 | 299 | 100.00% |
| weather_dates_ok | 299 | 299 | 100.00% |
| weather_match | 299 | 299 | 100.00% |

## Numeric Metrics

```json
{
  "attraction_diversity_unique_rate": {
    "avg": 0.9801,
    "p50": 1.0,
    "p90": 1.0
  },
  "attraction_grounding_rate": {
    "avg": 0.9993,
    "p50": 1.0,
    "p90": 1.0
  },
  "hotel_grounding_rate": {
    "avg": 1.0,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_diversity_unique_rate": {
    "avg": 0.8915,
    "p50": 0.9333,
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
    "avg": 0.9994,
    "p50": 1.0,
    "p90": 1.0
  },
  "recomputed_budget_per_person_day": {
    "avg": 921.1182,
    "p50": 918.4,
    "p90": 1489.33
  },
  "recomputed_budget_total": {
    "avg": 9834.5585,
    "p50": 9030.0,
    "p90": 17130.0
  }
}
```

## Failure Types

```json
{
  "meal_budget_inconsistent": 298,
  "attraction_budget_inconsistent": 211,
  "budget_arithmetic_inconsistent": 104,
  "budget_preference_mismatch": 101,
  "budget_relationship_mismatch": 70,
  "meal_cost_scale_too_low": 56,
  "budget_hard_constraint_exceeded": 48,
  "attraction_repeat_too_many": 41,
  "meal_repeat_too_many": 37,
  "hotel_budget_underestimated": 15,
  "meal_same_day_lunch_dinner_repeat": 4,
  "meal_invalid_name": 2,
  "schema": 1,
  "too_many_attractions": 1
}
```

## Failure Examples

### v3_hard_realbudget_eval_000004
- request: 张家界 2026-05-11->2026-05-13 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 4010, "total": 3010, "diff": 1000, "requested_budget": {"available": true, "amount": 3200, "scope": "total", "party_size": 1, "total": 3200, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "hard"}, "per_person_day": 1003.33, "budget_level": "comfortable", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "hard", "amount": 3200, "target_min_ratio": 0.7, "target_max_ratio": 1.0, "target_min_total": 2200, "target_max_total": 3200, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 1, "room_count": 1, "priced_nights": 2, "expected_min_total_hotels": 2600, "reported_total_hotels": 2600, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 610, "expected_total_attractions": 610, "reported_total_attractions": 610, "meal_per_person_cost_sum": 694, "expected_total_meals": 694, "reported_total_meals": 600, "reported_total_transportation": 200}}]`

### v3_hard_realbudget_eval_000008
- request: 大理 2026-05-11->2026-05-13 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 9098, "total": 6198, "diff": 2900, "requested_budget": {"available": true, "amount": 8700, "scope": "total", "party_size": 3, "total": 8700, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "hard"}, "per_person_day": 688.67, "budget_level": "comfortable", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "hard", "amount": 8700, "target_min_ratio": 0.7, "target_max_ratio": 1.0, "target_min_total": 6100, "target_max_total": 8700, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 3, "room_count": 2, "priced_nights": 2, "expected_min_total_hotels": 5200, "reported_total_hotels": 5200, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 484, "expected_total_attractions": 1452, "reported_total_attractions": 1758, "meal_per_person_cost_sum": 761, "expected_total_meals": 2283, "reported_total_meals": 1440, "reported_total_transportation": 700}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 484, "expected_total_attractions": 1452, "reported_total_attractions": 1758, "meal_per_person_cost_sum": 761, "expected_total_meals": 2283, "reported_total_meals": 1440, "reported_total_transportation": 700}}]`

### v3_hard_realbudget_eval_000006
- request: 南京 2026-07-06->2026-07-09 days=4 transport=自驾 hotel=亲子酒店 prefs=['亲子', '动物园', '海洋馆', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 10049, "total": 9049, "diff": 1000, "requested_budget": {"available": true, "amount": 9000, "scope": "total", "party_size": 3, "total": 9000, "source": "budget_constraint", "budget_level": "standard", "strictness": "hard"}, "per_person_day": 754.08, "budget_level": "standard", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "standard", "strictness": "hard", "amount": 9000, "target_min_ratio": 0.6, "target_max_ratio": 1.0, "target_min_total": 5400, "target_max_total": 9000, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": false, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 3, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 8100, "reported_total_hotels": 8100, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 45, "expected_total_attractions": 135, "reported_total_attractions": 120, "meal_per_person_cost_sum": 895, "expected_total_meals": 2685, "reported_total_meals": 1629, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 45, "expected_total_attractions": 135, "reported_total_attractions": 120, "meal_per_person_cost_sum": 895, "expected_total_meals": 2685, "reported_total_meals": 1629, "reported_total_transportation": 200}}]`

### v3_hard_realbudget_eval_000001
- request: 桂林 2026-09-04->2026-09-07 days=4 transport=打车 hotel=高端酒店 prefs=['高端酒店', '艺术', '特色餐厅', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 9914, "total": 10914, "diff": -1000, "requested_budget": {"available": true, "amount": 13100, "scope": "total", "party_size": 2, "total": 13100, "source": "budget_constraint", "budget_level": "premium", "strictness": "soft"}, "per_person_day": 1364.25, "budget_level": "premium", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "premium", "strictness": "soft", "amount": 13100, "target_min_ratio": 0.75, "target_max_ratio": 1.12, "target_min_total": 9800, "target_max_total": 14700, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 2, "room_count": 1, "priced_nights": 3, "expected_min_total_hotels": 3900, "reported_total_hotels": 3900, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 1314, "expected_total_attractions": 2628, "reported_total_attractions": 2588, "meal_per_person_cost_sum": 1175, "expected_total_meals": 2350, "reported_total_meals": 2626, "reported_total_transportation": 800}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 1314, "expected_total_attractions": 2628, "reported_total_attractions": 2588, "meal_per_person_cost_sum": 1175, "expected_total_meals": 2350, "reported_total_meals": 2626, "reported_total_transportation": 800}}]`

### v3_hard_realbudget_eval_000002
- request: 杭州 2026-05-01->2026-05-04 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '夜市', '老字号', '城市漫步']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "杭州植物园", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-05-01", "day_index": 0, "name": "杭州植物园"}, {"date": "2026-05-02", "day_index": 1, "name": "杭州植物园"}]}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 130, "expected_total_attractions": 520, "reported_total_attractions": 440, "meal_per_person_cost_sum": 735, "expected_total_meals": 2940, "reported_total_meals": 2608, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 130, "expected_total_attractions": 520, "reported_total_attractions": 440, "meal_per_person_cost_sum": 735, "expected_total_meals": 2940, "reported_total_meals": 2608, "reported_total_transportation": 200}}]`

### v3_hard_realbudget_eval_000000
- request: 昆明 2026-04-07->2026-04-11 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 5, "hotel_room_count": 3, "attraction_ticket_sum": 483, "expected_total_attractions": 2415, "reported_total_attractions": 1565, "meal_per_person_cost_sum": 1083, "expected_total_meals": 5415, "reported_total_meals": 5950, "reported_total_transportation": 1500}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 5, "hotel_room_count": 3, "attraction_ticket_sum": 483, "expected_total_attractions": 2415, "reported_total_attractions": 1565, "meal_per_person_cost_sum": 1083, "expected_total_meals": 5415, "reported_total_meals": 5950, "reported_total_transportation": 1500}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": false, "meal_cost_scale_ok": true, "budget_relationship_ok": false, "expected_total_hotels": 7200, "reported_total_hotels": 7200, "expected_total_attractions": 2415, "reported_total_attractions": 1565, "meal_scale_eval": {"ok": true, "party_total": 5, "budget_level": "comfortable", "per_person_lunch_dinner_floor": 50, "breakfast_policy": "excluded_from_meal_cost_scale", "meal_count": 15, "checked_count": 10, "failure_count": 0, "failures": []}}}]`

### v3_hard_realbudget_eval_000003
- request: 西安 2025-05-07->2025-05-11 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 199, "expected_total_attractions": 398, "reported_total_attractions": 442, "meal_per_person_cost_sum": 716, "expected_total_meals": 1432, "reported_total_meals": 1808, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 199, "expected_total_attractions": 398, "reported_total_attractions": 442, "meal_per_person_cost_sum": 716, "expected_total_meals": 1432, "reported_total_meals": 1808, "reported_total_transportation": 200}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": true, "meal_cost_scale_ok": false, "budget_relationship_ok": false, "expected_total_hotels": 1800, "reported_total_hotels": 1800, "expected_total_attractions": 398, "reported_total_attractions": 442, "meal_scale_eval": {"ok": false, "party_total": 2, "budget_level": "standard", "per_person_lunch_dinner_floor": 35, "breakfast_policy": "excluded_from_meal_cost_scale", "meal_count": 15, "checked_count": 10, "failure_count": 1, "failures": [{"date": "2025-05-10", "type": "lunch", "name": "马洪小炒泡馍馆", "estimated_cost": 31, "min_expected_cost": 35}]}}}]`

### v3_hard_realbudget_eval_000010
- request: 西安 2026-08-05->2026-08-09 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "西安博物院", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-08-08", "day_index": 3, "name": "西安博物院"}, {"date": "2026-08-09", "day_index": 4, "name": "西安博物院"}]}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 5, "hotel_room_count": 3, "attraction_ticket_sum": 199, "expected_total_attractions": 995, "reported_total_attractions": 1225, "meal_per_person_cost_sum": 644, "expected_total_meals": 3220, "reported_total_meals": 5375, "reported_total_transportation": 1500}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 5, "hotel_room_count": 3, "attraction_ticket_sum": 199, "expected_total_attractions": 995, "reported_total_attractions": 1225, "meal_per_person_cost_sum": 644, "expected_total_meals": 3220, "reported_total_meals": 5375, "reported_total_transportation": 1500}}]`

### v3_hard_realbudget_eval_000005
- request: 广州 2026-07-06->2026-07-10 days=5 transport=公共交通 hotel=民宿 prefs=['摄影', '自然风光', '城市漫步', '本地菜']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 3601, "total": 2701, "diff": 900, "requested_budget": {"available": true, "amount": 4500, "scope": "total", "party_size": 1, "total": 4500, "source": "budget_constraint", "budget_level": "standard", "strictness": "hard"}, "per_person_day": 540.2, "budget_level": "standard", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "standard", "strictness": "hard", "amount": 4500, "target_min_ratio": 0.6, "target_max_ratio": 1.0, "target_min_total": 2700, "target_max_total": 4500, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 4, "party_total": 1, "room_count": 1, "priced_nights": 4, "expected_min_total_hotels": 1200, "reported_total_hotels": 1200, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 186, "expected_total_attractions": 186, "reported_total_attractions": 166, "meal_per_person_cost_sum": 1223, "expected_total_meals": 1223, "reported_total_meals": 1235, "reported_total_transportation": 1000}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 186, "expected_total_attractions": 186, "reported_total_attractions": 166, "meal_per_person_cost_sum": 1223, "expected_total_meals": 1223, "reported_total_meals": 1235, "reported_total_transportation": 1000}}]`

### v3_hard_realbudget_eval_000007
- request: 成都 2026-05-11->2026-05-15 days=5 transport=公共交通 hotel=民宿 prefs=['小众展馆', '咖啡', '艺术', '城市漫步', '特色餐厅']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 1199, "expected_total_attractions": 2398, "reported_total_attractions": 2872, "meal_per_person_cost_sum": 2643, "expected_total_meals": 5286, "reported_total_meals": 5528, "reported_total_transportation": 300}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 1199, "expected_total_attractions": 2398, "reported_total_attractions": 2872, "meal_per_person_cost_sum": 2643, "expected_total_meals": 5286, "reported_total_meals": 5528, "reported_total_transportation": 300}}]`

### v3_hard_realbudget_eval_000011
- request: 福州 2026-06-21->2026-06-24 days=4 transport=打车 hotel=高端酒店 prefs=['高端酒店', '艺术', '特色餐厅', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 9850, "total": 10050, "diff": -200, "requested_budget": {"available": true, "amount": 13500, "scope": "total", "party_size": 2, "total": 13500, "source": "budget_constraint", "budget_level": "premium", "strictness": "soft"}, "per_person_day": 1256.25, "budget_level": "premium", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "premium", "strictness": "soft", "amount": 13500, "target_min_ratio": 0.75, "target_max_ratio": 1.12, "target_min_total": 10100, "target_max_total": 15100, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 2, "room_count": 1, "priced_nights": 3, "expected_min_total_hotels": 3900, "reported_total_hotels": 3900, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 828, "expected_total_attractions": 1656, "reported_total_attractions": 1874, "meal_per_person_cost_sum": 1443, "expected_total_meals": 2886, "reported_total_meals": 3276, "reported_total_transportation": 800}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 828, "expected_total_attractions": 1656, "reported_total_attractions": 1874, "meal_per_person_cost_sum": 1443, "expected_total_meals": 2886, "reported_total_meals": 3276, "reported_total_transportation": 800}}]`

### v3_hard_realbudget_eval_000009
- request: 苏州 2026-04-30->2026-05-03 days=4 transport=打车 hotel=亲子酒店 prefs=['亲子', '老人友好', '博物馆', '城市公园', '特色餐厅']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 320, "expected_total_attractions": 1280, "reported_total_attractions": 1440, "meal_per_person_cost_sum": 772, "expected_total_meals": 3088, "reported_total_meals": 2640, "reported_total_transportation": 500}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 320, "expected_total_attractions": 1280, "reported_total_attractions": 1440, "meal_per_person_cost_sum": 772, "expected_total_meals": 3088, "reported_total_meals": 2640, "reported_total_transportation": 500}}]`

### v3_hard_realbudget_eval_000014
- request: 成都 2026-06-06->2026-06-08 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 4023, "total": 3023, "diff": 1000, "requested_budget": {"available": true, "amount": 4300, "scope": "total", "party_size": 1, "total": 4300, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "hard"}, "per_person_day": 1007.67, "budget_level": "comfortable", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "hard", "amount": 4300, "target_min_ratio": 0.7, "target_max_ratio": 1.0, "target_min_total": 3000, "target_max_total": 4300, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 1, "room_count": 1, "priced_nights": 2, "expected_min_total_hotels": 2700, "reported_total_hotels": 2700, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 286, "expected_total_attractions": 286, "reported_total_attractions": 286, "meal_per_person_cost_sum": 863, "expected_total_meals": 863, "reported_total_meals": 837, "reported_total_transportation": 200}}]`

### v3_hard_realbudget_eval_000012
- request: 洛阳 2025-05-07->2025-05-10 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '夜市', '老字号', '城市漫步']
- errors: `[{"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 320, "expected_total_attractions": 1280, "reported_total_attractions": 1280, "meal_per_person_cost_sum": 631, "expected_total_meals": 2524, "reported_total_meals": 2400, "reported_total_transportation": 300}}]`

### v3_hard_realbudget_eval_000018
- request: 天津 2026-07-06->2026-07-08 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 855, "expected_total_attractions": 2565, "reported_total_attractions": 2493, "meal_per_person_cost_sum": 2477, "expected_total_meals": 7431, "reported_total_meals": 4896, "reported_total_transportation": 600}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 855, "expected_total_attractions": 2565, "reported_total_attractions": 2493, "meal_per_person_cost_sum": 2477, "expected_total_meals": 7431, "reported_total_meals": 4896, "reported_total_transportation": 600}}, {"stage": "rule", "type": "budget_hard_constraint_exceeded", "details": {"part_sum": 15189, "total": 15189, "diff": 0, "requested_budget": {"available": true, "amount": 7900, "scope": "total", "party_size": 3, "total": 7900, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "hard"}, "per_person_day": 1687.67, "budget_level": "comfortable", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "hard", "amount": 7900, "target_min_ratio": 0.7, "target_max_ratio": 1.0, "target_min_total": 5500, "target_max_total": 7900, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": true, "within_user_budget": false, "user_constraint_ok": false, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 3, "room_count": 2, "priced_nights": 2, "expected_min_total_hotels": 7200, "reported_total_hotels": 7200, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_hard_realbudget_eval_000016
- request: 苏州 2026-06-06->2026-06-09 days=4 transport=自驾 hotel=亲子酒店 prefs=['亲子', '动物园', '海洋馆', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 420, "expected_total_attractions": 1260, "reported_total_attractions": 1245, "meal_per_person_cost_sum": 581, "expected_total_meals": 1743, "reported_total_meals": 2109, "reported_total_transportation": 800}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 420, "expected_total_attractions": 1260, "reported_total_attractions": 1245, "meal_per_person_cost_sum": 581, "expected_total_meals": 1743, "reported_total_meals": 2109, "reported_total_transportation": 800}}, {"stage": "rule", "type": "budget_hard_constraint_exceeded", "details": {"part_sum": 12254, "total": 12254, "diff": 0, "requested_budget": {"available": true, "amount": 10000, "scope": "total", "party_size": 3, "total": 10000, "source": "budget_constraint", "budget_level": "standard", "strictness": "hard"}, "per_person_day": 1021.17, "budget_level": "standard", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "standard", "strictness": "hard", "amount": 10000, "target_min_ratio": 0.6, "target_max_ratio": 1.0, "target_min_total": 6000, "target_max_total": 10000, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": true, "within_user_budget": false, "user_constraint_ok": false, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 3, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 8100, "reported_total_hotels": 8100, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_hard_realbudget_eval_000013
- request: 武汉 2026-05-09->2026-05-13 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 163, "expected_total_attractions": 326, "reported_total_attractions": 306, "meal_per_person_cost_sum": 1004, "expected_total_meals": 2008, "reported_total_meals": 2204, "reported_total_transportation": 400}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 163, "expected_total_attractions": 326, "reported_total_attractions": 306, "meal_per_person_cost_sum": 1004, "expected_total_meals": 2008, "reported_total_meals": 2204, "reported_total_transportation": 400}}]`

### v3_hard_realbudget_eval_000017
- request: 苏州 2026-05-09->2026-05-13 days=5 transport=公共交通 hotel=民宿 prefs=['小众展馆', '咖啡', '艺术', '城市漫步', '特色餐厅']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 320, "expected_total_attractions": 640, "reported_total_attractions": 750, "meal_per_person_cost_sum": 1314, "expected_total_meals": 2628, "reported_total_meals": 3450, "reported_total_transportation": 1700}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 320, "expected_total_attractions": 640, "reported_total_attractions": 750, "meal_per_person_cost_sum": 1314, "expected_total_meals": 2628, "reported_total_meals": 3450, "reported_total_transportation": 1700}}]`

### v3_hard_realbudget_eval_000019
- request: 丽江 2026-05-11->2026-05-14 days=4 transport=打车 hotel=亲子酒店 prefs=['亲子', '老人友好', '博物馆', '城市公园', '特色餐厅']
- errors: `[{"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-05-14", "type": "lunch", "name": "云西小锅米线", "reason": "unknown_food_semantics"}]}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 9036, "total": 8036, "diff": 1000, "requested_budget": {"available": true, "amount": 7600, "scope": "total", "party_size": 2, "total": 7600, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "soft"}, "per_person_day": 1004.5, "budget_level": "comfortable", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "soft", "amount": 7600, "target_min_ratio": 0.7, "target_max_ratio": 1.1, "target_min_total": 5300, "target_max_total": 8400, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 2, "room_count": 1, "priced_nights": 3, "expected_min_total_hotels": 3900, "reported_total_hotels": 3900, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 1264, "expected_total_attractions": 2528, "reported_total_attractions": 2678, "meal_per_person_cost_sum": 760, "expected_total_meals": 1520, "reported_total_meals": 1658, "reported_total_transportation": 800}}]`

### v3_hard_realbudget_eval_000020
- request: 杭州 2026-06-21->2026-06-25 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 5, "hotel_room_count": 3, "attraction_ticket_sum": 150, "expected_total_attractions": 750, "reported_total_attractions": 650, "meal_per_person_cost_sum": 1186, "expected_total_meals": 5930, "reported_total_meals": 5950, "reported_total_transportation": 1500}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 5, "hotel_room_count": 3, "attraction_ticket_sum": 150, "expected_total_attractions": 750, "reported_total_attractions": 650, "meal_per_person_cost_sum": 1186, "expected_total_meals": 5930, "reported_total_meals": 5950, "reported_total_transportation": 1500}}]`
