# Rule Eval Report: sft_qwen25_7b_v3_1000_cp2_v1_A_C_smoke20

- records: 20
- generations: `training/outputs/eval/sft_qwen25_7b_v3_1000_cp2_v1_A_C_smoke20/generations.jsonl`
- records_path: `training/data/v3/eval_harder_prompt_ablation_20260505/A_C/records.jsonl`

## Boolean Metrics

| Metric | Pass | Total | Rate |
| --- | ---: | ---: | ---: |
| accommodation_type_ok | 20 | 20 | 100.00% |
| attraction_budget_consistent | 3 | 20 | 15.00% |
| attraction_budget_party_relation_ok | 11 | 20 | 55.00% |
| attraction_count_ok | 20 | 20 | 100.00% |
| attraction_diversity_ok | 12 | 20 | 60.00% |
| attraction_grounding_ok | 19 | 20 | 95.00% |
| attraction_repeat_limit_ok | 12 | 20 | 60.00% |
| budget_arithmetic_consistent | 15 | 20 | 75.00% |
| budget_consistent | 15 | 20 | 75.00% |
| budget_level_aligned | 14 | 20 | 70.00% |
| budget_preference_aligned | 14 | 20 | 70.00% |
| budget_relationship_ok | 3 | 20 | 15.00% |
| budget_user_constraint_ok | 16 | 20 | 80.00% |
| budget_within_user_budget | 18 | 20 | 90.00% |
| city_ok | 20 | 20 | 100.00% |
| date_range_ok | 20 | 20 | 100.00% |
| day_dates_ok | 19 | 20 | 95.00% |
| day_index_ok | 20 | 20 | 100.00% |
| days_len_ok | 19 | 20 | 95.00% |
| dpo_soft_pass | 0 | 20 | 0.00% |
| hard_pass | 0 | 20 | 0.00% |
| hotel_budget_covers_nights | 9 | 20 | 45.00% |
| hotel_budget_relation_ok | 9 | 20 | 45.00% |
| hotel_distance_placeholder_ok | 20 | 20 | 100.00% |
| hotel_grounding_ok | 20 | 20 | 100.00% |
| invalid_hotel_name_ok | 20 | 20 | 100.00% |
| json_extract_ok | 20 | 20 | 100.00% |
| legacy_hard_pass | 5 | 20 | 25.00% |
| location_object_ok | 20 | 20 | 100.00% |
| meal_budget_consistent | 0 | 20 | 0.00% |
| meal_complete | 20 | 20 | 100.00% |
| meal_cost_scale_ok | 16 | 20 | 80.00% |
| meal_diversity_ok | 17 | 20 | 85.00% |
| meal_grounding_ok | 15 | 20 | 75.00% |
| meal_lunch_dinner_same_day_ok | 18 | 20 | 90.00% |
| meal_repeat_limit_ok | 18 | 20 | 90.00% |
| meal_specific_ok | 19 | 20 | 95.00% |
| meal_valid_semantics_ok | 15 | 20 | 75.00% |
| middle_hotel_ok | 20 | 20 | 100.00% |
| schema_ok | 20 | 20 | 100.00% |
| sft_budget_semantic_hard_pass | 1 | 20 | 5.00% |
| sft_hard_pass | 0 | 20 | 0.00% |
| transportation_budget_nonnegative | 20 | 20 | 100.00% |
| weather_dates_ok | 19 | 20 | 95.00% |
| weather_match | 19 | 20 | 95.00% |

## Numeric Metrics

```json
{
  "attraction_diversity_unique_rate": {
    "avg": 0.9589,
    "p50": 1.0,
    "p90": 1.0
  },
  "attraction_grounding_rate": {
    "avg": 0.9955,
    "p50": 1.0,
    "p90": 1.0
  },
  "hotel_grounding_rate": {
    "avg": 1.0,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_diversity_unique_rate": {
    "avg": 0.5329,
    "p50": 0.625,
    "p90": 0.9
  },
  "meal_food_pois_grounding_rate": {
    "avg": 0.8911,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_grounding_rate": {
    "avg": 0.8911,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_semantic_valid_rate": {
    "avg": 0.9311,
    "p50": 1.0,
    "p90": 1.0
  }
}
```

