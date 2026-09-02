# Rule Eval Report: 260507_realbudget_hard_w10

- records: 300
- generations: `training/outputs/eval/by_model/sft_qwen25_7b_v3_1000_cp2_v1/260507_realbudget_hard_w10/generations.jsonl`
- records_path: `training/data/v3/eval_hard/records.jsonl`

## Boolean Metrics

| Metric | Pass | Total | Rate |
| --- | ---: | ---: | ---: |
| accommodation_type_ok | 298 | 298 | 100.00% |
| attraction_budget_consistent | 49 | 298 | 16.44% |
| attraction_budget_party_relation_ok | 248 | 298 | 83.22% |
| attraction_count_ok | 296 | 298 | 99.33% |
| attraction_diversity_ok | 249 | 298 | 83.56% |
| attraction_grounding_ok | 288 | 298 | 96.64% |
| attraction_repeat_limit_ok | 249 | 298 | 83.56% |
| budget_arithmetic_consistent | 207 | 298 | 69.46% |
| budget_consistent | 207 | 298 | 69.46% |
| budget_level_aligned | 230 | 298 | 77.18% |
| budget_preference_aligned | 230 | 298 | 77.18% |
| budget_relationship_ok | 124 | 298 | 41.61% |
| budget_selection_ok | 155 | 298 | 52.01% |
| budget_user_constraint_ok | 281 | 298 | 94.30% |
| budget_within_user_budget | 293 | 298 | 98.32% |
| city_ok | 298 | 298 | 100.00% |
| date_range_ok | 298 | 298 | 100.00% |
| day_dates_ok | 298 | 298 | 100.00% |
| day_index_ok | 298 | 298 | 100.00% |
| days_len_ok | 298 | 298 | 100.00% |
| dpo_soft_pass | 153 | 298 | 51.34% |
| dpo_soft_recomputed_budget_pass | 102 | 298 | 34.23% |
| hard_pass | 277 | 298 | 92.95% |
| hotel_budget_covers_nights | 200 | 298 | 67.11% |
| hotel_budget_relation_ok | 219 | 298 | 73.49% |
| hotel_distance_placeholder_ok | 298 | 298 | 100.00% |
| hotel_grounding_ok | 298 | 298 | 100.00% |
| invalid_hotel_name_ok | 298 | 298 | 100.00% |
| json_extract_ok | 298 | 300 | 99.33% |
| legacy_hard_pass | 119 | 298 | 39.93% |
| location_object_ok | 298 | 298 | 100.00% |
| meal_budget_consistent | 1 | 298 | 0.34% |
| meal_complete | 298 | 298 | 100.00% |
| meal_cost_scale_ok | 198 | 298 | 66.44% |
| meal_diversity_ok | 257 | 298 | 86.24% |
| meal_grounding_ok | 287 | 298 | 96.31% |
| meal_lunch_dinner_same_day_ok | 288 | 298 | 96.64% |
| meal_repeat_limit_ok | 261 | 298 | 87.58% |
| meal_specific_ok | 297 | 298 | 99.66% |
| meal_valid_semantics_ok | 288 | 298 | 96.64% |
| middle_hotel_ok | 298 | 298 | 100.00% |
| recomputed_budget_fit_ok | 155 | 298 | 52.01% |
| recomputed_budget_hard_ok | 265 | 298 | 88.93% |
| recomputed_budget_level_aligned | 155 | 298 | 52.01% |
| recomputed_budget_preference_aligned | 155 | 298 | 52.01% |
| recomputed_budget_user_constraint_ok | 265 | 298 | 88.93% |
| recomputed_budget_within_user_budget | 290 | 298 | 97.32% |
| schema_ok | 298 | 300 | 99.33% |
| sft_budget_semantic_hard_pass | 102 | 298 | 34.23% |
| sft_hard_pass | 277 | 298 | 92.95% |
| sft_no_budget_sum_hard_pass | 277 | 298 | 92.95% |
| sft_strict_hard_pass | 0 | 298 | 0.00% |
| transportation_budget_nonnegative | 298 | 298 | 100.00% |
| weather_dates_ok | 298 | 298 | 100.00% |
| weather_match | 298 | 298 | 100.00% |

