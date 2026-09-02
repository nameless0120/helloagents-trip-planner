# Rule Eval Report: base_qwen25_7b_prompt_ablation_20260505_B_C

- records: 300
- generations: `training/outputs/eval/prompt_ablation_20260505/base_qwen25_7b_prompt_ablation_20260505_B_C/generations.jsonl`
- records_path: `training/data/v3/eval_harder_prompt_ablation_20260505/B_C/records.jsonl`

## Boolean Metrics

| Metric | Pass | Total | Rate |
| --- | ---: | ---: | ---: |
| accommodation_type_ok | 197 | 230 | 85.65% |
| attraction_budget_consistent | 29 | 230 | 12.61% |
| attraction_budget_party_relation_ok | 63 | 230 | 27.39% |
| attraction_count_ok | 230 | 230 | 100.00% |
| attraction_diversity_ok | 203 | 230 | 88.26% |
| attraction_grounding_ok | 226 | 230 | 98.26% |
| attraction_repeat_limit_ok | 203 | 230 | 88.26% |
| budget_arithmetic_consistent | 108 | 230 | 46.96% |
| budget_consistent | 108 | 230 | 46.96% |
| budget_level_aligned | 89 | 230 | 38.70% |
| budget_preference_aligned | 89 | 230 | 38.70% |
| budget_relationship_ok | 22 | 230 | 9.57% |
| budget_user_constraint_ok | 184 | 230 | 80.00% |
| budget_within_user_budget | 217 | 230 | 94.35% |
| city_ok | 230 | 230 | 100.00% |
| date_range_ok | 230 | 230 | 100.00% |
| day_dates_ok | 230 | 230 | 100.00% |
| day_index_ok | 230 | 230 | 100.00% |
| days_len_ok | 230 | 230 | 100.00% |
| dpo_soft_pass | 0 | 230 | 0.00% |
| hard_pass | 0 | 230 | 0.00% |
| hotel_budget_covers_nights | 97 | 230 | 42.17% |
| hotel_budget_relation_ok | 105 | 230 | 45.65% |
| hotel_distance_placeholder_ok | 230 | 230 | 100.00% |
| hotel_grounding_ok | 228 | 230 | 99.13% |
| invalid_hotel_name_ok | 230 | 230 | 100.00% |
| json_extract_ok | 300 | 300 | 100.00% |
| legacy_hard_pass | 14 | 230 | 6.09% |
| location_object_ok | 230 | 230 | 100.00% |
| meal_budget_consistent | 0 | 230 | 0.00% |
| meal_complete | 230 | 230 | 100.00% |
| meal_cost_scale_ok | 157 | 230 | 68.26% |
| meal_diversity_ok | 138 | 230 | 60.00% |
| meal_grounding_ok | 137 | 230 | 59.57% |
| meal_lunch_dinner_same_day_ok | 194 | 230 | 84.35% |
| meal_repeat_limit_ok | 156 | 230 | 67.83% |
| meal_specific_ok | 221 | 230 | 96.09% |
| meal_valid_semantics_ok | 149 | 230 | 64.78% |
| middle_hotel_ok | 230 | 230 | 100.00% |
| schema_ok | 230 | 300 | 76.67% |
| sft_budget_semantic_hard_pass | 10 | 230 | 4.35% |
| sft_hard_pass | 0 | 230 | 0.00% |
| transportation_budget_nonnegative | 230 | 230 | 100.00% |
| weather_dates_ok | 230 | 230 | 100.00% |
| weather_match | 229 | 230 | 99.57% |

## Numeric Metrics

```json
{
  "attraction_diversity_unique_rate": {
    "avg": 0.9771,
    "p50": 1.0,
    "p90": 1.0
  },
  "attraction_grounding_rate": {
    "avg": 0.9971,
    "p50": 1.0,
    "p90": 1.0
  },
  "hotel_grounding_rate": {
    "avg": 0.9978,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_diversity_unique_rate": {
    "avg": 0.5274,
    "p50": 0.5,
    "p90": 1.0
  },
  "meal_food_pois_grounding_rate": {
    "avg": 0.8738,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_grounding_rate": {
    "avg": 0.8738,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_semantic_valid_rate": {
    "avg": 0.9235,
    "p50": 1.0,
    "p90": 1.0
  }
}
```

