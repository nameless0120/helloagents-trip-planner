# Rule Eval Report: 260507_realbudget_hard_w10

- records: 300
- generations: `training/outputs/eval/by_model/sft_qwen25_7b_v3_1000_cp2_v2a/260507_realbudget_hard_w10/generations.jsonl`
- records_path: `training/data/v3/eval_hard/records.jsonl`

## Boolean Metrics

| Metric | Pass | Total | Rate |
| --- | ---: | ---: | ---: |
| accommodation_type_ok | 297 | 297 | 100.00% |
| attraction_budget_consistent | 54 | 297 | 18.18% |
| attraction_budget_party_relation_ok | 252 | 297 | 84.85% |
| attraction_count_ok | 296 | 297 | 99.66% |
| attraction_diversity_ok | 245 | 297 | 82.49% |
| attraction_grounding_ok | 289 | 297 | 97.31% |
| attraction_repeat_limit_ok | 245 | 297 | 82.49% |
| budget_arithmetic_consistent | 213 | 297 | 71.72% |
| budget_consistent | 213 | 297 | 71.72% |
| budget_level_aligned | 230 | 297 | 77.44% |
| budget_preference_aligned | 230 | 297 | 77.44% |
| budget_relationship_ok | 128 | 297 | 43.10% |
| budget_selection_ok | 164 | 297 | 55.22% |
| budget_user_constraint_ok | 285 | 297 | 95.96% |
| budget_within_user_budget | 292 | 297 | 98.32% |
| city_ok | 297 | 297 | 100.00% |
| date_range_ok | 297 | 297 | 100.00% |
| day_dates_ok | 297 | 297 | 100.00% |
| day_index_ok | 297 | 297 | 100.00% |
| days_len_ok | 297 | 297 | 100.00% |
| dpo_soft_pass | 152 | 297 | 51.18% |
| dpo_soft_recomputed_budget_pass | 109 | 297 | 36.70% |
| hard_pass | 273 | 297 | 91.92% |
| hotel_budget_covers_nights | 201 | 297 | 67.68% |
| hotel_budget_relation_ok | 221 | 297 | 74.41% |
| hotel_distance_placeholder_ok | 297 | 297 | 100.00% |
| hotel_grounding_ok | 296 | 297 | 99.66% |
| invalid_hotel_name_ok | 297 | 297 | 100.00% |
| json_extract_ok | 299 | 300 | 99.67% |
| legacy_hard_pass | 119 | 297 | 40.07% |
| location_object_ok | 297 | 297 | 100.00% |
| meal_budget_consistent | 1 | 297 | 0.34% |
| meal_complete | 297 | 297 | 100.00% |
| meal_cost_scale_ok | 183 | 297 | 61.62% |
| meal_diversity_ok | 251 | 297 | 84.51% |
| meal_grounding_ok | 283 | 297 | 95.29% |
| meal_lunch_dinner_same_day_ok | 286 | 297 | 96.30% |
| meal_repeat_limit_ok | 259 | 297 | 87.21% |
| meal_specific_ok | 297 | 297 | 100.00% |
| meal_valid_semantics_ok | 283 | 297 | 95.29% |
| middle_hotel_ok | 297 | 297 | 100.00% |
| recomputed_budget_fit_ok | 164 | 297 | 55.22% |
| recomputed_budget_hard_ok | 264 | 297 | 88.89% |
| recomputed_budget_level_aligned | 164 | 297 | 55.22% |
| recomputed_budget_preference_aligned | 164 | 297 | 55.22% |
| recomputed_budget_user_constraint_ok | 264 | 297 | 88.89% |
| recomputed_budget_within_user_budget | 290 | 297 | 97.64% |
| schema_ok | 297 | 300 | 99.00% |
| sft_budget_semantic_hard_pass | 99 | 297 | 33.33% |
| sft_hard_pass | 273 | 297 | 91.92% |
| sft_no_budget_sum_hard_pass | 273 | 297 | 91.92% |
| sft_strict_hard_pass | 0 | 297 | 0.00% |
| transportation_budget_nonnegative | 297 | 297 | 100.00% |
| weather_dates_ok | 297 | 297 | 100.00% |
| weather_match | 297 | 297 | 100.00% |

