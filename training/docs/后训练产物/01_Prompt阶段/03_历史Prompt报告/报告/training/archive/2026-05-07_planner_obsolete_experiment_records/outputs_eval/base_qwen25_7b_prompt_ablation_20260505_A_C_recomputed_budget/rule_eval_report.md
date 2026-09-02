# Rule Eval Report: base_qwen25_7b_prompt_ablation_20260505_A_C_recomputed_budget

- records: 300
- generations: `training/outputs/eval/prompt_ablation_20260505/base_qwen25_7b_prompt_ablation_20260505_A_C/generations.jsonl`
- records_path: `training/data/v3/eval_harder_prompt_ablation_20260505/A_C/records.jsonl`

## Boolean Metrics

| Metric | Pass | Total | Rate |
| --- | ---: | ---: | ---: |
| accommodation_type_ok | 247 | 298 | 82.89% |
| attraction_budget_consistent | 37 | 298 | 12.42% |
| attraction_budget_party_relation_ok | 83 | 298 | 27.85% |
| attraction_count_ok | 298 | 298 | 100.00% |
| attraction_diversity_ok | 265 | 298 | 88.93% |
| attraction_grounding_ok | 296 | 298 | 99.33% |
| attraction_repeat_limit_ok | 265 | 298 | 88.93% |
| budget_arithmetic_consistent | 175 | 298 | 58.72% |
| budget_consistent | 175 | 298 | 58.72% |
| budget_level_aligned | 103 | 298 | 34.56% |
| budget_preference_aligned | 103 | 298 | 34.56% |
| budget_relationship_ok | 24 | 298 | 8.05% |
| budget_selection_ok | 72 | 298 | 24.16% |
| budget_user_constraint_ok | 245 | 298 | 82.21% |
| budget_within_user_budget | 288 | 298 | 96.64% |
| city_ok | 298 | 298 | 100.00% |
| date_range_ok | 298 | 298 | 100.00% |
| day_dates_ok | 298 | 298 | 100.00% |
| day_index_ok | 298 | 298 | 100.00% |
| days_len_ok | 298 | 298 | 100.00% |
| dpo_soft_pass | 18 | 298 | 6.04% |
| dpo_soft_recomputed_budget_pass | 15 | 298 | 5.03% |
| hard_pass | 145 | 298 | 48.66% |
| hotel_budget_covers_nights | 120 | 298 | 40.27% |
| hotel_budget_relation_ok | 132 | 298 | 44.30% |
| hotel_distance_placeholder_ok | 298 | 298 | 100.00% |
| hotel_grounding_ok | 294 | 298 | 98.66% |
| invalid_hotel_name_ok | 298 | 298 | 100.00% |
| json_extract_ok | 300 | 300 | 100.00% |
| legacy_hard_pass | 20 | 298 | 6.71% |
| location_object_ok | 298 | 298 | 100.00% |
| meal_budget_consistent | 1 | 298 | 0.34% |
| meal_complete | 298 | 298 | 100.00% |
| meal_cost_scale_ok | 199 | 298 | 66.78% |
| meal_diversity_ok | 197 | 298 | 66.11% |
| meal_grounding_ok | 157 | 298 | 52.68% |
| meal_lunch_dinner_same_day_ok | 246 | 298 | 82.55% |
| meal_repeat_limit_ok | 225 | 298 | 75.50% |
| meal_specific_ok | 286 | 298 | 95.97% |
| meal_valid_semantics_ok | 171 | 298 | 57.38% |
| middle_hotel_ok | 298 | 298 | 100.00% |
| recomputed_budget_fit_ok | 72 | 298 | 24.16% |
| recomputed_budget_hard_ok | 115 | 298 | 38.59% |
| recomputed_budget_level_aligned | 72 | 298 | 24.16% |
| recomputed_budget_preference_aligned | 72 | 298 | 24.16% |
| recomputed_budget_user_constraint_ok | 115 | 298 | 38.59% |
| recomputed_budget_within_user_budget | 153 | 298 | 51.34% |
| schema_ok | 298 | 300 | 99.33% |
| sft_budget_semantic_hard_pass | 10 | 298 | 3.36% |
| sft_hard_pass | 145 | 298 | 48.66% |
| sft_no_budget_sum_hard_pass | 145 | 298 | 48.66% |
| sft_strict_hard_pass | 0 | 298 | 0.00% |
| transportation_budget_nonnegative | 298 | 298 | 100.00% |
| weather_dates_ok | 298 | 298 | 100.00% |
| weather_match | 297 | 298 | 99.66% |

