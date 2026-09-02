# Rule Eval Report: sft_qwen25_7b_v3_260509_main_clean_step104_hard_w10

- records: 300
- generations: `training/outputs/eval/sft_qwen25_7b_v3_260509_main_clean_step104_hard_w10/generations.jsonl`
- records_path: `training/data/v3/eval_hard/records.jsonl`

## Boolean Metrics

| Metric | Pass | Total | Rate |
| --- | ---: | ---: | ---: |
| accommodation_type_ok | 299 | 299 | 100.00% |
| attraction_budget_consistent | 35 | 299 | 11.71% |
| attraction_budget_party_relation_ok | 213 | 299 | 71.24% |
| attraction_count_ok | 295 | 299 | 98.66% |
| attraction_diversity_ok | 225 | 299 | 75.25% |
| attraction_grounding_ok | 289 | 299 | 96.66% |
| attraction_repeat_limit_ok | 225 | 299 | 75.25% |
| budget_arithmetic_consistent | 209 | 299 | 69.90% |
| budget_consistent | 209 | 299 | 69.90% |
| budget_level_aligned | 228 | 299 | 76.25% |
| budget_preference_aligned | 228 | 299 | 76.25% |
| budget_relationship_ok | 127 | 299 | 42.47% |
| budget_selection_ok | 150 | 299 | 50.17% |
| budget_user_constraint_ok | 279 | 299 | 93.31% |
| budget_within_user_budget | 295 | 299 | 98.66% |
| city_ok | 299 | 299 | 100.00% |
| date_range_ok | 299 | 299 | 100.00% |
| day_dates_ok | 299 | 299 | 100.00% |
| day_index_ok | 299 | 299 | 100.00% |
| days_len_ok | 299 | 299 | 100.00% |
| dpo_soft_pass | 120 | 299 | 40.13% |
| dpo_soft_recomputed_budget_pass | 77 | 299 | 25.75% |
| hard_pass | 274 | 299 | 91.64% |
| hotel_budget_covers_nights | 217 | 299 | 72.58% |
| hotel_budget_relation_ok | 242 | 299 | 80.94% |
| hotel_distance_placeholder_ok | 299 | 299 | 100.00% |
| hotel_grounding_ok | 299 | 299 | 100.00% |
| invalid_hotel_name_ok | 299 | 299 | 100.00% |
| json_extract_ok | 300 | 300 | 100.00% |
| legacy_hard_pass | 105 | 299 | 35.12% |
| location_object_ok | 299 | 299 | 100.00% |
| meal_budget_consistent | 2 | 299 | 0.67% |
| meal_complete | 299 | 299 | 100.00% |
| meal_cost_scale_ok | 207 | 299 | 69.23% |
| meal_diversity_ok | 214 | 299 | 71.57% |
| meal_grounding_ok | 288 | 299 | 96.32% |
| meal_lunch_dinner_same_day_ok | 275 | 299 | 91.97% |
| meal_repeat_limit_ok | 227 | 299 | 75.92% |
| meal_specific_ok | 298 | 299 | 99.67% |
| meal_valid_semantics_ok | 288 | 299 | 96.32% |
| middle_hotel_ok | 299 | 299 | 100.00% |
| recomputed_budget_fit_ok | 150 | 299 | 50.17% |
| recomputed_budget_hard_ok | 256 | 299 | 85.62% |
| recomputed_budget_level_aligned | 150 | 299 | 50.17% |
| recomputed_budget_preference_aligned | 150 | 299 | 50.17% |
| recomputed_budget_user_constraint_ok | 256 | 299 | 85.62% |
| recomputed_budget_within_user_budget | 288 | 299 | 96.32% |
| schema_ok | 299 | 300 | 99.67% |
| sft_budget_semantic_hard_pass | 97 | 299 | 32.44% |
| sft_hard_pass | 274 | 299 | 91.64% |
| sft_no_budget_sum_hard_pass | 274 | 299 | 91.64% |
| sft_strict_hard_pass | 0 | 299 | 0.00% |
| transportation_budget_nonnegative | 299 | 299 | 100.00% |
| weather_dates_ok | 299 | 299 | 100.00% |
| weather_match | 299 | 299 | 100.00% |

