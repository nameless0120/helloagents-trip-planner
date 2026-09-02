# Rule Eval Report: base_qwen25_7b_v3_ctx_balanced_topk_w10_room_person_eval

- records: 300
- generations: `training/outputs/eval/base_qwen25_7b_v3_ctx_balanced_topk_w10/generations.jsonl`
- records_path: `training/data/v3/context_ablation/balanced_baseline_topk_context/records.jsonl`

## Boolean Metrics

| Metric | Pass | Total | Rate |
| --- | ---: | ---: | ---: |
| accommodation_type_ok | 258 | 296 | 87.16% |
| attraction_budget_consistent | 18 | 296 | 6.08% |
| attraction_budget_party_relation_ok | 74 | 296 | 25.00% |
| attraction_count_ok | 296 | 296 | 100.00% |
| attraction_diversity_ok | 254 | 296 | 85.81% |
| attraction_grounding_ok | 288 | 296 | 97.30% |
| attraction_repeat_limit_ok | 254 | 296 | 85.81% |
| budget_arithmetic_consistent | 200 | 296 | 67.57% |
| budget_consistent | 200 | 296 | 67.57% |
| budget_level_aligned | 123 | 296 | 41.55% |
| budget_preference_aligned | 123 | 296 | 41.55% |
| budget_relationship_ok | 18 | 296 | 6.08% |
| budget_user_constraint_ok | 247 | 296 | 83.45% |
| budget_within_user_budget | 286 | 296 | 96.62% |
| city_ok | 296 | 296 | 100.00% |
| date_range_ok | 296 | 296 | 100.00% |
| day_dates_ok | 296 | 296 | 100.00% |
| day_index_ok | 296 | 296 | 100.00% |
| days_len_ok | 296 | 296 | 100.00% |
| dpo_soft_pass | 0 | 296 | 0.00% |
| hard_pass | 0 | 296 | 0.00% |
| hotel_budget_covers_nights | 112 | 296 | 37.84% |
| hotel_budget_relation_ok | 118 | 296 | 39.86% |
| hotel_distance_placeholder_ok | 296 | 296 | 100.00% |
| hotel_grounding_ok | 296 | 296 | 100.00% |
| invalid_hotel_name_ok | 296 | 296 | 100.00% |
| json_extract_ok | 299 | 300 | 99.67% |
| legacy_hard_pass | 42 | 296 | 14.19% |
| location_object_ok | 296 | 296 | 100.00% |
| meal_budget_consistent | 0 | 296 | 0.00% |
| meal_complete | 296 | 296 | 100.00% |
| meal_cost_scale_ok | 231 | 296 | 78.04% |
| meal_diversity_ok | 167 | 296 | 56.42% |
| meal_grounding_ok | 255 | 296 | 86.15% |
| meal_lunch_dinner_same_day_ok | 221 | 296 | 74.66% |
| meal_repeat_limit_ok | 195 | 296 | 65.88% |
| meal_specific_ok | 294 | 296 | 99.32% |
| meal_valid_semantics_ok | 259 | 296 | 87.50% |
| middle_hotel_ok | 295 | 296 | 99.66% |
| schema_ok | 296 | 300 | 98.67% |
| sft_budget_semantic_hard_pass | 12 | 296 | 4.05% |
| sft_hard_pass | 0 | 296 | 0.00% |
| transportation_budget_nonnegative | 296 | 296 | 100.00% |
| weather_dates_ok | 296 | 296 | 100.00% |
| weather_match | 296 | 296 | 100.00% |

## Numeric Metrics

