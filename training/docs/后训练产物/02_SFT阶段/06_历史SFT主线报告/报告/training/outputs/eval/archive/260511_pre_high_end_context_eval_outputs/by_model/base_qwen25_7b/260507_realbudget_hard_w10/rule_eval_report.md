# Rule Eval Report: 260507_realbudget_hard_w10

- records: 300
- generations: `training/outputs/eval/by_model/base_qwen25_7b/260507_realbudget_hard_w10/generations.jsonl`
- records_path: `training/data/v3/eval_hard/records.jsonl`

## Boolean Metrics

| Metric | Pass | Total | Rate |
| --- | ---: | ---: | ---: |
| accommodation_type_ok | 286 | 299 | 95.65% |
| attraction_budget_consistent | 46 | 299 | 15.38% |
| attraction_budget_party_relation_ok | 84 | 299 | 28.09% |
| attraction_count_ok | 299 | 299 | 100.00% |
| attraction_diversity_ok | 239 | 299 | 79.93% |
| attraction_grounding_ok | 293 | 299 | 97.99% |
| attraction_repeat_limit_ok | 239 | 299 | 79.93% |
| budget_arithmetic_consistent | 186 | 299 | 62.21% |
| budget_consistent | 186 | 299 | 62.21% |
| budget_level_aligned | 31 | 299 | 10.37% |
| budget_preference_aligned | 31 | 299 | 10.37% |
| budget_relationship_ok | 11 | 299 | 3.68% |
| budget_selection_ok | 108 | 299 | 36.12% |
| budget_user_constraint_ok | 298 | 299 | 99.67% |
| budget_within_user_budget | 299 | 299 | 100.00% |
| city_ok | 299 | 299 | 100.00% |
| date_range_ok | 299 | 299 | 100.00% |
| day_dates_ok | 299 | 299 | 100.00% |
| day_index_ok | 299 | 299 | 100.00% |
| days_len_ok | 299 | 299 | 100.00% |
| dpo_soft_pass | 7 | 299 | 2.34% |
| dpo_soft_recomputed_budget_pass | 23 | 299 | 7.69% |
| hard_pass | 249 | 299 | 83.28% |
| hotel_budget_covers_nights | 80 | 299 | 26.76% |
| hotel_budget_relation_ok | 127 | 299 | 42.47% |
| hotel_distance_placeholder_ok | 299 | 299 | 100.00% |
| hotel_grounding_ok | 297 | 299 | 99.33% |
| invalid_hotel_name_ok | 299 | 299 | 100.00% |
| json_extract_ok | 299 | 300 | 99.67% |
| legacy_hard_pass | 16 | 299 | 5.35% |
| location_object_ok | 299 | 299 | 100.00% |
| meal_budget_consistent | 1 | 299 | 0.33% |
| meal_complete | 299 | 299 | 100.00% |
| meal_cost_scale_ok | 81 | 299 | 27.09% |
| meal_diversity_ok | 89 | 299 | 29.77% |
| meal_grounding_ok | 267 | 299 | 89.30% |
| meal_lunch_dinner_same_day_ok | 239 | 299 | 79.93% |
| meal_repeat_limit_ok | 98 | 299 | 32.78% |
| meal_specific_ok | 289 | 299 | 96.66% |
| meal_valid_semantics_ok | 270 | 299 | 90.30% |
| middle_hotel_ok | 298 | 299 | 99.67% |
| recomputed_budget_fit_ok | 108 | 299 | 36.12% |
| recomputed_budget_hard_ok | 281 | 299 | 93.98% |
| recomputed_budget_level_aligned | 108 | 299 | 36.12% |
| recomputed_budget_preference_aligned | 108 | 299 | 36.12% |
| recomputed_budget_user_constraint_ok | 281 | 299 | 93.98% |
| recomputed_budget_within_user_budget | 291 | 299 | 97.32% |
| schema_ok | 299 | 300 | 99.67% |
| sft_budget_semantic_hard_pass | 4 | 299 | 1.34% |
| sft_hard_pass | 249 | 299 | 83.28% |
| sft_no_budget_sum_hard_pass | 249 | 299 | 83.28% |
| sft_strict_hard_pass | 0 | 299 | 0.00% |
| transportation_budget_nonnegative | 299 | 299 | 100.00% |
| weather_dates_ok | 299 | 299 | 100.00% |
| weather_match | 298 | 299 | 99.67% |

## Numeric Metrics

