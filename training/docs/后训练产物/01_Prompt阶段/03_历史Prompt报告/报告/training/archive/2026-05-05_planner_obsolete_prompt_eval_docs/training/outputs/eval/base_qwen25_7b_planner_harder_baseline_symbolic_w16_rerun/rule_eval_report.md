# Rule Eval Report: base_qwen25_7b_v3_harder_baseline_symbolic_w16_rerun

- records: 300
- generations: `training/outputs/eval/base_qwen25_7b_v3_harder_baseline_symbolic_w16_rerun/generations.jsonl`
- records_path: `training/data/v3/eval_harder_food_bucket_meal_ablation_budget_symbolic_no_route/records.jsonl`

## Boolean Metrics

| Metric | Pass | Total | Rate |
| --- | ---: | ---: | ---: |
| attraction_count_ok | 297 | 297 | 100.00% |
| attraction_grounding_ok | 294 | 297 | 98.99% |
| budget_arithmetic_consistent | 279 | 297 | 93.94% |
| budget_consistent | 279 | 297 | 93.94% |
| budget_level_aligned | 288 | 297 | 96.97% |
| budget_preference_aligned | 288 | 297 | 96.97% |
| budget_within_user_budget | 297 | 297 | 100.00% |
| city_ok | 297 | 297 | 100.00% |
| date_range_ok | 297 | 297 | 100.00% |
| day_dates_ok | 297 | 297 | 100.00% |
| day_index_ok | 297 | 297 | 100.00% |
| days_len_ok | 297 | 297 | 100.00% |
| dpo_soft_pass | 25 | 297 | 8.42% |
| hard_pass | 263 | 297 | 88.55% |
| hotel_budget_covers_nights | 297 | 297 | 100.00% |
| hotel_distance_placeholder_ok | 297 | 297 | 100.00% |
| hotel_grounding_ok | 297 | 297 | 100.00% |
| invalid_hotel_name_ok | 297 | 297 | 100.00% |
| json_extract_ok | 300 | 300 | 100.00% |
| legacy_hard_pass | 25 | 297 | 8.42% |
| location_object_ok | 297 | 297 | 100.00% |
| meal_complete | 292 | 297 | 98.32% |
| meal_diversity_ok | 31 | 297 | 10.44% |
| meal_grounding_ok | 285 | 297 | 95.96% |
| meal_lunch_dinner_same_day_ok | 160 | 297 | 53.87% |
| meal_repeat_limit_ok | 52 | 297 | 17.51% |
| meal_specific_ok | 297 | 297 | 100.00% |
| meal_valid_semantics_ok | 287 | 297 | 96.63% |
| middle_hotel_ok | 296 | 297 | 99.66% |
| schema_ok | 297 | 300 | 99.00% |
| sft_hard_pass | 263 | 297 | 88.55% |
| weather_dates_ok | 297 | 297 | 100.00% |
| weather_match | 297 | 297 | 100.00% |

## Numeric Metrics

```json
{
  "attraction_grounding_rate": {
    "avg": 0.9979,
    "p50": 1.0,
    "p90": 1.0
  },
  "hotel_grounding_rate": {
    "avg": 1.0,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_diversity_unique_rate": {
    "avg": 0.3525,
    "p50": 0.25,
    "p90": 0.6667
  },
  "meal_food_pois_grounding_rate": {
    "avg": 0.9929,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_grounding_rate": {
    "avg": 0.9929,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_semantic_valid_rate": {
    "avg": 0.9949,
    "p50": 1.0,
    "p90": 1.0
  }
}
```

## Failure Types

```json
{
  "meal_repeat_too_many": 245,
  "meal_same_day_lunch_dinner_repeat": 137,
  "budget_arithmetic_inconsistent": 18,
  "meal_invalid_name": 10,
  "budget_preference_mismatch": 9,
  "schema": 3,
  "meal_grounding_miss": 2,
  "middle_hotel_null": 1
}
```

## Failure Examples