## Numeric Metrics

```json
{
  "attraction_diversity_unique_rate": {
    "avg": 0.9813,
    "p50": 1.0,
    "p90": 1.0
  },
  "attraction_grounding_rate": {
    "avg": 0.9971,
    "p50": 1.0,
    "p90": 1.0
  },
  "hotel_grounding_rate": {
    "avg": 1.0,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_diversity_unique_rate": {
    "avg": 0.8542,
    "p50": 0.8889,
    "p90": 1.0
  },
  "meal_food_pois_grounding_rate": {
    "avg": 0.9969,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_grounding_rate": {
    "avg": 0.9969,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_semantic_valid_rate": {
    "avg": 0.9972,
    "p50": 1.0,
    "p90": 1.0
  },
  "recomputed_budget_per_person_day": {
    "avg": 710.1092,
    "p50": 657.67,
    "p90": 1116.0
  },
  "recomputed_budget_total": {
    "avg": 7699.5805,
    "p50": 6876.0,
    "p90": 13275.0
  }
}
```

## Failure Types

```json
{
  "meal_budget_inconsistent": 297,
  "attraction_budget_inconsistent": 249,
  "budget_relationship_mismatch": 174,
  "meal_cost_scale_too_low": 100,
  "hotel_budget_underestimated": 98,
  "budget_arithmetic_inconsistent": 91,
  "budget_preference_mismatch": 68,
  "attraction_repeat_too_many": 49,
  "meal_repeat_too_many": 37,
  "budget_hard_constraint_exceeded": 17,
  "meal_same_day_lunch_dinner_repeat": 10,
  "meal_invalid_name": 10,
  "too_many_attractions": 2,
  "json_extract": 2,
  "meal_placeholder": 1,
  "meal_grounding_miss": 1
}
```

## Failure Examples

### v3_hard_realbudget_eval_000008
- request: 大理 2026-05-11->2026-05-13 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物']
- errors: `[{"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 115, "expected_total_attractions": 345, "reported_total_attractions": 345, "meal_per_person_cost_sum": 483, "expected_total_meals": 1449, "reported_total_meals": 1593, "reported_total_transportation": 1200}}]`

### v3_hard_realbudget_eval_000004
- request: 张家界 2026-05-11->2026-05-13 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 478, "expected_total_attractions": 478, "reported_total_attractions": 608, "meal_per_person_cost_sum": 500, "expected_total_meals": 500, "reported_total_meals": 616, "reported_total_transportation": 800}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 478, "expected_total_attractions": 478, "reported_total_attractions": 608, "meal_per_person_cost_sum": 500, "expected_total_meals": 500, "reported_total_meals": 616, "reported_total_transportation": 800}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": false, "meal_cost_scale_ok": true, "budget_relationship_ok": false, "expected_total_hotels": 800, "reported_total_hotels": 800, "expected_total_attractions": 478, "reported_total_attractions": 608, "meal_scale_eval": {"ok": true, "party_total": 1, "budget_level": "comfortable", "per_person_lunch_dinner_floor": 50, "breakfast_policy": "excluded_from_meal_cost_scale", "meal_count": 9, "checked_count": 6, "failure_count": 0, "failures": []}}}]`

