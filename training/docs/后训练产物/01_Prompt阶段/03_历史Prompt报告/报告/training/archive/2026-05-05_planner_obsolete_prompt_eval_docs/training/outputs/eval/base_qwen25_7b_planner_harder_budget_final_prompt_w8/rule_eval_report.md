# Rule Eval Report: base_qwen25_7b_v3_harder_budget_final_prompt_w8

- records: 300
- generations: `training/outputs/eval/base_qwen25_7b_v3_harder_budget_final_prompt_w8/generations.jsonl`
- records_path: `training/data/v3/eval_harder_prompt_budget_final_integer/records.jsonl`

## Boolean Metrics

| Metric | Pass | Total | Rate |
| --- | ---: | ---: | ---: |
| attraction_count_ok | 296 | 297 | 99.66% |
| attraction_grounding_ok | 291 | 297 | 97.98% |
| budget_arithmetic_consistent | 279 | 297 | 93.94% |
| budget_consistent | 279 | 297 | 93.94% |
| budget_level_aligned | 290 | 297 | 97.64% |
| budget_preference_aligned | 290 | 297 | 97.64% |
| budget_within_user_budget | 297 | 297 | 100.00% |
| city_ok | 297 | 297 | 100.00% |
| date_range_ok | 297 | 297 | 100.00% |
| day_dates_ok | 297 | 297 | 100.00% |
| day_index_ok | 297 | 297 | 100.00% |
| days_len_ok | 297 | 297 | 100.00% |
| dpo_soft_pass | 0 | 297 | 0.00% |
| hard_pass | 1 | 297 | 0.34% |
| hotel_budget_covers_nights | 297 | 297 | 100.00% |
| hotel_distance_placeholder_ok | 2 | 297 | 0.67% |
| hotel_grounding_ok | 294 | 297 | 98.99% |
| invalid_hotel_name_ok | 297 | 297 | 100.00% |
| json_extract_ok | 298 | 300 | 99.33% |
| legacy_hard_pass | 1 | 297 | 0.34% |
| location_object_ok | 297 | 297 | 100.00% |
| meal_complete | 294 | 297 | 98.99% |
| meal_diversity_ok | 121 | 297 | 40.74% |
| meal_grounding_ok | 117 | 297 | 39.39% |
| meal_lunch_dinner_same_day_ok | 280 | 297 | 94.28% |
| meal_repeat_limit_ok | 124 | 297 | 41.75% |
| meal_specific_ok | 153 | 297 | 51.52% |
| meal_valid_semantics_ok | 121 | 297 | 40.74% |
| middle_hotel_ok | 297 | 297 | 100.00% |
| schema_ok | 297 | 300 | 99.00% |
| sft_hard_pass | 1 | 297 | 0.34% |
| weather_dates_ok | 297 | 297 | 100.00% |
| weather_match | 297 | 297 | 100.00% |

## Numeric Metrics

```json
{
  "attraction_grounding_rate": {
    "avg": 0.9969,
    "p50": 1.0,
    "p90": 1.0
  },
  "hotel_grounding_rate": {
    "avg": 0.9975,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_diversity_unique_rate": {
    "avg": 0.3106,
    "p50": 0.25,
    "p90": 0.5556
  },
  "meal_food_pois_grounding_rate": {
    "avg": 0.4791,
    "p50": 0.3333,
    "p90": 1.0
  },
  "meal_grounding_rate": {
    "avg": 0.4791,
    "p50": 0.3333,
    "p90": 1.0
  },
  "meal_semantic_valid_rate": {
    "avg": 0.4996,
    "p50": 0.5333,
    "p90": 1.0
  }
}
```

## Failure Types

```json
{
  "hotel_distance_placeholder": 295,
  "meal_invalid_name": 176,
  "meal_repeat_too_many": 173,
  "meal_placeholder": 144,
  "budget_arithmetic_inconsistent": 18,
  "meal_same_day_lunch_dinner_repeat": 17,
  "budget_preference_mismatch": 7,
  "meal_grounding_miss": 4,
  "json_extract": 2,
  "schema": 1
}
```

## Failure Examples

### v3_harder_eval_000004
- request: 张家界 2026-05-07->2026-05-09 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆']
- errors: `[{"stage": "rule", "type": "hotel_distance_placeholder", "details": [{"date": "2026-05-07", "day_index": 0, "name": "梦回湘西主题客栈(张家界天门山店)", "distance": "距离景点27.4公里"}, {"date": "2026-05-08", "day_index": 1, "name": "张家界心悟山居度假民宿(武陵源景区店)", "distance": "距离景点8.3公里"}, {"date": "2026-05-09", "day_index": 2, "name": "梦回湘西主题客栈(张家界天门山店)", "distance": "距离景点27.4公里"}]}, {"stage": "rule", "type": "meal_placeholder", "details": [{"date": "2026-05-07", "type": "breakfast", "name": "早餐推荐"}, {"date": "2026-05-07", "type": "dinner", "name": "晚餐推荐"}, {"date": "2026-05-08", "type": "breakfast", "name": "早餐推荐"}, {"date": "2026-05-08", "type": "dinner", "name": "晚餐推荐"}, {"date": "2026-05-09", "type": "breakfast", "name": "早餐推荐"}, {"date": "2026-05-09", "type": "dinner", "name": "晚餐推荐"}]}, {"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-05-07", "type": "breakfast", "name": "早餐推荐", "reason": "unknown_food_semantics"}, {"date": "2026-05-07", "type": "dinner", "name": "晚餐推荐", "reason": "unknown_food_semantics"}, {"date": "2026-05-08", "type": "breakfast", "name": "早餐推荐", "reason": "unknown_food_semantics"}, {"date": "2026-05-08", "type": "dinner", "name": "晚餐推荐", "reason": "unknown_food_semantics"}, {"date": "2026-05-09", "type": "breakfast", "name": "早餐推荐", "reason": "unknown_food_semantics"}, {"date": "2026-05-09", "type": "dinner", "name": "晚餐推荐", "reason": "unknown_food_semantics"}]}]`

