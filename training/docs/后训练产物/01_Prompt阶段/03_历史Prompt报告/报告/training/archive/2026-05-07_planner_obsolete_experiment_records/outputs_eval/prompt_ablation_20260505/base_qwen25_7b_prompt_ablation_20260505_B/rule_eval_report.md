# Rule Eval Report: base_qwen25_7b_prompt_ablation_20260505_B

- records: 300
- generations: `training/outputs/eval/prompt_ablation_20260505/base_qwen25_7b_prompt_ablation_20260505_B/generations.jsonl`
- records_path: `training/data/v3/eval_harder_prompt_ablation_20260505/B/records.jsonl`

## Boolean Metrics

| Metric | Pass | Total | Rate |
| --- | ---: | ---: | ---: |
| accommodation_type_ok | 248 | 288 | 86.11% |
| attraction_budget_consistent | 33 | 288 | 11.46% |
| attraction_budget_party_relation_ok | 70 | 288 | 24.31% |
| attraction_count_ok | 286 | 288 | 99.31% |
| attraction_diversity_ok | 244 | 288 | 84.72% |
| attraction_grounding_ok | 283 | 288 | 98.26% |
| attraction_repeat_limit_ok | 244 | 288 | 84.72% |
| budget_arithmetic_consistent | 134 | 288 | 46.53% |
| budget_consistent | 134 | 288 | 46.53% |
| budget_level_aligned | 112 | 288 | 38.89% |
| budget_preference_aligned | 112 | 288 | 38.89% |
| budget_relationship_ok | 18 | 288 | 6.25% |
| budget_user_constraint_ok | 246 | 288 | 85.42% |
| budget_within_user_budget | 276 | 288 | 95.83% |
| city_ok | 288 | 288 | 100.00% |
| date_range_ok | 288 | 288 | 100.00% |
| day_dates_ok | 288 | 288 | 100.00% |
| day_index_ok | 288 | 288 | 100.00% |
| days_len_ok | 288 | 288 | 100.00% |
| dpo_soft_pass | 0 | 288 | 0.00% |
| hard_pass | 0 | 288 | 0.00% |
| hotel_budget_covers_nights | 111 | 288 | 38.54% |
| hotel_budget_relation_ok | 120 | 288 | 41.67% |
| hotel_distance_placeholder_ok | 288 | 288 | 100.00% |
| hotel_grounding_ok | 287 | 288 | 99.65% |
| invalid_hotel_name_ok | 288 | 288 | 100.00% |
| json_extract_ok | 298 | 300 | 99.33% |
| legacy_hard_pass | 20 | 288 | 6.94% |
| location_object_ok | 288 | 288 | 100.00% |
| meal_budget_consistent | 0 | 288 | 0.00% |
| meal_complete | 288 | 288 | 100.00% |
| meal_cost_scale_ok | 193 | 288 | 67.01% |
| meal_diversity_ok | 209 | 288 | 72.57% |
| meal_grounding_ok | 175 | 288 | 60.76% |
| meal_lunch_dinner_same_day_ok | 238 | 288 | 82.64% |
| meal_repeat_limit_ok | 232 | 288 | 80.56% |
| meal_specific_ok | 276 | 288 | 95.83% |
| meal_valid_semantics_ok | 190 | 288 | 65.97% |
| middle_hotel_ok | 288 | 288 | 100.00% |
| schema_ok | 288 | 300 | 96.00% |
| sft_budget_semantic_hard_pass | 10 | 288 | 3.47% |
| sft_hard_pass | 0 | 288 | 0.00% |
| transportation_budget_nonnegative | 288 | 288 | 100.00% |
| weather_dates_ok | 288 | 288 | 100.00% |
| weather_match | 287 | 288 | 99.65% |

## Numeric Metrics

```json
{
  "attraction_diversity_unique_rate": {
    "avg": 0.9718,
    "p50": 1.0,
    "p90": 1.0
  },
  "attraction_grounding_rate": {
    "avg": 0.997,
    "p50": 1.0,
    "p90": 1.0
  },
  "hotel_grounding_rate": {
    "avg": 0.9991,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_diversity_unique_rate": {
    "avg": 0.5327,
    "p50": 0.5,
    "p90": 1.0
  },
  "meal_food_pois_grounding_rate": {
    "avg": 0.8516,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_grounding_rate": {
    "avg": 0.8516,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_semantic_valid_rate": {
    "avg": 0.9066,
    "p50": 1.0,
    "p90": 1.0
  }
}
```

