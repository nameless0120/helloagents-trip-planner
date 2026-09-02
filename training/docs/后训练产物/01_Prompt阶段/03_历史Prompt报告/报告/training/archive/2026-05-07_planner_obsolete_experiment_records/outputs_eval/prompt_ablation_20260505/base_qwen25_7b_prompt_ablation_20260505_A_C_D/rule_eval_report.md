# Rule Eval Report: base_qwen25_7b_prompt_ablation_20260505_A_C_D

- records: 300
- generations: `training/outputs/eval/prompt_ablation_20260505/base_qwen25_7b_prompt_ablation_20260505_A_C_D/generations.jsonl`
- records_path: `training/data/v3/eval_harder_prompt_ablation_20260505/A_C_D/records.jsonl`

## Boolean Metrics

| Metric | Pass | Total | Rate |
| --- | ---: | ---: | ---: |
| accommodation_type_ok | 241 | 299 | 80.60% |
| attraction_budget_consistent | 36 | 299 | 12.04% |
| attraction_budget_party_relation_ok | 79 | 299 | 26.42% |
| attraction_count_ok | 299 | 299 | 100.00% |
| attraction_diversity_ok | 258 | 299 | 86.29% |
| attraction_grounding_ok | 296 | 299 | 99.00% |
| attraction_repeat_limit_ok | 258 | 299 | 86.29% |
| budget_arithmetic_consistent | 162 | 299 | 54.18% |
| budget_consistent | 162 | 299 | 54.18% |
| budget_level_aligned | 119 | 299 | 39.80% |
| budget_preference_aligned | 119 | 299 | 39.80% |
| budget_relationship_ok | 28 | 299 | 9.36% |
| budget_user_constraint_ok | 249 | 299 | 83.28% |
| budget_within_user_budget | 283 | 299 | 94.65% |
| city_ok | 299 | 299 | 100.00% |
| date_range_ok | 299 | 299 | 100.00% |
| day_dates_ok | 299 | 299 | 100.00% |
| day_index_ok | 299 | 299 | 100.00% |
| days_len_ok | 299 | 299 | 100.00% |
| dpo_soft_pass | 0 | 299 | 0.00% |
| hard_pass | 0 | 299 | 0.00% |
| hotel_budget_covers_nights | 114 | 299 | 38.13% |
| hotel_budget_relation_ok | 131 | 299 | 43.81% |
| hotel_distance_placeholder_ok | 299 | 299 | 100.00% |
| hotel_grounding_ok | 297 | 299 | 99.33% |
| invalid_hotel_name_ok | 299 | 299 | 100.00% |
| json_extract_ok | 299 | 300 | 99.67% |
| legacy_hard_pass | 22 | 299 | 7.36% |
| location_object_ok | 299 | 299 | 100.00% |
| meal_budget_consistent | 0 | 299 | 0.00% |
| meal_complete | 298 | 299 | 99.67% |
| meal_cost_scale_ok | 204 | 299 | 68.23% |
| meal_diversity_ok | 206 | 299 | 68.90% |
| meal_grounding_ok | 168 | 299 | 56.19% |
| meal_lunch_dinner_same_day_ok | 248 | 299 | 82.94% |
| meal_repeat_limit_ok | 234 | 299 | 78.26% |
| meal_specific_ok | 288 | 299 | 96.32% |
| meal_valid_semantics_ok | 181 | 299 | 60.54% |
| middle_hotel_ok | 299 | 299 | 100.00% |
| schema_ok | 299 | 300 | 99.67% |
| sft_budget_semantic_hard_pass | 12 | 299 | 4.01% |
| sft_hard_pass | 0 | 299 | 0.00% |
| transportation_budget_nonnegative | 299 | 299 | 100.00% |
| weather_dates_ok | 299 | 299 | 100.00% |
| weather_match | 298 | 299 | 99.67% |

## Numeric Metrics