## Failure Types

```json
{
  "meal_budget_inconsistent": 20,
  "attraction_budget_inconsistent": 17,
  "budget_relationship_mismatch": 17,
  "hotel_budget_underestimated": 11,
  "attraction_repeat_too_many": 8,
  "budget_preference_mismatch": 6,
  "budget_arithmetic_inconsistent": 5,
  "meal_invalid_name": 5,
  "meal_cost_scale_too_low": 4,
  "budget_hard_constraint_exceeded": 4,
  "meal_same_day_lunch_dinner_repeat": 2,
  "meal_repeat_too_many": 2,
  "meal_placeholder": 1,
  "weather_mismatch": 1
}
```

## Failure Examples

### v3_harder_eval_000004
- request: 张家界 2026-05-07->2026-05-09 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 160, "expected_total_attractions": 160, "reported_total_attractions": 240, "meal_per_person_cost_sum": 418, "expected_total_meals": 418, "reported_total_meals": 260, "reported_total_transportation": 100}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 160, "expected_total_attractions": 160, "reported_total_attractions": 240, "meal_per_person_cost_sum": 418, "expected_total_meals": 418, "reported_total_meals": 260, "reported_total_transportation": 100}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": false, "meal_cost_scale_ok": false, "budget_relationship_ok": false, "expected_total_hotels": 800, "reported_total_hotels": 800, "expected_total_attractions": 160, "reported_total_attractions": 240, "meal_scale_eval": {"ok": false, "party_total": 1, "budget_level": "comfortable", "per_person_lunch_dinner_floor": 50, "per_person_breakfast_floor": 20, "meal_count": 9, "checked_count": 6, "failure_count": 2, "failures": [{"date": "2026-05-09", "type": "lunch", "name": "业华湘·特色菜", "estimated_cost": 35, "min_expected_cost": 50}, {"date": "2026-05-09", "type": "dinner", "name": "自由人(张家界国光实验学校店)", "estimated_cost": 7, "min_expected_cost": 50}]}}}]`

### v3_harder_eval_000006
- request: 南京 2026-07-02->2026-07-05 days=4 transport=自驾 hotel=亲子酒店 prefs=['亲子', '动物园', '海洋馆', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 3, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 3300, "reported_total_hotels": 1650, "diff": -1650, "covers_nights": false}}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 3035, "total": 2935, "diff": 100, "requested_budget": {"available": true, "amount": 4000, "scope": "total", "party_size": 3, "total": 4000, "source": "budget_constraint", "budget_level": "standard", "strictness": "hard"}, "per_person_day": 244.58, "budget_level": "standard", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "standard", "strictness": "hard", "amount": 4000, "target_min_ratio": 0.55, "target_max_ratio": 1.0, "target_min_total": 2200, "target_max_total": 4000, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 3, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 3300, "reported_total_hotels": 1650, "diff": -1650, "covers_nights": false}, "hotel_budget_covers_nights": false}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 35, "expected_total_attractions": 105, "reported_total_attractions": 105, "meal_per_person_cost_sum": 1560, "expected_total_meals": 4680, "reported_total_meals": 1080, "reported_total_transportation": 200}}]`

### v3_harder_eval_000002
- request: 杭州 2026-04-27->2026-04-30 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '夜市', '老字号', '城市漫步']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 4, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 1500, "reported_total_hotels": 750, "diff": -750, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 160, "expected_total_attractions": 640, "reported_total_attractions": 240, "meal_per_person_cost_sum": 1167, "expected_total_meals": 4668, "reported_total_meals": 1212, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 160, "expected_total_attractions": 640, "reported_total_attractions": 240, "meal_per_person_cost_sum": 1167, "expected_total_meals": 4668, "reported_total_meals": 1212, "reported_total_transportation": 200}}]`

