# Rule Eval Report: base_qwen25_7b_prompt_ablation_20260505_C

- records: 300
- generations: `training/outputs/eval/prompt_ablation_20260505/base_qwen25_7b_prompt_ablation_20260505_C/generations.jsonl`
- records_path: `training/data/v3/eval_harder_prompt_ablation_20260505/C/records.jsonl`

## Boolean Metrics

| Metric | Pass | Total | Rate |
| --- | ---: | ---: | ---: |
| accommodation_type_ok | 266 | 295 | 90.17% |
| attraction_budget_consistent | 42 | 295 | 14.24% |
| attraction_budget_party_relation_ok | 83 | 295 | 28.14% |
| attraction_count_ok | 295 | 295 | 100.00% |
| attraction_diversity_ok | 263 | 295 | 89.15% |
| attraction_grounding_ok | 291 | 295 | 98.64% |
| attraction_repeat_limit_ok | 263 | 295 | 89.15% |
| budget_arithmetic_consistent | 136 | 295 | 46.10% |
| budget_consistent | 136 | 295 | 46.10% |
| budget_level_aligned | 110 | 295 | 37.29% |
| budget_preference_aligned | 110 | 295 | 37.29% |
| budget_relationship_ok | 19 | 295 | 6.44% |
| budget_user_constraint_ok | 240 | 295 | 81.36% |
| budget_within_user_budget | 277 | 295 | 93.90% |
| city_ok | 295 | 295 | 100.00% |
| date_range_ok | 295 | 295 | 100.00% |
| day_dates_ok | 295 | 295 | 100.00% |
| day_index_ok | 295 | 295 | 100.00% |
| days_len_ok | 295 | 295 | 100.00% |
| dpo_soft_pass | 0 | 295 | 0.00% |
| hard_pass | 0 | 295 | 0.00% |
| hotel_budget_covers_nights | 111 | 295 | 37.63% |
| hotel_budget_relation_ok | 129 | 295 | 43.73% |
| hotel_distance_placeholder_ok | 295 | 295 | 100.00% |
| hotel_grounding_ok | 294 | 295 | 99.66% |
| invalid_hotel_name_ok | 295 | 295 | 100.00% |
| json_extract_ok | 299 | 300 | 99.67% |
| legacy_hard_pass | 18 | 295 | 6.10% |
| location_object_ok | 295 | 295 | 100.00% |
| meal_budget_consistent | 0 | 295 | 0.00% |
| meal_complete | 295 | 295 | 100.00% |
| meal_cost_scale_ok | 190 | 295 | 64.41% |
| meal_diversity_ok | 201 | 295 | 68.14% |
| meal_grounding_ok | 145 | 295 | 49.15% |
| meal_lunch_dinner_same_day_ok | 247 | 295 | 83.73% |
| meal_repeat_limit_ok | 228 | 295 | 77.29% |
| meal_specific_ok | 284 | 295 | 96.27% |
| meal_valid_semantics_ok | 159 | 295 | 53.90% |
| middle_hotel_ok | 295 | 295 | 100.00% |
| schema_ok | 295 | 300 | 98.33% |
| sft_budget_semantic_hard_pass | 8 | 295 | 2.71% |
| sft_hard_pass | 0 | 295 | 0.00% |
| transportation_budget_nonnegative | 295 | 295 | 100.00% |
| weather_dates_ok | 295 | 295 | 100.00% |
| weather_match | 294 | 295 | 99.66% |

## Numeric Metrics

```json
{
  "attraction_diversity_unique_rate": {
    "avg": 0.9793,
    "p50": 1.0,
    "p90": 1.0
  },
  "attraction_grounding_rate": {
    "avg": 0.9973,
    "p50": 1.0,
    "p90": 1.0
  },
  "hotel_grounding_rate": {
    "avg": 0.9992,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_diversity_unique_rate": {
    "avg": 0.5291,
    "p50": 0.5,
    "p90": 1.0
  },
  "meal_food_pois_grounding_rate": {
    "avg": 0.8267,
    "p50": 0.9333,
    "p90": 1.0
  },
  "meal_grounding_rate": {
    "avg": 0.8267,
    "p50": 0.9333,
    "p90": 1.0
  },
  "meal_semantic_valid_rate": {
    "avg": 0.8898,
    "p50": 1.0,
    "p90": 1.0
  }
}
```