## Failure Types

```json
{
  "meal_budget_inconsistent": 286,
  "budget_relationship_mismatch": 270,
  "attraction_budget_inconsistent": 255,
  "hotel_budget_underestimated": 177,
  "budget_preference_mismatch": 176,
  "budget_arithmetic_inconsistent": 154,
  "meal_invalid_name": 98,
  "meal_cost_scale_too_low": 95,
  "meal_repeat_too_many": 56,
  "meal_same_day_lunch_dinner_repeat": 50,
  "attraction_repeat_too_many": 44,
  "budget_hard_constraint_exceeded": 42,
  "accommodation_type_mismatch": 40,
  "meal_grounding_miss": 15,
  "meal_placeholder": 12,
  "schema": 10,
  "json_extract": 2,
  "weather_mismatch": 1
}
```

## Failure Examples

### v3_harder_eval_000028
- request: 深圳 2026-03-04->2026-03-06 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "胡桃里音乐酒馆", "count": 3, "max_allowed": 2, "occurrences": [{"date": "2026-03-04", "type": "breakfast", "name": "胡桃里音乐酒馆(领展中心城店)"}, {"date": "2026-03-05", "type": "breakfast", "name": "胡桃里音乐酒馆(领展中心城店)"}, {"date": "2026-03-06", "type": "breakfast", "name": "胡桃里音乐酒馆(领展中心城店)"}]}, {"name_key": "blend咖啡部落", "count": 3, "max_allowed": 2, "occurrences": [{"date": "2026-03-04", "type": "dinner", "name": "blend咖啡部落(卓悦中心店)"}, {"date": "2026-03-05", "type": "dinner", "name": "blend咖啡部落(卓悦中心店)"}, {"date": "2026-03-06", "type": "dinner", "name": "blend咖啡部落(卓悦中心店)"}]}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 2, "party_total": 3, "room_count": 2, "priced_nights": 2, "expected_min_total_hotels": 3200, "reported_total_hotels": 1600, "diff": -1600, "covers_nights": false}}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 2959, "total": 3949, "diff": -990, "requested_budget": {"available": true, "amount": 4400, "scope": "total", "party_size": 3, "total": 4400, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "hard"}, "per_person_day": 438.78, "budget_level": "comfortable", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "hard", "amount": 4400, "target_min_ratio": 0.65, "target_max_ratio": 1.0, "target_min_total": 2900, "target_max_total": 4400, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 3, "room_count": 2, "priced_nights": 2, "expected_min_total_hotels": 3200, "reported_total_hotels": 1600, "diff": -1600, "covers_nights": false}, "hotel_budget_covers_nights": false}}]`

### v3_harder_eval_000004
- request: 张家界 2026-05-07->2026-05-09 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 2220, "total": 1700, "diff": 520, "requested_budget": {"available": true, "amount": 1700, "scope": "total", "party_size": 1, "total": 1700, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "hard"}, "per_person_day": 566.67, "budget_level": "comfortable", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "hard", "amount": 1700, "target_min_ratio": 0.65, "target_max_ratio": 1.0, "target_min_total": 1100, "target_max_total": 1700, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 1, "room_count": 1, "priced_nights": 3, "expected_min_total_hotels": 1200, "reported_total_hotels": 1200, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 320, "expected_total_attractions": 320, "reported_total_attractions": 240, "meal_per_person_cost_sum": 418, "expected_total_meals": 418, "reported_total_meals": 180, "reported_total_transportation": 600}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 320, "expected_total_attractions": 320, "reported_total_attractions": 240, "meal_per_person_cost_sum": 418, "expected_total_meals": 418, "reported_total_meals": 180, "reported_total_transportation": 600}}]`

### v3_harder_eval_000019
- request: 丽江 2026-05-07->2026-05-10 days=4 transport=打车 hotel=亲子酒店 prefs=['亲子', '老人友好', '博物馆', '城市公园', '特色餐厅']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "丽江古城", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-05-07", "day_index": 0, "name": "丽江古城"}, {"date": "2026-05-10", "day_index": 3, "name": "丽江古城"}]}]}, {"stage": "rule", "type": "meal_grounding_miss", "details": [{"date": "2026-05-07", "type": "lunch", "name": "丽江古城小吃街"}, {"date": "2026-05-07", "type": "dinner", "name": "丽江古城小吃街"}, {"date": "2026-05-08", "type": "lunch", "name": "丽江古城小吃街"}, {"date": "2026-05-08", "type": "dinner", "name": "丽江古城小吃街"}, {"date": "2026-05-09", "type": "lunch", "name": "丽江古城小吃街"}, {"date": "2026-05-09", "type": "dinner", "name": "丽江古城小吃街"}, {"date": "2026-05-10", "type": "lunch", "name": "丽江古城小吃街"}, {"date": "2026-05-10", "type": "dinner", "name": "丽江古城小吃街"}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 2, "room_count": 1, "priced_nights": 4, "expected_min_total_hotels": 2000, "reported_total_hotels": 1500, "diff": -500, "covers_nights": false}}]`

