# Rule Eval Report: base_qwen25_7b_prompt_ablation_20260505_B_D

- records: 300
- generations: `training/outputs/eval/prompt_ablation_20260505/base_qwen25_7b_prompt_ablation_20260505_B_D/generations.jsonl`
- records_path: `training/data/v3/eval_harder_prompt_ablation_20260505/B_D/records.jsonl`

## Boolean Metrics

| Metric | Pass | Total | Rate |
| --- | ---: | ---: | ---: |
| accommodation_type_ok | 229 | 298 | 76.85% |
| attraction_budget_consistent | 38 | 298 | 12.75% |
| attraction_budget_party_relation_ok | 87 | 298 | 29.19% |
| attraction_count_ok | 298 | 298 | 100.00% |
| attraction_diversity_ok | 247 | 298 | 82.89% |
| attraction_grounding_ok | 295 | 298 | 98.99% |
| attraction_repeat_limit_ok | 247 | 298 | 82.89% |
| budget_arithmetic_consistent | 144 | 298 | 48.32% |
| budget_consistent | 144 | 298 | 48.32% |
| budget_level_aligned | 111 | 298 | 37.25% |
| budget_preference_aligned | 111 | 298 | 37.25% |
| budget_relationship_ok | 26 | 298 | 8.72% |
| budget_user_constraint_ok | 246 | 298 | 82.55% |
| budget_within_user_budget | 279 | 298 | 93.62% |
| city_ok | 298 | 298 | 100.00% |
| date_range_ok | 298 | 298 | 100.00% |
| day_dates_ok | 298 | 298 | 100.00% |
| day_index_ok | 298 | 298 | 100.00% |
| days_len_ok | 298 | 298 | 100.00% |
| dpo_soft_pass | 0 | 298 | 0.00% |
| hard_pass | 0 | 298 | 0.00% |
| hotel_budget_covers_nights | 113 | 298 | 37.92% |
| hotel_budget_relation_ok | 123 | 298 | 41.28% |
| hotel_distance_placeholder_ok | 298 | 298 | 100.00% |
| hotel_grounding_ok | 298 | 298 | 100.00% |
| invalid_hotel_name_ok | 298 | 298 | 100.00% |
| json_extract_ok | 299 | 300 | 99.67% |
| legacy_hard_pass | 23 | 298 | 7.72% |
| location_object_ok | 298 | 298 | 100.00% |
| meal_budget_consistent | 0 | 298 | 0.00% |
| meal_complete | 297 | 298 | 99.66% |
| meal_cost_scale_ok | 196 | 298 | 65.77% |
| meal_diversity_ok | 223 | 298 | 74.83% |
| meal_grounding_ok | 175 | 298 | 58.72% |
| meal_lunch_dinner_same_day_ok | 252 | 298 | 84.56% |
| meal_repeat_limit_ok | 247 | 298 | 82.89% |
| meal_specific_ok | 286 | 298 | 95.97% |
| meal_valid_semantics_ok | 194 | 298 | 65.10% |
| middle_hotel_ok | 298 | 298 | 100.00% |
| schema_ok | 298 | 300 | 99.33% |
| sft_budget_semantic_hard_pass | 10 | 298 | 3.36% |
| sft_hard_pass | 0 | 298 | 0.00% |
| transportation_budget_nonnegative | 298 | 298 | 100.00% |
| weather_dates_ok | 298 | 298 | 100.00% |
| weather_match | 298 | 298 | 100.00% |

## Numeric Metrics

```json
{
  "attraction_diversity_unique_rate": {
    "avg": 0.9667,
    "p50": 1.0,
    "p90": 1.0
  },
  "attraction_grounding_rate": {
    "avg": 0.9984,
    "p50": 1.0,
    "p90": 1.0
  },
  "hotel_grounding_rate": {
    "avg": 1.0,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_diversity_unique_rate": {
    "avg": 0.5544,
    "p50": 0.5,
    "p90": 1.0
  },
  "meal_food_pois_grounding_rate": {
    "avg": 0.8399,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_grounding_rate": {
    "avg": 0.8399,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_semantic_valid_rate": {
    "avg": 0.9069,
    "p50": 1.0,
    "p90": 1.0
  }
}
```