## Numeric Metrics

```json
{
  "attraction_diversity_unique_rate": {
    "avg": 0.97,
    "p50": 1.0,
    "p90": 1.0
  },
  "attraction_grounding_rate": {
    "avg": 0.9961,
    "p50": 1.0,
    "p90": 1.0
  },
  "hotel_grounding_rate": {
    "avg": 1.0,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_diversity_unique_rate": {
    "avg": 0.8142,
    "p50": 0.8667,
    "p90": 1.0
  },
  "meal_food_pois_grounding_rate": {
    "avg": 0.9974,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_grounding_rate": {
    "avg": 0.9974,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_semantic_valid_rate": {
    "avg": 0.9974,
    "p50": 1.0,
    "p90": 1.0
  },
  "recomputed_budget_per_person_day": {
    "avg": 751.8875,
    "p50": 701.25,
    "p90": 1169.22
  },
  "recomputed_budget_total": {
    "avg": 8113.1438,
    "p50": 7215.0,
    "p90": 13627.0
  }
}
```

## Failure Types

```json
{
  "meal_budget_inconsistent": 298,
  "attraction_budget_inconsistent": 264,
  "budget_relationship_mismatch": 172,
  "meal_cost_scale_too_low": 92,
  "budget_arithmetic_inconsistent": 90,
  "hotel_budget_underestimated": 82,
  "attraction_repeat_too_many": 74,
  "meal_repeat_too_many": 72,
  "budget_preference_mismatch": 71,
  "meal_same_day_lunch_dinner_repeat": 24,
  "budget_hard_constraint_exceeded": 20,
  "meal_invalid_name": 11,
  "too_many_attractions": 4,
  "schema": 1,
  "meal_placeholder": 1
}
```

## Failure Examples

### v3_hard_realbudget_eval_000004
- request: 张家界 2026-05-11->2026-05-13 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 1960, "total": 2360, "diff": -400, "requested_budget": {"available": true, "amount": 3200, "scope": "total", "party_size": 1, "total": 3200, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "hard"}, "per_person_day": 786.67, "budget_level": "comfortable", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "hard", "amount": 3200, "target_min_ratio": 0.7, "target_max_ratio": 1.0, "target_min_total": 2200, "target_max_total": 3200, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 1, "room_count": 1, "priced_nights": 2, "expected_min_total_hotels": 800, "reported_total_hotels": 800, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 465, "expected_total_attractions": 465, "reported_total_attractions": 505, "meal_per_person_cost_sum": 492, "expected_total_meals": 492, "reported_total_meals": 355, "reported_total_transportation": 300}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 465, "expected_total_attractions": 465, "reported_total_attractions": 505, "meal_per_person_cost_sum": 492, "expected_total_meals": 492, "reported_total_meals": 355, "reported_total_transportation": 300}}]`

### v3_hard_realbudget_eval_000008
- request: 大理 2026-05-11->2026-05-13 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 7257, "total": 6257, "diff": 1000, "requested_budget": {"available": true, "amount": 8700, "scope": "total", "party_size": 3, "total": 8700, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "hard"}, "per_person_day": 695.22, "budget_level": "comfortable", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "hard", "amount": 8700, "target_min_ratio": 0.7, "target_max_ratio": 1.0, "target_min_total": 6100, "target_max_total": 8700, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 3, "room_count": 2, "priced_nights": 2, "expected_min_total_hotels": 3000, "reported_total_hotels": 3000, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 477, "expected_total_attractions": 1431, "reported_total_attractions": 1854, "meal_per_person_cost_sum": 589, "expected_total_meals": 1767, "reported_total_meals": 1403, "reported_total_transportation": 1000}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 477, "expected_total_attractions": 1431, "reported_total_attractions": 1854, "meal_per_person_cost_sum": 589, "expected_total_meals": 1767, "reported_total_meals": 1403, "reported_total_transportation": 1000}}]`