```json
{
  "attraction_diversity_unique_rate": {
    "avg": 0.9738,
    "p50": 1.0,
    "p90": 1.0
  },
  "attraction_grounding_rate": {
    "avg": 0.9956,
    "p50": 1.0,
    "p90": 1.0
  },
  "hotel_grounding_rate": {
    "avg": 1.0,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_diversity_unique_rate": {
    "avg": 0.7026,
    "p50": 0.75,
    "p90": 1.0
  },
  "meal_food_pois_grounding_rate": {
    "avg": 0.9823,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_grounding_rate": {
    "avg": 0.9823,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_semantic_valid_rate": {
    "avg": 0.9838,
    "p50": 1.0,
    "p90": 1.0
  }
}
```

## Failure Types

```json
{
  "meal_budget_inconsistent": 296,
  "attraction_budget_inconsistent": 278,
  "budget_relationship_mismatch": 278,
  "hotel_budget_underestimated": 184,
  "budget_preference_mismatch": 173,
  "meal_repeat_too_many": 101,
  "budget_arithmetic_inconsistent": 96,
  "meal_same_day_lunch_dinner_repeat": 75,
  "meal_cost_scale_too_low": 65,
  "budget_hard_constraint_exceeded": 49,
  "attraction_repeat_too_many": 42,
  "accommodation_type_mismatch": 38,
  "meal_invalid_name": 37,
  "meal_grounding_miss": 4,
  "schema": 3,
  "meal_placeholder": 2,
  "json_extract": 1,
  "middle_hotel_null": 1
}
```

## Failure Examples

### v3_harder_eval_000004
- request: 张家界 2026-05-08->2026-05-10 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-05-08", "lunch": "索溪山寨·湘西民间土菜(标志门店)", "dinner": "索溪山寨·湘西民间土菜(标志门店)"}, {"date": "2026-05-09", "lunch": "刘聋子粉馆(张家界总店)", "dinner": "刘聋子粉馆(张家界总店)"}, {"date": "2026-05-10", "lunch": "大队老渔村", "dinner": "大队老渔村"}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 2, "party_total": 1, "room_count": 1, "priced_nights": 2, "expected_min_total_hotels": 800, "reported_total_hotels": 1200, "diff": 400, "covers_nights": false}}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 1910, "total": 1810, "diff": 100, "requested_budget": {"available": true, "amount": 1700, "scope": "total", "party_size": 1, "total": 1700, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "hard"}, "per_person_day": 603.33, "budget_level": "comfortable", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "hard", "amount": 1700, "target_min_ratio": 0.65, "target_max_ratio": 1.0, "target_min_total": 1100, "target_max_total": 1700, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": false, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 1, "room_count": 1, "priced_nights": 2, "expected_min_total_hotels": 800, "reported_total_hotels": 1200, "diff": 400, "covers_nights": false}, "hotel_budget_covers_nights": false}}]`

### v3_harder_eval_000008
- request: 大理 2026-05-08->2026-05-10 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "南诏村·现炒云南菜", "count": 3, "max_allowed": 2, "occurrences": [{"date": "2026-05-08", "type": "lunch", "name": "南诏村·现炒云南菜"}, {"date": "2026-05-09", "type": "lunch", "name": "南诏村·现炒云南菜"}, {"date": "2026-05-10", "type": "lunch", "name": "南诏村·现炒云南菜"}]}, {"name_key": "桃红小馆·特色云南菜·庭院花园餐厅", "count": 3, "max_allowed": 2, "occurrences": [{"date": "2026-05-08", "type": "dinner", "name": "桃红小馆·特色云南菜·庭院花园餐厅"}, {"date": "2026-05-09", "type": "dinner", "name": "桃红小馆·特色云南菜·庭院花园餐厅"}, {"date": "2026-05-10", "type": "dinner", "name": "桃红小馆·特色云南菜·庭院花园餐厅"}]}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 2, "party_total": 3, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 4500, "reported_total_hotels": 2250, "diff": -2250, "covers_nights": false}}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 3669, "total": 3619, "diff": 50, "requested_budget": {"available": true, "amount": 5800, "scope": "total", "party_size": 3, "total": 5800, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "hard"}, "per_person_day": 402.11, "budget_level": "comfortable", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "hard", "amount": 5800, "target_min_ratio": 0.65, "target_max_ratio": 1.0, "target_min_total": 3800, "target_max_total": 5800, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 3, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 4500, "reported_total_hotels": 2250, "diff": -2250, "covers_nights": false}, "hotel_budget_covers_nights": false}}]`