```json
{
  "attraction_diversity_unique_rate": {
    "avg": 0.9576,
    "p50": 1.0,
    "p90": 1.0
  },
  "attraction_grounding_rate": {
    "avg": 0.9966,
    "p50": 1.0,
    "p90": 1.0
  },
  "hotel_grounding_rate": {
    "avg": 0.9933,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_diversity_unique_rate": {
    "avg": 0.544,
    "p50": 0.5,
    "p90": 0.9167
  },
  "meal_food_pois_grounding_rate": {
    "avg": 0.9775,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_grounding_rate": {
    "avg": 0.9775,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_semantic_valid_rate": {
    "avg": 0.9803,
    "p50": 1.0,
    "p90": 1.0
  },
  "recomputed_budget_per_person_day": {
    "avg": 608.2576,
    "p50": 557.67,
    "p90": 890.33
  },
  "recomputed_budget_total": {
    "avg": 6565.9365,
    "p50": 5932.0,
    "p90": 12266.0
  }
}
```

## Failure Types

```json
{
  "meal_budget_inconsistent": 297,
  "budget_relationship_mismatch": 288,
  "budget_preference_mismatch": 268,
  "attraction_budget_inconsistent": 253,
  "hotel_budget_underestimated": 219,
  "meal_cost_scale_too_low": 218,
  "meal_repeat_too_many": 201,
  "budget_arithmetic_inconsistent": 113,
  "attraction_repeat_too_many": 60,
  "meal_same_day_lunch_dinner_repeat": 60,
  "meal_invalid_name": 29,
  "accommodation_type_mismatch": 13,
  "meal_placeholder": 10,
  "meal_grounding_miss": 3,
  "budget_hard_constraint_exceeded": 1,
  "middle_hotel_null": 1,
  "weather_mismatch": 1,
  "json_extract": 1
}
```

## Failure Examples

### v3_hard_realbudget_eval_000004
- request: 张家界 2026-05-11->2026-05-13 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆']
- errors: `[{"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-05-11", "type": "dinner", "name": "老妈下饭菜(张家界中天鹭鸶湾一期店)", "reason": "unknown_food_semantics"}, {"date": "2026-05-12", "type": "dinner", "name": "老妈下饭菜(张家界中天鹭鸶湾一期店)", "reason": "unknown_food_semantics"}, {"date": "2026-05-13", "type": "dinner", "name": "老妈下饭菜(张家界中天鹭鸶湾一期店)", "reason": "unknown_food_semantics"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "索溪山寨·湘西民间土菜", "count": 3, "max_allowed": 2, "occurrences": [{"date": "2026-05-11", "type": "lunch", "name": "索溪山寨·湘西民间土菜(标志门店)"}, {"date": "2026-05-12", "type": "lunch", "name": "索溪山寨·湘西民间土菜(溪布街店)"}, {"date": "2026-05-13", "type": "lunch", "name": "索溪山寨·湘西民间土菜(溪布街店)"}]}, {"name_key": "老妈下饭菜", "count": 3, "max_allowed": 2, "occurrences": [{"date": "2026-05-11", "type": "dinner", "name": "老妈下饭菜(张家界中天鹭鸶湾一期店)"}, {"date": "2026-05-12", "type": "dinner", "name": "老妈下饭菜(张家界中天鹭鸶湾一期店)"}, {"date": "2026-05-13", "type": "dinner", "name": "老妈下饭菜(张家界中天鹭鸶湾一期店)"}]}]}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 3050, "total": 2850, "diff": 200, "requested_budget": {"available": true, "amount": 3200, "scope": "total", "party_size": 1, "total": 3200, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "hard"}, "per_person_day": 950.0, "budget_level": "comfortable", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "hard", "amount": 3200, "target_min_ratio": 0.7, "target_max_ratio": 1.0, "target_min_total": 2200, "target_max_total": 3200, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 2, "party_total": 1, "room_count": 1, "priced_nights": 3, "expected_min_total_hotels": 1200, "reported_total_hotels": 1200, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_hard_realbudget_eval_000008
- request: 大理 2026-05-11->2026-05-13 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 2, "party_total": 3, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 4500, "reported_total_hotels": 2250, "diff": -2250, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 40, "expected_total_attractions": 120, "reported_total_attractions": 210, "meal_per_person_cost_sum": 441, "expected_total_meals": 1323, "reported_total_meals": 468, "reported_total_transportation": 600}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 40, "expected_total_attractions": 120, "reported_total_attractions": 210, "meal_per_person_cost_sum": 441, "expected_total_meals": 1323, "reported_total_meals": 468, "reported_total_transportation": 600}}]`