### v3_hard_realbudget_eval_000002
- request: 杭州 2026-05-01->2026-05-04 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '夜市', '老字号', '城市漫步']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 5420, "total": 4520, "diff": 900, "requested_budget": {"available": true, "amount": 6300, "scope": "total", "party_size": 4, "total": 6300, "source": "budget_constraint", "budget_level": "limited", "strictness": "hard"}, "per_person_day": 282.5, "budget_level": "limited", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "limited", "strictness": "hard", "amount": 6300, "target_min_ratio": 0.72, "target_max_ratio": 1.0, "target_min_total": 4500, "target_max_total": 6300, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 4, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 1500, "reported_total_hotels": 1500, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 229, "expected_total_attractions": 916, "reported_total_attractions": 1016, "meal_per_person_cost_sum": 632, "expected_total_meals": 2528, "reported_total_meals": 1904, "reported_total_transportation": 1000}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 229, "expected_total_attractions": 916, "reported_total_attractions": 1016, "meal_per_person_cost_sum": 632, "expected_total_meals": 2528, "reported_total_meals": 1904, "reported_total_transportation": 1000}}]`

### v3_hard_realbudget_eval_000006
- request: 南京 2026-07-06->2026-07-09 days=4 transport=自驾 hotel=亲子酒店 prefs=['亲子', '动物园', '海洋馆', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 202, "expected_total_attractions": 606, "reported_total_attractions": 543, "meal_per_person_cost_sum": 720, "expected_total_meals": 2160, "reported_total_meals": 1620, "reported_total_transportation": 300}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 202, "expected_total_attractions": 606, "reported_total_attractions": 543, "meal_per_person_cost_sum": 720, "expected_total_meals": 2160, "reported_total_meals": 1620, "reported_total_transportation": 300}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": true, "meal_cost_scale_ok": false, "budget_relationship_ok": false, "expected_total_hotels": 7500, "reported_total_hotels": 7500, "expected_total_attractions": 606, "reported_total_attractions": 543, "meal_scale_eval": {"ok": false, "party_total": 3, "budget_level": "standard", "per_person_lunch_dinner_floor": 35, "breakfast_policy": "excluded_from_meal_cost_scale", "meal_count": 12, "checked_count": 8, "failure_count": 2, "failures": [{"date": "2026-07-07", "type": "lunch", "name": "小潘记鸭血粉丝汤", "estimated_cost": 34, "min_expected_cost": 35}, {"date": "2026-07-09", "type": "lunch", "name": "刘长兴(鼓楼店)", "estimated_cost": 28, "min_expected_cost": 35}]}}}]`

### v3_hard_realbudget_eval_000001
- request: 桂林 2026-09-04->2026-09-07 days=4 transport=打车 hotel=高端酒店 prefs=['高端酒店', '艺术', '特色餐厅', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 2, "room_count": 1, "priced_nights": 3, "expected_min_total_hotels": 3600, "reported_total_hotels": 7200, "diff": 3600, "covers_nights": false}}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 12786, "total": 10886, "diff": 1900, "requested_budget": {"available": true, "amount": 13100, "scope": "total", "party_size": 2, "total": 13100, "source": "budget_constraint", "budget_level": "premium", "strictness": "soft"}, "per_person_day": 1360.75, "budget_level": "premium", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "premium", "strictness": "soft", "amount": 13100, "target_min_ratio": 0.75, "target_max_ratio": 1.12, "target_min_total": 9800, "target_max_total": 14700, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 2, "room_count": 1, "priced_nights": 3, "expected_min_total_hotels": 3600, "reported_total_hotels": 7200, "diff": 3600, "covers_nights": false}, "hotel_budget_covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 985, "expected_total_attractions": 1970, "reported_total_attractions": 2550, "meal_per_person_cost_sum": 879, "expected_total_meals": 1758, "reported_total_meals": 2136, "reported_total_transportation": 900}}]`

