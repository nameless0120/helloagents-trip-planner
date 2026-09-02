# Rule Eval Report: base_qwen25_7b_v3_harder_food_bucket_return_dinner_prompt_w8

- records: 300
- generations: `training/outputs/eval/base_qwen25_7b_v3_harder_food_bucket_return_dinner_prompt_w8/generations.jsonl`
- records_path: `training/data/v3/eval_harder_food_bucket_return_dinner_no_route/records.jsonl`

## Boolean Metrics

| Metric | Pass | Total | Rate |
| --- | ---: | ---: | ---: |
| attraction_count_ok | 292 | 293 | 99.66% |
| attraction_grounding_ok | 281 | 293 | 95.90% |
| budget_arithmetic_consistent | 282 | 293 | 96.25% |
| budget_consistent | 282 | 293 | 96.25% |
| budget_level_aligned | 289 | 293 | 98.63% |
| budget_preference_aligned | 289 | 293 | 98.63% |
| budget_within_user_budget | 293 | 293 | 100.00% |
| city_ok | 293 | 293 | 100.00% |
| date_range_ok | 293 | 293 | 100.00% |
| day_dates_ok | 293 | 293 | 100.00% |
| day_index_ok | 293 | 293 | 100.00% |
| days_len_ok | 293 | 293 | 100.00% |
| dpo_soft_pass | 113 | 293 | 38.57% |
| hard_pass | 242 | 293 | 82.59% |
| hotel_budget_covers_nights | 293 | 293 | 100.00% |
| hotel_distance_placeholder_ok | 293 | 293 | 100.00% |
| hotel_grounding_ok | 292 | 293 | 99.66% |
| invalid_hotel_name_ok | 293 | 293 | 100.00% |
| json_extract_ok | 299 | 300 | 99.67% |
| legacy_hard_pass | 121 | 293 | 41.30% |
| location_object_ok | 293 | 293 | 100.00% |
| meal_complete | 292 | 293 | 99.66% |
| meal_diversity_ok | 148 | 293 | 50.51% |
| meal_grounding_ok | 260 | 293 | 88.74% |
| meal_lunch_dinner_same_day_ok | 208 | 293 | 70.99% |
| meal_repeat_limit_ok | 188 | 293 | 64.16% |
| meal_specific_ok | 293 | 293 | 100.00% |
| meal_valid_semantics_ok | 263 | 293 | 89.76% |
| middle_hotel_ok | 293 | 293 | 100.00% |
| schema_ok | 293 | 300 | 97.67% |
| sft_hard_pass | 242 | 293 | 82.59% |
| weather_dates_ok | 293 | 293 | 100.00% |
| weather_match | 293 | 293 | 100.00% |

## Numeric Metrics

```json
{
  "attraction_grounding_rate": {
    "avg": 0.9924,
    "p50": 1.0,
    "p90": 1.0
  },
  "hotel_grounding_rate": {
    "avg": 0.9966,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_diversity_unique_rate": {
    "avg": 0.6777,
    "p50": 0.7,
    "p90": 1.0
  },
  "meal_food_pois_grounding_rate": {
    "avg": 0.9868,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_grounding_rate": {
    "avg": 0.9868,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_semantic_valid_rate": {
    "avg": 0.9884,
    "p50": 1.0,
    "p90": 1.0
  }
}
```

## Failure Types

```json
{
  "meal_repeat_too_many": 105,
  "meal_same_day_lunch_dinner_repeat": 85,
  "meal_invalid_name": 30,
  "budget_arithmetic_inconsistent": 11,
  "schema": 6,
  "budget_preference_mismatch": 4,
  "meal_grounding_miss": 3,
  "json_extract": 1
}
```

## Failure Examples

