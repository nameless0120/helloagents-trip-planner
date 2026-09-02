# Rule Eval Report: base_qwen25_7b_v3_ctx_balanced_full_w10

- records: 300
- generations: `training/outputs/eval/base_qwen25_7b_v3_ctx_balanced_full_w10/generations.jsonl`
- records_path: `training/data/v3/context_ablation/balanced_baseline_full_context/records.jsonl`

## Boolean Metrics

| Metric | Pass | Total | Rate |
| --- | ---: | ---: | ---: |
| accommodation_type_ok | 222 | 292 | 76.03% |
| attraction_budget_consistent | 38 | 292 | 13.01% |
| attraction_count_ok | 292 | 292 | 100.00% |
| attraction_diversity_ok | 251 | 292 | 85.96% |
| attraction_grounding_ok | 283 | 292 | 96.92% |
| attraction_repeat_limit_ok | 251 | 292 | 85.96% |
| budget_arithmetic_consistent | 183 | 292 | 62.67% |
| budget_consistent | 183 | 292 | 62.67% |
| budget_level_aligned | 107 | 292 | 36.64% |
| budget_preference_aligned | 107 | 292 | 36.64% |
| budget_user_constraint_ok | 250 | 292 | 85.62% |
| budget_within_user_budget | 286 | 292 | 97.95% |
| city_ok | 292 | 292 | 100.00% |
| date_range_ok | 292 | 292 | 100.00% |
| day_dates_ok | 292 | 292 | 100.00% |
| day_index_ok | 292 | 292 | 100.00% |
| days_len_ok | 292 | 292 | 100.00% |
| dpo_soft_pass | 0 | 292 | 0.00% |
| hard_pass | 0 | 292 | 0.00% |
| hotel_budget_covers_nights | 214 | 292 | 73.29% |
| hotel_distance_placeholder_ok | 292 | 292 | 100.00% |
| hotel_grounding_ok | 291 | 292 | 99.66% |
| invalid_hotel_name_ok | 292 | 292 | 100.00% |
| json_extract_ok | 300 | 300 | 100.00% |
| legacy_hard_pass | 57 | 292 | 19.52% |
| location_object_ok | 292 | 292 | 100.00% |
| meal_budget_consistent | 3 | 292 | 1.03% |
| meal_complete | 292 | 292 | 100.00% |
| meal_diversity_ok | 149 | 292 | 51.03% |
| meal_grounding_ok | 255 | 292 | 87.33% |
| meal_lunch_dinner_same_day_ok | 202 | 292 | 69.18% |
| meal_repeat_limit_ok | 181 | 292 | 61.99% |
| meal_specific_ok | 291 | 292 | 99.66% |
| meal_valid_semantics_ok | 258 | 292 | 88.36% |
| middle_hotel_ok | 292 | 292 | 100.00% |
| schema_ok | 292 | 300 | 97.33% |
| sft_hard_pass | 0 | 292 | 0.00% |
| transportation_budget_nonnegative | 292 | 292 | 100.00% |
| weather_dates_ok | 292 | 292 | 100.00% |
| weather_match | 292 | 292 | 100.00% |

## Numeric Metrics

```json
{
  "attraction_diversity_unique_rate": {
    "avg": 0.9707,
    "p50": 1.0,
    "p90": 1.0
  },
  "attraction_grounding_rate": {
    "avg": 0.9946,
    "p50": 1.0,
    "p90": 1.0
  },
  "hotel_grounding_rate": {
    "avg": 0.9966,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_diversity_unique_rate": {
    "avg": 0.66,
    "p50": 0.7,
    "p90": 1.0
  },
  "meal_food_pois_grounding_rate": {
    "avg": 0.982,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_grounding_rate": {
    "avg": 0.982,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_semantic_valid_rate": {
    "avg": 0.9844,
    "p50": 1.0,
    "p90": 1.0
  }
}
```

## Failure Types