## Numeric Metrics

```json
{
  "attraction_diversity_unique_rate": {
    "avg": 0.9795,
    "p50": 1.0,
    "p90": 1.0
  },
  "attraction_grounding_rate": {
    "avg": 0.9985,
    "p50": 1.0,
    "p90": 1.0
  },
  "hotel_grounding_rate": {
    "avg": 0.9966,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_diversity_unique_rate": {
    "avg": 0.5152,
    "p50": 0.5,
    "p90": 1.0
  },
  "meal_food_pois_grounding_rate": {
    "avg": 0.8295,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_grounding_rate": {
    "avg": 0.8295,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_semantic_valid_rate": {
    "avg": 0.8963,
    "p50": 1.0,
    "p90": 1.0
  },
  "recomputed_budget_per_person_day": {
    "avg": 698.3832,
    "p50": 632.0,
    "p90": 1117.75
  },
  "recomputed_budget_total": {
    "avg": 7879.4597,
    "p50": 6680.0,
    "p90": 13244.0
  }
}
```

## Failure Types

```json
{
  "meal_budget_inconsistent": 298,
  "budget_relationship_mismatch": 274,
  "attraction_budget_inconsistent": 261,
  "budget_preference_mismatch": 195,
  "hotel_budget_underestimated": 178,
  "meal_invalid_name": 127,
  "budget_arithmetic_inconsistent": 123,
  "meal_cost_scale_too_low": 99,
  "meal_repeat_too_many": 73,
  "budget_hard_constraint_exceeded": 53,
  "meal_same_day_lunch_dinner_repeat": 52,
  "accommodation_type_mismatch": 51,
  "attraction_repeat_too_many": 33,
  "meal_grounding_miss": 14,
  "meal_placeholder": 12,
  "schema": 2,
  "weather_mismatch": 1
}
```

## Failure Examples

### v3_harder_eval_000018
- request: 天津 2026-07-02->2026-07-04 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "南楼煎饼", "count": 3, "max_allowed": 2, "occurrences": [{"date": "2026-07-02", "type": "breakfast", "name": "南楼煎饼(南楼总店)"}, {"date": "2026-07-03", "type": "breakfast", "name": "南楼煎饼(南楼总店)"}, {"date": "2026-07-04", "type": "breakfast", "name": "南楼煎饼(南楼总店)"}]}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 2, "party_total": 3, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 7200, "reported_total_hotels": 3600, "diff": -3600, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 210, "expected_total_attractions": 630, "reported_total_attractions": 210, "meal_per_person_cost_sum": 1602, "expected_total_meals": 4806, "reported_total_meals": 1080, "reported_total_transportation": 600}}]`

### v3_harder_eval_000034
- request: 武汉 2026-06-02->2026-06-04 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "吉庆78号私房菜", "count": 3, "max_allowed": 2, "occurrences": [{"date": "2026-06-02", "type": "dinner", "name": "吉庆78号私房菜(江汉路店)"}, {"date": "2026-06-03", "type": "lunch", "name": "吉庆78号私房菜(江汉路店)"}, {"date": "2026-06-04", "type": "lunch", "name": "吉庆78号私房菜(江汉路店)"}]}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 70, "expected_total_attractions": 70, "reported_total_attractions": 210, "meal_per_person_cost_sum": 578, "expected_total_meals": 578, "reported_total_meals": 234, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 70, "expected_total_attractions": 70, "reported_total_attractions": 210, "meal_per_person_cost_sum": 578, "expected_total_meals": 578, "reported_total_meals": 234, "reported_total_transportation": 200}}]`

### v3_harder_eval_000012
- request: 洛阳 2025-05-03->2025-05-06 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '夜市', '老字号', '城市漫步']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 4, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 1200, "reported_total_hotels": 600, "diff": -600, "covers_nights": false}}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 2000, "total": 1900, "diff": 100, "requested_budget": {"available": true, "amount": 3400, "scope": "total", "party_size": 4, "total": 3400, "source": "budget_constraint", "budget_level": "limited", "strictness": "hard"}, "per_person_day": 118.75, "budget_level": "limited", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "limited", "strictness": "hard", "amount": 3400, "target_min_ratio": 0.72, "target_max_ratio": 1.0, "target_min_total": 2400, "target_max_total": 3400, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 4, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 1200, "reported_total_hotels": 600, "diff": -600, "covers_nights": false}, "hotel_budget_covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 160, "expected_total_attractions": 640, "reported_total_attractions": 240, "meal_per_person_cost_sum": 1796, "expected_total_meals": 7184, "reported_total_meals": 960, "reported_total_transportation": 200}}]`