### v3_harder_eval_000001
- request: 桂林 2026-09-01->2026-09-04 days=4 transport=打车 hotel=高端酒店 prefs=['高端酒店', '艺术', '特色餐厅', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-09-01", "lunch": "椿记烧鹅(中山店)", "dinner": "椿记烧鹅(西街店)"}, {"date": "2026-09-04", "lunch": "椿记烧鹅(中山店)", "dinner": "椿记烧鹅(西街店)"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "椿记烧鹅", "count": 6, "max_allowed": 3, "occurrences": [{"date": "2026-09-01", "type": "lunch", "name": "椿记烧鹅(中山店)"}, {"date": "2026-09-01", "type": "dinner", "name": "椿记烧鹅(西街店)"}, {"date": "2026-09-02", "type": "lunch", "name": "椿记烧鹅(西街店)"}, {"date": "2026-09-03", "type": "lunch", "name": "椿记烧鹅(南溪店)"}, {"date": "2026-09-04", "type": "lunch", "name": "椿记烧鹅(中山店)"}, {"date": "2026-09-04", "type": "dinner", "name": "椿记烧鹅(西街店)"}]}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 625, "expected_total_attractions": 1250, "reported_total_attractions": 830, "meal_per_person_cost_sum": 1026, "expected_total_meals": 2052, "reported_total_meals": 360, "reported_total_transportation": 400}}]`

### v3_harder_eval_000006
- request: 南京 2026-07-03->2026-07-06 days=4 transport=自驾 hotel=亲子酒店 prefs=['亲子', '动物园', '海洋馆', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 3, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 3300, "reported_total_hotels": 1650, "diff": -1650, "covers_nights": false}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 35, "expected_total_attractions": 105, "reported_total_attractions": 105, "meal_per_person_cost_sum": 1836, "expected_total_meals": 5508, "reported_total_meals": 720, "reported_total_transportation": 200}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": false, "attraction_budget_party_relation_ok": true, "meal_cost_scale_ok": true, "budget_relationship_ok": false, "expected_total_hotels": 3300, "reported_total_hotels": 1650, "expected_total_attractions": 105, "reported_total_attractions": 105, "meal_scale_eval": {"ok": true, "party_total": 3, "budget_level": "standard", "per_person_lunch_dinner_floor": 35, "per_person_breakfast_floor": 14, "meal_count": 12, "checked_count": 8, "failure_count": 0, "failures": []}}}]`

### v3_harder_eval_000005
- request: 广州 2026-07-03->2026-07-07 days=5 transport=公共交通 hotel=民宿 prefs=['摄影', '自然风光', '城市漫步', '本地菜']
- errors: `[{"stage": "rule", "type": "meal_grounding_miss", "details": [{"date": "2026-07-07", "type": "lunch", "name": "大佛寺附近的茶餐厅"}]}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 2990, "total": 2090, "diff": 900, "requested_budget": {"available": true, "amount": 2600, "scope": "total", "party_size": 1, "total": 2600, "source": "budget_constraint", "budget_level": "standard", "strictness": "hard"}, "per_person_day": 418.0, "budget_level": "standard", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "standard", "strictness": "hard", "amount": 2600, "target_min_ratio": 0.55, "target_max_ratio": 1.0, "target_min_total": 1400, "target_max_total": 2600, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 4, "party_total": 1, "room_count": 1, "priced_nights": 4, "expected_min_total_hotels": 1200, "reported_total_hotels": 1200, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 615, "expected_total_attractions": 615, "reported_total_attractions": 1110, "meal_per_person_cost_sum": 1118, "expected_total_meals": 1118, "reported_total_meals": 480, "reported_total_transportation": 200}}]`

