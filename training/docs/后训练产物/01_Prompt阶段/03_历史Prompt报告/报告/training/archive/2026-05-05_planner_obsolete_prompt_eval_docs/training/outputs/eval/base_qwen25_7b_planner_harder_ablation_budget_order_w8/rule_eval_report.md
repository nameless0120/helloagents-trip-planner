# Rule Eval Report: base_qwen25_7b_v3_harder_ablation_budget_order_w8

- records: 300
- generations: `training/outputs/eval/base_qwen25_7b_v3_harder_ablation_budget_order_w8/generations.jsonl`
- records_path: `training/data/v3/eval_harder_food_bucket_meal_ablation_budget_order_no_route/records.jsonl`

## Boolean Metrics

| Metric | Pass | Total | Rate |
| --- | ---: | ---: | ---: |
| attraction_count_ok | 292 | 293 | 99.66% |
| attraction_grounding_ok | 288 | 293 | 98.29% |
| budget_arithmetic_consistent | 269 | 293 | 91.81% |
| budget_consistent | 269 | 293 | 91.81% |
| budget_level_aligned | 286 | 293 | 97.61% |
| budget_preference_aligned | 286 | 293 | 97.61% |
| budget_within_user_budget | 293 | 293 | 100.00% |
| city_ok | 293 | 293 | 100.00% |
| date_range_ok | 293 | 293 | 100.00% |
| day_dates_ok | 293 | 293 | 100.00% |
| day_index_ok | 293 | 293 | 100.00% |
| days_len_ok | 293 | 293 | 100.00% |
| dpo_soft_pass | 16 | 293 | 5.46% |
| hard_pass | 244 | 293 | 83.28% |
| hotel_budget_covers_nights | 293 | 293 | 100.00% |
| hotel_distance_placeholder_ok | 293 | 293 | 100.00% |
| hotel_grounding_ok | 292 | 293 | 99.66% |
| invalid_hotel_name_ok | 293 | 293 | 100.00% |
| json_extract_ok | 300 | 300 | 100.00% |
| legacy_hard_pass | 17 | 293 | 5.80% |
| location_object_ok | 293 | 293 | 100.00% |
| meal_complete | 285 | 293 | 97.27% |
| meal_diversity_ok | 30 | 293 | 10.24% |
| meal_grounding_ok | 278 | 293 | 94.88% |
| meal_lunch_dinner_same_day_ok | 146 | 293 | 49.83% |
| meal_repeat_limit_ok | 58 | 293 | 19.80% |
| meal_specific_ok | 293 | 293 | 100.00% |
| meal_valid_semantics_ok | 279 | 293 | 95.22% |
| middle_hotel_ok | 291 | 293 | 99.32% |
| schema_ok | 293 | 300 | 97.67% |
| sft_hard_pass | 244 | 293 | 83.28% |
| weather_dates_ok | 293 | 293 | 100.00% |
| weather_match | 292 | 293 | 99.66% |

## Numeric Metrics

```json
{
  "attraction_grounding_rate": {
    "avg": 0.9975,
    "p50": 1.0,
    "p90": 1.0
  },
  "hotel_grounding_rate": {
    "avg": 0.9966,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_diversity_unique_rate": {
    "avg": 0.3703,
    "p50": 0.2667,
    "p90": 0.75
  },
  "meal_food_pois_grounding_rate": {
    "avg": 0.9935,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_grounding_rate": {
    "avg": 0.9935,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_semantic_valid_rate": {
    "avg": 0.9938,
    "p50": 1.0,
    "p90": 1.0
  }
}
```

## Failure Types

```json
{
  "meal_repeat_too_many": 235,
  "meal_same_day_lunch_dinner_repeat": 147,
  "budget_arithmetic_inconsistent": 24,
  "meal_invalid_name": 14,
  "schema": 7,
  "budget_preference_mismatch": 7,
  "middle_hotel_null": 2,
  "weather_mismatch": 1,
  "meal_grounding_miss": 1
}
```

## Failure Examples