### v3_harder_eval_000008
- request: 大理 2026-05-07->2026-05-09 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物']
- errors: `[{"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-05-09", "type": "dinner", "name": "无", "reason": "empty_or_none"}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 2, "party_total": 3, "room_count": 2, "priced_nights": 2, "expected_min_total_hotels": 3000, "reported_total_hotels": 2250, "diff": -750, "covers_nights": false}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 75, "expected_total_attractions": 225, "reported_total_attractions": 225, "meal_per_person_cost_sum": 1275, "expected_total_meals": 3825, "reported_total_meals": 1350, "reported_total_transportation": 600}}]`

### v3_harder_eval_000038
- request: 厦门 2026-05-06->2026-05-08 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 2, "party_total": 3, "room_count": 2, "priced_nights": 2, "expected_min_total_hotels": 3200, "reported_total_hotels": 2400, "diff": -800, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 100, "expected_total_attractions": 300, "reported_total_attractions": 240, "meal_per_person_cost_sum": 1569, "expected_total_meals": 4707, "reported_total_meals": 1200, "reported_total_transportation": 600}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 100, "expected_total_attractions": 300, "reported_total_attractions": 240, "meal_per_person_cost_sum": 1569, "expected_total_meals": 4707, "reported_total_meals": 1200, "reported_total_transportation": 600}}]`

### v3_harder_eval_000018
- request: 天津 2026-07-02->2026-07-04 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 2, "party_total": 3, "room_count": 2, "priced_nights": 2, "expected_min_total_hotels": 4800, "reported_total_hotels": 3600, "diff": -1200, "covers_nights": false}}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 4950, "total": 4800, "diff": 150, "requested_budget": {"available": true, "amount": 4800, "scope": "total", "party_size": 3, "total": 4800, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "hard"}, "per_person_day": 533.33, "budget_level": "comfortable", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "hard", "amount": 4800, "target_min_ratio": 0.65, "target_max_ratio": 1.0, "target_min_total": 3100, "target_max_total": 4800, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 3, "room_count": 2, "priced_nights": 2, "expected_min_total_hotels": 4800, "reported_total_hotels": 3600, "diff": -1200, "covers_nights": false}, "hotel_budget_covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 130, "expected_total_attractions": 390, "reported_total_attractions": 210, "meal_per_person_cost_sum": 994, "expected_total_meals": 2982, "reported_total_meals": 540, "reported_total_transportation": 600}}]`

### v3_harder_eval_000016
- request: 苏州 2026-06-02->2026-06-05 days=4 transport=自驾 hotel=亲子酒店 prefs=['亲子', '动物园', '海洋馆', '城市公园', '本地美食']
- errors: `[{"stage": "schema", "message": "1 validation error for TripPlan\ndays.3.accommodation\n  Input should be a valid string [type=string_type, input_value=None, input_type=NoneType]\n    For further information visit https://errors.pydantic.dev/2.13/v/string_type"}]`