### v3_harder_eval_000002
- request: 杭州 2026-04-28->2026-05-01 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '夜市', '老字号', '城市漫步']
- errors: `[{"stage": "rule", "type": "meal_grounding_miss", "details": [{"date": "2026-04-29", "type": "dinner", "name": "爬屿·爬宠异宠体验馆(武林夜市店)"}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 4, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 1500, "reported_total_hotels": 750, "diff": -750, "covers_nights": false}}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 3170, "total": 2770, "diff": 400, "requested_budget": {"available": true, "amount": 3100, "scope": "total", "party_size": 4, "total": 3100, "source": "budget_constraint", "budget_level": "limited", "strictness": "hard"}, "per_person_day": 173.12, "budget_level": "limited", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "limited", "strictness": "hard", "amount": 3100, "target_min_ratio": 0.72, "target_max_ratio": 1.0, "target_min_total": 2200, "target_max_total": 3100, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 4, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 1500, "reported_total_hotels": 750, "diff": -750, "covers_nights": false}, "hotel_budget_covers_nights": false}}]`

### v3_harder_eval_000009
- request: 苏州 2026-04-27->2026-04-30 days=4 transport=打车 hotel=亲子酒店 prefs=['亲子', '老人友好', '博物馆', '城市公园', '特色餐厅']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "万福兴", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-04-27", "type": "lunch", "name": "万福兴(东中市总店)"}, {"date": "2026-04-28", "type": "dinner", "name": "万福兴(东中市总店)"}, {"date": "2026-04-29", "type": "dinner", "name": "万福兴(东中市总店)"}, {"date": "2026-04-30", "type": "dinner", "name": "万福兴(东中市总店)"}]}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 4, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 7500, "reported_total_hotels": 3750, "diff": -3750, "covers_nights": false}}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 5955, "total": 6355, "diff": -400, "requested_budget": {"available": true, "amount": 9100, "scope": "total", "party_size": 4, "total": 9100, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "soft"}, "per_person_day": 397.19, "budget_level": "comfortable", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "soft", "amount": 9100, "target_min_ratio": 0.65, "target_max_ratio": 1.05, "target_min_total": 5900, "target_max_total": 9600, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 4, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 7500, "reported_total_hotels": 3750, "diff": -3750, "covers_nights": false}, "hotel_budget_covers_nights": false}}]`

### v3_harder_eval_000000
- request: 昆明 2026-04-04->2026-04-08 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 4, "party_total": 5, "room_count": 3, "priced_nights": 4, "expected_min_total_hotels": 4800, "reported_total_hotels": 1600, "diff": -3200, "covers_nights": false}}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 4978, "total": 5978, "diff": -1000, "requested_budget": {"available": true, "amount": 12800, "scope": "total", "party_size": 5, "total": 12800, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "hard"}, "per_person_day": 239.12, "budget_level": "comfortable", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "hard", "amount": 12800, "target_min_ratio": 0.65, "target_max_ratio": 1.0, "target_min_total": 8300, "target_max_total": 12800, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 4, "party_total": 5, "room_count": 3, "priced_nights": 4, "expected_min_total_hotels": 4800, "reported_total_hotels": 1600, "diff": -3200, "covers_nights": false}, "hotel_budget_covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 5, "hotel_room_count": 3, "attraction_ticket_sum": 332, "expected_total_attractions": 1660, "reported_total_attractions": 1178, "meal_per_person_cost_sum": 2360, "expected_total_meals": 11800, "reported_total_meals": 1200, "reported_total_transportation": 1000}}]`