### v3_harder_eval_000001
- request: 桂林 2026-09-01->2026-09-04 days=4 transport=打车 hotel=高端酒店 prefs=['高端酒店', '艺术', '特色餐厅', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-09-01", "lunch": "椿记烧鹅(中山店)", "dinner": "椿记烧鹅(西街店)"}]}]`

### v3_harder_eval_000009
- request: 苏州 2026-04-27->2026-04-30 days=4 transport=打车 hotel=亲子酒店 prefs=['亲子', '老人友好', '博物馆', '城市公园', '特色餐厅']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "江南雅厨·非遗苏州菜", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-04-27", "type": "dinner", "name": "江南雅厨·非遗苏州菜(李公堤店)"}, {"date": "2026-04-28", "type": "dinner", "name": "江南雅厨·非遗苏州菜(李公堤店)"}, {"date": "2026-04-29", "type": "dinner", "name": "江南雅厨·非遗苏州菜(李公堤店)"}, {"date": "2026-04-30", "type": "dinner", "name": "江南雅厨·非遗苏州菜(李公堤店)"}]}]}]`

### v3_harder_eval_000014
- request: 成都 2026-06-03->2026-06-05 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆']
- errors: `[{"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-06-05", "type": "dinner", "name": "酒店晚餐", "reason": "generic_lodging_meal"}]}]`

### v3_harder_eval_000013
- request: 武汉 2026-05-06->2026-05-10 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-05-07", "lunch": "刘聋子牛肉粉馆(汉阳玫瑰街店)", "dinner": "刘聋子牛肉粉馆(汉阳玫瑰街店)"}, {"date": "2026-05-08", "lunch": "刘聋子牛肉粉馆(汉阳玫瑰街店)", "dinner": "刘聋子牛肉粉馆(汉阳玫瑰街店)"}, {"date": "2026-05-09", "lunch": "刘聋子牛肉粉馆(汉阳玫瑰街店)", "dinner": "刘聋子牛肉粉馆(汉阳玫瑰街店)"}, {"date": "2026-05-10", "lunch": "刘聋子牛肉粉馆(汉阳玫瑰街店)", "dinner": "刘聋子牛肉粉馆(汉阳玫瑰街店)"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "刘聋子牛肉粉馆", "count": 9, "max_allowed": 3, "occurrences": [{"date": "2026-05-06", "type": "dinner", "name": "刘聋子牛肉粉馆(汉阳玫瑰街店)"}, {"date": "2026-05-07", "type": "lunch", "name": "刘聋子牛肉粉馆(汉阳玫瑰街店)"}, {"date": "2026-05-07", "type": "dinner", "name": "刘聋子牛肉粉馆(汉阳玫瑰街店)"}, {"date": "2026-05-08", "type": "lunch", "name": "刘聋子牛肉粉馆(汉阳玫瑰街店)"}, {"date": "2026-05-08", "type": "dinner", "name": "刘聋子牛肉粉馆(汉阳玫瑰街店)"}, {"date": "2026-05-09", "type": "lunch", "name": "刘聋子牛肉粉馆(汉阳玫瑰街店)"}, {"date": "2026-05-09", "type": "dinner", "name": "刘聋子牛肉粉馆(汉阳玫瑰街店)"}, {"date": "2026-05-10", "type": "lunch", "name": "刘聋子牛肉粉馆(汉阳玫瑰街店)"}, {"date": "2026-05-10", "type": "dinner", "name": "刘聋子牛肉粉馆(汉阳玫瑰街店)"}]}]}]`

### v3_harder_eval_000012
- request: 洛阳 2025-05-04->2025-05-07 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '夜市', '老字号', '城市漫步']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2025-05-04", "lunch": "洛阳十字街小吃一条街", "dinner": "洛阳十字街小吃一条街"}, {"date": "2025-05-05", "lunch": "洛阳宴.洛阳菜(南昌路店)", "dinner": "洛阳宴.洛阳菜(南昌路店)"}, {"date": "2025-05-06", "lunch": "光头东烙馍村·水席洛阳菜(火车站店)", "dinner": "光头东烙馍村·水席洛阳菜(火车站店)"}, {"date": "2025-05-07", "lunch": "必胜客(正大广场店)", "dinner": "必胜客(正大广场店)"}]}]`

### v3_harder_eval_000018
- request: 天津 2026-07-03->2026-07-05 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-07-05", "lunch": "魏斯理汉堡(天津乐宾百货店)", "dinner": "魏斯理汉堡(天津乐宾百货店)"}]}]`