## Failure Types

```json
{
  "meal_budget_inconsistent": 298,
  "budget_relationship_mismatch": 272,
  "attraction_budget_inconsistent": 260,
  "budget_preference_mismatch": 187,
  "hotel_budget_underestimated": 185,
  "budget_arithmetic_inconsistent": 154,
  "meal_invalid_name": 104,
  "meal_cost_scale_too_low": 102,
  "accommodation_type_mismatch": 69,
  "budget_hard_constraint_exceeded": 52,
  "meal_repeat_too_many": 51,
  "attraction_repeat_too_many": 51,
  "meal_same_day_lunch_dinner_repeat": 46,
  "meal_grounding_miss": 19,
  "meal_placeholder": 12,
  "schema": 1,
  "json_extract": 1
}
```

## Failure Examples

### v3_harder_eval_000004
- request: 张家界 2026-05-07->2026-05-09 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 2, "party_total": 1, "room_count": 1, "priced_nights": 2, "expected_min_total_hotels": 800, "reported_total_hotels": 1200, "diff": 400, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 80, "expected_total_attractions": 80, "reported_total_attractions": 240, "meal_per_person_cost_sum": 418, "expected_total_meals": 418, "reported_total_meals": 240, "reported_total_transportation": 600}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 80, "expected_total_attractions": 80, "reported_total_attractions": 240, "meal_per_person_cost_sum": 418, "expected_total_meals": 418, "reported_total_meals": 240, "reported_total_transportation": 600}}]`

### v3_harder_eval_000014
- request: 成都 2026-06-02->2026-06-04 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-06-04", "lunch": "观锦餐厅(天府新谷店)", "dinner": "观锦餐厅(天廊店)"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "观锦餐厅", "count": 3, "max_allowed": 2, "occurrences": [{"date": "2026-06-02", "type": "lunch", "name": "观锦餐厅(天廊店)"}, {"date": "2026-06-04", "type": "lunch", "name": "观锦餐厅(天府新谷店)"}, {"date": "2026-06-04", "type": "dinner", "name": "观锦餐厅(天廊店)"}]}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 2, "party_total": 1, "room_count": 1, "priced_nights": 2, "expected_min_total_hotels": 900, "reported_total_hotels": 1350, "diff": 450, "covers_nights": false}}]`

### v3_harder_eval_000024
- request: 济南 2026-05-06->2026-05-08 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆']
- errors: `[{"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-05-08", "type": "dinner", "name": "酒店晚餐", "reason": "generic_lodging_meal"}]}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 2628, "total": 2428, "diff": 200, "requested_budget": {"available": true, "amount": 1700, "scope": "total", "party_size": 1, "total": 1700, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "hard"}, "per_person_day": 809.33, "budget_level": "comfortable", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "hard", "amount": 1700, "target_min_ratio": 0.65, "target_max_ratio": 1.0, "target_min_total": 1100, "target_max_total": 1700, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": false, "user_constraint_ok": false, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 1, "room_count": 1, "priced_nights": 3, "expected_min_total_hotels": 1200, "reported_total_hotels": 1200, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 240, "expected_total_attractions": 240, "reported_total_attractions": 480, "meal_per_person_cost_sum": 513, "expected_total_meals": 513, "reported_total_meals": 348, "reported_total_transportation": 600}}]`

### v3_harder_eval_000008
- request: 大理 2026-05-07->2026-05-09 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-05-09", "lunch": "陈氏海稍鱼(开发区店)", "dinner": "陈氏海稍鱼(开发区店)"}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 2, "party_total": 3, "room_count": 2, "priced_nights": 2, "expected_min_total_hotels": 3000, "reported_total_hotels": 2250, "diff": -750, "covers_nights": false}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 75, "expected_total_attractions": 225, "reported_total_attractions": 225, "meal_per_person_cost_sum": 1335, "expected_total_meals": 4005, "reported_total_meals": 1080, "reported_total_transportation": 600}}]`