## Failure Types

```json
{
  "meal_budget_inconsistent": 224,
  "budget_relationship_mismatch": 208,
  "attraction_budget_inconsistent": 201,
  "budget_preference_mismatch": 141,
  "hotel_budget_underestimated": 133,
  "budget_arithmetic_inconsistent": 122,
  "meal_invalid_name": 81,
  "meal_repeat_too_many": 74,
  "meal_cost_scale_too_low": 73,
  "schema": 70,
  "budget_hard_constraint_exceeded": 46,
  "meal_same_day_lunch_dinner_repeat": 36,
  "accommodation_type_mismatch": 33,
  "attraction_repeat_too_many": 27,
  "meal_grounding_miss": 12,
  "meal_placeholder": 9,
  "weather_mismatch": 1
}
```

## Failure Examples

### v3_harder_eval_000014
- request: 成都 2026-06-02->2026-06-04 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 2575, "total": 2585, "diff": -10, "requested_budget": {"available": true, "amount": 2100, "scope": "total", "party_size": 1, "total": 2100, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "hard"}, "per_person_day": 861.67, "budget_level": "comfortable", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "hard", "amount": 2100, "target_min_ratio": 0.65, "target_max_ratio": 1.0, "target_min_total": 1400, "target_max_total": 2100, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": false, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 1, "room_count": 1, "priced_nights": 3, "expected_min_total_hotels": 1350, "reported_total_hotels": 1350, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 115, "expected_total_attractions": 115, "reported_total_attractions": 235, "meal_per_person_cost_sum": 700, "expected_total_meals": 700, "reported_total_meals": 390, "reported_total_transportation": 600}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 115, "expected_total_attractions": 115, "reported_total_attractions": 235, "meal_per_person_cost_sum": 700, "expected_total_meals": 700, "reported_total_meals": 390, "reported_total_transportation": 600}}]`

### v3_harder_eval_000012
- request: 洛阳 2025-05-03->2025-05-06 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '夜市', '老字号', '城市漫步']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 4, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 1200, "reported_total_hotels": 600, "diff": -600, "covers_nights": false}}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 1240, "total": 1220, "diff": 20, "requested_budget": {"available": true, "amount": 3400, "scope": "total", "party_size": 4, "total": 3400, "source": "budget_constraint", "budget_level": "limited", "strictness": "hard"}, "per_person_day": 76.25, "budget_level": "limited", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "limited", "strictness": "hard", "amount": 3400, "target_min_ratio": 0.72, "target_max_ratio": 1.0, "target_min_total": 2400, "target_max_total": 3400, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 4, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 1200, "reported_total_hotels": 600, "diff": -600, "covers_nights": false}, "hotel_budget_covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 240, "expected_total_attractions": 960, "reported_total_attractions": 120, "meal_per_person_cost_sum": 1804, "expected_total_meals": 7216, "reported_total_meals": 320, "reported_total_transportation": 200}}]`

### v3_harder_eval_000036
- request: 长沙 2026-06-02->2026-06-05 days=4 transport=自驾 hotel=亲子酒店 prefs=['亲子', '动物园', '海洋馆', '城市公园', '本地美食']
- errors: `[{"stage": "schema", "message": "1 validation error for TripPlan\ndays.3.accommodation\n  Input should be a valid string [type=string_type, input_value=None, input_type=NoneType]\n    For further information visit https://errors.pydantic.dev/2.13/v/string_type"}]`

### v3_harder_eval_000029
- request: 长沙 2026-03-04->2026-03-07 days=4 transport=打车 hotel=亲子酒店 prefs=['亲子', '老人友好', '博物馆', '城市公园', '特色餐厅']
- errors: `[{"stage": "schema", "message": "1 validation error for TripPlan\ndays.3.accommodation\n  Input should be a valid string [type=string_type, input_value=None, input_type=NoneType]\n    For further information visit https://errors.pydantic.dev/2.13/v/string_type"}]`

