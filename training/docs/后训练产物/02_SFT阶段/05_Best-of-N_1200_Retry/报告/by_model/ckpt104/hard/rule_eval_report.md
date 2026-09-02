# Rule Eval Report: 260513_bestofn1200_retry_ckpt104_hard_w10

- records: 300
- generations: `training/outputs/eval/by_model/sft_qwen25_7b_v3_260513_bestofn1200_retry_ckpt104/260513_bestofn1200_retry_ckpt104_hard_w10/generations.jsonl`
- records_path: `training/data/v3/eval_hard/records.jsonl`

## Boolean Metrics

| Metric | Pass | Total | Rate |
| --- | ---: | ---: | ---: |
| accommodation_type_ok | 300 | 300 | 100.00% |
| attraction_budget_consistent | 92 | 300 | 30.67% |
| attraction_budget_party_relation_ok | 295 | 300 | 98.33% |
| attraction_count_ok | 296 | 300 | 98.67% |
| attraction_diversity_ok | 257 | 300 | 85.67% |
| attraction_grounding_ok | 298 | 300 | 99.33% |
| attraction_repeat_limit_ok | 257 | 300 | 85.67% |
| budget_arithmetic_consistent | 203 | 300 | 67.67% |
| budget_consistent | 203 | 300 | 67.67% |
| budget_level_aligned | 195 | 300 | 65.00% |
| budget_preference_aligned | 195 | 300 | 65.00% |
| budget_relationship_ok | 233 | 300 | 77.67% |
| budget_selection_ok | 148 | 300 | 49.33% |
| budget_user_constraint_ok | 240 | 300 | 80.00% |
| budget_within_user_budget | 274 | 300 | 91.33% |
| city_ok | 300 | 300 | 100.00% |
| date_range_ok | 300 | 300 | 100.00% |
| day_dates_ok | 300 | 300 | 100.00% |
| day_index_ok | 300 | 300 | 100.00% |
| days_len_ok | 300 | 300 | 100.00% |
| dpo_soft_pass | 145 | 300 | 48.33% |
| dpo_soft_recomputed_budget_pass | 107 | 300 | 35.67% |
| hard_pass | 289 | 300 | 96.33% |
| hotel_budget_covers_nights | 285 | 300 | 95.00% |
| hotel_budget_relation_ok | 289 | 300 | 96.33% |
| hotel_distance_placeholder_ok | 300 | 300 | 100.00% |
| hotel_grounding_ok | 299 | 300 | 99.67% |
| invalid_hotel_name_ok | 300 | 300 | 100.00% |
| json_extract_ok | 300 | 300 | 100.00% |
| legacy_hard_pass | 171 | 300 | 57.00% |
| location_object_ok | 300 | 300 | 100.00% |
| meal_budget_consistent | 0 | 300 | 0.00% |
| meal_complete | 300 | 300 | 100.00% |
| meal_cost_scale_ok | 241 | 300 | 80.33% |
| meal_diversity_ok | 266 | 300 | 88.67% |
| meal_grounding_ok | 297 | 300 | 99.00% |
| meal_lunch_dinner_same_day_ok | 294 | 300 | 98.00% |
| meal_repeat_limit_ok | 272 | 300 | 90.67% |
| meal_specific_ok | 300 | 300 | 100.00% |
| meal_valid_semantics_ok | 297 | 300 | 99.00% |
| middle_hotel_ok | 300 | 300 | 100.00% |
| recomputed_budget_fit_ok | 148 | 300 | 49.33% |
| recomputed_budget_hard_ok | 217 | 300 | 72.33% |
| recomputed_budget_level_aligned | 148 | 300 | 49.33% |
| recomputed_budget_preference_aligned | 148 | 300 | 49.33% |
| recomputed_budget_user_constraint_ok | 217 | 300 | 72.33% |
| recomputed_budget_within_user_budget | 255 | 300 | 85.00% |
| schema_ok | 300 | 300 | 100.00% |
| sft_budget_semantic_hard_pass | 173 | 300 | 57.67% |
| sft_hard_pass | 289 | 300 | 96.33% |
| sft_no_budget_sum_hard_pass | 289 | 300 | 96.33% |
| sft_strict_hard_pass | 0 | 300 | 0.00% |
| transportation_budget_nonnegative | 300 | 300 | 100.00% |
| weather_dates_ok | 300 | 300 | 100.00% |
| weather_match | 299 | 300 | 99.67% |