### v3_harder_eval_000019
- request: 丽江 2026-05-08->2026-05-11 days=4 transport=打车 hotel=亲子酒店 prefs=['亲子', '老人友好', '博物馆', '城市公园', '特色餐厅']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-05-09", "lunch": "则瓦米线·云南小吃集合(花巷店)", "dinner": "则瓦米线·云南小吃集合(一中店)"}, {"date": "2026-05-10", "lunch": "则瓦米线·云南小吃集合(花巷店)", "dinner": "则瓦米线·云南小吃集合(一中店)"}, {"date": "2026-05-11", "lunch": "则瓦米线·云南小吃集合(花巷店)", "dinner": "则瓦米线·云南小吃集合(一中店)"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "则瓦米线·云南小吃集合", "count": 7, "max_allowed": 3, "occurrences": [{"date": "2026-05-08", "type": "dinner", "name": "则瓦米线·云南小吃集合(花巷店)"}, {"date": "2026-05-09", "type": "lunch", "name": "则瓦米线·云南小吃集合(花巷店)"}, {"date": "2026-05-09", "type": "dinner", "name": "则瓦米线·云南小吃集合(一中店)"}, {"date": "2026-05-10", "type": "lunch", "name": "则瓦米线·云南小吃集合(花巷店)"}, {"date": "2026-05-10", "type": "dinner", "name": "则瓦米线·云南小吃集合(一中店)"}, {"date": "2026-05-11", "type": "lunch", "name": "则瓦米线·云南小吃集合(花巷店)"}, {"date": "2026-05-11", "type": "dinner", "name": "则瓦米线·云南小吃集合(一中店)"}]}]}]`

### v3_harder_eval_000020
- request: 杭州 2026-06-18->2026-06-22 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-06-22", "lunch": "老姑东北人(立涛园店)", "dinner": "老姑东北人(立涛园店)"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "老姑东北人", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-06-19", "type": "lunch", "name": "老姑东北人(立涛园店)"}, {"date": "2026-06-21", "type": "lunch", "name": "老姑东北人(立涛园店)"}, {"date": "2026-06-22", "type": "lunch", "name": "老姑东北人(立涛园店)"}, {"date": "2026-06-22", "type": "dinner", "name": "老姑东北人(立涛园店)"}]}]}]`

### v3_harder_eval_000023
- request: 大理 2026-09-01->2026-09-05 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "挖色菜香园", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-09-01", "type": "lunch", "name": "挖色菜香园"}, {"date": "2026-09-02", "type": "lunch", "name": "挖色菜香园"}, {"date": "2026-09-03", "type": "lunch", "name": "挖色菜香园"}, {"date": "2026-09-04", "type": "lunch", "name": "挖色菜香园"}, {"date": "2026-09-05", "type": "lunch", "name": "挖色菜香园"}]}, {"name_key": "岛七白族人家火烧猪私房菜", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-09-01", "type": "dinner", "name": "岛七白族人家火烧猪私房菜"}, {"date": "2026-09-02", "type": "dinner", "name": "岛七白族人家火烧猪私房菜"}, {"date": "2026-09-03", "type": "dinner", "name": "岛七白族人家火烧猪私房菜"}, {"date": "2026-09-04", "type": "dinner", "name": "岛七白族人家火烧猪私房菜"}, {"date": "2026-09-05", "type": "dinner", "name": "岛七白族人家火烧猪私房菜"}]}]}]`

