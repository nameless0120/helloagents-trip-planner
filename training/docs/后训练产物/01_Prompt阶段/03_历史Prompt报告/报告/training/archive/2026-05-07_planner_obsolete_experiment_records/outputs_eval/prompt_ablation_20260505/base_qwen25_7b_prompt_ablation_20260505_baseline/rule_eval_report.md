# Rule Eval Report: base_qwen25_7b_prompt_ablation_20260505_baseline

- records: 300
- generations: `training/outputs/eval/prompt_ablation_20260505/base_qwen25_7b_prompt_ablation_20260505_baseline/generations.jsonl`
- records_path: `training/data/v3/eval_harder_prompt_ablation_20260505/baseline/records.jsonl`

## Boolean Metrics

| Metric | Pass | Total | Rate |
| --- | ---: | ---: | ---: |
| accommodation_type_ok | 258 | 297 | 86.87% |
| attraction_budget_consistent | 36 | 297 | 12.12% |
| attraction_budget_party_relation_ok | 75 | 297 | 25.25% |
| attraction_count_ok | 297 | 297 | 100.00% |
| attraction_diversity_ok | 248 | 297 | 83.50% |
| attraction_grounding_ok | 291 | 297 | 97.98% |
| attraction_repeat_limit_ok | 248 | 297 | 83.50% |
| budget_arithmetic_consistent | 150 | 297 | 50.51% |
| budget_consistent | 150 | 297 | 50.51% |
| budget_level_aligned | 105 | 297 | 35.35% |
| budget_preference_aligned | 105 | 297 | 35.35% |
| budget_relationship_ok | 18 | 297 | 6.06% |
| budget_user_constraint_ok | 231 | 297 | 77.78% |
| budget_within_user_budget | 275 | 297 | 92.59% |
| city_ok | 297 | 297 | 100.00% |
| date_range_ok | 297 | 297 | 100.00% |
| day_dates_ok | 297 | 297 | 100.00% |
| day_index_ok | 297 | 297 | 100.00% |
| days_len_ok | 297 | 297 | 100.00% |
| dpo_soft_pass | 0 | 297 | 0.00% |
| hard_pass | 0 | 297 | 0.00% |
| hotel_budget_covers_nights | 108 | 297 | 36.36% |
| hotel_budget_relation_ok | 120 | 297 | 40.40% |
| hotel_distance_placeholder_ok | 297 | 297 | 100.00% |
| hotel_grounding_ok | 296 | 297 | 99.66% |
| invalid_hotel_name_ok | 297 | 297 | 100.00% |
| json_extract_ok | 299 | 300 | 99.67% |
| legacy_hard_pass | 12 | 297 | 4.04% |
| location_object_ok | 297 | 297 | 100.00% |
| meal_budget_consistent | 0 | 297 | 0.00% |
| meal_complete | 297 | 297 | 100.00% |
| meal_cost_scale_ok | 203 | 297 | 68.35% |
| meal_diversity_ok | 212 | 297 | 71.38% |
| meal_grounding_ok | 167 | 297 | 56.23% |
| meal_lunch_dinner_same_day_ok | 237 | 297 | 79.80% |
| meal_repeat_limit_ok | 241 | 297 | 81.14% |
| meal_specific_ok | 285 | 297 | 95.96% |
| meal_valid_semantics_ok | 186 | 297 | 62.63% |
| middle_hotel_ok | 297 | 297 | 100.00% |
| schema_ok | 297 | 300 | 99.00% |
| sft_budget_semantic_hard_pass | 5 | 297 | 1.68% |
| sft_hard_pass | 0 | 297 | 0.00% |
| transportation_budget_nonnegative | 297 | 297 | 100.00% |
| weather_dates_ok | 297 | 297 | 100.00% |
| weather_match | 296 | 297 | 99.66% |

## Numeric Metrics

```json
{
  "attraction_diversity_unique_rate": {
    "avg": 0.9692,
    "p50": 1.0,
    "p90": 1.0
  },
  "attraction_grounding_rate": {
    "avg": 0.996,
    "p50": 1.0,
    "p90": 1.0
  },
  "hotel_grounding_rate": {
    "avg": 0.9992,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_diversity_unique_rate": {
    "avg": 0.5451,
    "p50": 0.5,
    "p90": 1.0
  },
  "meal_food_pois_grounding_rate": {
    "avg": 0.8328,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_grounding_rate": {
    "avg": 0.8328,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_semantic_valid_rate": {
    "avg": 0.8972,
    "p50": 1.0,
    "p90": 1.0
  }
}
```