## Numeric Metrics

```json
{
  "attraction_diversity_unique_rate": {
    "avg": 0.9809,
    "p50": 1.0,
    "p90": 1.0
  },
  "attraction_grounding_rate": {
    "avg": 0.9992,
    "p50": 1.0,
    "p90": 1.0
  },
  "hotel_grounding_rate": {
    "avg": 0.9967,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_diversity_unique_rate": {
    "avg": 0.9101,
    "p50": 0.9333,
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
    "avg": 926.2602,
    "p50": 920.0,
    "p90": 1502.0
  },
  "recomputed_budget_total": {
    "avg": 9838.46,
    "p50": 9038.0,
    "p90": 17272.0
  }
}
```

## Failure Types

```json
{
  "meal_budget_inconsistent": 300,
  "attraction_budget_inconsistent": 208,
  "budget_preference_mismatch": 105,
  "budget_arithmetic_inconsistent": 97,
  "budget_relationship_mismatch": 67,
  "budget_hard_constraint_exceeded": 60,
  "meal_cost_scale_too_low": 59,
  "attraction_repeat_too_many": 43,
  "meal_repeat_too_many": 28,
  "hotel_budget_underestimated": 15,
  "meal_same_day_lunch_dinner_repeat": 6,
  "too_many_attractions": 4,
  "meal_invalid_name": 3,
  "weather_mismatch": 1
}
```

## Failure Examples

