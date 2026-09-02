# Rule Eval Report: sft_qwen25_7b_v3_1000_cp2_v1_A_C_w8

- records: 300
- generations: `training/outputs/eval/sft_qwen25_7b_v3_1000_cp2_v1_A_C_w8/generations.jsonl`
- records_path: `training/data/v3/eval_harder_prompt_ablation_20260505/A_C/records.jsonl`

## Boolean Metrics

| Metric | Pass | Total | Rate |
| --- | ---: | ---: | ---: |
| accommodation_type_ok | 298 | 298 | 100.00% |
| attraction_budget_consistent | 34 | 298 | 11.41% |
| attraction_budget_party_relation_ok | 119 | 298 | 39.93% |
| attraction_count_ok | 292 | 298 | 97.99% |
| attraction_diversity_ok | 209 | 298 | 70.13% |
| attraction_grounding_ok | 280 | 298 | 93.96% |
| attraction_repeat_limit_ok | 209 | 298 | 70.13% |
| budget_arithmetic_consistent | 221 | 298 | 74.16% |
| budget_consistent | 221 | 298 | 74.16% |
| budget_level_aligned | 170 | 298 | 57.05% |
| budget_preference_aligned | 170 | 298 | 57.05% |
| budget_relationship_ok | 41 | 298 | 13.76% |
| budget_user_constraint_ok | 230 | 298 | 77.18% |
| budget_within_user_budget | 276 | 298 | 92.62% |
| city_ok | 298 | 298 | 100.00% |
| date_range_ok | 298 | 298 | 100.00% |
| day_dates_ok | 298 | 298 | 100.00% |
| day_index_ok | 298 | 298 | 100.00% |
| days_len_ok | 298 | 298 | 100.00% |
| dpo_soft_pass | 0 | 298 | 0.00% |
| hard_pass | 0 | 298 | 0.00% |
| hotel_budget_covers_nights | 160 | 298 | 53.69% |
| hotel_budget_relation_ok | 162 | 298 | 54.36% |
| hotel_distance_placeholder_ok | 298 | 298 | 100.00% |
| hotel_grounding_ok | 298 | 298 | 100.00% |
| invalid_hotel_name_ok | 298 | 298 | 100.00% |
| json_extract_ok | 300 | 300 | 100.00% |
| legacy_hard_pass | 60 | 298 | 20.13% |
| location_object_ok | 298 | 298 | 100.00% |
| meal_budget_consistent | 0 | 298 | 0.00% |
| meal_complete | 298 | 298 | 100.00% |
| meal_cost_scale_ok | 230 | 298 | 77.18% |
| meal_diversity_ok | 223 | 298 | 74.83% |
| meal_grounding_ok | 209 | 298 | 70.13% |
| meal_lunch_dinner_same_day_ok | 264 | 298 | 88.59% |
| meal_repeat_limit_ok | 233 | 298 | 78.19% |
| meal_specific_ok | 292 | 298 | 97.99% |
| meal_valid_semantics_ok | 231 | 298 | 77.52% |
| middle_hotel_ok | 298 | 298 | 100.00% |
| schema_ok | 298 | 300 | 99.33% |
| sft_budget_semantic_hard_pass | 19 | 298 | 6.38% |
| sft_hard_pass | 0 | 298 | 0.00% |
| transportation_budget_nonnegative | 298 | 298 | 100.00% |
| weather_dates_ok | 295 | 298 | 98.99% |
| weather_match | 295 | 298 | 98.99% |

## Numeric Metrics

```json
{
  "attraction_diversity_unique_rate": {
    "avg": 0.9529,
    "p50": 1.0,
    "p90": 1.0
  },
  "attraction_grounding_rate": {
    "avg": 0.9911,
    "p50": 1.0,
    "p90": 1.0
  },
  "hotel_grounding_rate": {
    "avg": 1.0,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_diversity_unique_rate": {
    "avg": 0.5306,
    "p50": 0.5,
    "p90": 0.9
  },
  "meal_food_pois_grounding_rate": {
    "avg": 0.8468,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_grounding_rate": {
    "avg": 0.8468,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_semantic_valid_rate": {
    "avg": 0.9226,
    "p50": 1.0,
    "p90": 1.0
  }
}
```

