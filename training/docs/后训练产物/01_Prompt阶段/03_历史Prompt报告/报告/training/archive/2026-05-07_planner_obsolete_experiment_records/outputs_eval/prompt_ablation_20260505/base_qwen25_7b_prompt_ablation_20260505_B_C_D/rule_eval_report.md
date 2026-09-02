# Rule Eval Report: base_qwen25_7b_prompt_ablation_20260505_B_C_D

- records: 300
- generations: `training/outputs/eval/prompt_ablation_20260505/base_qwen25_7b_prompt_ablation_20260505_B_C_D/generations.jsonl`
- records_path: `training/data/v3/eval_harder_prompt_ablation_20260505/B_C_D/records.jsonl`

## Boolean Metrics

| Metric | Pass | Total | Rate |
| --- | ---: | ---: | ---: |
| accommodation_type_ok | 217 | 283 | 76.68% |
| attraction_budget_consistent | 30 | 283 | 10.60% |
| attraction_budget_party_relation_ok | 65 | 283 | 22.97% |
| attraction_count_ok | 282 | 283 | 99.65% |
| attraction_diversity_ok | 245 | 283 | 86.57% |
| attraction_grounding_ok | 278 | 283 | 98.23% |
| attraction_repeat_limit_ok | 245 | 283 | 86.57% |
| budget_arithmetic_consistent | 128 | 283 | 45.23% |
| budget_consistent | 128 | 283 | 45.23% |
| budget_level_aligned | 117 | 283 | 41.34% |
| budget_preference_aligned | 117 | 283 | 41.34% |
| budget_relationship_ok | 15 | 283 | 5.30% |
| budget_user_constraint_ok | 237 | 283 | 83.75% |
| budget_within_user_budget | 266 | 283 | 93.99% |
| city_ok | 283 | 283 | 100.00% |
| date_range_ok | 283 | 283 | 100.00% |
| day_dates_ok | 283 | 283 | 100.00% |
| day_index_ok | 283 | 283 | 100.00% |
| days_len_ok | 283 | 283 | 100.00% |
| dpo_soft_pass | 0 | 283 | 0.00% |
| hard_pass | 0 | 283 | 0.00% |
| hotel_budget_covers_nights | 103 | 283 | 36.40% |
| hotel_budget_relation_ok | 116 | 283 | 40.99% |
| hotel_distance_placeholder_ok | 283 | 283 | 100.00% |
| hotel_grounding_ok | 282 | 283 | 99.65% |
| invalid_hotel_name_ok | 283 | 283 | 100.00% |
| json_extract_ok | 299 | 300 | 99.67% |
| legacy_hard_pass | 18 | 283 | 6.36% |
| location_object_ok | 283 | 283 | 100.00% |
| meal_budget_consistent | 0 | 283 | 0.00% |
| meal_complete | 283 | 283 | 100.00% |
| meal_cost_scale_ok | 186 | 283 | 65.72% |
| meal_diversity_ok | 188 | 283 | 66.43% |
| meal_grounding_ok | 146 | 283 | 51.59% |
| meal_lunch_dinner_same_day_ok | 245 | 283 | 86.57% |
| meal_repeat_limit_ok | 208 | 283 | 73.50% |
| meal_specific_ok | 271 | 283 | 95.76% |
| meal_valid_semantics_ok | 162 | 283 | 57.24% |
| middle_hotel_ok | 283 | 283 | 100.00% |
| schema_ok | 283 | 300 | 94.33% |
| sft_budget_semantic_hard_pass | 5 | 283 | 1.77% |
| sft_hard_pass | 0 | 283 | 0.00% |
| transportation_budget_nonnegative | 283 | 283 | 100.00% |
| weather_dates_ok | 283 | 283 | 100.00% |
| weather_match | 282 | 283 | 99.65% |

## Numeric Metrics

```json
{
  "attraction_diversity_unique_rate": {
    "avg": 0.9702,
    "p50": 1.0,
    "p90": 1.0
  },
  "attraction_grounding_rate": {
    "avg": 0.9965,
    "p50": 1.0,
    "p90": 1.0
  },
  "hotel_grounding_rate": {
    "avg": 0.9991,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_diversity_unique_rate": {
    "avg": 0.517,
    "p50": 0.5,
    "p90": 1.0
  },
  "meal_food_pois_grounding_rate": {
    "avg": 0.8296,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_grounding_rate": {
    "avg": 0.8296,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_semantic_valid_rate": {
    "avg": 0.8869,
    "p50": 1.0,
    "p90": 1.0
  }
}
```