### v3_harder_eval_000029
- request: 长沙 2026-03-04->2026-03-07 days=4 transport=打车 hotel=亲子酒店 prefs=['亲子', '老人友好', '博物馆', '城市公园', '特色餐厅']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "乐悠悠亲子乐园", "count": 3, "max_allowed": 1, "occurrences": [{"date": "2026-03-05", "day_index": 1, "name": "乐悠悠亲子乐园"}, {"date": "2026-03-06", "day_index": 2, "name": "乐悠悠亲子乐园"}, {"date": "2026-03-07", "day_index": 3, "name": "乐悠悠亲子乐园"}]}]}, {"stage": "rule", "type": "accommodation_type_mismatch", "details": [{"date": "2026-03-07", "day_index": 3, "expected": "亲子酒店", "got": "无"}]}, {"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-03-07", "lunch": "友好饼店", "dinner": "友好饼店"}]}]`

### v3_harder_eval_000028
- request: 深圳 2026-03-04->2026-03-06 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 2, "party_total": 3, "room_count": 2, "priced_nights": 2, "expected_min_total_hotels": 3200, "reported_total_hotels": 1600, "diff": -1600, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 240, "expected_total_attractions": 720, "reported_total_attractions": 260, "meal_per_person_cost_sum": 1893, "expected_total_meals": 5679, "reported_total_meals": 780, "reported_total_transportation": 600}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 240, "expected_total_attractions": 720, "reported_total_attractions": 260, "meal_per_person_cost_sum": 1893, "expected_total_meals": 5679, "reported_total_meals": 780, "reported_total_transportation": 600}}]`

### v3_harder_eval_000038
- request: 厦门 2026-05-06->2026-05-08 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 2, "party_total": 3, "room_count": 2, "priced_nights": 2, "expected_min_total_hotels": 3200, "reported_total_hotels": 2400, "diff": -800, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 100, "expected_total_attractions": 300, "reported_total_attractions": 240, "meal_per_person_cost_sum": 1512, "expected_total_meals": 4536, "reported_total_meals": 1290, "reported_total_transportation": 600}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 100, "expected_total_attractions": 300, "reported_total_attractions": 240, "meal_per_person_cost_sum": 1512, "expected_total_meals": 4536, "reported_total_meals": 1290, "reported_total_transportation": 600}}]`

### v3_harder_eval_000018
- request: 天津 2026-07-02->2026-07-04 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-07-04", "lunch": "海底捞火锅(万象城店)", "dinner": "海底捞火锅(万象城店)"}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 2, "party_total": 3, "room_count": 2, "priced_nights": 2, "expected_min_total_hotels": 4800, "reported_total_hotels": 2400, "diff": -2400, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 130, "expected_total_attractions": 390, "reported_total_attractions": 210, "meal_per_person_cost_sum": 1416, "expected_total_meals": 4248, "reported_total_meals": 1080, "reported_total_transportation": 600}}]`

### v3_harder_eval_000034
- request: 武汉 2026-06-02->2026-06-04 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 2, "party_total": 1, "room_count": 1, "priced_nights": 2, "expected_min_total_hotels": 800, "reported_total_hotels": 1200, "diff": 400, "covers_nights": false}}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 2250, "total": 2050, "diff": 200, "requested_budget": {"available": true, "amount": 1800, "scope": "total", "party_size": 1, "total": 1800, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "hard"}, "per_person_day": 683.33, "budget_level": "comfortable", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "hard", "amount": 1800, "target_min_ratio": 0.65, "target_max_ratio": 1.0, "target_min_total": 1200, "target_max_total": 1800, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": false, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 1, "room_count": 1, "priced_nights": 2, "expected_min_total_hotels": 800, "reported_total_hotels": 1200, "diff": 400, "covers_nights": false}, "hotel_budget_covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 70, "expected_total_attractions": 70, "reported_total_attractions": 210, "meal_per_person_cost_sum": 582, "expected_total_meals": 582, "reported_total_meals": 240, "reported_total_transportation": 600}}]`

### v3_harder_eval_000022
- request: 桂林 2026-04-03->2026-04-06 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '夜市', '老字号', '城市漫步']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 4, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 1200, "reported_total_hotels": 600, "diff": -600, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 525, "expected_total_attractions": 2100, "reported_total_attractions": 1100, "meal_per_person_cost_sum": 1888, "expected_total_meals": 7552, "reported_total_meals": 480, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 525, "expected_total_attractions": 2100, "reported_total_attractions": 1100, "meal_per_person_cost_sum": 1888, "expected_total_meals": 7552, "reported_total_meals": 480, "reported_total_transportation": 200}}]`