## Failure Types

```json
{
  "meal_budget_inconsistent": 296,
  "attraction_budget_inconsistent": 264,
  "budget_relationship_mismatch": 257,
  "hotel_budget_underestimated": 138,
  "budget_preference_mismatch": 128,
  "attraction_repeat_too_many": 89,
  "budget_arithmetic_inconsistent": 77,
  "meal_cost_scale_too_low": 68,
  "budget_hard_constraint_exceeded": 68,
  "meal_invalid_name": 67,
  "meal_repeat_too_many": 65,
  "meal_same_day_lunch_dinner_repeat": 34,
  "meal_grounding_miss": 22,
  "too_many_attractions": 6,
  "meal_placeholder": 6,
  "weather_mismatch": 3,
  "schema": 2
}
```

## Failure Examples

### v3_harder_eval_000004
- request: 张家界 2026-05-07->2026-05-09 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 1400, "total": 1200, "diff": 200, "requested_budget": {"available": true, "amount": 1700, "scope": "total", "party_size": 1, "total": 1700, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "hard"}, "per_person_day": 400.0, "budget_level": "comfortable", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "hard", "amount": 1700, "target_min_ratio": 0.65, "target_max_ratio": 1.0, "target_min_total": 1100, "target_max_total": 1700, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 1, "room_count": 1, "priced_nights": 2, "expected_min_total_hotels": 800, "reported_total_hotels": 800, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 160, "expected_total_attractions": 160, "reported_total_attractions": 240, "meal_per_person_cost_sum": 418, "expected_total_meals": 418, "reported_total_meals": 260, "reported_total_transportation": 100}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 160, "expected_total_attractions": 160, "reported_total_attractions": 240, "meal_per_person_cost_sum": 418, "expected_total_meals": 418, "reported_total_meals": 260, "reported_total_transportation": 100}}]`

### v3_harder_eval_000001
- request: 桂林 2026-08-31->2026-09-03 days=4 transport=打车 hotel=高端酒店 prefs=['高端酒店', '艺术', '特色餐厅', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "味道制造·桂林菜", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-08-31", "type": "lunch", "name": "味道制造·桂林菜(七星店)"}, {"date": "2026-09-01", "type": "dinner", "name": "味道制造·桂林菜(七星店)"}, {"date": "2026-09-02", "type": "lunch", "name": "味道制造·桂林菜(七星店)"}, {"date": "2026-09-03", "type": "lunch", "name": "味道制造·桂林菜(七星店)"}]}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 345, "expected_total_attractions": 690, "reported_total_attractions": 630, "meal_per_person_cost_sum": 1220, "expected_total_meals": 2440, "reported_total_meals": 1248, "reported_total_transportation": 1200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 345, "expected_total_attractions": 690, "reported_total_attractions": 630, "meal_per_person_cost_sum": 1220, "expected_total_meals": 2440, "reported_total_meals": 1248, "reported_total_transportation": 1200}}]`