```json
{
  "meal_budget_inconsistent": 289,
  "attraction_budget_inconsistent": 254,
  "budget_preference_mismatch": 185,
  "meal_repeat_too_many": 111,
  "budget_arithmetic_inconsistent": 109,
  "meal_same_day_lunch_dinner_repeat": 90,
  "hotel_budget_underestimated": 78,
  "accommodation_type_mismatch": 70,
  "budget_hard_constraint_exceeded": 42,
  "attraction_repeat_too_many": 41,
  "meal_invalid_name": 34,
  "schema": 8,
  "meal_grounding_miss": 3,
  "meal_placeholder": 1
}
```

## Failure Examples

### v3_harder_eval_000004
- request: 张家界 2026-05-08->2026-05-10 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆']
- errors: `[{"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-05-08", "type": "dinner", "name": "酒店晚餐", "reason": "generic_lodging_meal"}, {"date": "2026-05-09", "type": "dinner", "name": "酒店晚餐", "reason": "generic_lodging_meal"}, {"date": "2026-05-10", "type": "dinner", "name": "酒店晚餐", "reason": "generic_lodging_meal"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "酒店晚餐", "count": 3, "max_allowed": 2, "occurrences": [{"date": "2026-05-08", "type": "dinner", "name": "酒店晚餐"}, {"date": "2026-05-09", "type": "dinner", "name": "酒店晚餐"}, {"date": "2026-05-10", "type": "dinner", "name": "酒店晚餐"}]}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 2, "priced_nights": 2, "expected_min_total_hotels": 800, "reported_total_hotels": 1200, "diff": 400, "covers_nights": false}}]`

### v3_harder_eval_000008
- request: 大理 2026-05-08->2026-05-10 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 2, "priced_nights": 2, "expected_min_total_hotels": 1500, "reported_total_hotels": 2250, "diff": 750, "covers_nights": false}}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 3669, "total": 3619, "diff": 50, "requested_budget": {"available": true, "amount": 5800, "scope": "total", "party_size": 3, "total": 5800, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "hard"}, "per_person_day": 402.11, "budget_level": "comfortable", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "hard", "amount": 5800, "target_min_ratio": 0.65, "target_max_ratio": 1.0, "target_min_total": 3800, "target_max_total": 5800, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 2, "priced_nights": 2, "expected_min_total_hotels": 1500, "reported_total_hotels": 2250, "diff": 750, "covers_nights": false}, "hotel_budget_covers_nights": false}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "attraction_ticket_sum": 75, "expected_total_attractions": 225, "reported_total_attractions": 225, "expected_total_meals": 1299, "reported_total_meals": 594, "reported_total_transportation": 600}}]`

### v3_harder_eval_000006
- request: 南京 2026-07-03->2026-07-06 days=4 transport=自驾 hotel=亲子酒店 prefs=['亲子', '动物园', '海洋馆', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "accommodation_type_mismatch", "details": [{"date": "2026-07-06", "day_index": 3, "expected": "亲子酒店", "got": "无住宿"}]}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 2810, "total": 2710, "diff": 100, "requested_budget": {"available": true, "amount": 4000, "scope": "total", "party_size": 3, "total": 4000, "source": "budget_constraint", "budget_level": "standard", "strictness": "hard"}, "per_person_day": 225.83, "budget_level": "standard", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "standard", "strictness": "hard", "amount": 4000, "target_min_ratio": 0.55, "target_max_ratio": 1.0, "target_min_total": 2200, "target_max_total": 4000, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 3, "priced_nights": 3, "expected_min_total_hotels": 1650, "reported_total_hotels": 1650, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "attraction_ticket_sum": 160, "expected_total_attractions": 480, "reported_total_attractions": 240, "expected_total_meals": 1416, "reported_total_meals": 720, "reported_total_transportation": 200}}]`