## Failure Types

```json
{
  "meal_budget_inconsistent": 291,
  "budget_relationship_mismatch": 276,
  "attraction_budget_inconsistent": 253,
  "budget_preference_mismatch": 185,
  "hotel_budget_underestimated": 184,
  "budget_arithmetic_inconsistent": 159,
  "meal_invalid_name": 136,
  "meal_cost_scale_too_low": 105,
  "meal_repeat_too_many": 67,
  "budget_hard_constraint_exceeded": 55,
  "meal_same_day_lunch_dinner_repeat": 48,
  "attraction_repeat_too_many": 32,
  "accommodation_type_mismatch": 29,
  "meal_grounding_miss": 14,
  "meal_placeholder": 11,
  "schema": 4,
  "weather_mismatch": 1,
  "json_extract": 1
}
```

## Failure Examples

### v3_harder_eval_000034
- request: 武汉 2026-06-02->2026-06-04 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 70, "expected_total_attractions": 70, "reported_total_attractions": 0, "meal_per_person_cost_sum": 525, "expected_total_meals": 525, "reported_total_meals": 270, "reported_total_transportation": 600}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 70, "expected_total_attractions": 70, "reported_total_attractions": 0, "meal_per_person_cost_sum": 525, "expected_total_meals": 525, "reported_total_meals": 270, "reported_total_transportation": 600}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": false, "meal_cost_scale_ok": false, "budget_relationship_ok": false, "expected_total_hotels": 1200, "reported_total_hotels": 1200, "expected_total_attractions": 70, "reported_total_attractions": 0, "meal_scale_eval": {"ok": false, "party_total": 1, "budget_level": "comfortable", "per_person_lunch_dinner_floor": 50, "per_person_breakfast_floor": 20, "meal_count": 9, "checked_count": 6, "failure_count": 1, "failures": [{"date": "2026-06-04", "type": "lunch", "name": "精武鸭脖.地标美食(顶秀嘉园店)", "estimated_cost": 18, "min_expected_cost": 50}]}}}]`

### v3_harder_eval_000004
- request: 张家界 2026-05-07->2026-05-09 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "索溪山寨·湘西民间土菜", "count": 3, "max_allowed": 2, "occurrences": [{"date": "2026-05-07", "type": "lunch", "name": "索溪山寨·湘西民间土菜(标志门店)"}, {"date": "2026-05-08", "type": "lunch", "name": "索溪山寨·湘西民间土菜(溪布街店)"}, {"date": "2026-05-09", "type": "lunch", "name": "索溪山寨·湘西民间土菜(标志门店)"}]}, {"name_key": "自由人", "count": 3, "max_allowed": 2, "occurrences": [{"date": "2026-05-07", "type": "dinner", "name": "自由人(张家界国光实验学校店)"}, {"date": "2026-05-08", "type": "dinner", "name": "自由人(张家界国光实验学校店)"}, {"date": "2026-05-09", "type": "dinner", "name": "自由人(张家界国光实验学校店)"}]}]}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 240, "expected_total_attractions": 240, "reported_total_attractions": 240, "meal_per_person_cost_sum": 327, "expected_total_meals": 327, "reported_total_meals": 189, "reported_total_transportation": 200}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": true, "meal_cost_scale_ok": false, "budget_relationship_ok": false, "expected_total_hotels": 800, "reported_total_hotels": 800, "expected_total_attractions": 240, "reported_total_attractions": 240, "meal_scale_eval": {"ok": false, "party_total": 1, "budget_level": "comfortable", "per_person_lunch_dinner_floor": 50, "per_person_breakfast_floor": 20, "meal_count": 9, "checked_count": 6, "failure_count": 3, "failures": [{"date": "2026-05-07", "type": "dinner", "name": "自由人(张家界国光实验学校店)", "estimated_cost": 7, "min_expected_cost": 50}, {"date": "2026-05-08", "type": "dinner", "name": "自由人(张家界国光实验学校店)", "estimated_cost": 7, "min_expected_cost": 50}, {"date": "2026-05-09", "type": "dinner", "name": "自由人(张家界国光实验学校店)", "estimated_cost": 7, "min_expected_cost": 50}]}}}]`

