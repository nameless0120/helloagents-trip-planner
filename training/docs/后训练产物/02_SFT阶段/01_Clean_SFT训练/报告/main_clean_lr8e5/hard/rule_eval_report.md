# Rule Eval Report: 260511_high_end_context_hard_w10

- records: 300
- generations: `training/outputs/eval/by_model/sft_qwen25_7b_v3_260509_main_clean_cp2_v2b_valloss_lr8e5/260511_high_end_context_hard_w10/generations.jsonl`
- records_path: `training/data/v3/eval_hard/records.jsonl`

## Boolean Metrics

| Metric | Pass | Total | Rate |
| --- | ---: | ---: | ---: |
| accommodation_type_ok | 299 | 299 | 100.00% |
| attraction_budget_consistent | 46 | 299 | 15.38% |
| attraction_budget_party_relation_ok | 244 | 299 | 81.61% |
| attraction_count_ok | 295 | 299 | 98.66% |
| attraction_diversity_ok | 236 | 299 | 78.93% |
| attraction_grounding_ok | 288 | 299 | 96.32% |
| attraction_repeat_limit_ok | 236 | 299 | 78.93% |
| budget_arithmetic_consistent | 197 | 299 | 65.89% |
| budget_consistent | 197 | 299 | 65.89% |
| budget_level_aligned | 217 | 299 | 72.58% |
| budget_preference_aligned | 217 | 299 | 72.58% |
| budget_relationship_ok | 135 | 299 | 45.15% |
| budget_selection_ok | 161 | 299 | 53.85% |
| budget_user_constraint_ok | 261 | 299 | 87.29% |
| budget_within_user_budget | 274 | 299 | 91.64% |
| city_ok | 299 | 299 | 100.00% |
| date_range_ok | 299 | 299 | 100.00% |
| day_dates_ok | 299 | 299 | 100.00% |
| day_index_ok | 299 | 299 | 100.00% |
| days_len_ok | 299 | 299 | 100.00% |
| dpo_soft_pass | 138 | 299 | 46.15% |
| dpo_soft_recomputed_budget_pass | 105 | 299 | 35.12% |
| hard_pass | 275 | 299 | 91.97% |
| hotel_budget_covers_nights | 219 | 299 | 73.24% |
| hotel_budget_relation_ok | 223 | 299 | 74.58% |
| hotel_distance_placeholder_ok | 299 | 299 | 100.00% |
| hotel_grounding_ok | 298 | 299 | 99.67% |
| invalid_hotel_name_ok | 299 | 299 | 100.00% |
| json_extract_ok | 299 | 300 | 99.67% |
| legacy_hard_pass | 135 | 299 | 45.15% |
| location_object_ok | 299 | 299 | 100.00% |
| meal_budget_consistent | 0 | 299 | 0.00% |
| meal_complete | 299 | 299 | 100.00% |
| meal_cost_scale_ok | 205 | 299 | 68.56% |
| meal_diversity_ok | 263 | 299 | 87.96% |
| meal_grounding_ok | 291 | 299 | 97.32% |
| meal_lunch_dinner_same_day_ok | 289 | 299 | 96.66% |
| meal_repeat_limit_ok | 270 | 299 | 90.30% |
| meal_specific_ok | 299 | 299 | 100.00% |
| meal_valid_semantics_ok | 296 | 299 | 99.00% |
| middle_hotel_ok | 299 | 299 | 100.00% |
| recomputed_budget_fit_ok | 161 | 299 | 53.85% |
| recomputed_budget_hard_ok | 224 | 299 | 74.92% |
| recomputed_budget_level_aligned | 161 | 299 | 53.85% |
| recomputed_budget_preference_aligned | 161 | 299 | 53.85% |
| recomputed_budget_user_constraint_ok | 224 | 299 | 74.92% |
| recomputed_budget_within_user_budget | 254 | 299 | 84.95% |
| schema_ok | 299 | 300 | 99.67% |
| sft_budget_semantic_hard_pass | 94 | 299 | 31.44% |
| sft_hard_pass | 275 | 299 | 91.97% |
| sft_no_budget_sum_hard_pass | 275 | 299 | 91.97% |
| sft_strict_hard_pass | 0 | 299 | 0.00% |
| transportation_budget_nonnegative | 299 | 299 | 100.00% |
| weather_dates_ok | 299 | 299 | 100.00% |
| weather_match | 299 | 299 | 100.00% |

