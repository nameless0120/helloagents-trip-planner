# Rule Eval Report: 260511_realbudget_hard_w20_2gpu

- records: 300
- generations: `training/outputs/eval/by_model/sft_qwen25_7b_v3_260509_main_clean_cp2_v2b_valloss_lr6e5/260511_realbudget_hard_w20_2gpu/generations.jsonl`
- records_path: `training/data/v3/eval_hard/records.jsonl`

## Boolean Metrics

| Metric | Pass | Total | Rate |
| --- | ---: | ---: | ---: |
| accommodation_type_ok | 300 | 300 | 100.00% |
| attraction_budget_consistent | 67 | 300 | 22.33% |
| attraction_budget_party_relation_ok | 284 | 300 | 94.67% |
| attraction_count_ok | 300 | 300 | 100.00% |
| attraction_diversity_ok | 241 | 300 | 80.33% |
| attraction_grounding_ok | 291 | 300 | 97.00% |
| attraction_repeat_limit_ok | 241 | 300 | 80.33% |
| budget_arithmetic_consistent | 214 | 300 | 71.33% |
| budget_consistent | 214 | 300 | 71.33% |
| budget_level_aligned | 193 | 300 | 64.33% |
| budget_preference_aligned | 193 | 300 | 64.33% |
| budget_relationship_ok | 204 | 300 | 68.00% |
| budget_selection_ok | 147 | 300 | 49.00% |
| budget_user_constraint_ok | 281 | 300 | 93.67% |
| budget_within_user_budget | 299 | 300 | 99.67% |
| city_ok | 300 | 300 | 100.00% |
| date_range_ok | 300 | 300 | 100.00% |
| day_dates_ok | 300 | 300 | 100.00% |
| day_index_ok | 300 | 300 | 100.00% |
| days_len_ok | 300 | 300 | 100.00% |
| dpo_soft_pass | 125 | 300 | 41.67% |
| dpo_soft_recomputed_budget_pass | 93 | 300 | 31.00% |
| hard_pass | 284 | 300 | 94.67% |
| hotel_budget_covers_nights | 285 | 300 | 95.00% |
| hotel_budget_relation_ok | 288 | 300 | 96.00% |
| hotel_distance_placeholder_ok | 300 | 300 | 100.00% |
| hotel_grounding_ok | 300 | 300 | 100.00% |
| invalid_hotel_name_ok | 300 | 300 | 100.00% |
| json_extract_ok | 300 | 300 | 100.00% |
| legacy_hard_pass | 159 | 300 | 53.00% |
| location_object_ok | 300 | 300 | 100.00% |
| meal_budget_consistent | 0 | 300 | 0.00% |
| meal_complete | 300 | 300 | 100.00% |
| meal_cost_scale_ok | 224 | 300 | 74.67% |
| meal_diversity_ok | 232 | 300 | 77.33% |
| meal_grounding_ok | 293 | 300 | 97.67% |
| meal_lunch_dinner_same_day_ok | 279 | 300 | 93.00% |
| meal_repeat_limit_ok | 242 | 300 | 80.67% |
| meal_specific_ok | 300 | 300 | 100.00% |
| meal_valid_semantics_ok | 294 | 300 | 98.00% |
| middle_hotel_ok | 300 | 300 | 100.00% |
| recomputed_budget_fit_ok | 147 | 300 | 49.00% |
| recomputed_budget_hard_ok | 253 | 300 | 84.33% |
| recomputed_budget_level_aligned | 147 | 300 | 49.00% |
| recomputed_budget_preference_aligned | 147 | 300 | 49.00% |
| recomputed_budget_user_constraint_ok | 253 | 300 | 84.33% |
| recomputed_budget_within_user_budget | 287 | 300 | 95.67% |
| schema_ok | 300 | 300 | 100.00% |
| sft_budget_semantic_hard_pass | 174 | 300 | 58.00% |
| sft_hard_pass | 284 | 300 | 94.67% |
| sft_no_budget_sum_hard_pass | 284 | 300 | 94.67% |
| sft_strict_hard_pass | 0 | 300 | 0.00% |
| transportation_budget_nonnegative | 300 | 300 | 100.00% |
| weather_dates_ok | 300 | 300 | 100.00% |
| weather_match | 300 | 300 | 100.00% |