### v3_harder_eval_000006
- request: 南京 2026-07-02->2026-07-05 days=4 transport=自驾 hotel=亲子酒店 prefs=['亲子', '动物园', '海洋馆', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "南京博物院", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-07-03", "day_index": 1, "name": "南京博物院"}, {"date": "2026-07-05", "day_index": 3, "name": "南京博物院"}]}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 3, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 3300, "reported_total_hotels": 1650, "diff": -1650, "covers_nights": false}}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 3850, "total": 2850, "diff": 1000, "requested_budget": {"available": true, "amount": 4000, "scope": "total", "party_size": 3, "total": 4000, "source": "budget_constraint", "budget_level": "standard", "strictness": "hard"}, "per_person_day": 237.5, "budget_level": "standard", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "standard", "strictness": "hard", "amount": 4000, "target_min_ratio": 0.55, "target_max_ratio": 1.0, "target_min_total": 2200, "target_max_total": 4000, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 3, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 3300, "reported_total_hotels": 1650, "diff": -1650, "covers_nights": false}, "hotel_budget_covers_nights": false}}]`

### v3_harder_eval_000002
- request: 杭州 2026-04-27->2026-04-30 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '夜市', '老字号', '城市漫步']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 4, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 1500, "reported_total_hotels": 750, "diff": -750, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 240, "expected_total_attractions": 960, "reported_total_attractions": 340, "meal_per_person_cost_sum": 1176, "expected_total_meals": 4704, "reported_total_meals": 1688, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 240, "expected_total_attractions": 960, "reported_total_attractions": 340, "meal_per_person_cost_sum": 1176, "expected_total_meals": 4704, "reported_total_meals": 1688, "reported_total_transportation": 200}}]`

### v3_harder_eval_000003
- request: 西安 2025-05-03->2025-05-07 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 134, "expected_total_attractions": 268, "reported_total_attractions": 214, "meal_per_person_cost_sum": 600, "expected_total_meals": 1200, "reported_total_meals": 800, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 134, "expected_total_attractions": 268, "reported_total_attractions": 214, "meal_per_person_cost_sum": 600, "expected_total_meals": 1200, "reported_total_meals": 800, "reported_total_transportation": 200}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": false, "meal_cost_scale_ok": true, "budget_relationship_ok": false, "expected_total_hotels": 1800, "reported_total_hotels": 1800, "expected_total_attractions": 268, "reported_total_attractions": 214, "meal_scale_eval": {"ok": true, "party_total": 2, "budget_level": "standard", "per_person_lunch_dinner_floor": 35, "per_person_breakfast_floor": 14, "meal_count": 15, "checked_count": 15, "failure_count": 0, "failures": []}}}]`

### v3_harder_eval_000007
- request: 成都 2026-05-07->2026-05-11 days=5 transport=公共交通 hotel=民宿 prefs=['小众展馆', '咖啡', '艺术', '城市漫步', '特色餐厅']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-05-08", "lunch": "星巴克(成都SKP店)", "dinner": "星巴克(成都大魔方招商花园城店)"}, {"date": "2026-05-09", "lunch": "星巴克(成都环球中心II店)", "dinner": "星巴克(成都SKP店)"}, {"date": "2026-05-10", "lunch": "星巴克(成都环球中心II店)", "dinner": "星巴克(成都SKP店)"}, {"date": "2026-05-11", "lunch": "星巴克(成都环球中心II店)", "dinner": "星巴克(成都SKP店)"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "星巴克", "count": 9, "max_allowed": 3, "occurrences": [{"date": "2026-05-07", "type": "lunch", "name": "星巴克(成都环球中心II店)"}, {"date": "2026-05-08", "type": "lunch", "name": "星巴克(成都SKP店)"}, {"date": "2026-05-08", "type": "dinner", "name": "星巴克(成都大魔方招商花园城店)"}, {"date": "2026-05-09", "type": "lunch", "name": "星巴克(成都环球中心II店)"}, {"date": "2026-05-09", "type": "dinner", "name": "星巴克(成都SKP店)"}, {"date": "2026-05-10", "type": "lunch", "name": "星巴克(成都环球中心II店)"}, {"date": "2026-05-10", "type": "dinner", "name": "星巴克(成都SKP店)"}, {"date": "2026-05-11", "type": "lunch", "name": "星巴克(成都环球中心II店)"}, {"date": "2026-05-11", "type": "dinner", "name": "星巴克(成都SKP店)"}]}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 355, "expected_total_attractions": 710, "reported_total_attractions": 1050, "meal_per_person_cost_sum": 748, "expected_total_meals": 1496, "reported_total_meals": 1120, "reported_total_transportation": 300}}]`