## Numeric Metrics

```json
{
  "attraction_diversity_unique_rate": {
    "avg": 0.9788,
    "p50": 1.0,
    "p90": 1.0
  },
  "attraction_grounding_rate": {
    "avg": 0.9969,
    "p50": 1.0,
    "p90": 1.0
  },
  "hotel_grounding_rate": {
    "avg": 0.9966,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_diversity_unique_rate": {
    "avg": 0.8675,
    "p50": 0.9,
    "p90": 1.0
  },
  "meal_food_pois_grounding_rate": {
    "avg": 0.9958,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_grounding_rate": {
    "avg": 0.9958,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_semantic_valid_rate": {
    "avg": 0.9958,
    "p50": 1.0,
    "p90": 1.0
  },
  "recomputed_budget_per_person_day": {
    "avg": 722.0512,
    "p50": 666.4,
    "p90": 1090.83
  },
  "recomputed_budget_total": {
    "avg": 7865.2593,
    "p50": 6956.0,
    "p90": 13236.0
  }
}
```

## Failure Types

```json
{
  "meal_budget_inconsistent": 296,
  "attraction_budget_inconsistent": 243,
  "budget_relationship_mismatch": 169,
  "meal_cost_scale_too_low": 114,
  "hotel_budget_underestimated": 96,
  "budget_arithmetic_inconsistent": 84,
  "budget_preference_mismatch": 67,
  "attraction_repeat_too_many": 52,
  "meal_repeat_too_many": 38,
  "meal_invalid_name": 14,
  "budget_hard_constraint_exceeded": 12,
  "meal_same_day_lunch_dinner_repeat": 11,
  "schema": 2,
  "json_extract": 1,
  "too_many_attractions": 1
}
```

## Failure Examples

### v3_hard_realbudget_eval_000004
- request: 张家界 2026-05-11->2026-05-13 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 398, "expected_total_attractions": 398, "reported_total_attractions": 418, "meal_per_person_cost_sum": 503, "expected_total_meals": 503, "reported_total_meals": 602, "reported_total_transportation": 1000}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 398, "expected_total_attractions": 398, "reported_total_attractions": 418, "meal_per_person_cost_sum": 503, "expected_total_meals": 503, "reported_total_meals": 602, "reported_total_transportation": 1000}}]`

### v3_hard_realbudget_eval_000008
- request: 大理 2026-05-11->2026-05-13 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "洱海公园", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-05-12", "day_index": 1, "name": "洱海公园"}, {"date": "2026-05-13", "day_index": 2, "name": "洱海公园"}]}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 166, "expected_total_attractions": 498, "reported_total_attractions": 516, "meal_per_person_cost_sum": 442, "expected_total_meals": 1326, "reported_total_meals": 1384, "reported_total_transportation": 1200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 166, "expected_total_attractions": 498, "reported_total_attractions": 516, "meal_per_person_cost_sum": 442, "expected_total_meals": 1326, "reported_total_meals": 1384, "reported_total_transportation": 1200}}]`

### v3_hard_realbudget_eval_000006
- request: 南京 2026-07-06->2026-07-09 days=4 transport=自驾 hotel=亲子酒店 prefs=['亲子', '动物园', '海洋馆', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 165, "expected_total_attractions": 495, "reported_total_attractions": 465, "meal_per_person_cost_sum": 663, "expected_total_meals": 1989, "reported_total_meals": 2076, "reported_total_transportation": 600}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 165, "expected_total_attractions": 495, "reported_total_attractions": 465, "meal_per_person_cost_sum": 663, "expected_total_meals": 1989, "reported_total_meals": 2076, "reported_total_transportation": 600}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": true, "meal_cost_scale_ok": false, "budget_relationship_ok": false, "expected_total_hotels": 7500, "reported_total_hotels": 7500, "expected_total_attractions": 495, "reported_total_attractions": 465, "meal_scale_eval": {"ok": false, "party_total": 3, "budget_level": "standard", "per_person_lunch_dinner_floor": 35, "breakfast_policy": "excluded_from_meal_cost_scale", "meal_count": 12, "checked_count": 8, "failure_count": 1, "failures": [{"date": "2026-07-09", "type": "lunch", "name": "小潘记鸭血粉丝汤", "estimated_cost": 34, "min_expected_cost": 35}]}}}]`