## Numeric Metrics

```json
{
  "attraction_diversity_unique_rate": {
    "avg": 0.9749,
    "p50": 1.0,
    "p90": 1.0
  },
  "attraction_grounding_rate": {
    "avg": 0.9962,
    "p50": 1.0,
    "p90": 1.0
  },
  "hotel_grounding_rate": {
    "avg": 1.0,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_diversity_unique_rate": {
    "avg": 0.8218,
    "p50": 0.8333,
    "p90": 1.0
  },
  "meal_food_pois_grounding_rate": {
    "avg": 0.9983,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_grounding_rate": {
    "avg": 0.9983,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_semantic_valid_rate": {
    "avg": 0.9986,
    "p50": 1.0,
    "p90": 1.0
  },
  "recomputed_budget_per_person_day": {
    "avg": 756.8904,
    "p50": 724.4,
    "p90": 1182.56
  },
  "recomputed_budget_total": {
    "avg": 8143.2633,
    "p50": 7241.0,
    "p90": 14230.0
  }
}
```

## Failure Types

```json
{
  "meal_budget_inconsistent": 300,
  "attraction_budget_inconsistent": 233,
  "budget_preference_mismatch": 107,
  "budget_relationship_mismatch": 96,
  "budget_arithmetic_inconsistent": 86,
  "meal_cost_scale_too_low": 76,
  "attraction_repeat_too_many": 59,
  "meal_repeat_too_many": 58,
  "meal_same_day_lunch_dinner_repeat": 21,
  "budget_hard_constraint_exceeded": 19,
  "hotel_budget_underestimated": 15,
  "meal_invalid_name": 6,
  "meal_grounding_miss": 1
}
```

## Failure Examples

### v3_hard_realbudget_eval_000004
- request: 张家界 2026-05-11->2026-05-13 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆']
- errors: `[{"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 318, "expected_total_attractions": 318, "reported_total_attractions": 318, "meal_per_person_cost_sum": 467, "expected_total_meals": 467, "reported_total_meals": 582, "reported_total_transportation": 500}}]`

### v3_hard_realbudget_eval_000008
- request: 大理 2026-05-11->2026-05-13 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 6200, "total": 6100, "diff": 100, "requested_budget": {"available": true, "amount": 8700, "scope": "total", "party_size": 3, "total": 8700, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "hard"}, "per_person_day": 677.78, "budget_level": "comfortable", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "hard", "amount": 8700, "target_min_ratio": 0.7, "target_max_ratio": 1.0, "target_min_total": 6100, "target_max_total": 8700, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 3, "room_count": 2, "priced_nights": 2, "expected_min_total_hotels": 3000, "reported_total_hotels": 3000, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 650, "expected_total_attractions": 1950, "reported_total_attractions": 1656, "meal_per_person_cost_sum": 442, "expected_total_meals": 1326, "reported_total_meals": 1344, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 650, "expected_total_attractions": 1950, "reported_total_attractions": 1656, "meal_per_person_cost_sum": 442, "expected_total_meals": 1326, "reported_total_meals": 1344, "reported_total_transportation": 200}}]`

### v3_hard_realbudget_eval_000001
- request: 桂林 2026-09-04->2026-09-07 days=4 transport=打车 hotel=高端酒店 prefs=['高端酒店', '艺术', '特色餐厅', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 805, "expected_total_attractions": 1610, "reported_total_attractions": 1370, "meal_per_person_cost_sum": 543, "expected_total_meals": 1086, "reported_total_meals": 1456, "reported_total_transportation": 1500}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 805, "expected_total_attractions": 1610, "reported_total_attractions": 1370, "meal_per_person_cost_sum": 543, "expected_total_meals": 1086, "reported_total_meals": 1456, "reported_total_transportation": 1500}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": true, "meal_cost_scale_ok": false, "budget_relationship_ok": false, "expected_total_hotels": 3600, "reported_total_hotels": 3600, "expected_total_attractions": 1610, "reported_total_attractions": 1370, "meal_scale_eval": {"ok": false, "party_total": 2, "budget_level": "premium", "per_person_lunch_dinner_floor": 70, "breakfast_policy": "excluded_from_meal_cost_scale", "meal_count": 12, "checked_count": 8, "failure_count": 4, "failures": [{"date": "2026-09-05", "type": "lunch", "name": "椿记烧鹅(中山店)", "estimated_cost": 56, "min_expected_cost": 70}, {"date": "2026-09-06", "type": "lunch", "name": "岩洞餐厅.天然岩洞特色菜(千古情店)", "estimated_cost": 66, "min_expected_cost": 70}, {"date": "2026-09-07", "type": "lunch", "name": "椿记烧鹅(西街店)", "estimated_cost": 56, "min_expected_cost": 70}, {"date": "2026-09-07", "type": "dinner", "name": "桂系手作·现熬黑糖珍珠鲜奶茶(桂林信息工程职业学院店)", "estimated_cost": 16, "min_expected_cost": 70}]}}}]`