### v3_hard_realbudget_eval_000002
- request: 杭州 2026-05-01->2026-05-04 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '夜市', '老字号', '城市漫步']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "方老大", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-05-01", "type": "breakfast", "name": "方老大"}, {"date": "2026-05-02", "type": "breakfast", "name": "方老大"}, {"date": "2026-05-03", "type": "breakfast", "name": "方老大"}, {"date": "2026-05-04", "type": "breakfast", "name": "方老大"}]}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 4, "room_count": 2, "priced_nights": 4, "expected_min_total_hotels": 2000, "reported_total_hotels": 1000, "diff": -1000, "covers_nights": false}}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 2976, "total": 2176, "diff": 800, "requested_budget": {"available": true, "amount": 6300, "scope": "total", "party_size": 4, "total": 6300, "source": "budget_constraint", "budget_level": "limited", "strictness": "hard"}, "per_person_day": 136.0, "budget_level": "limited", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "limited", "strictness": "hard", "amount": 6300, "target_min_ratio": 0.72, "target_max_ratio": 1.0, "target_min_total": 4500, "target_max_total": 6300, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 4, "room_count": 2, "priced_nights": 4, "expected_min_total_hotels": 2000, "reported_total_hotels": 1000, "diff": -1000, "covers_nights": false}, "hotel_budget_covers_nights": false}}]`

### v3_hard_realbudget_eval_000006
- request: 南京 2026-07-06->2026-07-09 days=4 transport=自驾 hotel=亲子酒店 prefs=['亲子', '动物园', '海洋馆', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "许阿姨糕团店", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-07-06", "type": "breakfast", "name": "许阿姨糕团店(南京总店)"}, {"date": "2026-07-07", "type": "breakfast", "name": "许阿姨糕团店(南京总店)"}, {"date": "2026-07-08", "type": "breakfast", "name": "许阿姨糕团店(南京总店)"}, {"date": "2026-07-09", "type": "breakfast", "name": "许阿姨糕团店(南京总店)"}]}, {"name_key": "南京大牌档", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-07-06", "type": "lunch", "name": "南京大牌档(中山陵紫金坊店)"}, {"date": "2026-07-07", "type": "lunch", "name": "南京大牌档(1912总统府店)"}, {"date": "2026-07-08", "type": "lunch", "name": "南京大牌档(中山陵紫金坊店)"}, {"date": "2026-07-09", "type": "lunch", "name": "南京大牌档(1912总统府店)"}]}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 3, "room_count": 2, "priced_nights": 4, "expected_min_total_hotels": 4400, "reported_total_hotels": 2200, "diff": -2200, "covers_nights": false}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 0, "expected_total_attractions": 0, "reported_total_attractions": 0, "meal_per_person_cost_sum": 530, "expected_total_meals": 1590, "reported_total_meals": 1080, "reported_total_transportation": 800}}]`

### v3_hard_realbudget_eval_000001
- request: 桂林 2026-09-04->2026-09-07 days=4 transport=打车 hotel=高端酒店 prefs=['高端酒店', '艺术', '特色餐厅', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 2, "room_count": 1, "priced_nights": 4, "expected_min_total_hotels": 3000, "reported_total_hotels": 2250, "diff": -750, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 625, "expected_total_attractions": 1250, "reported_total_attractions": 1110, "meal_per_person_cost_sum": 539, "expected_total_meals": 1078, "reported_total_meals": 1260, "reported_total_transportation": 800}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 625, "expected_total_attractions": 1250, "reported_total_attractions": 1110, "meal_per_person_cost_sum": 539, "expected_total_meals": 1078, "reported_total_meals": 1260, "reported_total_transportation": 800}}]`