### v3_hard_realbudget_eval_000007
- request: 成都 2026-05-11->2026-05-15 days=5 transport=公共交通 hotel=民宿 prefs=['小众展馆', '咖啡', '艺术', '城市漫步', '特色餐厅']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-05-14", "lunch": "悦百味·品质川菜(成都环贸ICD店)", "dinner": "悦百味·品质川菜(武侯欢肆店)"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "山面包", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-05-11", "type": "breakfast", "name": "山面包(望平街店)"}, {"date": "2026-05-12", "type": "breakfast", "name": "山面包(东郊记忆店)"}, {"date": "2026-05-13", "type": "breakfast", "name": "山面包(东郊记忆店)"}, {"date": "2026-05-14", "type": "breakfast", "name": "山面包(望平街店)"}, {"date": "2026-05-15", "type": "breakfast", "name": "山面包(东郊记忆店)"}]}, {"name_key": "悦百味·品质川菜", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-05-12", "type": "dinner", "name": "悦百味·品质川菜(优品道店)"}, {"date": "2026-05-13", "type": "dinner", "name": "悦百味·品质川菜(UPARK公园店)"}, {"date": "2026-05-14", "type": "lunch", "name": "悦百味·品质川菜(成都环贸ICD店)"}, {"date": "2026-05-14", "type": "dinner", "name": "悦百味·品质川菜(武侯欢肆店)"}]}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 4, "party_total": 2, "room_count": 1, "priced_nights": 4, "expected_min_total_hotels": 1200, "reported_total_hotels": 2400, "diff": 1200, "covers_nights": false}}]`

### v3_hard_realbudget_eval_000003
- request: 西安 2025-05-07->2025-05-11 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2025-05-10", "lunch": "苏福记(金萨店)", "dinner": "苏福记(高新店)"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "爱骅裤带面馆", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2025-05-07", "type": "breakfast", "name": "爱骅裤带面馆(钟楼店)"}, {"date": "2025-05-09", "type": "breakfast", "name": "爱骅裤带面馆( 总店 )"}, {"date": "2025-05-10", "type": "breakfast", "name": "爱骅裤带面馆( 总店 )"}, {"date": "2025-05-11", "type": "breakfast", "name": "爱骅裤带面馆( 总店 )"}]}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 4, "party_total": 2, "room_count": 1, "priced_nights": 4, "expected_min_total_hotels": 1800, "reported_total_hotels": 3600, "diff": 1800, "covers_nights": false}}]`

### v3_hard_realbudget_eval_000005
- request: 广州 2026-07-06->2026-07-10 days=5 transport=公共交通 hotel=民宿 prefs=['摄影', '自然风光', '城市漫步', '本地菜']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "银灯食府", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-07-06", "type": "breakfast", "name": "银灯食府(丽丰国际中心店)"}, {"date": "2026-07-07", "type": "breakfast", "name": "银灯食府(文化公园店)"}, {"date": "2026-07-08", "type": "breakfast", "name": "银灯食府(文化公园店)"}, {"date": "2026-07-09", "type": "breakfast", "name": "银灯食府(文化公园店)"}, {"date": "2026-07-10", "type": "breakfast", "name": "银灯食府(文化公园店)"}]}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 524, "expected_total_attractions": 524, "reported_total_attractions": 539, "meal_per_person_cost_sum": 1527, "expected_total_meals": 1527, "reported_total_meals": 1396, "reported_total_transportation": 100}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 524, "expected_total_attractions": 524, "reported_total_attractions": 539, "meal_per_person_cost_sum": 1527, "expected_total_meals": 1527, "reported_total_meals": 1396, "reported_total_transportation": 100}}]`