### v3_hard_realbudget_eval_000006
- request: 南京 2026-07-06->2026-07-09 days=4 transport=自驾 hotel=亲子酒店 prefs=['亲子', '动物园', '海洋馆', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "玄武湖景区", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-07-06", "day_index": 0, "name": "玄武湖景区"}, {"date": "2026-07-09", "day_index": 3, "name": "玄武湖景区"}]}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 75, "expected_total_attractions": 225, "reported_total_attractions": 195, "meal_per_person_cost_sum": 912, "expected_total_meals": 2736, "reported_total_meals": 1656, "reported_total_transportation": 100}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 75, "expected_total_attractions": 225, "reported_total_attractions": 195, "meal_per_person_cost_sum": 912, "expected_total_meals": 2736, "reported_total_meals": 1656, "reported_total_transportation": 100}}]`

### v3_hard_realbudget_eval_000002
- request: 杭州 2026-05-01->2026-05-04 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '夜市', '老字号', '城市漫步']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 229, "expected_total_attractions": 916, "reported_total_attractions": 756, "meal_per_person_cost_sum": 840, "expected_total_meals": 3360, "reported_total_meals": 2832, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 229, "expected_total_attractions": 916, "reported_total_attractions": 756, "meal_per_person_cost_sum": 840, "expected_total_meals": 3360, "reported_total_meals": 2832, "reported_total_transportation": 200}}]`

### v3_hard_realbudget_eval_000005
- request: 广州 2026-07-06->2026-07-10 days=5 transport=公共交通 hotel=民宿 prefs=['摄影', '自然风光', '城市漫步', '本地菜']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "银灯食府", "count": 6, "max_allowed": 3, "occurrences": [{"date": "2026-07-06", "type": "breakfast", "name": "银灯食府(文化公园店)"}, {"date": "2026-07-06", "type": "dinner", "name": "银灯食府(丽丰国际中心店)"}, {"date": "2026-07-07", "type": "breakfast", "name": "银灯食府(文化公园店)"}, {"date": "2026-07-08", "type": "breakfast", "name": "银灯食府(文化公园店)"}, {"date": "2026-07-09", "type": "breakfast", "name": "银灯食府(文化公园店)"}, {"date": "2026-07-10", "type": "breakfast", "name": "银灯食府(文化公园店)"}]}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 185, "expected_total_attractions": 185, "reported_total_attractions": 225, "meal_per_person_cost_sum": 1593, "expected_total_meals": 1593, "reported_total_meals": 1026, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 185, "expected_total_attractions": 185, "reported_total_attractions": 225, "meal_per_person_cost_sum": 1593, "expected_total_meals": 1593, "reported_total_meals": 1026, "reported_total_transportation": 200}}]`

### v3_hard_realbudget_eval_000003
- request: 西安 2025-05-07->2025-05-11 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "西安博物院", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2025-05-10", "day_index": 3, "name": "西安博物院"}, {"date": "2025-05-11", "day_index": 4, "name": "西安博物院"}]}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 199, "expected_total_attractions": 398, "reported_total_attractions": 438, "meal_per_person_cost_sum": 751, "expected_total_meals": 1502, "reported_total_meals": 1418, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 199, "expected_total_attractions": 398, "reported_total_attractions": 438, "meal_per_person_cost_sum": 751, "expected_total_meals": 1502, "reported_total_meals": 1418, "reported_total_transportation": 200}}]`