## Failure Types

```json
{
  "meal_budget_inconsistent": 297,
  "budget_relationship_mismatch": 279,
  "attraction_budget_inconsistent": 261,
  "budget_preference_mismatch": 192,
  "hotel_budget_underestimated": 189,
  "budget_arithmetic_inconsistent": 147,
  "meal_invalid_name": 111,
  "meal_cost_scale_too_low": 94,
  "budget_hard_constraint_exceeded": 66,
  "meal_same_day_lunch_dinner_repeat": 60,
  "meal_repeat_too_many": 56,
  "attraction_repeat_too_many": 49,
  "accommodation_type_mismatch": 39,
  "meal_grounding_miss": 19,
  "meal_placeholder": 12,
  "schema": 2,
  "weather_mismatch": 1,
  "json_extract": 1
}
```

## Failure Examples

### v3_harder_eval_000004
- request: 张家界 2026-05-07->2026-05-09 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 2, "party_total": 1, "room_count": 1, "priced_nights": 2, "expected_min_total_hotels": 800, "reported_total_hotels": 1200, "diff": 400, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 320, "expected_total_attractions": 320, "reported_total_attractions": 240, "meal_per_person_cost_sum": 418, "expected_total_meals": 418, "reported_total_meals": 240, "reported_total_transportation": 600}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 320, "expected_total_attractions": 320, "reported_total_attractions": 240, "meal_per_person_cost_sum": 418, "expected_total_meals": 418, "reported_total_meals": 240, "reported_total_transportation": 600}}]`

### v3_harder_eval_000014
- request: 成都 2026-06-02->2026-06-04 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆']
- errors: `[{"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-06-04", "type": "dinner", "name": "酒店晚餐", "reason": "generic_lodging_meal"}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 115, "expected_total_attractions": 115, "reported_total_attractions": 275, "meal_per_person_cost_sum": 724, "expected_total_meals": 724, "reported_total_meals": 399, "reported_total_transportation": 600}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 115, "expected_total_attractions": 115, "reported_total_attractions": 275, "meal_per_person_cost_sum": 724, "expected_total_meals": 724, "reported_total_meals": 399, "reported_total_transportation": 600}}]`

### v3_harder_eval_000008
- request: 大理 2026-05-07->2026-05-09 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物']
- errors: `[{"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-05-09", "type": "dinner", "name": "大理青朴酒店", "reason": "hotel_or_lodging_name"}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 2, "party_total": 3, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 4500, "reported_total_hotels": 2250, "diff": -2250, "covers_nights": false}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 75, "expected_total_attractions": 225, "reported_total_attractions": 225, "meal_per_person_cost_sum": 1965, "expected_total_meals": 5895, "reported_total_meals": 1107, "reported_total_transportation": 600}}]`

### v3_harder_eval_000002
- request: 杭州 2026-04-27->2026-04-30 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '夜市', '老字号', '城市漫步']
- errors: `[{"stage": "rule", "type": "accommodation_type_mismatch", "details": [{"date": "2026-04-30", "day_index": 3, "expected": "经济型酒店", "got": "青年旅舍"}]}, {"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-04-30", "type": "dinner", "name": "杭州拣枝而栖青年旅舍(龙湖滨江天街江陵路地铁站店)附近餐厅", "reason": "hotel_or_lodging_name"}]}, {"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-04-29", "lunch": "杭州酒家(延安路店)", "dinner": "杭州酒家(延安路店)"}]}]`

### v3_harder_eval_000007
- request: 成都 2026-05-07->2026-05-11 days=5 transport=公共交通 hotel=民宿 prefs=['小众展馆', '咖啡', '艺术', '城市漫步', '特色餐厅']
- errors: `[{"stage": "rule", "type": "meal_placeholder", "details": [{"date": "2026-05-08", "type": "dinner", "name": "M Stand(成都SKP店)"}, {"date": "2026-05-09", "type": "lunch", "name": "M Stand(成都SKP店)"}, {"date": "2026-05-10", "type": "dinner", "name": "M Stand(成都SKP店)"}]}, {"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-05-08", "type": "dinner", "name": "M Stand(成都SKP店)", "reason": "unknown_food_semantics"}, {"date": "2026-05-09", "type": "lunch", "name": "M Stand(成都SKP店)", "reason": "unknown_food_semantics"}, {"date": "2026-05-10", "type": "dinner", "name": "M Stand(成都SKP店)", "reason": "unknown_food_semantics"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "星巴克", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-05-07", "type": "dinner", "name": "星巴克(成都环球中心II店)"}, {"date": "2026-05-08", "type": "lunch", "name": "星巴克(成都SKP店)"}, {"date": "2026-05-09", "type": "dinner", "name": "星巴克(成都环球中心II店)"}, {"date": "2026-05-10", "type": "lunch", "name": "星巴克(成都SKP店)"}, {"date": "2026-05-11", "type": "dinner", "name": "星巴克(成都环球中心II店)"}]}]}]`

### v3_harder_eval_000009
- request: 苏州 2026-04-26->2026-04-29 days=4 transport=打车 hotel=亲子酒店 prefs=['亲子', '老人友好', '博物馆', '城市公园', '特色餐厅']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 4, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 7500, "reported_total_hotels": 4000, "diff": -3500, "covers_nights": false}}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 5419, "total": 8459, "diff": -3040, "requested_budget": {"available": true, "amount": 9100, "scope": "total", "party_size": 4, "total": 9100, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "soft"}, "per_person_day": 528.69, "budget_level": "comfortable", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "soft", "amount": 9100, "target_min_ratio": 0.65, "target_max_ratio": 1.05, "target_min_total": 5900, "target_max_total": 9600, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 4, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 7500, "reported_total_hotels": 4000, "diff": -3500, "covers_nights": false}, "hotel_budget_covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 175, "expected_total_attractions": 700, "reported_total_attractions": 259, "meal_per_person_cost_sum": 552, "expected_total_meals": 2208, "reported_total_meals": 360, "reported_total_transportation": 800}}]`