### v3_hard_realbudget_eval_000001
- request: 桂林 2026-09-04->2026-09-07 days=4 transport=打车 hotel=高端酒店 prefs=['高端酒店', '艺术', '特色餐厅', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 2, "room_count": 1, "priced_nights": 3, "expected_min_total_hotels": 3600, "reported_total_hotels": 7200, "diff": 3600, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 985, "expected_total_attractions": 1970, "reported_total_attractions": 1470, "meal_per_person_cost_sum": 726, "expected_total_meals": 1452, "reported_total_meals": 2630, "reported_total_transportation": 1800}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 985, "expected_total_attractions": 1970, "reported_total_attractions": 1470, "meal_per_person_cost_sum": 726, "expected_total_meals": 1452, "reported_total_meals": 2630, "reported_total_transportation": 1800}}]`

### v3_hard_realbudget_eval_000002
- request: 杭州 2026-05-01->2026-05-04 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '夜市', '老字号', '城市漫步']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 120, "expected_total_attractions": 480, "reported_total_attractions": 440, "meal_per_person_cost_sum": 656, "expected_total_meals": 2624, "reported_total_meals": 2064, "reported_total_transportation": 500}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 120, "expected_total_attractions": 480, "reported_total_attractions": 440, "meal_per_person_cost_sum": 656, "expected_total_meals": 2624, "reported_total_meals": 2064, "reported_total_transportation": 500}}]`

### v3_hard_realbudget_eval_000007
- request: 成都 2026-05-11->2026-05-15 days=5 transport=公共交通 hotel=民宿 prefs=['小众展馆', '咖啡', '艺术', '城市漫步', '特色餐厅']
- errors: `[{"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 245, "expected_total_attractions": 490, "reported_total_attractions": 490, "meal_per_person_cost_sum": 1525, "expected_total_meals": 3050, "reported_total_meals": 4394, "reported_total_transportation": 300}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": true, "meal_cost_scale_ok": false, "budget_relationship_ok": false, "expected_total_hotels": 1200, "reported_total_hotels": 1200, "expected_total_attractions": 490, "reported_total_attractions": 490, "meal_scale_eval": {"ok": false, "party_total": 2, "budget_level": "comfortable", "per_person_lunch_dinner_floor": 50, "breakfast_policy": "excluded_from_meal_cost_scale", "meal_count": 15, "checked_count": 10, "failure_count": 1, "failures": [{"date": "2026-05-15", "type": "dinner", "name": "叶婆婆钵钵鸡(太古里店)", "estimated_cost": 42, "min_expected_cost": 50}]}}}, {"stage": "rule", "type": "meal_cost_scale_too_low", "details": {"ok": false, "party_total": 2, "budget_level": "comfortable", "per_person_lunch_dinner_floor": 50, "breakfast_policy": "excluded_from_meal_cost_scale", "meal_count": 15, "checked_count": 10, "failure_count": 1, "failures": [{"date": "2026-05-15", "type": "dinner", "name": "叶婆婆钵钵鸡(太古里店)", "estimated_cost": 42, "min_expected_cost": 50}]}}]`

### v3_hard_realbudget_eval_000005
- request: 广州 2026-07-06->2026-07-10 days=5 transport=公共交通 hotel=民宿 prefs=['摄影', '自然风光', '城市漫步', '本地菜']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 585, "expected_total_attractions": 585, "reported_total_attractions": 575, "meal_per_person_cost_sum": 1265, "expected_total_meals": 1265, "reported_total_meals": 1275, "reported_total_transportation": 400}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 585, "expected_total_attractions": 585, "reported_total_attractions": 575, "meal_per_person_cost_sum": 1265, "expected_total_meals": 1265, "reported_total_meals": 1275, "reported_total_transportation": 400}}]`

### v3_hard_realbudget_eval_000003
- request: 西安 2025-05-07->2025-05-11 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 4, "party_total": 2, "room_count": 1, "priced_nights": 4, "expected_min_total_hotels": 1800, "reported_total_hotels": 3600, "diff": 1800, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 319, "expected_total_attractions": 638, "reported_total_attractions": 688, "meal_per_person_cost_sum": 698, "expected_total_meals": 1396, "reported_total_meals": 1878, "reported_total_transportation": 300}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 319, "expected_total_attractions": 638, "reported_total_attractions": 688, "meal_per_person_cost_sum": 698, "expected_total_meals": 1396, "reported_total_meals": 1878, "reported_total_transportation": 300}}]`