### v3_hard_realbudget_eval_000000
- request: 昆明 2026-04-07->2026-04-11 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-04-09", "lunch": "莱茵春天西餐厅(正义店)", "dinner": "莱茵春天西餐厅(美辰店)"}]}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 17300, "total": 17200, "diff": 100, "requested_budget": {"available": true, "amount": 24700, "scope": "total", "party_size": 5, "total": 24700, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "hard"}, "per_person_day": 688.0, "budget_level": "comfortable", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "hard", "amount": 24700, "target_min_ratio": 0.7, "target_max_ratio": 1.0, "target_min_total": 17300, "target_max_total": 24700, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 4, "party_total": 5, "room_count": 3, "priced_nights": 4, "expected_min_total_hotels": 4800, "reported_total_hotels": 4800, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 5, "hotel_room_count": 3, "attraction_ticket_sum": 506, "expected_total_attractions": 2530, "reported_total_attractions": 2365, "meal_per_person_cost_sum": 936, "expected_total_meals": 4680, "reported_total_meals": 5735, "reported_total_transportation": 4400}}]`

### v3_hard_realbudget_eval_000010
- request: 西安 2026-08-05->2026-08-09 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "西安博物院", "count": 3, "max_allowed": 1, "occurrences": [{"date": "2026-08-05", "day_index": 0, "name": "西安博物院"}, {"date": "2026-08-08", "day_index": 3, "name": "西安博物院"}, {"date": "2026-08-09", "day_index": 4, "name": "西安博物院"}]}, {"name_key": "西安碑林博物馆", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-08-07", "day_index": 2, "name": "西安碑林博物馆"}, {"date": "2026-08-08", "day_index": 3, "name": "西安碑林博物馆"}]}]}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 21600, "total": 21595, "diff": 5, "requested_budget": {"available": true, "amount": 30900, "scope": "total", "party_size": 5, "total": 30900, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "hard"}, "per_person_day": 863.8, "budget_level": "comfortable", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "hard", "amount": 30900, "target_min_ratio": 0.7, "target_max_ratio": 1.0, "target_min_total": 21600, "target_max_total": 30900, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 4, "party_total": 5, "room_count": 3, "priced_nights": 4, "expected_min_total_hotels": 5400, "reported_total_hotels": 5400, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 5, "hotel_room_count": 3, "attraction_ticket_sum": 904, "expected_total_attractions": 4520, "reported_total_attractions": 3565, "meal_per_person_cost_sum": 826, "expected_total_meals": 4130, "reported_total_meals": 4635, "reported_total_transportation": 8000}}]`

### v3_hard_realbudget_eval_000007
- request: 成都 2026-05-11->2026-05-15 days=5 transport=公共交通 hotel=民宿 prefs=['小众展馆', '咖啡', '艺术', '城市漫步', '特色餐厅']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-05-12", "lunch": "悦百味·品质川菜(UPARK公园店)", "dinner": "悦百味·品质川菜(优品道店)"}, {"date": "2026-05-15", "lunch": "悦百味·品质川菜(武侯欢肆店)", "dinner": "悦百味·品质川菜(UPARK公园店)"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "悦百味·品质川菜", "count": 6, "max_allowed": 3, "occurrences": [{"date": "2026-05-12", "type": "lunch", "name": "悦百味·品质川菜(UPARK公园店)"}, {"date": "2026-05-12", "type": "dinner", "name": "悦百味·品质川菜(优品道店)"}, {"date": "2026-05-13", "type": "lunch", "name": "悦百味·品质川菜(悠方店)"}, {"date": "2026-05-14", "type": "lunch", "name": "悦百味·品质川菜(成都环贸ICD店)"}, {"date": "2026-05-15", "type": "lunch", "name": "悦百味·品质川菜(武侯欢肆店)"}, {"date": "2026-05-15", "type": "dinner", "name": "悦百味·品质川菜(UPARK公园店)"}]}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 1266, "expected_total_attractions": 2532, "reported_total_attractions": 2878, "meal_per_person_cost_sum": 1669, "expected_total_meals": 3338, "reported_total_meals": 3122, "reported_total_transportation": 500}}]`

### v3_hard_realbudget_eval_000014
- request: 成都 2026-06-06->2026-06-08 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆']
- errors: `[{"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 165, "expected_total_attractions": 165, "reported_total_attractions": 165, "meal_per_person_cost_sum": 550, "expected_total_meals": 550, "reported_total_meals": 452, "reported_total_transportation": 200}}]`

### v3_hard_realbudget_eval_000009
- request: 苏州 2026-04-30->2026-05-03 days=4 transport=打车 hotel=亲子酒店 prefs=['亲子', '老人友好', '博物馆', '城市公园', '特色餐厅']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 322, "expected_total_attractions": 1288, "reported_total_attractions": 1268, "meal_per_person_cost_sum": 732, "expected_total_meals": 2928, "reported_total_meals": 3504, "reported_total_transportation": 2400}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 322, "expected_total_attractions": 1288, "reported_total_attractions": 1268, "meal_per_person_cost_sum": 732, "expected_total_meals": 2928, "reported_total_meals": 3504, "reported_total_transportation": 2400}}]`

### v3_hard_realbudget_eval_000012
- request: 洛阳 2025-05-07->2025-05-10 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '夜市', '老字号', '城市漫步']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 298, "expected_total_attractions": 1192, "reported_total_attractions": 1232, "meal_per_person_cost_sum": 606, "expected_total_meals": 2424, "reported_total_meals": 1648, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 298, "expected_total_attractions": 1192, "reported_total_attractions": 1232, "meal_per_person_cost_sum": 606, "expected_total_meals": 2424, "reported_total_meals": 1648, "reported_total_transportation": 200}}]`