## Numeric Metrics

```json
{
  "attraction_diversity_unique_rate": {
    "avg": 0.9743,
    "p50": 1.0,
    "p90": 1.0
  },
  "attraction_grounding_rate": {
    "avg": 0.9957,
    "p50": 1.0,
    "p90": 1.0
  },
  "hotel_grounding_rate": {
    "avg": 0.9967,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_diversity_unique_rate": {
    "avg": 0.864,
    "p50": 0.8889,
    "p90": 1.0
  },
  "meal_food_pois_grounding_rate": {
    "avg": 0.9978,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_grounding_rate": {
    "avg": 0.9978,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_semantic_valid_rate": {
    "avg": 0.9991,
    "p50": 1.0,
    "p90": 1.0
  },
  "recomputed_budget_per_person_day": {
    "avg": 890.9716,
    "p50": 906.0,
    "p90": 1439.0
  },
  "recomputed_budget_total": {
    "avg": 9578.5117,
    "p50": 8400.0,
    "p90": 17308.0
  }
}
```

## Failure Types

```json
{
  "meal_budget_inconsistent": 299,
  "attraction_budget_inconsistent": 253,
  "budget_relationship_mismatch": 164,
  "budget_arithmetic_inconsistent": 102,
  "meal_cost_scale_too_low": 94,
  "budget_preference_mismatch": 82,
  "hotel_budget_underestimated": 80,
  "attraction_repeat_too_many": 63,
  "budget_hard_constraint_exceeded": 38,
  "meal_repeat_too_many": 29,
  "meal_same_day_lunch_dinner_repeat": 10,
  "meal_grounding_miss": 5,
  "too_many_attractions": 4,
  "meal_invalid_name": 3,
  "json_extract": 1
}
```

## Failure Examples

### v3_hard_realbudget_eval_000004
- request: 张家界 2026-05-11->2026-05-13 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 3558, "total": 2858, "diff": 700, "requested_budget": {"available": true, "amount": 3200, "scope": "total", "party_size": 1, "total": 3200, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "hard"}, "per_person_day": 952.67, "budget_level": "comfortable", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "hard", "amount": 3200, "target_min_ratio": 0.7, "target_max_ratio": 1.0, "target_min_total": 2200, "target_max_total": 3200, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 1, "room_count": 1, "priced_nights": 2, "expected_min_total_hotels": 2600, "reported_total_hotels": 2600, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 160, "expected_total_attractions": 160, "reported_total_attractions": 160, "meal_per_person_cost_sum": 759, "expected_total_meals": 759, "reported_total_meals": 698, "reported_total_transportation": 100}}]`

### v3_hard_realbudget_eval_000008
- request: 大理 2026-05-11->2026-05-13 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 567, "expected_total_attractions": 1701, "reported_total_attractions": 1533, "meal_per_person_cost_sum": 669, "expected_total_meals": 2007, "reported_total_meals": 2256, "reported_total_transportation": 400}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 567, "expected_total_attractions": 1701, "reported_total_attractions": 1533, "meal_per_person_cost_sum": 669, "expected_total_meals": 2007, "reported_total_meals": 2256, "reported_total_transportation": 400}}, {"stage": "rule", "type": "budget_hard_constraint_exceeded", "details": {"part_sum": 9389, "total": 9389, "diff": 0, "requested_budget": {"available": true, "amount": 8700, "scope": "total", "party_size": 3, "total": 8700, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "hard"}, "per_person_day": 1043.22, "budget_level": "comfortable", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "hard", "amount": 8700, "target_min_ratio": 0.7, "target_max_ratio": 1.0, "target_min_total": 6100, "target_max_total": 8700, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": true, "within_user_budget": true, "user_constraint_ok": false, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 3, "room_count": 2, "priced_nights": 2, "expected_min_total_hotels": 5200, "reported_total_hotels": 5200, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_hard_realbudget_eval_000006
- request: 南京 2026-07-06->2026-07-09 days=4 transport=自驾 hotel=亲子酒店 prefs=['亲子', '动物园', '海洋馆', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 3, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 8100, "reported_total_hotels": 7050, "diff": -1050, "covers_nights": false}}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 8902, "total": 8802, "diff": 100, "requested_budget": {"available": true, "amount": 9000, "scope": "total", "party_size": 3, "total": 9000, "source": "budget_constraint", "budget_level": "standard", "strictness": "hard"}, "per_person_day": 733.5, "budget_level": "standard", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "standard", "strictness": "hard", "amount": 9000, "target_min_ratio": 0.6, "target_max_ratio": 1.0, "target_min_total": 5400, "target_max_total": 9000, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 3, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 8100, "reported_total_hotels": 7050, "diff": -1050, "covers_nights": false}, "hotel_budget_covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 165, "expected_total_attractions": 495, "reported_total_attractions": 360, "meal_per_person_cost_sum": 655, "expected_total_meals": 1965, "reported_total_meals": 1392, "reported_total_transportation": 100}}]`