### v3_harder_eval_000002
- request: 杭州 2026-04-27->2026-04-30 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '夜市', '老字号', '城市漫步']
- errors: `[{"stage": "rule", "type": "hotel_distance_placeholder", "details": [{"date": "2026-04-27", "day_index": 0, "name": "绿江宾馆(建德新安江体育馆店)", "distance": "距离景点2公里"}, {"date": "2026-04-28", "day_index": 1, "name": "绿江宾馆(建德新安江体育馆店)", "distance": "距离景点2公里"}, {"date": "2026-04-29", "day_index": 2, "name": "绿江宾馆(建德新安江体育馆店)", "distance": "距离景点2公里"}]}, {"stage": "rule", "type": "meal_placeholder", "details": [{"date": "2026-04-27", "type": "breakfast", "name": "早餐推荐"}, {"date": "2026-04-28", "type": "breakfast", "name": "早餐推荐"}, {"date": "2026-04-29", "type": "breakfast", "name": "早餐推荐"}, {"date": "2026-04-30", "type": "breakfast", "name": "早餐推荐"}]}, {"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-04-27", "type": "breakfast", "name": "早餐推荐", "reason": "unknown_food_semantics"}, {"date": "2026-04-28", "type": "breakfast", "name": "早餐推荐", "reason": "unknown_food_semantics"}, {"date": "2026-04-29", "type": "breakfast", "name": "早餐推荐", "reason": "unknown_food_semantics"}, {"date": "2026-04-30", "type": "breakfast", "name": "早餐推荐", "reason": "unknown_food_semantics"}, {"date": "2026-04-30", "type": "dinner", "name": "返程", "reason": "unknown_food_semantics"}]}]`

### v3_harder_eval_000006
- request: 南京 2026-07-02->2026-07-05 days=4 transport=自驾 hotel=亲子酒店 prefs=['亲子', '动物园', '海洋馆', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "hotel_distance_placeholder", "details": [{"date": "2026-07-02", "day_index": 0, "name": "提莫玩·本电竞酒店(新街口金陵中环店)", "distance": "距离景点2.7公里"}, {"date": "2026-07-03", "day_index": 1, "name": "南京集萃金陵嘉珑酒店", "distance": "距离景点7.0公里"}, {"date": "2026-07-04", "day_index": 2, "name": "南京绿发美高梅美荟酒店", "distance": "距离景点16.4公里"}]}]`

### v3_harder_eval_000007
- request: 成都 2026-05-07->2026-05-11 days=5 transport=公共交通 hotel=民宿 prefs=['小众展馆', '咖啡', '艺术', '城市漫步', '特色餐厅']
- errors: `[{"stage": "rule", "type": "hotel_distance_placeholder", "details": [{"date": "2026-05-07", "day_index": 0, "name": "幸福之家公寓(四川农业大学温江校区店)", "distance": "距离景点41.1公里"}, {"date": "2026-05-08", "day_index": 1, "name": "成都一家驿站(华西医院上锦院区店)", "distance": "距离景点18.7公里"}, {"date": "2026-05-09", "day_index": 2, "name": "成都希望旅馆", "distance": "距离景点19.7公里"}, {"date": "2026-05-10", "day_index": 3, "name": "成都逸享公寓(成都龙泉驿航空职业技术学院店)", "distance": "距离景点26.4公里"}]}, {"stage": "rule", "type": "meal_placeholder", "details": [{"date": "2026-05-09", "type": "lunch", "name": "M Stand(成都SKP店)"}]}, {"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-05-07", "type": "breakfast", "name": "幸福之家公寓早餐", "reason": "hotel_or_lodging_name"}, {"date": "2026-05-08", "type": "breakfast", "name": "幸福之家公寓早餐", "reason": "hotel_or_lodging_name"}, {"date": "2026-05-09", "type": "breakfast", "name": "幸福之家公寓早餐", "reason": "hotel_or_lodging_name"}, {"date": "2026-05-09", "type": "lunch", "name": "M Stand(成都SKP店)", "reason": "unknown_food_semantics"}, {"date": "2026-05-10", "type": "breakfast", "name": "幸福之家公寓早餐", "reason": "hotel_or_lodging_name"}, {"date": "2026-05-11", "type": "breakfast", "name": "幸福之家公寓早餐", "reason": "hotel_or_lodging_name"}]}]`

### v3_harder_eval_000001
- request: 桂林 2026-08-31->2026-09-03 days=4 transport=打车 hotel=高端酒店 prefs=['高端酒店', '艺术', '特色餐厅', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "hotel_distance_placeholder", "details": [{"date": "2026-08-31", "day_index": 0, "name": "画馨酒店(十里画廊遇龙河店)", "distance": "距离景点8.8公里"}, {"date": "2026-09-01", "day_index": 1, "name": "画馨酒店(十里画廊遇龙河店)", "distance": "距离景点6.3公里"}, {"date": "2026-09-02", "day_index": 2, "name": "禧山度假酒店", "distance": "距离景点6.0公里"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "山野间餐厅早餐", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-08-31", "type": "breakfast", "name": "山野间餐厅早餐"}, {"date": "2026-09-01", "type": "breakfast", "name": "山野间餐厅早餐"}, {"date": "2026-09-02", "type": "breakfast", "name": "山野间餐厅早餐"}, {"date": "2026-09-03", "type": "breakfast", "name": "山野间餐厅早餐"}]}, {"name_key": "岩洞餐厅.天然岩洞特色菜午餐", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-08-31", "type": "lunch", "name": "岩洞餐厅.天然岩洞特色菜午餐"}, {"date": "2026-09-01", "type": "lunch", "name": "岩洞餐厅.天然岩洞特色菜午餐"}, {"date": "2026-09-02", "type": "lunch", "name": "岩洞餐厅.天然岩洞特色菜午餐"}, {"date": "2026-09-03", "type": "lunch", "name": "岩洞餐厅.天然岩洞特色菜午餐"}]}, {"name_key": "味道制造·桂林菜晚餐", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-08-31", "type": "dinner", "name": "味道制造·桂林菜晚餐"}, {"date": "2026-09-01", "type": "dinner", "name": "味道制造·桂林菜晚餐"}, {"date": "2026-09-02", "type": "dinner", "name": "味道制造·桂林菜晚餐"}, {"date": "2026-09-03", "type": "dinner", "name": "味道制造·桂林菜晚餐"}]}]}]`