### v3_harder_eval_000011
- request: 福州 2026-06-18->2026-06-21 days=4 transport=打车 hotel=高端酒店 prefs=['高端酒店', '艺术', '特色餐厅', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "某有茶·黑糖珍珠奶茶", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-06-18", "type": "breakfast", "name": "某有茶·黑糖珍珠奶茶(三坊七巷店)"}, {"date": "2026-06-19", "type": "breakfast", "name": "某有茶·黑糖珍珠奶茶(三坊七巷店)"}, {"date": "2026-06-20", "type": "breakfast", "name": "某有茶·黑糖珍珠奶茶(三坊七巷店)"}, {"date": "2026-06-21", "type": "breakfast", "name": "某有茶·黑糖珍珠奶茶(三坊七巷店)"}, {"date": "2026-06-21", "type": "dinner", "name": "某有茶·黑糖珍珠奶茶(仓山万达金街店)"}]}, {"name_key": "紫阳海鲜楼·传承闽味", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-06-18", "type": "dinner", "name": "紫阳海鲜楼·传承闽味(长乐路总店)"}, {"date": "2026-06-19", "type": "dinner", "name": "紫阳海鲜楼·传承闽味(华林路店)"}, {"date": "2026-06-20", "type": "lunch", "name": "紫阳海鲜楼·传承闽味(华林路店)"}, {"date": "2026-06-21", "type": "lunch", "name": "紫阳海鲜楼·传承闽味(华林路店)"}]}]}]`

### v3_harder_eval_000000
- request: 昆明 2026-04-04->2026-04-08 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-04-04", "lunch": "四方小炒·云南菜小当家(联盟店)", "dinner": "四方小炒·云南菜小当家(联盟店)"}, {"date": "2026-04-05", "lunch": "四方小炒·云南菜小当家(联盟店)", "dinner": "四方小炒·云南菜小当家(联盟店)"}, {"date": "2026-04-06", "lunch": "四方小炒·云南菜小当家(联盟店)", "dinner": "四方小炒·云南菜小当家(联盟店)"}, {"date": "2026-04-07", "lunch": "四方小炒·云南菜小当家(联盟店)", "dinner": "四方小炒·云南菜小当家(联盟店)"}, {"date": "2026-04-08", "lunch": "四方小炒·云南菜小当家(联盟店)", "dinner": "四方小炒·云南菜小当家(联盟店)"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "晨曦豆花米线", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-04-04", "type": "breakfast", "name": "晨曦豆花米线"}, {"date": "2026-04-05", "type": "breakfast", "name": "晨曦豆花米线"}, {"date": "2026-04-06", "type": "breakfast", "name": "晨曦豆花米线"}, {"date": "2026-04-07", "type": "breakfast", "name": "晨曦豆花米线"}, {"date": "2026-04-08", "type": "breakfast", "name": "晨曦豆花米线"}]}, {"name_key": "四方小炒·云南菜小当家", "count": 10, "max_allowed": 3, "occurrences": [{"date": "2026-04-04", "type": "lunch", "name": "四方小炒·云南菜小当家(联盟店)"}, {"date": "2026-04-04", "type": "dinner", "name": "四方小炒·云南菜小当家(联盟店)"}, {"date": "2026-04-05", "type": "lunch", "name": "四方小炒·云南菜小当家(联盟店)"}, {"date": "2026-04-05", "type": "dinner", "name": "四方小炒·云南菜小当家(联盟店)"}, {"date": "2026-04-06", "type": "lunch", "name": "四方小炒·云南菜小当家(联盟店)"}, {"date": "2026-04-06", "type": "dinner", "name": "四方小炒·云南菜小当家(联盟店)"}, {"date": "2026-04-07", "type": "lunch", "name": "四方小炒·云南菜小当家(联盟店)"}, {"date": "2026-04-07", "type": "dinner", "name": "四方小炒·云南菜小当家(联盟店)"}, {"date": "2026-04-08", "type": "lunch", "name": "四方小炒·云南菜小当家(联盟店)"}, {"date": "2026-04-08", "type": "dinner", "name": "四方小炒·云南菜小当家(联盟店)"}]}]}]`