### v3_harder_eval_000001
- request: 桂林 2026-08-31->2026-09-03 days=4 transport=打车 hotel=高端酒店 prefs=['高端酒店', '艺术', '特色餐厅', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 2, "room_count": 1, "priced_nights": 3, "expected_min_total_hotels": 2250, "reported_total_hotels": 4500, "diff": 2250, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 415, "expected_total_attractions": 830, "reported_total_attractions": 1010, "meal_per_person_cost_sum": 1086, "expected_total_meals": 2172, "reported_total_meals": 1680, "reported_total_transportation": 1200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 415, "expected_total_attractions": 830, "reported_total_attractions": 1010, "meal_per_person_cost_sum": 1086, "expected_total_meals": 2172, "reported_total_meals": 1680, "reported_total_transportation": 1200}}]`

### v3_harder_eval_000000
- request: 昆明 2026-04-03->2026-04-07 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-04-03", "type": "lunch", "name": "云南过桥米线", "reason": "unknown_food_semantics"}, {"date": "2026-04-04", "type": "lunch", "name": "过桥米线", "reason": "unknown_food_semantics"}, {"date": "2026-04-05", "type": "lunch", "name": "过桥米线", "reason": "unknown_food_semantics"}, {"date": "2026-04-06", "type": "lunch", "name": "过桥米线", "reason": "unknown_food_semantics"}, {"date": "2026-04-07", "type": "lunch", "name": "过桥米线", "reason": "unknown_food_semantics"}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 4, "party_total": 5, "room_count": 3, "priced_nights": 4, "expected_min_total_hotels": 4800, "reported_total_hotels": 1600, "diff": -3200, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 5, "hotel_room_count": 3, "attraction_ticket_sum": 303, "expected_total_attractions": 1515, "reported_total_attractions": 1130, "meal_per_person_cost_sum": 800, "expected_total_meals": 4000, "reported_total_meals": 1200, "reported_total_transportation": 1000}}]`

### v3_harder_eval_000003
- request: 西安 2025-05-03->2025-05-07 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "陕西历史博物馆", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2025-05-03", "day_index": 0, "name": "陕西历史博物馆"}, {"date": "2025-05-05", "day_index": 2, "name": "陕西历史博物馆"}]}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 319, "expected_total_attractions": 638, "reported_total_attractions": 579, "meal_per_person_cost_sum": 600, "expected_total_meals": 1200, "reported_total_meals": 1080, "reported_total_transportation": 300}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 319, "expected_total_attractions": 638, "reported_total_attractions": 579, "meal_per_person_cost_sum": 600, "expected_total_meals": 1200, "reported_total_meals": 1080, "reported_total_transportation": 300}}]`

### v3_harder_eval_000005
- request: 广州 2026-07-02->2026-07-06 days=5 transport=公共交通 hotel=民宿 prefs=['摄影', '自然风光', '城市漫步', '本地菜']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "东山湖公园", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-07-04", "day_index": 2, "name": "东山湖公园"}, {"date": "2026-07-05", "day_index": 3, "name": "东山湖公园"}]}]}, {"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-07-06", "lunch": "滋粥楼·顺德菜(番禺广场总店)", "dinner": "滋粥楼·顺德菜(南村万博长隆商圈店)"}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 545, "expected_total_attractions": 545, "reported_total_attractions": 1015, "meal_per_person_cost_sum": 1096, "expected_total_meals": 1096, "reported_total_meals": 1042, "reported_total_transportation": 200}}]`

### v3_harder_eval_000007
- request: 成都 2026-05-07->2026-05-11 days=5 transport=公共交通 hotel=民宿 prefs=['小众展馆', '咖啡', '艺术', '城市漫步', '特色餐厅']
- errors: `[{"stage": "rule", "type": "meal_placeholder", "details": [{"date": "2026-05-08", "type": "dinner", "name": "M Stand(成都SKP店)"}]}, {"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-05-08", "type": "dinner", "name": "M Stand(成都SKP店)", "reason": "unknown_food_semantics"}]}, {"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-05-10", "lunch": "星巴克(成都环球中心II店)", "dinner": "星巴克(成都SKP店)"}]}]`