### v3_hard_realbudget_eval_000004
- request: 张家界 2026-05-11->2026-05-13 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 744, "expected_total_attractions": 744, "reported_total_attractions": 864, "meal_per_person_cost_sum": 694, "expected_total_meals": 694, "reported_total_meals": 680, "reported_total_transportation": 300}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 744, "expected_total_attractions": 744, "reported_total_attractions": 864, "meal_per_person_cost_sum": 694, "expected_total_meals": 694, "reported_total_meals": 680, "reported_total_transportation": 300}}, {"stage": "rule", "type": "budget_hard_constraint_exceeded", "details": {"part_sum": 4444, "total": 4444, "diff": 0, "requested_budget": {"available": true, "amount": 3200, "scope": "total", "party_size": 1, "total": 3200, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "hard"}, "per_person_day": 1481.33, "budget_level": "comfortable", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "hard", "amount": 3200, "target_min_ratio": 0.7, "target_max_ratio": 1.0, "target_min_total": 2200, "target_max_total": 3200, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": true, "within_user_budget": false, "user_constraint_ok": false, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 1, "room_count": 1, "priced_nights": 2, "expected_min_total_hotels": 2600, "reported_total_hotels": 2600, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_hard_realbudget_eval_000008
- request: 大理 2026-05-11->2026-05-13 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物']
- errors: `[{"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-05-13", "type": "dinner", "name": "洱海大游船", "reason": "unknown_food_semantics"}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 484, "expected_total_attractions": 1452, "reported_total_attractions": 1698, "meal_per_person_cost_sum": 659, "expected_total_meals": 1977, "reported_total_meals": 2079, "reported_total_transportation": 800}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 484, "expected_total_attractions": 1452, "reported_total_attractions": 1698, "meal_per_person_cost_sum": 659, "expected_total_meals": 1977, "reported_total_meals": 2079, "reported_total_transportation": 800}}]`

### v3_hard_realbudget_eval_000006
- request: 南京 2026-07-06->2026-07-09 days=4 transport=自驾 hotel=亲子酒店 prefs=['亲子', '动物园', '海洋馆', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 10130, "total": 9930, "diff": 200, "requested_budget": {"available": true, "amount": 9000, "scope": "total", "party_size": 3, "total": 9000, "source": "budget_constraint", "budget_level": "standard", "strictness": "hard"}, "per_person_day": 827.5, "budget_level": "standard", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "standard", "strictness": "hard", "amount": 9000, "target_min_ratio": 0.6, "target_max_ratio": 1.0, "target_min_total": 5400, "target_max_total": 9000, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": false, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 3, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 8100, "reported_total_hotels": 8100, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 10, "expected_total_attractions": 30, "reported_total_attractions": 30, "meal_per_person_cost_sum": 864, "expected_total_meals": 2592, "reported_total_meals": 1800, "reported_total_transportation": 200}}, {"stage": "rule", "type": "budget_hard_constraint_exceeded", "details": {"part_sum": 10130, "total": 9930, "diff": 200, "requested_budget": {"available": true, "amount": 9000, "scope": "total", "party_size": 3, "total": 9000, "source": "budget_constraint", "budget_level": "standard", "strictness": "hard"}, "per_person_day": 827.5, "budget_level": "standard", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "standard", "strictness": "hard", "amount": 9000, "target_min_ratio": 0.6, "target_max_ratio": 1.0, "target_min_total": 5400, "target_max_total": 9000, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": false, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 3, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 8100, "reported_total_hotels": 8100, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_hard_realbudget_eval_000001
- request: 桂林 2026-09-04->2026-09-07 days=4 transport=打车 hotel=高端酒店 prefs=['高端酒店', '艺术', '特色餐厅', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 705, "expected_total_attractions": 1410, "reported_total_attractions": 1400, "meal_per_person_cost_sum": 939, "expected_total_meals": 1878, "reported_total_meals": 1814, "reported_total_transportation": 800}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 705, "expected_total_attractions": 1410, "reported_total_attractions": 1400, "meal_per_person_cost_sum": 939, "expected_total_meals": 1878, "reported_total_meals": 1814, "reported_total_transportation": 800}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": true, "meal_cost_scale_ok": false, "budget_relationship_ok": false, "expected_total_hotels": 3900, "reported_total_hotels": 3900, "expected_total_attractions": 1410, "reported_total_attractions": 1400, "meal_scale_eval": {"ok": false, "party_total": 2, "budget_level": "premium", "per_person_lunch_dinner_floor": 70, "breakfast_policy": "excluded_from_meal_cost_scale", "meal_count": 12, "checked_count": 8, "failure_count": 3, "failures": [{"date": "2026-09-04", "type": "dinner", "name": "阳朔小渔村.土菜馆(十里画廊戏楼店)", "estimated_cost": 41, "min_expected_cost": 70}, {"date": "2026-09-05", "type": "lunch", "name": "欣桂厨(文明店)", "estimated_cost": 65, "min_expected_cost": 70}, {"date": "2026-09-06", "type": "dinner", "name": "岩洞餐厅.天然岩洞特色菜(千古情店)", "estimated_cost": 66, "min_expected_cost": 70}]}}}]`

### v3_hard_realbudget_eval_000002
- request: 杭州 2026-05-01->2026-05-04 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '夜市', '老字号', '城市漫步']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 229, "expected_total_attractions": 916, "reported_total_attractions": 836, "meal_per_person_cost_sum": 703, "expected_total_meals": 2812, "reported_total_meals": 2604, "reported_total_transportation": 400}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 229, "expected_total_attractions": 916, "reported_total_attractions": 836, "meal_per_person_cost_sum": 703, "expected_total_meals": 2812, "reported_total_meals": 2604, "reported_total_transportation": 400}}]`

### v3_hard_realbudget_eval_000005
- request: 广州 2026-07-06->2026-07-10 days=5 transport=公共交通 hotel=民宿 prefs=['摄影', '自然风光', '城市漫步', '本地菜']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 2985, "total": 3085, "diff": -100, "requested_budget": {"available": true, "amount": 4500, "scope": "total", "party_size": 1, "total": 4500, "source": "budget_constraint", "budget_level": "standard", "strictness": "hard"}, "per_person_day": 617.0, "budget_level": "standard", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "standard", "strictness": "hard", "amount": 4500, "target_min_ratio": 0.6, "target_max_ratio": 1.0, "target_min_total": 2700, "target_max_total": 4500, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 4, "party_total": 1, "room_count": 1, "priced_nights": 4, "expected_min_total_hotels": 1200, "reported_total_hotels": 1200, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 36, "expected_total_attractions": 36, "reported_total_attractions": 36, "meal_per_person_cost_sum": 1156, "expected_total_meals": 1156, "reported_total_meals": 1449, "reported_total_transportation": 300}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": true, "meal_cost_scale_ok": false, "budget_relationship_ok": false, "expected_total_hotels": 1200, "reported_total_hotels": 1200, "expected_total_attractions": 36, "reported_total_attractions": 36, "meal_scale_eval": {"ok": false, "party_total": 1, "budget_level": "standard", "per_person_lunch_dinner_floor": 35, "breakfast_policy": "excluded_from_meal_cost_scale", "meal_count": 15, "checked_count": 10, "failure_count": 1, "failures": [{"date": "2026-07-07", "type": "lunch", "name": "银记肠粉(北京路店)", "estimated_cost": 23, "min_expected_cost": 35}]}}}]`

