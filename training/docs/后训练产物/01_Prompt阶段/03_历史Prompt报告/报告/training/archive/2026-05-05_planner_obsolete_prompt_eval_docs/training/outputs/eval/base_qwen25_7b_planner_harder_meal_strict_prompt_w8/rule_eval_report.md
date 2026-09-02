# Rule Eval Report: base_qwen25_7b_v3_harder_meal_strict_prompt_w8

- records: 300
- generations: `training/outputs/eval/base_qwen25_7b_v3_harder_meal_strict_prompt_w8/generations.jsonl`
- records_path: `training/data/v3/eval_harder_food_bucket_meal_strict_no_route/records.jsonl`

## Boolean Metrics

| Metric | Pass | Total | Rate |
| --- | ---: | ---: | ---: |
| attraction_count_ok | 292 | 292 | 100.00% |
| attraction_grounding_ok | 284 | 292 | 97.26% |
| budget_arithmetic_consistent | 269 | 292 | 92.12% |
| budget_consistent | 269 | 292 | 92.12% |
| budget_level_aligned | 286 | 292 | 97.95% |
| budget_preference_aligned | 286 | 292 | 97.95% |
| budget_within_user_budget | 292 | 292 | 100.00% |
| city_ok | 292 | 292 | 100.00% |
| date_range_ok | 292 | 292 | 100.00% |
| day_dates_ok | 292 | 292 | 100.00% |
| day_index_ok | 292 | 292 | 100.00% |
| days_len_ok | 292 | 292 | 100.00% |
| dpo_soft_pass | 59 | 292 | 20.21% |
| hard_pass | 232 | 292 | 79.45% |
| hotel_budget_covers_nights | 291 | 292 | 99.66% |
| hotel_distance_placeholder_ok | 292 | 292 | 100.00% |
| hotel_grounding_ok | 292 | 292 | 100.00% |
| invalid_hotel_name_ok | 292 | 292 | 100.00% |
| json_extract_ok | 300 | 300 | 100.00% |
| legacy_hard_pass | 63 | 292 | 21.58% |
| location_object_ok | 292 | 292 | 100.00% |
| meal_complete | 286 | 292 | 97.95% |
| meal_diversity_ok | 97 | 292 | 33.22% |
| meal_grounding_ok | 263 | 292 | 90.07% |
| meal_lunch_dinner_same_day_ok | 210 | 292 | 71.92% |
| meal_repeat_limit_ok | 121 | 292 | 41.44% |
| meal_specific_ok | 292 | 292 | 100.00% |
| meal_valid_semantics_ok | 264 | 292 | 90.41% |
| middle_hotel_ok | 292 | 292 | 100.00% |
| schema_ok | 292 | 300 | 97.33% |
| sft_hard_pass | 232 | 292 | 79.45% |
| weather_dates_ok | 292 | 292 | 100.00% |
| weather_match | 292 | 292 | 100.00% |

## Numeric Metrics

```json
{
  "attraction_grounding_rate": {
    "avg": 0.995,
    "p50": 1.0,
    "p90": 1.0
  },
  "hotel_grounding_rate": {
    "avg": 1.0,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_diversity_unique_rate": {
    "avg": 0.5621,
    "p50": 0.5333,
    "p90": 1.0
  },
  "meal_food_pois_grounding_rate": {
    "avg": 0.9899,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_grounding_rate": {
    "avg": 0.9899,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_semantic_valid_rate": {
    "avg": 0.9906,
    "p50": 1.0,
    "p90": 1.0
  }
}
```

## Failure Types

```json
{
  "meal_repeat_too_many": 171,
  "meal_same_day_lunch_dinner_repeat": 82,
  "meal_invalid_name": 28,
  "budget_arithmetic_inconsistent": 23,
  "schema": 8,
  "budget_preference_mismatch": 6,
  "hotel_budget_underestimated": 1,
  "meal_grounding_miss": 1
}
```

## Failure Examples