### v3_harder_eval_000002
- request: 杭州 2026-04-28->2026-05-01 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '夜市', '老字号', '城市漫步']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "attraction_ticket_sum": 270, "expected_total_attractions": 1080, "reported_total_attractions": 270, "expected_total_meals": 483, "reported_total_meals": 360, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 4, "attraction_ticket_sum": 270, "expected_total_attractions": 1080, "reported_total_attractions": 270, "expected_total_meals": 483, "reported_total_meals": 360, "reported_total_transportation": 200}}, {"stage": "rule", "type": "budget_preference_mismatch", "details": {"part_sum": 1580, "total": 1580, "diff": 0, "requested_budget": {"available": true, "amount": 3100, "scope": "total", "party_size": 4, "total": 3100, "source": "budget_constraint", "budget_level": "limited", "strictness": "hard"}, "per_person_day": 98.75, "budget_level": "limited", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "limited", "strictness": "hard", "amount": 3100, "target_min_ratio": 0.72, "target_max_ratio": 1.0, "target_min_total": 2200, "target_max_total": 3100, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": true, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 3, "priced_nights": 3, "expected_min_total_hotels": 750, "reported_total_hotels": 750, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_harder_eval_000009
- request: 苏州 2026-04-27->2026-04-30 days=4 transport=打车 hotel=亲子酒店 prefs=['亲子', '老人友好', '博物馆', '城市公园', '特色餐厅']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "priced_nights": 4, "expected_min_total_hotels": 5000, "reported_total_hotels": 4000, "diff": -1000, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "attraction_ticket_sum": 215, "expected_total_attractions": 860, "reported_total_attractions": 285, "expected_total_meals": 727, "reported_total_meals": 936, "reported_total_transportation": 800}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 4, "attraction_ticket_sum": 215, "expected_total_attractions": 860, "reported_total_attractions": 285, "expected_total_meals": 727, "reported_total_meals": 936, "reported_total_transportation": 800}}]`

### v3_harder_eval_000001
- request: 桂林 2026-09-01->2026-09-04 days=4 transport=打车 hotel=高端酒店 prefs=['高端酒店', '艺术', '特色餐厅', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-09-01", "lunch": "椿记烧鹅(中山店)", "dinner": "椿记烧鹅(西街店)"}, {"date": "2026-09-02", "lunch": "椿记烧鹅(中山店)", "dinner": "椿记烧鹅(西街店)"}, {"date": "2026-09-03", "lunch": "椿记烧鹅(中山店)", "dinner": "椿记烧鹅(西街店)"}, {"date": "2026-09-04", "lunch": "椿记烧鹅(中山店)", "dinner": "椿记烧鹅(西街店)"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "椿记烧鹅", "count": 8, "max_allowed": 3, "occurrences": [{"date": "2026-09-01", "type": "lunch", "name": "椿记烧鹅(中山店)"}, {"date": "2026-09-01", "type": "dinner", "name": "椿记烧鹅(西街店)"}, {"date": "2026-09-02", "type": "lunch", "name": "椿记烧鹅(中山店)"}, {"date": "2026-09-02", "type": "dinner", "name": "椿记烧鹅(西街店)"}, {"date": "2026-09-03", "type": "lunch", "name": "椿记烧鹅(中山店)"}, {"date": "2026-09-03", "type": "dinner", "name": "椿记烧鹅(西街店)"}, {"date": "2026-09-04", "type": "lunch", "name": "椿记烧鹅(中山店)"}, {"date": "2026-09-04", "type": "dinner", "name": "椿记烧鹅(西街店)"}]}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "priced_nights": 4, "expected_min_total_hotels": 3000, "reported_total_hotels": 2250, "diff": -750, "covers_nights": false}}]`