### v3_hard_realbudget_eval_000000
- request: 昆明 2026-04-07->2026-04-11 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "昆明老街钱王街", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-04-08", "day_index": 1, "name": "昆明老街钱王街"}, {"date": "2026-04-11", "day_index": 4, "name": "昆明老街钱王街"}]}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 5, "hotel_room_count": 3, "attraction_ticket_sum": 573, "expected_total_attractions": 2865, "reported_total_attractions": 2665, "meal_per_person_cost_sum": 749, "expected_total_meals": 3745, "reported_total_meals": 4615, "reported_total_transportation": 1500}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 5, "hotel_room_count": 3, "attraction_ticket_sum": 573, "expected_total_attractions": 2865, "reported_total_attractions": 2665, "meal_per_person_cost_sum": 749, "expected_total_meals": 3745, "reported_total_meals": 4615, "reported_total_transportation": 1500}}]`

### v3_hard_realbudget_eval_000003
- request: 西安 2025-05-07->2025-05-11 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 4, "party_total": 2, "room_count": 1, "priced_nights": 4, "expected_min_total_hotels": 1800, "reported_total_hotels": 3600, "diff": 1800, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 267, "expected_total_attractions": 534, "reported_total_attractions": 606, "meal_per_person_cost_sum": 745, "expected_total_meals": 1490, "reported_total_meals": 1904, "reported_total_transportation": 400}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 267, "expected_total_attractions": 534, "reported_total_attractions": 606, "meal_per_person_cost_sum": 745, "expected_total_meals": 1490, "reported_total_meals": 1904, "reported_total_transportation": 400}}]`

### v3_hard_realbudget_eval_000007
- request: 成都 2026-05-11->2026-05-15 days=5 transport=公共交通 hotel=民宿 prefs=['小众展馆', '咖啡', '艺术', '城市漫步', '特色餐厅']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "梨园会馆-非遗川剧变脸演出", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-05-11", "day_index": 0, "name": "梨园会馆-非遗川剧变脸演出(文殊院店)"}, {"date": "2026-05-14", "day_index": 3, "name": "梨园会馆-非遗川剧变脸演出(文殊院店)"}]}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "悦百味·品质川菜", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-05-11", "type": "lunch", "name": "悦百味·品质川菜(优品道店)"}, {"date": "2026-05-12", "type": "lunch", "name": "悦百味·品质川菜(悠方店)"}, {"date": "2026-05-13", "type": "lunch", "name": "悦百味·品质川菜(成都环贸ICD店)"}, {"date": "2026-05-14", "type": "lunch", "name": "悦百味·品质川菜(UPARK公园店)"}]}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 1395, "expected_total_attractions": 2790, "reported_total_attractions": 2604, "meal_per_person_cost_sum": 2324, "expected_total_meals": 4648, "reported_total_meals": 5622, "reported_total_transportation": 500}}]`