### v3_hard_realbudget_eval_000000
- request: 昆明 2026-04-07->2026-04-11 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 4, "party_total": 5, "room_count": 3, "priced_nights": 4, "expected_min_total_hotels": 4800, "reported_total_hotels": 4000, "diff": -800, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 5, "hotel_room_count": 3, "attraction_ticket_sum": 536, "expected_total_attractions": 2680, "reported_total_attractions": 2850, "meal_per_person_cost_sum": 934, "expected_total_meals": 4670, "reported_total_meals": 5850, "reported_total_transportation": 5000}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 5, "hotel_room_count": 3, "attraction_ticket_sum": 536, "expected_total_attractions": 2680, "reported_total_attractions": 2850, "meal_per_person_cost_sum": 934, "expected_total_meals": 4670, "reported_total_meals": 5850, "reported_total_transportation": 5000}}]`

### v3_hard_realbudget_eval_000010
- request: 西安 2026-08-05->2026-08-09 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "西安博物院", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-08-07", "day_index": 2, "name": "西安博物院"}, {"date": "2026-08-08", "day_index": 3, "name": "西安博物院"}]}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "唐猫庭院·千年陕菜", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-08-05", "type": "dinner", "name": "唐猫庭院·千年陕菜(大唐不夜城店)"}, {"date": "2026-08-07", "type": "dinner", "name": "唐猫庭院·千年陕菜(大唐不夜城店)"}, {"date": "2026-08-08", "type": "dinner", "name": "唐猫庭院·千年陕菜(大唐不夜城店)"}, {"date": "2026-08-09", "type": "dinner", "name": "唐猫庭院·千年陕菜(大唐不夜城店)"}]}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 4, "party_total": 5, "room_count": 3, "priced_nights": 4, "expected_min_total_hotels": 5400, "reported_total_hotels": 4500, "diff": -900, "covers_nights": false}}]`

### v3_hard_realbudget_eval_000011
- request: 福州 2026-06-21->2026-06-24 days=4 transport=打车 hotel=高端酒店 prefs=['高端酒店', '艺术', '特色餐厅', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 2, "room_count": 1, "priced_nights": 3, "expected_min_total_hotels": 2250, "reported_total_hotels": 4500, "diff": 2250, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 567, "expected_total_attractions": 1134, "reported_total_attractions": 1404, "meal_per_person_cost_sum": 1483, "expected_total_meals": 2966, "reported_total_meals": 4884, "reported_total_transportation": 1200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 567, "expected_total_attractions": 1134, "reported_total_attractions": 1404, "meal_per_person_cost_sum": 1483, "expected_total_meals": 2966, "reported_total_meals": 4884, "reported_total_transportation": 1200}}]`

### v3_hard_realbudget_eval_000014
- request: 成都 2026-06-06->2026-06-08 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "山面包", "count": 3, "max_allowed": 2, "occurrences": [{"date": "2026-06-06", "type": "breakfast", "name": "山面包(望平街店)"}, {"date": "2026-06-07", "type": "breakfast", "name": "山面包(东郊记忆店)"}, {"date": "2026-06-08", "type": "breakfast", "name": "山面包(东郊记忆店)"}]}]}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 3719, "total": 4119, "diff": -400, "requested_budget": {"available": true, "amount": 4300, "scope": "total", "party_size": 1, "total": 4300, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "hard"}, "per_person_day": 1373.0, "budget_level": "comfortable", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "hard", "amount": 4300, "target_min_ratio": 0.7, "target_max_ratio": 1.0, "target_min_total": 3000, "target_max_total": 4300, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 1, "room_count": 1, "priced_nights": 2, "expected_min_total_hotels": 2500, "reported_total_hotels": 2500, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 130, "expected_total_attractions": 130, "reported_total_attractions": 130, "meal_per_person_cost_sum": 595, "expected_total_meals": 595, "reported_total_meals": 489, "reported_total_transportation": 600}}]`