### v3_harder_eval_000024
- request: 济南 2026-05-06->2026-05-08 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆']
- errors: `[{"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-05-08", "type": "dinner", "name": "酒店晚餐", "reason": "generic_lodging_meal"}]}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 2388, "total": 2488, "diff": -100, "requested_budget": {"available": true, "amount": 1700, "scope": "total", "party_size": 1, "total": 1700, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "hard"}, "per_person_day": 829.33, "budget_level": "comfortable", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "hard", "amount": 1700, "target_min_ratio": 0.65, "target_max_ratio": 1.0, "target_min_total": 1100, "target_max_total": 1700, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": false, "user_constraint_ok": false, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 1, "room_count": 1, "priced_nights": 3, "expected_min_total_hotels": 1200, "reported_total_hotels": 1200, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 240, "expected_total_attractions": 240, "reported_total_attractions": 240, "meal_per_person_cost_sum": 513, "expected_total_meals": 513, "reported_total_meals": 348, "reported_total_transportation": 600}}]`

### v3_harder_eval_000036
- request: 长沙 2026-06-02->2026-06-05 days=4 transport=自驾 hotel=亲子酒店 prefs=['亲子', '动物园', '海洋馆', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-06-05", "type": "lunch", "name": "酒店午餐", "reason": "generic_lodging_meal"}, {"date": "2026-06-05", "type": "dinner", "name": "酒店晚餐", "reason": "generic_lodging_meal"}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 3, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 3000, "reported_total_hotels": 1500, "diff": -1500, "covers_nights": false}}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 3340, "total": 3240, "diff": 100, "requested_budget": {"available": true, "amount": 5000, "scope": "total", "party_size": 3, "total": 5000, "source": "budget_constraint", "budget_level": "standard", "strictness": "hard"}, "per_person_day": 270.0, "budget_level": "standard", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "standard", "strictness": "hard", "amount": 5000, "target_min_ratio": 0.55, "target_max_ratio": 1.0, "target_min_total": 2800, "target_max_total": 5000, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 3, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 3000, "reported_total_hotels": 1500, "diff": -1500, "covers_nights": false}, "hotel_budget_covers_nights": false}}]`

### v3_harder_eval_000012
- request: 洛阳 2025-05-03->2025-05-06 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '夜市', '老字号', '城市漫步']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 4, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 1200, "reported_total_hotels": 600, "diff": -600, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 320, "expected_total_attractions": 1280, "reported_total_attractions": 1200, "meal_per_person_cost_sum": 1804, "expected_total_meals": 7216, "reported_total_meals": 960, "reported_total_transportation": 400}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 320, "expected_total_attractions": 1280, "reported_total_attractions": 1200, "meal_per_person_cost_sum": 1804, "expected_total_meals": 7216, "reported_total_meals": 960, "reported_total_transportation": 400}}]`

### v3_harder_eval_000019
- request: 丽江 2026-05-07->2026-05-10 days=4 transport=打车 hotel=亲子酒店 prefs=['亲子', '老人友好', '博物馆', '城市公园', '特色餐厅']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "丽江古城", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-05-07", "day_index": 0, "name": "丽江古城"}, {"date": "2026-05-10", "day_index": 3, "name": "丽江古城"}]}]}, {"stage": "rule", "type": "accommodation_type_mismatch", "details": [{"date": "2026-05-10", "day_index": 3, "expected": "亲子酒店", "got": "无住宿"}]}, {"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-05-07", "type": "lunch", "name": "丽江古城大水车东山雅居客栈餐厅", "reason": "hotel_or_lodging_name"}, {"date": "2026-05-07", "type": "dinner", "name": "丽江古城大水车东山雅居客栈餐厅", "reason": "hotel_or_lodging_name"}, {"date": "2026-05-08", "type": "lunch", "name": "丽江古城大水车东山雅居客栈餐厅", "reason": "hotel_or_lodging_name"}, {"date": "2026-05-08", "type": "dinner", "name": "丽江古城大水车东山雅居客栈餐厅", "reason": "hotel_or_lodging_name"}, {"date": "2026-05-09", "type": "lunch", "name": "丽江古城大水车东山雅居客栈餐厅", "reason": "hotel_or_lodging_name"}, {"date": "2026-05-09", "type": "dinner", "name": "丽江古城大水车东山雅居客栈餐厅", "reason": "hotel_or_lodging_name"}, {"date": "2026-05-10", "type": "lunch", "name": "丽江古城大水车东山雅居客栈餐厅", "reason": "hotel_or_lodging_name"}, {"date": "2026-05-10", "type": "dinner", "name": "无", "reason": "empty_or_none"}]}]`