### v3_harder_eval_000008
- request: 大理 2026-05-08->2026-05-10 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "老爷爷的手工鲜花饼", "count": 3, "max_allowed": 2, "occurrences": [{"date": "2026-05-08", "type": "breakfast", "name": "老爷爷的手工鲜花饼(总店)"}, {"date": "2026-05-09", "type": "breakfast", "name": "老爷爷的手工鲜花饼(总店)"}, {"date": "2026-05-10", "type": "breakfast", "name": "老爷爷的手工鲜花饼(总店)"}]}, {"name_key": "桃红小馆·特色云南菜·庭院花园餐厅", "count": 3, "max_allowed": 2, "occurrences": [{"date": "2026-05-08", "type": "dinner", "name": "桃红小馆·特色云南菜·庭院花园餐厅"}, {"date": "2026-05-09", "type": "dinner", "name": "桃红小馆·特色云南菜·庭院花园餐厅"}, {"date": "2026-05-10", "type": "dinner", "name": "桃红小馆·特色云南菜·庭院花园餐厅"}]}]}]`

### v3_harder_eval_000001
- request: 桂林 2026-09-01->2026-09-04 days=4 transport=打车 hotel=高端酒店 prefs=['高端酒店', '艺术', '特色餐厅', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-09-01", "lunch": "椿记烧鹅(中山店)", "dinner": "椿记烧鹅(西街店)"}, {"date": "2026-09-02", "lunch": "椿记烧鹅(中山店)", "dinner": "椿记烧鹅(西街店)"}, {"date": "2026-09-03", "lunch": "椿记烧鹅(中山店)", "dinner": "椿记烧鹅(西街店)"}, {"date": "2026-09-04", "lunch": "椿记烧鹅(中山店)", "dinner": "椿记烧鹅(西街店)"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "椿记烧鹅", "count": 8, "max_allowed": 3, "occurrences": [{"date": "2026-09-01", "type": "lunch", "name": "椿记烧鹅(中山店)"}, {"date": "2026-09-01", "type": "dinner", "name": "椿记烧鹅(西街店)"}, {"date": "2026-09-02", "type": "lunch", "name": "椿记烧鹅(中山店)"}, {"date": "2026-09-02", "type": "dinner", "name": "椿记烧鹅(西街店)"}, {"date": "2026-09-03", "type": "lunch", "name": "椿记烧鹅(中山店)"}, {"date": "2026-09-03", "type": "dinner", "name": "椿记烧鹅(西街店)"}, {"date": "2026-09-04", "type": "lunch", "name": "椿记烧鹅(中山店)"}, {"date": "2026-09-04", "type": "dinner", "name": "椿记烧鹅(西街店)"}]}]}]`