### v3_harder_eval_000000
- request: 昆明 2026-04-04->2026-04-08 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 5, "attraction_ticket_sum": 180, "expected_total_attractions": 900, "reported_total_attractions": 1280, "expected_total_meals": 3235, "reported_total_meals": 1200, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 5, "attraction_ticket_sum": 180, "expected_total_attractions": 900, "reported_total_attractions": 1280, "expected_total_meals": 3235, "reported_total_meals": 1200, "reported_total_transportation": 200}}, {"stage": "rule", "type": "budget_preference_mismatch", "details": {"part_sum": 4280, "total": 4280, "diff": 0, "requested_budget": {"available": true, "amount": 12800, "scope": "total", "party_size": 5, "total": 12800, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "hard"}, "per_person_day": 171.2, "budget_level": "comfortable", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "hard", "amount": 12800, "target_min_ratio": 0.65, "target_max_ratio": 1.0, "target_min_total": 8300, "target_max_total": 12800, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": true, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 4, "priced_nights": 4, "expected_min_total_hotels": 1600, "reported_total_hotels": 1600, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_harder_eval_000005
- request: 广州 2026-07-03->2026-07-07 days=5 transport=公共交通 hotel=民宿 prefs=['摄影', '自然风光', '城市漫步', '本地菜']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "流花湖公园", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-07-05", "day_index": 2, "name": "流花湖公园"}, {"date": "2026-07-07", "day_index": 4, "name": "流花湖公园"}]}]}, {"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-07-07", "type": "dinner", "name": "从零cosplay自拍体验馆", "reason": "unknown_food_semantics"}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 1, "attraction_ticket_sum": 235, "expected_total_attractions": 235, "reported_total_attractions": 1100, "expected_total_meals": 1396, "reported_total_meals": 480, "reported_total_transportation": 200}}]`

### v3_harder_eval_000003
- request: 西安 2025-05-04->2025-05-08 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "崔少野猫耳朵炒面", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2025-05-04", "type": "dinner", "name": "崔少野猫耳朵炒面(十里锦绣店)"}, {"date": "2025-05-05", "type": "lunch", "name": "崔少野猫耳朵炒面(十里锦绣店)"}, {"date": "2025-05-07", "type": "lunch", "name": "崔少野猫耳朵炒面(十里锦绣店)"}, {"date": "2025-05-08", "type": "lunch", "name": "崔少野猫耳朵炒面(十里锦绣店)"}]}, {"name_key": "马洪小炒泡馍馆", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2025-05-05", "type": "dinner", "name": "马洪小炒泡馍馆"}, {"date": "2025-05-06", "type": "dinner", "name": "马洪小炒泡馍馆"}, {"date": "2025-05-07", "type": "dinner", "name": "马洪小炒泡馍馆"}, {"date": "2025-05-08", "type": "dinner", "name": "马洪小炒泡馍馆"}]}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "attraction_ticket_sum": 50, "expected_total_attractions": 100, "reported_total_attractions": 240, "expected_total_meals": 622, "reported_total_meals": 480, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "attraction_ticket_sum": 50, "expected_total_attractions": 100, "reported_total_attractions": 240, "expected_total_meals": 622, "reported_total_meals": 480, "reported_total_transportation": 200}}]`

### v3_harder_eval_000007
- request: 成都 2026-05-08->2026-05-12 days=5 transport=公共交通 hotel=民宿 prefs=['小众展馆', '咖啡', '艺术', '城市漫步', '特色餐厅']
- errors: `[{"stage": "rule", "type": "accommodation_type_mismatch", "details": [{"date": "2026-05-12", "day_index": 4, "expected": "民宿", "got": "无住宿"}]}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 2900, "total": 2800, "diff": 100, "requested_budget": {"available": true, "amount": 7000, "scope": "total", "party_size": 2, "total": 7000, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "soft"}, "per_person_day": 280.0, "budget_level": "comfortable", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "soft", "amount": 7000, "target_min_ratio": 0.65, "target_max_ratio": 1.05, "target_min_total": 4600, "target_max_total": 7400, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 4, "priced_nights": 4, "expected_min_total_hotels": 1200, "reported_total_hotels": 1200, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "attraction_ticket_sum": 275, "expected_total_attractions": 550, "reported_total_attractions": 1020, "expected_total_meals": 2046, "reported_total_meals": 480, "reported_total_transportation": 200}}]`

### v3_harder_eval_000011
- request: 福州 2026-06-18->2026-06-21 days=4 transport=打车 hotel=高端酒店 prefs=['高端酒店', '艺术', '特色餐厅', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 5030, "total": 4030, "diff": 1000, "requested_budget": {"available": true, "amount": 8800, "scope": "total", "party_size": 2, "total": 8800, "source": "budget_constraint", "budget_level": "premium", "strictness": "soft"}, "per_person_day": 503.75, "budget_level": "premium", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "premium", "strictness": "soft", "amount": 8800, "target_min_ratio": 0.7, "target_max_ratio": 1.12, "target_min_total": 6200, "target_max_total": 9900, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 3, "priced_nights": 3, "expected_min_total_hotels": 2250, "reported_total_hotels": 2250, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "attraction_ticket_sum": 0, "expected_total_attractions": 0, "reported_total_attractions": 660, "expected_total_meals": 1724, "reported_total_meals": 1320, "reported_total_transportation": 800}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "attraction_ticket_sum": 0, "expected_total_attractions": 0, "reported_total_attractions": 660, "expected_total_meals": 1724, "reported_total_meals": 1320, "reported_total_transportation": 800}}]`

