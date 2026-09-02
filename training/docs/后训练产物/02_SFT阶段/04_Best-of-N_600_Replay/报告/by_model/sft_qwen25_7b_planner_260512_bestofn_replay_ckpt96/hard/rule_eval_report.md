# Rule Eval Report: 260511_high_end_context_hard_w10

- records: 300
- generations: `training/outputs/eval/by_model/sft_qwen25_7b_v3_260512_bestofn_replay_ckpt96/260511_high_end_context_hard_w10/generations.jsonl`
- records_path: `training/data/v3/eval_hard/records.jsonl`

## Boolean Metrics

| Metric | Pass | Total | Rate |
| --- | ---: | ---: | ---: |
| accommodation_type_ok | 299 | 299 | 100.00% |
| attraction_budget_consistent | 84 | 299 | 28.09% |
| attraction_budget_party_relation_ok | 291 | 299 | 97.32% |
| attraction_count_ok | 296 | 299 | 99.00% |
| attraction_diversity_ok | 255 | 299 | 85.28% |
| attraction_grounding_ok | 295 | 299 | 98.66% |
| attraction_repeat_limit_ok | 255 | 299 | 85.28% |
| budget_arithmetic_consistent | 188 | 299 | 62.88% |
| budget_consistent | 188 | 299 | 62.88% |
| budget_level_aligned | 200 | 299 | 66.89% |
| budget_preference_aligned | 200 | 299 | 66.89% |
| budget_relationship_ok | 223 | 299 | 74.58% |
| budget_selection_ok | 144 | 299 | 48.16% |
| budget_user_constraint_ok | 247 | 299 | 82.61% |
| budget_within_user_budget | 270 | 299 | 90.30% |
| city_ok | 299 | 299 | 100.00% |
| date_range_ok | 299 | 299 | 100.00% |
| day_dates_ok | 299 | 299 | 100.00% |
| day_index_ok | 299 | 299 | 100.00% |
| days_len_ok | 299 | 299 | 100.00% |
| dpo_soft_pass | 148 | 299 | 49.50% |
| dpo_soft_recomputed_budget_pass | 104 | 299 | 34.78% |
| hard_pass | 289 | 299 | 96.66% |
| hotel_budget_covers_nights | 275 | 299 | 91.97% |
| hotel_budget_relation_ok | 279 | 299 | 93.31% |
| hotel_distance_placeholder_ok | 299 | 299 | 100.00% |
| hotel_grounding_ok | 299 | 299 | 100.00% |
| invalid_hotel_name_ok | 299 | 299 | 100.00% |
| json_extract_ok | 300 | 300 | 100.00% |
| legacy_hard_pass | 148 | 299 | 49.50% |
| location_object_ok | 299 | 299 | 100.00% |
| meal_budget_consistent | 0 | 299 | 0.00% |
| meal_complete | 299 | 299 | 100.00% |
| meal_cost_scale_ok | 242 | 299 | 80.94% |
| meal_diversity_ok | 260 | 299 | 86.96% |
| meal_grounding_ok | 298 | 299 | 99.67% |
| meal_lunch_dinner_same_day_ok | 295 | 299 | 98.66% |
| meal_repeat_limit_ok | 263 | 299 | 87.96% |
| meal_specific_ok | 299 | 299 | 100.00% |
| meal_valid_semantics_ok | 298 | 299 | 99.67% |
| middle_hotel_ok | 299 | 299 | 100.00% |
| recomputed_budget_fit_ok | 144 | 299 | 48.16% |
| recomputed_budget_hard_ok | 212 | 299 | 70.90% |
| recomputed_budget_level_aligned | 144 | 299 | 48.16% |
| recomputed_budget_preference_aligned | 144 | 299 | 48.16% |
| recomputed_budget_user_constraint_ok | 212 | 299 | 70.90% |
| recomputed_budget_within_user_budget | 246 | 299 | 82.27% |
| schema_ok | 299 | 300 | 99.67% |
| sft_budget_semantic_hard_pass | 173 | 299 | 57.86% |
| sft_hard_pass | 289 | 299 | 96.66% |
| sft_no_budget_sum_hard_pass | 289 | 299 | 96.66% |
| sft_strict_hard_pass | 0 | 299 | 0.00% |
| transportation_budget_nonnegative | 299 | 299 | 100.00% |
| weather_dates_ok | 299 | 299 | 100.00% |
| weather_match | 297 | 299 | 99.33% |

## Numeric Metrics

