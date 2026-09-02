# Rule Eval Report: base_qwen25_7b_prompt_ablation_20260505_D

- records: 300
- generations: `training/outputs/eval/prompt_ablation_20260505/base_qwen25_7b_prompt_ablation_20260505_D/generations.jsonl`
- records_path: `training/data/v3/eval_harder_prompt_ablation_20260505/D/records.jsonl`

## Boolean Metrics

| Metric | Pass | Total | Rate |
| --- | ---: | ---: | ---: |
| accommodation_type_ok | 248 | 296 | 83.78% |
| attraction_budget_consistent | 35 | 296 | 11.82% |
| attraction_budget_party_relation_ok | 84 | 296 | 28.38% |
| attraction_count_ok | 295 | 296 | 99.66% |
| attraction_diversity_ok | 256 | 296 | 86.49% |
| attraction_grounding_ok | 293 | 296 | 98.99% |
| attraction_repeat_limit_ok | 256 | 296 | 86.49% |
| budget_arithmetic_consistent | 147 | 296 | 49.66% |
| budget_consistent | 147 | 296 | 49.66% |
| budget_level_aligned | 114 | 296 | 38.51% |
| budget_preference_aligned | 114 | 296 | 38.51% |
| budget_relationship_ok | 18 | 296 | 6.08% |
| budget_user_constraint_ok | 235 | 296 | 79.39% |
| budget_within_user_budget | 277 | 296 | 93.58% |
| city_ok | 296 | 296 | 100.00% |
| date_range_ok | 296 | 296 | 100.00% |
| day_dates_ok | 296 | 296 | 100.00% |
| day_index_ok | 296 | 296 | 100.00% |
| days_len_ok | 296 | 296 | 100.00% |
| dpo_soft_pass | 0 | 296 | 0.00% |
| hard_pass | 0 | 296 | 0.00% |
| hotel_budget_covers_nights | 108 | 296 | 36.49% |
| hotel_budget_relation_ok | 119 | 296 | 40.20% |
| hotel_distance_placeholder_ok | 296 | 296 | 100.00% |
| hotel_grounding_ok | 295 | 296 | 99.66% |
| invalid_hotel_name_ok | 296 | 296 | 100.00% |
| json_extract_ok | 298 | 300 | 99.33% |
| legacy_hard_pass | 16 | 296 | 5.41% |
| location_object_ok | 296 | 296 | 100.00% |
| meal_budget_consistent | 0 | 296 | 0.00% |
| meal_complete | 296 | 296 | 100.00% |
| meal_cost_scale_ok | 195 | 296 | 65.88% |
| meal_diversity_ok | 218 | 296 | 73.65% |
| meal_grounding_ok | 172 | 296 | 58.11% |
| meal_lunch_dinner_same_day_ok | 237 | 296 | 80.07% |
| meal_repeat_limit_ok | 252 | 296 | 85.14% |
| meal_specific_ok | 285 | 296 | 96.28% |
| meal_valid_semantics_ok | 193 | 296 | 65.20% |
| middle_hotel_ok | 296 | 296 | 100.00% |
| schema_ok | 296 | 300 | 98.67% |
| sft_budget_semantic_hard_pass | 4 | 296 | 1.35% |
| sft_hard_pass | 0 | 296 | 0.00% |
| transportation_budget_nonnegative | 296 | 296 | 100.00% |
| weather_dates_ok | 296 | 296 | 100.00% |
| weather_match | 296 | 296 | 100.00% |

## Numeric Metrics

```json
{
  "attraction_diversity_unique_rate": {
    "avg": 0.9759,
    "p50": 1.0,
    "p90": 1.0
  },
  "attraction_grounding_rate": {
    "avg": 0.9983,
    "p50": 1.0,
    "p90": 1.0
  },
  "hotel_grounding_rate": {
    "avg": 0.9992,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_diversity_unique_rate": {
    "avg": 0.5534,
    "p50": 0.5,
    "p90": 1.0
  },
  "meal_food_pois_grounding_rate": {
    "avg": 0.8409,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_grounding_rate": {
    "avg": 0.8409,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_semantic_valid_rate": {
    "avg": 0.9081,
    "p50": 1.0,
    "p90": 1.0
  }
}
```