### v3_hard_realbudget_eval_000001
- request: 桂林 2026-09-04->2026-09-07 days=4 transport=打车 hotel=高端酒店 prefs=['高端酒店', '艺术', '特色餐厅', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 2, "room_count": 1, "priced_nights": 3, "expected_min_total_hotels": 3900, "reported_total_hotels": 7800, "diff": 3900, "covers_nights": false}}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 12427, "total": 11427, "diff": 1000, "requested_budget": {"available": true, "amount": 13100, "scope": "total", "party_size": 2, "total": 13100, "source": "budget_constraint", "budget_level": "premium", "strictness": "soft"}, "per_person_day": 1428.38, "budget_level": "premium", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "premium", "strictness": "soft", "amount": 13100, "target_min_ratio": 0.75, "target_max_ratio": 1.12, "target_min_total": 9800, "target_max_total": 14700, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 2, "room_count": 1, "priced_nights": 3, "expected_min_total_hotels": 3900, "reported_total_hotels": 7800, "diff": 3900, "covers_nights": false}, "hotel_budget_covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 1016, "expected_total_attractions": 2032, "reported_total_attractions": 1671, "meal_per_person_cost_sum": 877, "expected_total_meals": 1754, "reported_total_meals": 1956, "reported_total_transportation": 1000}}]`

### v3_hard_realbudget_eval_000002
- request: 杭州 2026-05-01->2026-05-04 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '夜市', '老字号', '城市漫步']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 5100, "total": 4900, "diff": 200, "requested_budget": {"available": true, "amount": 6300, "scope": "total", "party_size": 4, "total": 6300, "source": "budget_constraint", "budget_level": "limited", "strictness": "hard"}, "per_person_day": 306.25, "budget_level": "limited", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "limited", "strictness": "hard", "amount": 6300, "target_min_ratio": 0.72, "target_max_ratio": 1.0, "target_min_total": 4500, "target_max_total": 6300, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 4, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 1500, "reported_total_hotels": 1500, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 179, "expected_total_attractions": 716, "reported_total_attractions": 616, "meal_per_person_cost_sum": 691, "expected_total_meals": 2764, "reported_total_meals": 2484, "reported_total_transportation": 500}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 179, "expected_total_attractions": 716, "reported_total_attractions": 616, "meal_per_person_cost_sum": 691, "expected_total_meals": 2764, "reported_total_meals": 2484, "reported_total_transportation": 500}}]`

### v3_hard_realbudget_eval_000005
- request: 广州 2026-07-06->2026-07-10 days=5 transport=公共交通 hotel=民宿 prefs=['摄影', '自然风光', '城市漫步', '本地菜']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 36, "expected_total_attractions": 36, "reported_total_attractions": 56, "meal_per_person_cost_sum": 1196, "expected_total_meals": 1196, "reported_total_meals": 1394, "reported_total_transportation": 600}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 36, "expected_total_attractions": 36, "reported_total_attractions": 56, "meal_per_person_cost_sum": 1196, "expected_total_meals": 1196, "reported_total_meals": 1394, "reported_total_transportation": 600}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": false, "meal_cost_scale_ok": true, "budget_relationship_ok": false, "expected_total_hotels": 1200, "reported_total_hotels": 1200, "expected_total_attractions": 36, "reported_total_attractions": 56, "meal_scale_eval": {"ok": true, "party_total": 1, "budget_level": "standard", "per_person_lunch_dinner_floor": 35, "breakfast_policy": "excluded_from_meal_cost_scale", "meal_count": 15, "checked_count": 10, "failure_count": 0, "failures": []}}}]`