### v3_harder_eval_000003
- request: 西安 2025-05-04->2025-05-08 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "魏家凉皮", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2025-05-04", "type": "breakfast", "name": "魏家凉皮(西大街店)"}, {"date": "2025-05-05", "type": "breakfast", "name": "魏家凉皮(西大街店)"}, {"date": "2025-05-06", "type": "breakfast", "name": "魏家凉皮(西大街店)"}, {"date": "2025-05-07", "type": "breakfast", "name": "魏家凉皮(西大街店)"}, {"date": "2025-05-08", "type": "breakfast", "name": "魏家凉皮(西大街店)"}]}, {"name_key": "李志贤灌汤包子", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2025-05-04", "type": "lunch", "name": "李志贤灌汤包子"}, {"date": "2025-05-05", "type": "lunch", "name": "李志贤灌汤包子"}, {"date": "2025-05-06", "type": "lunch", "name": "李志贤灌汤包子"}, {"date": "2025-05-07", "type": "lunch", "name": "李志贤灌汤包子"}, {"date": "2025-05-08", "type": "lunch", "name": "李志贤灌汤包子"}]}, {"name_key": "崔少野猫耳朵炒面", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2025-05-04", "type": "dinner", "name": "崔少野猫耳朵炒面(十里锦绣店)"}, {"date": "2025-05-05", "type": "dinner", "name": "崔少野猫耳朵炒面(十里锦绣店)"}, {"date": "2025-05-06", "type": "dinner", "name": "崔少野猫耳朵炒面(十里锦绣店)"}, {"date": "2025-05-07", "type": "dinner", "name": "崔少野猫耳朵炒面(十里锦绣店)"}, {"date": "2025-05-08", "type": "dinner", "name": "崔少野猫耳朵炒面(十里锦绣店)"}]}]}]`

### v3_harder_eval_000012
- request: 洛阳 2025-05-04->2025-05-07 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '夜市', '老字号', '城市漫步']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2025-05-04", "lunch": "洛阳十字街小吃一条街", "dinner": "洛阳十字街小吃一条街"}, {"date": "2025-05-05", "lunch": "小街天府", "dinner": "小街天府"}, {"date": "2025-05-06", "lunch": "光头东烙馍村·水席洛阳菜(火车站店)", "dinner": "光头东烙馍村·水席洛阳菜(火车站店)"}, {"date": "2025-05-07", "lunch": "必胜客(正大广场店)", "dinner": "必胜客(正大广场店)"}]}, {"stage": "rule", "type": "budget_preference_mismatch", "details": {"part_sum": 3368, "total": 3368, "diff": 0, "requested_budget": {"available": false, "amount": 0, "scope": "unknown", "party_size": 2, "total": 0}, "per_person_day": 421.0, "budget_level": "limited", "arithmetic_consistent": true, "within_user_budget": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 3, "priced_nights": 3, "expected_min_total_hotels": 700, "reported_total_hotels": 1200, "diff": 500, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_harder_eval_000007
- request: 成都 2026-05-08->2026-05-12 days=5 transport=公共交通 hotel=民宿 prefs=['小众展馆', '咖啡', '艺术', '城市漫步', '特色餐厅']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-05-08", "lunch": "观锦餐厅(天府新谷店)", "dinner": "观锦餐厅(天廊店)"}, {"date": "2026-05-09", "lunch": "观锦餐厅(天府新谷店)", "dinner": "观锦餐厅(天廊店)"}, {"date": "2026-05-10", "lunch": "观锦餐厅(天府新谷店)", "dinner": "观锦餐厅(天廊店)"}, {"date": "2026-05-11", "lunch": "观锦餐厅(天府新谷店)", "dinner": "观锦餐厅(天廊店)"}, {"date": "2026-05-12", "lunch": "观锦餐厅(天府新谷店)", "dinner": "观锦餐厅(天廊店)"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "四妹钵钵鸡", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-05-08", "type": "breakfast", "name": "四妹钵钵鸡(望平街店)"}, {"date": "2026-05-09", "type": "breakfast", "name": "四妹钵钵鸡(望平街店)"}, {"date": "2026-05-10", "type": "breakfast", "name": "四妹钵钵鸡(望平街店)"}, {"date": "2026-05-11", "type": "breakfast", "name": "四妹钵钵鸡(望平街店)"}, {"date": "2026-05-12", "type": "breakfast", "name": "四妹钵钵鸡(望平街店)"}]}, {"name_key": "观锦餐厅", "count": 10, "max_allowed": 3, "occurrences": [{"date": "2026-05-08", "type": "lunch", "name": "观锦餐厅(天府新谷店)"}, {"date": "2026-05-08", "type": "dinner", "name": "观锦餐厅(天廊店)"}, {"date": "2026-05-09", "type": "lunch", "name": "观锦餐厅(天府新谷店)"}, {"date": "2026-05-09", "type": "dinner", "name": "观锦餐厅(天廊店)"}, {"date": "2026-05-10", "type": "lunch", "name": "观锦餐厅(天府新谷店)"}, {"date": "2026-05-10", "type": "dinner", "name": "观锦餐厅(天廊店)"}, {"date": "2026-05-11", "type": "lunch", "name": "观锦餐厅(天府新谷店)"}, {"date": "2026-05-11", "type": "dinner", "name": "观锦餐厅(天廊店)"}, {"date": "2026-05-12", "type": "lunch", "name": "观锦餐厅(天府新谷店)"}, {"date": "2026-05-12", "type": "dinner", "name": "观锦餐厅(天廊店)"}]}]}]`

### v3_harder_eval_000005
- request: 广州 2026-07-03->2026-07-07 days=5 transport=公共交通 hotel=民宿 prefs=['摄影', '自然风光', '城市漫步', '本地菜']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "欧记大排档·江西景德菜", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-07-03", "type": "lunch", "name": "欧记大排档·江西景德菜(广州首店)"}, {"date": "2026-07-04", "type": "lunch", "name": "欧记大排档·江西景德菜(广州首店)"}, {"date": "2026-07-05", "type": "lunch", "name": "欧记大排档·江西景德菜(广州首店)"}, {"date": "2026-07-06", "type": "lunch", "name": "欧记大排档·江西景德菜(广州首店)"}, {"date": "2026-07-07", "type": "lunch", "name": "欧记大排档·江西景德菜(广州首店)"}]}, {"name_key": "银灯食府", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-07-03", "type": "dinner", "name": "银灯食府(文化公园店)"}, {"date": "2026-07-04", "type": "dinner", "name": "银灯食府(文化公园店)"}, {"date": "2026-07-05", "type": "dinner", "name": "银灯食府(文化公园店)"}, {"date": "2026-07-06", "type": "dinner", "name": "银灯食府(文化公园店)"}, {"date": "2026-07-07", "type": "dinner", "name": "银灯食府(文化公园店)"}]}]}]`