### v3_harder_eval_000016
- request: 苏州 2026-06-02->2026-06-05 days=4 transport=自驾 hotel=亲子酒店 prefs=['亲子', '动物园', '海洋馆', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "accommodation_type_mismatch", "details": [{"date": "2026-06-05", "day_index": 3, "expected": "亲子酒店", "got": "无住宿"}]}, {"stage": "rule", "type": "meal_grounding_miss", "details": [{"date": "2026-06-02", "type": "lunch", "name": "苏州乐园森林世界餐厅"}, {"date": "2026-06-02", "type": "dinner", "name": "苏州乐园森林世界餐厅"}, {"date": "2026-06-03", "type": "lunch", "name": "苏州乐园森林世界餐厅"}, {"date": "2026-06-03", "type": "dinner", "name": "苏州乐园森林世界餐厅"}, {"date": "2026-06-04", "type": "lunch", "name": "苏州乐园森林世界餐厅"}, {"date": "2026-06-04", "type": "dinner", "name": "苏州乐园森林世界餐厅"}, {"date": "2026-06-05", "type": "lunch", "name": "苏州乐园森林世界餐厅"}, {"date": "2026-06-05", "type": "dinner", "name": "苏州乐园森林世界餐厅"}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 3, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 7500, "reported_total_hotels": 3750, "diff": -3750, "covers_nights": false}}]`

### v3_harder_eval_000001
- request: 桂林 2026-08-31->2026-09-03 days=4 transport=打车 hotel=高端酒店 prefs=['高端酒店', '艺术', '特色餐厅', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "山野间餐厅", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-08-31", "type": "breakfast", "name": "山野间餐厅"}, {"date": "2026-09-01", "type": "breakfast", "name": "山野间餐厅"}, {"date": "2026-09-02", "type": "breakfast", "name": "山野间餐厅"}, {"date": "2026-09-03", "type": "breakfast", "name": "山野间餐厅"}]}, {"name_key": "岩洞餐厅.天然岩洞特色菜", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-08-31", "type": "lunch", "name": "岩洞餐厅.天然岩洞特色菜(千古情店)"}, {"date": "2026-09-01", "type": "lunch", "name": "岩洞餐厅.天然岩洞特色菜(千古情店)"}, {"date": "2026-09-02", "type": "lunch", "name": "岩洞餐厅.天然岩洞特色菜(千古情店)"}, {"date": "2026-09-03", "type": "lunch", "name": "岩洞餐厅.天然岩洞特色菜(千古情店)"}]}, {"name_key": "味道制造·桂林菜", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-08-31", "type": "dinner", "name": "味道制造·桂林菜(七星店)"}, {"date": "2026-09-01", "type": "dinner", "name": "味道制造·桂林菜(七星店)"}, {"date": "2026-09-02", "type": "dinner", "name": "味道制造·桂林菜(七星店)"}, {"date": "2026-09-03", "type": "dinner", "name": "味道制造·桂林菜(七星店)"}]}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 525, "expected_total_attractions": 1050, "reported_total_attractions": 1155, "meal_per_person_cost_sum": 1056, "expected_total_meals": 2112, "reported_total_meals": 612, "reported_total_transportation": 800}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 525, "expected_total_attractions": 1050, "reported_total_attractions": 1155, "meal_per_person_cost_sum": 1056, "expected_total_meals": 2112, "reported_total_meals": 612, "reported_total_transportation": 800}}]`