### v3_harder_eval_000014
- request: 成都 2026-06-03->2026-06-05 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 1, "attraction_ticket_sum": 195, "expected_total_attractions": 195, "reported_total_attractions": 295, "expected_total_meals": 756, "reported_total_meals": 463, "reported_total_transportation": 300}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 1, "attraction_ticket_sum": 195, "expected_total_attractions": 195, "reported_total_attractions": 295, "expected_total_meals": 756, "reported_total_meals": 463, "reported_total_transportation": 300}}, {"stage": "rule", "type": "budget_hard_constraint_exceeded", "details": {"part_sum": 2408, "total": 2408, "diff": 0, "requested_budget": {"available": true, "amount": 2100, "scope": "total", "party_size": 1, "total": 2100, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "hard"}, "per_person_day": 802.67, "budget_level": "comfortable", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "hard", "amount": 2100, "target_min_ratio": 0.65, "target_max_ratio": 1.0, "target_min_total": 1400, "target_max_total": 2100, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": true, "within_user_budget": true, "user_constraint_ok": false, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 2, "priced_nights": 3, "expected_min_total_hotels": 1350, "reported_total_hotels": 1350, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_harder_eval_000018
- request: 天津 2026-07-03->2026-07-05 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-07-05", "lunch": "魏斯理汉堡(天津乐宾百货店)", "dinner": "魏斯理汉堡(天津乐宾百货店)"}]}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 5220, "total": 5120, "diff": 100, "requested_budget": {"available": true, "amount": 4800, "scope": "total", "party_size": 3, "total": 4800, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "hard"}, "per_person_day": 568.89, "budget_level": "comfortable", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "hard", "amount": 4800, "target_min_ratio": 0.65, "target_max_ratio": 1.0, "target_min_total": 3100, "target_max_total": 4800, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": false, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 2, "priced_nights": 3, "expected_min_total_hotels": 3600, "reported_total_hotels": 3600, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "attraction_ticket_sum": 130, "expected_total_attractions": 390, "reported_total_attractions": 210, "expected_total_meals": 906, "reported_total_meals": 810, "reported_total_transportation": 600}}]`

### v3_harder_eval_000010
- request: 西安 2026-04-20->2026-04-24 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-04-24", "lunch": "马洪小炒泡馍馆", "dinner": "马洪小炒泡馍馆"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "马洪小炒泡馍馆", "count": 6, "max_allowed": 3, "occurrences": [{"date": "2026-04-20", "type": "dinner", "name": "马洪小炒泡馍馆"}, {"date": "2026-04-21", "type": "dinner", "name": "马洪小炒泡馍馆"}, {"date": "2026-04-22", "type": "dinner", "name": "马洪小炒泡馍馆"}, {"date": "2026-04-23", "type": "dinner", "name": "马洪小炒泡馍馆"}, {"date": "2026-04-24", "type": "lunch", "name": "马洪小炒泡馍馆"}, {"date": "2026-04-24", "type": "dinner", "name": "马洪小炒泡馍馆"}]}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 4, "priced_nights": 4, "expected_min_total_hotels": 1800, "reported_total_hotels": 2250, "diff": 450, "covers_nights": false}}]`

