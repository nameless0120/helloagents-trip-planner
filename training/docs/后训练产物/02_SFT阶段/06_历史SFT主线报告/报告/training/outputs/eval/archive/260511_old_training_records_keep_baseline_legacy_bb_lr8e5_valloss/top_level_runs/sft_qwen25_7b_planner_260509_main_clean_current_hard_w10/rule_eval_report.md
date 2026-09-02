# Rule Eval Report: sft_qwen25_7b_v3_260509_main_clean_current_hard_w10

- records: 300
- generations: `training/outputs/eval/sft_qwen25_7b_v3_260509_main_clean_current_hard_w10/generations.jsonl`
- records_path: `training/data/v3/eval_hard/records.jsonl`

## Boolean Metrics

| Metric | Pass | Total | Rate |
| --- | ---: | ---: | ---: |
| accommodation_type_ok | 299 | 299 | 100.00% |
| attraction_budget_consistent | 57 | 299 | 19.06% |
| attraction_budget_party_relation_ok | 282 | 299 | 94.31% |
| attraction_count_ok | 298 | 299 | 99.67% |
| attraction_diversity_ok | 245 | 299 | 81.94% |
| attraction_grounding_ok | 293 | 299 | 97.99% |
| attraction_repeat_limit_ok | 245 | 299 | 81.94% |
| budget_arithmetic_consistent | 207 | 299 | 69.23% |
| budget_consistent | 207 | 299 | 69.23% |
| budget_level_aligned | 220 | 299 | 73.58% |
| budget_preference_aligned | 220 | 299 | 73.58% |
| budget_relationship_ok | 196 | 299 | 65.55% |
| budget_selection_ok | 144 | 299 | 48.16% |
| budget_user_constraint_ok | 281 | 299 | 93.98% |
| budget_within_user_budget | 295 | 299 | 98.66% |
| city_ok | 299 | 299 | 100.00% |
| date_range_ok | 299 | 299 | 100.00% |
| day_dates_ok | 299 | 299 | 100.00% |
| day_index_ok | 299 | 299 | 100.00% |
| days_len_ok | 299 | 299 | 100.00% |
| dpo_soft_pass | 144 | 299 | 48.16% |
| dpo_soft_recomputed_budget_pass | 97 | 299 | 32.44% |
| hard_pass | 286 | 299 | 95.65% |
| hotel_budget_covers_nights | 282 | 299 | 94.31% |
| hotel_budget_relation_ok | 285 | 299 | 95.32% |
| hotel_distance_placeholder_ok | 299 | 299 | 100.00% |
| hotel_grounding_ok | 299 | 299 | 100.00% |
| invalid_hotel_name_ok | 299 | 299 | 100.00% |
| json_extract_ok | 300 | 300 | 100.00% |
| legacy_hard_pass | 157 | 299 | 52.51% |
| location_object_ok | 299 | 299 | 100.00% |
| meal_budget_consistent | 0 | 299 | 0.00% |
| meal_complete | 299 | 299 | 100.00% |
| meal_cost_scale_ok | 210 | 299 | 70.23% |
| meal_diversity_ok | 235 | 299 | 78.60% |
| meal_grounding_ok | 293 | 299 | 97.99% |
| meal_lunch_dinner_same_day_ok | 283 | 299 | 94.65% |
| meal_repeat_limit_ok | 248 | 299 | 82.94% |
| meal_specific_ok | 299 | 299 | 100.00% |
| meal_valid_semantics_ok | 293 | 299 | 97.99% |
| middle_hotel_ok | 299 | 299 | 100.00% |
| recomputed_budget_fit_ok | 144 | 299 | 48.16% |
| recomputed_budget_hard_ok | 252 | 299 | 84.28% |
| recomputed_budget_level_aligned | 144 | 299 | 48.16% |
| recomputed_budget_preference_aligned | 144 | 299 | 48.16% |
| recomputed_budget_user_constraint_ok | 252 | 299 | 84.28% |
| recomputed_budget_within_user_budget | 288 | 299 | 96.32% |
| schema_ok | 299 | 300 | 99.67% |
| sft_budget_semantic_hard_pass | 169 | 299 | 56.52% |
| sft_hard_pass | 286 | 299 | 95.65% |
| sft_no_budget_sum_hard_pass | 286 | 299 | 95.65% |
| sft_strict_hard_pass | 0 | 299 | 0.00% |
| transportation_budget_nonnegative | 299 | 299 | 100.00% |
| weather_dates_ok | 299 | 299 | 100.00% |
| weather_match | 299 | 299 | 100.00% |