### v3_harder_eval_000004
- request: 张家界 2026-05-08->2026-05-10 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-05-08", "lunch": "索溪山寨·湘西民间土菜(标志门店)", "dinner": "索溪山寨·湘西民间土菜(标志门店)"}, {"date": "2026-05-09", "lunch": "索溪山寨·湘西民间土菜(标志门店)", "dinner": "索溪山寨·湘西民间土菜(标志门店)"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "索溪山寨·湘西民间土菜", "count": 4, "max_allowed": 2, "occurrences": [{"date": "2026-05-08", "type": "lunch", "name": "索溪山寨·湘西民间土菜(标志门店)"}, {"date": "2026-05-08", "type": "dinner", "name": "索溪山寨·湘西民间土菜(标志门店)"}, {"date": "2026-05-09", "type": "lunch", "name": "索溪山寨·湘西民间土菜(标志门店)"}, {"date": "2026-05-09", "type": "dinner", "name": "索溪山寨·湘西民间土菜(标志门店)"}]}]}]`

### v3_harder_eval_000008
- request: 大理 2026-05-08->2026-05-10 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "老爷爷的手工鲜花饼", "count": 3, "max_allowed": 2, "occurrences": [{"date": "2026-05-08", "type": "breakfast", "name": "老爷爷的手工鲜花饼(总店)"}, {"date": "2026-05-09", "type": "breakfast", "name": "老爷爷的手工鲜花饼(总店)"}, {"date": "2026-05-10", "type": "breakfast", "name": "老爷爷的手工鲜花饼(总店)"}]}, {"name_key": "南诏村·现炒云南菜", "count": 3, "max_allowed": 2, "occurrences": [{"date": "2026-05-08", "type": "lunch", "name": "南诏村·现炒云南菜"}, {"date": "2026-05-09", "type": "lunch", "name": "南诏村·现炒云南菜"}, {"date": "2026-05-10", "type": "lunch", "name": "南诏村·现炒云南菜"}]}, {"name_key": "桃红小馆·特色云南菜·庭院花园餐厅", "count": 3, "max_allowed": 2, "occurrences": [{"date": "2026-05-08", "type": "dinner", "name": "桃红小馆·特色云南菜·庭院花园餐厅"}, {"date": "2026-05-09", "type": "dinner", "name": "桃红小馆·特色云南菜·庭院花园餐厅"}, {"date": "2026-05-10", "type": "dinner", "name": "桃红小馆·特色云南菜·庭院花园餐厅"}]}]}]`

### v3_harder_eval_000006
- request: 南京 2026-07-03->2026-07-06 days=4 transport=自驾 hotel=亲子酒店 prefs=['亲子', '动物园', '海洋馆', '城市公园', '本地美食']
- errors: `[{"stage": "schema", "message": "1 validation error for TripPlan\ndays.3.accommodation\n  Input should be a valid string [type=string_type, input_value=None, input_type=NoneType]\n    For further information visit https://errors.pydantic.dev/2.12/v/string_type"}]`

### v3_harder_eval_000001
- request: 桂林 2026-09-01->2026-09-04 days=4 transport=打车 hotel=高端酒店 prefs=['高端酒店', '艺术', '特色餐厅', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-09-01", "lunch": "椿记烧鹅(中山店)", "dinner": "椿记烧鹅(中山店)"}, {"date": "2026-09-02", "lunch": "椿记烧鹅(中山店)", "dinner": "椿记烧鹅(中山店)"}, {"date": "2026-09-03", "lunch": "椿记烧鹅(中山店)", "dinner": "椿记烧鹅(中山店)"}, {"date": "2026-09-04", "lunch": "椿记烧鹅(中山店)", "dinner": "椿记烧鹅(中山店)"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "椿记烧鹅", "count": 11, "max_allowed": 3, "occurrences": [{"date": "2026-09-01", "type": "lunch", "name": "椿记烧鹅(中山店)"}, {"date": "2026-09-01", "type": "dinner", "name": "椿记烧鹅(中山店)"}, {"date": "2026-09-02", "type": "breakfast", "name": "椿记烧鹅(中山店)"}, {"date": "2026-09-02", "type": "lunch", "name": "椿记烧鹅(中山店)"}, {"date": "2026-09-02", "type": "dinner", "name": "椿记烧鹅(中山店)"}, {"date": "2026-09-03", "type": "breakfast", "name": "椿记烧鹅(中山店)"}, {"date": "2026-09-03", "type": "lunch", "name": "椿记烧鹅(中山店)"}, {"date": "2026-09-03", "type": "dinner", "name": "椿记烧鹅(中山店)"}, {"date": "2026-09-04", "type": "breakfast", "name": "椿记烧鹅(中山店)"}, {"date": "2026-09-04", "type": "lunch", "name": "椿记烧鹅(中山店)"}]}]}]`