### v3_harder_eval_000008
- request: 大理 2026-05-07->2026-05-09 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "洱海公园", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-05-07", "day_index": 0, "name": "洱海公园"}, {"date": "2026-05-09", "day_index": 2, "name": "洱海公园"}]}]}, {"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-05-07", "type": "lunch", "name": "里白云南家常菜", "reason": "unknown_food_semantics"}]}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 5650, "total": 4650, "diff": 1000, "requested_budget": {"available": true, "amount": 5800, "scope": "total", "party_size": 3, "total": 5800, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "hard"}, "per_person_day": 516.67, "budget_level": "comfortable", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "hard", "amount": 5800, "target_min_ratio": 0.65, "target_max_ratio": 1.0, "target_min_total": 3800, "target_max_total": 5800, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 3, "room_count": 2, "priced_nights": 2, "expected_min_total_hotels": 3000, "reported_total_hotels": 3000, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_harder_eval_000009
- request: 苏州 2026-04-26->2026-04-29 days=4 transport=打车 hotel=亲子酒店 prefs=['亲子', '老人友好', '博物馆', '城市公园', '特色餐厅']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "留园", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-04-27", "day_index": 1, "name": "留园"}, {"date": "2026-04-29", "day_index": 3, "name": "留园"}]}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 4, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 7500, "reported_total_hotels": 3750, "diff": -3750, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 185, "expected_total_attractions": 740, "reported_total_attractions": 600, "meal_per_person_cost_sum": 984, "expected_total_meals": 3936, "reported_total_meals": 1008, "reported_total_transportation": 1200}}]`

### v3_harder_eval_000011
- request: 福州 2026-06-17->2026-06-20 days=4 transport=打车 hotel=高端酒店 prefs=['高端酒店', '艺术', '特色餐厅', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 2, "room_count": 1, "priced_nights": 3, "expected_min_total_hotels": 2250, "reported_total_hotels": 4500, "diff": 2250, "covers_nights": false}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 0, "expected_total_attractions": 0, "reported_total_attractions": 0, "meal_per_person_cost_sum": 1800, "expected_total_meals": 3600, "reported_total_meals": 2464, "reported_total_transportation": 1200}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": false, "attraction_budget_party_relation_ok": true, "meal_cost_scale_ok": true, "budget_relationship_ok": false, "expected_total_hotels": 2250, "reported_total_hotels": 4500, "expected_total_attractions": 0, "reported_total_attractions": 0, "meal_scale_eval": {"ok": true, "party_total": 2, "budget_level": "premium", "per_person_lunch_dinner_floor": 70, "per_person_breakfast_floor": 28, "meal_count": 12, "checked_count": 8, "failure_count": 0, "failures": []}}}]`

### v3_harder_eval_000014
- request: 成都 2026-06-02->2026-06-04 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 165, "expected_total_attractions": 165, "reported_total_attractions": 255, "meal_per_person_cost_sum": 757, "expected_total_meals": 757, "reported_total_meals": 545, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 165, "expected_total_attractions": 165, "reported_total_attractions": 255, "meal_per_person_cost_sum": 757, "expected_total_meals": 757, "reported_total_meals": 545, "reported_total_transportation": 200}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": false, "meal_cost_scale_ok": true, "budget_relationship_ok": false, "expected_total_hotels": 900, "reported_total_hotels": 900, "expected_total_attractions": 165, "reported_total_attractions": 255, "meal_scale_eval": {"ok": true, "party_total": 1, "budget_level": "comfortable", "per_person_lunch_dinner_floor": 50, "per_person_breakfast_floor": 20, "meal_count": 9, "checked_count": 6, "failure_count": 0, "failures": []}}}]`