## Numeric Metrics

```json
{
  "attraction_diversity_unique_rate": {
    "avg": 0.9774,
    "p50": 1.0,
    "p90": 1.0
  },
  "attraction_grounding_rate": {
    "avg": 0.9981,
    "p50": 1.0,
    "p90": 1.0
  },
  "hotel_grounding_rate": {
    "avg": 1.0,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_diversity_unique_rate": {
    "avg": 0.8344,
    "p50": 0.8667,
    "p90": 1.0
  },
  "meal_food_pois_grounding_rate": {
    "avg": 0.9987,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_grounding_rate": {
    "avg": 0.9987,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_semantic_valid_rate": {
    "avg": 0.9987,
    "p50": 1.0,
    "p90": 1.0
  },
  "recomputed_budget_per_person_day": {
    "avg": 759.2016,
    "p50": 721.6,
    "p90": 1170.75
  },
  "recomputed_budget_total": {
    "avg": 8151.6756,
    "p50": 7307.0,
    "p90": 14120.0
  }
}
```

## Failure Types

```json
{
  "meal_budget_inconsistent": 299,
  "attraction_budget_inconsistent": 242,
  "budget_relationship_mismatch": 103,
  "budget_arithmetic_inconsistent": 92,
  "meal_cost_scale_too_low": 89,
  "budget_preference_mismatch": 79,
  "attraction_repeat_too_many": 54,
  "meal_repeat_too_many": 51,
  "budget_hard_constraint_exceeded": 18,
  "hotel_budget_underestimated": 17,
  "meal_same_day_lunch_dinner_repeat": 16,
  "meal_invalid_name": 6,
  "schema": 1,
  "too_many_attractions": 1
}
```

## Failure Examples

### v3_hard_realbudget_eval_000004
- request: 张家界 2026-05-11->2026-05-13 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 664, "expected_total_attractions": 664, "reported_total_attractions": 774, "meal_per_person_cost_sum": 561, "expected_total_meals": 561, "reported_total_meals": 426, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 664, "expected_total_attractions": 664, "reported_total_attractions": 774, "meal_per_person_cost_sum": 561, "expected_total_meals": 561, "reported_total_meals": 426, "reported_total_transportation": 200}}]`

### v3_hard_realbudget_eval_000008
- request: 大理 2026-05-11->2026-05-13 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 6199, "total": 6200, "diff": -1, "requested_budget": {"available": true, "amount": 8700, "scope": "total", "party_size": 3, "total": 8700, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "hard"}, "per_person_day": 688.89, "budget_level": "comfortable", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "hard", "amount": 8700, "target_min_ratio": 0.7, "target_max_ratio": 1.0, "target_min_total": 6100, "target_max_total": 8700, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 3, "room_count": 2, "priced_nights": 2, "expected_min_total_hotels": 3000, "reported_total_hotels": 3000, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 370, "expected_total_attractions": 1110, "reported_total_attractions": 1248, "meal_per_person_cost_sum": 481, "expected_total_meals": 1443, "reported_total_meals": 1551, "reported_total_transportation": 400}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 370, "expected_total_attractions": 1110, "reported_total_attractions": 1248, "meal_per_person_cost_sum": 481, "expected_total_meals": 1443, "reported_total_meals": 1551, "reported_total_transportation": 400}}]`

### v3_hard_realbudget_eval_000006
- request: 南京 2026-07-06->2026-07-09 days=4 transport=自驾 hotel=亲子酒店 prefs=['亲子', '动物园', '海洋馆', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 165, "expected_total_attractions": 495, "reported_total_attractions": 405, "meal_per_person_cost_sum": 691, "expected_total_meals": 2073, "reported_total_meals": 1590, "reported_total_transportation": 500}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 165, "expected_total_attractions": 495, "reported_total_attractions": 405, "meal_per_person_cost_sum": 691, "expected_total_meals": 2073, "reported_total_meals": 1590, "reported_total_transportation": 500}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": true, "meal_cost_scale_ok": false, "budget_relationship_ok": false, "expected_total_hotels": 7500, "reported_total_hotels": 7500, "expected_total_attractions": 495, "reported_total_attractions": 405, "meal_scale_eval": {"ok": false, "party_total": 3, "budget_level": "standard", "per_person_lunch_dinner_floor": 35, "breakfast_policy": "excluded_from_meal_cost_scale", "meal_count": 12, "checked_count": 8, "failure_count": 1, "failures": [{"date": "2026-07-07", "type": "lunch", "name": "小潘记鸭血粉丝汤", "estimated_cost": 34, "min_expected_cost": 35}]}}}]`