### v3_hard_realbudget_eval_000006
- request: 南京 2026-07-06->2026-07-09 days=4 transport=自驾 hotel=亲子酒店 prefs=['亲子', '动物园', '海洋馆', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 75, "expected_total_attractions": 225, "reported_total_attractions": 150, "meal_per_person_cost_sum": 683, "expected_total_meals": 2049, "reported_total_meals": 2292, "reported_total_transportation": 600}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 75, "expected_total_attractions": 225, "reported_total_attractions": 150, "meal_per_person_cost_sum": 683, "expected_total_meals": 2049, "reported_total_meals": 2292, "reported_total_transportation": 600}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": false, "meal_cost_scale_ok": false, "budget_relationship_ok": false, "expected_total_hotels": 7500, "reported_total_hotels": 7500, "expected_total_attractions": 225, "reported_total_attractions": 150, "meal_scale_eval": {"ok": false, "party_total": 3, "budget_level": "standard", "per_person_lunch_dinner_floor": 35, "breakfast_policy": "excluded_from_meal_cost_scale", "meal_count": 12, "checked_count": 8, "failure_count": 1, "failures": [{"date": "2026-07-09", "type": "lunch", "name": "小潘记鸭血粉丝汤", "estimated_cost": 34, "min_expected_cost": 35}]}}}]`

### v3_hard_realbudget_eval_000002
- request: 杭州 2026-05-01->2026-05-04 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '夜市', '老字号', '城市漫步']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 160, "expected_total_attractions": 640, "reported_total_attractions": 480, "meal_per_person_cost_sum": 610, "expected_total_meals": 2440, "reported_total_meals": 2040, "reported_total_transportation": 500}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 160, "expected_total_attractions": 640, "reported_total_attractions": 480, "meal_per_person_cost_sum": 610, "expected_total_meals": 2440, "reported_total_meals": 2040, "reported_total_transportation": 500}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": false, "meal_cost_scale_ok": true, "budget_relationship_ok": false, "expected_total_hotels": 1500, "reported_total_hotels": 1500, "expected_total_attractions": 640, "reported_total_attractions": 480, "meal_scale_eval": {"ok": true, "party_total": 4, "budget_level": "limited", "per_person_lunch_dinner_floor": 25, "breakfast_policy": "excluded_from_meal_cost_scale", "meal_count": 12, "checked_count": 8, "failure_count": 0, "failures": []}}}]`

### v3_hard_realbudget_eval_000001
- request: 桂林 2026-09-04->2026-09-07 days=4 transport=打车 hotel=高端酒店 prefs=['高端酒店', '艺术', '特色餐厅', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 2, "room_count": 1, "priced_nights": 3, "expected_min_total_hotels": 3600, "reported_total_hotels": 7200, "diff": 3600, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 775, "expected_total_attractions": 1550, "reported_total_attractions": 1450, "meal_per_person_cost_sum": 664, "expected_total_meals": 1328, "reported_total_meals": 2652, "reported_total_transportation": 1000}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 775, "expected_total_attractions": 1550, "reported_total_attractions": 1450, "meal_per_person_cost_sum": 664, "expected_total_meals": 1328, "reported_total_meals": 2652, "reported_total_transportation": 1000}}]`

### v3_hard_realbudget_eval_000000
- request: 昆明 2026-04-07->2026-04-11 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 4, "party_total": 5, "room_count": 3, "priced_nights": 4, "expected_min_total_hotels": 4800, "reported_total_hotels": 4000, "diff": -800, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 5, "hotel_room_count": 3, "attraction_ticket_sum": 165, "expected_total_attractions": 825, "reported_total_attractions": 1150, "meal_per_person_cost_sum": 817, "expected_total_meals": 4085, "reported_total_meals": 3765, "reported_total_transportation": 1500}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 5, "hotel_room_count": 3, "attraction_ticket_sum": 165, "expected_total_attractions": 825, "reported_total_attractions": 1150, "meal_per_person_cost_sum": 817, "expected_total_meals": 4085, "reported_total_meals": 3765, "reported_total_transportation": 1500}}]`