### v3_harder_eval_000011
- request: 福州 2026-06-17->2026-06-20 days=4 transport=打车 hotel=高端酒店 prefs=['高端酒店', '艺术', '特色餐厅', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 0, "expected_total_attractions": 0, "reported_total_attractions": 0, "meal_per_person_cost_sum": 1710, "expected_total_meals": 3420, "reported_total_meals": 1080, "reported_total_transportation": 1000}}, {"stage": "rule", "type": "budget_preference_mismatch", "details": {"part_sum": 4330, "total": 4330, "diff": 0, "requested_budget": {"available": true, "amount": 8800, "scope": "total", "party_size": 2, "total": 8800, "source": "budget_constraint", "budget_level": "premium", "strictness": "soft"}, "per_person_day": 541.25, "budget_level": "premium", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "premium", "strictness": "soft", "amount": 8800, "target_min_ratio": 0.7, "target_max_ratio": 1.12, "target_min_total": 6200, "target_max_total": 9900, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": true, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 2, "room_count": 1, "priced_nights": 3, "expected_min_total_hotels": 2250, "reported_total_hotels": 2250, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_harder_eval_000034
- request: 武汉 2026-06-02->2026-06-04 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "吉庆78号私房菜", "count": 3, "max_allowed": 2, "occurrences": [{"date": "2026-06-02", "type": "dinner", "name": "吉庆78号私房菜(江汉路店)"}, {"date": "2026-06-03", "type": "lunch", "name": "吉庆78号私房菜(江汉路店)"}, {"date": "2026-06-04", "type": "lunch", "name": "吉庆78号私房菜(江汉路店)"}]}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 70, "expected_total_attractions": 70, "reported_total_attractions": 210, "meal_per_person_cost_sum": 572, "expected_total_meals": 572, "reported_total_meals": 234, "reported_total_transportation": 600}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 70, "expected_total_attractions": 70, "reported_total_attractions": 210, "meal_per_person_cost_sum": 572, "expected_total_meals": 572, "reported_total_meals": 234, "reported_total_transportation": 600}}]`

### v3_harder_eval_000024
- request: 济南 2026-05-06->2026-05-08 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆']
- errors: `[{"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-05-08", "type": "dinner", "name": "酒店晚餐", "reason": "generic_lodging_meal"}]}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 2198, "total": 1798, "diff": 400, "requested_budget": {"available": true, "amount": 1700, "scope": "total", "party_size": 1, "total": 1700, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "hard"}, "per_person_day": 599.33, "budget_level": "comfortable", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "hard", "amount": 1700, "target_min_ratio": 0.65, "target_max_ratio": 1.0, "target_min_total": 1100, "target_max_total": 1700, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": false, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 1, "room_count": 1, "priced_nights": 3, "expected_min_total_hotels": 1200, "reported_total_hotels": 1200, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 300, "expected_total_attractions": 300, "reported_total_attractions": 480, "meal_per_person_cost_sum": 513, "expected_total_meals": 513, "reported_total_meals": 318, "reported_total_transportation": 200}}]`

### v3_harder_eval_000014
- request: 成都 2026-06-02->2026-06-04 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-06-04", "lunch": "观锦餐厅(天府新谷店)", "dinner": "观锦餐厅(天廊店)"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "观锦餐厅", "count": 3, "max_allowed": 2, "occurrences": [{"date": "2026-06-02", "type": "lunch", "name": "观锦餐厅(天廊店)"}, {"date": "2026-06-04", "type": "lunch", "name": "观锦餐厅(天府新谷店)"}, {"date": "2026-06-04", "type": "dinner", "name": "观锦餐厅(天廊店)"}]}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 115, "expected_total_attractions": 115, "reported_total_attractions": 230, "meal_per_person_cost_sum": 744, "expected_total_meals": 744, "reported_total_meals": 399, "reported_total_transportation": 600}}]`

### v3_harder_eval_000012
- request: 洛阳 2025-05-03->2025-05-06 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '夜市', '老字号', '城市漫步']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 4, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 1200, "reported_total_hotels": 600, "diff": -600, "covers_nights": false}}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 2000, "total": 1960, "diff": 40, "requested_budget": {"available": true, "amount": 3400, "scope": "total", "party_size": 4, "total": 3400, "source": "budget_constraint", "budget_level": "limited", "strictness": "hard"}, "per_person_day": 122.5, "budget_level": "limited", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "limited", "strictness": "hard", "amount": 3400, "target_min_ratio": 0.72, "target_max_ratio": 1.0, "target_min_total": 2400, "target_max_total": 3400, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 4, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 1200, "reported_total_hotels": 600, "diff": -600, "covers_nights": false}, "hotel_budget_covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 160, "expected_total_attractions": 640, "reported_total_attractions": 240, "meal_per_person_cost_sum": 1772, "expected_total_meals": 7088, "reported_total_meals": 960, "reported_total_transportation": 200}}]`