```json
{
  "attraction_diversity_unique_rate": {
    "avg": 0.9694,
    "p50": 1.0,
    "p90": 1.0
  },
  "attraction_grounding_rate": {
    "avg": 0.998,
    "p50": 1.0,
    "p90": 1.0
  },
  "hotel_grounding_rate": {
    "avg": 0.9975,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_diversity_unique_rate": {
    "avg": 0.5148,
    "p50": 0.5,
    "p90": 1.0
  },
  "meal_food_pois_grounding_rate": {
    "avg": 0.8321,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_grounding_rate": {
    "avg": 0.8321,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_semantic_valid_rate": {
    "avg": 0.8949,
    "p50": 1.0,
    "p90": 1.0
  }
}
```

## Failure Types

```json
{
  "meal_budget_inconsistent": 298,
  "budget_relationship_mismatch": 271,
  "attraction_budget_inconsistent": 263,
  "hotel_budget_underestimated": 185,
  "budget_preference_mismatch": 180,
  "budget_arithmetic_inconsistent": 137,
  "meal_invalid_name": 118,
  "meal_cost_scale_too_low": 95,
  "meal_repeat_too_many": 65,
  "accommodation_type_mismatch": 58,
  "meal_same_day_lunch_dinner_repeat": 51,
  "budget_hard_constraint_exceeded": 50,
  "attraction_repeat_too_many": 41,
  "meal_grounding_miss": 13,
  "meal_placeholder": 11,
  "weather_mismatch": 1,
  "json_extract": 1
}
```

## Failure Examples

### v3_harder_eval_000002
- request: 杭州 2026-04-27->2026-04-30 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '夜市', '老字号', '城市漫步']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 4, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 1500, "reported_total_hotels": 1000, "diff": -500, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 110, "expected_total_attractions": 440, "reported_total_attractions": 1020, "meal_per_person_cost_sum": 2576, "expected_total_meals": 10304, "reported_total_meals": 1152, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 110, "expected_total_attractions": 440, "reported_total_attractions": 1020, "meal_per_person_cost_sum": 2576, "expected_total_meals": 10304, "reported_total_meals": 1152, "reported_total_transportation": 200}}]`

### v3_harder_eval_000018
- request: 天津 2026-07-02->2026-07-04 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "南楼煎饼", "count": 3, "max_allowed": 2, "occurrences": [{"date": "2026-07-02", "type": "breakfast", "name": "南楼煎饼(南楼总店)"}, {"date": "2026-07-03", "type": "breakfast", "name": "南楼煎饼(南楼总店)"}, {"date": "2026-07-04", "type": "breakfast", "name": "南楼煎饼(南楼总店)"}]}, {"name_key": "苏焰·地标天津菜", "count": 3, "max_allowed": 2, "occurrences": [{"date": "2026-07-02", "type": "dinner", "name": "苏焰·地标天津菜(金海道店)"}, {"date": "2026-07-03", "type": "dinner", "name": "苏焰·地标天津菜(金海道店)"}, {"date": "2026-07-04", "type": "dinner", "name": "苏焰·地标天津菜(金海道店)"}]}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 2, "party_total": 3, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 7200, "reported_total_hotels": 3600, "diff": -3600, "covers_nights": false}}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 6030, "total": 5930, "diff": 100, "requested_budget": {"available": true, "amount": 4800, "scope": "total", "party_size": 3, "total": 4800, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "hard"}, "per_person_day": 658.89, "budget_level": "comfortable", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "hard", "amount": 4800, "target_min_ratio": 0.65, "target_max_ratio": 1.0, "target_min_total": 3100, "target_max_total": 4800, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": false, "user_constraint_ok": false, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 3, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 7200, "reported_total_hotels": 3600, "diff": -3600, "covers_nights": false}, "hotel_budget_covers_nights": false}}]`