## Failure Types

```json
{
  "meal_budget_inconsistent": 296,
  "budget_relationship_mismatch": 278,
  "attraction_budget_inconsistent": 261,
  "hotel_budget_underestimated": 188,
  "budget_preference_mismatch": 182,
  "budget_arithmetic_inconsistent": 149,
  "meal_invalid_name": 103,
  "meal_cost_scale_too_low": 101,
  "budget_hard_constraint_exceeded": 61,
  "meal_same_day_lunch_dinner_repeat": 59,
  "accommodation_type_mismatch": 48,
  "meal_repeat_too_many": 44,
  "attraction_repeat_too_many": 40,
  "meal_grounding_miss": 21,
  "meal_placeholder": 11,
  "json_extract": 2,
  "schema": 2
}
```

## Failure Examples

### v3_harder_eval_000019
- request: 丽江 2026-05-07->2026-05-10 days=4 transport=打车 hotel=亲子酒店 prefs=['亲子', '老人友好', '博物馆', '城市公园', '特色餐厅']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "丽江古城", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-05-07", "day_index": 0, "name": "丽江古城"}, {"date": "2026-05-10", "day_index": 3, "name": "丽江古城"}]}]}, {"stage": "rule", "type": "meal_grounding_miss", "details": [{"date": "2026-05-07", "type": "lunch", "name": "丽江古城小吃"}, {"date": "2026-05-07", "type": "dinner", "name": "丽江古城特色餐厅"}, {"date": "2026-05-08", "type": "lunch", "name": "丽江古城小吃"}, {"date": "2026-05-08", "type": "dinner", "name": "丽江古城特色餐厅"}, {"date": "2026-05-09", "type": "lunch", "name": "丽江古城小吃"}, {"date": "2026-05-09", "type": "dinner", "name": "丽江古城特色餐厅"}, {"date": "2026-05-10", "type": "lunch", "name": "丽江古城小吃"}, {"date": "2026-05-10", "type": "dinner", "name": "丽江古城特色餐厅"}]}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 3020, "total": 3380, "diff": -360, "requested_budget": {"available": true, "amount": 5300, "scope": "total", "party_size": 2, "total": 5300, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "soft"}, "per_person_day": 422.5, "budget_level": "comfortable", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "soft", "amount": 5300, "target_min_ratio": 0.65, "target_max_ratio": 1.05, "target_min_total": 3400, "target_max_total": 5600, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 2, "room_count": 1, "priced_nights": 3, "expected_min_total_hotels": 1500, "reported_total_hotels": 1500, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_harder_eval_000004
- request: 张家界 2026-05-07->2026-05-09 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "自由人", "count": 3, "max_allowed": 2, "occurrences": [{"date": "2026-05-07", "type": "dinner", "name": "自由人(张家界国光实验学校店)"}, {"date": "2026-05-08", "type": "dinner", "name": "自由人(张家界国光实验学校店)"}, {"date": "2026-05-09", "type": "dinner", "name": "自由人(张家界国光实验学校店)"}]}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 2, "party_total": 1, "room_count": 1, "priced_nights": 2, "expected_min_total_hotels": 800, "reported_total_hotels": 1200, "diff": 400, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 160, "expected_total_attractions": 160, "reported_total_attractions": 240, "meal_per_person_cost_sum": 292, "expected_total_meals": 292, "reported_total_meals": 180, "reported_total_transportation": 200}}]`

### v3_harder_eval_000024
- request: 济南 2026-05-06->2026-05-08 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆']
- errors: `[{"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-05-08", "type": "dinner", "name": "酒店晚餐", "reason": "generic_lodging_meal"}]}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 240, "expected_total_attractions": 240, "reported_total_attractions": 240, "meal_per_person_cost_sum": 513, "expected_total_meals": 513, "reported_total_meals": 318, "reported_total_transportation": 600}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": true, "meal_cost_scale_ok": false, "budget_relationship_ok": false, "expected_total_hotels": 1200, "reported_total_hotels": 1200, "expected_total_attractions": 240, "reported_total_attractions": 240, "meal_scale_eval": {"ok": false, "party_total": 1, "budget_level": "comfortable", "per_person_lunch_dinner_floor": 50, "per_person_breakfast_floor": 20, "meal_count": 9, "checked_count": 6, "failure_count": 1, "failures": [{"date": "2026-05-07", "type": "lunch", "name": "醉得意·山茶油炒土鸡(济南芙蓉街店)", "estimated_cost": 45, "min_expected_cost": 50}]}}}]`