### v3_hard_realbudget_eval_000009
- request: 苏州 2026-04-30->2026-05-03 days=4 transport=打车 hotel=亲子酒店 prefs=['亲子', '老人友好', '博物馆', '城市公园', '特色餐厅']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 12684, "total": 11784, "diff": 900, "requested_budget": {"available": true, "amount": 16700, "scope": "total", "party_size": 4, "total": 16700, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "soft"}, "per_person_day": 736.5, "budget_level": "comfortable", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "soft", "amount": 16700, "target_min_ratio": 0.7, "target_max_ratio": 1.1, "target_min_total": 11700, "target_max_total": 18400, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 4, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 7500, "reported_total_hotels": 7500, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 495, "expected_total_attractions": 1980, "reported_total_attractions": 3320, "meal_per_person_cost_sum": 885, "expected_total_meals": 3540, "reported_total_meals": 1464, "reported_total_transportation": 400}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 495, "expected_total_attractions": 1980, "reported_total_attractions": 3320, "meal_per_person_cost_sum": 885, "expected_total_meals": 3540, "reported_total_meals": 1464, "reported_total_transportation": 400}}]`

### v3_hard_realbudget_eval_000018
- request: 天津 2026-07-06->2026-07-08 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 7664, "total": 5564, "diff": 2100, "requested_budget": {"available": true, "amount": 7900, "scope": "total", "party_size": 3, "total": 7900, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "hard"}, "per_person_day": 618.22, "budget_level": "comfortable", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "hard", "amount": 7900, "target_min_ratio": 0.7, "target_max_ratio": 1.0, "target_min_total": 5500, "target_max_total": 7900, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 3, "room_count": 2, "priced_nights": 2, "expected_min_total_hotels": 4800, "reported_total_hotels": 4800, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 444, "expected_total_attractions": 1332, "reported_total_attractions": 1434, "meal_per_person_cost_sum": 1090, "expected_total_meals": 3270, "reported_total_meals": 1330, "reported_total_transportation": 100}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 444, "expected_total_attractions": 1332, "reported_total_attractions": 1434, "meal_per_person_cost_sum": 1090, "expected_total_meals": 3270, "reported_total_meals": 1330, "reported_total_transportation": 100}}]`

### v3_hard_realbudget_eval_000012
- request: 洛阳 2025-05-07->2025-05-10 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '夜市', '老字号', '城市漫步']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 5156, "total": 4156, "diff": 1000, "requested_budget": {"available": true, "amount": 5800, "scope": "total", "party_size": 4, "total": 5800, "source": "budget_constraint", "budget_level": "limited", "strictness": "hard"}, "per_person_day": 259.75, "budget_level": "limited", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "limited", "strictness": "hard", "amount": 5800, "target_min_ratio": 0.72, "target_max_ratio": 1.0, "target_min_total": 4200, "target_max_total": 5800, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 4, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 1800, "reported_total_hotels": 1800, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 284, "expected_total_attractions": 1136, "reported_total_attractions": 1328, "meal_per_person_cost_sum": 606, "expected_total_meals": 2424, "reported_total_meals": 1428, "reported_total_transportation": 600}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 284, "expected_total_attractions": 1136, "reported_total_attractions": 1328, "meal_per_person_cost_sum": 606, "expected_total_meals": 2424, "reported_total_meals": 1428, "reported_total_transportation": 600}}]`

### v3_hard_realbudget_eval_000016
- request: 苏州 2026-06-06->2026-06-09 days=4 transport=自驾 hotel=亲子酒店 prefs=['亲子', '动物园', '海洋馆', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 150, "expected_total_attractions": 450, "reported_total_attractions": 510, "meal_per_person_cost_sum": 848, "expected_total_meals": 2544, "reported_total_meals": 2859, "reported_total_transportation": 1000}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 150, "expected_total_attractions": 450, "reported_total_attractions": 510, "meal_per_person_cost_sum": 848, "expected_total_meals": 2544, "reported_total_meals": 2859, "reported_total_transportation": 1000}}, {"stage": "rule", "type": "budget_hard_constraint_exceeded", "details": {"part_sum": 11869, "total": 11869, "diff": 0, "requested_budget": {"available": true, "amount": 10000, "scope": "total", "party_size": 3, "total": 10000, "source": "budget_constraint", "budget_level": "standard", "strictness": "hard"}, "per_person_day": 989.08, "budget_level": "standard", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "standard", "strictness": "hard", "amount": 10000, "target_min_ratio": 0.6, "target_max_ratio": 1.0, "target_min_total": 6000, "target_max_total": 10000, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": true, "within_user_budget": true, "user_constraint_ok": false, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 3, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 7500, "reported_total_hotels": 7500, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_hard_realbudget_eval_000019
- request: 丽江 2026-05-11->2026-05-14 days=4 transport=打车 hotel=亲子酒店 prefs=['亲子', '老人友好', '博物馆', '城市公园', '特色餐厅']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 877, "expected_total_attractions": 1754, "reported_total_attractions": 1854, "meal_per_person_cost_sum": 576, "expected_total_meals": 1152, "reported_total_meals": 1122, "reported_total_transportation": 1000}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 877, "expected_total_attractions": 1754, "reported_total_attractions": 1854, "meal_per_person_cost_sum": 576, "expected_total_meals": 1152, "reported_total_meals": 1122, "reported_total_transportation": 1000}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": true, "meal_cost_scale_ok": false, "budget_relationship_ok": false, "expected_total_hotels": 3600, "reported_total_hotels": 3600, "expected_total_attractions": 1754, "reported_total_attractions": 1854, "meal_scale_eval": {"ok": false, "party_total": 2, "budget_level": "comfortable", "per_person_lunch_dinner_floor": 50, "breakfast_policy": "excluded_from_meal_cost_scale", "meal_count": 12, "checked_count": 8, "failure_count": 1, "failures": [{"date": "2026-05-11", "type": "lunch", "name": "云老官保山火塘牛肉(丽江总店)", "estimated_cost": 34, "min_expected_cost": 50}]}}}]`