### v3_hard_realbudget_eval_000007
- request: 成都 2026-05-11->2026-05-15 days=5 transport=公共交通 hotel=民宿 prefs=['小众展馆', '咖啡', '艺术', '城市漫步', '特色餐厅']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "观锦餐厅", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-05-12", "type": "dinner", "name": "观锦餐厅(德商国际店)"}, {"date": "2026-05-13", "type": "dinner", "name": "观锦餐厅(天府新谷店)"}, {"date": "2026-05-14", "type": "lunch", "name": "观锦餐厅(天廊店)"}, {"date": "2026-05-15", "type": "dinner", "name": "观锦餐厅(德商国际店)"}]}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 566, "expected_total_attractions": 1132, "reported_total_attractions": 1350, "meal_per_person_cost_sum": 2582, "expected_total_meals": 5164, "reported_total_meals": 4800, "reported_total_transportation": 450}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 566, "expected_total_attractions": 1132, "reported_total_attractions": 1350, "meal_per_person_cost_sum": 2582, "expected_total_meals": 5164, "reported_total_meals": 4800, "reported_total_transportation": 450}}]`

### v3_hard_realbudget_eval_000010
- request: 西安 2026-08-05->2026-08-09 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "西安博物院", "count": 3, "max_allowed": 1, "occurrences": [{"date": "2026-08-07", "day_index": 2, "name": "西安博物院"}, {"date": "2026-08-08", "day_index": 3, "name": "西安博物院"}, {"date": "2026-08-09", "day_index": 4, "name": "西安博物院"}]}, {"name_key": "兴庆宫公园", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-08-07", "day_index": 2, "name": "兴庆宫公园"}, {"date": "2026-08-09", "day_index": 4, "name": "兴庆宫公园"}]}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 4, "party_total": 5, "room_count": 3, "priced_nights": 4, "expected_min_total_hotels": 16200, "reported_total_hotels": 10800, "diff": -5400, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 5, "hotel_room_count": 3, "attraction_ticket_sum": 319, "expected_total_attractions": 1595, "reported_total_attractions": 2250, "meal_per_person_cost_sum": 702, "expected_total_meals": 3510, "reported_total_meals": 3600, "reported_total_transportation": 5000}}]`

### v3_hard_realbudget_eval_000000
- request: 昆明 2026-04-07->2026-04-11 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 4, "party_total": 5, "room_count": 3, "priced_nights": 4, "expected_min_total_hotels": 7200, "reported_total_hotels": 4800, "diff": -2400, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 5, "hotel_room_count": 3, "attraction_ticket_sum": 278, "expected_total_attractions": 1390, "reported_total_attractions": 1265, "meal_per_person_cost_sum": 851, "expected_total_meals": 4255, "reported_total_meals": 3850, "reported_total_transportation": 7400}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 5, "hotel_room_count": 3, "attraction_ticket_sum": 278, "expected_total_attractions": 1390, "reported_total_attractions": 1265, "meal_per_person_cost_sum": 851, "expected_total_meals": 4255, "reported_total_meals": 3850, "reported_total_transportation": 7400}}]`

### v3_hard_realbudget_eval_000003
- request: 西安 2025-05-07->2025-05-11 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "兴庆宫公园", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2025-05-07", "day_index": 0, "name": "兴庆宫公园"}, {"date": "2025-05-10", "day_index": 3, "name": "兴庆宫公园"}]}, {"name_key": "西安钟楼", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2025-05-08", "day_index": 1, "name": "西安钟楼"}, {"date": "2025-05-11", "day_index": 4, "name": "西安钟楼"}]}, {"name_key": "西安博物院", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2025-05-10", "day_index": 3, "name": "西安博物院"}, {"date": "2025-05-11", "day_index": 4, "name": "西安博物院"}]}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 4, "party_total": 2, "room_count": 1, "priced_nights": 4, "expected_min_total_hotels": 1800, "reported_total_hotels": 3600, "diff": 1800, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 349, "expected_total_attractions": 698, "reported_total_attractions": 658, "meal_per_person_cost_sum": 634, "expected_total_meals": 1268, "reported_total_meals": 1678, "reported_total_transportation": 200}}]`

