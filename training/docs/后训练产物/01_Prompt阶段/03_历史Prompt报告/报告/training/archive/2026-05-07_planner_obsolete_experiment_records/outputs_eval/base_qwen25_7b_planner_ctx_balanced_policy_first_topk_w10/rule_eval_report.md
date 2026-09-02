# Rule Eval Report: base_qwen25_7b_v3_ctx_balanced_policy_first_topk_w10

- records: 300
- generations: `training/outputs/eval/base_qwen25_7b_v3_ctx_balanced_policy_first_topk_w10/generations.jsonl`
- records_path: `training/data/v3/context_ablation/balanced_baseline_policy_first_topk_context/records.jsonl`

## Boolean Metrics

| Metric | Pass | Total | Rate |
| --- | ---: | ---: | ---: |
| accommodation_type_ok | 257 | 297 | 86.53% |
| attraction_budget_consistent | 25 | 297 | 8.42% |
| attraction_count_ok | 296 | 297 | 99.66% |
| attraction_diversity_ok | 258 | 297 | 86.87% |
| attraction_grounding_ok | 284 | 297 | 95.62% |
| attraction_repeat_limit_ok | 258 | 297 | 86.87% |
| budget_arithmetic_consistent | 196 | 297 | 65.99% |
| budget_consistent | 196 | 297 | 65.99% |
| budget_level_aligned | 133 | 297 | 44.78% |
| budget_preference_aligned | 133 | 297 | 44.78% |
| budget_user_constraint_ok | 264 | 297 | 88.89% |
| budget_within_user_budget | 290 | 297 | 97.64% |
| city_ok | 297 | 297 | 100.00% |
| date_range_ok | 297 | 297 | 100.00% |
| day_dates_ok | 297 | 297 | 100.00% |
| day_index_ok | 297 | 297 | 100.00% |
| days_len_ok | 297 | 297 | 100.00% |
| dpo_soft_pass | 0 | 297 | 0.00% |
| hard_pass | 1 | 297 | 0.34% |
| hotel_budget_covers_nights | 253 | 297 | 85.19% |
| hotel_distance_placeholder_ok | 297 | 297 | 100.00% |
| hotel_grounding_ok | 297 | 297 | 100.00% |
| invalid_hotel_name_ok | 297 | 297 | 100.00% |
| json_extract_ok | 299 | 300 | 99.67% |
| legacy_hard_pass | 67 | 297 | 22.56% |
| location_object_ok | 297 | 297 | 100.00% |
| meal_budget_consistent | 1 | 297 | 0.34% |
| meal_complete | 297 | 297 | 100.00% |
| meal_diversity_ok | 152 | 297 | 51.18% |
| meal_grounding_ok | 254 | 297 | 85.52% |
| meal_lunch_dinner_same_day_ok | 220 | 297 | 74.07% |
| meal_repeat_limit_ok | 191 | 297 | 64.31% |
| meal_specific_ok | 297 | 297 | 100.00% |
| meal_valid_semantics_ok | 258 | 297 | 86.87% |
| middle_hotel_ok | 297 | 297 | 100.00% |
| schema_ok | 297 | 300 | 99.00% |
| sft_hard_pass | 1 | 297 | 0.34% |
| transportation_budget_nonnegative | 297 | 297 | 100.00% |
| weather_dates_ok | 297 | 297 | 100.00% |
| weather_match | 289 | 297 | 97.31% |

## Numeric Metrics

```json
{
  "attraction_diversity_unique_rate": {
    "avg": 0.9761,
    "p50": 1.0,
    "p90": 1.0
  },
  "attraction_grounding_rate": {
    "avg": 0.9924,
    "p50": 1.0,
    "p90": 1.0
  },
  "hotel_grounding_rate": {
    "avg": 1.0,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_diversity_unique_rate": {
    "avg": 0.667,
    "p50": 0.7,
    "p90": 1.0
  },
  "meal_food_pois_grounding_rate": {
    "avg": 0.9814,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_grounding_rate": {
    "avg": 0.9814,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_semantic_valid_rate": {
    "avg": 0.9836,
    "p50": 1.0,
    "p90": 1.0
  }
}
```

