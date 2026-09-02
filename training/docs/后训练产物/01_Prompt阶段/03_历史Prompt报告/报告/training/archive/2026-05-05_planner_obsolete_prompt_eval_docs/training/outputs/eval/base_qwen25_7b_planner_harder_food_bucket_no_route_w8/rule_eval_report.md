# Rule Eval Report: base_qwen25_7b_v3_harder_food_bucket_no_route_w8

- records: 300
- generations: `training/outputs/eval/base_qwen25_7b_v3_harder_food_bucket_no_route_w8/generations.jsonl`
- records_path: `training/data/v3/eval_harder_food_bucket_no_route/records.jsonl`

## Boolean Metrics

| Metric | Pass | Total | Rate |
| --- | ---: | ---: | ---: |
| attraction_count_ok | 295 | 296 | 99.66% |
| attraction_grounding_ok | 287 | 296 | 96.96% |
| budget_arithmetic_consistent | 281 | 296 | 94.93% |
| budget_consistent | 281 | 296 | 94.93% |
| budget_level_aligned | 289 | 296 | 97.64% |
| budget_preference_aligned | 289 | 296 | 97.64% |
| budget_within_user_budget | 296 | 296 | 100.00% |
| city_ok | 296 | 296 | 100.00% |
| date_range_ok | 296 | 296 | 100.00% |
| day_dates_ok | 296 | 296 | 100.00% |
| day_index_ok | 296 | 296 | 100.00% |
| days_len_ok | 296 | 296 | 100.00% |
| dpo_soft_pass | 77 | 296 | 26.01% |
| hard_pass | 159 | 296 | 53.72% |
| hotel_budget_covers_nights | 295 | 296 | 99.66% |
| hotel_distance_placeholder_ok | 296 | 296 | 100.00% |
| hotel_grounding_ok | 295 | 296 | 99.66% |
| invalid_hotel_name_ok | 296 | 296 | 100.00% |
| json_extract_ok | 299 | 300 | 99.67% |
| legacy_hard_pass | 83 | 296 | 28.04% |
| location_object_ok | 296 | 296 | 100.00% |
| meal_complete | 295 | 296 | 99.66% |
| meal_diversity_ok | 186 | 296 | 62.84% |
| meal_grounding_ok | 180 | 296 | 60.81% |
| meal_lunch_dinner_same_day_ok | 240 | 296 | 81.08% |
| meal_repeat_limit_ok | 216 | 296 | 72.97% |
| meal_specific_ok | 296 | 296 | 100.00% |
| meal_valid_semantics_ok | 180 | 296 | 60.81% |
| middle_hotel_ok | 296 | 296 | 100.00% |
| schema_ok | 296 | 300 | 98.67% |
| sft_hard_pass | 159 | 296 | 53.72% |
| weather_dates_ok | 296 | 296 | 100.00% |
| weather_match | 294 | 296 | 99.32% |

## Numeric Metrics

```json
{
  "attraction_grounding_rate": {
    "avg": 0.9948,
    "p50": 1.0,
    "p90": 1.0
  },
  "hotel_grounding_rate": {
    "avg": 0.9966,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_diversity_unique_rate": {
    "avg": 0.7436,
    "p50": 0.8333,
    "p90": 1.0
  },
  "meal_food_pois_grounding_rate": {
    "avg": 0.9598,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_grounding_rate": {
    "avg": 0.9598,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_semantic_valid_rate": {
    "avg": 0.9614,
    "p50": 1.0,
    "p90": 1.0
  }
}
```

## Failure Types

```json
{
  "meal_invalid_name": 116,
  "meal_repeat_too_many": 80,
  "meal_same_day_lunch_dinner_repeat": 56,
  "budget_arithmetic_inconsistent": 15,
  "budget_preference_mismatch": 7,
  "schema": 3,
  "weather_mismatch": 2,
  "json_extract": 1,
  "hotel_budget_underestimated": 1
}
```

## Failure Examples

### v3_harder_eval_000004
- request: 张家界 2026-05-08->2026-05-10 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆']
- errors: `[{"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-05-08", "type": "dinner", "name": "酒店晚餐", "reason": "generic_lodging_meal"}, {"date": "2026-05-09", "type": "dinner", "name": "酒店晚餐", "reason": "generic_lodging_meal"}, {"date": "2026-05-10", "type": "dinner", "name": "酒店晚餐", "reason": "generic_lodging_meal"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "酒店晚餐", "count": 3, "max_allowed": 2, "occurrences": [{"date": "2026-05-08", "type": "dinner", "name": "酒店晚餐"}, {"date": "2026-05-09", "type": "dinner", "name": "酒店晚餐"}, {"date": "2026-05-10", "type": "dinner", "name": "酒店晚餐"}]}]}]`