```json
{
  "attraction_diversity_unique_rate": {
    "avg": 0.9822,
    "p50": 1.0,
    "p90": 1.0
  },
  "attraction_grounding_rate": {
    "avg": 0.9987,
    "p50": 1.0,
    "p90": 1.0
  },
  "hotel_grounding_rate": {
    "avg": 1.0,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_diversity_unique_rate": {
    "avg": 0.8954,
    "p50": 0.9333,
    "p90": 1.0
  },
  "meal_food_pois_grounding_rate": {
    "avg": 0.9997,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_grounding_rate": {
    "avg": 0.9997,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_semantic_valid_rate": {
    "avg": 0.9997,
    "p50": 1.0,
    "p90": 1.0
  },
  "recomputed_budget_per_person_day": {
    "avg": 929.4472,
    "p50": 952.25,
    "p90": 1477.56
  },
  "recomputed_budget_total": {
    "avg": 9975.99,
    "p50": 9008.0,
    "p90": 17810.0
  }
}
```

## Failure Types

```json
{
  "meal_budget_inconsistent": 299,
  "attraction_budget_inconsistent": 215,
  "budget_arithmetic_inconsistent": 111,
  "budget_preference_mismatch": 99,
  "budget_relationship_mismatch": 76,
  "meal_cost_scale_too_low": 57,
  "budget_hard_constraint_exceeded": 52,
  "attraction_repeat_too_many": 44,
  "meal_repeat_too_many": 36,
  "hotel_budget_underestimated": 24,
  "meal_same_day_lunch_dinner_repeat": 4,
  "too_many_attractions": 3,
  "weather_mismatch": 2,
  "schema": 1,
  "meal_invalid_name": 1
}
```

## Failure Examples

### v3_hard_realbudget_eval_000004
- request: 张家界 2026-05-11->2026-05-13 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 3968, "total": 3568, "diff": 400, "requested_budget": {"available": true, "amount": 3200, "scope": "total", "party_size": 1, "total": 3200, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "hard"}, "per_person_day": 1189.33, "budget_level": "comfortable", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "hard", "amount": 3200, "target_min_ratio": 0.7, "target_max_ratio": 1.0, "target_min_total": 2200, "target_max_total": 3200, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": false, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 1, "room_count": 1, "priced_nights": 2, "expected_min_total_hotels": 2600, "reported_total_hotels": 2600, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 610, "expected_total_attractions": 610, "reported_total_attractions": 610, "meal_per_person_cost_sum": 694, "expected_total_meals": 694, "reported_total_meals": 558, "reported_total_transportation": 200}}, {"stage": "rule", "type": "budget_hard_constraint_exceeded", "details": {"part_sum": 3968, "total": 3568, "diff": 400, "requested_budget": {"available": true, "amount": 3200, "scope": "total", "party_size": 1, "total": 3200, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "hard"}, "per_person_day": 1189.33, "budget_level": "comfortable", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "hard", "amount": 3200, "target_min_ratio": 0.7, "target_max_ratio": 1.0, "target_min_total": 2200, "target_max_total": 3200, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": false, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 1, "room_count": 1, "priced_nights": 2, "expected_min_total_hotels": 2600, "reported_total_hotels": 2600, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_hard_realbudget_eval_000008
- request: 大理 2026-05-11->2026-05-13 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 8298, "total": 6298, "diff": 2000, "requested_budget": {"available": true, "amount": 8700, "scope": "total", "party_size": 3, "total": 8700, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "hard"}, "per_person_day": 699.78, "budget_level": "comfortable", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "hard", "amount": 8700, "target_min_ratio": 0.7, "target_max_ratio": 1.0, "target_min_total": 6100, "target_max_total": 8700, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 3, "room_count": 2, "priced_nights": 2, "expected_min_total_hotels": 5200, "reported_total_hotels": 5200, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 484, "expected_total_attractions": 1452, "reported_total_attractions": 1656, "meal_per_person_cost_sum": 722, "expected_total_meals": 2166, "reported_total_meals": 1242, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 484, "expected_total_attractions": 1452, "reported_total_attractions": 1656, "meal_per_person_cost_sum": 722, "expected_total_meals": 2166, "reported_total_meals": 1242, "reported_total_transportation": 200}}]`

### v3_hard_realbudget_eval_000006
- request: 南京 2026-07-06->2026-07-09 days=4 transport=自驾 hotel=亲子酒店 prefs=['亲子', '动物园', '海洋馆', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 110, "expected_total_attractions": 330, "reported_total_attractions": 330, "meal_per_person_cost_sum": 858, "expected_total_meals": 2574, "reported_total_meals": 2100, "reported_total_transportation": 800}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": true, "meal_cost_scale_ok": false, "budget_relationship_ok": false, "expected_total_hotels": 8100, "reported_total_hotels": 8100, "expected_total_attractions": 330, "reported_total_attractions": 330, "meal_scale_eval": {"ok": false, "party_total": 3, "budget_level": "standard", "per_person_lunch_dinner_floor": 35, "breakfast_policy": "excluded_from_meal_cost_scale", "meal_count": 12, "checked_count": 8, "failure_count": 1, "failures": [{"date": "2026-07-08", "type": "lunch", "name": "小潘记鸭血粉丝汤", "estimated_cost": 34, "min_expected_cost": 35}]}}}, {"stage": "rule", "type": "meal_cost_scale_too_low", "details": {"ok": false, "party_total": 3, "budget_level": "standard", "per_person_lunch_dinner_floor": 35, "breakfast_policy": "excluded_from_meal_cost_scale", "meal_count": 12, "checked_count": 8, "failure_count": 1, "failures": [{"date": "2026-07-08", "type": "lunch", "name": "小潘记鸭血粉丝汤", "estimated_cost": 34, "min_expected_cost": 35}]}}]`