### v3_harder_eval_000011
- request: 福州 2026-06-17->2026-06-20 days=4 transport=打车 hotel=高端酒店 prefs=['高端酒店', '艺术', '特色餐厅', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-06-20", "lunch": "紫阳海鲜楼·传承闽味(华林路店)", "dinner": "紫阳海鲜楼·传承闽味(华林路店)"}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 80, "expected_total_attractions": 160, "reported_total_attractions": 240, "meal_per_person_cost_sum": 1736, "expected_total_meals": 3472, "reported_total_meals": 1260, "reported_total_transportation": 800}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 80, "expected_total_attractions": 160, "reported_total_attractions": 240, "meal_per_person_cost_sum": 1736, "expected_total_meals": 3472, "reported_total_meals": 1260, "reported_total_transportation": 800}}]`

### v3_harder_eval_000006
- request: 南京 2026-07-02->2026-07-05 days=4 transport=自驾 hotel=亲子酒店 prefs=['亲子', '动物园', '海洋馆', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "accommodation_type_mismatch", "details": [{"date": "2026-07-05", "day_index": 3, "expected": "亲子酒店", "got": "无住宿"}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 3, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 3300, "reported_total_hotels": 1650, "diff": -1650, "covers_nights": false}}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 3110, "total": 3190, "diff": -80, "requested_budget": {"available": true, "amount": 4000, "scope": "total", "party_size": 3, "total": 4000, "source": "budget_constraint", "budget_level": "standard", "strictness": "hard"}, "per_person_day": 265.83, "budget_level": "standard", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "standard", "strictness": "hard", "amount": 4000, "target_min_ratio": 0.55, "target_max_ratio": 1.0, "target_min_total": 2200, "target_max_total": 4000, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 3, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 3300, "reported_total_hotels": 1650, "diff": -1650, "covers_nights": false}, "hotel_budget_covers_nights": false}}]`

### v3_harder_eval_000000
- request: 昆明 2026-04-03->2026-04-07 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_grounding_miss", "details": [{"date": "2026-04-03", "type": "lunch", "name": "云南民族村餐厅"}, {"date": "2026-04-03", "type": "dinner", "name": "云南民族村餐厅"}, {"date": "2026-04-04", "type": "lunch", "name": "云南民族村餐厅"}, {"date": "2026-04-04", "type": "dinner", "name": "云南民族村餐厅"}, {"date": "2026-04-05", "type": "lunch", "name": "云南民族村餐厅"}, {"date": "2026-04-05", "type": "dinner", "name": "云南民族村餐厅"}, {"date": "2026-04-06", "type": "lunch", "name": "云南民族村餐厅"}, {"date": "2026-04-06", "type": "dinner", "name": "云南民族村餐厅"}, {"date": "2026-04-07", "type": "lunch", "name": "云南民族村餐厅"}, {"date": "2026-04-07", "type": "dinner", "name": "云南民族村餐厅"}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 4, "party_total": 5, "room_count": 3, "priced_nights": 4, "expected_min_total_hotels": 4800, "reported_total_hotels": 1600, "diff": -3200, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 5, "hotel_room_count": 3, "attraction_ticket_sum": 110, "expected_total_attractions": 550, "reported_total_attractions": 290, "meal_per_person_cost_sum": 800, "expected_total_meals": 4000, "reported_total_meals": 480, "reported_total_transportation": 1000}}]`