### v3_hard_realbudget_eval_000000
- request: 昆明 2026-04-07->2026-04-11 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "云南省博物馆", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-04-07", "day_index": 0, "name": "云南省博物馆"}, {"date": "2026-04-10", "day_index": 3, "name": "云南省博物馆"}]}, {"name_key": "云南美术馆", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-04-07", "day_index": 0, "name": "云南美术馆(五一路)"}, {"date": "2026-04-11", "day_index": 4, "name": "云南美术馆(五一路)"}]}, {"name_key": "昆明老街钱王街", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-04-09", "day_index": 2, "name": "昆明老街钱王街"}, {"date": "2026-04-11", "day_index": 4, "name": "昆明老街钱王街"}]}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 4, "party_total": 5, "room_count": 3, "priced_nights": 4, "expected_min_total_hotels": 4800, "reported_total_hotels": 4000, "diff": -800, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 5, "hotel_room_count": 3, "attraction_ticket_sum": 100, "expected_total_attractions": 500, "reported_total_attractions": 400, "meal_per_person_cost_sum": 848, "expected_total_meals": 4240, "reported_total_meals": 4550, "reported_total_transportation": 1500}}]`

### v3_hard_realbudget_eval_000010
- request: 西安 2026-08-05->2026-08-09 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "西安博物院", "count": 3, "max_allowed": 1, "occurrences": [{"date": "2026-08-07", "day_index": 2, "name": "西安博物院"}, {"date": "2026-08-08", "day_index": 3, "name": "西安博物院"}, {"date": "2026-08-09", "day_index": 4, "name": "西安博物院"}]}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 4, "party_total": 5, "room_count": 3, "priced_nights": 4, "expected_min_total_hotels": 5400, "reported_total_hotels": 9000, "diff": 3600, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 5, "hotel_room_count": 3, "attraction_ticket_sum": 267, "expected_total_attractions": 1335, "reported_total_attractions": 2490, "meal_per_person_cost_sum": 680, "expected_total_meals": 3400, "reported_total_meals": 4675, "reported_total_transportation": 1500}}]`

### v3_hard_realbudget_eval_000011
- request: 福州 2026-06-21->2026-06-24 days=4 transport=打车 hotel=高端酒店 prefs=['高端酒店', '艺术', '特色餐厅', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 2, "room_count": 1, "priced_nights": 3, "expected_min_total_hotels": 2250, "reported_total_hotels": 4500, "diff": 2250, "covers_nights": false}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 344, "expected_total_attractions": 688, "reported_total_attractions": 688, "meal_per_person_cost_sum": 1757, "expected_total_meals": 3514, "reported_total_meals": 4044, "reported_total_transportation": 1000}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": false, "attraction_budget_party_relation_ok": true, "meal_cost_scale_ok": true, "budget_relationship_ok": false, "expected_total_hotels": 2250, "reported_total_hotels": 4500, "expected_total_attractions": 688, "reported_total_attractions": 688, "meal_scale_eval": {"ok": true, "party_total": 2, "budget_level": "premium", "per_person_lunch_dinner_floor": 70, "breakfast_policy": "excluded_from_meal_cost_scale", "meal_count": 12, "checked_count": 8, "failure_count": 0, "failures": []}}}]`

### v3_hard_realbudget_eval_000014
- request: 成都 2026-06-06->2026-06-08 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆']
- errors: `[{"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 165, "expected_total_attractions": 165, "reported_total_attractions": 165, "meal_per_person_cost_sum": 753, "expected_total_meals": 753, "reported_total_meals": 1129, "reported_total_transportation": 1200}}]`