### v3_harder_eval_000006
- request: 南京 2026-07-03->2026-07-06 days=4 transport=自驾 hotel=亲子酒店 prefs=['亲子', '动物园', '海洋馆', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-07-06", "type": "dinner", "name": "无", "reason": "empty_or_none"}]}]`

### v3_harder_eval_000000
- request: 昆明 2026-04-04->2026-04-08 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-04-04", "lunch": "四方小炒·云南菜小当家(联盟店)", "dinner": "四方小炒·云南菜小当家(同德店)"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "晨曦豆花米线", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-04-04", "type": "breakfast", "name": "晨曦豆花米线"}, {"date": "2026-04-05", "type": "breakfast", "name": "晨曦豆花米线"}, {"date": "2026-04-06", "type": "breakfast", "name": "晨曦豆花米线"}, {"date": "2026-04-07", "type": "breakfast", "name": "晨曦豆花米线"}, {"date": "2026-04-08", "type": "breakfast", "name": "晨曦豆花米线"}]}, {"name_key": "四方小炒·云南菜小当家", "count": 6, "max_allowed": 3, "occurrences": [{"date": "2026-04-04", "type": "lunch", "name": "四方小炒·云南菜小当家(联盟店)"}, {"date": "2026-04-04", "type": "dinner", "name": "四方小炒·云南菜小当家(同德店)"}, {"date": "2026-04-05", "type": "dinner", "name": "四方小炒·云南菜小当家(联盟店)"}, {"date": "2026-04-06", "type": "dinner", "name": "四方小炒·云南菜小当家(联盟店)"}, {"date": "2026-04-07", "type": "dinner", "name": "四方小炒·云南菜小当家(联盟店)"}, {"date": "2026-04-08", "type": "dinner", "name": "四方小炒·云南菜小当家(联盟店)"}]}, {"name_key": "四方小炒•云南菜小当家", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-04-05", "type": "lunch", "name": "四方小炒•云南菜小当家(同德店)"}, {"date": "2026-04-06", "type": "lunch", "name": "四方小炒•云南菜小当家(同德店)"}, {"date": "2026-04-07", "type": "lunch", "name": "四方小炒•云南菜小当家(同德店)"}, {"date": "2026-04-08", "type": "lunch", "name": "四方小炒•云南菜小当家(同德店)"}]}]}]`

### v3_harder_eval_000005
- request: 广州 2026-07-03->2026-07-07 days=5 transport=公共交通 hotel=民宿 prefs=['摄影', '自然风光', '城市漫步', '本地菜']
- errors: `[{"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-07-07", "type": "dinner", "name": "无", "reason": "empty_or_none"}]}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 2990, "total": 2060, "diff": 930, "requested_budget": {"available": false, "amount": 0, "scope": "unknown", "party_size": 1, "total": 0}, "per_person_day": 412.0, "budget_level": "standard", "arithmetic_consistent": false, "within_user_budget": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 4, "priced_nights": 4, "expected_min_total_hotels": 1200, "reported_total_hotels": 1200, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_harder_eval_000009
- request: 苏州 2026-04-27->2026-04-30 days=4 transport=打车 hotel=亲子酒店 prefs=['亲子', '老人友好', '博物馆', '城市公园', '特色餐厅']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "魏家凉皮", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-04-27", "type": "breakfast", "name": "魏家凉皮"}, {"date": "2026-04-28", "type": "breakfast", "name": "魏家凉皮"}, {"date": "2026-04-29", "type": "breakfast", "name": "魏家凉皮"}, {"date": "2026-04-30", "type": "breakfast", "name": "魏家凉皮"}]}, {"name_key": "老横泾面馆", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-04-27", "type": "lunch", "name": "老横泾面馆"}, {"date": "2026-04-28", "type": "lunch", "name": "老横泾面馆"}, {"date": "2026-04-29", "type": "lunch", "name": "老横泾面馆"}, {"date": "2026-04-30", "type": "lunch", "name": "老横泾面馆"}]}, {"name_key": "江南雅厨·非遗苏州菜", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-04-27", "type": "dinner", "name": "江南雅厨·非遗苏州菜"}, {"date": "2026-04-28", "type": "dinner", "name": "江南雅厨·非遗苏州菜"}, {"date": "2026-04-29", "type": "dinner", "name": "江南雅厨·非遗苏州菜"}, {"date": "2026-04-30", "type": "dinner", "name": "江南雅厨·非遗苏州菜"}]}]}]`

### v3_harder_eval_000003
- request: 西安 2025-05-04->2025-05-08 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "李志贤灌汤包子", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2025-05-04", "type": "breakfast", "name": "李志贤灌汤包子"}, {"date": "2025-05-05", "type": "breakfast", "name": "李志贤灌汤包子"}, {"date": "2025-05-06", "type": "breakfast", "name": "李志贤灌汤包子"}, {"date": "2025-05-07", "type": "breakfast", "name": "李志贤灌汤包子"}, {"date": "2025-05-08", "type": "breakfast", "name": "李志贤灌汤包子"}]}, {"name_key": "崔少野猫耳朵炒面", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2025-05-04", "type": "lunch", "name": "崔少野猫耳朵炒面(十里锦绣店)"}, {"date": "2025-05-05", "type": "lunch", "name": "崔少野猫耳朵炒面(十里锦绣店)"}, {"date": "2025-05-06", "type": "lunch", "name": "崔少野猫耳朵炒面(十里锦绣店)"}, {"date": "2025-05-07", "type": "lunch", "name": "崔少野猫耳朵炒面(十里锦绣店)"}, {"date": "2025-05-08", "type": "lunch", "name": "崔少野猫耳朵炒面(十里锦绣店)"}]}, {"name_key": "魏家凉皮", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2025-05-04", "type": "dinner", "name": "魏家凉皮(西大街店)"}, {"date": "2025-05-05", "type": "dinner", "name": "魏家凉皮(西大街店)"}, {"date": "2025-05-06", "type": "dinner", "name": "魏家凉皮(西大街店)"}, {"date": "2025-05-07", "type": "dinner", "name": "魏家凉皮(西大街店)"}, {"date": "2025-05-08", "type": "dinner", "name": "魏家凉皮(西大街店)"}]}]}]`

### v3_harder_eval_000010
- request: 西安 2026-04-20->2026-04-24 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "魏家凉皮", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-04-20", "type": "breakfast", "name": "魏家凉皮(西大街店)"}, {"date": "2026-04-21", "type": "breakfast", "name": "魏家凉皮(西大街店)"}, {"date": "2026-04-22", "type": "breakfast", "name": "魏家凉皮(西大街店)"}, {"date": "2026-04-23", "type": "breakfast", "name": "魏家凉皮(西大街店)"}, {"date": "2026-04-24", "type": "breakfast", "name": "魏家凉皮(西大街店)"}]}, {"name_key": "国人川菜", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-04-20", "type": "lunch", "name": "国人川菜(李家村店)"}, {"date": "2026-04-21", "type": "lunch", "name": "国人川菜(李家村店)"}, {"date": "2026-04-22", "type": "lunch", "name": "国人川菜(李家村店)"}, {"date": "2026-04-23", "type": "lunch", "name": "国人川菜(李家村店)"}, {"date": "2026-04-24", "type": "lunch", "name": "国人川菜(李家村店)"}]}, {"name_key": "马洪小炒泡馍馆", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-04-20", "type": "dinner", "name": "马洪小炒泡馍馆"}, {"date": "2026-04-21", "type": "dinner", "name": "马洪小炒泡馍馆"}, {"date": "2026-04-22", "type": "dinner", "name": "马洪小炒泡馍馆"}, {"date": "2026-04-23", "type": "dinner", "name": "马洪小炒泡馍馆"}, {"date": "2026-04-24", "type": "dinner", "name": "马洪小炒泡馍馆"}]}]}]`

### v3_harder_eval_000016
- request: 苏州 2026-06-03->2026-06-06 days=4 transport=自驾 hotel=亲子酒店 prefs=['亲子', '动物园', '海洋馆', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "稻山村·苏州菜", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-06-03", "type": "lunch", "name": "稻山村·苏州菜(石路店)"}, {"date": "2026-06-04", "type": "lunch", "name": "稻山村·苏州菜(石路店)"}, {"date": "2026-06-05", "type": "lunch", "name": "稻山村·苏州菜(石路店)"}, {"date": "2026-06-06", "type": "lunch", "name": "稻山村·苏州菜(曼哈顿店)"}]}]}]`

### v3_harder_eval_000013
- request: 武汉 2026-05-06->2026-05-10 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-05-10", "lunch": "刘聋子牛肉粉馆(汉阳玫瑰街店)", "dinner": "刘聋子牛肉粉馆(汉阳玫瑰街店)"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "刘聋子牛肉粉馆", "count": 6, "max_allowed": 3, "occurrences": [{"date": "2026-05-06", "type": "dinner", "name": "刘聋子牛肉粉馆(汉阳玫瑰街店)"}, {"date": "2026-05-07", "type": "dinner", "name": "刘聋子牛肉粉馆(汉阳玫瑰街店)"}, {"date": "2026-05-08", "type": "dinner", "name": "刘聋子牛肉粉馆(汉阳玫瑰街店)"}, {"date": "2026-05-09", "type": "dinner", "name": "刘聋子牛肉粉馆(汉阳玫瑰街店)"}, {"date": "2026-05-10", "type": "lunch", "name": "刘聋子牛肉粉馆(汉阳玫瑰街店)"}, {"date": "2026-05-10", "type": "dinner", "name": "刘聋子牛肉粉馆(汉阳玫瑰街店)"}]}]}]`

### v3_harder_eval_000018
- request: 天津 2026-07-03->2026-07-05 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "南楼煎饼", "count": 3, "max_allowed": 2, "occurrences": [{"date": "2026-07-03", "type": "breakfast", "name": "南楼煎饼(南楼总店)"}, {"date": "2026-07-04", "type": "breakfast", "name": "南楼煎饼(南楼总店)"}, {"date": "2026-07-05", "type": "breakfast", "name": "南楼煎饼(南楼总店)"}]}]}]`

### v3_harder_eval_000019
- request: 丽江 2026-05-08->2026-05-11 days=4 transport=打车 hotel=亲子酒店 prefs=['亲子', '老人友好', '博物馆', '城市公园', '特色餐厅']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-05-08", "lunch": "则瓦米线·云南小吃集合(花巷店)", "dinner": "则瓦米线·云南小吃集合(一中店)"}, {"date": "2026-05-09", "lunch": "则瓦米线·云南小吃集合(花巷店)", "dinner": "则瓦米线·云南小吃集合(一中店)"}, {"date": "2026-05-10", "lunch": "则瓦米线·云南小吃集合(花巷店)", "dinner": "则瓦米线·云南小吃集合(一中店)"}, {"date": "2026-05-11", "lunch": "则瓦米线·云南小吃集合(花巷店)", "dinner": "则瓦米线·云南小吃集合(一中店)"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "则瓦米线·云南小吃集合", "count": 8, "max_allowed": 3, "occurrences": [{"date": "2026-05-08", "type": "lunch", "name": "则瓦米线·云南小吃集合(花巷店)"}, {"date": "2026-05-08", "type": "dinner", "name": "则瓦米线·云南小吃集合(一中店)"}, {"date": "2026-05-09", "type": "lunch", "name": "则瓦米线·云南小吃集合(花巷店)"}, {"date": "2026-05-09", "type": "dinner", "name": "则瓦米线·云南小吃集合(一中店)"}, {"date": "2026-05-10", "type": "lunch", "name": "则瓦米线·云南小吃集合(花巷店)"}, {"date": "2026-05-10", "type": "dinner", "name": "则瓦米线·云南小吃集合(一中店)"}, {"date": "2026-05-11", "type": "lunch", "name": "则瓦米线·云南小吃集合(花巷店)"}, {"date": "2026-05-11", "type": "dinner", "name": "则瓦米线·云南小吃集合(一中店)"}]}]}]`