### v3_hard_realbudget_eval_000002
- request: 杭州 2026-05-01->2026-05-04 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '夜市', '老字号', '城市漫步']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 160, "expected_total_attractions": 640, "reported_total_attractions": 680, "meal_per_person_cost_sum": 720, "expected_total_meals": 2880, "reported_total_meals": 2028, "reported_total_transportation": 300}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 160, "expected_total_attractions": 640, "reported_total_attractions": 680, "meal_per_person_cost_sum": 720, "expected_total_meals": 2880, "reported_total_meals": 2028, "reported_total_transportation": 300}}]`

### v3_hard_realbudget_eval_000001
- request: 桂林 2026-09-04->2026-09-07 days=4 transport=打车 hotel=高端酒店 prefs=['高端酒店', '艺术', '特色餐厅', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 805, "expected_total_attractions": 1610, "reported_total_attractions": 1390, "meal_per_person_cost_sum": 728, "expected_total_meals": 1456, "reported_total_meals": 2610, "reported_total_transportation": 2700}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 805, "expected_total_attractions": 1610, "reported_total_attractions": 1390, "meal_per_person_cost_sum": 728, "expected_total_meals": 1456, "reported_total_meals": 2610, "reported_total_transportation": 2700}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": true, "meal_cost_scale_ok": false, "budget_relationship_ok": false, "expected_total_hotels": 3600, "reported_total_hotels": 3600, "expected_total_attractions": 1610, "reported_total_attractions": 1390, "meal_scale_eval": {"ok": false, "party_total": 2, "budget_level": "premium", "per_person_lunch_dinner_floor": 70, "breakfast_policy": "excluded_from_meal_cost_scale", "meal_count": 12, "checked_count": 8, "failure_count": 3, "failures": [{"date": "2026-09-05", "type": "lunch", "name": "阿甘酒家(依仁店)", "estimated_cost": 68, "min_expected_cost": 70}, {"date": "2026-09-06", "type": "lunch", "name": "椿记烧鹅(中山店)", "estimated_cost": 56, "min_expected_cost": 70}, {"date": "2026-09-07", "type": "lunch", "name": "澳门酒家(高新店)", "estimated_cost": 58, "min_expected_cost": 70}]}}}]`

### v3_hard_realbudget_eval_000005
- request: 广州 2026-07-06->2026-07-10 days=5 transport=公共交通 hotel=民宿 prefs=['摄影', '自然风光', '城市漫步', '本地菜']
- errors: `[{"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 186, "expected_total_attractions": 186, "reported_total_attractions": 186, "meal_per_person_cost_sum": 1383, "expected_total_meals": 1383, "reported_total_meals": 1136, "reported_total_transportation": 200}}]`