### v3_hard_realbudget_eval_000005
- request: 广州 2026-07-06->2026-07-10 days=5 transport=公共交通 hotel=民宿 prefs=['摄影', '自然风光', '城市漫步', '本地菜']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 185, "expected_total_attractions": 185, "reported_total_attractions": 175, "meal_per_person_cost_sum": 1131, "expected_total_meals": 1131, "reported_total_meals": 1225, "reported_total_transportation": 400}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 185, "expected_total_attractions": 185, "reported_total_attractions": 175, "meal_per_person_cost_sum": 1131, "expected_total_meals": 1131, "reported_total_meals": 1225, "reported_total_transportation": 400}}]`

### v3_hard_realbudget_eval_000007
- request: 成都 2026-05-11->2026-05-15 days=5 transport=公共交通 hotel=民宿 prefs=['小众展馆', '咖啡', '艺术', '城市漫步', '特色餐厅']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-05-12", "lunch": "蜀宴赋", "dinner": "蜀宴赋"}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 392, "expected_total_attractions": 784, "reported_total_attractions": 692, "meal_per_person_cost_sum": 2600, "expected_total_meals": 5200, "reported_total_meals": 5948, "reported_total_transportation": 400}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 392, "expected_total_attractions": 784, "reported_total_attractions": 692, "meal_per_person_cost_sum": 2600, "expected_total_meals": 5200, "reported_total_meals": 5948, "reported_total_transportation": 400}}]`

### v3_hard_realbudget_eval_000003
- request: 西安 2025-05-07->2025-05-11 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "兴庆宫公园", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2025-05-07", "day_index": 0, "name": "兴庆宫公园"}, {"date": "2025-05-10", "day_index": 3, "name": "兴庆宫公园"}]}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 4, "party_total": 2, "room_count": 1, "priced_nights": 4, "expected_min_total_hotels": 1800, "reported_total_hotels": 3600, "diff": 1800, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 199, "expected_total_attractions": 398, "reported_total_attractions": 468, "meal_per_person_cost_sum": 704, "expected_total_meals": 1408, "reported_total_meals": 1848, "reported_total_transportation": 200}}]`

### v3_hard_realbudget_eval_000010
- request: 西安 2026-08-05->2026-08-09 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "西安博物院", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-08-07", "day_index": 2, "name": "西安博物院"}, {"date": "2026-08-09", "day_index": 4, "name": "西安博物院"}]}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 4, "party_total": 5, "room_count": 3, "priced_nights": 4, "expected_min_total_hotels": 5400, "reported_total_hotels": 9000, "diff": 3600, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 5, "hotel_room_count": 3, "attraction_ticket_sum": 199, "expected_total_attractions": 995, "reported_total_attractions": 1895, "meal_per_person_cost_sum": 769, "expected_total_meals": 3845, "reported_total_meals": 4605, "reported_total_transportation": 6100}}]`

### v3_hard_realbudget_eval_000011
- request: 福州 2026-06-21->2026-06-24 days=4 transport=打车 hotel=高端酒店 prefs=['高端酒店', '艺术', '特色餐厅', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 2, "room_count": 1, "priced_nights": 3, "expected_min_total_hotels": 2250, "reported_total_hotels": 4500, "diff": 2250, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 264, "expected_total_attractions": 528, "reported_total_attractions": 524, "meal_per_person_cost_sum": 1370, "expected_total_meals": 2740, "reported_total_meals": 3888, "reported_total_transportation": 1000}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 264, "expected_total_attractions": 528, "reported_total_attractions": 524, "meal_per_person_cost_sum": 1370, "expected_total_meals": 2740, "reported_total_meals": 3888, "reported_total_transportation": 1000}}]`

### v3_hard_realbudget_eval_000009
- request: 苏州 2026-04-30->2026-05-03 days=4 transport=打车 hotel=亲子酒店 prefs=['亲子', '老人友好', '博物馆', '城市公园', '特色餐厅']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 331, "expected_total_attractions": 1324, "reported_total_attractions": 1636, "meal_per_person_cost_sum": 830, "expected_total_meals": 3320, "reported_total_meals": 3516, "reported_total_transportation": 1200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 331, "expected_total_attractions": 1324, "reported_total_attractions": 1636, "meal_per_person_cost_sum": 830, "expected_total_meals": 3320, "reported_total_meals": 3516, "reported_total_transportation": 1200}}]`