### v3_harder_eval_000013
- request: 武汉 2026-05-06->2026-05-10 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-05-06", "lunch": "刘聋子牛肉粉馆(汉阳龙兴东街店)", "dinner": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "方记老上海馄饨铺", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-05-06", "type": "breakfast", "name": "方记老上海馄饨铺(中南店)"}, {"date": "2026-05-07", "type": "breakfast", "name": "方记老上海馄饨铺(中南店)"}, {"date": "2026-05-08", "type": "breakfast", "name": "方记老上海馄饨铺(中南店)"}, {"date": "2026-05-09", "type": "breakfast", "name": "方记老上海馄饨铺(中南店)"}, {"date": "2026-05-10", "type": "breakfast", "name": "方记老上海馄饨铺(中南店)"}]}, {"name_key": "刘聋子牛肉粉馆", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-05-06", "type": "lunch", "name": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}, {"date": "2026-05-06", "type": "dinner", "name": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}, {"date": "2026-05-07", "type": "dinner", "name": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}, {"date": "2026-05-08", "type": "dinner", "name": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}, {"date": "2026-05-09", "type": "dinner", "name": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}]}]}]`

### v3_harder_eval_000019
- request: 丽江 2026-05-08->2026-05-11 days=4 transport=打车 hotel=亲子酒店 prefs=['亲子', '老人友好', '博物馆', '城市公园', '特色餐厅']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-05-08", "lunch": "则瓦米线·云南小吃集合(花巷店)", "dinner": "则瓦米线·云南小吃集合(花巷店)"}, {"date": "2026-05-09", "lunch": "则瓦米线·云南小吃集合(花巷店)", "dinner": "则瓦米线·云南小吃集合(花巷店)"}, {"date": "2026-05-10", "lunch": "则瓦米线·云南小吃集合(花巷店)", "dinner": "则瓦米线·云南小吃集合(花巷店)"}, {"date": "2026-05-11", "lunch": "则瓦米线·云南小吃集合(花巷店)", "dinner": "则瓦米线·云南小吃集合(花巷店)"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "则瓦米线·云南小吃集合", "count": 12, "max_allowed": 3, "occurrences": [{"date": "2026-05-08", "type": "breakfast", "name": "则瓦米线·云南小吃集合(花巷店)"}, {"date": "2026-05-08", "type": "lunch", "name": "则瓦米线·云南小吃集合(花巷店)"}, {"date": "2026-05-08", "type": "dinner", "name": "则瓦米线·云南小吃集合(花巷店)"}, {"date": "2026-05-09", "type": "breakfast", "name": "则瓦米线·云南小吃集合(花巷店)"}, {"date": "2026-05-09", "type": "lunch", "name": "则瓦米线·云南小吃集合(花巷店)"}, {"date": "2026-05-09", "type": "dinner", "name": "则瓦米线·云南小吃集合(花巷店)"}, {"date": "2026-05-10", "type": "breakfast", "name": "则瓦米线·云南小吃集合(花巷店)"}, {"date": "2026-05-10", "type": "lunch", "name": "则瓦米线·云南小吃集合(花巷店)"}, {"date": "2026-05-10", "type": "dinner", "name": "则瓦米线·云南小吃集合(花巷店)"}, {"date": "2026-05-11", "type": "breakfast", "name": "则瓦米线·云南小吃集合(花巷店)"}]}]}]`

### v3_harder_eval_000028
- request: 深圳 2026-03-05->2026-03-07 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-03-05", "lunch": "欧记大排档·江西景德菜(南山保利店)", "dinner": "欧记大排档·江西景德菜(南山保利店)"}, {"date": "2026-03-06", "lunch": "南门涮肉(深圳首店)", "dinner": "南门涮肉(深圳首店)"}, {"date": "2026-03-07", "lunch": "蘩楼(华强北总店)", "dinner": "蘩楼(华强北总店)"}]}]`

### v3_harder_eval_000031
- request: 成都 2026-05-08->2026-05-11 days=4 transport=打车 hotel=高端酒店 prefs=['高端酒店', '艺术', '特色餐厅', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "四妹钵钵鸡", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-05-08", "type": "breakfast", "name": "四妹钵钵鸡(望平街店)"}, {"date": "2026-05-09", "type": "breakfast", "name": "四妹钵钵鸡(望平街店)"}, {"date": "2026-05-10", "type": "breakfast", "name": "四妹钵钵鸡(望平街店)"}, {"date": "2026-05-11", "type": "breakfast", "name": "四妹钵钵鸡(望平街店)"}]}, {"name_key": "观锦餐厅", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-05-08", "type": "lunch", "name": "观锦餐厅(天府新谷店)"}, {"date": "2026-05-09", "type": "lunch", "name": "观锦餐厅(天廊店)"}, {"date": "2026-05-10", "type": "lunch", "name": "观锦餐厅(天廊店)"}, {"date": "2026-05-11", "type": "lunch", "name": "观锦餐厅(天廊店)"}]}, {"name_key": "南堂馆川菜文化餐厅", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-05-08", "type": "dinner", "name": "南堂馆川菜文化餐厅(天府店)"}, {"date": "2026-05-09", "type": "dinner", "name": "南堂馆川菜文化餐厅(天府店)"}, {"date": "2026-05-10", "type": "dinner", "name": "南堂馆川菜文化餐厅(天府店)"}, {"date": "2026-05-11", "type": "dinner", "name": "南堂馆川菜文化餐厅(天府店)"}]}]}]`

### v3_harder_eval_000021
- request: 上海 2026-06-18->2026-06-21 days=4 transport=打车 hotel=高端酒店 prefs=['高端酒店', '艺术', '特色餐厅', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-06-20", "lunch": "红子鸡凤凰楼", "dinner": "红子鸡凤凰楼"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "红子鸡凤凰楼", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-06-18", "type": "lunch", "name": "红子鸡凤凰楼"}, {"date": "2026-06-19", "type": "dinner", "name": "红子鸡凤凰楼"}, {"date": "2026-06-20", "type": "lunch", "name": "红子鸡凤凰楼"}, {"date": "2026-06-20", "type": "dinner", "name": "红子鸡凤凰楼"}, {"date": "2026-06-21", "type": "lunch", "name": "红子鸡凤凰楼"}]}]}]`

### v3_harder_eval_000023
- request: 大理 2026-09-01->2026-09-05 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "挖色菜香园", "count": 10, "max_allowed": 3, "occurrences": [{"date": "2026-09-01", "type": "breakfast", "name": "挖色菜香园"}, {"date": "2026-09-01", "type": "dinner", "name": "挖色菜香园"}, {"date": "2026-09-02", "type": "breakfast", "name": "挖色菜香园"}, {"date": "2026-09-02", "type": "dinner", "name": "挖色菜香园"}, {"date": "2026-09-03", "type": "breakfast", "name": "挖色菜香园"}, {"date": "2026-09-03", "type": "dinner", "name": "挖色菜香园"}, {"date": "2026-09-04", "type": "breakfast", "name": "挖色菜香园"}, {"date": "2026-09-04", "type": "dinner", "name": "挖色菜香园"}, {"date": "2026-09-05", "type": "breakfast", "name": "挖色菜香园"}, {"date": "2026-09-05", "type": "dinner", "name": "挖色菜香园"}]}, {"name_key": "岛七白族人家火烧猪私房菜", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-09-01", "type": "lunch", "name": "岛七白族人家火烧猪私房菜"}, {"date": "2026-09-02", "type": "lunch", "name": "岛七白族人家火烧猪私房菜"}, {"date": "2026-09-03", "type": "lunch", "name": "岛七白族人家火烧猪私房菜"}, {"date": "2026-09-04", "type": "lunch", "name": "岛七白族人家火烧猪私房菜"}, {"date": "2026-09-05", "type": "lunch", "name": "岛七白族人家火烧猪私房菜"}]}]}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 4152, "total": 3152, "diff": 1000, "requested_budget": {"available": false, "amount": 0, "scope": "unknown", "party_size": 3, "total": 0}, "per_person_day": 210.13, "budget_level": "standard", "arithmetic_consistent": false, "within_user_budget": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 4, "priced_nights": 4, "expected_min_total_hotels": 1600, "reported_total_hotels": 1600, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_harder_eval_000017
- request: 苏州 2026-05-06->2026-05-10 days=5 transport=公共交通 hotel=民宿 prefs=['小众展馆', '咖啡', '艺术', '城市漫步', '特色餐厅']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "秋娟馄饨店", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-05-06", "type": "breakfast", "name": "秋娟馄饨店"}, {"date": "2026-05-07", "type": "breakfast", "name": "秋娟馄饨店"}, {"date": "2026-05-08", "type": "breakfast", "name": "秋娟馄饨店"}, {"date": "2026-05-09", "type": "breakfast", "name": "秋娟馄饨店"}, {"date": "2026-05-10", "type": "breakfast", "name": "秋娟馄饨店"}]}, {"name_key": "烟雨人家特色农家菜", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-05-06", "type": "lunch", "name": "烟雨人家特色农家菜(周庄店)"}, {"date": "2026-05-07", "type": "lunch", "name": "烟雨人家特色农家菜(周庄店)"}, {"date": "2026-05-08", "type": "lunch", "name": "烟雨人家特色农家菜(周庄店)"}, {"date": "2026-05-09", "type": "lunch", "name": "烟雨人家特色农家菜(周庄店)"}, {"date": "2026-05-10", "type": "lunch", "name": "烟雨人家特色农家菜(周庄店)"}]}, {"name_key": "江南雅厨·非遗苏州菜", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-05-06", "type": "dinner", "name": "江南雅厨·非遗苏州菜(李公堤店)"}, {"date": "2026-05-07", "type": "dinner", "name": "江南雅厨·非遗苏州菜(李公堤店)"}, {"date": "2026-05-08", "type": "dinner", "name": "江南雅厨·非遗苏州菜(李公堤店)"}, {"date": "2026-05-09", "type": "dinner", "name": "江南雅厨·非遗苏州菜(李公堤店)"}, {"date": "2026-05-10", "type": "dinner", "name": "江南雅厨·非遗苏州菜(李公堤店)"}]}]}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 4240, "total": 3240, "diff": 1000, "requested_budget": {"available": false, "amount": 0, "scope": "unknown", "party_size": 2, "total": 0}, "per_person_day": 324.0, "budget_level": "comfortable", "arithmetic_consistent": false, "within_user_budget": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 4, "priced_nights": 4, "expected_min_total_hotels": 1200, "reported_total_hotels": 1200, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_harder_eval_000025
- request: 上海 2026-08-02->2026-08-06 days=5 transport=公共交通 hotel=民宿 prefs=['摄影', '自然风光', '城市漫步', '本地菜']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-08-02", "lunch": "外滩家宴·上海菜(外滩豫园店)", "dinner": "外滩家宴·上海菜(外滩豫园店)"}, {"date": "2026-08-03", "lunch": "外滩家宴·上海菜(外滩豫园店)", "dinner": "外滩家宴·上海菜(外滩豫园店)"}, {"date": "2026-08-04", "lunch": "外滩家宴·上海菜(外滩豫园店)", "dinner": "外滩家宴·上海菜(外滩豫园店)"}, {"date": "2026-08-05", "lunch": "外滩家宴·上海菜(外滩豫园店)", "dinner": "外滩家宴·上海菜(外滩豫园店)"}, {"date": "2026-08-06", "lunch": "外滩家宴·上海菜(外滩豫园店)", "dinner": "外滩家宴·上海菜(外滩豫园店)"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "外滩家宴·上海菜", "count": 10, "max_allowed": 3, "occurrences": [{"date": "2026-08-02", "type": "lunch", "name": "外滩家宴·上海菜(外滩豫园店)"}, {"date": "2026-08-02", "type": "dinner", "name": "外滩家宴·上海菜(外滩豫园店)"}, {"date": "2026-08-03", "type": "lunch", "name": "外滩家宴·上海菜(外滩豫园店)"}, {"date": "2026-08-03", "type": "dinner", "name": "外滩家宴·上海菜(外滩豫园店)"}, {"date": "2026-08-04", "type": "lunch", "name": "外滩家宴·上海菜(外滩豫园店)"}, {"date": "2026-08-04", "type": "dinner", "name": "外滩家宴·上海菜(外滩豫园店)"}, {"date": "2026-08-05", "type": "lunch", "name": "外滩家宴·上海菜(外滩豫园店)"}, {"date": "2026-08-05", "type": "dinner", "name": "外滩家宴·上海菜(外滩豫园店)"}, {"date": "2026-08-06", "type": "lunch", "name": "外滩家宴·上海菜(外滩豫园店)"}, {"date": "2026-08-06", "type": "dinner", "name": "外滩家宴·上海菜(外滩豫园店)"}]}]}]`