### v3_hard_realbudget_eval_000000
- request: 昆明 2026-04-07->2026-04-11 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 5, "hotel_room_count": 3, "attraction_ticket_sum": 736, "expected_total_attractions": 3680, "reported_total_attractions": 3360, "meal_per_person_cost_sum": 938, "expected_total_meals": 4690, "reported_total_meals": 5985, "reported_total_transportation": 1500}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 5, "hotel_room_count": 3, "attraction_ticket_sum": 736, "expected_total_attractions": 3680, "reported_total_attractions": 3360, "meal_per_person_cost_sum": 938, "expected_total_meals": 4690, "reported_total_meals": 5985, "reported_total_transportation": 1500}}, {"stage": "rule", "type": "budget_preference_mismatch", "details": {"part_sum": 15645, "total": 15645, "diff": 0, "requested_budget": {"available": true, "amount": 24700, "scope": "total", "party_size": 5, "total": 24700, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "hard"}, "per_person_day": 625.8, "budget_level": "comfortable", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "hard", "amount": 24700, "target_min_ratio": 0.7, "target_max_ratio": 1.0, "target_min_total": 17300, "target_max_total": 24700, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": true, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 4, "party_total": 5, "room_count": 3, "priced_nights": 4, "expected_min_total_hotels": 4800, "reported_total_hotels": 4800, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_hard_realbudget_eval_000010
- request: 西安 2026-08-05->2026-08-09 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "西安博物院", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-08-08", "day_index": 3, "name": "西安博物院"}, {"date": "2026-08-09", "day_index": 4, "name": "西安博物院"}]}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 5, "hotel_room_count": 3, "attraction_ticket_sum": 699, "expected_total_attractions": 3495, "reported_total_attractions": 3520, "meal_per_person_cost_sum": 776, "expected_total_meals": 3880, "reported_total_meals": 5880, "reported_total_transportation": 6800}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 5, "hotel_room_count": 3, "attraction_ticket_sum": 699, "expected_total_attractions": 3495, "reported_total_attractions": 3520, "meal_per_person_cost_sum": 776, "expected_total_meals": 3880, "reported_total_meals": 5880, "reported_total_transportation": 6800}}]`

### v3_hard_realbudget_eval_000003
- request: 西安 2025-05-07->2025-05-11 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "西安碑林博物馆", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2025-05-08", "day_index": 1, "name": "西安碑林博物馆"}, {"date": "2025-05-11", "day_index": 4, "name": "西安碑林博物馆"}]}]}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 4986, "total": 5086, "diff": -100, "requested_budget": {"available": true, "amount": 8400, "scope": "total", "party_size": 2, "total": 8400, "source": "budget_constraint", "budget_level": "standard", "strictness": "hard"}, "per_person_day": 508.6, "budget_level": "standard", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "standard", "strictness": "hard", "amount": 8400, "target_min_ratio": 0.6, "target_max_ratio": 1.0, "target_min_total": 5000, "target_max_total": 8400, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 4, "party_total": 2, "room_count": 1, "priced_nights": 4, "expected_min_total_hotels": 1800, "reported_total_hotels": 1800, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 303, "expected_total_attractions": 606, "reported_total_attractions": 622, "meal_per_person_cost_sum": 717, "expected_total_meals": 1434, "reported_total_meals": 2064, "reported_total_transportation": 500}}]`

### v3_hard_realbudget_eval_000007
- request: 成都 2026-05-11->2026-05-15 days=5 transport=公共交通 hotel=民宿 prefs=['小众展馆', '咖啡', '艺术', '城市漫步', '特色餐厅']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-05-13", "lunch": "悦百味·品质川菜(UPARK公园店)", "dinner": "悦百味·品质川菜(成都环贸ICD店)"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "悦百味·品质川菜", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-05-12", "type": "lunch", "name": "悦百味·品质川菜(优品道店)"}, {"date": "2026-05-13", "type": "lunch", "name": "悦百味·品质川菜(UPARK公园店)"}, {"date": "2026-05-13", "type": "dinner", "name": "悦百味·品质川菜(成都环贸ICD店)"}, {"date": "2026-05-14", "type": "lunch", "name": "悦百味·品质川菜(武侯欢肆店)"}, {"date": "2026-05-15", "type": "dinner", "name": "悦百味·品质川菜(悠方店)"}]}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 1448, "expected_total_attractions": 2896, "reported_total_attractions": 2862, "meal_per_person_cost_sum": 2159, "expected_total_meals": 4318, "reported_total_meals": 4594, "reported_total_transportation": 400}}]`

### v3_hard_realbudget_eval_000014
- request: 成都 2026-06-06->2026-06-08 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-06-07", "lunch": "悦百味·品质川菜(UPARK公园店)", "dinner": "悦百味·品质川菜(悠方店)"}]}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 165, "expected_total_attractions": 165, "reported_total_attractions": 165, "meal_per_person_cost_sum": 675, "expected_total_meals": 675, "reported_total_meals": 603, "reported_total_transportation": 300}}]`