### v3_harder_eval_000026
- request: 扬州 2026-05-08->2026-05-11 days=4 transport=自驾 hotel=亲子酒店 prefs=['亲子', '动物园', '海洋馆', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "大毛.淮扬菜", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-05-08", "type": "lunch", "name": "大毛.淮扬菜(瘦西湖店)"}, {"date": "2026-05-09", "type": "lunch", "name": "大毛.淮扬菜(瘦西湖店)"}, {"date": "2026-05-10", "type": "lunch", "name": "大毛.淮扬菜(瘦西湖店)"}, {"date": "2026-05-11", "type": "lunch", "name": "大毛.淮扬菜(瘦西湖店)"}]}, {"name_key": "东关街美食广场", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-05-08", "type": "dinner", "name": "东关街美食广场"}, {"date": "2026-05-09", "type": "dinner", "name": "东关街美食广场"}, {"date": "2026-05-10", "type": "dinner", "name": "东关街美食广场"}, {"date": "2026-05-11", "type": "dinner", "name": "东关街美食广场"}]}]}]`

### v3_harder_eval_000025
- request: 上海 2026-08-02->2026-08-06 days=5 transport=公共交通 hotel=民宿 prefs=['摄影', '自然风光', '城市漫步', '本地菜']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-08-06", "lunch": "农家菜老大(松江店)", "dinner": "农家菜老大(松江店)"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "农家菜老大", "count": 6, "max_allowed": 3, "occurrences": [{"date": "2026-08-02", "type": "dinner", "name": "农家菜老大(松江店)"}, {"date": "2026-08-03", "type": "dinner", "name": "农家菜老大(松江店)"}, {"date": "2026-08-04", "type": "dinner", "name": "农家菜老大(松江店)"}, {"date": "2026-08-05", "type": "dinner", "name": "农家菜老大(松江店)"}, {"date": "2026-08-06", "type": "lunch", "name": "农家菜老大(松江店)"}, {"date": "2026-08-06", "type": "dinner", "name": "农家菜老大(松江店)"}]}]}]`

### v3_harder_eval_000028
- request: 深圳 2026-03-05->2026-03-07 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-03-05", "lunch": "欧记大排档·江西景德菜(南山保利店)", "dinner": "欧记大排档·江西景德菜(南山保利店)"}, {"date": "2026-03-06", "lunch": "南门涮肉(深圳首店)", "dinner": "南门涮肉(深圳首店)"}, {"date": "2026-03-07", "lunch": "螺一一螺蛳粉", "dinner": "螺一一螺蛳粉"}]}]`

### v3_harder_eval_000022
- request: 桂林 2026-04-04->2026-04-07 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '夜市', '老字号', '城市漫步']
- errors: `[{"stage": "rule", "type": "meal_grounding_miss", "details": [{"date": "2026-04-04", "type": "dinner", "name": "民俗街夜市"}]}]`

### v3_harder_eval_000030
- request: 三亚 2026-05-08->2026-05-12 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "椰小鸡·椰子鸡", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-05-08", "type": "dinner", "name": "椰小鸡·椰子鸡(海棠68环球美食店)"}, {"date": "2026-05-09", "type": "dinner", "name": "椰小鸡·椰子鸡(三亚湾店)"}, {"date": "2026-05-10", "type": "dinner", "name": "椰小鸡·椰子鸡(海棠68环球美食店)"}, {"date": "2026-05-11", "type": "dinner", "name": "椰小鸡·椰子鸡(海棠68环球美食店)"}, {"date": "2026-05-12", "type": "dinner", "name": "椰小鸡·椰子鸡(海棠68环球美食店)"}]}, {"name_key": "创味·民间海南菜", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-05-09", "type": "lunch", "name": "创味·民间海南菜(南山店)"}, {"date": "2026-05-10", "type": "lunch", "name": "创味·民间海南菜(南山店)"}, {"date": "2026-05-11", "type": "lunch", "name": "创味·民间海南菜(南山店)"}, {"date": "2026-05-12", "type": "lunch", "name": "创味·民间海南菜(南山店)"}]}]}]`

### v3_harder_eval_000034
- request: 武汉 2026-06-03->2026-06-05 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-06-03", "lunch": "刘聋子牛肉粉馆(汉阳龙兴东街店)", "dinner": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}, {"date": "2026-06-05", "lunch": "刘聋子牛肉粉馆(汉阳龙兴东街店)", "dinner": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "刘聋子牛肉粉馆", "count": 5, "max_allowed": 2, "occurrences": [{"date": "2026-06-03", "type": "lunch", "name": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}, {"date": "2026-06-03", "type": "dinner", "name": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}, {"date": "2026-06-04", "type": "dinner", "name": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}, {"date": "2026-06-05", "type": "lunch", "name": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}, {"date": "2026-06-05", "type": "dinner", "name": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}]}]}]`