### v3_harder_eval_000032
- request: 丽江 2026-05-06->2026-05-09 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '夜市', '老字号', '城市漫步']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 4, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 1200, "reported_total_hotels": 600, "diff": -600, "covers_nights": false}}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 2080, "total": 1880, "diff": 200, "requested_budget": {"available": true, "amount": 2400, "scope": "total", "party_size": 4, "total": 2400, "source": "budget_constraint", "budget_level": "limited", "strictness": "hard"}, "per_person_day": 117.5, "budget_level": "limited", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "limited", "strictness": "hard", "amount": 2400, "target_min_ratio": 0.72, "target_max_ratio": 1.0, "target_min_total": 1700, "target_max_total": 2400, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 4, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 1200, "reported_total_hotels": 600, "diff": -600, "covers_nights": false}, "hotel_budget_covers_nights": false}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 240, "expected_total_attractions": 960, "reported_total_attractions": 960, "meal_per_person_cost_sum": 413, "expected_total_meals": 1652, "reported_total_meals": 320, "reported_total_transportation": 200}}]`

### v3_harder_eval_000029
- request: 长沙 2026-03-04->2026-03-07 days=4 transport=打车 hotel=亲子酒店 prefs=['亲子', '老人友好', '博物馆', '城市公园', '特色餐厅']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-03-04", "lunch": "长沙芙蓉国温德姆至尊豪廷大酒店", "dinner": "长沙芙蓉国温德姆至尊豪廷大酒店"}, {"date": "2026-03-05", "lunch": "长沙芙蓉国温德姆至尊豪廷大酒店", "dinner": "长沙芙蓉国温德姆至尊豪廷大酒店"}, {"date": "2026-03-06", "lunch": "长沙芙蓉国温德姆至尊豪廷大酒店", "dinner": "长沙芙蓉国温德姆至尊豪廷大酒店"}, {"date": "2026-03-07", "lunch": "长沙芙蓉国温德姆至尊豪廷大酒店", "dinner": "长沙芙蓉国温德姆至尊豪廷大酒店"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "友好饼店", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-03-04", "type": "breakfast", "name": "友好饼店"}, {"date": "2026-03-05", "type": "breakfast", "name": "友好饼店"}, {"date": "2026-03-06", "type": "breakfast", "name": "友好饼店"}, {"date": "2026-03-07", "type": "breakfast", "name": "友好饼店"}]}, {"name_key": "长沙芙蓉国温德姆至尊豪廷大酒店", "count": 8, "max_allowed": 3, "occurrences": [{"date": "2026-03-04", "type": "lunch", "name": "长沙芙蓉国温德姆至尊豪廷大酒店"}, {"date": "2026-03-04", "type": "dinner", "name": "长沙芙蓉国温德姆至尊豪廷大酒店"}, {"date": "2026-03-05", "type": "lunch", "name": "长沙芙蓉国温德姆至尊豪廷大酒店"}, {"date": "2026-03-05", "type": "dinner", "name": "长沙芙蓉国温德姆至尊豪廷大酒店"}, {"date": "2026-03-06", "type": "lunch", "name": "长沙芙蓉国温德姆至尊豪廷大酒店"}, {"date": "2026-03-06", "type": "dinner", "name": "长沙芙蓉国温德姆至尊豪廷大酒店"}, {"date": "2026-03-07", "type": "lunch", "name": "长沙芙蓉国温德姆至尊豪廷大酒店"}, {"date": "2026-03-07", "type": "dinner", "name": "长沙芙蓉国温德姆至尊豪廷大酒店"}]}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 40, "expected_total_attractions": 80, "reported_total_attractions": 0, "meal_per_person_cost_sum": 1104, "expected_total_meals": 2208, "reported_total_meals": 360, "reported_total_transportation": 800}}]`

### v3_harder_eval_000026
- request: 扬州 2026-05-07->2026-05-10 days=4 transport=自驾 hotel=亲子酒店 prefs=['亲子', '动物园', '海洋馆', '城市公园', '本地美食']
- errors: `[{"stage": "schema", "message": "1 validation error for TripPlan\ndays.3.accommodation\n  Input should be a valid string [type=string_type, input_value=None, input_type=NoneType]\n    For further information visit https://errors.pydantic.dev/2.13/v/string_type"}]`

### v3_harder_eval_000007
- request: 成都 2026-05-07->2026-05-11 days=5 transport=公共交通 hotel=民宿 prefs=['小众展馆', '咖啡', '艺术', '城市漫步', '特色餐厅']
- errors: `[{"stage": "rule", "type": "meal_placeholder", "details": [{"date": "2026-05-08", "type": "dinner", "name": "M Stand(成都SKP店)"}, {"date": "2026-05-10", "type": "lunch", "name": "M Stand(成都SKP店)"}]}, {"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-05-08", "type": "dinner", "name": "M Stand(成都SKP店)", "reason": "unknown_food_semantics"}, {"date": "2026-05-10", "type": "lunch", "name": "M Stand(成都SKP店)", "reason": "unknown_food_semantics"}]}, {"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-05-09", "lunch": "星巴克(成都大魔方招商花园城店)", "dinner": "星巴克(成都环球中心II店)"}, {"date": "2026-05-11", "lunch": "星巴克(成都环球中心II店)", "dinner": "星巴克(成都环球中心II店)"}]}]`