### v3_harder_eval_000000
- request: 昆明 2026-04-04->2026-04-08 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-04-04", "lunch": "四方小炒·云南菜小当家(联盟店)", "dinner": "四方小炒·云南菜小当家(联盟店)"}, {"date": "2026-04-05", "lunch": "四方小炒·云南菜小当家(联盟店)", "dinner": "四方小炒·云南菜小当家(联盟店)"}, {"date": "2026-04-06", "lunch": "四方小炒·云南菜小当家(联盟店)", "dinner": "四方小炒·云南菜小当家(联盟店)"}, {"date": "2026-04-07", "lunch": "四方小炒·云南菜小当家(联盟店)", "dinner": "四方小炒·云南菜小当家(联盟店)"}, {"date": "2026-04-08", "lunch": "四方小炒·云南菜小当家(联盟店)", "dinner": "四方小炒·云南菜小当家(联盟店)"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "晨曦豆花米线", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-04-04", "type": "breakfast", "name": "晨曦豆花米线"}, {"date": "2026-04-05", "type": "breakfast", "name": "晨曦豆花米线"}, {"date": "2026-04-06", "type": "breakfast", "name": "晨曦豆花米线"}, {"date": "2026-04-07", "type": "breakfast", "name": "晨曦豆花米线"}, {"date": "2026-04-08", "type": "breakfast", "name": "晨曦豆花米线"}]}, {"name_key": "四方小炒·云南菜小当家", "count": 10, "max_allowed": 3, "occurrences": [{"date": "2026-04-04", "type": "lunch", "name": "四方小炒·云南菜小当家(联盟店)"}, {"date": "2026-04-04", "type": "dinner", "name": "四方小炒·云南菜小当家(联盟店)"}, {"date": "2026-04-05", "type": "lunch", "name": "四方小炒·云南菜小当家(联盟店)"}, {"date": "2026-04-05", "type": "dinner", "name": "四方小炒·云南菜小当家(联盟店)"}, {"date": "2026-04-06", "type": "lunch", "name": "四方小炒·云南菜小当家(联盟店)"}, {"date": "2026-04-06", "type": "dinner", "name": "四方小炒·云南菜小当家(联盟店)"}, {"date": "2026-04-07", "type": "lunch", "name": "四方小炒·云南菜小当家(联盟店)"}, {"date": "2026-04-07", "type": "dinner", "name": "四方小炒·云南菜小当家(联盟店)"}, {"date": "2026-04-08", "type": "lunch", "name": "四方小炒·云南菜小当家(联盟店)"}, {"date": "2026-04-08", "type": "dinner", "name": "四方小炒·云南菜小当家(联盟店)"}]}]}]`

### v3_harder_eval_000005
- request: 广州 2026-07-03->2026-07-07 days=5 transport=公共交通 hotel=民宿 prefs=['摄影', '自然风光', '城市漫步', '本地菜']
- errors: `[{"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-07-07", "type": "dinner", "name": "广州塔-空中漫步", "reason": "unknown_food_semantics"}]}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 2980, "total": 2080, "diff": 900, "requested_budget": {"available": false, "amount": 0, "scope": "unknown", "party_size": 1, "total": 0}, "per_person_day": 416.0, "budget_level": "standard", "arithmetic_consistent": false, "within_user_budget": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 4, "priced_nights": 4, "expected_min_total_hotels": 1200, "reported_total_hotels": 1200, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_harder_eval_000003
- request: 西安 2025-05-04->2025-05-08 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "魏家凉皮", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2025-05-04", "type": "breakfast", "name": "魏家凉皮(西大街店)"}, {"date": "2025-05-05", "type": "breakfast", "name": "魏家凉皮(西大街店)"}, {"date": "2025-05-06", "type": "breakfast", "name": "魏家凉皮(西大街店)"}, {"date": "2025-05-07", "type": "breakfast", "name": "魏家凉皮(西大街店)"}, {"date": "2025-05-08", "type": "breakfast", "name": "魏家凉皮(西大街店)"}]}, {"name_key": "崔少野猫耳朵炒面", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2025-05-04", "type": "lunch", "name": "崔少野猫耳朵炒面(十里锦绣店)"}, {"date": "2025-05-05", "type": "lunch", "name": "崔少野猫耳朵炒面(十里锦绣店)"}, {"date": "2025-05-06", "type": "lunch", "name": "崔少野猫耳朵炒面(十里锦绣店)"}, {"date": "2025-05-07", "type": "lunch", "name": "崔少野猫耳朵炒面(十里锦绣店)"}, {"date": "2025-05-08", "type": "lunch", "name": "崔少野猫耳朵炒面(十里锦绣店)"}]}, {"name_key": "李志贤灌汤包子", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2025-05-04", "type": "dinner", "name": "李志贤灌汤包子"}, {"date": "2025-05-05", "type": "dinner", "name": "李志贤灌汤包子"}, {"date": "2025-05-06", "type": "dinner", "name": "李志贤灌汤包子"}, {"date": "2025-05-07", "type": "dinner", "name": "李志贤灌汤包子"}, {"date": "2025-05-08", "type": "dinner", "name": "李志贤灌汤包子"}]}]}]`

### v3_harder_eval_000014
- request: 成都 2026-06-03->2026-06-05 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "四妹钵钵鸡", "count": 3, "max_allowed": 2, "occurrences": [{"date": "2026-06-03", "type": "breakfast", "name": "四妹钵钵鸡(望平街店)"}, {"date": "2026-06-04", "type": "breakfast", "name": "四妹钵钵鸡(望平街店)"}, {"date": "2026-06-05", "type": "breakfast", "name": "四妹钵钵鸡(望平街店)"}]}, {"name_key": "观锦餐厅", "count": 3, "max_allowed": 2, "occurrences": [{"date": "2026-06-03", "type": "lunch", "name": "观锦餐厅(天廊店)"}, {"date": "2026-06-04", "type": "lunch", "name": "观锦餐厅(天府新谷店)"}, {"date": "2026-06-05", "type": "lunch", "name": "观锦餐厅(天府新谷店)"}]}, {"name_key": "悦百味·品质川菜", "count": 3, "max_allowed": 2, "occurrences": [{"date": "2026-06-03", "type": "dinner", "name": "悦百味·品质川菜(悠方店)"}, {"date": "2026-06-04", "type": "dinner", "name": "悦百味·品质川菜(悠方店)"}, {"date": "2026-06-05", "type": "dinner", "name": "悦百味·品质川菜(悠方店)"}]}]}]`

### v3_harder_eval_000009
- request: 苏州 2026-04-27->2026-04-30 days=4 transport=打车 hotel=亲子酒店 prefs=['亲子', '老人友好', '博物馆', '城市公园', '特色餐厅']
- errors: `[{"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-04-28", "type": "dinner", "name": "苏州乐园森林世界", "reason": "unknown_food_semantics"}, {"date": "2026-04-30", "type": "dinner", "name": "苏州太仓华发铂尔曼酒店", "reason": "hotel_or_lodging_name"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "魏家凉皮", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-04-27", "type": "breakfast", "name": "魏家凉皮"}, {"date": "2026-04-28", "type": "breakfast", "name": "魏家凉皮"}, {"date": "2026-04-29", "type": "breakfast", "name": "魏家凉皮"}, {"date": "2026-04-30", "type": "breakfast", "name": "魏家凉皮"}]}, {"name_key": "老横泾面馆", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-04-27", "type": "lunch", "name": "老横泾面馆"}, {"date": "2026-04-28", "type": "lunch", "name": "老横泾面馆"}, {"date": "2026-04-29", "type": "lunch", "name": "老横泾面馆"}, {"date": "2026-04-30", "type": "lunch", "name": "老横泾面馆"}]}]}]`

### v3_harder_eval_000011
- request: 福州 2026-06-18->2026-06-21 days=4 transport=打车 hotel=高端酒店 prefs=['高端酒店', '艺术', '特色餐厅', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "紫阳海鲜楼·传承闽味", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-06-18", "type": "dinner", "name": "紫阳海鲜楼·传承闽味(长乐路总店)"}, {"date": "2026-06-19", "type": "dinner", "name": "紫阳海鲜楼·传承闽味(华林路店)"}, {"date": "2026-06-20", "type": "lunch", "name": "紫阳海鲜楼·传承闽味(华林路店)"}, {"date": "2026-06-21", "type": "lunch", "name": "紫阳海鲜楼·传承闽味(华林路店)"}]}]}]`