### v3_harder_eval_000008
- request: 大理 2026-05-07->2026-05-09 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物']
- errors: `[{"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-05-09", "type": "dinner", "name": "酒店晚餐", "reason": "generic_lodging_meal"}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 2, "party_total": 3, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 4500, "reported_total_hotels": 2250, "diff": -2250, "covers_nights": false}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 75, "expected_total_attractions": 225, "reported_total_attractions": 225, "meal_per_person_cost_sum": 1488, "expected_total_meals": 4464, "reported_total_meals": 810, "reported_total_transportation": 600}}]`

### v3_harder_eval_000011
- request: 福州 2026-06-17->2026-06-20 days=4 transport=打车 hotel=高端酒店 prefs=['高端酒店', '艺术', '特色餐厅', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 2, "room_count": 1, "priced_nights": 3, "expected_min_total_hotels": 2250, "reported_total_hotels": 2700, "diff": 450, "covers_nights": false}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 0, "expected_total_attractions": 0, "reported_total_attractions": 0, "meal_per_person_cost_sum": 1790, "expected_total_meals": 3580, "reported_total_meals": 1260, "reported_total_transportation": 1200}}, {"stage": "rule", "type": "budget_preference_mismatch", "details": {"part_sum": 5160, "total": 5160, "diff": 0, "requested_budget": {"available": true, "amount": 8800, "scope": "total", "party_size": 2, "total": 8800, "source": "budget_constraint", "budget_level": "premium", "strictness": "soft"}, "per_person_day": 645.0, "budget_level": "premium", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "premium", "strictness": "soft", "amount": 8800, "target_min_ratio": 0.7, "target_max_ratio": 1.12, "target_min_total": 6200, "target_max_total": 9900, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": true, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 2, "room_count": 1, "priced_nights": 3, "expected_min_total_hotels": 2250, "reported_total_hotels": 2700, "diff": 450, "covers_nights": false}, "hotel_budget_covers_nights": false}}]`

### v3_harder_eval_000014
- request: 成都 2026-06-02->2026-06-04 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆']
- errors: `[{"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-06-04", "type": "dinner", "name": "酒店晚餐", "reason": "generic_lodging_meal"}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 115, "expected_total_attractions": 115, "reported_total_attractions": 275, "meal_per_person_cost_sum": 674, "expected_total_meals": 674, "reported_total_meals": 433, "reported_total_transportation": 600}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 115, "expected_total_attractions": 115, "reported_total_attractions": 275, "meal_per_person_cost_sum": 674, "expected_total_meals": 674, "reported_total_meals": 433, "reported_total_transportation": 600}}]`

### v3_harder_eval_000018
- request: 天津 2026-07-02->2026-07-04 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物']
- errors: `[{"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-07-04", "type": "dinner", "name": "酒店早餐", "reason": "hotel_or_lodging_name"}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 2, "party_total": 3, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 7200, "reported_total_hotels": 3600, "diff": -3600, "covers_nights": false}}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 5490, "total": 5890, "diff": -400, "requested_budget": {"available": true, "amount": 4800, "scope": "total", "party_size": 3, "total": 4800, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "hard"}, "per_person_day": 654.44, "budget_level": "comfortable", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "hard", "amount": 4800, "target_min_ratio": 0.65, "target_max_ratio": 1.0, "target_min_total": 3100, "target_max_total": 4800, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": false, "user_constraint_ok": false, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 3, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 7200, "reported_total_hotels": 3600, "diff": -3600, "covers_nights": false}, "hotel_budget_covers_nights": false}}]`

### v3_harder_eval_000006
- request: 南京 2026-07-02->2026-07-05 days=4 transport=自驾 hotel=亲子酒店 prefs=['亲子', '动物园', '海洋馆', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 3, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 3300, "reported_total_hotels": 1650, "diff": -1650, "covers_nights": false}}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 2210, "total": 2190, "diff": 20, "requested_budget": {"available": true, "amount": 4000, "scope": "total", "party_size": 3, "total": 4000, "source": "budget_constraint", "budget_level": "standard", "strictness": "hard"}, "per_person_day": 182.5, "budget_level": "standard", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "standard", "strictness": "hard", "amount": 4000, "target_min_ratio": 0.55, "target_max_ratio": 1.0, "target_min_total": 2200, "target_max_total": 4000, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 3, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 3300, "reported_total_hotels": 1650, "diff": -1650, "covers_nights": false}, "hotel_budget_covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 45, "expected_total_attractions": 135, "reported_total_attractions": 120, "meal_per_person_cost_sum": 640, "expected_total_meals": 1920, "reported_total_meals": 240, "reported_total_transportation": 200}}]`

