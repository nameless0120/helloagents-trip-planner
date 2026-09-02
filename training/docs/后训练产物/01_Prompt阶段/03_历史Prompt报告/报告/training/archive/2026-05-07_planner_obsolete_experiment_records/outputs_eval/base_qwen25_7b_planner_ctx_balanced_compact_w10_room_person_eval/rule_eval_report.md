# Rule Eval Report: base_qwen25_7b_v3_ctx_balanced_compact_w10_room_person_eval

- records: 300
- generations: `training/outputs/eval/base_qwen25_7b_v3_ctx_balanced_compact_w10/generations.jsonl`
- records_path: `training/data/v3/context_ablation/balanced_baseline_compact_context/records.jsonl`

## Boolean Metrics

| Metric | Pass | Total | Rate |
| --- | ---: | ---: | ---: |
| accommodation_type_ok | 231 | 296 | 78.04% |
| attraction_budget_consistent | 33 | 296 | 11.15% |
| attraction_budget_party_relation_ok | 72 | 296 | 24.32% |
| attraction_count_ok | 296 | 296 | 100.00% |
| attraction_diversity_ok | 266 | 296 | 89.86% |
| attraction_grounding_ok | 292 | 296 | 98.65% |
| attraction_repeat_limit_ok | 266 | 296 | 89.86% |
| budget_arithmetic_consistent | 196 | 296 | 66.22% |
| budget_consistent | 196 | 296 | 66.22% |
| budget_level_aligned | 123 | 296 | 41.55% |
| budget_preference_aligned | 123 | 296 | 41.55% |
| budget_relationship_ok | 18 | 296 | 6.08% |
| budget_user_constraint_ok | 245 | 296 | 82.77% |
| budget_within_user_budget | 287 | 296 | 96.96% |
| city_ok | 296 | 296 | 100.00% |
| date_range_ok | 296 | 296 | 100.00% |
| day_dates_ok | 296 | 296 | 100.00% |
| day_index_ok | 296 | 296 | 100.00% |
| days_len_ok | 296 | 296 | 100.00% |
| dpo_soft_pass | 0 | 296 | 0.00% |
| hard_pass | 0 | 296 | 0.00% |
| hotel_budget_covers_nights | 114 | 296 | 38.51% |
| hotel_budget_relation_ok | 120 | 296 | 40.54% |
| hotel_distance_placeholder_ok | 296 | 296 | 100.00% |
| hotel_grounding_ok | 296 | 296 | 100.00% |
| invalid_hotel_name_ok | 296 | 296 | 100.00% |
| json_extract_ok | 299 | 300 | 99.67% |
| legacy_hard_pass | 37 | 296 | 12.50% |
| location_object_ok | 296 | 296 | 100.00% |
| meal_budget_consistent | 0 | 296 | 0.00% |
| meal_complete | 296 | 296 | 100.00% |
| meal_cost_scale_ok | 227 | 296 | 76.69% |
| meal_diversity_ok | 145 | 296 | 48.99% |
| meal_grounding_ok | 268 | 296 | 90.54% |
| meal_lunch_dinner_same_day_ok | 211 | 296 | 71.28% |
| meal_repeat_limit_ok | 177 | 296 | 59.80% |
| meal_specific_ok | 296 | 296 | 100.00% |
| meal_valid_semantics_ok | 269 | 296 | 90.88% |
| middle_hotel_ok | 296 | 296 | 100.00% |
| schema_ok | 296 | 300 | 98.67% |
| sft_budget_semantic_hard_pass | 11 | 296 | 3.72% |
| sft_hard_pass | 0 | 296 | 0.00% |
| transportation_budget_nonnegative | 296 | 296 | 100.00% |
| weather_dates_ok | 296 | 296 | 100.00% |
| weather_match | 296 | 296 | 100.00% |

## Numeric Metrics