### v3_hard_realbudget_eval_000011
- request: 福州 2026-06-21->2026-06-24 days=4 transport=打车 hotel=高端酒店 prefs=['高端酒店', '艺术', '特色餐厅', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "福建博物院", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-06-22", "day_index": 1, "name": "福建博物院"}, {"date": "2026-06-24", "day_index": 3, "name": "福建博物院"}]}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 2, "room_count": 1, "priced_nights": 3, "expected_min_total_hotels": 3900, "reported_total_hotels": 7800, "diff": 3900, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 117, "expected_total_attractions": 234, "reported_total_attractions": 204, "meal_per_person_cost_sum": 1810, "expected_total_meals": 3620, "reported_total_meals": 4594, "reported_total_transportation": 1000}}]`

### v3_hard_realbudget_eval_000014
- request: 成都 2026-06-06->2026-06-08 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆']
- errors: `[{"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 130, "expected_total_attractions": 130, "reported_total_attractions": 130, "meal_per_person_cost_sum": 1329, "expected_total_meals": 1329, "reported_total_meals": 1383, "reported_total_transportation": 300}}, {"stage": "rule", "type": "budget_hard_constraint_exceeded", "details": {"part_sum": 4513, "total": 4513, "diff": 0, "requested_budget": {"available": true, "amount": 4300, "scope": "total", "party_size": 1, "total": 4300, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "hard"}, "per_person_day": 1504.33, "budget_level": "comfortable", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "hard", "amount": 4300, "target_min_ratio": 0.7, "target_max_ratio": 1.0, "target_min_total": 3000, "target_max_total": 4300, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": true, "within_user_budget": true, "user_constraint_ok": false, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 1, "room_count": 1, "priced_nights": 2, "expected_min_total_hotels": 2700, "reported_total_hotels": 2700, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "budget_preference_mismatch", "details": {"part_sum": 4513, "total": 4513, "diff": 0, "requested_budget": {"available": true, "amount": 4300, "scope": "total", "party_size": 1, "total": 4300, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "hard"}, "per_person_day": 1504.33, "budget_level": "comfortable", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "hard", "amount": 4300, "target_min_ratio": 0.7, "target_max_ratio": 1.0, "target_min_total": 3000, "target_max_total": 4300, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": true, "within_user_budget": true, "user_constraint_ok": false, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 1, "room_count": 1, "priced_nights": 2, "expected_min_total_hotels": 2700, "reported_total_hotels": 2700, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_hard_realbudget_eval_000009
- request: 苏州 2026-04-30->2026-05-03 days=4 transport=打车 hotel=亲子酒店 prefs=['亲子', '老人友好', '博物馆', '城市公园', '特色餐厅']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 4, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 8100, "reported_total_hotels": 10800, "diff": 2700, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 140, "expected_total_attractions": 560, "reported_total_attractions": 520, "meal_per_person_cost_sum": 843, "expected_total_meals": 3372, "reported_total_meals": 2948, "reported_total_transportation": 1200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 140, "expected_total_attractions": 560, "reported_total_attractions": 520, "meal_per_person_cost_sum": 843, "expected_total_meals": 3372, "reported_total_meals": 2948, "reported_total_transportation": 1200}}]`

### v3_hard_realbudget_eval_000012
- request: 洛阳 2025-05-07->2025-05-10 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '夜市', '老字号', '城市漫步']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "洛阳博物馆", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2025-05-07", "day_index": 0, "name": "洛阳博物馆"}, {"date": "2025-05-08", "day_index": 1, "name": "洛阳博物馆"}]}, {"name_key": "洛阳十字街小吃一条街", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2025-05-07", "day_index": 0, "name": "洛阳十字街小吃一条街"}, {"date": "2025-05-09", "day_index": 2, "name": "洛阳十字街小吃一条街"}]}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 294, "expected_total_attractions": 1176, "reported_total_attractions": 1008, "meal_per_person_cost_sum": 606, "expected_total_meals": 2424, "reported_total_meals": 1868, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 294, "expected_total_attractions": 1176, "reported_total_attractions": 1008, "meal_per_person_cost_sum": 606, "expected_total_meals": 2424, "reported_total_meals": 1868, "reported_total_transportation": 200}}]`

### v3_hard_realbudget_eval_000018
- request: 天津 2026-07-06->2026-07-08 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 19203, "total": 19103, "diff": 100, "requested_budget": {"available": true, "amount": 7900, "scope": "total", "party_size": 3, "total": 7900, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "hard"}, "per_person_day": 2122.56, "budget_level": "comfortable", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "hard", "amount": 7900, "target_min_ratio": 0.7, "target_max_ratio": 1.0, "target_min_total": 5500, "target_max_total": 7900, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": false, "user_constraint_ok": false, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 3, "room_count": 2, "priced_nights": 2, "expected_min_total_hotels": 7200, "reported_total_hotels": 7200, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 393, "expected_total_attractions": 1179, "reported_total_attractions": 1449, "meal_per_person_cost_sum": 3758, "expected_total_meals": 11274, "reported_total_meals": 9354, "reported_total_transportation": 1200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 393, "expected_total_attractions": 1179, "reported_total_attractions": 1449, "meal_per_person_cost_sum": 3758, "expected_total_meals": 11274, "reported_total_meals": 9354, "reported_total_transportation": 1200}}]`