### v3_harder_eval_000038
- request: 厦门 2026-05-06->2026-05-08 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物']
- errors: `[{"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-05-07", "type": "breakfast", "name": "厦门原宿海景公寓早餐", "reason": "hotel_or_lodging_name"}, {"date": "2026-05-08", "type": "dinner", "name": "厦门屿海民宿晚餐", "reason": "generic_lodging_meal"}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 2, "party_total": 3, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 4800, "reported_total_hotels": 2400, "diff": -2400, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 110, "expected_total_attractions": 330, "reported_total_attractions": 240, "meal_per_person_cost_sum": 1302, "expected_total_meals": 3906, "reported_total_meals": 1620, "reported_total_transportation": 600}}]`

### v3_harder_eval_000023
- request: 大理 2026-08-31->2026-09-04 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_grounding_miss", "details": [{"date": "2026-08-31", "type": "lunch", "name": "大理古城小吃街"}, {"date": "2026-08-31", "type": "dinner", "name": "大理古城特色餐厅"}, {"date": "2026-09-01", "type": "lunch", "name": "大理古城小吃街"}, {"date": "2026-09-01", "type": "dinner", "name": "大理古城特色餐厅"}, {"date": "2026-09-02", "type": "lunch", "name": "大理古城小吃街"}, {"date": "2026-09-02", "type": "dinner", "name": "大理古城特色餐厅"}, {"date": "2026-09-03", "type": "lunch", "name": "大理古城小吃街"}, {"date": "2026-09-03", "type": "dinner", "name": "大理古城特色餐厅"}, {"date": "2026-09-04", "type": "lunch", "name": "双廊古镇小吃街"}, {"date": "2026-09-04", "type": "dinner", "name": "双廊古镇特色餐厅"}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 4, "party_total": 4, "room_count": 2, "priced_nights": 4, "expected_min_total_hotels": 3200, "reported_total_hotels": 1600, "diff": -1600, "covers_nights": false}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 75, "expected_total_attractions": 300, "reported_total_attractions": 300, "meal_per_person_cost_sum": 800, "expected_total_meals": 3200, "reported_total_meals": 320, "reported_total_transportation": 200}}]`