### v3_harder_eval_000020
- request: 杭州 2026-06-18->2026-06-22 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "柳来原味螺蛳粉", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-06-18", "type": "breakfast", "name": "柳来原味螺蛳粉(枫香路店)"}, {"date": "2026-06-19", "type": "breakfast", "name": "柳来原味螺蛳粉(枫香路店)"}, {"date": "2026-06-20", "type": "breakfast", "name": "柳来原味螺蛳粉(枫香路店)"}, {"date": "2026-06-21", "type": "breakfast", "name": "柳来原味螺蛳粉(枫香路店)"}, {"date": "2026-06-22", "type": "breakfast", "name": "柳来原味螺蛳粉(枫香路店)"}]}, {"name_key": "老姑东北人", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-06-19", "type": "lunch", "name": "老姑东北人(立涛园店)"}, {"date": "2026-06-20", "type": "lunch", "name": "老姑东北人(立涛园店)"}, {"date": "2026-06-21", "type": "lunch", "name": "老姑东北人(立涛园店)"}, {"date": "2026-06-22", "type": "lunch", "name": "老姑东北人(立涛园店)"}]}]}]`

### v3_harder_eval_000024
- request: 济南 2026-05-07->2026-05-09 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "穆得老周家牛肉烧饼", "count": 3, "max_allowed": 2, "occurrences": [{"date": "2026-05-07", "type": "breakfast", "name": "穆得老周家牛肉烧饼"}, {"date": "2026-05-08", "type": "breakfast", "name": "穆得老周家牛肉烧饼"}, {"date": "2026-05-09", "type": "breakfast", "name": "穆得老周家牛肉烧饼"}]}]}]`