### v3_harder_eval_000022
- request: 桂林 2026-04-03->2026-04-06 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '夜市', '老字号', '城市漫步']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 4, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 1200, "reported_total_hotels": 800, "diff": -400, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 525, "expected_total_attractions": 2100, "reported_total_attractions": 1250, "meal_per_person_cost_sum": 1768, "expected_total_meals": 7072, "reported_total_meals": 480, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 525, "expected_total_attractions": 2100, "reported_total_attractions": 1250, "meal_per_person_cost_sum": 1768, "expected_total_meals": 7072, "reported_total_meals": 480, "reported_total_transportation": 200}}]`

### v3_harder_eval_000019
- request: 丽江 2026-05-07->2026-05-10 days=4 transport=打车 hotel=亲子酒店 prefs=['亲子', '老人友好', '博物馆', '城市公园', '特色餐厅']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "丽江古城", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-05-07", "day_index": 0, "name": "丽江古城"}, {"date": "2026-05-10", "day_index": 3, "name": "丽江古城"}]}]}, {"stage": "rule", "type": "accommodation_type_mismatch", "details": [{"date": "2026-05-10", "day_index": 3, "expected": "亲子酒店", "got": "无住宿"}]}, {"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-05-07", "type": "breakfast", "name": "丽江古城内的特色早餐", "reason": "unknown_food_semantics"}, {"date": "2026-05-08", "type": "breakfast", "name": "丽江古城内的特色早餐", "reason": "unknown_food_semantics"}, {"date": "2026-05-09", "type": "breakfast", "name": "丽江古城内的特色早餐", "reason": "unknown_food_semantics"}]}]`