### v3_harder_eval_000013
- request: 武汉 2026-05-05->2026-05-09 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-05-06", "type": "dinner", "name": "解放公园餐厅", "reason": "non_food_poi_name"}, {"date": "2026-05-07", "type": "lunch", "name": "江汉关博物馆餐厅", "reason": "non_food_poi_name"}, {"date": "2026-05-08", "type": "lunch", "name": "解放公园餐厅", "reason": "non_food_poi_name"}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 70, "expected_total_attractions": 140, "reported_total_attractions": 210, "meal_per_person_cost_sum": 800, "expected_total_meals": 1600, "reported_total_meals": 480, "reported_total_transportation": 800}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 70, "expected_total_attractions": 140, "reported_total_attractions": 210, "meal_per_person_cost_sum": 800, "expected_total_meals": 1600, "reported_total_meals": 480, "reported_total_transportation": 800}}]`

### v3_harder_eval_000005
- request: 广州 2026-07-02->2026-07-06 days=5 transport=公共交通 hotel=民宿 prefs=['摄影', '自然风光', '城市漫步', '本地菜']
- errors: `[{"stage": "rule", "type": "accommodation_type_mismatch", "details": [{"date": "2026-07-06", "day_index": 4, "expected": "民宿", "got": "无住宿"}]}, {"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-07-06", "type": "dinner", "name": "无", "reason": "empty_or_none"}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 450, "expected_total_attractions": 450, "reported_total_attractions": 600, "meal_per_person_cost_sum": 889, "expected_total_meals": 889, "reported_total_meals": 390, "reported_total_transportation": 200}}]`

### v3_harder_eval_000003
- request: 西安 2025-05-03->2025-05-07 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 3470, "total": 3630, "diff": -160, "requested_budget": {"available": true, "amount": 3700, "scope": "total", "party_size": 2, "total": 3700, "source": "budget_constraint", "budget_level": "standard", "strictness": "hard"}, "per_person_day": 363.0, "budget_level": "standard", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "standard", "strictness": "hard", "amount": 3700, "target_min_ratio": 0.55, "target_max_ratio": 1.0, "target_min_total": 2000, "target_max_total": 3700, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 4, "party_total": 2, "room_count": 1, "priced_nights": 4, "expected_min_total_hotels": 1800, "reported_total_hotels": 1800, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 224, "expected_total_attractions": 448, "reported_total_attractions": 430, "meal_per_person_cost_sum": 550, "expected_total_meals": 1100, "reported_total_meals": 240, "reported_total_transportation": 1000}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 224, "expected_total_attractions": 448, "reported_total_attractions": 430, "meal_per_person_cost_sum": 550, "expected_total_meals": 1100, "reported_total_meals": 240, "reported_total_transportation": 1000}}]`

### v3_harder_eval_000010
- request: 西安 2026-04-19->2026-04-23 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 4, "party_total": 5, "room_count": 3, "priced_nights": 4, "expected_min_total_hotels": 5400, "reported_total_hotels": 2250, "diff": -3150, "covers_nights": false}}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 4300, "total": 4200, "diff": 100, "requested_budget": {"available": true, "amount": 11100, "scope": "total", "party_size": 5, "total": 11100, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "hard"}, "per_person_day": 168.0, "budget_level": "comfortable", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "hard", "amount": 11100, "target_min_ratio": 0.65, "target_max_ratio": 1.0, "target_min_total": 7200, "target_max_total": 11100, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 4, "party_total": 5, "room_count": 3, "priced_nights": 4, "expected_min_total_hotels": 5400, "reported_total_hotels": 2250, "diff": -3150, "covers_nights": false}, "hotel_budget_covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 5, "hotel_room_count": 3, "attraction_ticket_sum": 254, "expected_total_attractions": 1270, "reported_total_attractions": 450, "meal_per_person_cost_sum": 650, "expected_total_meals": 3250, "reported_total_meals": 600, "reported_total_transportation": 1000}}]`