## Failure Types

```json
{
  "meal_budget_inconsistent": 296,
  "attraction_budget_inconsistent": 272,
  "budget_preference_mismatch": 164,
  "meal_repeat_too_many": 106,
  "budget_arithmetic_inconsistent": 101,
  "meal_same_day_lunch_dinner_repeat": 77,
  "hotel_budget_underestimated": 44,
  "accommodation_type_mismatch": 40,
  "meal_invalid_name": 39,
  "attraction_repeat_too_many": 39,
  "budget_hard_constraint_exceeded": 33,
  "weather_mismatch": 8,
  "meal_grounding_miss": 4,
  "schema": 2,
  "json_extract": 1
}
```

## Failure Examples

### v3_harder_eval_000004
- request: 张家界 2026-05-08->2026-05-10 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆']
- errors: `[{"stage": "json_extract", "message": "响应中未找到完整的顶层TripPlan JSON对象"}]`

### v3_harder_eval_000008
- request: 大理 2026-05-08->2026-05-10 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 2520, "total": 2420, "diff": 100, "requested_budget": {"available": true, "amount": 5800, "scope": "total", "party_size": 3, "total": 5800, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "hard"}, "per_person_day": 268.89, "budget_level": "comfortable", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "hard", "amount": 5800, "target_min_ratio": 0.65, "target_max_ratio": 1.0, "target_min_total": 3800, "target_max_total": 5800, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 2, "priced_nights": 2, "expected_min_total_hotels": 1500, "reported_total_hotels": 1500, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "attraction_ticket_sum": 0, "expected_total_attractions": 0, "reported_total_attractions": 180, "expected_total_meals": 1062, "reported_total_meals": 540, "reported_total_transportation": 300}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "attraction_ticket_sum": 0, "expected_total_attractions": 0, "reported_total_attractions": 180, "expected_total_meals": 1062, "reported_total_meals": 540, "reported_total_transportation": 300}}]`

### v3_harder_eval_000002
- request: 杭州 2026-04-28->2026-05-01 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '夜市', '老字号', '城市漫步']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 3250, "total": 2250, "diff": 1000, "requested_budget": {"available": true, "amount": 3100, "scope": "total", "party_size": 4, "total": 3100, "source": "budget_constraint", "budget_level": "limited", "strictness": "hard"}, "per_person_day": 140.62, "budget_level": "limited", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "limited", "strictness": "hard", "amount": 3100, "target_min_ratio": 0.72, "target_max_ratio": 1.0, "target_min_total": 2200, "target_max_total": 3100, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 3, "priced_nights": 3, "expected_min_total_hotels": 750, "reported_total_hotels": 750, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "attraction_ticket_sum": 270, "expected_total_attractions": 1080, "reported_total_attractions": 1100, "expected_total_meals": 2192, "reported_total_meals": 1200, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 4, "attraction_ticket_sum": 270, "expected_total_attractions": 1080, "reported_total_attractions": 1100, "expected_total_meals": 2192, "reported_total_meals": 1200, "reported_total_transportation": 200}}]`