### v3_hard_realbudget_eval_000009
- request: 苏州 2026-04-30->2026-05-03 days=4 transport=打车 hotel=亲子酒店 prefs=['亲子', '老人友好', '博物馆', '城市公园', '特色餐厅']
- errors: `[{"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-05-02", "type": "dinner", "name": "江南雅厨·隐轩精致雅宴(相城店)", "reason": "unknown_food_semantics"}, {"date": "2026-05-03", "type": "dinner", "name": "江南雅厨·隐轩精致雅宴(相城店)", "reason": "unknown_food_semantics"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "江南雅厨·非遗苏州菜", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-04-30", "type": "lunch", "name": "江南雅厨·非遗苏州菜(李公堤店)"}, {"date": "2026-05-01", "type": "lunch", "name": "江南雅厨·非遗苏州菜(李公堤店)"}, {"date": "2026-05-02", "type": "lunch", "name": "江南雅厨·非遗苏州菜(李公堤店)"}, {"date": "2026-05-03", "type": "lunch", "name": "江南雅厨·非遗苏州菜(李公堤店)"}]}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 300, "expected_total_attractions": 1200, "reported_total_attractions": 1640, "meal_per_person_cost_sum": 1619, "expected_total_meals": 6476, "reported_total_meals": 4744, "reported_total_transportation": 1000}}]`

### v3_hard_realbudget_eval_000012
- request: 洛阳 2025-05-07->2025-05-10 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '夜市', '老字号', '城市漫步']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 378, "expected_total_attractions": 1512, "reported_total_attractions": 1632, "meal_per_person_cost_sum": 577, "expected_total_meals": 2308, "reported_total_meals": 1668, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 378, "expected_total_attractions": 1512, "reported_total_attractions": 1632, "meal_per_person_cost_sum": 577, "expected_total_meals": 2308, "reported_total_meals": 1668, "reported_total_transportation": 200}}]`

### v3_hard_realbudget_eval_000018
- request: 天津 2026-07-06->2026-07-08 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 9400, "total": 9300, "diff": 100, "requested_budget": {"available": true, "amount": 7900, "scope": "total", "party_size": 3, "total": 7900, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "hard"}, "per_person_day": 1033.33, "budget_level": "comfortable", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "hard", "amount": 7900, "target_min_ratio": 0.7, "target_max_ratio": 1.0, "target_min_total": 5500, "target_max_total": 7900, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": false, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 3, "room_count": 2, "priced_nights": 2, "expected_min_total_hotels": 4800, "reported_total_hotels": 4800, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 223, "expected_total_attractions": 669, "reported_total_attractions": 759, "meal_per_person_cost_sum": 1071, "expected_total_meals": 3213, "reported_total_meals": 2841, "reported_total_transportation": 1000}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 223, "expected_total_attractions": 669, "reported_total_attractions": 759, "meal_per_person_cost_sum": 1071, "expected_total_meals": 3213, "reported_total_meals": 2841, "reported_total_transportation": 1000}}]`