### v3_harder_eval_000012
- request: 洛阳 2025-05-03->2025-05-06 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '夜市', '老字号', '城市漫步']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 4, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 1200, "reported_total_hotels": 600, "diff": -600, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 160, "expected_total_attractions": 640, "reported_total_attractions": 240, "meal_per_person_cost_sum": 1772, "expected_total_meals": 7088, "reported_total_meals": 920, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 160, "expected_total_attractions": 640, "reported_total_attractions": 240, "meal_per_person_cost_sum": 1772, "expected_total_meals": 7088, "reported_total_meals": 920, "reported_total_transportation": 200}}]`

### v3_harder_eval_000014
- request: 成都 2026-06-02->2026-06-04 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-06-02", "lunch": "观锦餐厅(天廊店)", "dinner": "观锦餐厅(天府新谷店)"}, {"date": "2026-06-04", "lunch": "陈麻婆豆腐(旗舰店)", "dinner": "陈麻婆豆腐(旗舰店)"}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 60, "expected_total_attractions": 60, "reported_total_attractions": 180, "meal_per_person_cost_sum": 700, "expected_total_meals": 700, "reported_total_meals": 414, "reported_total_transportation": 600}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 60, "expected_total_attractions": 60, "reported_total_attractions": 180, "meal_per_person_cost_sum": 700, "expected_total_meals": 700, "reported_total_meals": 414, "reported_total_transportation": 600}}]`

### v3_harder_eval_000029
- request: 长沙 2026-03-04->2026-03-07 days=4 transport=打车 hotel=亲子酒店 prefs=['亲子', '老人友好', '博物馆', '城市公园', '特色餐厅']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "友好饼店", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-03-04", "type": "lunch", "name": "友好饼店"}, {"date": "2026-03-05", "type": "lunch", "name": "友好饼店"}, {"date": "2026-03-06", "type": "lunch", "name": "友好饼店"}, {"date": "2026-03-07", "type": "lunch", "name": "友好饼店"}]}, {"name_key": "长沙芙蓉国温德姆至尊豪廷大酒店", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-03-04", "type": "dinner", "name": "长沙芙蓉国温德姆至尊豪廷大酒店"}, {"date": "2026-03-05", "type": "dinner", "name": "长沙芙蓉国温德姆至尊豪廷大酒店"}, {"date": "2026-03-06", "type": "dinner", "name": "长沙芙蓉国温德姆至尊豪廷大酒店"}, {"date": "2026-03-07", "type": "dinner", "name": "长沙芙蓉国温德姆至尊豪廷大酒店"}]}]}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 3280, "total": 4000, "diff": -720, "requested_budget": {"available": true, "amount": 6200, "scope": "total", "party_size": 2, "total": 6200, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "soft"}, "per_person_day": 500.0, "budget_level": "comfortable", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "soft", "amount": 6200, "target_min_ratio": 0.65, "target_max_ratio": 1.05, "target_min_total": 4000, "target_max_total": 6500, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 2, "room_count": 1, "priced_nights": 4, "expected_min_total_hotels": 2000, "reported_total_hotels": 2000, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 40, "expected_total_attractions": 80, "reported_total_attractions": 120, "meal_per_person_cost_sum": 744, "expected_total_meals": 1488, "reported_total_meals": 360, "reported_total_transportation": 800}}]`

### v3_harder_eval_000036
- request: 长沙 2026-06-02->2026-06-05 days=4 transport=自驾 hotel=亲子酒店 prefs=['亲子', '动物园', '海洋馆', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 3, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 3000, "reported_total_hotels": 1500, "diff": -1500, "covers_nights": false}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 120, "expected_total_attractions": 360, "reported_total_attractions": 360, "meal_per_person_cost_sum": 2160, "expected_total_meals": 6480, "reported_total_meals": 1620, "reported_total_transportation": 200}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": false, "attraction_budget_party_relation_ok": true, "meal_cost_scale_ok": true, "budget_relationship_ok": false, "expected_total_hotels": 3000, "reported_total_hotels": 1500, "expected_total_attractions": 360, "reported_total_attractions": 360, "meal_scale_eval": {"ok": true, "party_total": 3, "budget_level": "standard", "per_person_lunch_dinner_floor": 35, "per_person_breakfast_floor": 14, "meal_count": 12, "checked_count": 8, "failure_count": 0, "failures": []}}}]`