### v3_harder_eval_000028
- request: 深圳 2026-03-04->2026-03-06 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 2, "party_total": 3, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 4800, "reported_total_hotels": 2400, "diff": -2400, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 240, "expected_total_attractions": 720, "reported_total_attractions": 460, "meal_per_person_cost_sum": 2142, "expected_total_meals": 6426, "reported_total_meals": 750, "reported_total_transportation": 600}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 240, "expected_total_attractions": 720, "reported_total_attractions": 460, "meal_per_person_cost_sum": 2142, "expected_total_meals": 6426, "reported_total_meals": 750, "reported_total_transportation": 600}}]`

### v3_harder_eval_000005
- request: 广州 2026-07-02->2026-07-06 days=5 transport=公共交通 hotel=民宿 prefs=['摄影', '自然风光', '城市漫步', '本地菜']
- errors: `[{"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-07-06", "type": "dinner", "name": "广州十三行博物馆", "reason": "non_food_poi_name"}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 460, "expected_total_attractions": 460, "reported_total_attractions": 1100, "meal_per_person_cost_sum": 904, "expected_total_meals": 904, "reported_total_meals": 360, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 460, "expected_total_attractions": 460, "reported_total_attractions": 1100, "meal_per_person_cost_sum": 904, "expected_total_meals": 904, "reported_total_meals": 360, "reported_total_transportation": 200}}]`

### v3_harder_eval_000029
- request: 长沙 2026-03-04->2026-03-07 days=4 transport=打车 hotel=亲子酒店 prefs=['亲子', '老人友好', '博物馆', '城市公园', '特色餐厅']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "友好饼店", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-03-04", "type": "breakfast", "name": "友好饼店"}, {"date": "2026-03-05", "type": "breakfast", "name": "友好饼店"}, {"date": "2026-03-06", "type": "breakfast", "name": "友好饼店"}, {"date": "2026-03-07", "type": "breakfast", "name": "友好饼店"}]}, {"name_key": "长沙芙蓉国温德姆至尊豪廷大酒店", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-03-04", "type": "lunch", "name": "长沙芙蓉国温德姆至尊豪廷大酒店"}, {"date": "2026-03-05", "type": "lunch", "name": "长沙芙蓉国温德姆至尊豪廷大酒店"}, {"date": "2026-03-06", "type": "lunch", "name": "长沙芙蓉国温德姆至尊豪廷大酒店"}, {"date": "2026-03-07", "type": "lunch", "name": "长沙芙蓉国温德姆至尊豪廷大酒店"}]}, {"name_key": "友好友善茶饮巴士", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-03-04", "type": "dinner", "name": "友好友善茶饮巴士"}, {"date": "2026-03-05", "type": "dinner", "name": "友好友善茶饮巴士"}, {"date": "2026-03-06", "type": "dinner", "name": "友好友善茶饮巴士"}, {"date": "2026-03-07", "type": "dinner", "name": "友好友善茶饮巴士"}]}]}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 2780, "total": 3060, "diff": -280, "requested_budget": {"available": true, "amount": 6200, "scope": "total", "party_size": 2, "total": 6200, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "soft"}, "per_person_day": 382.5, "budget_level": "comfortable", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "soft", "amount": 6200, "target_min_ratio": 0.65, "target_max_ratio": 1.05, "target_min_total": 4000, "target_max_total": 6500, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 2, "room_count": 1, "priced_nights": 3, "expected_min_total_hotels": 1500, "reported_total_hotels": 1500, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 77, "expected_total_attractions": 154, "reported_total_attractions": 120, "meal_per_person_cost_sum": 1104, "expected_total_meals": 2208, "reported_total_meals": 360, "reported_total_transportation": 800}}]`