### v3_harder_eval_000000
- request: 昆明 2026-04-03->2026-04-07 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_grounding_miss", "details": [{"date": "2026-04-03", "type": "lunch", "name": "云南民族特色餐厅"}, {"date": "2026-04-03", "type": "dinner", "name": "本地家常菜馆"}, {"date": "2026-04-04", "type": "lunch", "name": "本地特色餐厅"}, {"date": "2026-04-04", "type": "dinner", "name": "本地家常菜馆"}, {"date": "2026-04-05", "type": "lunch", "name": "本地特色餐厅"}, {"date": "2026-04-05", "type": "dinner", "name": "本地家常菜馆"}, {"date": "2026-04-06", "type": "lunch", "name": "本地特色餐厅"}, {"date": "2026-04-06", "type": "dinner", "name": "本地家常菜馆"}, {"date": "2026-04-07", "type": "lunch", "name": "本地特色餐厅"}, {"date": "2026-04-07", "type": "dinner", "name": "本地家常菜馆"}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 4, "party_total": 5, "room_count": 3, "priced_nights": 4, "expected_min_total_hotels": 4800, "reported_total_hotels": 1600, "diff": -3200, "covers_nights": false}}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 4983, "total": 5983, "diff": -1000, "requested_budget": {"available": true, "amount": 12800, "scope": "total", "party_size": 5, "total": 12800, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "hard"}, "per_person_day": 239.32, "budget_level": "comfortable", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "hard", "amount": 12800, "target_min_ratio": 0.65, "target_max_ratio": 1.0, "target_min_total": 8300, "target_max_total": 12800, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 4, "party_total": 5, "room_count": 3, "priced_nights": 4, "expected_min_total_hotels": 4800, "reported_total_hotels": 1600, "diff": -3200, "covers_nights": false}, "hotel_budget_covers_nights": false}}]`

### v3_harder_eval_000005
- request: 广州 2026-07-02->2026-07-06 days=5 transport=公共交通 hotel=民宿 prefs=['摄影', '自然风光', '城市漫步', '本地菜']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "流花湖公园", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-07-02", "day_index": 0, "name": "流花湖公园"}, {"date": "2026-07-06", "day_index": 4, "name": "流花湖公园"}]}, {"name_key": "海珠湖公园", "count": 3, "max_allowed": 1, "occurrences": [{"date": "2026-07-03", "day_index": 1, "name": "海珠湖公园"}, {"date": "2026-07-04", "day_index": 2, "name": "海珠湖公园"}, {"date": "2026-07-05", "day_index": 3, "name": "海珠湖公园"}]}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 255, "expected_total_attractions": 255, "reported_total_attractions": 1050, "meal_per_person_cost_sum": 1058, "expected_total_meals": 1058, "reported_total_meals": 1032, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 255, "expected_total_attractions": 255, "reported_total_attractions": 1050, "meal_per_person_cost_sum": 1058, "expected_total_meals": 1058, "reported_total_meals": 1032, "reported_total_transportation": 200}}]`

### v3_harder_eval_000008
- request: 大理 2026-05-07->2026-05-09 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物']
- errors: `[{"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-05-07", "type": "lunch", "name": "里白云南家常菜", "reason": "unknown_food_semantics"}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 2, "party_total": 3, "room_count": 2, "priced_nights": 2, "expected_min_total_hotels": 4800, "reported_total_hotels": 2400, "diff": -2400, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 75, "expected_total_attractions": 225, "reported_total_attractions": 324, "meal_per_person_cost_sum": 692, "expected_total_meals": 2076, "reported_total_meals": 1076, "reported_total_transportation": 1000}}]`

### v3_harder_eval_000011
- request: 福州 2026-06-17->2026-06-20 days=4 transport=打车 hotel=高端酒店 prefs=['高端酒店', '艺术', '特色餐厅', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 2, "room_count": 1, "priced_nights": 3, "expected_min_total_hotels": 2250, "reported_total_hotels": 4500, "diff": 2250, "covers_nights": false}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 0, "expected_total_attractions": 0, "reported_total_attractions": 0, "meal_per_person_cost_sum": 1660, "expected_total_meals": 3320, "reported_total_meals": 2864, "reported_total_transportation": 1200}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": false, "attraction_budget_party_relation_ok": true, "meal_cost_scale_ok": true, "budget_relationship_ok": false, "expected_total_hotels": 2250, "reported_total_hotels": 4500, "expected_total_attractions": 0, "reported_total_attractions": 0, "meal_scale_eval": {"ok": true, "party_total": 2, "budget_level": "premium", "per_person_lunch_dinner_floor": 70, "per_person_breakfast_floor": 28, "meal_count": 12, "checked_count": 8, "failure_count": 0, "failures": []}}}]`