### v3_harder_eval_000013
- request: 武汉 2026-05-06->2026-05-10 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-05-08", "lunch": "刘聋子牛肉粉馆(汉阳玫瑰街店)", "dinner": "刘聋子牛肉粉馆(汉阳玫瑰街店)"}, {"date": "2026-05-09", "lunch": "刘聋子牛肉粉馆(汉阳玫瑰街店)", "dinner": "刘聋子牛肉粉馆(汉阳玫瑰街店)"}, {"date": "2026-05-10", "lunch": "刘聋子牛肉粉馆(汉阳玫瑰街店)", "dinner": "刘聋子牛肉粉馆(汉阳玫瑰街店)"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "刘聋子牛肉粉馆", "count": 8, "max_allowed": 3, "occurrences": [{"date": "2026-05-06", "type": "dinner", "name": "刘聋子牛肉粉馆(汉阳玫瑰街店)"}, {"date": "2026-05-07", "type": "dinner", "name": "刘聋子牛肉粉馆(汉阳玫瑰街店)"}, {"date": "2026-05-08", "type": "lunch", "name": "刘聋子牛肉粉馆(汉阳玫瑰街店)"}, {"date": "2026-05-08", "type": "dinner", "name": "刘聋子牛肉粉馆(汉阳玫瑰街店)"}, {"date": "2026-05-09", "type": "lunch", "name": "刘聋子牛肉粉馆(汉阳玫瑰街店)"}, {"date": "2026-05-09", "type": "dinner", "name": "刘聋子牛肉粉馆(汉阳玫瑰街店)"}, {"date": "2026-05-10", "type": "lunch", "name": "刘聋子牛肉粉馆(汉阳玫瑰街店)"}, {"date": "2026-05-10", "type": "dinner", "name": "刘聋子牛肉粉馆(汉阳玫瑰街店)"}]}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "attraction_ticket_sum": 70, "expected_total_attractions": 140, "reported_total_attractions": 210, "expected_total_meals": 694, "reported_total_meals": 1200, "reported_total_transportation": 200}}]`

### v3_harder_eval_000019
- request: 丽江 2026-05-08->2026-05-11 days=4 transport=打车 hotel=亲子酒店 prefs=['亲子', '老人友好', '博物馆', '城市公园', '特色餐厅']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "丽江古城", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-05-08", "day_index": 0, "name": "丽江古城"}, {"date": "2026-05-11", "day_index": 3, "name": "丽江古城"}]}]}, {"stage": "rule", "type": "accommodation_type_mismatch", "details": [{"date": "2026-05-11", "day_index": 3, "expected": "亲子酒店", "got": "无住宿"}]}, {"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-05-08", "lunch": "则瓦米线·云南小吃集合(花巷店)", "dinner": "则瓦米线·云南小吃集合(一中店)"}, {"date": "2026-05-09", "lunch": "则瓦米线·云南小吃集合(花巷店)", "dinner": "则瓦米线·云南小吃集合(一中店)"}, {"date": "2026-05-10", "lunch": "则瓦米线·云南小吃集合(花巷店)", "dinner": "则瓦米线·云南小吃集合(一中店)"}, {"date": "2026-05-11", "lunch": "则瓦米线·云南小吃集合(花巷店)", "dinner": "则瓦米线·云南小吃集合(一中店)"}]}]`