### v3_hard_realbudget_eval_000016
- request: 苏州 2026-06-06->2026-06-09 days=4 transport=自驾 hotel=亲子酒店 prefs=['亲子', '动物园', '海洋馆', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 500, "expected_total_attractions": 1500, "reported_total_attractions": 1385, "meal_per_person_cost_sum": 559, "expected_total_meals": 1677, "reported_total_meals": 1836, "reported_total_transportation": 300}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 500, "expected_total_attractions": 1500, "reported_total_attractions": 1385, "meal_per_person_cost_sum": 559, "expected_total_meals": 1677, "reported_total_meals": 1836, "reported_total_transportation": 300}}, {"stage": "rule", "type": "budget_hard_constraint_exceeded", "details": {"part_sum": 11621, "total": 11621, "diff": 0, "requested_budget": {"available": true, "amount": 10000, "scope": "total", "party_size": 3, "total": 10000, "source": "budget_constraint", "budget_level": "standard", "strictness": "hard"}, "per_person_day": 968.42, "budget_level": "standard", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "standard", "strictness": "hard", "amount": 10000, "target_min_ratio": 0.6, "target_max_ratio": 1.0, "target_min_total": 6000, "target_max_total": 10000, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": true, "within_user_budget": true, "user_constraint_ok": false, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 3, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 8100, "reported_total_hotels": 8100, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_hard_realbudget_eval_000019
- request: 丽江 2026-05-11->2026-05-14 days=4 transport=打车 hotel=亲子酒店 prefs=['亲子', '老人友好', '博物馆', '城市公园', '特色餐厅']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 960, "expected_total_attractions": 1920, "reported_total_attractions": 1680, "meal_per_person_cost_sum": 790, "expected_total_meals": 1580, "reported_total_meals": 1388, "reported_total_transportation": 1000}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 960, "expected_total_attractions": 1920, "reported_total_attractions": 1680, "meal_per_person_cost_sum": 790, "expected_total_meals": 1580, "reported_total_meals": 1388, "reported_total_transportation": 1000}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": true, "meal_cost_scale_ok": false, "budget_relationship_ok": false, "expected_total_hotels": 3900, "reported_total_hotels": 3900, "expected_total_attractions": 1920, "reported_total_attractions": 1680, "meal_scale_eval": {"ok": false, "party_total": 2, "budget_level": "comfortable", "per_person_lunch_dinner_floor": 50, "breakfast_policy": "excluded_from_meal_cost_scale", "meal_count": 12, "checked_count": 8, "failure_count": 1, "failures": [{"date": "2026-05-14", "type": "lunch", "name": "云老官保山火塘牛肉(丽江总店)", "estimated_cost": 34, "min_expected_cost": 50}]}}}]`