### v3_hard_realbudget_eval_000010
- request: 西安 2026-08-05->2026-08-09 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 5, "hotel_room_count": 3, "attraction_ticket_sum": 919, "expected_total_attractions": 4595, "reported_total_attractions": 4140, "meal_per_person_cost_sum": 796, "expected_total_meals": 3980, "reported_total_meals": 3660, "reported_total_transportation": 600}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 5, "hotel_room_count": 3, "attraction_ticket_sum": 919, "expected_total_attractions": 4595, "reported_total_attractions": 4140, "meal_per_person_cost_sum": 796, "expected_total_meals": 3980, "reported_total_meals": 3660, "reported_total_transportation": 600}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": true, "meal_cost_scale_ok": false, "budget_relationship_ok": false, "expected_total_hotels": 16200, "reported_total_hotels": 16200, "expected_total_attractions": 4595, "reported_total_attractions": 4140, "meal_scale_eval": {"ok": false, "party_total": 5, "budget_level": "comfortable", "per_person_lunch_dinner_floor": 50, "breakfast_policy": "excluded_from_meal_cost_scale", "meal_count": 15, "checked_count": 10, "failure_count": 2, "failures": [{"date": "2026-08-07", "type": "lunch", "name": "虎子水盆羊肉(翠华路总店)", "estimated_cost": 43, "min_expected_cost": 50}, {"date": "2026-08-08", "type": "dinner", "name": "果渊斋老米家泡馍馆(回坊总店)", "estimated_cost": 31, "min_expected_cost": 50}]}}}]`

### v3_hard_realbudget_eval_000014
- request: 成都 2026-06-06->2026-06-08 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆']
- errors: `[{"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 266, "expected_total_attractions": 266, "reported_total_attractions": 266, "meal_per_person_cost_sum": 1981, "expected_total_meals": 1981, "reported_total_meals": 1957, "reported_total_transportation": 300}}, {"stage": "rule", "type": "budget_hard_constraint_exceeded", "details": {"part_sum": 5223, "total": 5223, "diff": 0, "requested_budget": {"available": true, "amount": 4300, "scope": "total", "party_size": 1, "total": 4300, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "hard"}, "per_person_day": 1741.0, "budget_level": "comfortable", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "hard", "amount": 4300, "target_min_ratio": 0.7, "target_max_ratio": 1.0, "target_min_total": 3000, "target_max_total": 4300, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": true, "within_user_budget": true, "user_constraint_ok": false, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 1, "room_count": 1, "priced_nights": 2, "expected_min_total_hotels": 2700, "reported_total_hotels": 2700, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "budget_preference_mismatch", "details": {"part_sum": 5223, "total": 5223, "diff": 0, "requested_budget": {"available": true, "amount": 4300, "scope": "total", "party_size": 1, "total": 4300, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "hard"}, "per_person_day": 1741.0, "budget_level": "comfortable", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "hard", "amount": 4300, "target_min_ratio": 0.7, "target_max_ratio": 1.0, "target_min_total": 3000, "target_max_total": 4300, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": true, "within_user_budget": true, "user_constraint_ok": false, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 1, "room_count": 1, "priced_nights": 2, "expected_min_total_hotels": 2700, "reported_total_hotels": 2700, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_hard_realbudget_eval_000011
- request: 福州 2026-06-21->2026-06-24 days=4 transport=打车 hotel=高端酒店 prefs=['高端酒店', '艺术', '特色餐厅', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-06-24", "lunch": "紫阳海鲜楼·传承闽味(华林路店)", "dinner": "紫阳海鲜楼·传承闽味(金洲南路店)"}]}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 9098, "total": 10100, "diff": -1002, "requested_budget": {"available": true, "amount": 13500, "scope": "total", "party_size": 2, "total": 13500, "source": "budget_constraint", "budget_level": "premium", "strictness": "soft"}, "per_person_day": 1262.5, "budget_level": "premium", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "premium", "strictness": "soft", "amount": 13500, "target_min_ratio": 0.75, "target_max_ratio": 1.12, "target_min_total": 10100, "target_max_total": 15100, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 2, "room_count": 1, "priced_nights": 3, "expected_min_total_hotels": 3900, "reported_total_hotels": 3900, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 327, "expected_total_attractions": 654, "reported_total_attractions": 674, "meal_per_person_cost_sum": 1542, "expected_total_meals": 3084, "reported_total_meals": 3524, "reported_total_transportation": 1000}}]`