### v3_harder_eval_000009
- request: 苏州 2026-04-26->2026-04-29 days=4 transport=打车 hotel=亲子酒店 prefs=['亲子', '老人友好', '博物馆', '城市公园', '特色餐厅']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 4, "room_count": 2, "priced_nights": 4, "expected_min_total_hotels": 10000, "reported_total_hotels": 4000, "diff": -6000, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 170, "expected_total_attractions": 680, "reported_total_attractions": 350, "meal_per_person_cost_sum": 1296, "expected_total_meals": 5184, "reported_total_meals": 1368, "reported_total_transportation": 1200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 170, "expected_total_attractions": 680, "reported_total_attractions": 350, "meal_per_person_cost_sum": 1296, "expected_total_meals": 5184, "reported_total_meals": 1368, "reported_total_transportation": 1200}}]`

### v3_harder_eval_000002
- request: 杭州 2026-04-27->2026-04-30 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '夜市', '老字号', '城市漫步']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 4, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 1500, "reported_total_hotels": 750, "diff": -750, "covers_nights": false}}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 2280, "total": 2200, "diff": 80, "requested_budget": {"available": true, "amount": 3100, "scope": "total", "party_size": 4, "total": 3100, "source": "budget_constraint", "budget_level": "limited", "strictness": "hard"}, "per_person_day": 137.5, "budget_level": "limited", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "limited", "strictness": "hard", "amount": 3100, "target_min_ratio": 0.72, "target_max_ratio": 1.0, "target_min_total": 2200, "target_max_total": 3100, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 4, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 1500, "reported_total_hotels": 750, "diff": -750, "covers_nights": false}, "hotel_budget_covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 110, "expected_total_attractions": 440, "reported_total_attractions": 250, "meal_per_person_cost_sum": 3660, "expected_total_meals": 14640, "reported_total_meals": 1080, "reported_total_transportation": 200}}]`

### v3_harder_eval_000036
- request: 长沙 2026-06-02->2026-06-05 days=4 transport=自驾 hotel=亲子酒店 prefs=['亲子', '动物园', '海洋馆', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "accommodation_type_mismatch", "details": [{"date": "2026-06-05", "day_index": 3, "expected": "亲子酒店", "got": "无"}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 3, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 3000, "reported_total_hotels": 1500, "diff": -1500, "covers_nights": false}}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 2640, "total": 2840, "diff": -200, "requested_budget": {"available": true, "amount": 5000, "scope": "total", "party_size": 3, "total": 5000, "source": "budget_constraint", "budget_level": "standard", "strictness": "hard"}, "per_person_day": 236.67, "budget_level": "standard", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "standard", "strictness": "hard", "amount": 5000, "target_min_ratio": 0.55, "target_max_ratio": 1.0, "target_min_total": 2800, "target_max_total": 5000, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 3, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 3000, "reported_total_hotels": 1500, "diff": -1500, "covers_nights": false}, "hotel_budget_covers_nights": false}}]`

### v3_harder_eval_000001
- request: 桂林 2026-08-31->2026-09-03 days=4 transport=打车 hotel=高端酒店 prefs=['高端酒店', '艺术', '特色餐厅', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 6555, "total": 5555, "diff": 1000, "requested_budget": {"available": true, "amount": 9100, "scope": "total", "party_size": 2, "total": 9100, "source": "budget_constraint", "budget_level": "premium", "strictness": "soft"}, "per_person_day": 694.38, "budget_level": "premium", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "premium", "strictness": "soft", "amount": 9100, "target_min_ratio": 0.7, "target_max_ratio": 1.12, "target_min_total": 6400, "target_max_total": 10200, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 2, "room_count": 1, "priced_nights": 4, "expected_min_total_hotels": 3000, "reported_total_hotels": 3000, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 525, "expected_total_attractions": 1050, "reported_total_attractions": 1275, "meal_per_person_cost_sum": 1032, "expected_total_meals": 2064, "reported_total_meals": 1080, "reported_total_transportation": 1200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 525, "expected_total_attractions": 1050, "reported_total_attractions": 1275, "meal_per_person_cost_sum": 1032, "expected_total_meals": 2064, "reported_total_meals": 1080, "reported_total_transportation": 1200}}]`