### v3_harder_eval_000009
- request: 苏州 2026-04-26->2026-04-29 days=4 transport=打车 hotel=亲子酒店 prefs=['亲子', '老人友好', '博物馆', '城市公园', '特色餐厅']
- errors: `[{"stage": "rule", "type": "meal_grounding_miss", "details": [{"date": "2026-04-26", "type": "dinner", "name": "苏州本帮菜馆"}, {"date": "2026-04-27", "type": "dinner", "name": "苏州本帮菜馆"}, {"date": "2026-04-28", "type": "dinner", "name": "苏州本帮菜馆"}, {"date": "2026-04-29", "type": "dinner", "name": "苏州本帮菜馆"}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 4, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 7500, "reported_total_hotels": 3750, "diff": -3750, "covers_nights": false}}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 7200, "total": 7100, "diff": 100, "requested_budget": {"available": true, "amount": 9100, "scope": "total", "party_size": 4, "total": 9100, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "soft"}, "per_person_day": 443.75, "budget_level": "comfortable", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "soft", "amount": 9100, "target_min_ratio": 0.65, "target_max_ratio": 1.05, "target_min_total": 5900, "target_max_total": 9600, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 4, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 7500, "reported_total_hotels": 3750, "diff": -3750, "covers_nights": false}, "hotel_budget_covers_nights": false}}]`

### v3_harder_eval_000014
- request: 成都 2026-06-02->2026-06-04 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 1800, "total": 1700, "diff": 100, "requested_budget": {"available": true, "amount": 2100, "scope": "total", "party_size": 1, "total": 2100, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "hard"}, "per_person_day": 566.67, "budget_level": "comfortable", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "hard", "amount": 2100, "target_min_ratio": 0.65, "target_max_ratio": 1.0, "target_min_total": 1400, "target_max_total": 2100, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 1, "room_count": 1, "priced_nights": 2, "expected_min_total_hotels": 900, "reported_total_hotels": 900, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 190, "expected_total_attractions": 190, "reported_total_attractions": 259, "meal_per_person_cost_sum": 757, "expected_total_meals": 757, "reported_total_meals": 541, "reported_total_transportation": 100}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 190, "expected_total_attractions": 190, "reported_total_attractions": 259, "meal_per_person_cost_sum": 757, "expected_total_meals": 757, "reported_total_meals": 541, "reported_total_transportation": 100}}]`

### v3_harder_eval_000010
- request: 西安 2026-04-19->2026-04-23 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "陕西历史博物馆", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-04-19", "day_index": 0, "name": "陕西历史博物馆"}, {"date": "2026-04-22", "day_index": 3, "name": "陕西历史博物馆"}]}, {"name_key": "西安博物院", "count": 4, "max_allowed": 1, "occurrences": [{"date": "2026-04-19", "day_index": 0, "name": "西安博物院"}, {"date": "2026-04-20", "day_index": 1, "name": "西安博物院"}, {"date": "2026-04-21", "day_index": 2, "name": "西安博物院"}, {"date": "2026-04-22", "day_index": 3, "name": "西安博物院"}]}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 4, "party_total": 5, "room_count": 3, "priced_nights": 4, "expected_min_total_hotels": 5400, "reported_total_hotels": 3600, "diff": -1800, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 5, "hotel_room_count": 3, "attraction_ticket_sum": 145, "expected_total_attractions": 725, "reported_total_attractions": 1050, "meal_per_person_cost_sum": 1150, "expected_total_meals": 5750, "reported_total_meals": 1500, "reported_total_transportation": 1000}}]`