### v3_harder_eval_000006
- request: 南京 2026-07-03->2026-07-06 days=4 transport=自驾 hotel=亲子酒店 prefs=['亲子', '动物园', '海洋馆', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "accommodation_type_mismatch", "details": [{"date": "2026-07-06", "day_index": 3, "expected": "亲子酒店", "got": "无住宿"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "金陵家宴·金陵春.南京菜", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-07-03", "type": "dinner", "name": "金陵家宴·金陵春.南京菜(夫子庙店)"}, {"date": "2026-07-04", "type": "dinner", "name": "金陵家宴·金陵春.南京菜(夫子庙店)"}, {"date": "2026-07-05", "type": "dinner", "name": "金陵家宴·金陵春.南京菜(夫子庙店)"}, {"date": "2026-07-06", "type": "dinner", "name": "金陵家宴·金陵春.南京菜(夫子庙店)"}]}]}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 2550, "total": 2640, "diff": -90, "requested_budget": {"available": true, "amount": 4000, "scope": "total", "party_size": 3, "total": 4000, "source": "budget_constraint", "budget_level": "standard", "strictness": "hard"}, "per_person_day": 220.0, "budget_level": "standard", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "standard", "strictness": "hard", "amount": 4000, "target_min_ratio": 0.55, "target_max_ratio": 1.0, "target_min_total": 2200, "target_max_total": 4000, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 3, "priced_nights": 3, "expected_min_total_hotels": 1650, "reported_total_hotels": 1650, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_harder_eval_000001
- request: 桂林 2026-09-01->2026-09-04 days=4 transport=打车 hotel=高端酒店 prefs=['高端酒店', '艺术', '特色餐厅', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-09-01", "lunch": "椿记烧鹅(中山店)", "dinner": "椿记烧鹅(西街店)"}, {"date": "2026-09-02", "lunch": "椿记烧鹅(西街店)", "dinner": "椿记烧鹅(南溪店)"}, {"date": "2026-09-03", "lunch": "椿记烧鹅(南溪店)", "dinner": "椿记烧鹅(中山店)"}, {"date": "2026-09-04", "lunch": "椿记烧鹅(西街店)", "dinner": "椿记烧鹅(中山店)"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "椿记烧鹅", "count": 8, "max_allowed": 3, "occurrences": [{"date": "2026-09-01", "type": "lunch", "name": "椿记烧鹅(中山店)"}, {"date": "2026-09-01", "type": "dinner", "name": "椿记烧鹅(西街店)"}, {"date": "2026-09-02", "type": "lunch", "name": "椿记烧鹅(西街店)"}, {"date": "2026-09-02", "type": "dinner", "name": "椿记烧鹅(南溪店)"}, {"date": "2026-09-03", "type": "lunch", "name": "椿记烧鹅(南溪店)"}, {"date": "2026-09-03", "type": "dinner", "name": "椿记烧鹅(中山店)"}, {"date": "2026-09-04", "type": "lunch", "name": "椿记烧鹅(西街店)"}, {"date": "2026-09-04", "type": "dinner", "name": "椿记烧鹅(中山店)"}]}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "attraction_ticket_sum": 625, "expected_total_attractions": 1250, "reported_total_attractions": 615, "expected_total_meals": 1016, "reported_total_meals": 660, "reported_total_transportation": 400}}]`

### v3_harder_eval_000005
- request: 广州 2026-07-03->2026-07-07 days=5 transport=公共交通 hotel=民宿 prefs=['摄影', '自然风光', '城市漫步', '本地菜']
- errors: `[{"stage": "rule", "type": "accommodation_type_mismatch", "details": [{"date": "2026-07-07", "day_index": 4, "expected": "民宿", "got": "无住宿"}]}, {"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-07-06", "lunch": "滋粥楼·顺德菜(南村万博长隆商圈店)", "dinner": "滋粥楼·顺德菜(番禺广场总店)"}]}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 2900, "total": 2000, "diff": 900, "requested_budget": {"available": true, "amount": 2600, "scope": "total", "party_size": 1, "total": 2600, "source": "budget_constraint", "budget_level": "standard", "strictness": "hard"}, "per_person_day": 400.0, "budget_level": "standard", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "standard", "strictness": "hard", "amount": 2600, "target_min_ratio": 0.55, "target_max_ratio": 1.0, "target_min_total": 1400, "target_max_total": 2600, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 4, "priced_nights": 4, "expected_min_total_hotels": 1200, "reported_total_hotels": 1200, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_harder_eval_000009
- request: 苏州 2026-04-27->2026-04-30 days=4 transport=打车 hotel=亲子酒店 prefs=['亲子', '老人友好', '博物馆', '城市公园', '特色餐厅']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 6015, "total": 6915, "diff": -900, "requested_budget": {"available": true, "amount": 9100, "scope": "total", "party_size": 4, "total": 9100, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "soft"}, "per_person_day": 432.19, "budget_level": "comfortable", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "soft", "amount": 9100, "target_min_ratio": 0.65, "target_max_ratio": 1.05, "target_min_total": 5900, "target_max_total": 9600, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 3, "priced_nights": 3, "expected_min_total_hotels": 3750, "reported_total_hotels": 3750, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "attraction_ticket_sum": 135, "expected_total_attractions": 540, "reported_total_attractions": 265, "expected_total_meals": 1956, "reported_total_meals": 1200, "reported_total_transportation": 800}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 4, "attraction_ticket_sum": 135, "expected_total_attractions": 540, "reported_total_attractions": 265, "expected_total_meals": 1956, "reported_total_meals": 1200, "reported_total_transportation": 800}}]`

### v3_harder_eval_000000
- request: 昆明 2026-04-04->2026-04-08 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 4950, "total": 5950, "diff": -1000, "requested_budget": {"available": true, "amount": 12800, "scope": "total", "party_size": 5, "total": 12800, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "hard"}, "per_person_day": 238.0, "budget_level": "comfortable", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "hard", "amount": 12800, "target_min_ratio": 0.65, "target_max_ratio": 1.0, "target_min_total": 8300, "target_max_total": 12800, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 4, "priced_nights": 4, "expected_min_total_hotels": 1600, "reported_total_hotels": 1600, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 5, "attraction_ticket_sum": 110, "expected_total_attractions": 550, "reported_total_attractions": 1150, "expected_total_meals": 2460, "reported_total_meals": 1200, "reported_total_transportation": 1000}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 5, "attraction_ticket_sum": 110, "expected_total_attractions": 550, "reported_total_attractions": 1150, "expected_total_meals": 2460, "reported_total_meals": 1200, "reported_total_transportation": 1000}}]`

### v3_harder_eval_000003
- request: 西安 2025-05-04->2025-05-08 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2025-05-08", "type": "dinner", "name": "酒店晚餐", "reason": "generic_lodging_meal"}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "attraction_ticket_sum": 200, "expected_total_attractions": 400, "reported_total_attractions": 450, "expected_total_meals": 966, "reported_total_meals": 480, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "attraction_ticket_sum": 200, "expected_total_attractions": 400, "reported_total_attractions": 450, "expected_total_meals": 966, "reported_total_meals": 480, "reported_total_transportation": 200}}]`