```json
{
  "attraction_diversity_unique_rate": {
    "avg": 0.9793,
    "p50": 1.0,
    "p90": 1.0
  },
  "attraction_grounding_rate": {
    "avg": 0.9974,
    "p50": 1.0,
    "p90": 1.0
  },
  "hotel_grounding_rate": {
    "avg": 1.0,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_diversity_unique_rate": {
    "avg": 0.6802,
    "p50": 0.7,
    "p90": 1.0
  },
  "meal_food_pois_grounding_rate": {
    "avg": 0.9845,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_grounding_rate": {
    "avg": 0.9845,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_semantic_valid_rate": {
    "avg": 0.9854,
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
  "attraction_budget_inconsistent": 263,
  "hotel_budget_underestimated": 182,
  "budget_preference_mismatch": 173,
  "meal_repeat_too_many": 119,
  "budget_arithmetic_inconsistent": 100,
  "meal_same_day_lunch_dinner_repeat": 85,
  "meal_cost_scale_too_low": 69,
  "accommodation_type_mismatch": 65,
  "budget_hard_constraint_exceeded": 51,
  "attraction_repeat_too_many": 30,
  "meal_invalid_name": 27,
  "schema": 3,
  "json_extract": 1,
  "meal_grounding_miss": 1
}
```

## Failure Examples

### v3_harder_eval_000008
- request: 大理 2026-05-08->2026-05-10 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "大理古城", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-05-08", "day_index": 0, "name": "大理古城"}, {"date": "2026-05-10", "day_index": 2, "name": "大理古城"}]}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 2, "party_total": 3, "room_count": 2, "priced_nights": 2, "expected_min_total_hotels": 3000, "reported_total_hotels": 2250, "diff": -750, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 0, "expected_total_attractions": 0, "reported_total_attractions": 1200, "meal_per_person_cost_sum": 1026, "expected_total_meals": 3078, "reported_total_meals": 1440, "reported_total_transportation": 300}}]`

### v3_harder_eval_000004
- request: 张家界 2026-05-08->2026-05-10 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆']
- errors: `[{"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-05-08", "type": "dinner", "name": "酒店晚餐", "reason": "generic_lodging_meal"}, {"date": "2026-05-09", "type": "dinner", "name": "酒店晚餐", "reason": "generic_lodging_meal"}, {"date": "2026-05-10", "type": "dinner", "name": "酒店晚餐", "reason": "generic_lodging_meal"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "酒店晚餐", "count": 3, "max_allowed": 2, "occurrences": [{"date": "2026-05-08", "type": "dinner", "name": "酒店晚餐"}, {"date": "2026-05-09", "type": "dinner", "name": "酒店晚餐"}, {"date": "2026-05-10", "type": "dinner", "name": "酒店晚餐"}]}]}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 0, "expected_total_attractions": 0, "reported_total_attractions": 0, "meal_per_person_cost_sum": 400, "expected_total_meals": 400, "reported_total_meals": 450, "reported_total_transportation": 200}}]`

### v3_harder_eval_000002
- request: 杭州 2026-04-28->2026-05-01 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '夜市', '老字号', '城市漫步']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 4, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 1500, "reported_total_hotels": 750, "diff": -750, "covers_nights": false}}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 3130, "total": 2930, "diff": 200, "requested_budget": {"available": true, "amount": 3100, "scope": "total", "party_size": 4, "total": 3100, "source": "budget_constraint", "budget_level": "limited", "strictness": "hard"}, "per_person_day": 183.12, "budget_level": "limited", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "limited", "strictness": "hard", "amount": 3100, "target_min_ratio": 0.72, "target_max_ratio": 1.0, "target_min_total": 2200, "target_max_total": 3100, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 4, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 1500, "reported_total_hotels": 750, "diff": -750, "covers_nights": false}, "hotel_budget_covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 280, "expected_total_attractions": 1120, "reported_total_attractions": 1100, "meal_per_person_cost_sum": 1768, "expected_total_meals": 7072, "reported_total_meals": 1080, "reported_total_transportation": 200}}]`

### v3_harder_eval_000006
- request: 南京 2026-07-03->2026-07-06 days=4 transport=自驾 hotel=亲子酒店 prefs=['亲子', '动物园', '海洋馆', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "accommodation_type_mismatch", "details": [{"date": "2026-07-06", "day_index": 3, "expected": "亲子酒店", "got": "无住宿"}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 3, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 3300, "reported_total_hotels": 1650, "diff": -1650, "covers_nights": false}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 0, "expected_total_attractions": 0, "reported_total_attractions": 0, "meal_per_person_cost_sum": 1701, "expected_total_meals": 5103, "reported_total_meals": 810, "reported_total_transportation": 200}}]`

### v3_harder_eval_000009
- request: 苏州 2026-04-27->2026-04-30 days=4 transport=打车 hotel=亲子酒店 prefs=['亲子', '老人友好', '博物馆', '城市公园', '特色餐厅']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 4, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 7500, "reported_total_hotels": 3750, "diff": -3750, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 215, "expected_total_attractions": 860, "reported_total_attractions": 265, "meal_per_person_cost_sum": 3404, "expected_total_meals": 13616, "reported_total_meals": 2832, "reported_total_transportation": 800}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 215, "expected_total_attractions": 860, "reported_total_attractions": 265, "meal_per_person_cost_sum": 3404, "expected_total_meals": 13616, "reported_total_meals": 2832, "reported_total_transportation": 800}}]`