### v3_hard_realbudget_eval_000001
- request: 桂林 2026-09-04->2026-09-07 days=4 transport=打车 hotel=高端酒店 prefs=['高端酒店', '艺术', '特色餐厅', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "桂林市两江四湖景区", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-09-05", "day_index": 1, "name": "桂林市两江四湖景区"}, {"date": "2026-09-06", "day_index": 2, "name": "桂林市两江四湖景区"}]}]}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 11074, "total": 10074, "diff": 1000, "requested_budget": {"available": true, "amount": 13100, "scope": "total", "party_size": 2, "total": 13100, "source": "budget_constraint", "budget_level": "premium", "strictness": "soft"}, "per_person_day": 1259.25, "budget_level": "premium", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "premium", "strictness": "soft", "amount": 13100, "target_min_ratio": 0.75, "target_max_ratio": 1.12, "target_min_total": 9800, "target_max_total": 14700, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 2, "room_count": 1, "priced_nights": 3, "expected_min_total_hotels": 3900, "reported_total_hotels": 3900, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 835, "expected_total_attractions": 1670, "reported_total_attractions": 1690, "meal_per_person_cost_sum": 987, "expected_total_meals": 1974, "reported_total_meals": 2284, "reported_total_transportation": 3200}}]`

### v3_hard_realbudget_eval_000002
- request: 杭州 2026-05-01->2026-05-04 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '夜市', '老字号', '城市漫步']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 229, "expected_total_attractions": 916, "reported_total_attractions": 836, "meal_per_person_cost_sum": 770, "expected_total_meals": 3080, "reported_total_meals": 2464, "reported_total_transportation": 700}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 229, "expected_total_attractions": 916, "reported_total_attractions": 836, "meal_per_person_cost_sum": 770, "expected_total_meals": 3080, "reported_total_meals": 2464, "reported_total_transportation": 700}}]`

### v3_hard_realbudget_eval_000000
- request: 昆明 2026-04-07->2026-04-11 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 5, "hotel_room_count": 3, "attraction_ticket_sum": 483, "expected_total_attractions": 2415, "reported_total_attractions": 1565, "meal_per_person_cost_sum": 1079, "expected_total_meals": 5395, "reported_total_meals": 5635, "reported_total_transportation": 2800}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 5, "hotel_room_count": 3, "attraction_ticket_sum": 483, "expected_total_attractions": 2415, "reported_total_attractions": 1565, "meal_per_person_cost_sum": 1079, "expected_total_meals": 5395, "reported_total_meals": 5635, "reported_total_transportation": 2800}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": false, "meal_cost_scale_ok": true, "budget_relationship_ok": false, "expected_total_hotels": 7200, "reported_total_hotels": 7200, "expected_total_attractions": 2415, "reported_total_attractions": 1565, "meal_scale_eval": {"ok": true, "party_total": 5, "budget_level": "comfortable", "per_person_lunch_dinner_floor": 50, "breakfast_policy": "excluded_from_meal_cost_scale", "meal_count": 15, "checked_count": 10, "failure_count": 0, "failures": []}}}]`