### v3_harder_eval_000011
- request: 福州 2026-06-17->2026-06-20 days=4 transport=打车 hotel=高端酒店 prefs=['高端酒店', '艺术', '特色餐厅', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 0, "expected_total_attractions": 0, "reported_total_attractions": 0, "meal_per_person_cost_sum": 1710, "expected_total_meals": 3420, "reported_total_meals": 1200, "reported_total_transportation": 800}}, {"stage": "rule", "type": "budget_preference_mismatch", "details": {"part_sum": 5000, "total": 5000, "diff": 0, "requested_budget": {"available": true, "amount": 8800, "scope": "total", "party_size": 2, "total": 8800, "source": "budget_constraint", "budget_level": "premium", "strictness": "soft"}, "per_person_day": 625.0, "budget_level": "premium", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "premium", "strictness": "soft", "amount": 8800, "target_min_ratio": 0.7, "target_max_ratio": 1.12, "target_min_total": 6200, "target_max_total": 9900, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": true, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 2, "room_count": 1, "priced_nights": 4, "expected_min_total_hotels": 3000, "reported_total_hotels": 3000, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_harder_eval_000014
- request: 成都 2026-06-02->2026-06-04 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆']
- errors: `[{"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-06-04", "type": "dinner", "name": "酒店早餐", "reason": "hotel_or_lodging_name"}]}, {"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-06-02", "lunch": "观锦餐厅(天廊店)", "dinner": "观锦餐厅(天府新谷店)"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "观锦餐厅", "count": 3, "max_allowed": 2, "occurrences": [{"date": "2026-06-02", "type": "lunch", "name": "观锦餐厅(天廊店)"}, {"date": "2026-06-02", "type": "dinner", "name": "观锦餐厅(天府新谷店)"}, {"date": "2026-06-03", "type": "dinner", "name": "观锦餐厅(天府新谷店)"}]}]}]`

### v3_harder_eval_000032
- request: 丽江 2026-05-06->2026-05-09 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '夜市', '老字号', '城市漫步']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "丽江古城", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-05-06", "day_index": 0, "name": "丽江古城"}, {"date": "2026-05-09", "day_index": 3, "name": "丽江古城"}]}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 4, "room_count": 2, "priced_nights": 4, "expected_min_total_hotels": 1600, "reported_total_hotels": 800, "diff": -800, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 320, "expected_total_attractions": 1280, "reported_total_attractions": 960, "meal_per_person_cost_sum": 1648, "expected_total_meals": 6592, "reported_total_meals": 960, "reported_total_transportation": 200}}]`

### v3_harder_eval_000026
- request: 扬州 2026-05-07->2026-05-10 days=4 transport=自驾 hotel=亲子酒店 prefs=['亲子', '动物园', '海洋馆', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-05-07", "type": "lunch", "name": "扬州炒饭", "reason": "unknown_food_semantics"}, {"date": "2026-05-07", "type": "dinner", "name": "扬州炒面", "reason": "unknown_food_semantics"}, {"date": "2026-05-08", "type": "lunch", "name": "扬州炒饭", "reason": "unknown_food_semantics"}, {"date": "2026-05-08", "type": "dinner", "name": "扬州炒面", "reason": "unknown_food_semantics"}, {"date": "2026-05-09", "type": "lunch", "name": "扬州炒饭", "reason": "unknown_food_semantics"}, {"date": "2026-05-09", "type": "dinner", "name": "扬州炒面", "reason": "unknown_food_semantics"}, {"date": "2026-05-10", "type": "lunch", "name": "扬州炒饭", "reason": "unknown_food_semantics"}, {"date": "2026-05-10", "type": "dinner", "name": "扬州炒面", "reason": "unknown_food_semantics"}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 3, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 3000, "reported_total_hotels": 1500, "diff": -1500, "covers_nights": false}}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 2300, "total": 2400, "diff": -100, "requested_budget": {"available": true, "amount": 4300, "scope": "total", "party_size": 3, "total": 4300, "source": "budget_constraint", "budget_level": "standard", "strictness": "hard"}, "per_person_day": 200.0, "budget_level": "standard", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "standard", "strictness": "hard", "amount": 4300, "target_min_ratio": 0.55, "target_max_ratio": 1.0, "target_min_total": 2400, "target_max_total": 4300, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 3, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 3000, "reported_total_hotels": 1500, "diff": -1500, "covers_nights": false}, "hotel_budget_covers_nights": false}}]`

### v3_harder_eval_000008
- request: 大理 2026-05-07->2026-05-09 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物']
- errors: `[{"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-05-09", "type": "dinner", "name": "无", "reason": "empty_or_none"}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 2, "party_total": 3, "room_count": 2, "priced_nights": 2, "expected_min_total_hotels": 3000, "reported_total_hotels": 2250, "diff": -750, "covers_nights": false}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 75, "expected_total_attractions": 225, "reported_total_attractions": 225, "meal_per_person_cost_sum": 1275, "expected_total_meals": 3825, "reported_total_meals": 1350, "reported_total_transportation": 600}}]`

### v3_harder_eval_000031
- request: 成都 2026-05-07->2026-05-10 days=4 transport=打车 hotel=高端酒店 prefs=['高端酒店', '艺术', '特色餐厅', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-05-10", "type": "dinner", "name": "酒店早餐", "reason": "hotel_or_lodging_name"}]}, {"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-05-07", "lunch": "观锦餐厅(天府新谷店)", "dinner": "观锦餐厅(天廊店)"}, {"date": "2026-05-09", "lunch": "陶德砂锅(蜀汉店)", "dinner": "陶德砂锅(蜀汉店)"}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 195, "expected_total_attractions": 390, "reported_total_attractions": 295, "meal_per_person_cost_sum": 1722, "expected_total_meals": 3444, "reported_total_meals": 1440, "reported_total_transportation": 800}}]`

### v3_harder_eval_000028
- request: 深圳 2026-03-04->2026-03-06 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 2, "party_total": 3, "room_count": 2, "priced_nights": 2, "expected_min_total_hotels": 3200, "reported_total_hotels": 2400, "diff": -800, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 240, "expected_total_attractions": 720, "reported_total_attractions": 660, "meal_per_person_cost_sum": 2202, "expected_total_meals": 6606, "reported_total_meals": 810, "reported_total_transportation": 600}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 240, "expected_total_attractions": 720, "reported_total_attractions": 660, "meal_per_person_cost_sum": 2202, "expected_total_meals": 6606, "reported_total_meals": 810, "reported_total_transportation": 600}}]`

### v3_harder_eval_000004
- request: 张家界 2026-05-07->2026-05-09 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 2229, "total": 1729, "diff": 500, "requested_budget": {"available": true, "amount": 1700, "scope": "total", "party_size": 1, "total": 1700, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "hard"}, "per_person_day": 576.33, "budget_level": "comfortable", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "hard", "amount": 1700, "target_min_ratio": 0.65, "target_max_ratio": 1.0, "target_min_total": 1100, "target_max_total": 1700, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": false, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 1, "room_count": 1, "priced_nights": 3, "expected_min_total_hotels": 1200, "reported_total_hotels": 1200, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 80, "expected_total_attractions": 80, "reported_total_attractions": 240, "meal_per_person_cost_sum": 445, "expected_total_meals": 445, "reported_total_meals": 189, "reported_total_transportation": 600}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 80, "expected_total_attractions": 80, "reported_total_attractions": 240, "meal_per_person_cost_sum": 445, "expected_total_meals": 445, "reported_total_meals": 189, "reported_total_transportation": 600}}]`