### v3_harder_eval_000007
- request: 成都 2026-05-08->2026-05-12 days=5 transport=公共交通 hotel=民宿 prefs=['小众展馆', '咖啡', '艺术', '城市漫步', '特色餐厅']
- errors: `[{"stage": "rule", "type": "accommodation_type_mismatch", "details": [{"date": "2026-05-12", "day_index": 4, "expected": "民宿", "got": "无住宿"}]}, {"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-05-12", "type": "dinner", "name": "无", "reason": "empty_or_none"}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "attraction_ticket_sum": 355, "expected_total_attractions": 710, "reported_total_attractions": 450, "expected_total_meals": 1910, "reported_total_meals": 480, "reported_total_transportation": 200}}]`

### v3_harder_eval_000014
- request: 成都 2026-06-03->2026-06-05 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆']
- errors: `[{"stage": "schema", "message": "1 validation error for TripPlan\ndays.2.accommodation\n  Input should be a valid string [type=string_type, input_value=None, input_type=NoneType]\n    For further information visit https://errors.pydantic.dev/2.12/v/string_type"}]`

### v3_harder_eval_000011
- request: 福州 2026-06-18->2026-06-21 days=4 transport=打车 hotel=高端酒店 prefs=['高端酒店', '艺术', '特色餐厅', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "attraction_ticket_sum": 50, "expected_total_attractions": 100, "reported_total_attractions": 1100, "expected_total_meals": 1624, "reported_total_meals": 1080, "reported_total_transportation": 400}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "attraction_ticket_sum": 50, "expected_total_attractions": 100, "reported_total_attractions": 1100, "expected_total_meals": 1624, "reported_total_meals": 1080, "reported_total_transportation": 400}}, {"stage": "rule", "type": "budget_preference_mismatch", "details": {"part_sum": 4830, "total": 4830, "diff": 0, "requested_budget": {"available": true, "amount": 8800, "scope": "total", "party_size": 2, "total": 8800, "source": "budget_constraint", "budget_level": "premium", "strictness": "soft"}, "per_person_day": 603.75, "budget_level": "premium", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "premium", "strictness": "soft", "amount": 8800, "target_min_ratio": 0.7, "target_max_ratio": 1.12, "target_min_total": 6200, "target_max_total": 9900, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": true, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 3, "priced_nights": 3, "expected_min_total_hotels": 2250, "reported_total_hotels": 2250, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_harder_eval_000018
- request: 天津 2026-07-03->2026-07-05 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "attraction_ticket_sum": 210, "expected_total_attractions": 630, "reported_total_attractions": 210, "expected_total_meals": 1167, "reported_total_meals": 720, "reported_total_transportation": 300}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "attraction_ticket_sum": 210, "expected_total_attractions": 630, "reported_total_attractions": 210, "expected_total_meals": 1167, "reported_total_meals": 720, "reported_total_transportation": 300}}]`

### v3_harder_eval_000012
- request: 洛阳 2025-05-04->2025-05-07 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '夜市', '老字号', '城市漫步']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2025-05-04", "lunch": "洛阳十字街小吃一条街", "dinner": "洛阳十字街小吃一条街"}, {"date": "2025-05-05", "lunch": "洛阳宴.洛阳菜(南昌路店)", "dinner": "洛阳宴.洛阳菜(南昌路店)"}, {"date": "2025-05-06", "lunch": "洛阳宴.洛阳菜(南昌路店)", "dinner": "洛阳宴.洛阳菜(南昌路店)"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "洛阳宴.洛阳菜", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2025-05-05", "type": "lunch", "name": "洛阳宴.洛阳菜(南昌路店)"}, {"date": "2025-05-05", "type": "dinner", "name": "洛阳宴.洛阳菜(南昌路店)"}, {"date": "2025-05-06", "type": "lunch", "name": "洛阳宴.洛阳菜(南昌路店)"}, {"date": "2025-05-06", "type": "dinner", "name": "洛阳宴.洛阳菜(南昌路店)"}, {"date": "2025-05-07", "type": "lunch", "name": "洛阳宴.洛阳菜(南昌路店)"}]}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "priced_nights": 3, "expected_min_total_hotels": 700, "reported_total_hotels": 900, "diff": 200, "covers_nights": false}}]`