### v3_harder_eval_000014
- request: 成都 2026-06-02->2026-06-04 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆']
- errors: `[{"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-06-04", "type": "dinner", "name": "酒店晚餐", "reason": "generic_lodging_meal"}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 2, "party_total": 1, "room_count": 1, "priced_nights": 2, "expected_min_total_hotels": 900, "reported_total_hotels": 1350, "diff": 450, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 115, "expected_total_attractions": 115, "reported_total_attractions": 170, "meal_per_person_cost_sum": 1074, "expected_total_meals": 1074, "reported_total_meals": 390, "reported_total_transportation": 600}}]`

### v3_harder_eval_000028
- request: 深圳 2026-03-04->2026-03-06 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物']
- errors: `[{"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-03-06", "type": "dinner", "name": "酒店晚餐", "reason": "generic_lodging_meal"}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 2, "party_total": 3, "room_count": 2, "priced_nights": 2, "expected_min_total_hotels": 3200, "reported_total_hotels": 2400, "diff": -800, "covers_nights": false}}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 4058, "total": 3658, "diff": 400, "requested_budget": {"available": true, "amount": 4400, "scope": "total", "party_size": 3, "total": 4400, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "hard"}, "per_person_day": 406.44, "budget_level": "comfortable", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "hard", "amount": 4400, "target_min_ratio": 0.65, "target_max_ratio": 1.0, "target_min_total": 2900, "target_max_total": 4400, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 3, "room_count": 2, "priced_nights": 2, "expected_min_total_hotels": 3200, "reported_total_hotels": 2400, "diff": -800, "covers_nights": false}, "hotel_budget_covers_nights": false}}]`

### v3_harder_eval_000034
- request: 武汉 2026-06-02->2026-06-04 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 70, "expected_total_attractions": 70, "reported_total_attractions": 210, "meal_per_person_cost_sum": 514, "expected_total_meals": 514, "reported_total_meals": 234, "reported_total_transportation": 600}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 70, "expected_total_attractions": 70, "reported_total_attractions": 210, "meal_per_person_cost_sum": 514, "expected_total_meals": 514, "reported_total_meals": 234, "reported_total_transportation": 600}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": false, "meal_cost_scale_ok": false, "budget_relationship_ok": false, "expected_total_hotels": 1200, "reported_total_hotels": 1200, "expected_total_attractions": 70, "reported_total_attractions": 210, "meal_scale_eval": {"ok": false, "party_total": 1, "budget_level": "comfortable", "per_person_lunch_dinner_floor": 50, "per_person_breakfast_floor": 20, "meal_count": 9, "checked_count": 6, "failure_count": 1, "failures": [{"date": "2026-06-04", "type": "lunch", "name": "精武鸭脖.地标美食(顶秀嘉园店)", "estimated_cost": 18, "min_expected_cost": 50}]}}}]`