### v3_harder_eval_000000
- request: 昆明 2026-04-03->2026-04-07 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "hotel_distance_placeholder", "details": [{"date": "2026-04-03", "day_index": 0, "name": "千旺宾馆(昆明经济管理学院海源校区店)", "distance": "距离景点12.3公里"}, {"date": "2026-04-04", "day_index": 1, "name": "昆明橙子酒店", "distance": "距离景点25.3公里"}, {"date": "2026-04-05", "day_index": 2, "name": "昆明尚和大酒店", "distance": "距离景点30.8公里"}, {"date": "2026-04-06", "day_index": 3, "name": "昆明尚和大酒店", "distance": "距离景点25.6公里"}]}, {"stage": "rule", "type": "meal_placeholder", "details": [{"date": "2026-04-03", "type": "breakfast", "name": "早餐推荐"}, {"date": "2026-04-03", "type": "lunch", "name": "午餐推荐"}, {"date": "2026-04-03", "type": "dinner", "name": "晚餐推荐"}, {"date": "2026-04-04", "type": "breakfast", "name": "早餐推荐"}, {"date": "2026-04-04", "type": "lunch", "name": "午餐推荐"}, {"date": "2026-04-04", "type": "dinner", "name": "晚餐推荐"}, {"date": "2026-04-05", "type": "breakfast", "name": "早餐推荐"}, {"date": "2026-04-05", "type": "lunch", "name": "午餐推荐"}, {"date": "2026-04-05", "type": "dinner", "name": "晚餐推荐"}, {"date": "2026-04-06", "type": "breakfast", "name": "早餐推荐"}]}, {"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-04-03", "type": "breakfast", "name": "早餐推荐", "reason": "unknown_food_semantics"}, {"date": "2026-04-03", "type": "lunch", "name": "午餐推荐", "reason": "unknown_food_semantics"}, {"date": "2026-04-03", "type": "dinner", "name": "晚餐推荐", "reason": "unknown_food_semantics"}, {"date": "2026-04-04", "type": "breakfast", "name": "早餐推荐", "reason": "unknown_food_semantics"}, {"date": "2026-04-04", "type": "lunch", "name": "午餐推荐", "reason": "unknown_food_semantics"}, {"date": "2026-04-04", "type": "dinner", "name": "晚餐推荐", "reason": "unknown_food_semantics"}, {"date": "2026-04-05", "type": "breakfast", "name": "早餐推荐", "reason": "unknown_food_semantics"}, {"date": "2026-04-05", "type": "lunch", "name": "午餐推荐", "reason": "unknown_food_semantics"}, {"date": "2026-04-05", "type": "dinner", "name": "晚餐推荐", "reason": "unknown_food_semantics"}, {"date": "2026-04-06", "type": "breakfast", "name": "早餐推荐", "reason": "unknown_food_semantics"}]}]`

### v3_harder_eval_000005
- request: 广州 2026-07-02->2026-07-06 days=5 transport=公共交通 hotel=民宿 prefs=['摄影', '自然风光', '城市漫步', '本地菜']
- errors: `[{"stage": "rule", "type": "hotel_distance_placeholder", "details": [{"date": "2026-07-02", "day_index": 0, "name": "广州好运来公寓(广州石井地铁站店)", "distance": "距离景点11.4公里"}, {"date": "2026-07-03", "day_index": 1, "name": "广州好运来公寓(广州石井地铁站店)", "distance": "距离景点15.7公里"}, {"date": "2026-07-04", "day_index": 2, "name": "广州好运来公寓(广州石井地铁站店)", "distance": "距离景点11.4公里"}, {"date": "2026-07-05", "day_index": 3, "name": "广州好运来公寓(广州石井地铁站店)", "distance": "距离景点40.4公里"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "滋粥楼·顺德菜", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-07-02", "type": "breakfast", "name": "滋粥楼·顺德菜(南村万博长隆商圈店)"}, {"date": "2026-07-03", "type": "breakfast", "name": "滋粥楼·顺德菜(南村万博长隆商圈店)"}, {"date": "2026-07-04", "type": "breakfast", "name": "滋粥楼·顺德菜(南村万博长隆商圈店)"}, {"date": "2026-07-05", "type": "breakfast", "name": "滋粥楼·顺德菜(南村万博长隆商圈店)"}, {"date": "2026-07-06", "type": "breakfast", "name": "滋粥楼·顺德菜(南村万博长隆商圈店)"}]}, {"name_key": "欧记大排档·江西景德菜", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-07-02", "type": "lunch", "name": "欧记大排档·江西景德菜(广州首店)"}, {"date": "2026-07-03", "type": "lunch", "name": "欧记大排档·江西景德菜(广州首店)"}, {"date": "2026-07-04", "type": "lunch", "name": "欧记大排档·江西景德菜(广州首店)"}, {"date": "2026-07-05", "type": "lunch", "name": "欧记大排档·江西景德菜(广州首店)"}, {"date": "2026-07-06", "type": "lunch", "name": "欧记大排档·江西景德菜(广州首店)"}]}, {"name_key": "广州仔潮汕仔特色店", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-07-02", "type": "dinner", "name": "广州仔潮汕仔特色店(广州总店)"}, {"date": "2026-07-03", "type": "dinner", "name": "广州仔潮汕仔特色店(广州总店)"}, {"date": "2026-07-04", "type": "dinner", "name": "广州仔潮汕仔特色店(广州总店)"}, {"date": "2026-07-05", "type": "dinner", "name": "广州仔潮汕仔特色店(广州总店)"}, {"date": "2026-07-06", "type": "dinner", "name": "广州仔潮汕仔特色店(广州总店)"}]}]}]`

### v3_harder_eval_000003
- request: 西安 2025-05-03->2025-05-07 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食']
- errors: `[{"stage": "rule", "type": "hotel_distance_placeholder", "details": [{"date": "2025-05-03", "day_index": 0, "name": "坤逸·精品酒店(西安阿房宫南地铁站赳赳大秦剧院店)", "distance": "距离景点44.3公里"}, {"date": "2025-05-04", "day_index": 1, "name": "坤逸·精品酒店(西安阿房宫南地铁站赳赳大秦剧院店)", "distance": "距离景点11.2公里"}, {"date": "2025-05-05", "day_index": 2, "name": "坤逸·精品酒店(西安阿房宫南地铁站赳赳大秦剧院店)", "distance": "距离景点12.6公里"}, {"date": "2025-05-06", "day_index": 3, "name": "坤逸·精品酒店(西安阿房宫南地铁站赳赳大秦剧院店)", "distance": "距离景点35.0公里"}, {"date": "2025-05-07", "day_index": 4, "name": "坤逸·精品酒店(西安阿房宫南地铁站赳赳大秦剧院店)", "distance": "距离景点35.3公里"}]}, {"stage": "rule", "type": "meal_grounding_miss", "details": [{"date": "2025-05-03", "type": "lunch", "name": "陕西特色小吃"}, {"date": "2025-05-03", "type": "dinner", "name": "西安美食"}, {"date": "2025-05-04", "type": "lunch", "name": "陕西特色小吃"}, {"date": "2025-05-04", "type": "dinner", "name": "西安美食"}, {"date": "2025-05-05", "type": "lunch", "name": "陕西特色小吃"}, {"date": "2025-05-05", "type": "dinner", "name": "西安美食"}, {"date": "2025-05-06", "type": "lunch", "name": "陕西特色小吃"}, {"date": "2025-05-06", "type": "dinner", "name": "西安美食"}, {"date": "2025-05-07", "type": "lunch", "name": "陕西特色小吃"}, {"date": "2025-05-07", "type": "dinner", "name": "西安美食"}]}]`

### v3_harder_eval_000009
- request: 苏州 2026-04-26->2026-04-29 days=4 transport=打车 hotel=亲子酒店 prefs=['亲子', '老人友好', '博物馆', '城市公园', '特色餐厅']
- errors: `[{"stage": "rule", "type": "hotel_distance_placeholder", "details": [{"date": "2026-04-26", "day_index": 0, "name": "苏州凯悦酒店", "distance": "距离景点2.7公里"}, {"date": "2026-04-27", "day_index": 1, "name": "苏州凯悦酒店", "distance": "距离景点2.7公里"}, {"date": "2026-04-28", "day_index": 2, "name": "苏州凯悦酒店", "distance": "距离景点2.7公里"}]}, {"stage": "rule", "type": "meal_placeholder", "details": [{"date": "2026-04-26", "type": "breakfast", "name": "早餐推荐"}, {"date": "2026-04-26", "type": "lunch", "name": "午餐推荐"}, {"date": "2026-04-26", "type": "dinner", "name": "晚餐推荐"}, {"date": "2026-04-27", "type": "breakfast", "name": "早餐推荐"}, {"date": "2026-04-27", "type": "lunch", "name": "午餐推荐"}, {"date": "2026-04-27", "type": "dinner", "name": "晚餐推荐"}, {"date": "2026-04-28", "type": "breakfast", "name": "早餐推荐"}, {"date": "2026-04-28", "type": "lunch", "name": "午餐推荐"}, {"date": "2026-04-28", "type": "dinner", "name": "晚餐推荐"}, {"date": "2026-04-29", "type": "breakfast", "name": "早餐推荐"}]}, {"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-04-26", "type": "breakfast", "name": "早餐推荐", "reason": "unknown_food_semantics"}, {"date": "2026-04-26", "type": "lunch", "name": "午餐推荐", "reason": "unknown_food_semantics"}, {"date": "2026-04-26", "type": "dinner", "name": "晚餐推荐", "reason": "unknown_food_semantics"}, {"date": "2026-04-27", "type": "breakfast", "name": "早餐推荐", "reason": "unknown_food_semantics"}, {"date": "2026-04-27", "type": "lunch", "name": "午餐推荐", "reason": "unknown_food_semantics"}, {"date": "2026-04-27", "type": "dinner", "name": "晚餐推荐", "reason": "unknown_food_semantics"}, {"date": "2026-04-28", "type": "breakfast", "name": "早餐推荐", "reason": "unknown_food_semantics"}, {"date": "2026-04-28", "type": "lunch", "name": "午餐推荐", "reason": "unknown_food_semantics"}, {"date": "2026-04-28", "type": "dinner", "name": "晚餐推荐", "reason": "unknown_food_semantics"}, {"date": "2026-04-29", "type": "breakfast", "name": "早餐推荐", "reason": "unknown_food_semantics"}]}]`

### v3_harder_eval_000014
- request: 成都 2026-06-02->2026-06-04 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆']
- errors: `[{"stage": "rule", "type": "hotel_distance_placeholder", "details": [{"date": "2026-06-02", "day_index": 0, "name": "栖樾酒店(成都新会展中心世豪广场店)", "distance": "距离景点10.4公里"}, {"date": "2026-06-03", "day_index": 1, "name": "大魔方前途智能酒店(成都环球中心会展店)", "distance": "距离景点8.2公里"}, {"date": "2026-06-04", "day_index": 2, "name": "成都锦上公寓(火车东站店)", "distance": "距离景点12.7公里"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "观锦餐厅", "count": 5, "max_allowed": 2, "occurrences": [{"date": "2026-06-02", "type": "breakfast", "name": "观锦餐厅(天府新谷店)早餐"}, {"date": "2026-06-02", "type": "dinner", "name": "观锦餐厅(天廊店)晚餐"}, {"date": "2026-06-03", "type": "breakfast", "name": "观锦餐厅(天廊店)早餐"}, {"date": "2026-06-04", "type": "breakfast", "name": "观锦餐厅(天府新谷店)早餐"}, {"date": "2026-06-04", "type": "dinner", "name": "观锦餐厅(天廊店)晚餐"}]}]}]`

### v3_harder_eval_000008
- request: 大理 2026-05-07->2026-05-09 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物']
- errors: `[{"stage": "rule", "type": "hotel_distance_placeholder", "details": [{"date": "2026-05-07", "day_index": 0, "name": "大理青朴酒店", "distance": "距离景点11.7公里"}, {"date": "2026-05-08", "day_index": 1, "name": "大理青朴酒店", "distance": "距离景点9.5公里"}, {"date": "2026-05-09", "day_index": 2, "name": "大理青朴酒店", "distance": "距离景点13.4公里"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "野菌皇海景餐厅早餐", "count": 3, "max_allowed": 2, "occurrences": [{"date": "2026-05-07", "type": "breakfast", "name": "野菌皇海景餐厅早餐"}, {"date": "2026-05-08", "type": "breakfast", "name": "野菌皇海景餐厅早餐"}, {"date": "2026-05-09", "type": "breakfast", "name": "野菌皇海景餐厅早餐"}]}, {"name_key": "海东茄子烧烤午餐", "count": 3, "max_allowed": 2, "occurrences": [{"date": "2026-05-07", "type": "lunch", "name": "海东茄子烧烤午餐"}, {"date": "2026-05-08", "type": "lunch", "name": "海东茄子烧烤午餐"}, {"date": "2026-05-09", "type": "lunch", "name": "海东茄子烧烤午餐"}]}, {"name_key": "阿鹏故事野生菌物料海景餐厅晚餐", "count": 3, "max_allowed": 2, "occurrences": [{"date": "2026-05-07", "type": "dinner", "name": "阿鹏故事野生菌物料海景餐厅晚餐"}, {"date": "2026-05-08", "type": "dinner", "name": "阿鹏故事野生菌物料海景餐厅晚餐"}, {"date": "2026-05-09", "type": "dinner", "name": "阿鹏故事野生菌物料海景餐厅晚餐"}]}]}]`

### v3_harder_eval_000011
- request: 福州 2026-06-17->2026-06-20 days=4 transport=打车 hotel=高端酒店 prefs=['高端酒店', '艺术', '特色餐厅', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "hotel_distance_placeholder", "details": [{"date": "2026-06-17", "day_index": 0, "name": "福州金融街万达连江中路亚朵酒店", "distance": "距离景点3.4公里"}, {"date": "2026-06-18", "day_index": 1, "name": "福州金融街万达连江中路亚朵酒店", "distance": "距离景点3.4公里"}, {"date": "2026-06-19", "day_index": 2, "name": "福州金融街万达连江中路亚朵酒店", "distance": "距离景点2.9公里"}, {"date": "2026-06-20", "day_index": 3, "name": "福州金融街万达连江中路亚朵酒店", "distance": "距离景点12.0公里"}]}, {"stage": "rule", "type": "meal_placeholder", "details": [{"date": "2026-06-17", "type": "breakfast", "name": "早餐推荐"}, {"date": "2026-06-17", "type": "lunch", "name": "午餐推荐"}, {"date": "2026-06-17", "type": "dinner", "name": "晚餐推荐"}, {"date": "2026-06-18", "type": "breakfast", "name": "早餐推荐"}, {"date": "2026-06-18", "type": "lunch", "name": "午餐推荐"}, {"date": "2026-06-18", "type": "dinner", "name": "晚餐推荐"}, {"date": "2026-06-19", "type": "breakfast", "name": "早餐推荐"}, {"date": "2026-06-19", "type": "lunch", "name": "午餐推荐"}, {"date": "2026-06-19", "type": "dinner", "name": "晚餐推荐"}, {"date": "2026-06-20", "type": "breakfast", "name": "早餐推荐"}]}, {"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-06-17", "type": "breakfast", "name": "早餐推荐", "reason": "unknown_food_semantics"}, {"date": "2026-06-17", "type": "lunch", "name": "午餐推荐", "reason": "unknown_food_semantics"}, {"date": "2026-06-17", "type": "dinner", "name": "晚餐推荐", "reason": "unknown_food_semantics"}, {"date": "2026-06-18", "type": "breakfast", "name": "早餐推荐", "reason": "unknown_food_semantics"}, {"date": "2026-06-18", "type": "lunch", "name": "午餐推荐", "reason": "unknown_food_semantics"}, {"date": "2026-06-18", "type": "dinner", "name": "晚餐推荐", "reason": "unknown_food_semantics"}, {"date": "2026-06-19", "type": "breakfast", "name": "早餐推荐", "reason": "unknown_food_semantics"}, {"date": "2026-06-19", "type": "lunch", "name": "午餐推荐", "reason": "unknown_food_semantics"}, {"date": "2026-06-19", "type": "dinner", "name": "晚餐推荐", "reason": "unknown_food_semantics"}, {"date": "2026-06-20", "type": "breakfast", "name": "早餐推荐", "reason": "unknown_food_semantics"}]}]`

### v3_harder_eval_000016
- request: 苏州 2026-06-02->2026-06-05 days=4 transport=自驾 hotel=亲子酒店 prefs=['亲子', '动物园', '海洋馆', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "hotel_distance_placeholder", "details": [{"date": "2026-06-02", "day_index": 0, "name": "苏州凯悦酒店", "distance": "距离景点2公里"}, {"date": "2026-06-03", "day_index": 1, "name": "苏州凯悦酒店", "distance": "距离景点2公里"}, {"date": "2026-06-04", "day_index": 2, "name": "苏州凯悦酒店", "distance": "距离景点2公里"}]}, {"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-06-02", "type": "dinner", "name": "酒店晚餐", "reason": "generic_lodging_meal"}, {"date": "2026-06-03", "type": "dinner", "name": "酒店晚餐", "reason": "generic_lodging_meal"}, {"date": "2026-06-04", "type": "dinner", "name": "酒店晚餐", "reason": "generic_lodging_meal"}, {"date": "2026-06-05", "type": "dinner", "name": "酒店晚餐", "reason": "generic_lodging_meal"}]}]`