### v3_hard_realbudget_eval_000007
- request: 成都 2026-05-11->2026-05-15 days=5 transport=公共交通 hotel=民宿 prefs=['小众展馆', '咖啡', '艺术', '城市漫步', '特色餐厅']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "春熙路步行街", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-05-11", "day_index": 0, "name": "春熙路步行街"}, {"date": "2026-05-15", "day_index": 4, "name": "春熙路步行街"}]}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "山面包", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-05-11", "type": "breakfast", "name": "山面包(东郊记忆店)"}, {"date": "2026-05-12", "type": "breakfast", "name": "山面包(东郊记忆店)"}, {"date": "2026-05-13", "type": "breakfast", "name": "山面包(东郊记忆店)"}, {"date": "2026-05-14", "type": "breakfast", "name": "山面包(东郊记忆店)"}, {"date": "2026-05-15", "type": "breakfast", "name": "山面包(东郊记忆店)"}]}, {"name_key": "观锦餐厅", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-05-11", "type": "lunch", "name": "观锦餐厅(天府新谷店)"}, {"date": "2026-05-12", "type": "lunch", "name": "观锦餐厅(天廊店)"}, {"date": "2026-05-13", "type": "lunch", "name": "观锦餐厅(天府新谷店)"}, {"date": "2026-05-14", "type": "lunch", "name": "观锦餐厅(天廊店)"}, {"date": "2026-05-15", "type": "lunch", "name": "观锦餐厅(天府新谷店)"}]}, {"name_key": "悦百味·品质川菜", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-05-11", "type": "dinner", "name": "悦百味·品质川菜(优品道店)"}, {"date": "2026-05-12", "type": "dinner", "name": "悦百味·品质川菜(优品道店)"}, {"date": "2026-05-13", "type": "dinner", "name": "悦百味·品质川菜(优品道店)"}, {"date": "2026-05-14", "type": "dinner", "name": "悦百味·品质川菜(优品道店)"}, {"date": "2026-05-15", "type": "dinner", "name": "悦百味·品质川菜(优品道店)"}]}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 4, "party_total": 2, "room_count": 1, "priced_nights": 5, "expected_min_total_hotels": 1500, "reported_total_hotels": 1200, "diff": -300, "covers_nights": false}}]`

### v3_hard_realbudget_eval_000005
- request: 广州 2026-07-06->2026-07-10 days=5 transport=公共交通 hotel=民宿 prefs=['摄影', '自然风光', '城市漫步', '本地菜']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "银灯食府", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-07-06", "type": "breakfast", "name": "银灯食府(文化公园店)"}, {"date": "2026-07-07", "type": "breakfast", "name": "银灯食府(文化公园店)"}, {"date": "2026-07-08", "type": "breakfast", "name": "银灯食府(文化公园店)"}, {"date": "2026-07-09", "type": "breakfast", "name": "银灯食府(文化公园店)"}, {"date": "2026-07-10", "type": "breakfast", "name": "银灯食府(文化公园店)"}]}, {"name_key": "民记煲仔饭", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-07-07", "type": "lunch", "name": "民记煲仔饭(北京路店)"}, {"date": "2026-07-08", "type": "lunch", "name": "民记煲仔饭(北京路店)"}, {"date": "2026-07-09", "type": "lunch", "name": "民记煲仔饭(北京路店)"}, {"date": "2026-07-10", "type": "lunch", "name": "民记煲仔饭(北京路店)"}]}, {"name_key": "丘大6仔记", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-07-07", "type": "dinner", "name": "丘大6仔记(滨江东路店)"}, {"date": "2026-07-08", "type": "dinner", "name": "丘大6仔记(滨江东路店)"}, {"date": "2026-07-09", "type": "dinner", "name": "丘大6仔记(滨江东路店)"}, {"date": "2026-07-10", "type": "dinner", "name": "丘大6仔记(滨江东路店)"}]}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 4, "party_total": 1, "room_count": 1, "priced_nights": 5, "expected_min_total_hotels": 1500, "reported_total_hotels": 1200, "diff": -300, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 675, "expected_total_attractions": 675, "reported_total_attractions": 1155, "meal_per_person_cost_sum": 1057, "expected_total_meals": 1057, "reported_total_meals": 1080, "reported_total_transportation": 200}}]`