### v3_harder_eval_000001
- request: 桂林 2026-09-01->2026-09-04 days=4 transport=打车 hotel=高端酒店 prefs=['高端酒店', '艺术', '特色餐厅', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-09-03", "type": "dinner", "name": "桂林山水公园", "reason": "non_food_poi_name"}, {"date": "2026-09-04", "type": "dinner", "name": "酒店晚餐", "reason": "generic_lodging_meal"}]}]`

### v3_harder_eval_000007
- request: 成都 2026-05-08->2026-05-12 days=5 transport=公共交通 hotel=民宿 prefs=['小众展馆', '咖啡', '艺术', '城市漫步', '特色餐厅']
- errors: `[{"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-05-12", "type": "dinner", "name": "无", "reason": "empty_or_none"}]}]`

### v3_harder_eval_000005
- request: 广州 2026-07-03->2026-07-07 days=5 transport=公共交通 hotel=民宿 prefs=['摄影', '自然风光', '城市漫步', '本地菜']
- errors: `[{"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-07-07", "type": "dinner", "name": "无", "reason": "empty_or_none"}]}]`

### v3_harder_eval_000003
- request: 西安 2025-05-04->2025-05-08 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2025-05-07", "lunch": "清真刚刚烤肉(小南门店)", "dinner": "清真刚刚烤肉(芙蓉街店)"}, {"date": "2025-05-08", "lunch": "清真刚刚烤肉(芙蓉街店)", "dinner": "清真刚刚烤肉(小南门店)"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "清真刚刚烤肉", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2025-05-06", "type": "lunch", "name": "清真刚刚烤肉(芙蓉街店)"}, {"date": "2025-05-07", "type": "lunch", "name": "清真刚刚烤肉(小南门店)"}, {"date": "2025-05-07", "type": "dinner", "name": "清真刚刚烤肉(芙蓉街店)"}, {"date": "2025-05-08", "type": "lunch", "name": "清真刚刚烤肉(芙蓉街店)"}, {"date": "2025-05-08", "type": "dinner", "name": "清真刚刚烤肉(小南门店)"}]}]}]`

### v3_harder_eval_000008
- request: 大理 2026-05-08->2026-05-10 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物']
- errors: `[{"stage": "json_extract", "message": "响应中未找到完整的顶层TripPlan JSON对象"}]`

### v3_harder_eval_000009
- request: 苏州 2026-04-27->2026-04-30 days=4 transport=打车 hotel=亲子酒店 prefs=['亲子', '老人友好', '博物馆', '城市公园', '特色餐厅']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "江南雅厨·非遗苏州菜", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-04-27", "type": "dinner", "name": "江南雅厨·非遗苏州菜(李公堤店)"}, {"date": "2026-04-28", "type": "dinner", "name": "江南雅厨·非遗苏州菜(李公堤店)"}, {"date": "2026-04-29", "type": "dinner", "name": "江南雅厨·非遗苏州菜(李公堤店)"}, {"date": "2026-04-30", "type": "dinner", "name": "江南雅厨·非遗苏州菜(李公堤店)"}]}]}]`

### v3_harder_eval_000010
- request: 西安 2026-04-20->2026-04-24 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-04-24", "type": "dinner", "name": "无", "reason": "empty_or_none"}]}]`