### v3_harder_eval_000007
- request: 成都 2026-05-08->2026-05-12 days=5 transport=公共交通 hotel=民宿 prefs=['小众展馆', '咖啡', '艺术', '城市漫步', '特色餐厅']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "都江堰景区", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-05-11", "day_index": 3, "name": "都江堰景区"}, {"date": "2026-05-12", "day_index": 4, "name": "都江堰景区"}]}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 355, "expected_total_attractions": 710, "reported_total_attractions": 1010, "meal_per_person_cost_sum": 2176, "expected_total_meals": 4352, "reported_total_meals": 960, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 355, "expected_total_attractions": 710, "reported_total_attractions": 1010, "meal_per_person_cost_sum": 2176, "expected_total_meals": 4352, "reported_total_meals": 960, "reported_total_transportation": 200}}]`

### v3_harder_eval_000003
- request: 西安 2025-05-04->2025-05-08 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 2960, "total": 3760, "diff": -800, "requested_budget": {"available": true, "amount": 3700, "scope": "total", "party_size": 2, "total": 3700, "source": "budget_constraint", "budget_level": "standard", "strictness": "hard"}, "per_person_day": 376.0, "budget_level": "standard", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "standard", "strictness": "hard", "amount": 3700, "target_min_ratio": 0.55, "target_max_ratio": 1.0, "target_min_total": 2000, "target_max_total": 3700, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": false, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 4, "party_total": 2, "room_count": 1, "priced_nights": 4, "expected_min_total_hotels": 1800, "reported_total_hotels": 1800, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 170, "expected_total_attractions": 340, "reported_total_attractions": 480, "meal_per_person_cost_sum": 950, "expected_total_meals": 1900, "reported_total_meals": 480, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 170, "expected_total_attractions": 340, "reported_total_attractions": 480, "meal_per_person_cost_sum": 950, "expected_total_meals": 1900, "reported_total_meals": 480, "reported_total_transportation": 200}}]`

### v3_harder_eval_000014
- request: 成都 2026-06-03->2026-06-05 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 2, "party_total": 1, "room_count": 1, "priced_nights": 2, "expected_min_total_hotels": 900, "reported_total_hotels": 1350, "diff": 450, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 115, "expected_total_attractions": 115, "reported_total_attractions": 175, "meal_per_person_cost_sum": 749, "expected_total_meals": 749, "reported_total_meals": 450, "reported_total_transportation": 300}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 115, "expected_total_attractions": 115, "reported_total_attractions": 175, "meal_per_person_cost_sum": 749, "expected_total_meals": 749, "reported_total_meals": 450, "reported_total_transportation": 300}}]`

### v3_harder_eval_000011
- request: 福州 2026-06-18->2026-06-21 days=4 transport=打车 hotel=高端酒店 prefs=['高端酒店', '艺术', '特色餐厅', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 50, "expected_total_attractions": 100, "reported_total_attractions": 674, "meal_per_person_cost_sum": 2054, "expected_total_meals": 4108, "reported_total_meals": 1020, "reported_total_transportation": 800}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 50, "expected_total_attractions": 100, "reported_total_attractions": 674, "meal_per_person_cost_sum": 2054, "expected_total_meals": 4108, "reported_total_meals": 1020, "reported_total_transportation": 800}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": false, "meal_cost_scale_ok": true, "budget_relationship_ok": false, "expected_total_hotels": 2250, "reported_total_hotels": 2250, "expected_total_attractions": 100, "reported_total_attractions": 674, "meal_scale_eval": {"ok": true, "party_total": 2, "budget_level": "premium", "per_person_lunch_dinner_floor": 70, "per_person_breakfast_floor": 28, "meal_count": 12, "checked_count": 8, "failure_count": 0, "failures": []}}}]`