### v3_harder_eval_000024
- request: 济南 2026-05-06->2026-05-08 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆']
- errors: `[{"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-05-08", "type": "dinner", "name": "酒店晚餐", "reason": "generic_lodging_meal"}]}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 2198, "total": 1798, "diff": 400, "requested_budget": {"available": true, "amount": 1700, "scope": "total", "party_size": 1, "total": 1700, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "hard"}, "per_person_day": 599.33, "budget_level": "comfortable", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "hard", "amount": 1700, "target_min_ratio": 0.65, "target_max_ratio": 1.0, "target_min_total": 1100, "target_max_total": 1700, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": false, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 1, "room_count": 1, "priced_nights": 3, "expected_min_total_hotels": 1200, "reported_total_hotels": 1200, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 240, "expected_total_attractions": 240, "reported_total_attractions": 480, "meal_per_person_cost_sum": 513, "expected_total_meals": 513, "reported_total_meals": 318, "reported_total_transportation": 200}}]`

### v3_harder_eval_000036
- request: 长沙 2026-06-02->2026-06-05 days=4 transport=自驾 hotel=亲子酒店 prefs=['亲子', '动物园', '海洋馆', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "accommodation_type_mismatch", "details": [{"date": "2026-06-05", "day_index": 3, "expected": "亲子酒店", "got": "无住宿"}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 3, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 3000, "reported_total_hotels": 1500, "diff": -1500, "covers_nights": false}}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 3600, "total": 3800, "diff": -200, "requested_budget": {"available": true, "amount": 5000, "scope": "total", "party_size": 3, "total": 5000, "source": "budget_constraint", "budget_level": "standard", "strictness": "hard"}, "per_person_day": 316.67, "budget_level": "standard", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "standard", "strictness": "hard", "amount": 5000, "target_min_ratio": 0.55, "target_max_ratio": 1.0, "target_min_total": 2800, "target_max_total": 5000, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 3, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 3000, "reported_total_hotels": 1500, "diff": -1500, "covers_nights": false}, "hotel_budget_covers_nights": false}}]`

### v3_harder_eval_000029
- request: 长沙 2026-03-04->2026-03-07 days=4 transport=打车 hotel=亲子酒店 prefs=['亲子', '老人友好', '博物馆', '城市公园', '特色餐厅']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "乐悠悠亲子乐园", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-03-04", "day_index": 0, "name": "乐悠悠亲子乐园"}, {"date": "2026-03-07", "day_index": 3, "name": "乐悠悠亲子乐园"}]}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "友好饼店", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-03-04", "type": "breakfast", "name": "友好饼店"}, {"date": "2026-03-05", "type": "breakfast", "name": "友好饼店"}, {"date": "2026-03-06", "type": "breakfast", "name": "友好饼店"}, {"date": "2026-03-07", "type": "breakfast", "name": "友好饼店"}]}, {"name_key": "长沙芙蓉国温德姆至尊豪廷大酒店", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-03-04", "type": "lunch", "name": "长沙芙蓉国温德姆至尊豪廷大酒店"}, {"date": "2026-03-05", "type": "lunch", "name": "长沙芙蓉国温德姆至尊豪廷大酒店"}, {"date": "2026-03-06", "type": "lunch", "name": "长沙芙蓉国温德姆至尊豪廷大酒店"}, {"date": "2026-03-07", "type": "lunch", "name": "长沙芙蓉国温德姆至尊豪廷大酒店"}]}, {"name_key": "友好友善茶饮巴士", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-03-04", "type": "dinner", "name": "友好友善茶饮巴士"}, {"date": "2026-03-05", "type": "dinner", "name": "友好友善茶饮巴士"}, {"date": "2026-03-06", "type": "dinner", "name": "友好友善茶饮巴士"}, {"date": "2026-03-07", "type": "dinner", "name": "友好友善茶饮巴士"}]}]}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 2817, "total": 3217, "diff": -400, "requested_budget": {"available": true, "amount": 6200, "scope": "total", "party_size": 2, "total": 6200, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "soft"}, "per_person_day": 402.12, "budget_level": "comfortable", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "soft", "amount": 6200, "target_min_ratio": 0.65, "target_max_ratio": 1.05, "target_min_total": 4000, "target_max_total": 6500, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 2, "room_count": 1, "priced_nights": 3, "expected_min_total_hotels": 1500, "reported_total_hotels": 1500, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_harder_eval_000002
- request: 杭州 2026-04-27->2026-04-30 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '夜市', '老字号', '城市漫步']
- errors: `[{"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-04-30", "type": "dinner", "name": "酒店晚餐", "reason": "generic_lodging_meal"}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 4, "room_count": 2, "priced_nights": 4, "expected_min_total_hotels": 2000, "reported_total_hotels": 1000, "diff": -1000, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 270, "expected_total_attractions": 1080, "reported_total_attractions": 260, "meal_per_person_cost_sum": 2504, "expected_total_meals": 10016, "reported_total_meals": 960, "reported_total_transportation": 200}}]`

### v3_harder_eval_000023
- request: 大理 2026-08-31->2026-09-04 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "大理古城", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-08-31", "day_index": 0, "name": "大理古城"}, {"date": "2026-09-04", "day_index": 4, "name": "大理古城"}]}]}, {"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-09-01", "type": "lunch", "name": "洱海公园附近餐厅", "reason": "non_food_poi_name"}, {"date": "2026-09-04", "type": "dinner", "name": "客栈晚餐", "reason": "generic_lodging_meal"}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 4, "party_total": 4, "room_count": 2, "priced_nights": 4, "expected_min_total_hotels": 3200, "reported_total_hotels": 1600, "diff": -1600, "covers_nights": false}}]`