### v3_harder_eval_000029
- request: 长沙 2026-03-04->2026-03-07 days=4 transport=打车 hotel=亲子酒店 prefs=['亲子', '老人友好', '博物馆', '城市公园', '特色餐厅']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "友好饼店", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-03-04", "type": "breakfast", "name": "友好饼店"}, {"date": "2026-03-05", "type": "breakfast", "name": "友好饼店"}, {"date": "2026-03-06", "type": "breakfast", "name": "友好饼店"}, {"date": "2026-03-07", "type": "breakfast", "name": "友好饼店"}]}, {"name_key": "长沙芙蓉国温德姆至尊豪廷大酒店", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-03-04", "type": "lunch", "name": "长沙芙蓉国温德姆至尊豪廷大酒店"}, {"date": "2026-03-05", "type": "lunch", "name": "长沙芙蓉国温德姆至尊豪廷大酒店"}, {"date": "2026-03-06", "type": "lunch", "name": "长沙芙蓉国温德姆至尊豪廷大酒店"}, {"date": "2026-03-07", "type": "lunch", "name": "长沙芙蓉国温德姆至尊豪廷大酒店"}]}, {"name_key": "友好友善茶饮巴士", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-03-04", "type": "dinner", "name": "友好友善茶饮巴士"}, {"date": "2026-03-05", "type": "dinner", "name": "友好友善茶饮巴士"}, {"date": "2026-03-06", "type": "dinner", "name": "友好友善茶饮巴士"}, {"date": "2026-03-07", "type": "dinner", "name": "友好友善茶饮巴士"}]}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 40, "expected_total_attractions": 80, "reported_total_attractions": 0, "meal_per_person_cost_sum": 1104, "expected_total_meals": 2208, "reported_total_meals": 360, "reported_total_transportation": 800}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 40, "expected_total_attractions": 80, "reported_total_attractions": 0, "meal_per_person_cost_sum": 1104, "expected_total_meals": 2208, "reported_total_meals": 360, "reported_total_transportation": 800}}]`

### v3_harder_eval_000012
- request: 洛阳 2025-05-03->2025-05-06 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '夜市', '老字号', '城市漫步']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 4, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 1200, "reported_total_hotels": 600, "diff": -600, "covers_nights": false}}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 1520, "total": 1420, "diff": 100, "requested_budget": {"available": true, "amount": 3400, "scope": "total", "party_size": 4, "total": 3400, "source": "budget_constraint", "budget_level": "limited", "strictness": "hard"}, "per_person_day": 88.75, "budget_level": "limited", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "limited", "strictness": "hard", "amount": 3400, "target_min_ratio": 0.72, "target_max_ratio": 1.0, "target_min_total": 2400, "target_max_total": 3400, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 4, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 1200, "reported_total_hotels": 600, "diff": -600, "covers_nights": false}, "hotel_budget_covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 240, "expected_total_attractions": 960, "reported_total_attractions": 240, "meal_per_person_cost_sum": 533, "expected_total_meals": 2132, "reported_total_meals": 480, "reported_total_transportation": 200}}]`

### v3_harder_eval_000018
- request: 天津 2026-07-02->2026-07-04 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-07-03", "lunch": "苏焰·地标天津菜(多伦道店)", "dinner": "苏焰·地标天津菜(金海道店)"}, {"date": "2026-07-04", "lunch": "海底捞火锅(万象城店)", "dinner": "海底捞火锅(万象城店)"}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 2, "party_total": 3, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 7200, "reported_total_hotels": 3600, "diff": -3600, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 130, "expected_total_attractions": 390, "reported_total_attractions": 210, "meal_per_person_cost_sum": 1458, "expected_total_meals": 4374, "reported_total_meals": 1080, "reported_total_transportation": 600}}]`

### v3_harder_eval_000008
- request: 大理 2026-05-07->2026-05-09 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物']
- errors: `[{"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-05-09", "type": "dinner", "name": "天怡客栈(大理古城南门店)", "reason": "hotel_or_lodging_name"}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 2, "party_total": 3, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 5400, "reported_total_hotels": 2250, "diff": -3150, "covers_nights": false}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 75, "expected_total_attractions": 225, "reported_total_attractions": 225, "meal_per_person_cost_sum": 1488, "expected_total_meals": 4464, "reported_total_meals": 810, "reported_total_transportation": 600}}]`