### v3_harder_eval_000016
- request: 苏州 2026-06-02->2026-06-05 days=4 transport=自驾 hotel=亲子酒店 prefs=['亲子', '动物园', '海洋馆', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-06-02", "type": "dinner", "name": "松鹤楼", "reason": "unknown_food_semantics"}, {"date": "2026-06-03", "type": "dinner", "name": "松鹤楼", "reason": "unknown_food_semantics"}, {"date": "2026-06-04", "type": "dinner", "name": "松鹤楼", "reason": "unknown_food_semantics"}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 3, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 7500, "reported_total_hotels": 3750, "diff": -3750, "covers_nights": false}}, {"stage": "rule", "type": "weather_mismatch", "details": [{"date": "2026-06-05", "issue": "missing_weather_row"}]}]`

### v3_harder_eval_000010
- request: 西安 2026-04-19->2026-04-23 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "西安博物院", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-04-19", "day_index": 0, "name": "西安博物院"}, {"date": "2026-04-21", "day_index": 2, "name": "西安博物院"}]}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 4, "party_total": 5, "room_count": 3, "priced_nights": 4, "expected_min_total_hotels": 5400, "reported_total_hotels": 3600, "diff": -1800, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 5, "hotel_room_count": 3, "attraction_ticket_sum": 199, "expected_total_attractions": 995, "reported_total_attractions": 1055, "meal_per_person_cost_sum": 1150, "expected_total_meals": 5750, "reported_total_meals": 1500, "reported_total_transportation": 2000}}]`

### v3_harder_eval_000013
- request: 武汉 2026-05-05->2026-05-09 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "汉口江滩", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-05-06", "day_index": 1, "name": "汉口江滩"}, {"date": "2026-05-09", "day_index": 4, "name": "汉口江滩"}]}]}, {"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-05-05", "type": "lunch", "name": "东湖渔家乐", "reason": "unknown_food_semantics"}, {"date": "2026-05-05", "type": "dinner", "name": "东湖鱼庄", "reason": "unknown_food_semantics"}, {"date": "2026-05-06", "type": "dinner", "name": "汉口老灶台", "reason": "unknown_food_semantics"}, {"date": "2026-05-07", "type": "lunch", "name": "沙湖鱼庄", "reason": "unknown_food_semantics"}, {"date": "2026-05-07", "type": "dinner", "name": "沙湖农家菜", "reason": "unknown_food_semantics"}, {"date": "2026-05-08", "type": "lunch", "name": "月湖鱼馆", "reason": "unknown_food_semantics"}, {"date": "2026-05-08", "type": "dinner", "name": "月湖农家菜", "reason": "unknown_food_semantics"}, {"date": "2026-05-09", "type": "dinner", "name": "汉口老灶台", "reason": "unknown_food_semantics"}]}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 2900, "total": 2800, "diff": 100, "requested_budget": {"available": true, "amount": 3900, "scope": "total", "party_size": 2, "total": 3900, "source": "budget_constraint", "budget_level": "standard", "strictness": "hard"}, "per_person_day": 280.0, "budget_level": "standard", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "standard", "strictness": "hard", "amount": 3900, "target_min_ratio": 0.55, "target_max_ratio": 1.0, "target_min_total": 2100, "target_max_total": 3900, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 4, "party_total": 2, "room_count": 1, "priced_nights": 4, "expected_min_total_hotels": 1600, "reported_total_hotels": 1600, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_harder_eval_000015
- request: 南京 2026-04-03->2026-04-07 days=5 transport=公共交通 hotel=民宿 prefs=['摄影', '自然风光', '城市漫步', '本地菜']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "玄武湖景区", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-04-03", "day_index": 0, "name": "玄武湖景区"}, {"date": "2026-04-05", "day_index": 2, "name": "玄武湖景区"}]}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 125, "expected_total_attractions": 125, "reported_total_attractions": 205, "meal_per_person_cost_sum": 950, "expected_total_meals": 950, "reported_total_meals": 1035, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 125, "expected_total_attractions": 125, "reported_total_attractions": 205, "meal_per_person_cost_sum": 950, "expected_total_meals": 950, "reported_total_meals": 1035, "reported_total_transportation": 200}}]`

### v3_harder_eval_000018
- request: 天津 2026-07-02->2026-07-04 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 2, "party_total": 3, "room_count": 2, "priced_nights": 2, "expected_min_total_hotels": 4800, "reported_total_hotels": 2400, "diff": -2400, "covers_nights": false}}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 4100, "total": 3700, "diff": 400, "requested_budget": {"available": true, "amount": 4800, "scope": "total", "party_size": 3, "total": 4800, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "hard"}, "per_person_day": 411.11, "budget_level": "comfortable", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "hard", "amount": 4800, "target_min_ratio": 0.65, "target_max_ratio": 1.0, "target_min_total": 3100, "target_max_total": 4800, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 3, "room_count": 2, "priced_nights": 2, "expected_min_total_hotels": 4800, "reported_total_hotels": 2400, "diff": -2400, "covers_nights": false}, "hotel_budget_covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 160, "expected_total_attractions": 480, "reported_total_attractions": 460, "meal_per_person_cost_sum": 1581, "expected_total_meals": 4743, "reported_total_meals": 1040, "reported_total_transportation": 200}}]`