### v3_hard_realbudget_eval_000016
- request: 苏州 2026-06-06->2026-06-09 days=4 transport=自驾 hotel=亲子酒店 prefs=['亲子', '动物园', '海洋馆', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 400, "expected_total_attractions": 1200, "reported_total_attractions": 1290, "meal_per_person_cost_sum": 760, "expected_total_meals": 2280, "reported_total_meals": 2136, "reported_total_transportation": 1000}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 400, "expected_total_attractions": 1200, "reported_total_attractions": 1290, "meal_per_person_cost_sum": 760, "expected_total_meals": 2280, "reported_total_meals": 2136, "reported_total_transportation": 1000}}, {"stage": "rule", "type": "budget_hard_constraint_exceeded", "details": {"part_sum": 11926, "total": 11926, "diff": 0, "requested_budget": {"available": true, "amount": 10000, "scope": "total", "party_size": 3, "total": 10000, "source": "budget_constraint", "budget_level": "standard", "strictness": "hard"}, "per_person_day": 993.83, "budget_level": "standard", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "standard", "strictness": "hard", "amount": 10000, "target_min_ratio": 0.6, "target_max_ratio": 1.0, "target_min_total": 6000, "target_max_total": 10000, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": true, "within_user_budget": true, "user_constraint_ok": false, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 3, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 7500, "reported_total_hotels": 7500, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_hard_realbudget_eval_000013
- request: 武汉 2026-05-09->2026-05-13 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 4, "party_total": 2, "room_count": 1, "priced_nights": 4, "expected_min_total_hotels": 1600, "reported_total_hotels": 2400, "diff": 800, "covers_nights": false}}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 5100, "total": 4900, "diff": 200, "requested_budget": {"available": true, "amount": 6800, "scope": "total", "party_size": 2, "total": 6800, "source": "budget_constraint", "budget_level": "standard", "strictness": "hard"}, "per_person_day": 490.0, "budget_level": "standard", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "standard", "strictness": "hard", "amount": 6800, "target_min_ratio": 0.6, "target_max_ratio": 1.0, "target_min_total": 4100, "target_max_total": 6800, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 4, "party_total": 2, "room_count": 1, "priced_nights": 4, "expected_min_total_hotels": 1600, "reported_total_hotels": 2400, "diff": 800, "covers_nights": false}, "hotel_budget_covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 239, "expected_total_attractions": 478, "reported_total_attractions": 446, "meal_per_person_cost_sum": 945, "expected_total_meals": 1890, "reported_total_meals": 1454, "reported_total_transportation": 800}}]`

### v3_hard_realbudget_eval_000019
- request: 丽江 2026-05-11->2026-05-14 days=4 transport=打车 hotel=亲子酒店 prefs=['亲子', '老人友好', '博物馆', '城市公园', '特色餐厅']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 2, "room_count": 1, "priced_nights": 3, "expected_min_total_hotels": 1500, "reported_total_hotels": 3000, "diff": 1500, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 740, "expected_total_attractions": 1480, "reported_total_attractions": 1440, "meal_per_person_cost_sum": 739, "expected_total_meals": 1478, "reported_total_meals": 1462, "reported_total_transportation": 400}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 740, "expected_total_attractions": 1480, "reported_total_attractions": 1440, "meal_per_person_cost_sum": 739, "expected_total_meals": 1478, "reported_total_meals": 1462, "reported_total_transportation": 400}}]`

### v3_hard_realbudget_eval_000017
- request: 苏州 2026-05-09->2026-05-13 days=5 transport=公共交通 hotel=民宿 prefs=['小众展馆', '咖啡', '艺术', '城市漫步', '特色餐厅']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "留园", "count": 3, "max_allowed": 1, "occurrences": [{"date": "2026-05-10", "day_index": 1, "name": "留园"}, {"date": "2026-05-12", "day_index": 3, "name": "留园"}, {"date": "2026-05-13", "day_index": 4, "name": "留园"}]}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 4, "party_total": 2, "room_count": 1, "priced_nights": 4, "expected_min_total_hotels": 1200, "reported_total_hotels": 2400, "diff": 1200, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 410, "expected_total_attractions": 820, "reported_total_attractions": 840, "meal_per_person_cost_sum": 1230, "expected_total_meals": 2460, "reported_total_meals": 3244, "reported_total_transportation": 600}}]`

### v3_hard_realbudget_eval_000020
- request: 杭州 2026-06-21->2026-06-25 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "杭州西湖风景名胜区-太子湾公园", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-06-21", "day_index": 0, "name": "杭州西湖风景名胜区-太子湾公园"}, {"date": "2026-06-23", "day_index": 2, "name": "杭州西湖风景名胜区-太子湾公园"}]}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 4, "party_total": 5, "room_count": 3, "priced_nights": 4, "expected_min_total_hotels": 6000, "reported_total_hotels": 4000, "diff": -2000, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 5, "hotel_room_count": 3, "attraction_ticket_sum": 376, "expected_total_attractions": 1880, "reported_total_attractions": 2700, "meal_per_person_cost_sum": 1357, "expected_total_meals": 6785, "reported_total_meals": 4800, "reported_total_transportation": 7400}}]`