### v3_harder_eval_000035
- request: 深圳 2026-09-01->2026-09-05 days=5 transport=公共交通 hotel=民宿 prefs=['摄影', '自然风光', '城市漫步', '本地菜']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "欧记大排档·江西景德菜", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-09-01", "type": "lunch", "name": "欧记大排档·江西景德菜(南山保利店)"}, {"date": "2026-09-02", "type": "lunch", "name": "欧记大排档·江西景德菜(南山保利店)"}, {"date": "2026-09-03", "type": "lunch", "name": "欧记大排档·江西景德菜(南山保利店)"}, {"date": "2026-09-04", "type": "lunch", "name": "欧记大排档·江西景德菜(南山保利店)"}, {"date": "2026-09-05", "type": "lunch", "name": "欧记大排档·江西景德菜(南山保利店)"}]}, {"name_key": "蘩楼", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-09-01", "type": "dinner", "name": "蘩楼(华强北总店)"}, {"date": "2026-09-02", "type": "dinner", "name": "蘩楼(华强北总店)"}, {"date": "2026-09-03", "type": "dinner", "name": "蘩楼(华强北总店)"}, {"date": "2026-09-04", "type": "dinner", "name": "蘩楼(华强北总店)"}, {"date": "2026-09-05", "type": "dinner", "name": "蘩楼(华强北总店)"}]}]}]`

### v3_harder_eval_000033
- request: 苏州 2026-05-08->2026-05-12 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "稻山村·苏州菜", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-05-08", "type": "lunch", "name": "稻山村·苏州菜(石路店)"}, {"date": "2026-05-09", "type": "lunch", "name": "稻山村·苏州菜(石路店)"}, {"date": "2026-05-10", "type": "lunch", "name": "稻山村·苏州菜(石路店)"}, {"date": "2026-05-11", "type": "lunch", "name": "稻山村·苏州菜(石路店)"}, {"date": "2026-05-12", "type": "lunch", "name": "稻山村·苏州菜(石路店)"}]}, {"name_key": "吴记小园楼", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-05-08", "type": "dinner", "name": "吴记小园楼(白塔西路总店)"}, {"date": "2026-05-09", "type": "dinner", "name": "吴记小园楼(白塔西路总店)"}, {"date": "2026-05-10", "type": "dinner", "name": "吴记小园楼(白塔西路总店)"}, {"date": "2026-05-11", "type": "dinner", "name": "吴记小园楼(白塔西路总店)"}, {"date": "2026-05-12", "type": "dinner", "name": "吴记小园楼(白塔西路总店)"}]}]}]`

### v3_harder_eval_000038
- request: 厦门 2026-05-07->2026-05-09 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物']
- errors: `[{"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-05-09", "type": "dinner", "name": "酒店晚餐", "reason": "generic_lodging_meal"}]}]`

### v3_harder_eval_000036
- request: 长沙 2026-06-03->2026-06-06 days=4 transport=自驾 hotel=亲子酒店 prefs=['亲子', '动物园', '海洋馆', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-06-03", "type": "dinner", "name": "酒店晚餐", "reason": "generic_lodging_meal"}, {"date": "2026-06-04", "type": "dinner", "name": "长沙海底世界", "reason": "unknown_food_semantics"}, {"date": "2026-06-06", "type": "dinner", "name": "酒店晚餐", "reason": "generic_lodging_meal"}]}]`

### v3_harder_eval_000037
- request: 贵阳 2026-01-04->2026-01-08 days=5 transport=公共交通 hotel=民宿 prefs=['小众展馆', '咖啡', '艺术', '城市漫步', '特色餐厅']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-01-05", "lunch": "赛维利亚中西餐厅(金阳店)", "dinner": "赛维利亚中西餐厅(金阳店)"}, {"date": "2026-01-06", "lunch": "金顶山小耳朵清水烫(温馨小院店)", "dinner": "金顶山小耳朵清水烫(温馨小院店)"}, {"date": "2026-01-07", "lunch": "佳乡烟火 · 织金土烙锅(小十字店)", "dinner": "佳乡烟火 · 织金土烙锅(小十字店)"}, {"date": "2026-01-08", "lunch": "黔大叔大牌档(甲秀楼店)", "dinner": "黔大叔大牌档(甲秀楼店)"}]}]`