### v3_hard_realbudget_eval_000014
- request: 成都 2026-06-06->2026-06-08 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 220, "expected_total_attractions": 220, "reported_total_attractions": 225, "meal_per_person_cost_sum": 1163, "expected_total_meals": 1163, "reported_total_meals": 1443, "reported_total_transportation": 800}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 220, "expected_total_attractions": 220, "reported_total_attractions": 225, "meal_per_person_cost_sum": 1163, "expected_total_meals": 1163, "reported_total_meals": 1443, "reported_total_transportation": 800}}]`

### v3_hard_realbudget_eval_000012
- request: 洛阳 2025-05-07->2025-05-10 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '夜市', '老字号', '城市漫步']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 4992, "total": 5092, "diff": -100, "requested_budget": {"available": true, "amount": 5800, "scope": "total", "party_size": 4, "total": 5800, "source": "budget_constraint", "budget_level": "limited", "strictness": "hard"}, "per_person_day": 318.25, "budget_level": "limited", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "limited", "strictness": "hard", "amount": 5800, "target_min_ratio": 0.72, "target_max_ratio": 1.0, "target_min_total": 4200, "target_max_total": 5800, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 4, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 1200, "reported_total_hotels": 1200, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 405, "expected_total_attractions": 1620, "reported_total_attractions": 1388, "meal_per_person_cost_sum": 564, "expected_total_meals": 2256, "reported_total_meals": 2204, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 405, "expected_total_attractions": 1620, "reported_total_attractions": 1388, "meal_per_person_cost_sum": 564, "expected_total_meals": 2256, "reported_total_meals": 2204, "reported_total_transportation": 200}}]`

### v3_hard_realbudget_eval_000018
- request: 天津 2026-07-06->2026-07-08 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 7923, "total": 8923, "diff": -1000, "requested_budget": {"available": true, "amount": 7900, "scope": "total", "party_size": 3, "total": 7900, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "hard"}, "per_person_day": 991.44, "budget_level": "comfortable", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "hard", "amount": 7900, "target_min_ratio": 0.7, "target_max_ratio": 1.0, "target_min_total": 5500, "target_max_total": 7900, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": false, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 3, "room_count": 2, "priced_nights": 2, "expected_min_total_hotels": 4800, "reported_total_hotels": 4800, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 368, "expected_total_attractions": 1104, "reported_total_attractions": 993, "meal_per_person_cost_sum": 989, "expected_total_meals": 2967, "reported_total_meals": 1830, "reported_total_transportation": 300}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 368, "expected_total_attractions": 1104, "reported_total_attractions": 993, "meal_per_person_cost_sum": 989, "expected_total_meals": 2967, "reported_total_meals": 1830, "reported_total_transportation": 300}}]`