### v3_harder_eval_000008
- request: 大理 2026-05-07->2026-05-09 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物']
- errors: `[{"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-05-09", "type": "dinner", "name": "无", "reason": "empty_or_none"}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 2, "party_total": 3, "room_count": 2, "priced_nights": 2, "expected_min_total_hotels": 3000, "reported_total_hotels": 2250, "diff": -750, "covers_nights": false}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 75, "expected_total_attractions": 225, "reported_total_attractions": 225, "meal_per_person_cost_sum": 1275, "expected_total_meals": 3825, "reported_total_meals": 1350, "reported_total_transportation": 600}}]`

### v3_harder_eval_000011
- request: 福州 2026-06-17->2026-06-20 days=4 transport=打车 hotel=高端酒店 prefs=['高端酒店', '艺术', '特色餐厅', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 0, "expected_total_attractions": 0, "reported_total_attractions": 0, "meal_per_person_cost_sum": 1790, "expected_total_meals": 3580, "reported_total_meals": 1212, "reported_total_transportation": 1200}}, {"stage": "rule", "type": "budget_preference_mismatch", "details": {"part_sum": 5412, "total": 5412, "diff": 0, "requested_budget": {"available": true, "amount": 8800, "scope": "total", "party_size": 2, "total": 8800, "source": "budget_constraint", "budget_level": "premium", "strictness": "soft"}, "per_person_day": 676.5, "budget_level": "premium", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "premium", "strictness": "soft", "amount": 8800, "target_min_ratio": 0.7, "target_max_ratio": 1.12, "target_min_total": 6200, "target_max_total": 9900, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": true, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 2, "room_count": 1, "priced_nights": 4, "expected_min_total_hotels": 3000, "reported_total_hotels": 3000, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_harder_eval_000018
- request: 天津 2026-07-02->2026-07-04 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-07-03", "lunch": "苏焰·地标天津菜(多伦道店)", "dinner": "苏焰·地标天津菜(金海道店)"}, {"date": "2026-07-04", "lunch": "苏焰·地标天津菜(多伦道店)", "dinner": "苏焰·地标天津菜(金海道店)"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "南楼煎饼", "count": 3, "max_allowed": 2, "occurrences": [{"date": "2026-07-02", "type": "breakfast", "name": "南楼煎饼(南楼总店)"}, {"date": "2026-07-03", "type": "breakfast", "name": "南楼煎饼(南楼总店)"}, {"date": "2026-07-04", "type": "breakfast", "name": "南楼煎饼(南楼总店)"}]}, {"name_key": "苏焰·地标天津菜", "count": 5, "max_allowed": 2, "occurrences": [{"date": "2026-07-02", "type": "dinner", "name": "苏焰·地标天津菜(金海道店)"}, {"date": "2026-07-03", "type": "lunch", "name": "苏焰·地标天津菜(多伦道店)"}, {"date": "2026-07-03", "type": "dinner", "name": "苏焰·地标天津菜(金海道店)"}, {"date": "2026-07-04", "type": "lunch", "name": "苏焰·地标天津菜(多伦道店)"}, {"date": "2026-07-04", "type": "dinner", "name": "苏焰·地标天津菜(金海道店)"}]}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 2, "party_total": 3, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 7200, "reported_total_hotels": 3600, "diff": -3600, "covers_nights": false}}]`

### v3_harder_eval_000032
- request: 丽江 2026-05-06->2026-05-09 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '夜市', '老字号', '城市漫步']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "丽江古城", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-05-06", "day_index": 0, "name": "丽江古城"}, {"date": "2026-05-09", "day_index": 3, "name": "丽江古城"}]}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 4, "room_count": 2, "priced_nights": 4, "expected_min_total_hotels": 1600, "reported_total_hotels": 600, "diff": -1000, "covers_nights": false}}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 2144, "total": 1944, "diff": 200, "requested_budget": {"available": true, "amount": 2400, "scope": "total", "party_size": 4, "total": 2400, "source": "budget_constraint", "budget_level": "limited", "strictness": "hard"}, "per_person_day": 121.5, "budget_level": "limited", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "limited", "strictness": "hard", "amount": 2400, "target_min_ratio": 0.72, "target_max_ratio": 1.0, "target_min_total": 1700, "target_max_total": 2400, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 4, "room_count": 2, "priced_nights": 4, "expected_min_total_hotels": 1600, "reported_total_hotels": 600, "diff": -1000, "covers_nights": false}, "hotel_budget_covers_nights": false}}]`

### v3_harder_eval_000031
- request: 成都 2026-05-07->2026-05-10 days=4 transport=打车 hotel=高端酒店 prefs=['高端酒店', '艺术', '特色餐厅', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 195, "expected_total_attractions": 390, "reported_total_attractions": 240, "meal_per_person_cost_sum": 1958, "expected_total_meals": 3916, "reported_total_meals": 1512, "reported_total_transportation": 800}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 195, "expected_total_attractions": 390, "reported_total_attractions": 240, "meal_per_person_cost_sum": 1958, "expected_total_meals": 3916, "reported_total_meals": 1512, "reported_total_transportation": 800}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": false, "meal_cost_scale_ok": true, "budget_relationship_ok": false, "expected_total_hotels": 2400, "reported_total_hotels": 2400, "expected_total_attractions": 390, "reported_total_attractions": 240, "meal_scale_eval": {"ok": true, "party_total": 2, "budget_level": "premium", "per_person_lunch_dinner_floor": 70, "per_person_breakfast_floor": 28, "meal_count": 12, "checked_count": 8, "failure_count": 0, "failures": []}}}]`