### v3_harder_eval_000013
- request: 武汉 2026-05-06->2026-05-10 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 3030, "total": 2930, "diff": 100, "requested_budget": {"available": true, "amount": 3900, "scope": "total", "party_size": 2, "total": 3900, "source": "budget_constraint", "budget_level": "standard", "strictness": "hard"}, "per_person_day": 293.0, "budget_level": "standard", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "standard", "strictness": "hard", "amount": 3900, "target_min_ratio": 0.55, "target_max_ratio": 1.0, "target_min_total": 2100, "target_max_total": 3900, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 4, "party_total": 2, "room_count": 1, "priced_nights": 4, "expected_min_total_hotels": 1600, "reported_total_hotels": 1600, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 130, "expected_total_attractions": 260, "reported_total_attractions": 210, "meal_per_person_cost_sum": 1474, "expected_total_meals": 2948, "reported_total_meals": 1020, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 130, "expected_total_attractions": 260, "reported_total_attractions": 210, "meal_per_person_cost_sum": 1474, "expected_total_meals": 2948, "reported_total_meals": 1020, "reported_total_transportation": 200}}]`

### v3_harder_eval_000018
- request: 天津 2026-07-03->2026-07-05 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 2, "party_total": 3, "room_count": 2, "priced_nights": 2, "expected_min_total_hotels": 4800, "reported_total_hotels": 2400, "diff": -2400, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 210, "expected_total_attractions": 630, "reported_total_attractions": 210, "meal_per_person_cost_sum": 1281, "expected_total_meals": 3843, "reported_total_meals": 780, "reported_total_transportation": 300}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 210, "expected_total_attractions": 630, "reported_total_attractions": 210, "meal_per_person_cost_sum": 1281, "expected_total_meals": 3843, "reported_total_meals": 780, "reported_total_transportation": 300}}]`

### v3_harder_eval_000019
- request: 丽江 2026-05-08->2026-05-11 days=4 transport=打车 hotel=亲子酒店 prefs=['亲子', '老人友好', '博物馆', '城市公园', '特色餐厅']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 320, "expected_total_attractions": 640, "reported_total_attractions": 240, "meal_per_person_cost_sum": 1204, "expected_total_meals": 2408, "reported_total_meals": 480, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 320, "expected_total_attractions": 640, "reported_total_attractions": 240, "meal_per_person_cost_sum": 1204, "expected_total_meals": 2408, "reported_total_meals": 480, "reported_total_transportation": 200}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": false, "meal_cost_scale_ok": true, "budget_relationship_ok": false, "expected_total_hotels": 1500, "reported_total_hotels": 1500, "expected_total_attractions": 640, "reported_total_attractions": 240, "meal_scale_eval": {"ok": true, "party_total": 2, "budget_level": "comfortable", "per_person_lunch_dinner_floor": 50, "per_person_breakfast_floor": 20, "meal_count": 12, "checked_count": 8, "failure_count": 0, "failures": []}}}]`

### v3_harder_eval_000012
- request: 洛阳 2025-05-04->2025-05-07 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '夜市', '老字号', '城市漫步']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2025-05-04", "lunch": "洛阳十字街小吃一条街", "dinner": "洛阳十字街小吃一条街"}, {"date": "2025-05-05", "lunch": "洛阳宴.洛阳菜(南昌路店)", "dinner": "洛阳宴.洛阳菜(南昌路店)"}, {"date": "2025-05-06", "lunch": "洛阳宴.洛阳菜(南昌路店)", "dinner": "洛阳宴.洛阳菜(南昌路店)"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "洛阳宴.洛阳菜", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2025-05-05", "type": "lunch", "name": "洛阳宴.洛阳菜(南昌路店)"}, {"date": "2025-05-05", "type": "dinner", "name": "洛阳宴.洛阳菜(南昌路店)"}, {"date": "2025-05-06", "type": "lunch", "name": "洛阳宴.洛阳菜(南昌路店)"}, {"date": "2025-05-06", "type": "dinner", "name": "洛阳宴.洛阳菜(南昌路店)"}, {"date": "2025-05-07", "type": "lunch", "name": "洛阳宴.洛阳菜(南昌路店)"}]}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 4, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 1400, "reported_total_hotels": 1200, "diff": -200, "covers_nights": false}}]`

### v3_harder_eval_000016
- request: 苏州 2026-06-03->2026-06-06 days=4 transport=自驾 hotel=亲子酒店 prefs=['亲子', '动物园', '海洋馆', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 3, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 7500, "reported_total_hotels": 3750, "diff": -3750, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 289, "expected_total_attractions": 867, "reported_total_attractions": 1000, "meal_per_person_cost_sum": 2265, "expected_total_meals": 6795, "reported_total_meals": 1440, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 289, "expected_total_attractions": 867, "reported_total_attractions": 1000, "meal_per_person_cost_sum": 2265, "expected_total_meals": 6795, "reported_total_meals": 1440, "reported_total_transportation": 200}}]`