### v3_hard_realbudget_eval_000011
- request: 福州 2026-06-21->2026-06-24 days=4 transport=打车 hotel=高端酒店 prefs=['高端酒店', '艺术', '特色餐厅', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 515, "expected_total_attractions": 1030, "reported_total_attractions": 854, "meal_per_person_cost_sum": 1432, "expected_total_meals": 2864, "reported_total_meals": 3486, "reported_total_transportation": 1000}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 515, "expected_total_attractions": 1030, "reported_total_attractions": 854, "meal_per_person_cost_sum": 1432, "expected_total_meals": 2864, "reported_total_meals": 3486, "reported_total_transportation": 1000}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": true, "meal_cost_scale_ok": false, "budget_relationship_ok": false, "expected_total_hotels": 2250, "reported_total_hotels": 2250, "expected_total_attractions": 1030, "reported_total_attractions": 854, "meal_scale_eval": {"ok": false, "party_total": 2, "budget_level": "premium", "per_person_lunch_dinner_floor": 70, "breakfast_policy": "excluded_from_meal_cost_scale", "meal_count": 12, "checked_count": 8, "failure_count": 1, "failures": [{"date": "2026-06-24", "type": "lunch", "name": "陈金兰饮食店(柳前巷店)", "estimated_cost": 57, "min_expected_cost": 70}]}}}]`

### v3_hard_realbudget_eval_000018
- request: 天津 2026-07-06->2026-07-08 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 10104, "total": 9104, "diff": 1000, "requested_budget": {"available": true, "amount": 7900, "scope": "total", "party_size": 3, "total": 7900, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "hard"}, "per_person_day": 1011.56, "budget_level": "comfortable", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "hard", "amount": 7900, "target_min_ratio": 0.7, "target_max_ratio": 1.0, "target_min_total": 5500, "target_max_total": 7900, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": false, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 3, "room_count": 2, "priced_nights": 2, "expected_min_total_hotels": 4800, "reported_total_hotels": 4800, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 691, "expected_total_attractions": 2073, "reported_total_attractions": 1995, "meal_per_person_cost_sum": 1043, "expected_total_meals": 3129, "reported_total_meals": 2709, "reported_total_transportation": 600}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 691, "expected_total_attractions": 2073, "reported_total_attractions": 1995, "meal_per_person_cost_sum": 1043, "expected_total_meals": 3129, "reported_total_meals": 2709, "reported_total_transportation": 600}}]`