### v3_harder_eval_000004
- request: 张家界 2026-05-07->2026-05-09 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 2220, "total": 2040, "diff": 180, "requested_budget": {"available": true, "amount": 1700, "scope": "total", "party_size": 1, "total": 1700, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "hard"}, "per_person_day": 680.0, "budget_level": "comfortable", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "hard", "amount": 1700, "target_min_ratio": 0.65, "target_max_ratio": 1.0, "target_min_total": 1100, "target_max_total": 1700, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": false, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 1, "room_count": 1, "priced_nights": 3, "expected_min_total_hotels": 1200, "reported_total_hotels": 1200, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 320, "expected_total_attractions": 320, "reported_total_attractions": 240, "meal_per_person_cost_sum": 90, "expected_total_meals": 90, "reported_total_meals": 180, "reported_total_transportation": 600}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 320, "expected_total_attractions": 320, "reported_total_attractions": 240, "meal_per_person_cost_sum": 90, "expected_total_meals": 90, "reported_total_meals": 180, "reported_total_transportation": 600}}]`

### v3_harder_eval_000038
- request: 厦门 2026-05-06->2026-05-08 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 2, "party_total": 3, "room_count": 2, "priced_nights": 2, "expected_min_total_hotels": 3200, "reported_total_hotels": 2400, "diff": -800, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 100, "expected_total_attractions": 300, "reported_total_attractions": 240, "meal_per_person_cost_sum": 1569, "expected_total_meals": 4707, "reported_total_meals": 1440, "reported_total_transportation": 600}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 100, "expected_total_attractions": 300, "reported_total_attractions": 240, "meal_per_person_cost_sum": 1569, "expected_total_meals": 4707, "reported_total_meals": 1440, "reported_total_transportation": 600}}]`

### v3_harder_eval_000028
- request: 深圳 2026-03-04->2026-03-06 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物']
- errors: `[{"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-03-06", "type": "dinner", "name": "酒店早餐", "reason": "hotel_or_lodging_name"}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 2, "party_total": 3, "room_count": 2, "priced_nights": 2, "expected_min_total_hotels": 3200, "reported_total_hotels": 1600, "diff": -1600, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 240, "expected_total_attractions": 720, "reported_total_attractions": 460, "meal_per_person_cost_sum": 1736, "expected_total_meals": 5208, "reported_total_meals": 780, "reported_total_transportation": 600}}]`

### v3_harder_eval_000024
- request: 济南 2026-05-06->2026-05-08 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆']
- errors: `[{"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-05-08", "type": "dinner", "name": "酒店早餐", "reason": "hotel_or_lodging_name"}]}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 2235, "total": 1700, "diff": 535, "requested_budget": {"available": true, "amount": 1700, "scope": "total", "party_size": 1, "total": 1700, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "hard"}, "per_person_day": 566.67, "budget_level": "comfortable", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "hard", "amount": 1700, "target_min_ratio": 0.65, "target_max_ratio": 1.0, "target_min_total": 1100, "target_max_total": 1700, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 1, "room_count": 1, "priced_nights": 3, "expected_min_total_hotels": 1200, "reported_total_hotels": 1200, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 240, "expected_total_attractions": 240, "reported_total_attractions": 240, "meal_per_person_cost_sum": 493, "expected_total_meals": 493, "reported_total_meals": 195, "reported_total_transportation": 600}}]`

### v3_harder_eval_000023
- request: 大理 2026-08-31->2026-09-04 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_grounding_miss", "details": [{"date": "2026-08-31", "type": "lunch", "name": "大理古城小吃街"}, {"date": "2026-08-31", "type": "dinner", "name": "大理古城特色餐厅"}, {"date": "2026-09-01", "type": "lunch", "name": "大理古城小吃街"}, {"date": "2026-09-01", "type": "dinner", "name": "大理古城特色餐厅"}, {"date": "2026-09-02", "type": "lunch", "name": "大理古城小吃街"}, {"date": "2026-09-02", "type": "dinner", "name": "大理古城特色餐厅"}, {"date": "2026-09-03", "type": "lunch", "name": "大理古城小吃街"}, {"date": "2026-09-03", "type": "dinner", "name": "大理古城特色餐厅"}, {"date": "2026-09-04", "type": "lunch", "name": "双廊古镇小吃街"}, {"date": "2026-09-04", "type": "dinner", "name": "双廊古镇特色餐厅"}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 4, "party_total": 4, "room_count": 2, "priced_nights": 4, "expected_min_total_hotels": 3200, "reported_total_hotels": 1600, "diff": -1600, "covers_nights": false}}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 3145, "total": 2845, "diff": 300, "requested_budget": {"available": true, "amount": 5500, "scope": "total", "party_size": 4, "total": 5500, "source": "budget_constraint", "budget_level": "standard", "strictness": "hard"}, "per_person_day": 142.25, "budget_level": "standard", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "standard", "strictness": "hard", "amount": 5500, "target_min_ratio": 0.55, "target_max_ratio": 1.0, "target_min_total": 3000, "target_max_total": 5500, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 4, "party_total": 4, "room_count": 2, "priced_nights": 4, "expected_min_total_hotels": 3200, "reported_total_hotels": 1600, "diff": -1600, "covers_nights": false}, "hotel_budget_covers_nights": false}}]`