### v3_hard_realbudget_eval_000003
- request: 西安 2025-05-07->2025-05-11 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 4, "party_total": 2, "room_count": 1, "priced_nights": 4, "expected_min_total_hotels": 1800, "reported_total_hotels": 3600, "diff": 1800, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 399, "expected_total_attractions": 798, "reported_total_attractions": 858, "meal_per_person_cost_sum": 751, "expected_total_meals": 1502, "reported_total_meals": 2044, "reported_total_transportation": 300}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 399, "expected_total_attractions": 798, "reported_total_attractions": 858, "meal_per_person_cost_sum": 751, "expected_total_meals": 1502, "reported_total_meals": 2044, "reported_total_transportation": 300}}]`

### v3_hard_realbudget_eval_000005
- request: 广州 2026-07-06->2026-07-10 days=5 transport=公共交通 hotel=民宿 prefs=['摄影', '自然风光', '城市漫步', '本地菜']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 3050, "total": 2050, "diff": 1000, "requested_budget": {"available": true, "amount": 4500, "scope": "total", "party_size": 1, "total": 4500, "source": "budget_constraint", "budget_level": "standard", "strictness": "hard"}, "per_person_day": 410.0, "budget_level": "standard", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "standard", "strictness": "hard", "amount": 4500, "target_min_ratio": 0.6, "target_max_ratio": 1.0, "target_min_total": 2700, "target_max_total": 4500, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 4, "party_total": 1, "room_count": 1, "priced_nights": 4, "expected_min_total_hotels": 1200, "reported_total_hotels": 1200, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 166, "expected_total_attractions": 166, "reported_total_attractions": 166, "meal_per_person_cost_sum": 1163, "expected_total_meals": 1163, "reported_total_meals": 1384, "reported_total_transportation": 300}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": true, "meal_cost_scale_ok": false, "budget_relationship_ok": false, "expected_total_hotels": 1200, "reported_total_hotels": 1200, "expected_total_attractions": 166, "reported_total_attractions": 166, "meal_scale_eval": {"ok": false, "party_total": 1, "budget_level": "standard", "per_person_lunch_dinner_floor": 35, "breakfast_policy": "excluded_from_meal_cost_scale", "meal_count": 15, "checked_count": 10, "failure_count": 1, "failures": [{"date": "2026-07-07", "type": "lunch", "name": "银记肠粉(北京路店)", "estimated_cost": 23, "min_expected_cost": 35}]}}}]`

### v3_hard_realbudget_eval_000010
- request: 西安 2026-08-05->2026-08-09 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "西安博物院", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-08-05", "day_index": 0, "name": "西安博物院"}, {"date": "2026-08-09", "day_index": 4, "name": "西安博物院"}]}, {"name_key": "兴庆宫公园", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-08-05", "day_index": 0, "name": "兴庆宫公园"}, {"date": "2026-08-09", "day_index": 4, "name": "兴庆宫公园"}]}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 4, "party_total": 5, "room_count": 3, "priced_nights": 4, "expected_min_total_hotels": 16200, "reported_total_hotels": 10800, "diff": -5400, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 5, "hotel_room_count": 3, "attraction_ticket_sum": 919, "expected_total_attractions": 4595, "reported_total_attractions": 4395, "meal_per_person_cost_sum": 784, "expected_total_meals": 3920, "reported_total_meals": 4800, "reported_total_transportation": 2000}}]`

### v3_hard_realbudget_eval_000007
- request: 成都 2026-05-11->2026-05-15 days=5 transport=公共交通 hotel=民宿 prefs=['小众展馆', '咖啡', '艺术', '城市漫步', '特色餐厅']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 1648, "expected_total_attractions": 3296, "reported_total_attractions": 3154, "meal_per_person_cost_sum": 2525, "expected_total_meals": 5050, "reported_total_meals": 4644, "reported_total_transportation": 1000}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 1648, "expected_total_attractions": 3296, "reported_total_attractions": 3154, "meal_per_person_cost_sum": 2525, "expected_total_meals": 5050, "reported_total_meals": 4644, "reported_total_transportation": 1000}}]`