### v3_harder_eval_000008
- request: 大理 2026-05-07->2026-05-09 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物']
- errors: `[{"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-05-09", "type": "dinner", "name": "无", "reason": "empty_or_none"}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 2, "party_total": 3, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 4500, "reported_total_hotels": 2250, "diff": -2250, "covers_nights": false}}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 4185, "total": 4175, "diff": 10, "requested_budget": {"available": true, "amount": 5800, "scope": "total", "party_size": 3, "total": 5800, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "hard"}, "per_person_day": 463.89, "budget_level": "comfortable", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "hard", "amount": 5800, "target_min_ratio": 0.65, "target_max_ratio": 1.0, "target_min_total": 3800, "target_max_total": 5800, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 3, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 4500, "reported_total_hotels": 2250, "diff": -2250, "covers_nights": false}, "hotel_budget_covers_nights": false}}]`

### v3_harder_eval_000019
- request: 丽江 2026-05-07->2026-05-10 days=4 transport=打车 hotel=亲子酒店 prefs=['亲子', '老人友好', '博物馆', '城市公园', '特色餐厅']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "丽江古城", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-05-07", "day_index": 0, "name": "丽江古城"}, {"date": "2026-05-10", "day_index": 3, "name": "丽江古城"}]}]}, {"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-05-07", "type": "breakfast", "name": "丽江古城内的特色早餐", "reason": "unknown_food_semantics"}, {"date": "2026-05-08", "type": "breakfast", "name": "丽江古城内的特色早餐", "reason": "unknown_food_semantics"}, {"date": "2026-05-09", "type": "breakfast", "name": "丽江古城内的特色早餐", "reason": "unknown_food_semantics"}, {"date": "2026-05-10", "type": "breakfast", "name": "丽江古城内的特色早餐", "reason": "unknown_food_semantics"}]}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 2420, "total": 2400, "diff": 20, "requested_budget": {"available": true, "amount": 5300, "scope": "total", "party_size": 2, "total": 5300, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "soft"}, "per_person_day": 300.0, "budget_level": "comfortable", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "soft", "amount": 5300, "target_min_ratio": 0.65, "target_max_ratio": 1.05, "target_min_total": 3400, "target_max_total": 5600, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 2, "room_count": 1, "priced_nights": 3, "expected_min_total_hotels": 1500, "reported_total_hotels": 1500, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_harder_eval_000022
- request: 桂林 2026-04-03->2026-04-06 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '夜市', '老字号', '城市漫步']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 4, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 1200, "reported_total_hotels": 600, "diff": -600, "covers_nights": false}}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 2390, "total": 2400, "diff": -10, "requested_budget": {"available": true, "amount": 2400, "scope": "total", "party_size": 4, "total": 2400, "source": "budget_constraint", "budget_level": "limited", "strictness": "hard"}, "per_person_day": 150.0, "budget_level": "limited", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "limited", "strictness": "hard", "amount": 2400, "target_min_ratio": 0.72, "target_max_ratio": 1.0, "target_min_total": 1700, "target_max_total": 2400, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 4, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 1200, "reported_total_hotels": 600, "diff": -600, "covers_nights": false}, "hotel_budget_covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 525, "expected_total_attractions": 2100, "reported_total_attractions": 1110, "meal_per_person_cost_sum": 1724, "expected_total_meals": 6896, "reported_total_meals": 480, "reported_total_transportation": 200}}]`

### v3_harder_eval_000009
- request: 苏州 2026-04-26->2026-04-29 days=4 transport=打车 hotel=亲子酒店 prefs=['亲子', '老人友好', '博物馆', '城市公园', '特色餐厅']
- errors: `[{"stage": "rule", "type": "accommodation_type_mismatch", "details": [{"date": "2026-04-26", "day_index": 0, "expected": "亲子酒店", "got": "经济型酒店"}, {"date": "2026-04-27", "day_index": 1, "expected": "亲子酒店", "got": "经济型酒店"}, {"date": "2026-04-28", "day_index": 2, "expected": "亲子酒店", "got": "经济型酒店"}, {"date": "2026-04-29", "day_index": 3, "expected": "亲子酒店", "got": "经济型酒店"}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 4, "room_count": 2, "priced_nights": 4, "expected_min_total_hotels": 3200, "reported_total_hotels": 1200, "diff": -2000, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 90, "expected_total_attractions": 360, "reported_total_attractions": 240, "meal_per_person_cost_sum": 640, "expected_total_meals": 2560, "reported_total_meals": 360, "reported_total_transportation": 800}}]`