### v3_hard_realbudget_eval_000003
- request: 西安 2025-05-07->2025-05-11 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "陕西历史博物馆", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2025-05-08", "day_index": 1, "name": "陕西历史博物馆"}, {"date": "2025-05-10", "day_index": 3, "name": "陕西历史博物馆"}]}, {"name_key": "陕西考古博物馆", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2025-05-09", "day_index": 2, "name": "陕西考古博物馆"}, {"date": "2025-05-10", "day_index": 3, "name": "陕西考古博物馆"}]}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "魏家凉皮", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2025-05-07", "type": "breakfast", "name": "魏家凉皮(西大街店)"}, {"date": "2025-05-08", "type": "breakfast", "name": "魏家凉皮(秦飞大厦店)"}, {"date": "2025-05-09", "type": "breakfast", "name": "魏家凉皮(秦飞大厦店)"}, {"date": "2025-05-10", "type": "breakfast", "name": "魏家凉皮(秦飞大厦店)"}, {"date": "2025-05-11", "type": "breakfast", "name": "魏家凉皮(秦飞大厦店)"}]}, {"name_key": "崔少野猫耳朵炒面", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2025-05-07", "type": "lunch", "name": "崔少野猫耳朵炒面(十里锦绣店)"}, {"date": "2025-05-08", "type": "lunch", "name": "崔少野猫耳朵炒面(十里锦绣店)"}, {"date": "2025-05-09", "type": "lunch", "name": "崔少野猫耳朵炒面(十里锦绣店)"}, {"date": "2025-05-10", "type": "lunch", "name": "崔少野猫耳朵炒面(十里锦绣店)"}, {"date": "2025-05-11", "type": "lunch", "name": "崔少野猫耳朵炒面(十里锦绣店)"}]}, {"name_key": "清真·汉城烧烤", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2025-05-07", "type": "dinner", "name": "清真·汉城烧烤(建章路店)"}, {"date": "2025-05-08", "type": "dinner", "name": "清真·汉城烧烤(建章路店)"}, {"date": "2025-05-09", "type": "dinner", "name": "清真·汉城烧烤(建章路店)"}, {"date": "2025-05-10", "type": "dinner", "name": "清真·汉城烧烤(建章路店)"}, {"date": "2025-05-11", "type": "dinner", "name": "清真·汉城烧烤(建章路店)"}]}]}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 4540, "total": 4440, "diff": 100, "requested_budget": {"available": true, "amount": 8400, "scope": "total", "party_size": 2, "total": 8400, "source": "budget_constraint", "budget_level": "standard", "strictness": "hard"}, "per_person_day": 444.0, "budget_level": "standard", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "standard", "strictness": "hard", "amount": 8400, "target_min_ratio": 0.6, "target_max_ratio": 1.0, "target_min_total": 5000, "target_max_total": 8400, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 4, "party_total": 2, "room_count": 1, "priced_nights": 5, "expected_min_total_hotels": 2250, "reported_total_hotels": 2250, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_hard_realbudget_eval_000010
- request: 西安 2026-08-05->2026-08-09 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-08-05", "lunch": "魏家凉皮(西大街店)", "dinner": "魏家凉皮(秦飞大厦店)"}, {"date": "2026-08-07", "lunch": "果渊斋老米家泡馍馆(回坊总店)", "dinner": "果渊斋老米家泡馍馆(回坊总店)"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "爱骅裤带面馆", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-08-05", "type": "breakfast", "name": "爱骅裤带面馆(钟楼店)"}, {"date": "2026-08-06", "type": "breakfast", "name": "爱骅裤带面馆(钟楼店)"}, {"date": "2026-08-07", "type": "breakfast", "name": "爱骅裤带面馆(钟楼店)"}, {"date": "2026-08-08", "type": "breakfast", "name": "爱骅裤带面馆(钟楼店)"}, {"date": "2026-08-09", "type": "breakfast", "name": "爱骅裤带面馆(钟楼店)"}]}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 4, "party_total": 5, "room_count": 3, "priced_nights": 5, "expected_min_total_hotels": 6750, "reported_total_hotels": 2250, "diff": -4500, "covers_nights": false}}]`

### v3_hard_realbudget_eval_000000
- request: 昆明 2026-04-07->2026-04-11 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "昆明老街", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-04-08", "day_index": 1, "name": "昆明老街"}, {"date": "2026-04-11", "day_index": 4, "name": "昆明老街"}]}, {"name_key": "昆明老街记忆", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-04-08", "day_index": 1, "name": "昆明老街记忆"}, {"date": "2026-04-11", "day_index": 4, "name": "昆明老街记忆"}]}]}, {"stage": "rule", "type": "meal_placeholder", "details": [{"date": "2026-04-07", "type": "breakfast", "name": "BA(翠湖公园店)"}]}, {"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-04-07", "type": "breakfast", "name": "BA(翠湖公园店)", "reason": "non_food_poi_name"}]}]`