### v3_hard_realbudget_eval_000011
- request: 福州 2026-06-21->2026-06-24 days=4 transport=打车 hotel=高端酒店 prefs=['高端酒店', '艺术', '特色餐厅', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 2, "room_count": 1, "priced_nights": 3, "expected_min_total_hotels": 3900, "reported_total_hotels": 7800, "diff": 3900, "covers_nights": false}}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 12298, "total": 12398, "diff": -100, "requested_budget": {"available": true, "amount": 13500, "scope": "total", "party_size": 2, "total": 13500, "source": "budget_constraint", "budget_level": "premium", "strictness": "soft"}, "per_person_day": 1549.75, "budget_level": "premium", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "premium", "strictness": "soft", "amount": 13500, "target_min_ratio": 0.75, "target_max_ratio": 1.12, "target_min_total": 10100, "target_max_total": 15100, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 2, "room_count": 1, "priced_nights": 3, "expected_min_total_hotels": 3900, "reported_total_hotels": 7800, "diff": 3900, "covers_nights": false}, "hotel_budget_covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 227, "expected_total_attractions": 454, "reported_total_attractions": 494, "meal_per_person_cost_sum": 1491, "expected_total_meals": 2982, "reported_total_meals": 3404, "reported_total_transportation": 600}}]`

### v3_hard_realbudget_eval_000014
- request: 成都 2026-06-06->2026-06-08 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 3988, "total": 4088, "diff": -100, "requested_budget": {"available": true, "amount": 4300, "scope": "total", "party_size": 1, "total": 4300, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "hard"}, "per_person_day": 1362.67, "budget_level": "comfortable", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "hard", "amount": 4300, "target_min_ratio": 0.7, "target_max_ratio": 1.0, "target_min_total": 3000, "target_max_total": 4300, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 1, "room_count": 1, "priced_nights": 2, "expected_min_total_hotels": 2700, "reported_total_hotels": 2700, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 130, "expected_total_attractions": 130, "reported_total_attractions": 130, "meal_per_person_cost_sum": 856, "expected_total_meals": 856, "reported_total_meals": 858, "reported_total_transportation": 300}}]`

### v3_hard_realbudget_eval_000009
- request: 苏州 2026-04-30->2026-05-03 days=4 transport=打车 hotel=亲子酒店 prefs=['亲子', '老人友好', '博物馆', '城市公园', '特色餐厅']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 320, "expected_total_attractions": 1280, "reported_total_attractions": 1440, "meal_per_person_cost_sum": 771, "expected_total_meals": 3084, "reported_total_meals": 3928, "reported_total_transportation": 1200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 320, "expected_total_attractions": 1280, "reported_total_attractions": 1440, "meal_per_person_cost_sum": 771, "expected_total_meals": 3084, "reported_total_meals": 3928, "reported_total_transportation": 1200}}]`

### v3_hard_realbudget_eval_000012
- request: 洛阳 2025-05-07->2025-05-10 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '夜市', '老字号', '城市漫步']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 5136, "total": 4136, "diff": 1000, "requested_budget": {"available": true, "amount": 5800, "scope": "total", "party_size": 4, "total": 5800, "source": "budget_constraint", "budget_level": "limited", "strictness": "hard"}, "per_person_day": 258.5, "budget_level": "limited", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "limited", "strictness": "hard", "amount": 5800, "target_min_ratio": 0.72, "target_max_ratio": 1.0, "target_min_total": 4200, "target_max_total": 5800, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 4, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 1800, "reported_total_hotels": 1800, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 187, "expected_total_attractions": 748, "reported_total_attractions": 708, "meal_per_person_cost_sum": 630, "expected_total_meals": 2520, "reported_total_meals": 1828, "reported_total_transportation": 800}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 187, "expected_total_attractions": 748, "reported_total_attractions": 708, "meal_per_person_cost_sum": 630, "expected_total_meals": 2520, "reported_total_meals": 1828, "reported_total_transportation": 800}}]`

### v3_hard_realbudget_eval_000018
- request: 天津 2026-07-06->2026-07-08 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 2, "party_total": 3, "room_count": 2, "priced_nights": 2, "expected_min_total_hotels": 7200, "reported_total_hotels": 3600, "diff": -3600, "covers_nights": false}}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 10898, "total": 7898, "diff": 3000, "requested_budget": {"available": true, "amount": 7900, "scope": "total", "party_size": 3, "total": 7900, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "hard"}, "per_person_day": 877.56, "budget_level": "comfortable", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "hard", "amount": 7900, "target_min_ratio": 0.7, "target_max_ratio": 1.0, "target_min_total": 5500, "target_max_total": 7900, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 3, "room_count": 2, "priced_nights": 2, "expected_min_total_hotels": 7200, "reported_total_hotels": 3600, "diff": -3600, "covers_nights": false}, "hotel_budget_covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 955, "expected_total_attractions": 2865, "reported_total_attractions": 2793, "meal_per_person_cost_sum": 3189, "expected_total_meals": 9567, "reported_total_meals": 3805, "reported_total_transportation": 700}}]`