## Failure Types

```json
{
  "meal_budget_inconsistent": 281,
  "budget_relationship_mismatch": 268,
  "attraction_budget_inconsistent": 253,
  "hotel_budget_underestimated": 180,
  "budget_preference_mismatch": 166,
  "budget_arithmetic_inconsistent": 155,
  "meal_invalid_name": 121,
  "meal_cost_scale_too_low": 97,
  "meal_repeat_too_many": 75,
  "accommodation_type_mismatch": 66,
  "budget_hard_constraint_exceeded": 46,
  "attraction_repeat_too_many": 38,
  "meal_same_day_lunch_dinner_repeat": 38,
  "schema": 16,
  "meal_grounding_miss": 16,
  "meal_placeholder": 12,
  "weather_mismatch": 1,
  "json_extract": 1
}
```

## Failure Examples

### v3_harder_eval_000014
- request: 成都 2026-06-02->2026-06-04 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆']
- errors: `[{"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-06-04", "type": "dinner", "name": "无", "reason": "empty_or_none"}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 2, "party_total": 1, "room_count": 1, "priced_nights": 2, "expected_min_total_hotels": 900, "reported_total_hotels": 1350, "diff": 450, "covers_nights": false}}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 2115, "total": 2100, "diff": 15, "requested_budget": {"available": true, "amount": 2100, "scope": "total", "party_size": 1, "total": 2100, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "hard"}, "per_person_day": 700.0, "budget_level": "comfortable", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "hard", "amount": 2100, "target_min_ratio": 0.65, "target_max_ratio": 1.0, "target_min_total": 1400, "target_max_total": 2100, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 1, "room_count": 1, "priced_nights": 2, "expected_min_total_hotels": 900, "reported_total_hotels": 1350, "diff": 450, "covers_nights": false}, "hotel_budget_covers_nights": false}}]`

### v3_harder_eval_000024
- request: 济南 2026-05-06->2026-05-08 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆']
- errors: `[{"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-05-08", "type": "dinner", "name": "酒店早餐", "reason": "hotel_or_lodging_name"}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 2, "party_total": 1, "room_count": 1, "priced_nights": 3, "expected_min_total_hotels": 1200, "reported_total_hotels": 800, "diff": -400, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 240, "expected_total_attractions": 240, "reported_total_attractions": 480, "meal_per_person_cost_sum": 493, "expected_total_meals": 493, "reported_total_meals": 240, "reported_total_transportation": 200}}]`

### v3_harder_eval_000011
- request: 福州 2026-06-17->2026-06-20 days=4 transport=打车 hotel=高端酒店 prefs=['高端酒店', '艺术', '特色餐厅', '城市地标', '休闲慢游']
- errors: `[{"stage": "schema", "message": "1 validation error for TripPlan\ndays.3.accommodation\n  Input should be a valid string [type=string_type, input_value=None, input_type=NoneType]\n    For further information visit https://errors.pydantic.dev/2.13/v/string_type"}]`

### v3_harder_eval_000002
- request: 杭州 2026-04-27->2026-04-30 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '夜市', '老字号', '城市漫步']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 4, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 1500, "reported_total_hotels": 1000, "diff": -500, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 110, "expected_total_attractions": 440, "reported_total_attractions": 220, "meal_per_person_cost_sum": 3660, "expected_total_meals": 14640, "reported_total_meals": 960, "reported_total_transportation": 400}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 110, "expected_total_attractions": 440, "reported_total_attractions": 220, "meal_per_person_cost_sum": 3660, "expected_total_meals": 14640, "reported_total_meals": 960, "reported_total_transportation": 400}}]`

### v3_harder_eval_000012
- request: 洛阳 2025-05-03->2025-05-06 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '夜市', '老字号', '城市漫步']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 4, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 1200, "reported_total_hotels": 600, "diff": -600, "covers_nights": false}}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 1400, "total": 1480, "diff": -80, "requested_budget": {"available": true, "amount": 3400, "scope": "total", "party_size": 4, "total": 3400, "source": "budget_constraint", "budget_level": "limited", "strictness": "hard"}, "per_person_day": 92.5, "budget_level": "limited", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "limited", "strictness": "hard", "amount": 3400, "target_min_ratio": 0.72, "target_max_ratio": 1.0, "target_min_total": 2400, "target_max_total": 3400, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 4, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 1200, "reported_total_hotels": 600, "diff": -600, "covers_nights": false}, "hotel_budget_covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 240, "expected_total_attractions": 960, "reported_total_attractions": 120, "meal_per_person_cost_sum": 1616, "expected_total_meals": 6464, "reported_total_meals": 480, "reported_total_transportation": 200}}]`