### v3_harder_eval_000023
- request: 大理 2026-08-31->2026-09-04 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_grounding_miss", "details": [{"date": "2026-08-31", "type": "lunch", "name": "大理古城小吃街"}, {"date": "2026-08-31", "type": "dinner", "name": "大理古城美食街"}, {"date": "2026-09-01", "type": "lunch", "name": "大理古城小吃街"}, {"date": "2026-09-01", "type": "dinner", "name": "大理古城美食街"}, {"date": "2026-09-02", "type": "lunch", "name": "大理古城小吃街"}, {"date": "2026-09-02", "type": "dinner", "name": "大理古城美食街"}, {"date": "2026-09-03", "type": "lunch", "name": "大理古城小吃街"}, {"date": "2026-09-03", "type": "dinner", "name": "大理古城美食街"}, {"date": "2026-09-04", "type": "lunch", "name": "双廊古镇小吃街"}, {"date": "2026-09-04", "type": "dinner", "name": "双廊古镇美食街"}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 4, "party_total": 4, "room_count": 2, "priced_nights": 4, "expected_min_total_hotels": 3200, "reported_total_hotels": 1600, "diff": -1600, "covers_nights": false}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 75, "expected_total_attractions": 300, "reported_total_attractions": 300, "meal_per_person_cost_sum": 800, "expected_total_meals": 3200, "reported_total_meals": 320, "reported_total_transportation": 200}}]`

### v3_harder_eval_000032
- request: 丽江 2026-05-06->2026-05-09 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '夜市', '老字号', '城市漫步']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "丽江古城", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-05-06", "day_index": 0, "name": "丽江古城"}, {"date": "2026-05-09", "day_index": 3, "name": "丽江古城"}]}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 4, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 1200, "reported_total_hotels": 600, "diff": -600, "covers_nights": false}}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 2080, "total": 1880, "diff": 200, "requested_budget": {"available": true, "amount": 2400, "scope": "total", "party_size": 4, "total": 2400, "source": "budget_constraint", "budget_level": "limited", "strictness": "hard"}, "per_person_day": 117.5, "budget_level": "limited", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "limited", "strictness": "hard", "amount": 2400, "target_min_ratio": 0.72, "target_max_ratio": 1.0, "target_min_total": 1700, "target_max_total": 2400, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 4, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 1200, "reported_total_hotels": 600, "diff": -600, "covers_nights": false}, "hotel_budget_covers_nights": false}}]`

### v3_harder_eval_000022
- request: 桂林 2026-04-03->2026-04-06 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '夜市', '老字号', '城市漫步']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 4, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 1200, "reported_total_hotels": 800, "diff": -400, "covers_nights": false}}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 2600, "total": 2400, "diff": 200, "requested_budget": {"available": true, "amount": 2400, "scope": "total", "party_size": 4, "total": 2400, "source": "budget_constraint", "budget_level": "limited", "strictness": "hard"}, "per_person_day": 150.0, "budget_level": "limited", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "limited", "strictness": "hard", "amount": 2400, "target_min_ratio": 0.72, "target_max_ratio": 1.0, "target_min_total": 1700, "target_max_total": 2400, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 4, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 1200, "reported_total_hotels": 800, "diff": -400, "covers_nights": false}, "hotel_budget_covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 525, "expected_total_attractions": 2100, "reported_total_attractions": 1120, "meal_per_person_cost_sum": 1820, "expected_total_meals": 7280, "reported_total_meals": 480, "reported_total_transportation": 200}}]`

### v3_harder_eval_000038
- request: 厦门 2026-05-06->2026-05-08 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物']
- errors: `[{"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-05-06", "type": "dinner", "name": "厦门屿海民宿", "reason": "hotel_or_lodging_name"}]}, {"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-05-07", "lunch": "阿杰店沙茶面(老八市地标店)", "dinner": "阿杰店沙茶面(老八市地标店)"}, {"date": "2026-05-08", "lunch": "肯德基(滨北店)", "dinner": "肯德基(滨北店)"}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 2, "party_total": 3, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 4800, "reported_total_hotels": 2400, "diff": -2400, "covers_nights": false}}]`