### v3_harder_eval_000013
- request: 武汉 2026-05-06->2026-05-10 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "东湖生态旅游风景区", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-05-06", "day_index": 0, "name": "东湖生态旅游风景区"}, {"date": "2026-05-09", "day_index": 3, "name": "东湖生态旅游风景区"}]}, {"name_key": "解放公园", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-05-08", "day_index": 2, "name": "解放公园"}, {"date": "2026-05-10", "day_index": 4, "name": "解放公园"}]}]}, {"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-05-10", "type": "dinner", "name": "酒店晚餐", "reason": "generic_lodging_meal"}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "attraction_ticket_sum": 130, "expected_total_attractions": 260, "reported_total_attractions": 290, "expected_total_meals": 1368, "reported_total_meals": 660, "reported_total_transportation": 200}}]`

### v3_harder_eval_000019
- request: 丽江 2026-05-08->2026-05-11 days=4 transport=打车 hotel=亲子酒店 prefs=['亲子', '老人友好', '博物馆', '城市公园', '特色餐厅']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "attraction_ticket_sum": 320, "expected_total_attractions": 640, "reported_total_attractions": 240, "expected_total_meals": 1210, "reported_total_meals": 480, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "attraction_ticket_sum": 320, "expected_total_attractions": 640, "reported_total_attractions": 240, "expected_total_meals": 1210, "reported_total_meals": 480, "reported_total_transportation": 200}}, {"stage": "rule", "type": "budget_preference_mismatch", "details": {"part_sum": 2420, "total": 2420, "diff": 0, "requested_budget": {"available": true, "amount": 5300, "scope": "total", "party_size": 2, "total": 5300, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "soft"}, "per_person_day": 302.5, "budget_level": "comfortable", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "soft", "amount": 5300, "target_min_ratio": 0.65, "target_max_ratio": 1.05, "target_min_total": 3400, "target_max_total": 5600, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": true, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 3, "priced_nights": 3, "expected_min_total_hotels": 1500, "reported_total_hotels": 1500, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_harder_eval_000016
- request: 苏州 2026-06-03->2026-06-06 days=4 transport=自驾 hotel=亲子酒店 prefs=['亲子', '动物园', '海洋馆', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "稻山村·苏州菜", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-06-03", "type": "lunch", "name": "稻山村·苏州菜(石路店)"}, {"date": "2026-06-04", "type": "lunch", "name": "稻山村·苏州菜(石路店)"}, {"date": "2026-06-05", "type": "lunch", "name": "稻山村·苏州菜(石路店)"}, {"date": "2026-06-06", "type": "lunch", "name": "稻山村·苏州菜(石路店)"}]}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "priced_nights": 4, "expected_min_total_hotels": 5000, "reported_total_hotels": 3750, "diff": -1250, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "attraction_ticket_sum": 149, "expected_total_attractions": 447, "reported_total_attractions": 289, "expected_total_meals": 2163, "reported_total_meals": 1020, "reported_total_transportation": 400}}]`