### v3_harder_eval_000022
- request: 桂林 2026-04-03->2026-04-06 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '夜市', '老字号', '城市漫步']
- errors: `[{"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-04-06", "type": "dinner", "name": "无", "reason": "empty_or_none"}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 525, "expected_total_attractions": 2100, "reported_total_attractions": 1100, "meal_per_person_cost_sum": 1516, "expected_total_meals": 6064, "reported_total_meals": 480, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 525, "expected_total_attractions": 2100, "reported_total_attractions": 1100, "meal_per_person_cost_sum": 1516, "expected_total_meals": 6064, "reported_total_meals": 480, "reported_total_transportation": 200}}]`

### v3_harder_eval_000004
- request: 张家界 2026-05-07->2026-05-09 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 80, "expected_total_attractions": 80, "reported_total_attractions": 240, "meal_per_person_cost_sum": 418, "expected_total_meals": 418, "reported_total_meals": 180, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 80, "expected_total_attractions": 80, "reported_total_attractions": 240, "meal_per_person_cost_sum": 418, "expected_total_meals": 418, "reported_total_meals": 180, "reported_total_transportation": 200}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": false, "meal_cost_scale_ok": false, "budget_relationship_ok": false, "expected_total_hotels": 800, "reported_total_hotels": 800, "expected_total_attractions": 80, "reported_total_attractions": 240, "meal_scale_eval": {"ok": false, "party_total": 1, "budget_level": "comfortable", "per_person_lunch_dinner_floor": 50, "per_person_breakfast_floor": 20, "meal_count": 9, "checked_count": 6, "failure_count": 2, "failures": [{"date": "2026-05-07", "type": "dinner", "name": "自由人(张家界国光实验学校店)", "estimated_cost": 7, "min_expected_cost": 50}, {"date": "2026-05-08", "type": "dinner", "name": "业华湘·特色菜", "estimated_cost": 35, "min_expected_cost": 50}]}}}]`

### v3_harder_eval_000032
- request: 丽江 2026-05-06->2026-05-09 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '夜市', '老字号', '城市漫步']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 4, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 1200, "reported_total_hotels": 600, "diff": -600, "covers_nights": false}}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 2144, "total": 1944, "diff": 200, "requested_budget": {"available": true, "amount": 2400, "scope": "total", "party_size": 4, "total": 2400, "source": "budget_constraint", "budget_level": "limited", "strictness": "hard"}, "per_person_day": 121.5, "budget_level": "limited", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "limited", "strictness": "hard", "amount": 2400, "target_min_ratio": 0.72, "target_max_ratio": 1.0, "target_min_total": 1700, "target_max_total": 2400, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 4, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 1200, "reported_total_hotels": 600, "diff": -600, "covers_nights": false}, "hotel_budget_covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 320, "expected_total_attractions": 1280, "reported_total_attractions": 960, "meal_per_person_cost_sum": 802, "expected_total_meals": 3208, "reported_total_meals": 384, "reported_total_transportation": 200}}]`