### v3_harder_eval_000035
- request: 深圳 2026-08-31->2026-09-04 days=5 transport=公共交通 hotel=民宿 prefs=['摄影', '自然风光', '城市漫步', '本地菜']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "深圳湾公园", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-08-31", "day_index": 0, "name": "深圳湾公园"}, {"date": "2026-09-04", "day_index": 4, "name": "深圳湾公园"}]}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "欧记大排档•江西景德菜", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-08-31", "type": "breakfast", "name": "欧记大排档•江西景德菜(深圳首店)"}, {"date": "2026-09-01", "type": "breakfast", "name": "欧记大排档•江西景德菜(深圳首店)"}, {"date": "2026-09-02", "type": "breakfast", "name": "欧记大排档•江西景德菜(深圳首店)"}, {"date": "2026-09-03", "type": "breakfast", "name": "欧记大排档•江西景德菜(深圳首店)"}, {"date": "2026-09-04", "type": "breakfast", "name": "欧记大排档•江西景德菜(深圳首店)"}]}, {"name_key": "欧记大排档·江西景德菜", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-08-31", "type": "lunch", "name": "欧记大排档·江西景德菜(南山保利店)"}, {"date": "2026-09-01", "type": "lunch", "name": "欧记大排档·江西景德菜(南山保利店)"}, {"date": "2026-09-02", "type": "lunch", "name": "欧记大排档·江西景德菜(南山保利店)"}, {"date": "2026-09-03", "type": "lunch", "name": "欧记大排档·江西景德菜(南山保利店)"}, {"date": "2026-09-04", "type": "lunch", "name": "欧记大排档·江西景德菜(南山保利店)"}]}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 320, "expected_total_attractions": 320, "reported_total_attractions": 600, "meal_per_person_cost_sum": 1315, "expected_total_meals": 1315, "reported_total_meals": 405, "reported_total_transportation": 200}}]`

### v3_harder_eval_000038
- request: 厦门 2026-05-06->2026-05-08 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物']
- errors: `[{"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-05-07", "type": "breakfast", "name": "厦门原宿海景公寓早餐", "reason": "hotel_or_lodging_name"}, {"date": "2026-05-08", "type": "dinner", "name": "厦门屿海民宿晚餐", "reason": "generic_lodging_meal"}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 2, "party_total": 3, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 4800, "reported_total_hotels": 2400, "diff": -2400, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 100, "expected_total_attractions": 300, "reported_total_attractions": 230, "meal_per_person_cost_sum": 1572, "expected_total_meals": 4716, "reported_total_meals": 1440, "reported_total_transportation": 600}}]`