### v3_harder_eval_000001
- request: 桂林 2026-09-01->2026-09-04 days=4 transport=打车 hotel=高端酒店 prefs=['高端酒店', '艺术', '特色餐厅', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-09-04", "type": "dinner", "name": "画馨酒店(十里画廊遇龙河店)餐厅", "reason": "hotel_or_lodging_name"}]}, {"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-09-01", "lunch": "椿记烧鹅(中山店)", "dinner": "椿记烧鹅(西街店)"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "椿记烧鹅", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-09-01", "type": "lunch", "name": "椿记烧鹅(中山店)"}, {"date": "2026-09-01", "type": "dinner", "name": "椿记烧鹅(西街店)"}, {"date": "2026-09-02", "type": "lunch", "name": "椿记烧鹅(西街店)"}, {"date": "2026-09-03", "type": "lunch", "name": "椿记烧鹅(西街店)"}, {"date": "2026-09-04", "type": "lunch", "name": "椿记烧鹅(西街店)"}]}]}]`

### v3_harder_eval_000007
- request: 成都 2026-05-08->2026-05-12 days=5 transport=公共交通 hotel=民宿 prefs=['小众展馆', '咖啡', '艺术', '城市漫步', '特色餐厅']
- errors: `[{"stage": "rule", "type": "accommodation_type_mismatch", "details": [{"date": "2026-05-12", "day_index": 4, "expected": "民宿", "got": "无住宿"}]}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 2130, "total": 2030, "diff": 100, "requested_budget": {"available": true, "amount": 7000, "scope": "total", "party_size": 2, "total": 7000, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "soft"}, "per_person_day": 203.0, "budget_level": "comfortable", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "soft", "amount": 7000, "target_min_ratio": 0.65, "target_max_ratio": 1.05, "target_min_total": 4600, "target_max_total": 7400, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 4, "party_total": 2, "room_count": 1, "priced_nights": 4, "expected_min_total_hotels": 1200, "reported_total_hotels": 1200, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 275, "expected_total_attractions": 550, "reported_total_attractions": 250, "meal_per_person_cost_sum": 2078, "expected_total_meals": 4156, "reported_total_meals": 480, "reported_total_transportation": 200}}]`

### v3_harder_eval_000005
- request: 广州 2026-07-03->2026-07-07 days=5 transport=公共交通 hotel=民宿 prefs=['摄影', '自然风光', '城市漫步', '本地菜']
- errors: `[{"stage": "rule", "type": "accommodation_type_mismatch", "details": [{"date": "2026-07-07", "day_index": 4, "expected": "民宿", "got": "无住宿"}]}, {"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-07-07", "lunch": "滋粥楼·顺德菜(番禺广场总店)", "dinner": "滋粥楼·顺德菜(南村万博长隆商圈店)"}]}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 2900, "total": 2700, "diff": 200, "requested_budget": {"available": true, "amount": 2600, "scope": "total", "party_size": 1, "total": 2600, "source": "budget_constraint", "budget_level": "standard", "strictness": "hard"}, "per_person_day": 540.0, "budget_level": "standard", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "standard", "strictness": "hard", "amount": 2600, "target_min_ratio": 0.55, "target_max_ratio": 1.0, "target_min_total": 1400, "target_max_total": 2600, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": false, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 4, "party_total": 1, "room_count": 1, "priced_nights": 4, "expected_min_total_hotels": 1200, "reported_total_hotels": 1200, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_harder_eval_000003
- request: 西安 2025-05-04->2025-05-08 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2025-05-07", "lunch": "清真刚刚烤肉(小南门店)", "dinner": "清真刚刚烤肉(芙蓉街店)"}, {"date": "2025-05-08", "lunch": "清真刚刚烤肉(芙蓉街店)", "dinner": "清真刚刚烤肉(芙蓉街店)"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "清真刚刚烤肉", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2025-05-06", "type": "dinner", "name": "清真刚刚烤肉(芙蓉街店)"}, {"date": "2025-05-07", "type": "lunch", "name": "清真刚刚烤肉(小南门店)"}, {"date": "2025-05-07", "type": "dinner", "name": "清真刚刚烤肉(芙蓉街店)"}, {"date": "2025-05-08", "type": "lunch", "name": "清真刚刚烤肉(芙蓉街店)"}, {"date": "2025-05-08", "type": "dinner", "name": "清真刚刚烤肉(芙蓉街店)"}]}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 200, "expected_total_attractions": 400, "reported_total_attractions": 540, "meal_per_person_cost_sum": 1190, "expected_total_meals": 2380, "reported_total_meals": 480, "reported_total_transportation": 200}}]`

### v3_harder_eval_000000
- request: 昆明 2026-04-04->2026-04-08 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "欢乐+倍亲子乐园", "count": 3, "max_allowed": 1, "occurrences": [{"date": "2026-04-06", "day_index": 2, "name": "欢乐+倍亲子乐园"}, {"date": "2026-04-07", "day_index": 3, "name": "欢乐+倍亲子乐园"}, {"date": "2026-04-08", "day_index": 4, "name": "欢乐+倍亲子乐园"}]}]}, {"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-04-04", "lunch": "四方小炒·云南菜小当家(联盟店)", "dinner": "四方小炒·云南菜小当家(同德店)"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "超英砂锅煲云南菜", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-04-05", "type": "dinner", "name": "超英砂锅煲云南菜"}, {"date": "2026-04-06", "type": "dinner", "name": "超英砂锅煲云南菜"}, {"date": "2026-04-07", "type": "dinner", "name": "超英砂锅煲云南菜"}, {"date": "2026-04-08", "type": "dinner", "name": "超英砂锅煲云南菜"}]}]}]`