### v3_harder_eval_000034
- request: 武汉 2026-06-02->2026-06-04 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 2220, "total": 2120, "diff": 100, "requested_budget": {"available": true, "amount": 1800, "scope": "total", "party_size": 1, "total": 1800, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "hard"}, "per_person_day": 706.67, "budget_level": "comfortable", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "hard", "amount": 1800, "target_min_ratio": 0.65, "target_max_ratio": 1.0, "target_min_total": 1200, "target_max_total": 1800, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": false, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 1, "room_count": 1, "priced_nights": 3, "expected_min_total_hotels": 1200, "reported_total_hotels": 1200, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 70, "expected_total_attractions": 70, "reported_total_attractions": 210, "meal_per_person_cost_sum": 496, "expected_total_meals": 496, "reported_total_meals": 210, "reported_total_transportation": 600}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 70, "expected_total_attractions": 70, "reported_total_attractions": 210, "meal_per_person_cost_sum": 496, "expected_total_meals": 496, "reported_total_meals": 210, "reported_total_transportation": 600}}]`

### v3_harder_eval_000019
- request: 丽江 2026-05-07->2026-05-10 days=4 transport=打车 hotel=亲子酒店 prefs=['亲子', '老人友好', '博物馆', '城市公园', '特色餐厅']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "丽江古城", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-05-07", "day_index": 0, "name": "丽江古城"}, {"date": "2026-05-10", "day_index": 3, "name": "丽江古城"}]}, {"name_key": "束河古镇", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-05-07", "day_index": 0, "name": "束河古镇"}, {"date": "2026-05-09", "day_index": 2, "name": "束河古镇"}]}]}, {"stage": "rule", "type": "accommodation_type_mismatch", "details": [{"date": "2026-05-10", "day_index": 3, "expected": "亲子酒店", "got": "无"}]}, {"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-05-07", "type": "breakfast", "name": "丽江古城内的特色早餐", "reason": "unknown_food_semantics"}, {"date": "2026-05-08", "type": "breakfast", "name": "丽江古城内的特色早餐", "reason": "unknown_food_semantics"}, {"date": "2026-05-09", "type": "breakfast", "name": "丽江古城内的特色早餐", "reason": "unknown_food_semantics"}, {"date": "2026-05-10", "type": "breakfast", "name": "丽江古城内的特色早餐", "reason": "unknown_food_semantics"}]}]`

### v3_harder_eval_000026
- request: 扬州 2026-05-07->2026-05-10 days=4 transport=自驾 hotel=亲子酒店 prefs=['亲子', '动物园', '海洋馆', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "accommodation_type_mismatch", "details": [{"date": "2026-05-10", "day_index": 3, "expected": "亲子酒店", "got": "无"}]}, {"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-05-07", "type": "lunch", "name": "扬州炒饭", "reason": "unknown_food_semantics"}, {"date": "2026-05-07", "type": "dinner", "name": "扬州炒面", "reason": "unknown_food_semantics"}, {"date": "2026-05-08", "type": "lunch", "name": "扬州炒饭", "reason": "unknown_food_semantics"}, {"date": "2026-05-08", "type": "dinner", "name": "扬州炒面", "reason": "unknown_food_semantics"}, {"date": "2026-05-09", "type": "lunch", "name": "扬州炒饭", "reason": "unknown_food_semantics"}, {"date": "2026-05-09", "type": "dinner", "name": "扬州炒面", "reason": "unknown_food_semantics"}, {"date": "2026-05-10", "type": "lunch", "name": "扬州炒饭", "reason": "unknown_food_semantics"}, {"date": "2026-05-10", "type": "dinner", "name": "扬州炒面", "reason": "unknown_food_semantics"}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 3, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 3000, "reported_total_hotels": 1500, "diff": -1500, "covers_nights": false}}]`