### v3_hard_realbudget_eval_000011
- request: 福州 2026-06-21->2026-06-24 days=4 transport=打车 hotel=高端酒店 prefs=['高端酒店', '艺术', '特色餐厅', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "兴仙饭店·闽味海鲜", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-06-21", "type": "lunch", "name": "兴仙饭店·闽味海鲜(马尾总店)"}, {"date": "2026-06-22", "type": "lunch", "name": "兴仙饭店·闽味海鲜(烟台山店)"}, {"date": "2026-06-23", "type": "lunch", "name": "兴仙饭店·闽味海鲜(得贵路M17店)"}, {"date": "2026-06-24", "type": "lunch", "name": "兴仙饭店·闽味海鲜(得贵路M17店)"}]}]}, {"stage": "rule", "type": "budget_preference_mismatch", "details": {"part_sum": 5240, "total": 5240, "diff": 0, "requested_budget": {"available": true, "amount": 13500, "scope": "total", "party_size": 2, "total": 13500, "source": "budget_constraint", "budget_level": "premium", "strictness": "soft"}, "per_person_day": 655.0, "budget_level": "premium", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "premium", "strictness": "soft", "amount": 13500, "target_min_ratio": 0.75, "target_max_ratio": 1.12, "target_min_total": 10100, "target_max_total": 15100, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": true, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 2, "room_count": 1, "priced_nights": 4, "expected_min_total_hotels": 3000, "reported_total_hotels": 3000, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_hard_realbudget_eval_000009
- request: 苏州 2026-04-30->2026-05-03 days=4 transport=打车 hotel=亲子酒店 prefs=['亲子', '老人友好', '博物馆', '城市公园', '特色餐厅']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "老横泾面馆", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-04-30", "type": "lunch", "name": "老横泾面馆(吴中横泾总店)"}, {"date": "2026-05-01", "type": "breakfast", "name": "老横泾面馆(吴中横泾总店)"}, {"date": "2026-05-02", "type": "breakfast", "name": "老横泾面馆(吴中横泾总店)"}, {"date": "2026-05-03", "type": "breakfast", "name": "老横泾面馆(吴中横泾总店)"}]}, {"name_key": "浆小白豆浆夜市", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-04-30", "type": "dinner", "name": "浆小白豆浆夜市(阳光天地翡丽湾花园北区店)"}, {"date": "2026-05-01", "type": "dinner", "name": "浆小白豆浆夜市(阳光天地翡丽湾花园北区店)"}, {"date": "2026-05-02", "type": "dinner", "name": "浆小白豆浆夜市(阳光天地翡丽湾花园北区店)"}, {"date": "2026-05-03", "type": "dinner", "name": "浆小白豆浆夜市(阳光天地翡丽湾花园北区店)"}]}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 4, "room_count": 2, "priced_nights": 4, "expected_min_total_hotels": 10000, "reported_total_hotels": 5000, "diff": -5000, "covers_nights": false}}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 7250, "total": 7200, "diff": 50, "requested_budget": {"available": true, "amount": 16700, "scope": "total", "party_size": 4, "total": 16700, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "soft"}, "per_person_day": 450.0, "budget_level": "comfortable", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "soft", "amount": 16700, "target_min_ratio": 0.7, "target_max_ratio": 1.1, "target_min_total": 11700, "target_max_total": 18400, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 4, "room_count": 2, "priced_nights": 4, "expected_min_total_hotels": 10000, "reported_total_hotels": 5000, "diff": -5000, "covers_nights": false}, "hotel_budget_covers_nights": false}}]`

### v3_hard_realbudget_eval_000014
- request: 成都 2026-06-06->2026-06-08 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆']
- errors: `[{"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 135, "expected_total_attractions": 135, "reported_total_attractions": 275, "meal_per_person_cost_sum": 811, "expected_total_meals": 811, "reported_total_meals": 408, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 1, "hotel_room_count": 1, "attraction_ticket_sum": 135, "expected_total_attractions": 135, "reported_total_attractions": 275, "meal_per_person_cost_sum": 811, "expected_total_meals": 811, "reported_total_meals": 408, "reported_total_transportation": 200}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": false, "meal_cost_scale_ok": true, "budget_relationship_ok": false, "expected_total_hotels": 1350, "reported_total_hotels": 1350, "expected_total_attractions": 135, "reported_total_attractions": 275, "meal_scale_eval": {"ok": true, "party_total": 1, "budget_level": "comfortable", "per_person_lunch_dinner_floor": 50, "breakfast_policy": "excluded_from_meal_cost_scale", "meal_count": 9, "checked_count": 6, "failure_count": 0, "failures": []}}}]`

### v3_hard_realbudget_eval_000012
- request: 洛阳 2025-05-07->2025-05-10 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '夜市', '老字号', '城市漫步']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "方中山胡辣汤", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2025-05-07", "type": "breakfast", "name": "方中山胡辣汤(洛阳一店)"}, {"date": "2025-05-08", "type": "breakfast", "name": "方中山胡辣汤(洛阳二店)"}, {"date": "2025-05-09", "type": "breakfast", "name": "方中山胡辣汤(洛阳二店)"}, {"date": "2025-05-10", "type": "breakfast", "name": "方中山胡辣汤(洛阳二店)"}]}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 4, "room_count": 2, "priced_nights": 4, "expected_min_total_hotels": 2000, "reported_total_hotels": 1000, "diff": -1000, "covers_nights": false}}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 2190, "total": 2150, "diff": 40, "requested_budget": {"available": true, "amount": 5800, "scope": "total", "party_size": 4, "total": 5800, "source": "budget_constraint", "budget_level": "limited", "strictness": "hard"}, "per_person_day": 134.38, "budget_level": "limited", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "limited", "strictness": "hard", "amount": 5800, "target_min_ratio": 0.72, "target_max_ratio": 1.0, "target_min_total": 4200, "target_max_total": 5800, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 4, "room_count": 2, "priced_nights": 4, "expected_min_total_hotels": 2000, "reported_total_hotels": 1000, "diff": -1000, "covers_nights": false}, "hotel_budget_covers_nights": false}}]`