### v3_hard_realbudget_eval_000009
- request: 苏州 2026-04-30->2026-05-03 days=4 transport=打车 hotel=亲子酒店 prefs=['亲子', '老人友好', '博物馆', '城市公园', '特色餐厅']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "苏州丝绸博物馆", "count": 3, "max_allowed": 1, "occurrences": [{"date": "2026-05-01", "day_index": 1, "name": "苏州丝绸博物馆"}, {"date": "2026-05-02", "day_index": 2, "name": "苏州丝绸博物馆"}, {"date": "2026-05-03", "day_index": 3, "name": "苏州丝绸博物馆"}]}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 120, "expected_total_attractions": 480, "reported_total_attractions": 500, "meal_per_person_cost_sum": 549, "expected_total_meals": 2196, "reported_total_meals": 2728, "reported_total_transportation": 1000}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 120, "expected_total_attractions": 480, "reported_total_attractions": 500, "meal_per_person_cost_sum": 549, "expected_total_meals": 2196, "reported_total_meals": 2728, "reported_total_transportation": 1000}}]`

### v3_hard_realbudget_eval_000011
- request: 福州 2026-06-21->2026-06-24 days=4 transport=打车 hotel=高端酒店 prefs=['高端酒店', '艺术', '特色餐厅', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-06-23", "lunch": "紫阳海鲜楼·传承闽味(长乐路总店)", "dinner": "紫阳海鲜楼·传承闽味(华林路店)"}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 487, "expected_total_attractions": 974, "reported_total_attractions": 874, "meal_per_person_cost_sum": 1448, "expected_total_meals": 2896, "reported_total_meals": 3876, "reported_total_transportation": 1500}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 487, "expected_total_attractions": 974, "reported_total_attractions": 874, "meal_per_person_cost_sum": 1448, "expected_total_meals": 2896, "reported_total_meals": 3876, "reported_total_transportation": 1500}}]`

### v3_hard_realbudget_eval_000012
- request: 洛阳 2025-05-07->2025-05-10 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '夜市', '老字号', '城市漫步']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 4908, "total": 5908, "diff": -1000, "requested_budget": {"available": true, "amount": 5800, "scope": "total", "party_size": 4, "total": 5800, "source": "budget_constraint", "budget_level": "limited", "strictness": "hard"}, "per_person_day": 369.25, "budget_level": "limited", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "limited", "strictness": "hard", "amount": 5800, "target_min_ratio": 0.72, "target_max_ratio": 1.0, "target_min_total": 4200, "target_max_total": 5800, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": false, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 4, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 1800, "reported_total_hotels": 1800, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 315, "expected_total_attractions": 1260, "reported_total_attractions": 1108, "meal_per_person_cost_sum": 606, "expected_total_meals": 2424, "reported_total_meals": 1800, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 315, "expected_total_attractions": 1260, "reported_total_attractions": 1108, "meal_per_person_cost_sum": 606, "expected_total_meals": 2424, "reported_total_meals": 1800, "reported_total_transportation": 200}}]`

### v3_hard_realbudget_eval_000018
- request: 天津 2026-07-06->2026-07-08 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 8899, "total": 7900, "diff": 999, "requested_budget": {"available": true, "amount": 7900, "scope": "total", "party_size": 3, "total": 7900, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "hard"}, "per_person_day": 877.78, "budget_level": "comfortable", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "hard", "amount": 7900, "target_min_ratio": 0.7, "target_max_ratio": 1.0, "target_min_total": 5500, "target_max_total": 7900, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 3, "room_count": 2, "priced_nights": 2, "expected_min_total_hotels": 4800, "reported_total_hotels": 4800, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 594, "expected_total_attractions": 1782, "reported_total_attractions": 1632, "meal_per_person_cost_sum": 1336, "expected_total_meals": 4008, "reported_total_meals": 2367, "reported_total_transportation": 100}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 594, "expected_total_attractions": 1782, "reported_total_attractions": 1632, "meal_per_person_cost_sum": 1336, "expected_total_meals": 4008, "reported_total_meals": 2367, "reported_total_transportation": 100}}]`

### v3_hard_realbudget_eval_000016
- request: 苏州 2026-06-06->2026-06-09 days=4 transport=自驾 hotel=亲子酒店 prefs=['亲子', '动物园', '海洋馆', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 135, "expected_total_attractions": 405, "reported_total_attractions": 345, "meal_per_person_cost_sum": 771, "expected_total_meals": 2313, "reported_total_meals": 1620, "reported_total_transportation": 500}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 135, "expected_total_attractions": 405, "reported_total_attractions": 345, "meal_per_person_cost_sum": 771, "expected_total_meals": 2313, "reported_total_meals": 1620, "reported_total_transportation": 500}}]`