### v3_harder_eval_000023
- request: 大理 2026-09-01->2026-09-05 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-09-02", "type": "dinner", "name": "随园食单(善德居店)", "reason": "unknown_food_semantics"}, {"date": "2026-09-05", "type": "lunch", "name": "随园食单(善德居店)", "reason": "unknown_food_semantics"}]}]`

### v3_harder_eval_000017
- request: 苏州 2026-05-06->2026-05-10 days=5 transport=公共交通 hotel=民宿 prefs=['小众展馆', '咖啡', '艺术', '城市漫步', '特色餐厅']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-05-08", "lunch": "魏家凉皮(邵磨针巷店)", "dinner": "魏家凉皮(邵磨针巷店)"}]}]`

### v3_harder_eval_000025
- request: 上海 2026-08-02->2026-08-06 days=5 transport=公共交通 hotel=民宿 prefs=['摄影', '自然风光', '城市漫步', '本地菜']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-08-02", "lunch": "农家菜老大(松江店)", "dinner": "农家菜老大(九亭店)"}]}]`

### v3_harder_eval_000026
- request: 扬州 2026-05-08->2026-05-11 days=4 transport=自驾 hotel=亲子酒店 prefs=['亲子', '动物园', '海洋馆', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "大毛.淮扬菜", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-05-08", "type": "lunch", "name": "大毛.淮扬菜(瘦西湖店)"}, {"date": "2026-05-09", "type": "lunch", "name": "大毛.淮扬菜(瘦西湖店)"}, {"date": "2026-05-10", "type": "lunch", "name": "大毛.淮扬菜(瘦西湖店)"}, {"date": "2026-05-11", "type": "lunch", "name": "大毛.淮扬菜(瘦西湖店)"}]}, {"name_key": "东关街美食广场", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-05-08", "type": "dinner", "name": "东关街美食广场"}, {"date": "2026-05-09", "type": "dinner", "name": "东关街美食广场"}, {"date": "2026-05-10", "type": "dinner", "name": "东关街美食广场"}, {"date": "2026-05-11", "type": "dinner", "name": "东关街美食广场"}]}]}]`

### v3_harder_eval_000028
- request: 深圳 2026-03-05->2026-03-07 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "欧记大排档•江西景德菜", "count": 3, "max_allowed": 2, "occurrences": [{"date": "2026-03-05", "type": "breakfast", "name": "欧记大排档•江西景德菜(深圳首店)"}, {"date": "2026-03-06", "type": "breakfast", "name": "欧记大排档•江西景德菜(南山保利店)"}, {"date": "2026-03-07", "type": "breakfast", "name": "欧记大排档•江西景德菜(南山保利店)"}]}]}]`