### v3_harder_eval_000010
- request: 西安 2026-04-20->2026-04-24 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-04-20", "lunch": "国人川菜(李家村店)", "dinner": "国人川菜(李家村店)"}, {"date": "2026-04-21", "lunch": "国人川菜(李家村店)", "dinner": "国人川菜(李家村店)"}, {"date": "2026-04-22", "lunch": "国人川菜(李家村店)", "dinner": "国人川菜(李家村店)"}, {"date": "2026-04-23", "lunch": "国人川菜(李家村店)", "dinner": "国人川菜(李家村店)"}, {"date": "2026-04-24", "lunch": "国人川菜(李家村店)", "dinner": "国人川菜(李家村店)"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "魏家凉皮", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-04-20", "type": "breakfast", "name": "魏家凉皮(西大街店)"}, {"date": "2026-04-21", "type": "breakfast", "name": "魏家凉皮(西大街店)"}, {"date": "2026-04-22", "type": "breakfast", "name": "魏家凉皮(西大街店)"}, {"date": "2026-04-23", "type": "breakfast", "name": "魏家凉皮(西大街店)"}, {"date": "2026-04-24", "type": "breakfast", "name": "魏家凉皮(西大街店)"}]}, {"name_key": "国人川菜", "count": 10, "max_allowed": 3, "occurrences": [{"date": "2026-04-20", "type": "lunch", "name": "国人川菜(李家村店)"}, {"date": "2026-04-20", "type": "dinner", "name": "国人川菜(李家村店)"}, {"date": "2026-04-21", "type": "lunch", "name": "国人川菜(李家村店)"}, {"date": "2026-04-21", "type": "dinner", "name": "国人川菜(李家村店)"}, {"date": "2026-04-22", "type": "lunch", "name": "国人川菜(李家村店)"}, {"date": "2026-04-22", "type": "dinner", "name": "国人川菜(李家村店)"}, {"date": "2026-04-23", "type": "lunch", "name": "国人川菜(李家村店)"}, {"date": "2026-04-23", "type": "dinner", "name": "国人川菜(李家村店)"}, {"date": "2026-04-24", "type": "lunch", "name": "国人川菜(李家村店)"}, {"date": "2026-04-24", "type": "dinner", "name": "国人川菜(李家村店)"}]}]}]`

### v3_harder_eval_000012
- request: 洛阳 2025-05-04->2025-05-07 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '夜市', '老字号', '城市漫步']
- errors: `[{"stage": "rule", "type": "budget_preference_mismatch", "details": {"part_sum": 3560, "total": 3560, "diff": 0, "requested_budget": {"available": false, "amount": 0, "scope": "unknown", "party_size": 2, "total": 0}, "per_person_day": 445.0, "budget_level": "limited", "arithmetic_consistent": true, "within_user_budget": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 3, "priced_nights": 3, "expected_min_total_hotels": 700, "reported_total_hotels": 1200, "diff": 500, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_harder_eval_000016
- request: 苏州 2026-06-03->2026-06-06 days=4 transport=自驾 hotel=亲子酒店 prefs=['亲子', '动物园', '海洋馆', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-06-03", "lunch": "稻山村·苏州菜(石路店)", "dinner": "稻山村·苏州菜(石路店)"}, {"date": "2026-06-04", "lunch": "稻山村·苏州菜(石路店)", "dinner": "稻山村·苏州菜(石路店)"}, {"date": "2026-06-05", "lunch": "稻山村·苏州菜(石路店)", "dinner": "稻山村·苏州菜(石路店)"}, {"date": "2026-06-06", "lunch": "稻山村·苏州菜(石路店)", "dinner": "稻山村·苏州菜(石路店)"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "魏家凉皮", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-06-03", "type": "breakfast", "name": "魏家凉皮(邵磨针巷店)"}, {"date": "2026-06-04", "type": "breakfast", "name": "魏家凉皮(邵磨针巷店)"}, {"date": "2026-06-05", "type": "breakfast", "name": "魏家凉皮(邵磨针巷店)"}, {"date": "2026-06-06", "type": "breakfast", "name": "魏家凉皮(邵磨针巷店)"}]}, {"name_key": "稻山村·苏州菜", "count": 8, "max_allowed": 3, "occurrences": [{"date": "2026-06-03", "type": "lunch", "name": "稻山村·苏州菜(石路店)"}, {"date": "2026-06-03", "type": "dinner", "name": "稻山村·苏州菜(石路店)"}, {"date": "2026-06-04", "type": "lunch", "name": "稻山村·苏州菜(石路店)"}, {"date": "2026-06-04", "type": "dinner", "name": "稻山村·苏州菜(石路店)"}, {"date": "2026-06-05", "type": "lunch", "name": "稻山村·苏州菜(石路店)"}, {"date": "2026-06-05", "type": "dinner", "name": "稻山村·苏州菜(石路店)"}, {"date": "2026-06-06", "type": "lunch", "name": "稻山村·苏州菜(石路店)"}, {"date": "2026-06-06", "type": "dinner", "name": "稻山村·苏州菜(石路店)"}]}]}]`

### v3_harder_eval_000013
- request: 武汉 2026-05-06->2026-05-10 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-05-06", "lunch": "刘聋子牛肉粉馆(汉阳龙兴东街店)", "dinner": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}, {"date": "2026-05-07", "lunch": "刘聋子牛肉粉馆(汉阳龙兴东街店)", "dinner": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}, {"date": "2026-05-08", "lunch": "刘聋子牛肉粉馆(汉阳龙兴东街店)", "dinner": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}, {"date": "2026-05-09", "lunch": "刘聋子牛肉粉馆(汉阳龙兴东街店)", "dinner": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}, {"date": "2026-05-10", "lunch": "刘聋子牛肉粉馆(汉阳龙兴东街店)", "dinner": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "方记老上海馄饨铺", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-05-06", "type": "breakfast", "name": "方记老上海馄饨铺(中南店)"}, {"date": "2026-05-07", "type": "breakfast", "name": "方记老上海馄饨铺(中南店)"}, {"date": "2026-05-08", "type": "breakfast", "name": "方记老上海馄饨铺(中南店)"}, {"date": "2026-05-09", "type": "breakfast", "name": "方记老上海馄饨铺(中南店)"}, {"date": "2026-05-10", "type": "breakfast", "name": "方记老上海馄饨铺(中南店)"}]}, {"name_key": "刘聋子牛肉粉馆", "count": 10, "max_allowed": 3, "occurrences": [{"date": "2026-05-06", "type": "lunch", "name": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}, {"date": "2026-05-06", "type": "dinner", "name": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}, {"date": "2026-05-07", "type": "lunch", "name": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}, {"date": "2026-05-07", "type": "dinner", "name": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}, {"date": "2026-05-08", "type": "lunch", "name": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}, {"date": "2026-05-08", "type": "dinner", "name": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}, {"date": "2026-05-09", "type": "lunch", "name": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}, {"date": "2026-05-09", "type": "dinner", "name": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}, {"date": "2026-05-10", "type": "lunch", "name": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}, {"date": "2026-05-10", "type": "dinner", "name": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}]}]}]`