### v3_harder_eval_000000
- request: 昆明 2026-04-03->2026-04-07 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "schema", "message": "1 validation error for TripPlan\ndays.4.accommodation\n  Input should be a valid string [type=string_type, input_value=None, input_type=NoneType]\n    For further information visit https://errors.pydantic.dev/2.13/v/string_type"}]`

### v3_harder_eval_000006
- request: 南京 2026-07-02->2026-07-05 days=4 transport=自驾 hotel=亲子酒店 prefs=['亲子', '动物园', '海洋馆', '城市公园', '本地美食']
- errors: `[{"stage": "schema", "message": "1 validation error for TripPlan\ndays.3.accommodation\n  Input should be a valid string [type=string_type, input_value=None, input_type=NoneType]\n    For further information visit https://errors.pydantic.dev/2.13/v/string_type"}]`

### v3_harder_eval_000007
- request: 成都 2026-05-07->2026-05-11 days=5 transport=公共交通 hotel=民宿 prefs=['小众展馆', '咖啡', '艺术', '城市漫步', '特色餐厅']
- errors: `[{"stage": "schema", "message": "1 validation error for TripPlan\ndays.4.accommodation\n  Input should be a valid string [type=string_type, input_value=None, input_type=NoneType]\n    For further information visit https://errors.pydantic.dev/2.13/v/string_type"}]`