### v3_hard_realbudget_eval_000016
- request: 苏州 2026-06-06->2026-06-09 days=4 transport=自驾 hotel=亲子酒店 prefs=['亲子', '动物园', '海洋馆', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "苏州丝绸博物馆", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-06-09", "day_index": 3, "name": "苏州丝绸博物馆"}, {"date": "2026-06-09", "day_index": 3, "name": "苏州丝绸博物馆"}]}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 140, "expected_total_attractions": 420, "reported_total_attractions": 390, "meal_per_person_cost_sum": 527, "expected_total_meals": 1581, "reported_total_meals": 1530, "reported_total_transportation": 1000}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 140, "expected_total_attractions": 420, "reported_total_attractions": 390, "meal_per_person_cost_sum": 527, "expected_total_meals": 1581, "reported_total_meals": 1530, "reported_total_transportation": 1000}}]`

### v3_hard_realbudget_eval_000019
- request: 丽江 2026-05-11->2026-05-14 days=4 transport=打车 hotel=亲子酒店 prefs=['亲子', '老人友好', '博物馆', '城市公园', '特色餐厅']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 904, "expected_total_attractions": 1808, "reported_total_attractions": 1861, "meal_per_person_cost_sum": 737, "expected_total_meals": 1474, "reported_total_meals": 1174, "reported_total_transportation": 1000}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 904, "expected_total_attractions": 1808, "reported_total_attractions": 1861, "meal_per_person_cost_sum": 737, "expected_total_meals": 1474, "reported_total_meals": 1174, "reported_total_transportation": 1000}}]`

### v3_hard_realbudget_eval_000013
- request: 武汉 2026-05-09->2026-05-13 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "武昌江滩", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-05-12", "day_index": 3, "name": "武昌江滩"}, {"date": "2026-05-12", "day_index": 3, "name": "武昌江滩"}]}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 163, "expected_total_attractions": 326, "reported_total_attractions": 276, "meal_per_person_cost_sum": 876, "expected_total_meals": 1752, "reported_total_meals": 1858, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 163, "expected_total_attractions": 326, "reported_total_attractions": 276, "meal_per_person_cost_sum": 876, "expected_total_meals": 1752, "reported_total_meals": 1858, "reported_total_transportation": 200}}]`

### v3_hard_realbudget_eval_000017
- request: 苏州 2026-05-09->2026-05-13 days=5 transport=公共交通 hotel=民宿 prefs=['小众展馆', '咖啡', '艺术', '城市漫步', '特色餐厅']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "留园", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-05-10", "day_index": 1, "name": "留园"}, {"date": "2026-05-13", "day_index": 4, "name": "留园"}]}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "稻山村·苏州菜", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-05-10", "type": "lunch", "name": "稻山村·苏州菜(石路店)"}, {"date": "2026-05-11", "type": "dinner", "name": "稻山村·苏州菜(石路店)"}, {"date": "2026-05-12", "type": "lunch", "name": "稻山村·苏州菜(石路店)"}, {"date": "2026-05-13", "type": "lunch", "name": "稻山村·苏州菜(石路店)"}]}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 542, "expected_total_attractions": 1084, "reported_total_attractions": 1074, "meal_per_person_cost_sum": 1199, "expected_total_meals": 2398, "reported_total_meals": 2844, "reported_total_transportation": 1000}}]`

### v3_hard_realbudget_eval_000020
- request: 杭州 2026-06-21->2026-06-25 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "杭州植物园", "count": 3, "max_allowed": 1, "occurrences": [{"date": "2026-06-22", "day_index": 1, "name": "杭州植物园"}, {"date": "2026-06-24", "day_index": 3, "name": "杭州植物园"}, {"date": "2026-06-25", "day_index": 4, "name": "杭州植物园"}]}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 5, "hotel_room_count": 3, "attraction_ticket_sum": 100, "expected_total_attractions": 500, "reported_total_attractions": 450, "meal_per_person_cost_sum": 1000, "expected_total_meals": 5000, "reported_total_meals": 6090, "reported_total_transportation": 6360}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 5, "hotel_room_count": 3, "attraction_ticket_sum": 100, "expected_total_attractions": 500, "reported_total_attractions": 450, "meal_per_person_cost_sum": 1000, "expected_total_meals": 5000, "reported_total_meals": 6090, "reported_total_transportation": 6360}}]`