### v3_hard_realbudget_eval_000013
- request: 武汉 2026-05-09->2026-05-13 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-05-11", "lunch": "肥肥虾庄(江汉路黄鹤楼店)", "dinner": "肥肥虾庄(江汉路M+店)"}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 163, "expected_total_attractions": 326, "reported_total_attractions": 316, "meal_per_person_cost_sum": 897, "expected_total_meals": 1794, "reported_total_meals": 1900, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 163, "expected_total_attractions": 326, "reported_total_attractions": 316, "meal_per_person_cost_sum": 897, "expected_total_meals": 1794, "reported_total_meals": 1900, "reported_total_transportation": 200}}]`

### v3_hard_realbudget_eval_000019
- request: 丽江 2026-05-11->2026-05-14 days=4 transport=打车 hotel=亲子酒店 prefs=['亲子', '老人友好', '博物馆', '城市公园', '特色餐厅']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 1142, "expected_total_attractions": 2284, "reported_total_attractions": 2528, "meal_per_person_cost_sum": 681, "expected_total_meals": 1362, "reported_total_meals": 1146, "reported_total_transportation": 800}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 1142, "expected_total_attractions": 2284, "reported_total_attractions": 2528, "meal_per_person_cost_sum": 681, "expected_total_meals": 1362, "reported_total_meals": 1146, "reported_total_transportation": 800}}]`

### v3_hard_realbudget_eval_000017
- request: 苏州 2026-05-09->2026-05-13 days=5 transport=公共交通 hotel=民宿 prefs=['小众展馆', '咖啡', '艺术', '城市漫步', '特色餐厅']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "肯达美术馆", "count": 5, "max_allowed": 1, "occurrences": [{"date": "2026-05-09", "day_index": 0, "name": "肯达美术馆"}, {"date": "2026-05-10", "day_index": 1, "name": "肯达美术馆"}, {"date": "2026-05-11", "day_index": 2, "name": "肯达美术馆"}, {"date": "2026-05-12", "day_index": 3, "name": "肯达美术馆"}, {"date": "2026-05-13", "day_index": 4, "name": "肯达美术馆"}]}]}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 4198, "total": 4200, "diff": -2, "requested_budget": {"available": true, "amount": 10100, "scope": "total", "party_size": 2, "total": 10100, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "soft"}, "per_person_day": 420.0, "budget_level": "comfortable", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "soft", "amount": 10100, "target_min_ratio": 0.7, "target_max_ratio": 1.1, "target_min_total": 7100, "target_max_total": 11100, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 4, "party_total": 2, "room_count": 1, "priced_nights": 4, "expected_min_total_hotels": 1200, "reported_total_hotels": 1200, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 502, "expected_total_attractions": 1004, "reported_total_attractions": 874, "meal_per_person_cost_sum": 782, "expected_total_meals": 1564, "reported_total_meals": 1924, "reported_total_transportation": 200}}]`

### v3_hard_realbudget_eval_000021
- request: 上海 2026-06-21->2026-06-24 days=4 transport=打车 hotel=高端酒店 prefs=['高端酒店', '艺术', '特色餐厅', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 1361, "expected_total_attractions": 2722, "reported_total_attractions": 2858, "meal_per_person_cost_sum": 3143, "expected_total_meals": 6286, "reported_total_meals": 5392, "reported_total_transportation": 900}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 1361, "expected_total_attractions": 2722, "reported_total_attractions": 2858, "meal_per_person_cost_sum": 3143, "expected_total_meals": 6286, "reported_total_meals": 5392, "reported_total_transportation": 900}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": true, "meal_cost_scale_ok": false, "budget_relationship_ok": false, "expected_total_hotels": 2550, "reported_total_hotels": 2550, "expected_total_attractions": 2722, "reported_total_attractions": 2858, "meal_scale_eval": {"ok": false, "party_total": 2, "budget_level": "premium", "per_person_lunch_dinner_floor": 70, "breakfast_policy": "excluded_from_meal_cost_scale", "meal_count": 12, "checked_count": 8, "failure_count": 1, "failures": [{"date": "2026-06-21", "type": "lunch", "name": "沈大成(南京东路店)", "estimated_cost": 43, "min_expected_cost": 70}]}}}]`