### v3_harder_eval_000011
- request: 福州 2026-06-18->2026-06-21 days=4 transport=打车 hotel=高端酒店 prefs=['高端酒店', '艺术', '特色餐厅', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 130, "expected_total_attractions": 260, "reported_total_attractions": 1000, "meal_per_person_cost_sum": 1598, "expected_total_meals": 3196, "reported_total_meals": 1440, "reported_total_transportation": 800}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 130, "expected_total_attractions": 260, "reported_total_attractions": 1000, "meal_per_person_cost_sum": 1598, "expected_total_meals": 3196, "reported_total_meals": 1440, "reported_total_transportation": 800}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": false, "meal_cost_scale_ok": false, "budget_relationship_ok": false, "expected_total_hotels": 3000, "reported_total_hotels": 3000, "expected_total_attractions": 260, "reported_total_attractions": 1000, "meal_scale_eval": {"ok": false, "party_total": 2, "budget_level": "premium", "per_person_lunch_dinner_floor": 70, "per_person_breakfast_floor": 28, "meal_count": 12, "checked_count": 8, "failure_count": 1, "failures": [{"date": "2026-06-20", "type": "lunch", "name": "后街捞化", "estimated_cost": 54, "min_expected_cost": 70}]}}}]`

### v3_harder_eval_000014
- request: 成都 2026-06-03->2026-06-05 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-06-03", "lunch": "观锦餐厅(天廊店)", "dinner": "观锦餐厅(天廊店)"}, {"date": "2026-06-04", "lunch": "马旺子·川小馆(成都太古里店)", "dinner": "马旺子·川小馆(成都太古里店)"}, {"date": "2026-06-05", "lunch": "悦百味·品质川菜(悠方店)", "dinner": "悦百味·品质川菜(悠方店)"}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 2, "party_total": 1, "room_count": 1, "priced_nights": 2, "expected_min_total_hotels": 900, "reported_total_hotels": 1350, "diff": 450, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 165, "expected_total_attractions": 165, "reported_total_attractions": 230, "meal_per_person_cost_sum": 916, "expected_total_meals": 916, "reported_total_meals": 450, "reported_total_transportation": 300}}]`