### v3_hard_realbudget_eval_000009
- request: 苏州 2026-04-30->2026-05-03 days=4 transport=打车 hotel=亲子酒店 prefs=['亲子', '老人友好', '博物馆', '城市公园', '特色餐厅']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 320, "expected_total_attractions": 1280, "reported_total_attractions": 1440, "meal_per_person_cost_sum": 699, "expected_total_meals": 2796, "reported_total_meals": 3248, "reported_total_transportation": 1000}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 320, "expected_total_attractions": 1280, "reported_total_attractions": 1440, "meal_per_person_cost_sum": 699, "expected_total_meals": 2796, "reported_total_meals": 3248, "reported_total_transportation": 1000}}]`

### v3_hard_realbudget_eval_000012
- request: 洛阳 2025-05-07->2025-05-10 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '夜市', '老字号', '城市漫步']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 298, "expected_total_attractions": 1192, "reported_total_attractions": 1208, "meal_per_person_cost_sum": 585, "expected_total_meals": 2340, "reported_total_meals": 2000, "reported_total_transportation": 800}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 298, "expected_total_attractions": 1192, "reported_total_attractions": 1208, "meal_per_person_cost_sum": 585, "expected_total_meals": 2340, "reported_total_meals": 2000, "reported_total_transportation": 800}}, {"stage": "rule", "type": "budget_hard_constraint_exceeded", "details": {"part_sum": 5808, "total": 5808, "diff": 0, "requested_budget": {"available": true, "amount": 5800, "scope": "total", "party_size": 4, "total": 5800, "source": "budget_constraint", "budget_level": "limited", "strictness": "hard"}, "per_person_day": 363.0, "budget_level": "limited", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "limited", "strictness": "hard", "amount": 5800, "target_min_ratio": 0.72, "target_max_ratio": 1.0, "target_min_total": 4200, "target_max_total": 5800, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": true, "within_user_budget": true, "user_constraint_ok": false, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 4, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 1800, "reported_total_hotels": 1800, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_hard_realbudget_eval_000018
- request: 天津 2026-07-06->2026-07-08 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 775, "expected_total_attractions": 2325, "reported_total_attractions": 2595, "meal_per_person_cost_sum": 3173, "expected_total_meals": 9519, "reported_total_meals": 5829, "reported_total_transportation": 400}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 775, "expected_total_attractions": 2325, "reported_total_attractions": 2595, "meal_per_person_cost_sum": 3173, "expected_total_meals": 9519, "reported_total_meals": 5829, "reported_total_transportation": 400}}, {"stage": "rule", "type": "budget_hard_constraint_exceeded", "details": {"part_sum": 16024, "total": 16024, "diff": 0, "requested_budget": {"available": true, "amount": 7900, "scope": "total", "party_size": 3, "total": 7900, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "hard"}, "per_person_day": 1780.44, "budget_level": "comfortable", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "hard", "amount": 7900, "target_min_ratio": 0.7, "target_max_ratio": 1.0, "target_min_total": 5500, "target_max_total": 7900, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": true, "within_user_budget": false, "user_constraint_ok": false, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 3, "room_count": 2, "priced_nights": 2, "expected_min_total_hotels": 7200, "reported_total_hotels": 7200, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_hard_realbudget_eval_000016
- request: 苏州 2026-06-06->2026-06-09 days=4 transport=自驾 hotel=亲子酒店 prefs=['亲子', '动物园', '海洋馆', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 140, "expected_total_attractions": 420, "reported_total_attractions": 450, "meal_per_person_cost_sum": 609, "expected_total_meals": 1827, "reported_total_meals": 2148, "reported_total_transportation": 800}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 140, "expected_total_attractions": 420, "reported_total_attractions": 450, "meal_per_person_cost_sum": 609, "expected_total_meals": 1827, "reported_total_meals": 2148, "reported_total_transportation": 800}}, {"stage": "rule", "type": "budget_hard_constraint_exceeded", "details": {"part_sum": 11498, "total": 11498, "diff": 0, "requested_budget": {"available": true, "amount": 10000, "scope": "total", "party_size": 3, "total": 10000, "source": "budget_constraint", "budget_level": "standard", "strictness": "hard"}, "per_person_day": 958.17, "budget_level": "standard", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "standard", "strictness": "hard", "amount": 10000, "target_min_ratio": 0.6, "target_max_ratio": 1.0, "target_min_total": 6000, "target_max_total": 10000, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": true, "within_user_budget": true, "user_constraint_ok": false, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 3, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 8100, "reported_total_hotels": 8100, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_hard_realbudget_eval_000013
- request: 武汉 2026-05-09->2026-05-13 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 163, "expected_total_attractions": 326, "reported_total_attractions": 316, "meal_per_person_cost_sum": 1004, "expected_total_meals": 2008, "reported_total_meals": 2504, "reported_total_transportation": 400}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 163, "expected_total_attractions": 326, "reported_total_attractions": 316, "meal_per_person_cost_sum": 1004, "expected_total_meals": 2008, "reported_total_meals": 2504, "reported_total_transportation": 400}}]`