### v3_harder_eval_000012
- request: 洛阳 2025-05-03->2025-05-06 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '夜市', '老字号', '城市漫步']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 4, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 1200, "reported_total_hotels": 600, "diff": -600, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 320, "expected_total_attractions": 1280, "reported_total_attractions": 1040, "meal_per_person_cost_sum": 689, "expected_total_meals": 2756, "reported_total_meals": 1024, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 320, "expected_total_attractions": 1280, "reported_total_attractions": 1040, "meal_per_person_cost_sum": 689, "expected_total_meals": 2756, "reported_total_meals": 1024, "reported_total_transportation": 200}}]`

### v3_harder_eval_000019
- request: 丽江 2026-05-07->2026-05-10 days=4 transport=打车 hotel=亲子酒店 prefs=['亲子', '老人友好', '博物馆', '城市公园', '特色餐厅']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 400, "expected_total_attractions": 800, "reported_total_attractions": 720, "meal_per_person_cost_sum": 1080, "expected_total_meals": 2160, "reported_total_meals": 720, "reported_total_transportation": 1200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 400, "expected_total_attractions": 800, "reported_total_attractions": 720, "meal_per_person_cost_sum": 1080, "expected_total_meals": 2160, "reported_total_meals": 720, "reported_total_transportation": 1200}}]`

### v3_harder_eval_000020
- request: 杭州 2026-06-17->2026-06-21 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "杭州西湖风景名胜区-太子湾公园", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-06-19", "day_index": 2, "name": "杭州西湖风景名胜区-太子湾公园"}, {"date": "2026-06-21", "day_index": 4, "name": "杭州西湖风景名胜区-太子湾公园"}]}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "友好饭店·新友记中餐厅", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-06-17", "type": "lunch", "name": "友好饭店·新友记中餐厅"}, {"date": "2026-06-18", "type": "lunch", "name": "友好饭店·新友记中餐厅"}, {"date": "2026-06-19", "type": "lunch", "name": "友好饭店·新友记中餐厅"}, {"date": "2026-06-20", "type": "lunch", "name": "友好饭店·新友记中餐厅"}, {"date": "2026-06-21", "type": "lunch", "name": "友好饭店·新友记中餐厅"}]}, {"name_key": "友好饭店·道乐日式拉面·烧鸟·酒场", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-06-17", "type": "dinner", "name": "友好饭店·道乐日式拉面·烧鸟·酒场(湖滨店)"}, {"date": "2026-06-18", "type": "dinner", "name": "友好饭店·道乐日式拉面·烧鸟·酒场(湖滨店)"}, {"date": "2026-06-19", "type": "dinner", "name": "友好饭店·道乐日式拉面·烧鸟·酒场(湖滨店)"}, {"date": "2026-06-20", "type": "dinner", "name": "友好饭店·道乐日式拉面·烧鸟·酒场(湖滨店)"}, {"date": "2026-06-21", "type": "dinner", "name": "友好饭店·道乐日式拉面·烧鸟·酒场(湖滨店)"}]}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 4, "party_total": 5, "room_count": 3, "priced_nights": 4, "expected_min_total_hotels": 6000, "reported_total_hotels": 4000, "diff": -2000, "covers_nights": false}}]`