### v3_harder_eval_000027
- request: 杭州 2026-05-06->2026-05-10 days=5 transport=公共交通 hotel=民宿 prefs=['小众展馆', '咖啡', '艺术', '城市漫步', '特色餐厅']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "知味观", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-05-06", "type": "lunch", "name": "知味观(湖滨总店)"}, {"date": "2026-05-08", "type": "lunch", "name": "知味观(湖滨总店)"}, {"date": "2026-05-09", "type": "lunch", "name": "知味观(湖滨总店)"}, {"date": "2026-05-10", "type": "lunch", "name": "知味观(湖滨总店)"}]}, {"name_key": "杭州酒家", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-05-06", "type": "dinner", "name": "杭州酒家(延安路店)"}, {"date": "2026-05-07", "type": "dinner", "name": "杭州酒家(延安路店)"}, {"date": "2026-05-08", "type": "dinner", "name": "杭州酒家(延安路店)"}, {"date": "2026-05-09", "type": "dinner", "name": "杭州酒家(延安路店)"}]}]}]`

### v3_harder_eval_000039
- request: 深圳 2025-11-05->2025-11-08 days=4 transport=打车 hotel=亲子酒店 prefs=['亲子', '老人友好', '博物馆', '城市公园', '特色餐厅']
- errors: `[{"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2025-11-08", "type": "dinner", "name": "酒店晚餐", "reason": "generic_lodging_meal"}]}, {"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2025-11-05", "lunch": "蘩楼(华强北总店)", "dinner": "蘩楼(华强北总店)"}, {"date": "2025-11-06", "lunch": "蘩楼(华强北总店)", "dinner": "蘩楼(华强北总店)"}, {"date": "2025-11-07", "lunch": "蘩楼(华强北总店)", "dinner": "蘩楼(华强北总店)"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "蘩楼", "count": 7, "max_allowed": 3, "occurrences": [{"date": "2025-11-05", "type": "lunch", "name": "蘩楼(华强北总店)"}, {"date": "2025-11-05", "type": "dinner", "name": "蘩楼(华强北总店)"}, {"date": "2025-11-06", "type": "lunch", "name": "蘩楼(华强北总店)"}, {"date": "2025-11-06", "type": "dinner", "name": "蘩楼(华强北总店)"}, {"date": "2025-11-07", "type": "lunch", "name": "蘩楼(华强北总店)"}, {"date": "2025-11-07", "type": "dinner", "name": "蘩楼(华强北总店)"}, {"date": "2025-11-08", "type": "lunch", "name": "蘩楼(华强北总店)"}]}]}]`

### v3_harder_eval_000033
- request: 苏州 2026-05-08->2026-05-12 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-05-08", "lunch": "稻山村·苏州菜(石路店)", "dinner": "稻山村·苏州菜(曼哈顿店)"}, {"date": "2026-05-09", "lunch": "稻山村·苏州菜(石路店)", "dinner": "稻山村·苏州菜(曼哈顿店)"}, {"date": "2026-05-10", "lunch": "稻山村·苏州菜(石路店)", "dinner": "稻山村·苏州菜(曼哈顿店)"}, {"date": "2026-05-11", "lunch": "稻山村·苏州菜(石路店)", "dinner": "稻山村·苏州菜(曼哈顿店)"}, {"date": "2026-05-12", "lunch": "稻山村·苏州菜(石路店)", "dinner": "稻山村·苏州菜(曼哈顿店)"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "魏家凉皮", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-05-08", "type": "breakfast", "name": "魏家凉皮(邵磨针巷店)"}, {"date": "2026-05-09", "type": "breakfast", "name": "魏家凉皮(邵磨针巷店)"}, {"date": "2026-05-10", "type": "breakfast", "name": "魏家凉皮(邵磨针巷店)"}, {"date": "2026-05-11", "type": "breakfast", "name": "魏家凉皮(邵磨针巷店)"}, {"date": "2026-05-12", "type": "breakfast", "name": "魏家凉皮(邵磨针巷店)"}]}, {"name_key": "稻山村·苏州菜", "count": 10, "max_allowed": 3, "occurrences": [{"date": "2026-05-08", "type": "lunch", "name": "稻山村·苏州菜(石路店)"}, {"date": "2026-05-08", "type": "dinner", "name": "稻山村·苏州菜(曼哈顿店)"}, {"date": "2026-05-09", "type": "lunch", "name": "稻山村·苏州菜(石路店)"}, {"date": "2026-05-09", "type": "dinner", "name": "稻山村·苏州菜(曼哈顿店)"}, {"date": "2026-05-10", "type": "lunch", "name": "稻山村·苏州菜(石路店)"}, {"date": "2026-05-10", "type": "dinner", "name": "稻山村·苏州菜(曼哈顿店)"}, {"date": "2026-05-11", "type": "lunch", "name": "稻山村·苏州菜(石路店)"}, {"date": "2026-05-11", "type": "dinner", "name": "稻山村·苏州菜(曼哈顿店)"}, {"date": "2026-05-12", "type": "lunch", "name": "稻山村·苏州菜(石路店)"}, {"date": "2026-05-12", "type": "dinner", "name": "稻山村·苏州菜(曼哈顿店)"}]}]}]`