### v3_hard_realbudget_eval_000016
- request: 苏州 2026-06-06->2026-06-09 days=4 transport=自驾 hotel=亲子酒店 prefs=['亲子', '动物园', '海洋馆', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 3, "room_count": 2, "priced_nights": 4, "expected_min_total_hotels": 10000, "reported_total_hotels": 4800, "diff": -5200, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 149, "expected_total_attractions": 447, "reported_total_attractions": 1129, "meal_per_person_cost_sum": 755, "expected_total_meals": 2265, "reported_total_meals": 1200, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 149, "expected_total_attractions": 447, "reported_total_attractions": 1129, "meal_per_person_cost_sum": 755, "expected_total_meals": 2265, "reported_total_meals": 1200, "reported_total_transportation": 200}}]`

### v3_hard_realbudget_eval_000018
- request: 天津 2026-07-06->2026-07-08 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物']
- errors: `[{"stage": "rule", "type": "attraction_repeat_too_many", "details": [{"name_key": "天津之眼", "count": 2, "max_allowed": 1, "occurrences": [{"date": "2026-07-06", "day_index": 0, "name": "天津之眼"}, {"date": "2026-07-08", "day_index": 2, "name": "天津之眼"}]}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "魏家凉皮", "count": 3, "max_allowed": 2, "occurrences": [{"date": "2026-07-06", "type": "breakfast", "name": "魏家凉皮(体育中心店)"}, {"date": "2026-07-07", "type": "breakfast", "name": "魏家凉皮(体育中心店)"}, {"date": "2026-07-08", "type": "breakfast", "name": "魏家凉皮(体育中心店)"}]}, {"name_key": "南楼煎饼", "count": 3, "max_allowed": 2, "occurrences": [{"date": "2026-07-06", "type": "lunch", "name": "南楼煎饼(滨江道店)"}, {"date": "2026-07-07", "type": "lunch", "name": "南楼煎饼(南楼总店)"}, {"date": "2026-07-08", "type": "lunch", "name": "南楼煎饼(南楼总店)"}]}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 2, "party_total": 3, "room_count": 2, "priced_nights": 3, "expected_min_total_hotels": 4500, "reported_total_hotels": 2250, "diff": -2250, "covers_nights": false}}]`

### v3_hard_realbudget_eval_000019
- request: 丽江 2026-05-11->2026-05-14 days=4 transport=打车 hotel=亲子酒店 prefs=['亲子', '老人友好', '博物馆', '城市公园', '特色餐厅']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "party_total": 2, "room_count": 1, "priced_nights": 4, "expected_min_total_hotels": 2000, "reported_total_hotels": 1500, "diff": -500, "covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 400, "expected_total_attractions": 800, "reported_total_attractions": 240, "meal_per_person_cost_sum": 459, "expected_total_meals": 918, "reported_total_meals": 420, "reported_total_transportation": 200}}, {"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 400, "expected_total_attractions": 800, "reported_total_attractions": 240, "meal_per_person_cost_sum": 459, "expected_total_meals": 918, "reported_total_meals": 420, "reported_total_transportation": 200}}]`