### v3_harder_eval_000019
- request: 丽江 2026-05-07->2026-05-10 days=4 transport=打车 hotel=亲子酒店 prefs=['亲子', '老人友好', '博物馆', '城市公园', '特色餐厅']
- errors: `[{"stage": "rule", "type": "meal_grounding_miss", "details": [{"date": "2026-05-07", "type": "lunch", "name": "丽江古城小吃"}, {"date": "2026-05-07", "type": "dinner", "name": "丽江古城餐厅"}, {"date": "2026-05-08", "type": "lunch", "name": "丽江古城小吃"}, {"date": "2026-05-08", "type": "dinner", "name": "丽江古城餐厅"}, {"date": "2026-05-09", "type": "lunch", "name": "丽江古城小吃"}, {"date": "2026-05-09", "type": "dinner", "name": "丽江古城餐厅"}, {"date": "2026-05-10", "type": "lunch", "name": "丽江古城小吃"}, {"date": "2026-05-10", "type": "dinner", "name": "丽江古城餐厅"}]}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 3020, "total": 3380, "diff": -360, "requested_budget": {"available": true, "amount": 5300, "scope": "total", "party_size": 2, "total": 5300, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "soft"}, "per_person_day": 422.5, "budget_level": "comfortable", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "soft", "amount": 5300, "target_min_ratio": 0.65, "target_max_ratio": 1.05, "target_min_total": 3400, "target_max_total": 5600, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 2, "room_count": 1, "priced_nights": 3, "expected_min_total_hotels": 1500, "reported_total_hotels": 1500, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 400, "expected_total_attractions": 800, "reported_total_attractions": 240, "meal_per_person_cost_sum": 640, "expected_total_meals": 1280, "reported_total_meals": 480, "reported_total_transportation": 800}}]`

### v3_harder_eval_000000
- request: 昆明 2026-04-03->2026-04-07 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-04-03", "type": "lunch", "name": "小人国主题公园", "reason": "non_food_poi_name"}, {"date": "2026-04-03", "type": "dinner", "name": "昆明捞渔河湿地公园", "reason": "non_food_poi_name"}, {"date": "2026-04-04", "type": "lunch", "name": "国立西南联合大学旧址", "reason": "unknown_food_semantics"}, {"date": "2026-04-04", "type": "dinner", "name": "昆明融创滇池后海", "reason": "unknown_food_semantics"}, {"date": "2026-04-05", "type": "lunch", "name": "云南美术馆(五一路)", "reason": "non_food_poi_name"}, {"date": "2026-04-05", "type": "dinner", "name": "昆明瀑布公园", "reason": "non_food_poi_name"}, {"date": "2026-04-06", "type": "lunch", "name": "云南民族博物馆", "reason": "non_food_poi_name"}, {"date": "2026-04-06", "type": "dinner", "name": "昆明海晏村网红沙滩", "reason": "unknown_food_semantics"}, {"date": "2026-04-07", "type": "lunch", "name": "欢乐+倍亲子乐园", "reason": "unknown_food_semantics"}, {"date": "2026-04-07", "type": "dinner", "name": "酒店晚餐", "reason": "generic_lodging_meal"}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 4, "party_total": 5, "room_count": 3, "priced_nights": 4, "expected_min_total_hotels": 4800, "reported_total_hotels": 2000, "diff": -2800, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 5, "hotel_room_count": 3, "attraction_ticket_sum": 353, "expected_total_attractions": 1765, "reported_total_attractions": 513, "meal_per_person_cost_sum": 523, "expected_total_meals": 2615, "reported_total_meals": 600, "reported_total_transportation": 1000}}]`