### v3_harder_eval_000024
- request: 济南 2026-05-06->2026-05-08 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆']
- errors: `[{"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-05-08", "type": "dinner", "name": "酒店晚餐", "reason": "generic_lodging_meal"}]}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 2282, "total": 1882, "diff": 400, "requested_budget": {"available": true, "amount": 1700, "scope": "total", "party_size": 1, "total": 1700, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "hard"}, "per_person_day": 627.33, "budget_level": "comfortable", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "hard", "amount": 1700, "target_min_ratio": 0.65, "target_max_ratio": 1.0, "target_min_total": 1100, "target_max_total": 1700, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": false, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 1, "room_count": 1, "priced_nights": 3, "expected_min_total_hotels": 1200, "reported_total_hotels": 1200, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 240, "expected_total_attractions": 240, "reported_total_attractions": 480, "meal_per_person_cost_sum": 513, "expected_total_meals": 513, "reported_total_meals": 402, "reported_total_transportation": 200}}]`

### v3_harder_eval_000034
- request: 武汉 2026-06-02->2026-06-04 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 2, "party_total": 1, "room_count": 1, "priced_nights": 2, "expected_min_total_hotels": 800, "reported_total_hotels": 1200, "diff": 400, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 130, "expected_total_attractions": 130, "reported_total_attractions": 207, "meal_per_person_cost_sum": 559, "expected_total_meals": 559, "reported_total_meals": 210, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 130, "expected_total_attractions": 130, "reported_total_attractions": 207, "meal_per_person_cost_sum": 559, "expected_total_meals": 559, "reported_total_meals": 210, "reported_total_transportation": 200}}]`

### v3_harder_eval_000032
- request: 丽江 2026-05-06->2026-05-09 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '夜市', '老字号', '城市漫步']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "丽江古城", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-05-06", "day_index": 0, "name": "丽江古城"}, {"date": "2026-05-09", "day_index": 3, "name": "丽江古城"}]}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 4, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 1200, "reported_total_hotels": 800, "diff": -400, "covers_nights": false}}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 2440, "total": 1640, "diff": 800, "requested_budget": {"available": true, "amount": 2400, "scope": "total", "party_size": 4, "total": 2400, "source": "budget_constraint", "budget_level": "limited", "strictness": "hard"}, "per_person_day": 102.5, "budget_level": "limited", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "limited", "strictness": "hard", "amount": 2400, "target_min_ratio": 0.72, "target_max_ratio": 1.0, "target_min_total": 1700, "target_max_total": 2400, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 4, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 1200, "reported_total_hotels": 800, "diff": -400, "covers_nights": false}, "hotel_budget_covers_nights": false}}]`