### v3_hard_realbudget_eval_000013
- request: 武汉 2026-05-09->2026-05-13 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-05-11", "lunch": "刘聋子牛肉粉馆(汉阳玫瑰街店)", "dinner": "刘聋子牛肉粉馆(光谷新竹路店)"}, {"date": "2026-05-12", "lunch": "刘聋子牛肉粉馆(汉阳龙兴东街店)", "dinner": "刘聋子牛肉粉馆(光谷新竹路店)"}, {"date": "2026-05-13", "lunch": "刘聋子牛肉粉馆(汉阳龙兴东街店)", "dinner": "刘聋子牛肉粉馆(光谷新竹路店)"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "矮子馅饼", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-05-09", "type": "breakfast", "name": "矮子馅饼(三弓路店)"}, {"date": "2026-05-10", "type": "breakfast", "name": "矮子馅饼(武汉总店)"}, {"date": "2026-05-12", "type": "breakfast", "name": "矮子馅饼(大成路店)"}, {"date": "2026-05-13", "type": "breakfast", "name": "矮子馅饼(三弓路店)"}]}, {"name_key": "刘聋子牛肉粉馆", "count": 7, "max_allowed": 3, "occurrences": [{"date": "2026-05-10", "type": "dinner", "name": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}, {"date": "2026-05-11", "type": "lunch", "name": "刘聋子牛肉粉馆(汉阳玫瑰街店)"}, {"date": "2026-05-11", "type": "dinner", "name": "刘聋子牛肉粉馆(光谷新竹路店)"}, {"date": "2026-05-12", "type": "lunch", "name": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}, {"date": "2026-05-12", "type": "dinner", "name": "刘聋子牛肉粉馆(光谷新竹路店)"}, {"date": "2026-05-13", "type": "lunch", "name": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}, {"date": "2026-05-13", "type": "dinner", "name": "刘聋子牛肉粉馆(光谷新竹路店)"}]}]}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 2850, "total": 3040, "diff": -190, "requested_budget": {"available": true, "amount": 6800, "scope": "total", "party_size": 2, "total": 6800, "source": "budget_constraint", "budget_level": "standard", "strictness": "hard"}, "per_person_day": 304.0, "budget_level": "standard", "strictness": "hard", "budget_fit_policy": {"enabled": true, "budget_level": "standard", "strictness": "hard", "amount": 6800, "target_min_ratio": 0.6, "target_max_ratio": 1.0, "target_min_total": 4100, "target_max_total": 6800, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 4, "party_total": 2, "room_count": 1, "priced_nights": 5, "expected_min_total_hotels": 2000, "reported_total_hotels": 2000, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_hard_realbudget_eval_000017
- request: 苏州 2026-05-09->2026-05-13 days=5 transport=公共交通 hotel=民宿 prefs=['小众展馆', '咖啡', '艺术', '城市漫步', '特色餐厅']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 4, "party_total": 2, "room_count": 1, "priced_nights": 5, "expected_min_total_hotels": 1500, "reported_total_hotels": 1200, "diff": -300, "covers_nights": false}}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 2055, "total": 1955, "diff": 100, "requested_budget": {"available": true, "amount": 10100, "scope": "total", "party_size": 2, "total": 10100, "source": "budget_constraint", "budget_level": "comfortable", "strictness": "soft"}, "per_person_day": 195.5, "budget_level": "comfortable", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "comfortable", "strictness": "soft", "amount": 10100, "target_min_ratio": 0.7, "target_max_ratio": 1.1, "target_min_total": 7100, "target_max_total": 11100, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 4, "party_total": 2, "room_count": 1, "priced_nights": 5, "expected_min_total_hotels": 1500, "reported_total_hotels": 1200, "diff": -300, "covers_nights": false}, "hotel_budget_covers_nights": false}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 135, "expected_total_attractions": 270, "reported_total_attractions": 295, "meal_per_person_cost_sum": 626, "expected_total_meals": 1252, "reported_total_meals": 360, "reported_total_transportation": 200}}]`

### v3_hard_realbudget_eval_000021
- request: 上海 2026-06-21->2026-06-24 days=4 transport=打车 hotel=高端酒店 prefs=['高端酒店', '艺术', '特色餐厅', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "沪西老弄堂面馆", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-06-21", "type": "breakfast", "name": "沪西老弄堂面馆"}, {"date": "2026-06-22", "type": "breakfast", "name": "沪西老弄堂面馆"}, {"date": "2026-06-23", "type": "breakfast", "name": "沪西老弄堂面馆"}, {"date": "2026-06-24", "type": "breakfast", "name": "沪西老弄堂面馆"}]}, {"name_key": "沈大成", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-06-21", "type": "lunch", "name": "沈大成(南京东路店)"}, {"date": "2026-06-22", "type": "lunch", "name": "沈大成(南京东路店)"}, {"date": "2026-06-23", "type": "lunch", "name": "沈大成(南京东路店)"}, {"date": "2026-06-24", "type": "lunch", "name": "沈大成(南京东路店)"}]}, {"name_key": "紫阳村地道家常菜", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-06-21", "type": "dinner", "name": "紫阳村地道家常菜(川沙店)"}, {"date": "2026-06-22", "type": "dinner", "name": "紫阳村地道家常菜(川沙店)"}, {"date": "2026-06-23", "type": "dinner", "name": "紫阳村地道家常菜(川沙店)"}, {"date": "2026-06-24", "type": "dinner", "name": "紫阳村地道家常菜(川沙店)"}]}]}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 5670, "total": 6020, "diff": -350, "requested_budget": {"available": true, "amount": 14300, "scope": "total", "party_size": 2, "total": 14300, "source": "budget_constraint", "budget_level": "premium", "strictness": "soft"}, "per_person_day": 752.5, "budget_level": "premium", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "premium", "strictness": "soft", "amount": 14300, "target_min_ratio": 0.75, "target_max_ratio": 1.12, "target_min_total": 10700, "target_max_total": 16000, "instruction": "budget.total应尽量落在target_min_total和target_max_total之间；不要为了省钱显著低于预算档位。"}, "arithmetic_consistent": false, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 3, "party_total": 2, "room_count": 1, "priced_nights": 4, "expected_min_total_hotels": 3400, "reported_total_hotels": 3400, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}, {"stage": "rule", "type": "attraction_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 545, "expected_total_attractions": 1090, "reported_total_attractions": 150, "meal_per_person_cost_sum": 740, "expected_total_meals": 1480, "reported_total_meals": 1320, "reported_total_transportation": 800}}]`