### v3_hard_realbudget_eval_000019
- request: 丽江 2026-05-11->2026-05-14 days=4 transport=打车 hotel=亲子酒店 prefs=['亲子', '老人友好', '博物馆', '城市公园', '特色餐厅']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 984, "expected_total_attractions": 1968, "reported_total_attractions": 2108, "meal_per_person_cost_sum": 727, "expected_total_meals": 1454, "reported_total_meals": 1404, "reported_total_transportation": 800}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 984, "expected_total_attractions": 1968, "reported_total_attractions": 2108, "meal_per_person_cost_sum": 727, "expected_total_meals": 1454, "reported_total_meals": 1404, "reported_total_transportation": 800}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": true, "meal_cost_scale_ok": false, "budget_relationship_ok": false, "expected_total_hotels": 3900, "reported_total_hotels": 3900, "expected_total_attractions": 1968, "reported_total_attractions": 2108, "meal_scale_eval": {"ok": false, "party_total": 2, "budget_level": "comfortable", "per_person_lunch_dinner_floor": 50, "breakfast_policy": "excluded_from_meal_cost_scale", "meal_count": 12, "checked_count": 8, "failure_count": 1, "failures": [{"date": "2026-05-11", "type": "dinner", "name": "云老官保山火塘牛肉(丽江总店)", "estimated_cost": 34, "min_expected_cost": 50}]}}}]`

### v3_hard_realbudget_eval_000020
- request: 杭州 2026-06-21->2026-06-25 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 5, "hotel_room_count": 3, "attraction_ticket_sum": 160, "expected_total_attractions": 800, "reported_total_attractions": 750, "meal_per_person_cost_sum": 1191, "expected_total_meals": 5955, "reported_total_meals": 5950, "reported_total_transportation": 1000}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 5, "hotel_room_count": 3, "attraction_ticket_sum": 160, "expected_total_attractions": 800, "reported_total_attractions": 750, "meal_per_person_cost_sum": 1191, "expected_total_meals": 5955, "reported_total_meals": 5950, "reported_total_transportation": 1000}}]`

### v3_hard_realbudget_eval_000017
- request: 苏州 2026-05-09->2026-05-13 days=5 transport=公共交通 hotel=民宿 prefs=['小众展馆', '咖啡', '艺术', '城市漫步', '特色餐厅']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 775, "expected_total_attractions": 1550, "reported_total_attractions": 1678, "meal_per_person_cost_sum": 1502, "expected_total_meals": 3004, "reported_total_meals": 3844, "reported_total_transportation": 400}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 775, "expected_total_attractions": 1550, "reported_total_attractions": 1678, "meal_per_person_cost_sum": 1502, "expected_total_meals": 3004, "reported_total_meals": 3844, "reported_total_transportation": 400}}]`