### v3_harder_eval_000010
- request: 西安 2026-04-20->2026-04-24 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-04-24", "lunch": "清真刚刚烤肉(小南门店)", "dinner": "清真刚刚烤肉(小南门店)"}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 4, "party_total": 5, "room_count": 3, "priced_nights": 4, "expected_min_total_hotels": 5400, "reported_total_hotels": 2250, "diff": -3150, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 5, "hotel_room_count": 3, "attraction_ticket_sum": 257, "expected_total_attractions": 1285, "reported_total_attractions": 510, "meal_per_person_cost_sum": 2745, "expected_total_meals": 13725, "reported_total_meals": 1200, "reported_total_transportation": 1000}}]`

### v3_harder_eval_000017
- request: 苏州 2026-05-06->2026-05-10 days=5 transport=公共交通 hotel=民宿 prefs=['小众展馆', '咖啡', '艺术', '城市漫步', '特色餐厅']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "秋娟馄饨店", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-05-06", "type": "breakfast", "name": "秋娟馄饨店"}, {"date": "2026-05-07", "type": "breakfast", "name": "秋娟馄饨店"}, {"date": "2026-05-08", "type": "breakfast", "name": "秋娟馄饨店"}, {"date": "2026-05-09", "type": "breakfast", "name": "秋娟馄饨店"}, {"date": "2026-05-10", "type": "breakfast", "name": "秋娟馄饨店"}]}, {"name_key": "老横泾面馆", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-05-06", "type": "lunch", "name": "老横泾面馆(吴中横泾总店)"}, {"date": "2026-05-07", "type": "lunch", "name": "老横泾面馆(吴中横泾总店)"}, {"date": "2026-05-08", "type": "lunch", "name": "老横泾面馆(吴中横泾总店)"}, {"date": "2026-05-09", "type": "lunch", "name": "老横泾面馆(吴中横泾总店)"}, {"date": "2026-05-10", "type": "lunch", "name": "老横泾面馆(吴中横泾总店)"}]}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 205, "expected_total_attractions": 410, "reported_total_attractions": 1000, "meal_per_person_cost_sum": 1790, "expected_total_meals": 3580, "reported_total_meals": 1440, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 205, "expected_total_attractions": 410, "reported_total_attractions": 1000, "meal_per_person_cost_sum": 1790, "expected_total_meals": 3580, "reported_total_meals": 1440, "reported_total_transportation": 200}}]`

### v3_harder_eval_000020
- request: 杭州 2026-06-18->2026-06-22 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 4, "party_total": 5, "room_count": 3, "priced_nights": 4, "expected_min_total_hotels": 6000, "reported_total_hotels": 2000, "diff": -4000, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 5, "hotel_room_count": 3, "attraction_ticket_sum": 568, "expected_total_attractions": 2840, "reported_total_attractions": 1110, "meal_per_person_cost_sum": 4770, "expected_total_meals": 23850, "reported_total_meals": 1530, "reported_total_transportation": 1000}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 5, "hotel_room_count": 3, "attraction_ticket_sum": 568, "expected_total_attractions": 2840, "reported_total_attractions": 1110, "meal_per_person_cost_sum": 4770, "expected_total_meals": 23850, "reported_total_meals": 1530, "reported_total_transportation": 1000}}]`