### v3_hard_realbudget_eval_000013
- request: 武汉 2026-05-09->2026-05-13 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "江汉关博物馆", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-05-11", "day_index": 2, "name": "江汉关博物馆"}, {"date": "2026-05-13", "day_index": 4, "name": "江汉关博物馆"}]}]}, {"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-05-13", "lunch": "刘聋子牛肉粉馆(汉阳玫瑰街店)", "dinner": "刘聋子牛肉粉馆(光谷新竹路店)"}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 4, "party_total": 2, "room_count": 1, "priced_nights": 4, "expected_min_total_hotels": 1600, "reported_total_hotels": 2400, "diff": 800, "covers_nights": false}}]`

### v3_hard_realbudget_eval_000017
- request: 苏州 2026-05-09->2026-05-13 days=5 transport=公共交通 hotel=民宿 prefs=['小众展馆', '咖啡', '艺术', '城市漫步', '特色餐厅']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 6234, "total": 7234, "diff": -1000, "requested_budget": {"available": true, "amount": 10100, "scope": "total", "party_size": 2, "total": 10100, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "soft"}, "per_person_day": 723.4, "budget_level": "comfortable", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "soft", "amount": 10100, "target_min_ratio": 0.7, "target_max_ratio": 1.1, "target_min_total": 7100, "target_max_total": 11100, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 4, "party_total": 2, "room_count": 1, "priced_nights": 4, "expected_min_total_hotels": 1200, "reported_total_hotels": 1200, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 300, "expected_total_attractions": 600, "reported_total_attractions": 670, "meal_per_person_cost_sum": 982, "expected_total_meals": 1964, "reported_total_meals": 3164, "reported_total_transportation": 1200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 300, "expected_total_attractions": 600, "reported_total_attractions": 670, "meal_per_person_cost_sum": 982, "expected_total_meals": 1964, "reported_total_meals": 3164, "reported_total_transportation": 1200}}]`

### v3_hard_realbudget_eval_000020
- request: 杭州 2026-06-21->2026-06-25 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 4, "party_total": 5, "room_count": 3, "priced_nights": 4, "expected_min_total_hotels": 6000, "reported_total_hotels": 4000, "diff": -2000, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 5, "hotel_room_count": 3, "attraction_ticket_sum": 928, "expected_total_attractions": 4640, "reported_total_attractions": 4350, "meal_per_person_cost_sum": 1102, "expected_total_meals": 5510, "reported_total_meals": 3765, "reported_total_transportation": 1500}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 5, "hotel_room_count": 3, "attraction_ticket_sum": 928, "expected_total_attractions": 4640, "reported_total_attractions": 4350, "meal_per_person_cost_sum": 1102, "expected_total_meals": 5510, "reported_total_meals": 3765, "reported_total_transportation": 1500}}]`