### v3_harder_eval_000038
- request: 厦门 2026-05-06->2026-05-08 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 2, "party_total": 3, "room_count": 2, "priced_nights": 2, "expected_min_total_hotels": 3200, "reported_total_hotels": 2400, "diff": -800, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 100, "expected_total_attractions": 300, "reported_total_attractions": 240, "meal_per_person_cost_sum": 1569, "expected_total_meals": 4707, "reported_total_meals": 1440, "reported_total_transportation": 600}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 100, "expected_total_attractions": 300, "reported_total_attractions": 240, "meal_per_person_cost_sum": 1569, "expected_total_meals": 4707, "reported_total_meals": 1440, "reported_total_transportation": 600}}]`

### v3_harder_eval_000034
- request: 武汉 2026-06-02->2026-06-04 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 2, "party_total": 1, "room_count": 1, "priced_nights": 2, "expected_min_total_hotels": 800, "reported_total_hotels": 1200, "diff": 400, "covers_nights": false}}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 2180, "total": 2400, "diff": -220, "requested_budget": {"available": true, "amount": 1800, "scope": "total", "party_size": 1, "total": 1800, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "hard"}, "per_person_day": 800.0, "budget_level": "comfortable", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "hard", "amount": 1800, "target_min_ratio": 0.65, "target_max_ratio": 1.0, "target_min_total": 1200, "target_max_total": 1800, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": false, "user_constraint_ok": false, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 1, "room_count": 1, "priced_nights": 2, "expected_min_total_hotels": 800, "reported_total_hotels": 1200, "diff": 400, "covers_nights": false}, "hotel_budget_covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 70, "expected_total_attractions": 70, "reported_total_attractions": 140, "meal_per_person_cost_sum": 463, "expected_total_meals": 463, "reported_total_meals": 240, "reported_total_transportation": 600}}]`

### v3_harder_eval_000016
- request: 苏州 2026-06-02->2026-06-05 days=4 transport=自驾 hotel=亲子酒店 prefs=['亲子', '动物园', '海洋馆', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "accommodation_type_mismatch", "details": [{"date": "2026-06-02", "day_index": 0, "expected": "亲子酒店", "got": "经济型酒店"}, {"date": "2026-06-03", "day_index": 1, "expected": "亲子酒店", "got": "经济型酒店"}, {"date": "2026-06-04", "day_index": 2, "expected": "亲子酒店", "got": "经济型酒店"}, {"date": "2026-06-05", "day_index": 3, "expected": "亲子酒店", "got": "经济型酒店"}]}, {"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-06-02", "type": "dinner", "name": "酒店晚餐", "reason": "generic_lodging_meal"}, {"date": "2026-06-03", "type": "dinner", "name": "酒店晚餐", "reason": "generic_lodging_meal"}, {"date": "2026-06-04", "type": "dinner", "name": "酒店晚餐", "reason": "generic_lodging_meal"}, {"date": "2026-06-05", "type": "dinner", "name": "酒店晚餐", "reason": "generic_lodging_meal"}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 3, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 4700, "reported_total_hotels": 3300, "diff": -1400, "covers_nights": false}}]`

### v3_harder_eval_000018
- request: 天津 2026-07-02->2026-07-04 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物']
- errors: `[{"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-07-04", "type": "dinner", "name": "酒店早餐", "reason": "hotel_or_lodging_name"}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 2, "party_total": 3, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 7200, "reported_total_hotels": 3600, "diff": -3600, "covers_nights": false}}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 5850, "total": 5750, "diff": 100, "requested_budget": {"available": true, "amount": 4800, "scope": "total", "party_size": 3, "total": 4800, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "hard"}, "per_person_day": 638.89, "budget_level": "comfortable", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "hard", "amount": 4800, "target_min_ratio": 0.65, "target_max_ratio": 1.0, "target_min_total": 3100, "target_max_total": 4800, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": false, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 3, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 7200, "reported_total_hotels": 3600, "diff": -3600, "covers_nights": false}, "hotel_budget_covers_nights": false}}]`

### v3_harder_eval_000008
- request: 大理 2026-05-07->2026-05-09 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物']
- errors: `[{"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-05-09", "type": "dinner", "name": "无", "reason": "empty_or_none"}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 2, "party_total": 3, "room_count": 2, "priced_nights": 2, "expected_min_total_hotels": 3000, "reported_total_hotels": 1500, "diff": -1500, "covers_nights": false}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 75, "expected_total_attractions": 225, "reported_total_attractions": 225, "meal_per_person_cost_sum": 1275, "expected_total_meals": 3825, "reported_total_meals": 1050, "reported_total_transportation": 600}}]`