### v3_harder_eval_000021
- request: 上海 2026-06-17->2026-06-20 days=4 transport=打车 hotel=高端酒店 prefs=['高端酒店', '艺术', '特色餐厅', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-06-17", "lunch": "3号仓库·餐厅(上海首店)", "dinner": "3号仓库·餐厅(徐汇绿地缤纷城店)"}, {"date": "2026-06-18", "lunch": "3号仓库·餐厅(上海首店)", "dinner": "3号仓库·餐厅(徐汇绿地缤纷城店)"}, {"date": "2026-06-19", "lunch": "3号仓库·餐厅(上海首店)", "dinner": "3号仓库·餐厅(徐汇绿地缤纷城店)"}, {"date": "2026-06-20", "lunch": "3号仓库·餐厅(上海首店)", "dinner": "3号仓库·餐厅(徐汇绿地缤纷城店)"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "紫阳村地道家常菜", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-06-17", "type": "breakfast", "name": "紫阳村地道家常菜(川沙店)"}, {"date": "2026-06-18", "type": "breakfast", "name": "紫阳村地道家常菜(川沙店)"}, {"date": "2026-06-19", "type": "breakfast", "name": "紫阳村地道家常菜(川沙店)"}, {"date": "2026-06-20", "type": "breakfast", "name": "紫阳村地道家常菜(川沙店)"}]}, {"name_key": "3号仓库·餐厅", "count": 8, "max_allowed": 3, "occurrences": [{"date": "2026-06-17", "type": "lunch", "name": "3号仓库·餐厅(上海首店)"}, {"date": "2026-06-17", "type": "dinner", "name": "3号仓库·餐厅(徐汇绿地缤纷城店)"}, {"date": "2026-06-18", "type": "lunch", "name": "3号仓库·餐厅(上海首店)"}, {"date": "2026-06-18", "type": "dinner", "name": "3号仓库·餐厅(徐汇绿地缤纷城店)"}, {"date": "2026-06-19", "type": "lunch", "name": "3号仓库·餐厅(上海首店)"}, {"date": "2026-06-19", "type": "dinner", "name": "3号仓库·餐厅(徐汇绿地缤纷城店)"}, {"date": "2026-06-20", "type": "lunch", "name": "3号仓库·餐厅(上海首店)"}, {"date": "2026-06-20", "type": "dinner", "name": "3号仓库·餐厅(徐汇绿地缤纷城店)"}]}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 585, "expected_total_attractions": 1170, "reported_total_attractions": 1505, "meal_per_person_cost_sum": 1560, "expected_total_meals": 3120, "reported_total_meals": 1014, "reported_total_transportation": 800}}]`

### v3_harder_eval_000031
- request: 成都 2026-05-07->2026-05-10 days=4 transport=打车 hotel=高端酒店 prefs=['高端酒店', '艺术', '特色餐厅', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 195, "expected_total_attractions": 390, "reported_total_attractions": 430, "meal_per_person_cost_sum": 1958, "expected_total_meals": 3916, "reported_total_meals": 1320, "reported_total_transportation": 800}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 195, "expected_total_attractions": 390, "reported_total_attractions": 430, "meal_per_person_cost_sum": 1958, "expected_total_meals": 3916, "reported_total_meals": 1320, "reported_total_transportation": 800}}, {"stage": "rule", "type": "budget_preference_mismatch", "details": {"part_sum": 4950, "total": 4950, "diff": 0, "requested_budget": {"available": true, "amount": 9600, "scope": "total", "party_size": 2, "total": 9600, "source": "budget_constraint", "budget_level": "premium", "strictness": "soft"}, "per_person_day": 618.75, "budget_level": "premium", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "premium", "strictness": "soft", "amount": 9600, "target_min_ratio": 0.7, "target_max_ratio": 1.12, "target_min_total": 6700, "target_max_total": 10800, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": true, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 2, "room_count": 1, "priced_nights": 3, "expected_min_total_hotels": 2400, "reported_total_hotels": 2400, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_harder_eval_000026
- request: 扬州 2026-05-07->2026-05-10 days=4 transport=自驾 hotel=亲子酒店 prefs=['亲子', '动物园', '海洋馆', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "accommodation_type_mismatch", "details": [{"date": "2026-05-10", "day_index": 3, "expected": "亲子酒店", "got": "无住宿"}]}, {"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-05-07", "type": "lunch", "name": "扬州炒饭", "reason": "unknown_food_semantics"}, {"date": "2026-05-07", "type": "dinner", "name": "扬州炒面", "reason": "unknown_food_semantics"}, {"date": "2026-05-08", "type": "lunch", "name": "扬州炒饭", "reason": "unknown_food_semantics"}, {"date": "2026-05-08", "type": "dinner", "name": "扬州炒面", "reason": "unknown_food_semantics"}, {"date": "2026-05-09", "type": "lunch", "name": "扬州炒饭", "reason": "unknown_food_semantics"}, {"date": "2026-05-09", "type": "dinner", "name": "扬州炒面", "reason": "unknown_food_semantics"}, {"date": "2026-05-10", "type": "lunch", "name": "扬州炒饭", "reason": "unknown_food_semantics"}, {"date": "2026-05-10", "type": "dinner", "name": "扬州炒面", "reason": "unknown_food_semantics"}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 3, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 3000, "reported_total_hotels": 1500, "diff": -1500, "covers_nights": false}}]`

### v3_harder_eval_000009
- request: 苏州 2026-04-26->2026-04-29 days=4 transport=打车 hotel=亲子酒店 prefs=['亲子', '老人友好', '博物馆', '城市公园', '特色餐厅']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 4, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 7500, "reported_total_hotels": 4000, "diff": -3500, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 250, "expected_total_attractions": 1000, "reported_total_attractions": 370, "meal_per_person_cost_sum": 1296, "expected_total_meals": 5184, "reported_total_meals": 1368, "reported_total_transportation": 800}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 250, "expected_total_attractions": 1000, "reported_total_attractions": 370, "meal_per_person_cost_sum": 1296, "expected_total_meals": 5184, "reported_total_meals": 1368, "reported_total_transportation": 800}}]`