### v3_harder_eval_000013
- request: 武汉 2026-05-05->2026-05-09 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食']
- errors: `[{"stage": "rule", "type": "hotel_distance_placeholder", "details": [{"date": "2026-05-05", "day_index": 0, "name": "东湖家旅游民宿(东湖风景区店)", "distance": "距离景点6.5公里"}, {"date": "2026-05-06", "day_index": 1, "name": "全季酒店(武汉汉口火车站常青路店)", "distance": "距离景点18.7公里"}, {"date": "2026-05-07", "day_index": 2, "name": "速8主题公寓(湖北大学店)", "distance": "距离景点3.6公里"}, {"date": "2026-05-08", "day_index": 3, "name": "全季酒店(武汉汉口火车站常青路店)", "distance": "距离景点4.3公里"}]}, {"stage": "rule", "type": "meal_placeholder", "details": [{"date": "2026-05-05", "type": "breakfast", "name": "早餐推荐"}, {"date": "2026-05-05", "type": "lunch", "name": "午餐推荐"}, {"date": "2026-05-05", "type": "dinner", "name": "晚餐推荐"}, {"date": "2026-05-06", "type": "breakfast", "name": "早餐推荐"}, {"date": "2026-05-06", "type": "lunch", "name": "午餐推荐"}, {"date": "2026-05-06", "type": "dinner", "name": "晚餐推荐"}, {"date": "2026-05-07", "type": "breakfast", "name": "早餐推荐"}, {"date": "2026-05-07", "type": "lunch", "name": "午餐推荐"}, {"date": "2026-05-07", "type": "dinner", "name": "晚餐推荐"}, {"date": "2026-05-08", "type": "breakfast", "name": "早餐推荐"}]}, {"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-05-05", "type": "breakfast", "name": "早餐推荐", "reason": "unknown_food_semantics"}, {"date": "2026-05-05", "type": "lunch", "name": "午餐推荐", "reason": "unknown_food_semantics"}, {"date": "2026-05-05", "type": "dinner", "name": "晚餐推荐", "reason": "unknown_food_semantics"}, {"date": "2026-05-06", "type": "breakfast", "name": "早餐推荐", "reason": "unknown_food_semantics"}, {"date": "2026-05-06", "type": "lunch", "name": "午餐推荐", "reason": "unknown_food_semantics"}, {"date": "2026-05-06", "type": "dinner", "name": "晚餐推荐", "reason": "unknown_food_semantics"}, {"date": "2026-05-07", "type": "breakfast", "name": "早餐推荐", "reason": "unknown_food_semantics"}, {"date": "2026-05-07", "type": "lunch", "name": "午餐推荐", "reason": "unknown_food_semantics"}, {"date": "2026-05-07", "type": "dinner", "name": "晚餐推荐", "reason": "unknown_food_semantics"}, {"date": "2026-05-08", "type": "breakfast", "name": "早餐推荐", "reason": "unknown_food_semantics"}]}]`