### v3_harder_eval_000035
- request: 深圳 2026-09-01->2026-09-05 days=5 transport=公共交通 hotel=民宿 prefs=['摄影', '自然风光', '城市漫步', '本地菜']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-09-01", "lunch": "欧记大排档•江西景德菜(深圳首店)", "dinner": "欧记大排档•江西景德菜(南山保利店)"}, {"date": "2026-09-02", "lunch": "欧记大排档·江西景德菜(南山保利店)", "dinner": "欧记大排档·江西景德菜(罗湖东门町店)"}, {"date": "2026-09-03", "lunch": "欧记大排档·江西景德菜(南山保利店)", "dinner": "欧记大排档·江西景德菜(罗湖东门町店)"}, {"date": "2026-09-04", "lunch": "欧记大排档·江西景德菜(南山保利店)", "dinner": "欧记大排档·江西景德菜(罗湖东门町店)"}, {"date": "2026-09-05", "lunch": "欧记大排档·江西景德菜(南山保利店)", "dinner": "欧记大排档·江西景德菜(罗湖东门町店)"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "欧记大排档·江西景德菜", "count": 8, "max_allowed": 3, "occurrences": [{"date": "2026-09-02", "type": "lunch", "name": "欧记大排档·江西景德菜(南山保利店)"}, {"date": "2026-09-02", "type": "dinner", "name": "欧记大排档·江西景德菜(罗湖东门町店)"}, {"date": "2026-09-03", "type": "lunch", "name": "欧记大排档·江西景德菜(南山保利店)"}, {"date": "2026-09-03", "type": "dinner", "name": "欧记大排档·江西景德菜(罗湖东门町店)"}, {"date": "2026-09-04", "type": "lunch", "name": "欧记大排档·江西景德菜(南山保利店)"}, {"date": "2026-09-04", "type": "dinner", "name": "欧记大排档·江西景德菜(罗湖东门町店)"}, {"date": "2026-09-05", "type": "lunch", "name": "欧记大排档·江西景德菜(南山保利店)"}, {"date": "2026-09-05", "type": "dinner", "name": "欧记大排档·江西景德菜(罗湖东门町店)"}]}]}]`