### v3_harder_eval_000017
- request: 苏州 2026-05-06->2026-05-10 days=5 transport=公共交通 hotel=民宿 prefs=['小众展馆', '咖啡', '艺术', '城市漫步', '特色餐厅']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-05-08", "lunch": "江南雅厨·非遗苏州菜(李公堤店)", "dinner": "江南雅厨·非遗苏州菜(李公堤店)"}, {"date": "2026-05-10", "lunch": "江南雅厨·非遗苏州菜(李公堤店)", "dinner": "江南雅厨·非遗苏州菜(李公堤店)"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "江南雅厨·非遗苏州菜", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-05-08", "type": "lunch", "name": "江南雅厨·非遗苏州菜(李公堤店)"}, {"date": "2026-05-08", "type": "dinner", "name": "江南雅厨·非遗苏州菜(李公堤店)"}, {"date": "2026-05-09", "type": "dinner", "name": "江南雅厨·非遗苏州菜(李公堤店)"}, {"date": "2026-05-10", "type": "lunch", "name": "江南雅厨·非遗苏州菜(李公堤店)"}, {"date": "2026-05-10", "type": "dinner", "name": "江南雅厨·非遗苏州菜(李公堤店)"}]}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "attraction_ticket_sum": 195, "expected_total_attractions": 390, "reported_total_attractions": 330, "expected_total_meals": 2982, "reported_total_meals": 1128, "reported_total_transportation": 200}}]`

### v3_harder_eval_000010
- request: 西安 2026-04-20->2026-04-24 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "陕西历史博物馆", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-04-21", "day_index": 1, "name": "陕西历史博物馆"}, {"date": "2026-04-23", "day_index": 3, "name": "陕西历史博物馆"}]}, {"name_key": "陕西考古博物馆", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-04-22", "day_index": 2, "name": "陕西考古博物馆"}, {"date": "2026-04-24", "day_index": 4, "name": "陕西考古博物馆"}]}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "苏福记", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-04-21", "type": "lunch", "name": "苏福记(高新店)"}, {"date": "2026-04-22", "type": "lunch", "name": "苏福记(金萨店)"}, {"date": "2026-04-23", "type": "lunch", "name": "苏福记(高新店)"}, {"date": "2026-04-24", "type": "lunch", "name": "苏福记(金萨店)"}]}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 5, "attraction_ticket_sum": 200, "expected_total_attractions": 1000, "reported_total_attractions": 1200, "expected_total_meals": 2279, "reported_total_meals": 1230, "reported_total_transportation": 1000}}]`

### v3_harder_eval_000020
- request: 杭州 2026-06-18->2026-06-22 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-06-18", "type": "dinner", "name": "钱塘·萧山本帮菜(萧山机场大会展店)", "reason": "unknown_food_semantics"}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 5, "attraction_ticket_sum": 413, "expected_total_attractions": 2065, "reported_total_attractions": 1020, "expected_total_meals": 4520, "reported_total_meals": 1200, "reported_total_transportation": 1000}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 5, "attraction_ticket_sum": 413, "expected_total_attractions": 2065, "reported_total_attractions": 1020, "expected_total_meals": 4520, "reported_total_meals": 1200, "reported_total_transportation": 1000}}]`