### v3_hard_realbudget_eval_000016
- request: 苏州 2026-06-06->2026-06-09 days=4 transport=自驾 hotel=亲子酒店 prefs=['亲子', '动物园', '海洋馆', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 10990, "total": 9990, "diff": 1000, "requested_budget": {"available": true, "amount": 10000, "scope": "total", "party_size": 3, "total": 10000, "source": "budget_constraint", "budget_level": "standard", "strictness": "hard"}, "per_person_day": 832.5, "budget_level": "standard", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "standard", "strictness": "hard", "amount": 10000, "target_min_ratio": 0.6, "target_max_ratio": 1.0, "target_min_total": 6000, "target_max_total": 10000, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 3, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 8100, "reported_total_hotels": 8100, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 420, "expected_total_attractions": 1260, "reported_total_attractions": 1260, "meal_per_person_cost_sum": 883, "expected_total_meals": 2649, "reported_total_meals": 1530, "reported_total_transportation": 100}}]`

### v3_hard_realbudget_eval_000013
- request: 武汉 2026-05-09->2026-05-13 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 223, "expected_total_attractions": 446, "reported_total_attractions": 416, "meal_per_person_cost_sum": 988, "expected_total_meals": 1976, "reported_total_meals": 2204, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 223, "expected_total_attractions": 446, "reported_total_attractions": 416, "meal_per_person_cost_sum": 988, "expected_total_meals": 1976, "reported_total_meals": 2204, "reported_total_transportation": 200}}]`

### v3_hard_realbudget_eval_000019
- request: 丽江 2026-05-11->2026-05-14 days=4 transport=打车 hotel=亲子酒店 prefs=['亲子', '老人友好', '博物馆', '城市公园', '特色餐厅']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "丽江古道藏家博物馆", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-05-12", "day_index": 1, "name": "丽江古道藏家博物馆"}, {"date": "2026-05-13", "day_index": 2, "name": "丽江古道藏家博物馆"}]}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 884, "expected_total_attractions": 1768, "reported_total_attractions": 1878, "meal_per_person_cost_sum": 789, "expected_total_meals": 1578, "reported_total_meals": 1404, "reported_total_transportation": 800}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 884, "expected_total_attractions": 1768, "reported_total_attractions": 1878, "meal_per_person_cost_sum": 789, "expected_total_meals": 1578, "reported_total_meals": 1404, "reported_total_transportation": 800}}]`

### v3_hard_realbudget_eval_000017
- request: 苏州 2026-05-09->2026-05-13 days=5 transport=公共交通 hotel=民宿 prefs=['小众展馆', '咖啡', '艺术', '城市漫步', '特色餐厅']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 6060, "total": 7060, "diff": -1000, "requested_budget": {"available": true, "amount": 10100, "scope": "total", "party_size": 2, "total": 10100, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "soft"}, "per_person_day": 706.0, "budget_level": "comfortable", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "soft", "amount": 10100, "target_min_ratio": 0.7, "target_max_ratio": 1.1, "target_min_total": 7100, "target_max_total": 11100, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 4, "party_total": 2, "room_count": 1, "priced_nights": 4, "expected_min_total_hotels": 1200, "reported_total_hotels": 1200, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 320, "expected_total_attractions": 640, "reported_total_attractions": 730, "meal_per_person_cost_sum": 1115, "expected_total_meals": 2230, "reported_total_meals": 2830, "reported_total_transportation": 1300}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 320, "expected_total_attractions": 640, "reported_total_attractions": 730, "meal_per_person_cost_sum": 1115, "expected_total_meals": 2230, "reported_total_meals": 2830, "reported_total_transportation": 1300}}]`

### v3_hard_realbudget_eval_000021
- request: 上海 2026-06-21->2026-06-24 days=4 transport=打车 hotel=高端酒店 prefs=['高端酒店', '艺术', '特色餐厅', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 1139, "expected_total_attractions": 2278, "reported_total_attractions": 2588, "meal_per_person_cost_sum": 2160, "expected_total_meals": 4320, "reported_total_meals": 4884, "reported_total_transportation": 1000}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 1139, "expected_total_attractions": 2278, "reported_total_attractions": 2588, "meal_per_person_cost_sum": 2160, "expected_total_meals": 4320, "reported_total_meals": 4884, "reported_total_transportation": 1000}}]`