### v3_harder_eval_000032
- request: 丽江 2026-05-06->2026-05-09 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '夜市', '老字号', '城市漫步']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 4, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 1200, "reported_total_hotels": 600, "diff": -600, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 320, "expected_total_attractions": 1280, "reported_total_attractions": 960, "meal_per_person_cost_sum": 413, "expected_total_meals": 1652, "reported_total_meals": 480, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 320, "expected_total_attractions": 1280, "reported_total_attractions": 960, "meal_per_person_cost_sum": 413, "expected_total_meals": 1652, "reported_total_meals": 480, "reported_total_transportation": 200}}]`

### v3_harder_eval_000026
- request: 扬州 2026-05-07->2026-05-10 days=4 transport=自驾 hotel=亲子酒店 prefs=['亲子', '动物园', '海洋馆', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "accommodation_type_mismatch", "details": [{"date": "2026-05-10", "day_index": 3, "expected": "亲子酒店", "got": "无"}]}, {"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-05-07", "type": "lunch", "name": "扬州炒饭", "reason": "unknown_food_semantics"}, {"date": "2026-05-07", "type": "dinner", "name": "扬州炒面", "reason": "unknown_food_semantics"}, {"date": "2026-05-08", "type": "lunch", "name": "扬州炒面", "reason": "unknown_food_semantics"}, {"date": "2026-05-08", "type": "dinner", "name": "扬州炒饭", "reason": "unknown_food_semantics"}, {"date": "2026-05-09", "type": "lunch", "name": "扬州炒面", "reason": "unknown_food_semantics"}, {"date": "2026-05-09", "type": "dinner", "name": "扬州炒饭", "reason": "unknown_food_semantics"}, {"date": "2026-05-10", "type": "lunch", "name": "扬州炒面", "reason": "unknown_food_semantics"}, {"date": "2026-05-10", "type": "dinner", "name": "扬州炒饭", "reason": "unknown_food_semantics"}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 3, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 3000, "reported_total_hotels": 1500, "diff": -1500, "covers_nights": false}}]`

### v3_harder_eval_000011
- request: 福州 2026-06-17->2026-06-20 days=4 transport=打车 hotel=高端酒店 prefs=['高端酒店', '艺术', '特色餐厅', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 0, "expected_total_attractions": 0, "reported_total_attractions": 0, "meal_per_person_cost_sum": 975, "expected_total_meals": 1950, "reported_total_meals": 720, "reported_total_transportation": 800}}, {"stage": "rule", "type": "budget_preference_mismatch", "details": {"part_sum": 4520, "total": 4520, "diff": 0, "requested_budget": {"available": true, "amount": 8800, "scope": "total", "party_size": 2, "total": 8800, "source": "budget_constraint", "budget_level": "premium", "strictness": "soft"}, "per_person_day": 565.0, "budget_level": "premium", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "premium", "strictness": "soft", "amount": 8800, "target_min_ratio": 0.7, "target_max_ratio": 1.12, "target_min_total": 6200, "target_max_total": 9900, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": true, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 2, "room_count": 1, "priced_nights": 4, "expected_min_total_hotels": 3000, "reported_total_hotels": 3000, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_harder_eval_000016
- request: 苏州 2026-06-02->2026-06-05 days=4 transport=自驾 hotel=亲子酒店 prefs=['亲子', '动物园', '海洋馆', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "accommodation_type_mismatch", "details": [{"date": "2026-06-05", "day_index": 3, "expected": "亲子酒店", "got": "无"}]}, {"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-06-02", "type": "dinner", "name": "松鹤楼", "reason": "unknown_food_semantics"}, {"date": "2026-06-03", "type": "lunch", "name": "松鹤楼", "reason": "unknown_food_semantics"}, {"date": "2026-06-03", "type": "dinner", "name": "松鹤楼", "reason": "unknown_food_semantics"}, {"date": "2026-06-04", "type": "lunch", "name": "松鹤楼", "reason": "unknown_food_semantics"}, {"date": "2026-06-04", "type": "dinner", "name": "松鹤楼", "reason": "unknown_food_semantics"}, {"date": "2026-06-05", "type": "lunch", "name": "松鹤楼", "reason": "unknown_food_semantics"}, {"date": "2026-06-05", "type": "dinner", "name": "松鹤楼", "reason": "unknown_food_semantics"}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 3, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 7500, "reported_total_hotels": 3750, "diff": -3750, "covers_nights": false}}]`

### v3_harder_eval_000035
- request: 深圳 2026-08-31->2026-09-04 days=5 transport=公共交通 hotel=民宿 prefs=['摄影', '自然风光', '城市漫步', '本地菜']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-09-02", "lunch": "欧记大排档·江西景德菜(罗湖东门町店)", "dinner": "欧记大排档·江西景德菜(南山保利店)"}, {"date": "2026-09-04", "lunch": "香港新发烧腊茶餐厅(凤凰路店)", "dinner": "香港新发烧腊茶餐厅(书城店)"}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 320, "expected_total_attractions": 320, "reported_total_attractions": 600, "meal_per_person_cost_sum": 998, "expected_total_meals": 998, "reported_total_meals": 480, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 320, "expected_total_attractions": 320, "reported_total_attractions": 600, "meal_per_person_cost_sum": 998, "expected_total_meals": 998, "reported_total_meals": 480, "reported_total_transportation": 200}}]`