### v3_harder_eval_000016
- request: 苏州 2026-06-02->2026-06-05 days=4 transport=自驾 hotel=亲子酒店 prefs=['亲子', '动物园', '海洋馆', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-06-02", "type": "dinner", "name": "松鹤楼", "reason": "unknown_food_semantics"}, {"date": "2026-06-03", "type": "dinner", "name": "松鹤楼", "reason": "unknown_food_semantics"}, {"date": "2026-06-04", "type": "dinner", "name": "松鹤楼", "reason": "unknown_food_semantics"}, {"date": "2026-06-05", "type": "dinner", "name": "松鹤楼", "reason": "unknown_food_semantics"}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 3, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 7500, "reported_total_hotels": 3750, "diff": -3750, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 195, "expected_total_attractions": 585, "reported_total_attractions": 335, "meal_per_person_cost_sum": 920, "expected_total_meals": 2760, "reported_total_meals": 900, "reported_total_transportation": 200}}]`

### v3_harder_eval_000015
- request: 南京 2026-04-03->2026-04-07 days=5 transport=公共交通 hotel=民宿 prefs=['摄影', '自然风光', '城市漫步', '本地菜']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "玄武湖景区", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-04-03", "day_index": 0, "name": "玄武湖景区"}, {"date": "2026-04-07", "day_index": 4, "name": "玄武湖景区"}]}, {"name_key": "南京博物院", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-04-03", "day_index": 0, "name": "南京博物院"}, {"date": "2026-04-06", "day_index": 3, "name": "南京博物院"}]}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 75, "expected_total_attractions": 75, "reported_total_attractions": 175, "meal_per_person_cost_sum": 950, "expected_total_meals": 950, "reported_total_meals": 732, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 75, "expected_total_attractions": 75, "reported_total_attractions": 175, "meal_per_person_cost_sum": 950, "expected_total_meals": 950, "reported_total_meals": 732, "reported_total_transportation": 200}}]`

### v3_harder_eval_000013
- request: 武汉 2026-05-05->2026-05-09 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "汉口江滩", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-05-05", "day_index": 0, "name": "汉口江滩"}, {"date": "2026-05-08", "day_index": 3, "name": "汉口江滩"}]}]}, {"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-05-05", "type": "lunch", "name": "汉味轩", "reason": "unknown_food_semantics"}, {"date": "2026-05-05", "type": "dinner", "name": "老汉口酒楼", "reason": "unknown_food_semantics"}, {"date": "2026-05-06", "type": "lunch", "name": "蔡林记", "reason": "unknown_food_semantics"}, {"date": "2026-05-06", "type": "dinner", "name": "老汉口酒楼", "reason": "unknown_food_semantics"}, {"date": "2026-05-07", "type": "lunch", "name": "蔡林记", "reason": "unknown_food_semantics"}, {"date": "2026-05-07", "type": "dinner", "name": "老汉口酒楼", "reason": "unknown_food_semantics"}, {"date": "2026-05-08", "type": "lunch", "name": "蔡林记", "reason": "unknown_food_semantics"}, {"date": "2026-05-08", "type": "dinner", "name": "老汉口酒楼", "reason": "unknown_food_semantics"}, {"date": "2026-05-09", "type": "lunch", "name": "蔡林记", "reason": "unknown_food_semantics"}, {"date": "2026-05-09", "type": "dinner", "name": "老汉口酒楼", "reason": "unknown_food_semantics"}]}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 2700, "total": 2600, "diff": 100, "requested_budget": {"available": true, "amount": 3900, "scope": "total", "party_size": 2, "total": 3900, "source": "budget_constraint", "budget_level": "standard", "strictness": "hard"}, "per_person_day": 260.0, "budget_level": "standard", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "standard", "strictness": "hard", "amount": 3900, "target_min_ratio": 0.55, "target_max_ratio": 1.0, "target_min_total": 2100, "target_max_total": 3900, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 4, "party_total": 2, "room_count": 1, "priced_nights": 4, "expected_min_total_hotels": 1600, "reported_total_hotels": 1600, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_harder_eval_000018
- request: 天津 2026-07-02->2026-07-04 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 2, "party_total": 3, "room_count": 2, "priced_nights": 2, "expected_min_total_hotels": 4800, "reported_total_hotels": 2400, "diff": -2400, "covers_nights": false}}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 4200, "total": 3800, "diff": 400, "requested_budget": {"available": true, "amount": 4800, "scope": "total", "party_size": 3, "total": 4800, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "hard"}, "per_person_day": 422.22, "budget_level": "comfortable", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "hard", "amount": 4800, "target_min_ratio": 0.65, "target_max_ratio": 1.0, "target_min_total": 3100, "target_max_total": 4800, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 3, "room_count": 2, "priced_nights": 2, "expected_min_total_hotels": 4800, "reported_total_hotels": 2400, "diff": -2400, "covers_nights": false}, "hotel_budget_covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 160, "expected_total_attractions": 480, "reported_total_attractions": 460, "meal_per_person_cost_sum": 1581, "expected_total_meals": 4743, "reported_total_meals": 1040, "reported_total_transportation": 300}}]`