### v3_harder_eval_000018
- request: 天津 2026-07-03->2026-07-05 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-07-04", "lunch": "天津卫码头(水上公园店)", "dinner": "天津卫码头(水上公园店)"}, {"date": "2026-07-05", "lunch": "魏斯理汉堡(天津乐宾百货店)", "dinner": "魏斯理汉堡(天津乐宾百货店)"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "南楼煎饼", "count": 4, "max_allowed": 2, "occurrences": [{"date": "2026-07-03", "type": "breakfast", "name": "南楼煎饼"}, {"date": "2026-07-03", "type": "dinner", "name": "南楼煎饼"}, {"date": "2026-07-04", "type": "breakfast", "name": "南楼煎饼"}, {"date": "2026-07-05", "type": "breakfast", "name": "南楼煎饼"}]}]}]`

### v3_harder_eval_000019
- request: 丽江 2026-05-08->2026-05-11 days=4 transport=打车 hotel=亲子酒店 prefs=['亲子', '老人友好', '博物馆', '城市公园', '特色餐厅']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-05-08", "lunch": "则瓦米线·云南小吃集合(花巷店)", "dinner": "则瓦米线·云南小吃集合(花巷店)"}, {"date": "2026-05-09", "lunch": "则瓦米线·云南小吃集合(花巷店)", "dinner": "则瓦米线·云南小吃集合(花巷店)"}, {"date": "2026-05-10", "lunch": "则瓦米线·云南小吃集合(花巷店)", "dinner": "则瓦米线·云南小吃集合(花巷店)"}, {"date": "2026-05-11", "lunch": "则瓦米线·云南小吃集合(花巷店)", "dinner": "则瓦米线·云南小吃集合(花巷店)"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "隔壁老王·家常云南菜", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-05-08", "type": "breakfast", "name": "隔壁老王·家常云南菜(丽江旗舰店)"}, {"date": "2026-05-09", "type": "breakfast", "name": "隔壁老王·家常云南菜(丽江旗舰店)"}, {"date": "2026-05-10", "type": "breakfast", "name": "隔壁老王·家常云南菜(丽江旗舰店)"}, {"date": "2026-05-11", "type": "breakfast", "name": "隔壁老王·家常云南菜(丽江旗舰店)"}]}, {"name_key": "则瓦米线·云南小吃集合", "count": 8, "max_allowed": 3, "occurrences": [{"date": "2026-05-08", "type": "lunch", "name": "则瓦米线·云南小吃集合(花巷店)"}, {"date": "2026-05-08", "type": "dinner", "name": "则瓦米线·云南小吃集合(花巷店)"}, {"date": "2026-05-09", "type": "lunch", "name": "则瓦米线·云南小吃集合(花巷店)"}, {"date": "2026-05-09", "type": "dinner", "name": "则瓦米线·云南小吃集合(花巷店)"}, {"date": "2026-05-10", "type": "lunch", "name": "则瓦米线·云南小吃集合(花巷店)"}, {"date": "2026-05-10", "type": "dinner", "name": "则瓦米线·云南小吃集合(花巷店)"}, {"date": "2026-05-11", "type": "lunch", "name": "则瓦米线·云南小吃集合(花巷店)"}, {"date": "2026-05-11", "type": "dinner", "name": "则瓦米线·云南小吃集合(花巷店)"}]}]}]`

### v3_harder_eval_000024
- request: 济南 2026-05-07->2026-05-09 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "穆得老周家牛肉烧饼", "count": 3, "max_allowed": 2, "occurrences": [{"date": "2026-05-07", "type": "breakfast", "name": "穆得老周家牛肉烧饼"}, {"date": "2026-05-08", "type": "breakfast", "name": "穆得老周家牛肉烧饼"}, {"date": "2026-05-09", "type": "breakfast", "name": "穆得老周家牛肉烧饼"}]}, {"name_key": "老济南济南菜", "count": 3, "max_allowed": 2, "occurrences": [{"date": "2026-05-07", "type": "lunch", "name": "老济南济南菜(大明湖店)"}, {"date": "2026-05-08", "type": "lunch", "name": "老济南济南菜(大明湖店)"}, {"date": "2026-05-09", "type": "lunch", "name": "老济南济南菜(大明湖店)"}]}, {"name_key": "鑫龙火锅城", "count": 3, "max_allowed": 2, "occurrences": [{"date": "2026-05-07", "type": "dinner", "name": "鑫龙火锅城(环山路店)"}, {"date": "2026-05-08", "type": "dinner", "name": "鑫龙火锅城(环山路店)"}, {"date": "2026-05-09", "type": "dinner", "name": "鑫龙火锅城(环山路店)"}]}]}]`