### v3_harder_eval_000000
- request: 昆明 2026-04-03->2026-04-07 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-04-03", "type": "lunch", "name": "小人国主题公园", "reason": "non_food_poi_name"}, {"date": "2026-04-03", "type": "dinner", "name": "昆明捞渔河湿地公园", "reason": "non_food_poi_name"}, {"date": "2026-04-04", "type": "lunch", "name": "国立西南联合大学旧址", "reason": "unknown_food_semantics"}, {"date": "2026-04-04", "type": "dinner", "name": "云南民族博物馆", "reason": "non_food_poi_name"}, {"date": "2026-04-05", "type": "lunch", "name": "西华园", "reason": "unknown_food_semantics"}, {"date": "2026-04-05", "type": "dinner", "name": "月牙潭公园", "reason": "non_food_poi_name"}, {"date": "2026-04-06", "type": "lunch", "name": "云南美术馆(五一路)", "reason": "non_food_poi_name"}, {"date": "2026-04-06", "type": "dinner", "name": "宝海公园", "reason": "non_food_poi_name"}, {"date": "2026-04-07", "type": "lunch", "name": "西华园", "reason": "unknown_food_semantics"}, {"date": "2026-04-07", "type": "dinner", "name": "宝海公园", "reason": "non_food_poi_name"}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 4, "party_total": 5, "room_count": 3, "priced_nights": 4, "expected_min_total_hotels": 4800, "reported_total_hotels": 2000, "diff": -2800, "covers_nights": false}}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 3730, "total": 3930, "diff": -200, "requested_budget": {"available": true, "amount": 12800, "scope": "total", "party_size": 5, "total": 12800, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "hard"}, "per_person_day": 157.2, "budget_level": "comfortable", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "hard", "amount": 12800, "target_min_ratio": 0.65, "target_max_ratio": 1.0, "target_min_total": 8300, "target_max_total": 12800, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 4, "party_total": 5, "room_count": 3, "priced_nights": 4, "expected_min_total_hotels": 4800, "reported_total_hotels": 2000, "diff": -2800, "covers_nights": false}, "hotel_budget_covers_nights": false}}]`

### v3_harder_eval_000026
- request: 扬州 2026-05-07->2026-05-10 days=4 transport=自驾 hotel=亲子酒店 prefs=['亲子', '动物园', '海洋馆', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "accommodation_type_mismatch", "details": [{"date": "2026-05-10", "day_index": 3, "expected": "亲子酒店", "got": "无住宿"}]}, {"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-05-07", "type": "lunch", "name": "扬州炒饭", "reason": "unknown_food_semantics"}, {"date": "2026-05-07", "type": "dinner", "name": "扬州炒面", "reason": "unknown_food_semantics"}, {"date": "2026-05-08", "type": "lunch", "name": "扬州炒面", "reason": "unknown_food_semantics"}, {"date": "2026-05-08", "type": "dinner", "name": "扬州炒饭", "reason": "unknown_food_semantics"}, {"date": "2026-05-09", "type": "lunch", "name": "扬州炒面", "reason": "unknown_food_semantics"}, {"date": "2026-05-09", "type": "dinner", "name": "扬州炒饭", "reason": "unknown_food_semantics"}, {"date": "2026-05-10", "type": "lunch", "name": "扬州炒面", "reason": "unknown_food_semantics"}, {"date": "2026-05-10", "type": "dinner", "name": "扬州炒饭", "reason": "unknown_food_semantics"}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 3, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 3000, "reported_total_hotels": 1500, "diff": -1500, "covers_nights": false}}]`

### v3_harder_eval_000011
- request: 福州 2026-06-17->2026-06-20 days=4 transport=打车 hotel=高端酒店 prefs=['高端酒店', '艺术', '特色餐厅', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 2, "room_count": 1, "priced_nights": 3, "expected_min_total_hotels": 2250, "reported_total_hotels": 3000, "diff": 750, "covers_nights": false}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 0, "expected_total_attractions": 0, "reported_total_attractions": 0, "meal_per_person_cost_sum": 1710, "expected_total_meals": 3420, "reported_total_meals": 1440, "reported_total_transportation": 800}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": false, "attraction_budget_party_relation_ok": true, "meal_cost_scale_ok": true, "budget_relationship_ok": false, "expected_total_hotels": 2250, "reported_total_hotels": 3000, "expected_total_attractions": 0, "reported_total_attractions": 0, "meal_scale_eval": {"ok": true, "party_total": 2, "budget_level": "premium", "per_person_lunch_dinner_floor": 70, "per_person_breakfast_floor": 28, "meal_count": 12, "checked_count": 8, "failure_count": 0, "failures": []}}}]`