### v3_harder_eval_000031
- request: 成都 2026-05-07->2026-05-10 days=4 transport=打车 hotel=高端酒店 prefs=['高端酒店', '艺术', '特色餐厅', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 195, "expected_total_attractions": 390, "reported_total_attractions": 295, "meal_per_person_cost_sum": 1120, "expected_total_meals": 2240, "reported_total_meals": 780, "reported_total_transportation": 800}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 195, "expected_total_attractions": 390, "reported_total_attractions": 295, "meal_per_person_cost_sum": 1120, "expected_total_meals": 2240, "reported_total_meals": 780, "reported_total_transportation": 800}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": false, "meal_cost_scale_ok": false, "budget_relationship_ok": false, "expected_total_hotels": 2400, "reported_total_hotels": 2400, "expected_total_attractions": 390, "reported_total_attractions": 295, "meal_scale_eval": {"ok": false, "party_total": 2, "budget_level": "premium", "per_person_lunch_dinner_floor": 70, "per_person_breakfast_floor": 28, "meal_count": 12, "checked_count": 8, "failure_count": 1, "failures": [{"date": "2026-05-08", "type": "dinner", "name": "陶德砂锅(蜀汉店)", "estimated_cost": 69, "min_expected_cost": 70}]}}}]`

### v3_harder_eval_000007
- request: 成都 2026-05-07->2026-05-11 days=5 transport=公共交通 hotel=民宿 prefs=['小众展馆', '咖啡', '艺术', '城市漫步', '特色餐厅']
- errors: `[{"stage": "rule", "type": "accommodation_type_mismatch", "details": [{"date": "2026-05-11", "day_index": 4, "expected": "民宿", "got": "无"}]}, {"stage": "rule", "type": "meal_placeholder", "details": [{"date": "2026-05-08", "type": "lunch", "name": "M Stand(成都SKP店)"}, {"date": "2026-05-11", "type": "lunch", "name": "M Stand(成都SKP店)"}]}, {"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-05-08", "type": "lunch", "name": "M Stand(成都SKP店)", "reason": "unknown_food_semantics"}, {"date": "2026-05-11", "type": "lunch", "name": "M Stand(成都SKP店)", "reason": "unknown_food_semantics"}]}]`

### v3_harder_eval_000006
- request: 南京 2026-07-02->2026-07-05 days=4 transport=自驾 hotel=亲子酒店 prefs=['亲子', '动物园', '海洋馆', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "accommodation_type_mismatch", "details": [{"date": "2026-07-05", "day_index": 3, "expected": "亲子酒店", "got": "无"}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 3, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 3300, "reported_total_hotels": 1650, "diff": -1650, "covers_nights": false}}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 3000, "total": 3990, "diff": -990, "requested_budget": {"available": true, "amount": 4000, "scope": "total", "party_size": 3, "total": 4000, "source": "budget_constraint", "budget_level": "standard", "strictness": "hard"}, "per_person_day": 332.5, "budget_level": "standard", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "standard", "strictness": "hard", "amount": 4000, "target_min_ratio": 0.55, "target_max_ratio": 1.0, "target_min_total": 2200, "target_max_total": 4000, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 3, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 3300, "reported_total_hotels": 1650, "diff": -1650, "covers_nights": false}, "hotel_budget_covers_nights": false}}]`