### v3_harder_eval_000012
- request: 洛阳 2025-05-04->2025-05-07 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '夜市', '老字号', '城市漫步']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "洛阳十字街小吃一条街", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2025-05-04", "type": "lunch", "name": "洛阳十字街小吃一条街"}, {"date": "2025-05-05", "type": "dinner", "name": "洛阳十字街小吃一条街"}, {"date": "2025-05-06", "type": "dinner", "name": "洛阳十字街小吃一条街"}, {"date": "2025-05-07", "type": "dinner", "name": "洛阳十字街小吃一条街"}]}]}, {"stage": "rule", "type": "budget_preference_mismatch", "details": {"part_sum": 2920, "total": 2920, "diff": 0, "requested_budget": {"available": false, "amount": 0, "scope": "unknown", "party_size": 2, "total": 0}, "per_person_day": 365.0, "budget_level": "limited", "arithmetic_consistent": true, "within_user_budget": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 3, "priced_nights": 3, "expected_min_total_hotels": 700, "reported_total_hotels": 1200, "diff": 500, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_harder_eval_000016
- request: 苏州 2026-06-03->2026-06-06 days=4 transport=自驾 hotel=亲子酒店 prefs=['亲子', '动物园', '海洋馆', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "稻山村·苏州菜", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-06-03", "type": "lunch", "name": "稻山村·苏州菜(石路店)"}, {"date": "2026-06-04", "type": "lunch", "name": "稻山村·苏州菜(石路店)"}, {"date": "2026-06-05", "type": "lunch", "name": "稻山村·苏州菜(曼哈顿店)"}, {"date": "2026-06-06", "type": "lunch", "name": "稻山村·苏州菜(石路店)"}]}]}]`

### v3_harder_eval_000013
- request: 武汉 2026-05-06->2026-05-10 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "刘聋子牛肉粉馆", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-05-06", "type": "dinner", "name": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}, {"date": "2026-05-07", "type": "dinner", "name": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}, {"date": "2026-05-08", "type": "dinner", "name": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}, {"date": "2026-05-09", "type": "dinner", "name": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}, {"date": "2026-05-10", "type": "lunch", "name": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}]}]}]`

### v3_harder_eval_000017
- request: 苏州 2026-05-06->2026-05-10 days=5 transport=公共交通 hotel=民宿 prefs=['小众展馆', '咖啡', '艺术', '城市漫步', '特色餐厅']
- errors: `[{"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-05-10", "type": "dinner", "name": "无", "reason": "empty_or_none"}]}]`

### v3_harder_eval_000018
- request: 天津 2026-07-03->2026-07-05 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物']
- errors: `[{"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-07-04", "type": "dinner", "name": "五大道地标钟", "reason": "unknown_food_semantics"}, {"date": "2026-07-05", "type": "dinner", "name": "天津之眼", "reason": "unknown_food_semantics"}]}]`

### v3_harder_eval_000019
- request: 丽江 2026-05-08->2026-05-11 days=4 transport=打车 hotel=亲子酒店 prefs=['亲子', '老人友好', '博物馆', '城市公园', '特色餐厅']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "则瓦米线·云南小吃集合", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-05-08", "type": "lunch", "name": "则瓦米线·云南小吃集合(花巷店)"}, {"date": "2026-05-09", "type": "lunch", "name": "则瓦米线·云南小吃集合(一中店)"}, {"date": "2026-05-10", "type": "lunch", "name": "则瓦米线·云南小吃集合(花巷店)"}, {"date": "2026-05-11", "type": "lunch", "name": "则瓦米线·云南小吃集合(一中店)"}]}]}]`

### v3_harder_eval_000022
- request: 桂林 2026-04-04->2026-04-07 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '夜市', '老字号', '城市漫步']
- errors: `[{"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-04-07", "type": "dinner", "name": "桂林博物馆", "reason": "hotel_or_lodging_name"}]}, {"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-04-06", "lunch": "田源米粉(三多店)", "dinner": "田源米粉(三多店)"}]}]`

### v3_harder_eval_000020
- request: 杭州 2026-06-18->2026-06-22 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-06-22", "type": "dinner", "name": "酒店晚餐", "reason": "generic_lodging_meal"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "老姑东北人", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-06-18", "type": "dinner", "name": "老姑东北人(立涛园店)"}, {"date": "2026-06-20", "type": "lunch", "name": "老姑东北人(立涛园店)"}, {"date": "2026-06-21", "type": "dinner", "name": "老姑东北人(立涛园店)"}, {"date": "2026-06-22", "type": "lunch", "name": "老姑东北人(立涛园店)"}]}]}]`

### v3_harder_eval_000023
- request: 大理 2026-09-01->2026-09-05 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-09-02", "type": "dinner", "name": "随园食单(善德居店)", "reason": "unknown_food_semantics"}, {"date": "2026-09-04", "type": "lunch", "name": "随园食单(善德居店)", "reason": "unknown_food_semantics"}, {"date": "2026-09-05", "type": "lunch", "name": "随园食单(善德居店)", "reason": "unknown_food_semantics"}, {"date": "2026-09-05", "type": "dinner", "name": "无", "reason": "empty_or_none"}]}]`

### v3_harder_eval_000024
- request: 济南 2026-05-07->2026-05-09 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆']
- errors: `[{"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-05-09", "type": "dinner", "name": "无", "reason": "empty_or_none"}]}]`

### v3_harder_eval_000028
- request: 深圳 2026-03-05->2026-03-07 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-03-05", "lunch": "欧记大排档·江西景德菜(南山保利店)", "dinner": "欧记大排档·江西景德菜(南山保利店)"}, {"date": "2026-03-06", "lunch": "蘩楼(华强北总店)", "dinner": "蘩楼(华强北总店)"}, {"date": "2026-03-07", "lunch": "南门涮肉(深圳首店)", "dinner": "南门涮肉(深圳首店)"}]}]`

### v3_harder_eval_000025
- request: 上海 2026-08-02->2026-08-06 days=5 transport=公共交通 hotel=民宿 prefs=['摄影', '自然风光', '城市漫步', '本地菜']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-08-03", "lunch": "农家菜老大(松江店)", "dinner": "农家菜老大(九亭店)"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "农家菜老大", "count": 6, "max_allowed": 3, "occurrences": [{"date": "2026-08-02", "type": "dinner", "name": "农家菜老大(松江店)"}, {"date": "2026-08-03", "type": "lunch", "name": "农家菜老大(松江店)"}, {"date": "2026-08-03", "type": "dinner", "name": "农家菜老大(九亭店)"}, {"date": "2026-08-04", "type": "dinner", "name": "农家菜老大(松江店)"}, {"date": "2026-08-05", "type": "dinner", "name": "农家菜老大(松江店)"}, {"date": "2026-08-06", "type": "dinner", "name": "农家菜老大(松江店)"}]}]}]`