### v3_harder_eval_000012
- request: 洛阳 2025-05-03->2025-05-06 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '夜市', '老字号', '城市漫步']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "隋唐城遗址植物园", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2025-05-03", "day_index": 0, "name": "隋唐城遗址植物园"}, {"date": "2025-05-06", "day_index": 3, "name": "隋唐城遗址植物园"}]}, {"name_key": "应天门", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2025-05-04", "day_index": 1, "name": "应天门"}, {"date": "2025-05-06", "day_index": 3, "name": "应天门"}]}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 4, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 1200, "reported_total_hotels": 600, "diff": -600, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 320, "expected_total_attractions": 1280, "reported_total_attractions": 640, "meal_per_person_cost_sum": 738, "expected_total_meals": 2952, "reported_total_meals": 1128, "reported_total_transportation": 200}}]`

### v3_harder_eval_000019
- request: 丽江 2026-05-07->2026-05-10 days=4 transport=打车 hotel=亲子酒店 prefs=['亲子', '老人友好', '博物馆', '城市公园', '特色餐厅']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "束河古镇", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-05-07", "day_index": 0, "name": "束河古镇"}, {"date": "2026-05-10", "day_index": 3, "name": "束河古镇"}]}, {"name_key": "黑龙潭", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-05-08", "day_index": 1, "name": "黑龙潭"}, {"date": "2026-05-09", "day_index": 2, "name": "黑龙潭"}]}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 640, "expected_total_attractions": 1280, "reported_total_attractions": 960, "meal_per_person_cost_sum": 1080, "expected_total_meals": 2160, "reported_total_meals": 720, "reported_total_transportation": 1200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 640, "expected_total_attractions": 1280, "reported_total_attractions": 960, "meal_per_person_cost_sum": 1080, "expected_total_meals": 2160, "reported_total_meals": 720, "reported_total_transportation": 1200}}]`

### v3_harder_eval_000021
- request: 上海 2026-06-17->2026-06-20 days=4 transport=打车 hotel=高端酒店 prefs=['高端酒店', '艺术', '特色餐厅', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "3号仓库·餐厅", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-06-17", "type": "lunch", "name": "3号仓库·餐厅(徐汇绿地缤纷城店)"}, {"date": "2026-06-18", "type": "lunch", "name": "3号仓库·餐厅(上海首店)"}, {"date": "2026-06-19", "type": "dinner", "name": "3号仓库·餐厅(徐汇绿地缤纷城店)"}, {"date": "2026-06-20", "type": "lunch", "name": "3号仓库·餐厅(上海首店)"}]}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 545, "expected_total_attractions": 1090, "reported_total_attractions": 1155, "meal_per_person_cost_sum": 2370, "expected_total_meals": 4740, "reported_total_meals": 2132, "reported_total_transportation": 1200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 545, "expected_total_attractions": 1090, "reported_total_attractions": 1155, "meal_per_person_cost_sum": 2370, "expected_total_meals": 4740, "reported_total_meals": 2132, "reported_total_transportation": 1200}}]`