### v3_harder_eval_000022
- request: 桂林 2026-04-04->2026-04-07 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '夜市', '老字号', '城市漫步']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "碗碗都市香米粉店", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-04-04", "type": "breakfast", "name": "碗碗都市香米粉店(铁西店)"}, {"date": "2026-04-05", "type": "breakfast", "name": "碗碗都市香米粉店(铁西店)"}, {"date": "2026-04-06", "type": "breakfast", "name": "碗碗都市香米粉店(铁西店)"}, {"date": "2026-04-07", "type": "breakfast", "name": "碗碗都市香米粉店(铁西店)"}]}, {"name_key": "阿甘酒家", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-04-04", "type": "dinner", "name": "阿甘酒家(依仁店)"}, {"date": "2026-04-05", "type": "dinner", "name": "阿甘酒家(依仁店)"}, {"date": "2026-04-06", "type": "dinner", "name": "阿甘酒家(依仁店)"}, {"date": "2026-04-07", "type": "dinner", "name": "阿甘酒家(依仁店)"}]}]}, {"stage": "rule", "type": "budget_preference_mismatch", "details": {"part_sum": 3392, "total": 3492, "diff": -100, "requested_budget": {"available": false, "amount": 0, "scope": "unknown", "party_size": 2, "total": 0}, "per_person_day": 436.5, "budget_level": "limited", "arithmetic_consistent": true, "within_user_budget": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 3, "priced_nights": 3, "expected_min_total_hotels": 600, "reported_total_hotels": 800, "diff": 200, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`