### v3_harder_eval_000029
- request: 长沙 2026-03-05->2026-03-08 days=4 transport=打车 hotel=亲子酒店 prefs=['亲子', '老人友好', '博物馆', '城市公园', '特色餐厅']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-03-05", "lunch": "喜座·湖南美食村落(总店)", "dinner": "喜座·湖南美食村落(总店)"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "喜座·湖南美食村落", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-03-05", "type": "lunch", "name": "喜座·湖南美食村落(总店)"}, {"date": "2026-03-05", "type": "dinner", "name": "喜座·湖南美食村落(总店)"}, {"date": "2026-03-06", "type": "dinner", "name": "喜座·湖南美食村落(总店)"}, {"date": "2026-03-07", "type": "dinner", "name": "喜座·湖南美食村落(总店)"}, {"date": "2026-03-08", "type": "dinner", "name": "喜座·湖南美食村落(总店)"}]}]}]`

### v3_harder_eval_000044
- request: 西安 2025-05-04->2025-05-06 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "魏家凉皮", "count": 3, "max_allowed": 2, "occurrences": [{"date": "2025-05-04", "type": "breakfast", "name": "魏家凉皮(西大街店)"}, {"date": "2025-05-05", "type": "breakfast", "name": "魏家凉皮(西大街店)"}, {"date": "2025-05-06", "type": "breakfast", "name": "魏家凉皮(西大街店)"}]}, {"name_key": "马洪小炒泡馍馆", "count": 3, "max_allowed": 2, "occurrences": [{"date": "2025-05-04", "type": "dinner", "name": "马洪小炒泡馍馆"}, {"date": "2025-05-05", "type": "dinner", "name": "马洪小炒泡馍馆"}, {"date": "2025-05-06", "type": "dinner", "name": "马洪小炒泡馍馆"}]}]}]`