### v3_hard_realbudget_eval_000016
- request: 苏州 2026-06-06->2026-06-09 days=4 transport=自驾 hotel=亲子酒店 prefs=['亲子', '动物园', '海洋馆', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 400, "expected_total_attractions": 1200, "reported_total_attractions": 1095, "meal_per_person_cost_sum": 903, "expected_total_meals": 2709, "reported_total_meals": 2205, "reported_total_transportation": 100}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 400, "expected_total_attractions": 1200, "reported_total_attractions": 1095, "meal_per_person_cost_sum": 903, "expected_total_meals": 2709, "reported_total_meals": 2205, "reported_total_transportation": 100}}, {"stage": "rule", "type": "budget_hard_constraint_exceeded", "details": {"part_sum": 10900, "total": 10900, "diff": 0, "requested_budget": {"available": true, "amount": 10000, "scope": "total", "party_size": 3, "total": 10000, "source": "budget_constraint", "budget_level": "standard", "strictness": "hard"}, "per_person_day": 908.33, "budget_level": "standard", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "standard", "strictness": "hard", "amount": 10000, "target_min_ratio": 0.6, "target_max_ratio": 1.0, "target_min_total": 6000, "target_max_total": 10000, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": true, "within_user_budget": true, "user_constraint_ok": false, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 3, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 7500, "reported_total_hotels": 7500, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_hard_realbudget_eval_000019
- request: 丽江 2026-05-11->2026-05-14 days=4 transport=打车 hotel=亲子酒店 prefs=['亲子', '老人友好', '博物馆', '城市公园', '特色餐厅']
- errors: `[{"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-05-13", "type": "lunch", "name": "大野三秋·雪山汤池度假酒店", "reason": "hotel_or_lodging_name"}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 2, "room_count": 1, "priced_nights": 3, "expected_min_total_hotels": 1500, "reported_total_hotels": 3000, "diff": 1500, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 760, "expected_total_attractions": 1520, "reported_total_attractions": 1400, "meal_per_person_cost_sum": 805, "expected_total_meals": 1610, "reported_total_meals": 1894, "reported_total_transportation": 1300}}]`

### v3_hard_realbudget_eval_000013
- request: 武汉 2026-05-09->2026-05-13 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "江汉关博物馆", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-05-12", "day_index": 3, "name": "江汉关博物馆"}, {"date": "2026-05-13", "day_index": 4, "name": "江汉关博物馆"}]}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 4, "party_total": 2, "room_count": 1, "priced_nights": 4, "expected_min_total_hotels": 1600, "reported_total_hotels": 2400, "diff": 800, "covers_nights": false}}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 4280, "total": 4180, "diff": 100, "requested_budget": {"available": true, "amount": 6800, "scope": "total", "party_size": 2, "total": 6800, "source": "budget_constraint", "budget_level": "standard", "strictness": "hard"}, "per_person_day": 418.0, "budget_level": "standard", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "standard", "strictness": "hard", "amount": 6800, "target_min_ratio": 0.6, "target_max_ratio": 1.0, "target_min_total": 4100, "target_max_total": 6800, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 4, "party_total": 2, "room_count": 1, "priced_nights": 4, "expected_min_total_hotels": 1600, "reported_total_hotels": 2400, "diff": 800, "covers_nights": false}, "hotel_budget_covers_nights": false}}]`

### v3_hard_realbudget_eval_000017
- request: 苏州 2026-05-09->2026-05-13 days=5 transport=公共交通 hotel=民宿 prefs=['小众展馆', '咖啡', '艺术', '城市漫步', '特色餐厅']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "留园", "count": 3, "max_allowed": 1, "occurrences": [{"date": "2026-05-10", "day_index": 1, "name": "留园"}, {"date": "2026-05-12", "day_index": 3, "name": "留园"}, {"date": "2026-05-13", "day_index": 4, "name": "留园"}]}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 4, "party_total": 2, "room_count": 1, "priced_nights": 4, "expected_min_total_hotels": 1200, "reported_total_hotels": 2400, "diff": 1200, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 410, "expected_total_attractions": 820, "reported_total_attractions": 1030, "meal_per_person_cost_sum": 1198, "expected_total_meals": 2396, "reported_total_meals": 3296, "reported_total_transportation": 400}}]`

### v3_hard_realbudget_eval_000020
- request: 杭州 2026-06-21->2026-06-25 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 4, "party_total": 5, "room_count": 3, "priced_nights": 4, "expected_min_total_hotels": 6000, "reported_total_hotels": 4000, "diff": -2000, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 5, "hotel_room_count": 3, "attraction_ticket_sum": 160, "expected_total_attractions": 800, "reported_total_attractions": 1150, "meal_per_person_cost_sum": 1277, "expected_total_meals": 6385, "reported_total_meals": 4800, "reported_total_transportation": 9000}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 5, "hotel_room_count": 3, "attraction_ticket_sum": 160, "expected_total_attractions": 800, "reported_total_attractions": 1150, "meal_per_person_cost_sum": 1277, "expected_total_meals": 6385, "reported_total_meals": 4800, "reported_total_transportation": 9000}}]`