### v3_harder_eval_000028
- request: 深圳 2026-03-04->2026-03-06 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物']
- errors: `[{"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-03-06", "type": "dinner", "name": "酒店早餐", "reason": "hotel_or_lodging_name"}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 2, "party_total": 3, "room_count": 2, "priced_nights": 2, "expected_min_total_hotels": 3200, "reported_total_hotels": 1600, "diff": -1600, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 240, "expected_total_attractions": 720, "reported_total_attractions": 240, "meal_per_person_cost_sum": 1988, "expected_total_meals": 5964, "reported_total_meals": 1620, "reported_total_transportation": 600}}]`

### v3_harder_eval_000019
- request: 丽江 2026-05-07->2026-05-10 days=4 transport=打车 hotel=亲子酒店 prefs=['亲子', '老人友好', '博物馆', '城市公园', '特色餐厅']
- errors: `[{"stage": "rule", "type": "accommodation_type_mismatch", "details": [{"date": "2026-05-10", "day_index": 3, "expected": "亲子酒店", "got": "无"}]}, {"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-05-07", "type": "breakfast", "name": "丽江古城内的特色早餐", "reason": "unknown_food_semantics"}, {"date": "2026-05-08", "type": "breakfast", "name": "丽江古城内的特色早餐", "reason": "unknown_food_semantics"}, {"date": "2026-05-09", "type": "breakfast", "name": "丽江古城内的特色早餐", "reason": "unknown_food_semantics"}, {"date": "2026-05-10", "type": "breakfast", "name": "酒店提供的早餐", "reason": "hotel_or_lodging_name"}]}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 3020, "total": 3380, "diff": -360, "requested_budget": {"available": true, "amount": 5300, "scope": "total", "party_size": 2, "total": 5300, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "soft"}, "per_person_day": 422.5, "budget_level": "comfortable", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "soft", "amount": 5300, "target_min_ratio": 0.65, "target_max_ratio": 1.05, "target_min_total": 3400, "target_max_total": 5600, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 2, "room_count": 1, "priced_nights": 3, "expected_min_total_hotels": 1500, "reported_total_hotels": 1500, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_harder_eval_000029
- request: 长沙 2026-03-04->2026-03-07 days=4 transport=打车 hotel=亲子酒店 prefs=['亲子', '老人友好', '博物馆', '城市公园', '特色餐厅']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "乐悠悠亲子乐园", "count": 4, "max_allowed": 1, "occurrences": [{"date": "2026-03-04", "day_index": 0, "name": "乐悠悠亲子乐园"}, {"date": "2026-03-05", "day_index": 1, "name": "乐悠悠亲子乐园"}, {"date": "2026-03-06", "day_index": 2, "name": "乐悠悠亲子乐园"}, {"date": "2026-03-07", "day_index": 3, "name": "乐悠悠亲子乐园"}]}]}, {"stage": "rule", "type": "accommodation_type_mismatch", "details": [{"date": "2026-03-07", "day_index": 3, "expected": "亲子酒店", "got": "无"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "友好饼店", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-03-04", "type": "breakfast", "name": "友好饼店"}, {"date": "2026-03-05", "type": "breakfast", "name": "友好饼店"}, {"date": "2026-03-06", "type": "breakfast", "name": "友好饼店"}, {"date": "2026-03-07", "type": "breakfast", "name": "友好饼店"}]}, {"name_key": "长沙芙蓉国温德姆至尊豪廷大酒店", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-03-04", "type": "lunch", "name": "长沙芙蓉国温德姆至尊豪廷大酒店"}, {"date": "2026-03-05", "type": "lunch", "name": "长沙芙蓉国温德姆至尊豪廷大酒店"}, {"date": "2026-03-06", "type": "lunch", "name": "长沙芙蓉国温德姆至尊豪廷大酒店"}, {"date": "2026-03-07", "type": "lunch", "name": "长沙芙蓉国温德姆至尊豪廷大酒店"}]}, {"name_key": "友好友善茶饮巴士", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-03-04", "type": "dinner", "name": "友好友善茶饮巴士"}, {"date": "2026-03-05", "type": "dinner", "name": "友好友善茶饮巴士"}, {"date": "2026-03-06", "type": "dinner", "name": "友好友善茶饮巴士"}, {"date": "2026-03-07", "type": "dinner", "name": "友好友善茶饮巴士"}]}]}]`