### v3_harder_eval_000015
- request: 南京 2026-04-03->2026-04-07 days=5 transport=公共交通 hotel=民宿 prefs=['摄影', '自然风光', '城市漫步', '本地菜']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "玄武湖景区", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-04-03", "day_index": 0, "name": "玄武湖景区"}, {"date": "2026-04-05", "day_index": 2, "name": "玄武湖景区"}]}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 4, "party_total": 1, "room_count": 1, "priced_nights": 5, "expected_min_total_hotels": 1500, "reported_total_hotels": 1200, "diff": -300, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 143, "expected_total_attractions": 143, "reported_total_attractions": 220, "meal_per_person_cost_sum": 1190, "expected_total_meals": 1190, "reported_total_meals": 2340, "reported_total_transportation": 1000}}]`

### v3_harder_eval_000012
- request: 洛阳 2025-05-03->2025-05-06 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '夜市', '老字号', '城市漫步']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 4, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 1200, "reported_total_hotels": 600, "diff": -600, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 400, "expected_total_attractions": 1600, "reported_total_attractions": 240, "meal_per_person_cost_sum": 1772, "expected_total_meals": 7088, "reported_total_meals": 920, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 400, "expected_total_attractions": 1600, "reported_total_attractions": 240, "meal_per_person_cost_sum": 1772, "expected_total_meals": 7088, "reported_total_meals": 920, "reported_total_transportation": 200}}]`

### v3_harder_eval_000024
- request: 济南 2026-05-06->2026-05-08 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆']
- errors: `[{"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-05-08", "type": "dinner", "name": "酒店晚餐", "reason": "generic_lodging_meal"}]}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 160, "expected_total_attractions": 160, "reported_total_attractions": 240, "meal_per_person_cost_sum": 513, "expected_total_meals": 513, "reported_total_meals": 318, "reported_total_transportation": 600}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 160, "expected_total_attractions": 160, "reported_total_attractions": 240, "meal_per_person_cost_sum": 513, "expected_total_meals": 513, "reported_total_meals": 318, "reported_total_transportation": 600}}]`

### v3_harder_eval_000018
- request: 天津 2026-07-02->2026-07-04 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-07-03", "lunch": "苏焰·地标天津菜(多伦道店)", "dinner": "苏焰·地标天津菜(金海道店)"}, {"date": "2026-07-04", "lunch": "龙四爷铜锅涮肉(海河地标店)", "dinner": "龙四爷铜锅涮肉(海河地标店)"}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 2, "party_total": 3, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 7200, "reported_total_hotels": 3600, "diff": -3600, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 130, "expected_total_attractions": 390, "reported_total_attractions": 240, "meal_per_person_cost_sum": 1338, "expected_total_meals": 4014, "reported_total_meals": 1080, "reported_total_transportation": 600}}]`

### v3_harder_eval_000019
- request: 丽江 2026-05-07->2026-05-10 days=4 transport=打车 hotel=亲子酒店 prefs=['亲子', '老人友好', '博物馆', '城市公园', '特色餐厅']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "丽江古城", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-05-07", "day_index": 0, "name": "丽江古城"}, {"date": "2026-05-10", "day_index": 3, "name": "丽江古城"}]}]}, {"stage": "rule", "type": "meal_grounding_miss", "details": [{"date": "2026-05-07", "type": "lunch", "name": "丽江古城内的特色小吃"}, {"date": "2026-05-07", "type": "dinner", "name": "丽江古城内的特色餐厅"}, {"date": "2026-05-08", "type": "lunch", "name": "丽江古城内的特色小吃"}, {"date": "2026-05-08", "type": "dinner", "name": "丽江古城内的特色餐厅"}, {"date": "2026-05-09", "type": "lunch", "name": "丽江古城内的特色小吃"}, {"date": "2026-05-09", "type": "dinner", "name": "丽江古城内的特色餐厅"}, {"date": "2026-05-10", "type": "lunch", "name": "丽江古城内的特色小吃"}, {"date": "2026-05-10", "type": "dinner", "name": "丽江古城内的特色餐厅"}]}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 2780, "total": 2800, "diff": -20, "requested_budget": {"available": true, "amount": 5300, "scope": "total", "party_size": 2, "total": 5300, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "soft"}, "per_person_day": 350.0, "budget_level": "comfortable", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "soft", "amount": 5300, "target_min_ratio": 0.65, "target_max_ratio": 1.05, "target_min_total": 3400, "target_max_total": 5600, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 2, "room_count": 1, "priced_nights": 3, "expected_min_total_hotels": 1500, "reported_total_hotels": 1500, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`