### v3_harder_eval_000031
- request: 成都 2026-05-07->2026-05-10 days=4 transport=打车 hotel=高端酒店 prefs=['高端酒店', '艺术', '特色餐厅', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-05-09", "lunch": "观锦餐厅(天府新谷店)", "dinner": "观锦餐厅(天廊店)"}]}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 5410, "total": 5300, "diff": 110, "requested_budget": {"available": true, "amount": 9600, "scope": "total", "party_size": 2, "total": 9600, "source": "budget_constraint", "budget_level": "premium", "strictness": "soft"}, "per_person_day": 662.5, "budget_level": "premium", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "premium", "strictness": "soft", "amount": 9600, "target_min_ratio": 0.7, "target_max_ratio": 1.12, "target_min_total": 6700, "target_max_total": 10800, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 2, "room_count": 1, "priced_nights": 4, "expected_min_total_hotels": 3200, "reported_total_hotels": 3200, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 115, "expected_total_attractions": 230, "reported_total_attractions": 210, "meal_per_person_cost_sum": 1926, "expected_total_meals": 3852, "reported_total_meals": 1200, "reported_total_transportation": 800}}]`

### v3_harder_eval_000004
- request: 张家界 2026-05-07->2026-05-09 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-05-07", "lunch": "索溪山寨·湘西民间土菜(标志门店)", "dinner": "索溪山寨·湘西民间土菜(标志门店)"}, {"date": "2026-05-08", "lunch": "业华湘·特色菜", "dinner": "业华湘·特色菜"}, {"date": "2026-05-09", "lunch": "自由人(张家界国光实验学校店)", "dinner": "自由人(张家界国光实验学校店)"}]}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 1820, "total": 1720, "diff": 100, "requested_budget": {"available": true, "amount": 1700, "scope": "total", "party_size": 1, "total": 1700, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "hard"}, "per_person_day": 573.33, "budget_level": "comfortable", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "hard", "amount": 1700, "target_min_ratio": 0.65, "target_max_ratio": 1.0, "target_min_total": 1100, "target_max_total": 1700, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": false, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 1, "room_count": 1, "priced_nights": 3, "expected_min_total_hotels": 1200, "reported_total_hotels": 1200, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 160, "expected_total_attractions": 160, "reported_total_attractions": 240, "meal_per_person_cost_sum": 314, "expected_total_meals": 314, "reported_total_meals": 180, "reported_total_transportation": 200}}]`

### v3_harder_eval_000026
- request: 扬州 2026-05-07->2026-05-10 days=4 transport=自驾 hotel=亲子酒店 prefs=['亲子', '动物园', '海洋馆', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "accommodation_type_mismatch", "details": [{"date": "2026-05-10", "day_index": 3, "expected": "亲子酒店", "got": "无住宿"}]}, {"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-05-07", "type": "lunch", "name": "扬州炒饭", "reason": "unknown_food_semantics"}, {"date": "2026-05-07", "type": "dinner", "name": "扬州炒面", "reason": "unknown_food_semantics"}, {"date": "2026-05-08", "type": "lunch", "name": "扬州炒饭", "reason": "unknown_food_semantics"}, {"date": "2026-05-08", "type": "dinner", "name": "扬州炒面", "reason": "unknown_food_semantics"}, {"date": "2026-05-09", "type": "lunch", "name": "扬州炒饭", "reason": "unknown_food_semantics"}, {"date": "2026-05-09", "type": "dinner", "name": "扬州炒面", "reason": "unknown_food_semantics"}, {"date": "2026-05-10", "type": "lunch", "name": "扬州炒饭", "reason": "unknown_food_semantics"}, {"date": "2026-05-10", "type": "dinner", "name": "扬州炒面", "reason": "unknown_food_semantics"}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 3, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 3000, "reported_total_hotels": 1500, "diff": -1500, "covers_nights": false}}]`

### v3_harder_eval_000013
- request: 武汉 2026-05-05->2026-05-09 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-05-05", "type": "dinner", "name": "江城人家", "reason": "unknown_food_semantics"}, {"date": "2026-05-06", "type": "lunch", "name": "江城人家", "reason": "unknown_food_semantics"}, {"date": "2026-05-07", "type": "lunch", "name": "江城人家", "reason": "unknown_food_semantics"}, {"date": "2026-05-08", "type": "lunch", "name": "江城人家", "reason": "unknown_food_semantics"}, {"date": "2026-05-09", "type": "lunch", "name": "江城人家", "reason": "unknown_food_semantics"}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 4, "party_total": 2, "room_count": 1, "priced_nights": 4, "expected_min_total_hotels": 1600, "reported_total_hotels": 2000, "diff": 400, "covers_nights": false}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 0, "expected_total_attractions": 0, "reported_total_attractions": 0, "meal_per_person_cost_sum": 800, "expected_total_meals": 1600, "reported_total_meals": 480, "reported_total_transportation": 200}}]`