### v3_harder_eval_000021
- request: 上海 2026-06-18->2026-06-21 days=4 transport=打车 hotel=高端酒店 prefs=['高端酒店', '艺术', '特色餐厅', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "莱莱小笼", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-06-18", "type": "breakfast", "name": "莱莱小笼"}, {"date": "2026-06-19", "type": "breakfast", "name": "莱莱小笼"}, {"date": "2026-06-20", "type": "breakfast", "name": "莱莱小笼"}, {"date": "2026-06-21", "type": "breakfast", "name": "莱莱小笼"}]}, {"name_key": "紫阳村地道家常菜", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-06-18", "type": "lunch", "name": "紫阳村地道家常菜(川沙店)"}, {"date": "2026-06-19", "type": "lunch", "name": "紫阳村地道家常菜(川沙店)"}, {"date": "2026-06-20", "type": "lunch", "name": "紫阳村地道家常菜(川沙店)"}, {"date": "2026-06-21", "type": "lunch", "name": "紫阳村地道家常菜(川沙店)"}]}, {"name_key": "南门涮肉", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-06-18", "type": "dinner", "name": "南门涮肉(上海一店)"}, {"date": "2026-06-19", "type": "dinner", "name": "南门涮肉(上海一店)"}, {"date": "2026-06-20", "type": "dinner", "name": "南门涮肉(上海一店)"}, {"date": "2026-06-21", "type": "dinner", "name": "南门涮肉(上海一店)"}]}]}]`

### v3_harder_eval_000017
- request: 苏州 2026-05-06->2026-05-10 days=5 transport=公共交通 hotel=民宿 prefs=['小众展馆', '咖啡', '艺术', '城市漫步', '特色餐厅']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "秋娟馄饨店", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-05-06", "type": "breakfast", "name": "秋娟馄饨店"}, {"date": "2026-05-07", "type": "breakfast", "name": "秋娟馄饨店"}, {"date": "2026-05-08", "type": "breakfast", "name": "秋娟馄饨店"}, {"date": "2026-05-09", "type": "breakfast", "name": "秋娟馄饨店"}, {"date": "2026-05-10", "type": "breakfast", "name": "秋娟馄饨店"}]}, {"name_key": "老横泾面馆", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-05-06", "type": "lunch", "name": "老横泾面馆(吴中横泾总店)"}, {"date": "2026-05-07", "type": "lunch", "name": "老横泾面馆(吴中横泾总店)"}, {"date": "2026-05-08", "type": "lunch", "name": "老横泾面馆(吴中横泾总店)"}, {"date": "2026-05-09", "type": "lunch", "name": "老横泾面馆(吴中横泾总店)"}, {"date": "2026-05-10", "type": "lunch", "name": "老横泾面馆(吴中横泾总店)"}]}, {"name_key": "江南雅厨·非遗苏州菜", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-05-06", "type": "dinner", "name": "江南雅厨·非遗苏州菜(李公堤店)"}, {"date": "2026-05-07", "type": "dinner", "name": "江南雅厨·非遗苏州菜(李公堤店)"}, {"date": "2026-05-08", "type": "dinner", "name": "江南雅厨·非遗苏州菜(李公堤店)"}, {"date": "2026-05-09", "type": "dinner", "name": "江南雅厨·非遗苏州菜(李公堤店)"}, {"date": "2026-05-10", "type": "dinner", "name": "江南雅厨·非遗苏州菜(李公堤店)"}]}]}]`

### v3_harder_eval_000020
- request: 杭州 2026-06-18->2026-06-22 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "柳来原味螺蛳粉", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-06-18", "type": "breakfast", "name": "柳来原味螺蛳粉(枫香路店)"}, {"date": "2026-06-19", "type": "breakfast", "name": "柳来原味螺蛳粉(枫香路店)"}, {"date": "2026-06-20", "type": "breakfast", "name": "柳来原味螺蛳粉(枫香路店)"}, {"date": "2026-06-21", "type": "breakfast", "name": "柳来原味螺蛳粉(枫香路店)"}, {"date": "2026-06-22", "type": "breakfast", "name": "柳来原味螺蛳粉(枫香路店)"}]}, {"name_key": "入江南·金奖杭帮菜·浙江菜", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-06-18", "type": "lunch", "name": "入江南·金奖杭帮菜·浙江菜(虎跑店)"}, {"date": "2026-06-19", "type": "lunch", "name": "入江南·金奖杭帮菜·浙江菜(虎跑店)"}, {"date": "2026-06-20", "type": "lunch", "name": "入江南·金奖杭帮菜·浙江菜(虎跑店)"}, {"date": "2026-06-21", "type": "lunch", "name": "入江南·金奖杭帮菜·浙江菜(虎跑店)"}, {"date": "2026-06-22", "type": "lunch", "name": "入江南·金奖杭帮菜·浙江菜(虎跑店)"}]}, {"name_key": "老姑东北人", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-06-18", "type": "dinner", "name": "老姑东北人(立涛园店)"}, {"date": "2026-06-19", "type": "dinner", "name": "老姑东北人(立涛园店)"}, {"date": "2026-06-20", "type": "dinner", "name": "老姑东北人(立涛园店)"}, {"date": "2026-06-21", "type": "dinner", "name": "老姑东北人(立涛园店)"}, {"date": "2026-06-22", "type": "dinner", "name": "老姑东北人(立涛园店)"}]}]}]`