### v3_harder_eval_000031
- request: 成都 2026-05-07->2026-05-10 days=4 transport=打车 hotel=高端酒店 prefs=['高端酒店', '艺术', '特色餐厅', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 140, "expected_total_attractions": 280, "reported_total_attractions": 290, "meal_per_person_cost_sum": 996, "expected_total_meals": 1992, "reported_total_meals": 780, "reported_total_transportation": 800}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 140, "expected_total_attractions": 280, "reported_total_attractions": 290, "meal_per_person_cost_sum": 996, "expected_total_meals": 1992, "reported_total_meals": 780, "reported_total_transportation": 800}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": true, "meal_cost_scale_ok": false, "budget_relationship_ok": false, "expected_total_hotels": 2400, "reported_total_hotels": 2400, "expected_total_attractions": 280, "reported_total_attractions": 290, "meal_scale_eval": {"ok": false, "party_total": 2, "budget_level": "premium", "per_person_lunch_dinner_floor": 70, "per_person_breakfast_floor": 28, "meal_count": 12, "checked_count": 8, "failure_count": 1, "failures": [{"date": "2026-05-08", "type": "dinner", "name": "陶德砂锅(蜀汉店)", "estimated_cost": 69, "min_expected_cost": 70}]}}}]`

### v3_harder_eval_000007
- request: 成都 2026-05-07->2026-05-11 days=5 transport=公共交通 hotel=民宿 prefs=['小众展馆', '咖啡', '艺术', '城市漫步', '特色餐厅']
- errors: `[{"stage": "rule", "type": "meal_placeholder", "details": [{"date": "2026-05-08", "type": "dinner", "name": "M Stand(成都SKP店)"}, {"date": "2026-05-09", "type": "lunch", "name": "M Stand(成都SKP店)"}, {"date": "2026-05-10", "type": "dinner", "name": "M Stand(成都SKP店)"}]}, {"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-05-08", "type": "dinner", "name": "M Stand(成都SKP店)", "reason": "unknown_food_semantics"}, {"date": "2026-05-09", "type": "lunch", "name": "M Stand(成都SKP店)", "reason": "unknown_food_semantics"}, {"date": "2026-05-10", "type": "dinner", "name": "M Stand(成都SKP店)", "reason": "unknown_food_semantics"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "星巴克", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-05-07", "type": "dinner", "name": "星巴克(成都环球中心II店)"}, {"date": "2026-05-08", "type": "lunch", "name": "星巴克(成都SKP店)"}, {"date": "2026-05-09", "type": "dinner", "name": "星巴克(成都环球中心II店)"}, {"date": "2026-05-10", "type": "lunch", "name": "星巴克(成都大魔方招商花园城店)"}, {"date": "2026-05-11", "type": "dinner", "name": "星巴克(成都环球中心II店)"}]}]}]`

### v3_harder_eval_000002
- request: 杭州 2026-04-27->2026-04-30 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '夜市', '老字号', '城市漫步']
- errors: `[{"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-04-30", "type": "dinner", "name": "杭州拣枝而栖青年旅舍(龙湖滨江天街江陵路地铁站店)附近小吃", "reason": "hotel_or_lodging_name"}]}, {"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-04-29", "lunch": "杭州酒家(延安路店)", "dinner": "杭州酒家(延安路店)"}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 4, "room_count": 2, "priced_nights": 4, "expected_min_total_hotels": 2000, "reported_total_hotels": 1000, "diff": -1000, "covers_nights": false}}]`