### v3_harder_eval_000006
- request: 南京 2026-07-02->2026-07-05 days=4 transport=自驾 hotel=亲子酒店 prefs=['亲子', '动物园', '海洋馆', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "accommodation_type_mismatch", "details": [{"date": "2026-07-05", "day_index": 3, "expected": "亲子酒店", "got": "无"}]}, {"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-07-05", "type": "dinner", "name": "酒店晚餐", "reason": "generic_lodging_meal"}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 3, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 3300, "reported_total_hotels": 1650, "diff": -1650, "covers_nights": false}}]`

### v3_harder_eval_000031
- request: 成都 2026-05-07->2026-05-10 days=4 transport=打车 hotel=高端酒店 prefs=['高端酒店', '艺术', '特色餐厅', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-05-10", "type": "dinner", "name": "酒店晚餐", "reason": "generic_lodging_meal"}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 195, "expected_total_attractions": 390, "reported_total_attractions": 450, "meal_per_person_cost_sum": 1836, "expected_total_meals": 3672, "reported_total_meals": 1020, "reported_total_transportation": 800}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 195, "expected_total_attractions": 390, "reported_total_attractions": 450, "meal_per_person_cost_sum": 1836, "expected_total_meals": 3672, "reported_total_meals": 1020, "reported_total_transportation": 800}}]`

### v3_harder_eval_000007
- request: 成都 2026-05-07->2026-05-11 days=5 transport=公共交通 hotel=民宿 prefs=['小众展馆', '咖啡', '艺术', '城市漫步', '特色餐厅']
- errors: `[{"stage": "rule", "type": "accommodation_type_mismatch", "details": [{"date": "2026-05-11", "day_index": 4, "expected": "民宿", "got": "无"}]}, {"stage": "rule", "type": "meal_placeholder", "details": [{"date": "2026-05-08", "type": "dinner", "name": "M Stand(成都SKP店)"}, {"date": "2026-05-10", "type": "lunch", "name": "M Stand(成都SKP店)"}]}, {"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-05-08", "type": "dinner", "name": "M Stand(成都SKP店)", "reason": "unknown_food_semantics"}, {"date": "2026-05-10", "type": "lunch", "name": "M Stand(成都SKP店)", "reason": "unknown_food_semantics"}]}]`

### v3_harder_eval_000013
- request: 武汉 2026-05-05->2026-05-09 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-05-05", "type": "lunch", "name": "东湖家旅游民宿(东湖风景区店)附近的餐厅", "reason": "hotel_or_lodging_name"}, {"date": "2026-05-05", "type": "dinner", "name": "东湖家旅游民宿(东湖风景区店)附近的餐厅", "reason": "hotel_or_lodging_name"}, {"date": "2026-05-06", "type": "lunch", "name": "东湖家旅游民宿(东湖风景区店)附近的餐厅", "reason": "hotel_or_lodging_name"}, {"date": "2026-05-06", "type": "dinner", "name": "东湖家旅游民宿(东湖风景区店)附近的餐厅", "reason": "hotel_or_lodging_name"}, {"date": "2026-05-07", "type": "lunch", "name": "东湖家旅游民宿(东湖风景区店)附近的餐厅", "reason": "hotel_or_lodging_name"}, {"date": "2026-05-07", "type": "dinner", "name": "东湖家旅游民宿(东湖风景区店)附近的餐厅", "reason": "hotel_or_lodging_name"}, {"date": "2026-05-08", "type": "lunch", "name": "东湖家旅游民宿(东湖风景区店)附近的餐厅", "reason": "hotel_or_lodging_name"}, {"date": "2026-05-08", "type": "dinner", "name": "东湖家旅游民宿(东湖风景区店)附近的餐厅", "reason": "hotel_or_lodging_name"}, {"date": "2026-05-09", "type": "lunch", "name": "东湖家旅游民宿(东湖风景区店)附近的餐厅", "reason": "hotel_or_lodging_name"}, {"date": "2026-05-09", "type": "dinner", "name": "东湖家旅游民宿(东湖风景区店)附近的餐厅", "reason": "hotel_or_lodging_name"}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 4, "party_total": 2, "room_count": 1, "priced_nights": 4, "expected_min_total_hotels": 1600, "reported_total_hotels": 2000, "diff": 400, "covers_nights": false}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 0, "expected_total_attractions": 0, "reported_total_attractions": 0, "meal_per_person_cost_sum": 800, "expected_total_meals": 1600, "reported_total_meals": 1200, "reported_total_transportation": 500}}]`