### v3_harder_eval_000016
- request: 苏州 2026-06-03->2026-06-06 days=4 transport=自驾 hotel=亲子酒店 prefs=['亲子', '动物园', '海洋馆', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "accommodation_type_mismatch", "details": [{"date": "2026-06-06", "day_index": 3, "expected": "亲子酒店", "got": "无住宿"}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "attraction_ticket_sum": 90, "expected_total_attractions": 270, "reported_total_attractions": 260, "expected_total_meals": 698, "reported_total_meals": 1020, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "attraction_ticket_sum": 90, "expected_total_attractions": 270, "reported_total_attractions": 260, "expected_total_meals": 698, "reported_total_meals": 1020, "reported_total_transportation": 200}}]`

### v3_harder_eval_000012
- request: 洛阳 2025-05-04->2025-05-07 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '夜市', '老字号', '城市漫步']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2025-05-04", "lunch": "洛阳十字街小吃一条街", "dinner": "洛阳十字街小吃一条街"}, {"date": "2025-05-05", "lunch": "洛阳宴.洛阳菜(南昌路店)", "dinner": "洛阳宴.洛阳菜(南昌路店)"}, {"date": "2025-05-06", "lunch": "光头东烙馍村·水席洛阳菜(火车站店)", "dinner": "光头东烙馍村·水席洛阳菜(火车站店)"}, {"date": "2025-05-07", "lunch": "必胜客(正大广场店)", "dinner": "必胜客(正大广场店)"}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "priced_nights": 3, "expected_min_total_hotels": 700, "reported_total_hotels": 1200, "diff": 500, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "attraction_ticket_sum": 240, "expected_total_attractions": 960, "reported_total_attractions": 320, "expected_total_meals": 2040, "reported_total_meals": 1224, "reported_total_transportation": 200}}]`

### v3_harder_eval_000020
- request: 杭州 2026-06-18->2026-06-22 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 5, "attraction_ticket_sum": 413, "expected_total_attractions": 2065, "reported_total_attractions": 1200, "expected_total_meals": 4310, "reported_total_meals": 1200, "reported_total_transportation": 500}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 5, "attraction_ticket_sum": 413, "expected_total_attractions": 2065, "reported_total_attractions": 1200, "expected_total_meals": 4310, "reported_total_meals": 1200, "reported_total_transportation": 500}}, {"stage": "rule", "type": "budget_preference_mismatch", "details": {"part_sum": 4900, "total": 4900, "diff": 0, "requested_budget": {"available": true, "amount": 16100, "scope": "total", "party_size": 5, "total": 16100, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "hard"}, "per_person_day": 196.0, "budget_level": "comfortable", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "hard", "amount": 16100, "target_min_ratio": 0.65, "target_max_ratio": 1.0, "target_min_total": 10500, "target_max_total": 16100, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": true, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 4, "priced_nights": 4, "expected_min_total_hotels": 2000, "reported_total_hotels": 2000, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_harder_eval_000017
- request: 苏州 2026-05-06->2026-05-10 days=5 transport=公共交通 hotel=民宿 prefs=['小众展馆', '咖啡', '艺术', '城市漫步', '特色餐厅']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "attraction_ticket_sum": 295, "expected_total_attractions": 590, "reported_total_attractions": 180, "expected_total_meals": 2322, "reported_total_meals": 480, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "attraction_ticket_sum": 295, "expected_total_attractions": 590, "reported_total_attractions": 180, "expected_total_meals": 2322, "reported_total_meals": 480, "reported_total_transportation": 200}}, {"stage": "rule", "type": "budget_preference_mismatch", "details": {"part_sum": 2060, "total": 2060, "diff": 0, "requested_budget": {"available": true, "amount": 6700, "scope": "total", "party_size": 2, "total": 6700, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "soft"}, "per_person_day": 206.0, "budget_level": "comfortable", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "soft", "amount": 6700, "target_min_ratio": 0.65, "target_max_ratio": 1.05, "target_min_total": 4400, "target_max_total": 7000, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": true, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 4, "priced_nights": 4, "expected_min_total_hotels": 1200, "reported_total_hotels": 1200, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`