### v3_harder_eval_000018
- request: 天津 2026-07-03->2026-07-05 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 2, "party_total": 3, "room_count": 2, "priced_nights": 2, "expected_min_total_hotels": 4800, "reported_total_hotels": 3600, "diff": -1200, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 201, "expected_total_attractions": 603, "reported_total_attractions": 340, "meal_per_person_cost_sum": 1386, "expected_total_meals": 4158, "reported_total_meals": 810, "reported_total_transportation": 600}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 201, "expected_total_attractions": 603, "reported_total_attractions": 340, "meal_per_person_cost_sum": 1386, "expected_total_meals": 4158, "reported_total_meals": 810, "reported_total_transportation": 600}}]`

### v3_harder_eval_000012
- request: 洛阳 2025-05-04->2025-05-07 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '夜市', '老字号', '城市漫步']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2025-05-04", "lunch": "洛阳十字街小吃一条街", "dinner": "洛阳十字街小吃一条街"}, {"date": "2025-05-05", "lunch": "光头东烙馍村·水席洛阳菜(火车站店)", "dinner": "光头东烙馍村·水席洛阳菜(火车站店)"}, {"date": "2025-05-07", "lunch": "必胜客(正大广场店)", "dinner": "必胜客(正大广场店)"}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 4, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 1400, "reported_total_hotels": 900, "diff": -500, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 240, "expected_total_attractions": 960, "reported_total_attractions": 240, "meal_per_person_cost_sum": 1392, "expected_total_meals": 5568, "reported_total_meals": 480, "reported_total_transportation": 200}}]`

### v3_harder_eval_000019
- request: 丽江 2026-05-08->2026-05-11 days=4 transport=打车 hotel=亲子酒店 prefs=['亲子', '老人友好', '博物馆', '城市公园', '特色餐厅']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-05-11", "lunch": "则瓦米线·云南小吃集合(花巷店)", "dinner": "则瓦米线·云南小吃集合(花巷店)"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "则瓦米线·云南小吃集合", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-05-08", "type": "lunch", "name": "则瓦米线·云南小吃集合(花巷店)"}, {"date": "2026-05-09", "type": "lunch", "name": "则瓦米线·云南小吃集合(花巷店)"}, {"date": "2026-05-10", "type": "lunch", "name": "则瓦米线·云南小吃集合(花巷店)"}, {"date": "2026-05-11", "type": "lunch", "name": "则瓦米线·云南小吃集合(花巷店)"}, {"date": "2026-05-11", "type": "dinner", "name": "则瓦米线·云南小吃集合(花巷店)"}]}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 400, "expected_total_attractions": 800, "reported_total_attractions": 240, "meal_per_person_cost_sum": 1166, "expected_total_meals": 2332, "reported_total_meals": 486, "reported_total_transportation": 200}}]`

### v3_harder_eval_000016
- request: 苏州 2026-06-03->2026-06-06 days=4 transport=自驾 hotel=亲子酒店 prefs=['亲子', '动物园', '海洋馆', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "accommodation_type_mismatch", "details": [{"date": "2026-06-06", "day_index": 3, "expected": "亲子酒店", "got": "无住宿"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "稻山村·苏州菜", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-06-03", "type": "lunch", "name": "稻山村·苏州菜(石路店)"}, {"date": "2026-06-04", "type": "lunch", "name": "稻山村·苏州菜(石路店)"}, {"date": "2026-06-05", "type": "lunch", "name": "稻山村·苏州菜(石路店)"}, {"date": "2026-06-06", "type": "lunch", "name": "稻山村·苏州菜(石路店)"}]}, {"name_key": "树山留白馆•地道苏帮菜•土鸡汤", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-06-03", "type": "dinner", "name": "树山留白馆•地道苏帮菜•土鸡汤"}, {"date": "2026-06-04", "type": "dinner", "name": "树山留白馆•地道苏帮菜•土鸡汤"}, {"date": "2026-06-05", "type": "dinner", "name": "树山留白馆•地道苏帮菜•土鸡汤"}, {"date": "2026-06-06", "type": "dinner", "name": "树山留白馆•地道苏帮菜•土鸡汤"}]}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 3, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 7500, "reported_total_hotels": 3750, "diff": -3750, "covers_nights": false}}]`

### v3_harder_eval_000013
- request: 武汉 2026-05-06->2026-05-10 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-05-10", "lunch": "刘聋子牛肉粉馆(汉阳玫瑰街店)", "dinner": "刘聋子牛肉粉馆(汉阳玫瑰街店)"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "刘聋子牛肉粉馆", "count": 6, "max_allowed": 3, "occurrences": [{"date": "2026-05-06", "type": "dinner", "name": "刘聋子牛肉粉馆(汉阳玫瑰街店)"}, {"date": "2026-05-07", "type": "dinner", "name": "刘聋子牛肉粉馆(汉阳玫瑰街店)"}, {"date": "2026-05-08", "type": "dinner", "name": "刘聋子牛肉粉馆(汉阳玫瑰街店)"}, {"date": "2026-05-09", "type": "dinner", "name": "刘聋子牛肉粉馆(汉阳玫瑰街店)"}, {"date": "2026-05-10", "type": "lunch", "name": "刘聋子牛肉粉馆(汉阳玫瑰街店)"}, {"date": "2026-05-10", "type": "dinner", "name": "刘聋子牛肉粉馆(汉阳玫瑰街店)"}]}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 140, "expected_total_attractions": 280, "reported_total_attractions": 210, "meal_per_person_cost_sum": 878, "expected_total_meals": 1756, "reported_total_meals": 480, "reported_total_transportation": 200}}]`