### v3_harder_eval_000010
- request: 西安 2026-04-19->2026-04-23 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "json_extract", "message": "响应中未找到完整的顶层TripPlan JSON对象"}]`

### v3_harder_eval_000015
- request: 南京 2026-04-03->2026-04-07 days=5 transport=公共交通 hotel=民宿 prefs=['摄影', '自然风光', '城市漫步', '本地菜']
- errors: `[{"stage": "rule", "type": "hotel_distance_placeholder", "details": [{"date": "2026-04-03", "day_index": 0, "name": "本色电竞酒店(南京明发外滩广场店)", "distance": "距离景点2公里"}, {"date": "2026-04-04", "day_index": 1, "name": "君驿商务公寓(南京河西儿童医院店)", "distance": "距离景点2公里"}, {"date": "2026-04-05", "day_index": 2, "name": "智逸美居之金陵美民宿(雨花台1号店)", "distance": "距离景点2公里"}, {"date": "2026-04-06", "day_index": 3, "name": "优舍酒店式公寓(南京南站店)", "distance": "距离景点2公里"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "十朝春精菜馆", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-04-03", "type": "breakfast", "name": "十朝春精菜馆"}, {"date": "2026-04-04", "type": "breakfast", "name": "十朝春精菜馆"}, {"date": "2026-04-05", "type": "breakfast", "name": "十朝春精菜馆"}, {"date": "2026-04-06", "type": "breakfast", "name": "十朝春精菜馆"}, {"date": "2026-04-07", "type": "breakfast", "name": "十朝春精菜馆"}]}, {"name_key": "金陵家宴·金陵春.南京菜", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-04-03", "type": "lunch", "name": "金陵家宴·金陵春.南京菜(夫子庙店)"}, {"date": "2026-04-04", "type": "lunch", "name": "金陵家宴·金陵春.南京菜(夫子庙店)"}, {"date": "2026-04-05", "type": "lunch", "name": "金陵家宴·金陵春.南京菜(夫子庙店)"}, {"date": "2026-04-06", "type": "lunch", "name": "金陵家宴·金陵春.南京菜(夫子庙店)"}, {"date": "2026-04-07", "type": "lunch", "name": "金陵家宴·金陵春.南京菜(夫子庙店)"}]}, {"name_key": "小厨娘淮扬菜·新街口艾尚天地店", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-04-03", "type": "dinner", "name": "小厨娘淮扬菜·新街口艾尚天地店"}, {"date": "2026-04-04", "type": "dinner", "name": "小厨娘淮扬菜·新街口艾尚天地店"}, {"date": "2026-04-05", "type": "dinner", "name": "小厨娘淮扬菜·新街口艾尚天地店"}, {"date": "2026-04-06", "type": "dinner", "name": "小厨娘淮扬菜·新街口艾尚天地店"}, {"date": "2026-04-07", "type": "dinner", "name": "小厨娘淮扬菜·新街口艾尚天地店"}]}]}]`

### v3_harder_eval_000012
- request: 洛阳 2025-05-03->2025-05-06 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '夜市', '老字号', '城市漫步']
- errors: `[{"stage": "rule", "type": "hotel_distance_placeholder", "details": [{"date": "2025-05-03", "day_index": 0, "name": "栾川一家人宾馆", "distance": "距离景点121.1公里"}, {"date": "2025-05-04", "day_index": 1, "name": "宜阳君临宾馆", "distance": "距离景点37.5公里"}, {"date": "2025-05-05", "day_index": 2, "name": "鑫升宾馆(宜阳流泉镇店)", "distance": "距离景点21.2公里"}]}, {"stage": "rule", "type": "meal_placeholder", "details": [{"date": "2025-05-03", "type": "breakfast", "name": "早餐推荐"}, {"date": "2025-05-03", "type": "lunch", "name": "午餐推荐"}, {"date": "2025-05-03", "type": "dinner", "name": "晚餐推荐"}, {"date": "2025-05-04", "type": "breakfast", "name": "早餐推荐"}, {"date": "2025-05-04", "type": "lunch", "name": "午餐推荐"}, {"date": "2025-05-04", "type": "dinner", "name": "晚餐推荐"}, {"date": "2025-05-05", "type": "breakfast", "name": "早餐推荐"}, {"date": "2025-05-05", "type": "lunch", "name": "午餐推荐"}, {"date": "2025-05-05", "type": "dinner", "name": "晚餐推荐"}, {"date": "2025-05-06", "type": "breakfast", "name": "早餐推荐"}]}, {"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2025-05-03", "type": "breakfast", "name": "早餐推荐", "reason": "unknown_food_semantics"}, {"date": "2025-05-03", "type": "lunch", "name": "午餐推荐", "reason": "unknown_food_semantics"}, {"date": "2025-05-03", "type": "dinner", "name": "晚餐推荐", "reason": "unknown_food_semantics"}, {"date": "2025-05-04", "type": "breakfast", "name": "早餐推荐", "reason": "unknown_food_semantics"}, {"date": "2025-05-04", "type": "lunch", "name": "午餐推荐", "reason": "unknown_food_semantics"}, {"date": "2025-05-04", "type": "dinner", "name": "晚餐推荐", "reason": "unknown_food_semantics"}, {"date": "2025-05-05", "type": "breakfast", "name": "早餐推荐", "reason": "unknown_food_semantics"}, {"date": "2025-05-05", "type": "lunch", "name": "午餐推荐", "reason": "unknown_food_semantics"}, {"date": "2025-05-05", "type": "dinner", "name": "晚餐推荐", "reason": "unknown_food_semantics"}, {"date": "2025-05-06", "type": "breakfast", "name": "早餐推荐", "reason": "unknown_food_semantics"}]}]`

### v3_harder_eval_000018
- request: 天津 2026-07-02->2026-07-04 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物']
- errors: `[{"stage": "rule", "type": "hotel_distance_placeholder", "details": [{"date": "2026-07-02", "day_index": 0, "name": "天津津湾广场桔子水晶酒店", "distance": "距离景点2公里"}, {"date": "2026-07-03", "day_index": 1, "name": "天津津湾广场桔子水晶酒店", "distance": "距离景点2公里"}]}, {"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-07-03", "lunch": "苏焰·地标天津菜", "dinner": "苏焰·地标天津菜"}, {"date": "2026-07-04", "lunch": "海底捞火锅", "dinner": "海底捞火锅"}]}]`

### v3_harder_eval_000019
- request: 丽江 2026-05-07->2026-05-10 days=4 transport=打车 hotel=亲子酒店 prefs=['亲子', '老人友好', '博物馆', '城市公园', '特色餐厅']
- errors: `[{"stage": "rule", "type": "hotel_distance_placeholder", "details": [{"date": "2026-05-07", "day_index": 0, "name": "静隅花间·与诗同眠", "distance": "距离景点2公里"}, {"date": "2026-05-08", "day_index": 1, "name": "静隅花间·与诗同眠", "distance": "距离景点2公里"}, {"date": "2026-05-09", "day_index": 2, "name": "静隅花间·与诗同眠", "distance": "距离景点2公里"}]}, {"stage": "rule", "type": "meal_placeholder", "details": [{"date": "2026-05-07", "type": "breakfast", "name": "早餐推荐"}, {"date": "2026-05-07", "type": "lunch", "name": "午餐推荐"}, {"date": "2026-05-07", "type": "dinner", "name": "晚餐推荐"}, {"date": "2026-05-08", "type": "breakfast", "name": "早餐推荐"}, {"date": "2026-05-08", "type": "lunch", "name": "午餐推荐"}, {"date": "2026-05-08", "type": "dinner", "name": "晚餐推荐"}, {"date": "2026-05-09", "type": "breakfast", "name": "早餐推荐"}, {"date": "2026-05-09", "type": "lunch", "name": "午餐推荐"}, {"date": "2026-05-09", "type": "dinner", "name": "晚餐推荐"}, {"date": "2026-05-10", "type": "breakfast", "name": "早餐推荐"}]}, {"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-05-07", "type": "breakfast", "name": "早餐推荐", "reason": "unknown_food_semantics"}, {"date": "2026-05-07", "type": "lunch", "name": "午餐推荐", "reason": "unknown_food_semantics"}, {"date": "2026-05-07", "type": "dinner", "name": "晚餐推荐", "reason": "unknown_food_semantics"}, {"date": "2026-05-08", "type": "breakfast", "name": "早餐推荐", "reason": "unknown_food_semantics"}, {"date": "2026-05-08", "type": "lunch", "name": "午餐推荐", "reason": "unknown_food_semantics"}, {"date": "2026-05-08", "type": "dinner", "name": "晚餐推荐", "reason": "unknown_food_semantics"}, {"date": "2026-05-09", "type": "breakfast", "name": "早餐推荐", "reason": "unknown_food_semantics"}, {"date": "2026-05-09", "type": "lunch", "name": "午餐推荐", "reason": "unknown_food_semantics"}, {"date": "2026-05-09", "type": "dinner", "name": "晚餐推荐", "reason": "unknown_food_semantics"}, {"date": "2026-05-10", "type": "breakfast", "name": "早餐推荐", "reason": "unknown_food_semantics"}]}]`

### v3_harder_eval_000024
- request: 济南 2026-05-06->2026-05-08 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆']
- errors: `[{"stage": "rule", "type": "hotel_distance_placeholder", "details": [{"date": "2026-05-06", "day_index": 0, "name": "城市便捷酒店(济南奥体中心店)", "distance": "距离景点10.9公里"}, {"date": "2026-05-07", "day_index": 1, "name": "城市便捷酒店(济南奥体中心店)", "distance": "距离景点10.9公里"}, {"date": "2026-05-08", "day_index": 2, "name": "城市便捷酒店(济南奥体中心店)", "distance": "距离景点10.9公里"}]}, {"stage": "rule", "type": "meal_placeholder", "details": [{"date": "2026-05-06", "type": "breakfast", "name": "早餐推荐"}, {"date": "2026-05-06", "type": "lunch", "name": "午餐推荐"}, {"date": "2026-05-06", "type": "dinner", "name": "晚餐推荐"}, {"date": "2026-05-07", "type": "breakfast", "name": "早餐推荐"}, {"date": "2026-05-07", "type": "lunch", "name": "午餐推荐"}, {"date": "2026-05-07", "type": "dinner", "name": "晚餐推荐"}, {"date": "2026-05-08", "type": "breakfast", "name": "早餐推荐"}, {"date": "2026-05-08", "type": "lunch", "name": "午餐推荐"}, {"date": "2026-05-08", "type": "dinner", "name": "晚餐推荐"}]}, {"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-05-06", "type": "breakfast", "name": "早餐推荐", "reason": "unknown_food_semantics"}, {"date": "2026-05-06", "type": "lunch", "name": "午餐推荐", "reason": "unknown_food_semantics"}, {"date": "2026-05-06", "type": "dinner", "name": "晚餐推荐", "reason": "unknown_food_semantics"}, {"date": "2026-05-07", "type": "breakfast", "name": "早餐推荐", "reason": "unknown_food_semantics"}, {"date": "2026-05-07", "type": "lunch", "name": "午餐推荐", "reason": "unknown_food_semantics"}, {"date": "2026-05-07", "type": "dinner", "name": "晚餐推荐", "reason": "unknown_food_semantics"}, {"date": "2026-05-08", "type": "breakfast", "name": "早餐推荐", "reason": "unknown_food_semantics"}, {"date": "2026-05-08", "type": "lunch", "name": "午餐推荐", "reason": "unknown_food_semantics"}, {"date": "2026-05-08", "type": "dinner", "name": "晚餐推荐", "reason": "unknown_food_semantics"}]}]`