### v3_harder_eval_000028
- request: 深圳 2026-03-04->2026-03-06 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 2, "party_total": 3, "room_count": 2, "priced_nights": 2, "expected_min_total_hotels": 3200, "reported_total_hotels": 2400, "diff": -800, "covers_nights": false}}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 7150, "total": 6150, "diff": 1000, "requested_budget": {"available": true, "amount": 4400, "scope": "total", "party_size": 3, "total": 4400, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "hard"}, "per_person_day": 683.33, "budget_level": "comfortable", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "hard", "amount": 4400, "target_min_ratio": 0.65, "target_max_ratio": 1.0, "target_min_total": 2900, "target_max_total": 4400, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": false, "user_constraint_ok": false, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 3, "room_count": 2, "priced_nights": 2, "expected_min_total_hotels": 3200, "reported_total_hotels": 2400, "diff": -800, "covers_nights": false}, "hotel_budget_covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 240, "expected_total_attractions": 720, "reported_total_attractions": 2620, "meal_per_person_cost_sum": 2202, "expected_total_meals": 6606, "reported_total_meals": 1530, "reported_total_transportation": 600}}]`

### v3_harder_eval_000020
- request: 杭州 2026-06-17->2026-06-21 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "accommodation_type_mismatch", "details": [{"date": "2026-06-21", "day_index": 4, "expected": "舒适型酒店", "got": "无住宿"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "友好饭店·新友记中餐厅", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-06-17", "type": "breakfast", "name": "友好饭店·新友记中餐厅"}, {"date": "2026-06-18", "type": "breakfast", "name": "友好饭店·新友记中餐厅"}, {"date": "2026-06-19", "type": "breakfast", "name": "友好饭店·新友记中餐厅"}, {"date": "2026-06-20", "type": "breakfast", "name": "友好饭店·新友记中餐厅"}]}, {"name_key": "友好饭店西湖旋转餐厅", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-06-17", "type": "lunch", "name": "友好饭店西湖旋转餐厅"}, {"date": "2026-06-18", "type": "lunch", "name": "友好饭店西湖旋转餐厅"}, {"date": "2026-06-19", "type": "lunch", "name": "友好饭店西湖旋转餐厅"}, {"date": "2026-06-20", "type": "lunch", "name": "友好饭店西湖旋转餐厅"}, {"date": "2026-06-21", "type": "lunch", "name": "友好饭店西湖旋转餐厅"}]}, {"name_key": "友好饭店·千霸冲绳料理", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-06-17", "type": "dinner", "name": "友好饭店·千霸冲绳料理"}, {"date": "2026-06-18", "type": "dinner", "name": "友好饭店·千霸冲绳料理"}, {"date": "2026-06-19", "type": "dinner", "name": "友好饭店·千霸冲绳料理"}, {"date": "2026-06-20", "type": "dinner", "name": "友好饭店·千霸冲绳料理"}, {"date": "2026-06-21", "type": "dinner", "name": "友好饭店·千霸冲绳料理"}]}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 4, "party_total": 5, "room_count": 3, "priced_nights": 4, "expected_min_total_hotels": 6000, "reported_total_hotels": 2500, "diff": -3500, "covers_nights": false}}]`

### v3_harder_eval_000007
- request: 成都 2026-05-07->2026-05-11 days=5 transport=公共交通 hotel=民宿 prefs=['小众展馆', '咖啡', '艺术', '城市漫步', '特色餐厅']
- errors: `[{"stage": "rule", "type": "meal_placeholder", "details": [{"date": "2026-05-08", "type": "dinner", "name": "M Stand(成都SKP店)"}, {"date": "2026-05-10", "type": "lunch", "name": "M Stand(成都SKP店)"}]}, {"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-05-08", "type": "dinner", "name": "M Stand(成都SKP店)", "reason": "unknown_food_semantics"}, {"date": "2026-05-10", "type": "lunch", "name": "M Stand(成都SKP店)", "reason": "unknown_food_semantics"}]}, {"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-05-09", "lunch": "星巴克(成都大魔方招商花园城店)", "dinner": "星巴克(成都环球中心II店)"}]}]`