### v3_harder_eval_000017
- request: 苏州 2026-05-06->2026-05-10 days=5 transport=公共交通 hotel=民宿 prefs=['小众展馆', '咖啡', '艺术', '城市漫步', '特色餐厅']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "秋娟馄饨店", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-05-06", "type": "breakfast", "name": "秋娟馄饨店"}, {"date": "2026-05-07", "type": "breakfast", "name": "秋娟馄饨店"}, {"date": "2026-05-08", "type": "breakfast", "name": "秋娟馄饨店"}, {"date": "2026-05-09", "type": "breakfast", "name": "秋娟馄饨店"}, {"date": "2026-05-10", "type": "breakfast", "name": "秋娟馄饨店"}]}, {"name_key": "哑巴生煎", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-05-07", "type": "dinner", "name": "哑巴生煎(临顿路店)"}, {"date": "2026-05-08", "type": "dinner", "name": "哑巴生煎(临顿路店)"}, {"date": "2026-05-09", "type": "dinner", "name": "哑巴生煎(临顿路店)"}, {"date": "2026-05-10", "type": "dinner", "name": "哑巴生煎(临顿路店)"}]}]}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 3399, "total": 2499, "diff": 900, "requested_budget": {"available": true, "amount": 6700, "scope": "total", "party_size": 2, "total": 6700, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "soft"}, "per_person_day": 249.9, "budget_level": "comfortable", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "soft", "amount": 6700, "target_min_ratio": 0.65, "target_max_ratio": 1.05, "target_min_total": 4400, "target_max_total": 7000, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 4, "party_total": 2, "room_count": 1, "priced_nights": 4, "expected_min_total_hotels": 1600, "reported_total_hotels": 1600, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 215, "expected_total_attractions": 430, "reported_total_attractions": 275, "meal_per_person_cost_sum": 2114, "expected_total_meals": 4228, "reported_total_meals": 1124, "reported_total_transportation": 400}}]`

### v3_harder_eval_000020
- request: 杭州 2026-06-18->2026-06-22 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 4, "party_total": 5, "room_count": 3, "priced_nights": 4, "expected_min_total_hotels": 6000, "reported_total_hotels": 2000, "diff": -4000, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 5, "hotel_room_count": 3, "attraction_ticket_sum": 110, "expected_total_attractions": 550, "reported_total_attractions": 280, "meal_per_person_cost_sum": 4565, "expected_total_meals": 22825, "reported_total_meals": 1650, "reported_total_transportation": 1000}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 5, "hotel_room_count": 3, "attraction_ticket_sum": 110, "expected_total_attractions": 550, "reported_total_attractions": 280, "meal_per_person_cost_sum": 4565, "expected_total_meals": 22825, "reported_total_meals": 1650, "reported_total_transportation": 1000}}]`

### v3_harder_eval_000024
- request: 济南 2026-05-07->2026-05-09 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 2105, "total": 2005, "diff": 100, "requested_budget": {"available": true, "amount": 1700, "scope": "total", "party_size": 1, "total": 1700, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "hard"}, "per_person_day": 668.33, "budget_level": "comfortable", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "hard", "amount": 1700, "target_min_ratio": 0.65, "target_max_ratio": 1.0, "target_min_total": 1100, "target_max_total": 1700, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": false, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 1, "room_count": 1, "priced_nights": 3, "expected_min_total_hotels": 1200, "reported_total_hotels": 1200, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 160, "expected_total_attractions": 160, "reported_total_attractions": 240, "meal_per_person_cost_sum": 576, "expected_total_meals": 576, "reported_total_meals": 465, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 160, "expected_total_attractions": 160, "reported_total_attractions": 240, "meal_per_person_cost_sum": 576, "expected_total_meals": 576, "reported_total_meals": 465, "reported_total_transportation": 200}}]`