### v3_hard_realbudget_eval_000013
- request: 武汉 2026-05-09->2026-05-13 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "汉口江滩", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-05-11", "day_index": 2, "name": "汉口江滩"}, {"date": "2026-05-13", "day_index": 4, "name": "汉口江滩"}]}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 4, "party_total": 2, "room_count": 1, "priced_nights": 4, "expected_min_total_hotels": 1600, "reported_total_hotels": 3200, "diff": 1600, "covers_nights": false}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 210, "expected_total_attractions": 420, "reported_total_attractions": 420, "meal_per_person_cost_sum": 997, "expected_total_meals": 1994, "reported_total_meals": 2200, "reported_total_transportation": 200}}]`

### v3_hard_realbudget_eval_000020
- request: 杭州 2026-06-21->2026-06-25 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 4, "party_total": 5, "room_count": 3, "priced_nights": 4, "expected_min_total_hotels": 18000, "reported_total_hotels": 12000, "diff": -6000, "covers_nights": false}}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 16900, "total": 18900, "diff": -2000, "requested_budget": {"available": true, "amount": 27000, "scope": "total", "party_size": 5, "total": 27000, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "hard"}, "per_person_day": 756.0, "budget_level": "comfortable", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "hard", "amount": 27000, "target_min_ratio": 0.7, "target_max_ratio": 1.0, "target_min_total": 18900, "target_max_total": 27000, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 4, "party_total": 5, "room_count": 3, "priced_nights": 4, "expected_min_total_hotels": 18000, "reported_total_hotels": 12000, "diff": -6000, "covers_nights": false}, "hotel_budget_covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 5, "hotel_room_count": 3, "attraction_ticket_sum": 160, "expected_total_attractions": 800, "reported_total_attractions": 650, "meal_per_person_cost_sum": 991, "expected_total_meals": 4955, "reported_total_meals": 3250, "reported_total_transportation": 1000}}]`

### v3_hard_realbudget_eval_000017
- request: 苏州 2026-05-09->2026-05-13 days=5 transport=公共交通 hotel=民宿 prefs=['小众展馆', '咖啡', '艺术', '城市漫步', '特色餐厅']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "留园", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-05-10", "day_index": 1, "name": "留园"}, {"date": "2026-05-12", "day_index": 3, "name": "留园"}]}, {"name_key": "西园戒幢律寺", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-05-11", "day_index": 2, "name": "西园戒幢律寺"}, {"date": "2026-05-12", "day_index": 3, "name": "西园戒幢律寺"}]}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 4, "party_total": 2, "room_count": 1, "priced_nights": 4, "expected_min_total_hotels": 1200, "reported_total_hotels": 2400, "diff": 1200, "covers_nights": false}}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 6780, "total": 7800, "diff": -1020, "requested_budget": {"available": true, "amount": 10100, "scope": "total", "party_size": 2, "total": 10100, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "soft"}, "per_person_day": 780.0, "budget_level": "comfortable", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "soft", "amount": 10100, "target_min_ratio": 0.7, "target_max_ratio": 1.1, "target_min_total": 7100, "target_max_total": 11100, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 4, "party_total": 2, "room_count": 1, "priced_nights": 4, "expected_min_total_hotels": 1200, "reported_total_hotels": 2400, "diff": 1200, "covers_nights": false}, "hotel_budget_covers_nights": false}}]`
