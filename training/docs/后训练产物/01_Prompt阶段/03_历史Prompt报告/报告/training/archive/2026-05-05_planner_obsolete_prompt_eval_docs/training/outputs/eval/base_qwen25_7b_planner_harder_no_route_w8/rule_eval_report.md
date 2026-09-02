# Rule Eval Report: base_qwen25_7b_v3_harder_no_route_w8

- records: 300
- generations: `training/outputs/eval/base_qwen25_7b_v3_harder_no_route_w8/generations.jsonl`
- records_path: `training/data/v3/eval_harder_prompt_budget_final_no_route/records.jsonl`

## Boolean Metrics

| Metric | Pass | Total | Rate |
| --- | ---: | ---: | ---: |
| attraction_count_ok | 298 | 298 | 100.00% |
| attraction_grounding_ok | 288 | 298 | 96.64% |
| budget_arithmetic_consistent | 288 | 298 | 96.64% |
| budget_consistent | 288 | 298 | 96.64% |
| budget_level_aligned | 287 | 298 | 96.31% |
| budget_preference_aligned | 287 | 298 | 96.31% |
| budget_within_user_budget | 298 | 298 | 100.00% |
| city_ok | 298 | 298 | 100.00% |
| date_range_ok | 298 | 298 | 100.00% |
| day_dates_ok | 298 | 298 | 100.00% |
| day_index_ok | 298 | 298 | 100.00% |
| days_len_ok | 298 | 298 | 100.00% |
| dpo_soft_pass | 0 | 298 | 0.00% |
| hard_pass | 2 | 298 | 0.67% |
| hotel_budget_covers_nights | 296 | 298 | 99.33% |
| hotel_distance_placeholder_ok | 10 | 298 | 3.36% |
| hotel_grounding_ok | 297 | 298 | 99.66% |
| invalid_hotel_name_ok | 298 | 298 | 100.00% |
| json_extract_ok | 298 | 300 | 99.33% |
| legacy_hard_pass | 1 | 298 | 0.34% |
| location_object_ok | 298 | 298 | 100.00% |
| meal_complete | 297 | 298 | 99.66% |
| meal_diversity_ok | 121 | 298 | 40.60% |
| meal_grounding_ok | 105 | 298 | 35.23% |
| meal_lunch_dinner_same_day_ok | 292 | 298 | 97.99% |
| meal_repeat_limit_ok | 121 | 298 | 40.60% |
| meal_specific_ok | 151 | 298 | 50.67% |
| meal_valid_semantics_ok | 114 | 298 | 38.26% |
| middle_hotel_ok | 298 | 298 | 100.00% |
| schema_ok | 298 | 300 | 99.33% |
| sft_hard_pass | 2 | 298 | 0.67% |
| weather_dates_ok | 298 | 298 | 100.00% |
| weather_match | 297 | 298 | 99.66% |

## Numeric Metrics

```json
{
  "attraction_grounding_rate": {
    "avg": 0.9936,
    "p50": 1.0,
    "p90": 1.0
  },
  "hotel_grounding_rate": {
    "avg": 0.9966,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_diversity_unique_rate": {
    "avg": 0.3243,
    "p50": 0.25,
    "p90": 0.6
  },
  "meal_food_pois_grounding_rate": {
    "avg": 0.4668,
    "p50": 0.3333,
    "p90": 1.0
  },
  "meal_grounding_rate": {
    "avg": 0.4668,
    "p50": 0.3333,
    "p90": 1.0
  },
  "meal_semantic_valid_rate": {
    "avg": 0.4947,
    "p50": 0.3333,
    "p90": 1.0
  }
}
```

## Failure Types

```json
{
  "hotel_distance_placeholder": 288,
  "meal_invalid_name": 184,
  "meal_repeat_too_many": 177,
  "meal_placeholder": 147,
  "budget_preference_mismatch": 11,
  "budget_arithmetic_inconsistent": 10,
  "meal_grounding_miss": 9,
  "meal_same_day_lunch_dinner_repeat": 6,
  "json_extract": 2,
  "hotel_budget_underestimated": 2,
  "weather_mismatch": 1
}
```

## Failure Examples

### v3_harder_eval_000004
- request: 张家界 2026-05-07->2026-05-09 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆']
- errors: `[{"stage": "rule", "type": "hotel_distance_placeholder", "details": [{"date": "2026-05-07", "day_index": 0, "name": "梦回湘西主题客栈(张家界天门山店)", "distance": "距离景点2公里"}, {"date": "2026-05-08", "day_index": 1, "name": "张家界心悟山居度假民宿(武陵源景区店)", "distance": "距离景点2公里"}]}, {"stage": "rule", "type": "meal_placeholder", "details": [{"date": "2026-05-07", "type": "breakfast", "name": "早餐推荐"}, {"date": "2026-05-07", "type": "dinner", "name": "晚餐推荐"}, {"date": "2026-05-08", "type": "breakfast", "name": "早餐推荐"}, {"date": "2026-05-08", "type": "dinner", "name": "晚餐推荐"}, {"date": "2026-05-09", "type": "breakfast", "name": "早餐推荐"}, {"date": "2026-05-09", "type": "dinner", "name": "晚餐推荐"}]}, {"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-05-07", "type": "breakfast", "name": "早餐推荐", "reason": "unknown_food_semantics"}, {"date": "2026-05-07", "type": "dinner", "name": "晚餐推荐", "reason": "unknown_food_semantics"}, {"date": "2026-05-08", "type": "breakfast", "name": "早餐推荐", "reason": "unknown_food_semantics"}, {"date": "2026-05-08", "type": "dinner", "name": "晚餐推荐", "reason": "unknown_food_semantics"}, {"date": "2026-05-09", "type": "breakfast", "name": "早餐推荐", "reason": "unknown_food_semantics"}, {"date": "2026-05-09", "type": "dinner", "name": "晚餐推荐", "reason": "unknown_food_semantics"}]}]`

### v3_harder_eval_000002
- request: 杭州 2026-04-27->2026-04-30 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '夜市', '老字号', '城市漫步']
- errors: `[{"stage": "rule", "type": "hotel_distance_placeholder", "details": [{"date": "2026-04-27", "day_index": 0, "name": "绿江宾馆(建德新安江体育馆店)", "distance": "距离景点2公里"}, {"date": "2026-04-28", "day_index": 1, "name": "绿江宾馆(建德新安江体育馆店)", "distance": "距离景点2公里"}, {"date": "2026-04-29", "day_index": 2, "name": "绿江宾馆(建德新安江体育馆店)", "distance": "距离景点2公里"}]}, {"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-04-30", "type": "dinner", "name": "无", "reason": "empty_or_none"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "知味观", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-04-27", "type": "breakfast", "name": "知味观(湖滨总店)早餐"}, {"date": "2026-04-28", "type": "breakfast", "name": "知味观(湖滨总店)早餐"}, {"date": "2026-04-29", "type": "breakfast", "name": "知味观(湖滨总店)早餐"}, {"date": "2026-04-30", "type": "breakfast", "name": "知味观(湖滨总店)早餐"}]}, {"name_key": "老秦凉都黄牛肉馆", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-04-27", "type": "lunch", "name": "老秦凉都黄牛肉馆(滨江总店)午餐"}, {"date": "2026-04-28", "type": "lunch", "name": "老秦凉都黄牛肉馆(滨江总店)午餐"}, {"date": "2026-04-29", "type": "lunch", "name": "老秦凉都黄牛肉馆(滨江总店)午餐"}, {"date": "2026-04-30", "type": "lunch", "name": "老秦凉都黄牛肉馆(滨江总店)午餐"}]}]}]`

### v3_harder_eval_000006
- request: 南京 2026-07-02->2026-07-05 days=4 transport=自驾 hotel=亲子酒店 prefs=['亲子', '动物园', '海洋馆', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "hotel_distance_placeholder", "details": [{"date": "2026-07-02", "day_index": 0, "name": "提莫玩·本电竞酒店(新街口金陵中环店)", "distance": "距离景点2公里"}, {"date": "2026-07-03", "day_index": 1, "name": "南京集萃金陵嘉珑酒店", "distance": "距离景点2公里"}, {"date": "2026-07-04", "day_index": 2, "name": "南京绿发美高梅美荟酒店", "distance": "距离景点2公里"}]}]`

### v3_harder_eval_000007
- request: 成都 2026-05-07->2026-05-11 days=5 transport=公共交通 hotel=民宿 prefs=['小众展馆', '咖啡', '艺术', '城市漫步', '特色餐厅']
- errors: `[{"stage": "rule", "type": "hotel_distance_placeholder", "details": [{"date": "2026-05-07", "day_index": 0, "name": "幸福之家公寓(四川农业大学温江校区店)", "distance": "距离景点2公里"}, {"date": "2026-05-08", "day_index": 1, "name": "成都希望旅馆", "distance": "距离景点2公里"}, {"date": "2026-05-09", "day_index": 2, "name": "成都青柚共享酒店(文殊院骡马市地铁站店)", "distance": "距离景点2公里"}, {"date": "2026-05-10", "day_index": 3, "name": "成都逸享公寓(成都龙泉驿航空职业技术学院店)", "distance": "距离景点2公里"}]}, {"stage": "rule", "type": "meal_placeholder", "details": [{"date": "2026-05-07", "type": "breakfast", "name": "早餐推荐"}, {"date": "2026-05-07", "type": "lunch", "name": "午餐推荐"}, {"date": "2026-05-07", "type": "dinner", "name": "晚餐推荐"}, {"date": "2026-05-08", "type": "breakfast", "name": "早餐推荐"}, {"date": "2026-05-08", "type": "lunch", "name": "午餐推荐"}, {"date": "2026-05-08", "type": "dinner", "name": "晚餐推荐"}, {"date": "2026-05-09", "type": "breakfast", "name": "早餐推荐"}, {"date": "2026-05-09", "type": "lunch", "name": "午餐推荐"}, {"date": "2026-05-09", "type": "dinner", "name": "晚餐推荐"}, {"date": "2026-05-10", "type": "breakfast", "name": "早餐推荐"}]}, {"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-05-07", "type": "breakfast", "name": "早餐推荐", "reason": "unknown_food_semantics"}, {"date": "2026-05-07", "type": "lunch", "name": "午餐推荐", "reason": "unknown_food_semantics"}, {"date": "2026-05-07", "type": "dinner", "name": "晚餐推荐", "reason": "unknown_food_semantics"}, {"date": "2026-05-08", "type": "breakfast", "name": "早餐推荐", "reason": "unknown_food_semantics"}, {"date": "2026-05-08", "type": "lunch", "name": "午餐推荐", "reason": "unknown_food_semantics"}, {"date": "2026-05-08", "type": "dinner", "name": "晚餐推荐", "reason": "unknown_food_semantics"}, {"date": "2026-05-09", "type": "breakfast", "name": "早餐推荐", "reason": "unknown_food_semantics"}, {"date": "2026-05-09", "type": "lunch", "name": "午餐推荐", "reason": "unknown_food_semantics"}, {"date": "2026-05-09", "type": "dinner", "name": "晚餐推荐", "reason": "unknown_food_semantics"}, {"date": "2026-05-10", "type": "breakfast", "name": "早餐推荐", "reason": "unknown_food_semantics"}]}]`

### v3_harder_eval_000001
- request: 桂林 2026-08-31->2026-09-03 days=4 transport=打车 hotel=高端酒店 prefs=['高端酒店', '艺术', '特色餐厅', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "hotel_distance_placeholder", "details": [{"date": "2026-08-31", "day_index": 0, "name": "画馨酒店(十里画廊遇龙河店)", "distance": "距离景点2公里"}, {"date": "2026-09-01", "day_index": 1, "name": "画馨酒店(十里画廊遇龙河店)", "distance": "距离景点2公里"}, {"date": "2026-09-02", "day_index": 2, "name": "画馨酒店(十里画廊遇龙河店)", "distance": "距离景点2公里"}, {"date": "2026-09-03", "day_index": 3, "name": "画馨酒店(十里画廊遇龙河店)", "distance": "距离景点2公里"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "山野间餐厅早餐", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-08-31", "type": "breakfast", "name": "山野间餐厅早餐"}, {"date": "2026-09-01", "type": "breakfast", "name": "山野间餐厅早餐"}, {"date": "2026-09-02", "type": "breakfast", "name": "山野间餐厅早餐"}, {"date": "2026-09-03", "type": "breakfast", "name": "山野间餐厅早餐"}]}, {"name_key": "岩洞餐厅.天然岩洞特色菜午餐", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-08-31", "type": "lunch", "name": "岩洞餐厅.天然岩洞特色菜午餐"}, {"date": "2026-09-01", "type": "lunch", "name": "岩洞餐厅.天然岩洞特色菜午餐"}, {"date": "2026-09-02", "type": "lunch", "name": "岩洞餐厅.天然岩洞特色菜午餐"}, {"date": "2026-09-03", "type": "lunch", "name": "岩洞餐厅.天然岩洞特色菜午餐"}]}, {"name_key": "味道制造·桂林菜晚餐", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-08-31", "type": "dinner", "name": "味道制造·桂林菜晚餐"}, {"date": "2026-09-01", "type": "dinner", "name": "味道制造·桂林菜晚餐"}, {"date": "2026-09-02", "type": "dinner", "name": "味道制造·桂林菜晚餐"}, {"date": "2026-09-03", "type": "dinner", "name": "味道制造·桂林菜晚餐"}]}]}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 4616, "total": 6376, "diff": -1760, "requested_budget": {"available": false, "amount": 0, "scope": "unknown", "party_size": 2, "total": 0}, "per_person_day": 797.0, "budget_level": "premium", "arithmetic_consistent": false, "within_user_budget": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 3, "priced_nights": 3, "expected_min_total_hotels": 2250, "reported_total_hotels": 2700, "diff": 450, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_harder_eval_000000
- request: 昆明 2026-04-03->2026-04-07 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "hotel_distance_placeholder", "details": [{"date": "2026-04-03", "day_index": 0, "name": "千旺宾馆(昆明经济管理学院海源校区店)", "distance": "距离景点2公里"}, {"date": "2026-04-04", "day_index": 1, "name": "昆明橙子酒店", "distance": "距离景点2公里"}, {"date": "2026-04-05", "day_index": 2, "name": "昆明尚和大酒店", "distance": "距离景点2公里"}, {"date": "2026-04-06", "day_index": 3, "name": "明珠宾馆(永定街)", "distance": "距离景点2公里"}]}, {"stage": "rule", "type": "meal_placeholder", "details": [{"date": "2026-04-03", "type": "breakfast", "name": "早餐推荐"}, {"date": "2026-04-03", "type": "lunch", "name": "午餐推荐"}, {"date": "2026-04-03", "type": "dinner", "name": "晚餐推荐"}, {"date": "2026-04-04", "type": "breakfast", "name": "早餐推荐"}, {"date": "2026-04-04", "type": "lunch", "name": "午餐推荐"}, {"date": "2026-04-04", "type": "dinner", "name": "晚餐推荐"}, {"date": "2026-04-05", "type": "breakfast", "name": "早餐推荐"}, {"date": "2026-04-05", "type": "lunch", "name": "午餐推荐"}, {"date": "2026-04-05", "type": "dinner", "name": "晚餐推荐"}, {"date": "2026-04-06", "type": "breakfast", "name": "早餐推荐"}]}, {"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-04-03", "type": "breakfast", "name": "早餐推荐", "reason": "unknown_food_semantics"}, {"date": "2026-04-03", "type": "lunch", "name": "午餐推荐", "reason": "unknown_food_semantics"}, {"date": "2026-04-03", "type": "dinner", "name": "晚餐推荐", "reason": "unknown_food_semantics"}, {"date": "2026-04-04", "type": "breakfast", "name": "早餐推荐", "reason": "unknown_food_semantics"}, {"date": "2026-04-04", "type": "lunch", "name": "午餐推荐", "reason": "unknown_food_semantics"}, {"date": "2026-04-04", "type": "dinner", "name": "晚餐推荐", "reason": "unknown_food_semantics"}, {"date": "2026-04-05", "type": "breakfast", "name": "早餐推荐", "reason": "unknown_food_semantics"}, {"date": "2026-04-05", "type": "lunch", "name": "午餐推荐", "reason": "unknown_food_semantics"}, {"date": "2026-04-05", "type": "dinner", "name": "晚餐推荐", "reason": "unknown_food_semantics"}, {"date": "2026-04-06", "type": "breakfast", "name": "早餐推荐", "reason": "unknown_food_semantics"}]}]`

### v3_harder_eval_000003
- request: 西安 2025-05-03->2025-05-07 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食']
- errors: `[{"stage": "rule", "type": "hotel_distance_placeholder", "details": [{"date": "2025-05-03", "day_index": 0, "name": "坤逸·精品酒店(西安阿房宫南地铁站赳赳大秦剧院店)", "distance": "距离景点2公里"}, {"date": "2025-05-04", "day_index": 1, "name": "坤逸·精品酒店(西安阿房宫南地铁站赳赳大秦剧院店)", "distance": "距离景点2公里"}, {"date": "2025-05-05", "day_index": 2, "name": "坤逸·精品酒店(西安阿房宫南地铁站赳赳大秦剧院店)", "distance": "距离景点2公里"}, {"date": "2025-05-06", "day_index": 3, "name": "坤逸·精品酒店(西安阿房宫南地铁站赳赳大秦剧院店)", "distance": "距离景点2公里"}]}]`

### v3_harder_eval_000005
- request: 广州 2026-07-02->2026-07-06 days=5 transport=公共交通 hotel=民宿 prefs=['摄影', '自然风光', '城市漫步', '本地菜']
- errors: `[{"stage": "rule", "type": "hotel_distance_placeholder", "details": [{"date": "2026-07-02", "day_index": 0, "name": "广州好运来公寓(广州石井地铁站店)", "distance": "距离景点2公里"}, {"date": "2026-07-03", "day_index": 1, "name": "广州好运来公寓(广州石井地铁站店)", "distance": "距离景点2公里"}, {"date": "2026-07-04", "day_index": 2, "name": "广州好运来公寓(广州石井地铁站店)", "distance": "距离景点2公里"}, {"date": "2026-07-05", "day_index": 3, "name": "广州好运来公寓(广州石井地铁站店)", "distance": "距离景点2公里"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "滋粥楼·顺德菜", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-07-02", "type": "breakfast", "name": "滋粥楼·顺德菜(南村万博长隆商圈店)"}, {"date": "2026-07-03", "type": "breakfast", "name": "滋粥楼·顺德菜(南村万博长隆商圈店)"}, {"date": "2026-07-04", "type": "breakfast", "name": "滋粥楼·顺德菜(南村万博长隆商圈店)"}, {"date": "2026-07-05", "type": "breakfast", "name": "滋粥楼·顺德菜(南村万博长隆商圈店)"}, {"date": "2026-07-06", "type": "breakfast", "name": "滋粥楼·顺德菜(南村万博长隆商圈店)"}]}, {"name_key": "欧记大排档·江西景德菜", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-07-02", "type": "lunch", "name": "欧记大排档·江西景德菜(广州首店)"}, {"date": "2026-07-03", "type": "lunch", "name": "欧记大排档·江西景德菜(广州首店)"}, {"date": "2026-07-04", "type": "lunch", "name": "欧记大排档·江西景德菜(广州首店)"}, {"date": "2026-07-05", "type": "lunch", "name": "欧记大排档·江西景德菜(广州首店)"}, {"date": "2026-07-06", "type": "lunch", "name": "欧记大排档·江西景德菜(广州首店)"}]}, {"name_key": "广州仔潮汕仔特色店", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-07-02", "type": "dinner", "name": "广州仔潮汕仔特色店(广州总店)"}, {"date": "2026-07-03", "type": "dinner", "name": "广州仔潮汕仔特色店(广州总店)"}, {"date": "2026-07-04", "type": "dinner", "name": "广州仔潮汕仔特色店(广州总店)"}, {"date": "2026-07-05", "type": "dinner", "name": "广州仔潮汕仔特色店(广州总店)"}, {"date": "2026-07-06", "type": "dinner", "name": "广州仔潮汕仔特色店(广州总店)"}]}]}]`

### v3_harder_eval_000008
- request: 大理 2026-05-07->2026-05-09 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物']
- errors: `[{"stage": "rule", "type": "hotel_distance_placeholder", "details": [{"date": "2026-05-07", "day_index": 0, "name": "Q·STAR·安隐-设计师高级美学民宿(大理古城店)", "distance": "距离景点1公里"}, {"date": "2026-05-08", "day_index": 1, "name": "Q·STAR·安隐-设计师高级美学民宿(大理古城店)", "distance": "距离景点1公里"}]}, {"stage": "rule", "type": "meal_placeholder", "details": [{"date": "2026-05-07", "type": "breakfast", "name": "早餐推荐"}, {"date": "2026-05-08", "type": "breakfast", "name": "早餐推荐"}, {"date": "2026-05-09", "type": "breakfast", "name": "早餐推荐"}]}, {"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-05-07", "type": "breakfast", "name": "早餐推荐", "reason": "unknown_food_semantics"}, {"date": "2026-05-08", "type": "breakfast", "name": "早餐推荐", "reason": "unknown_food_semantics"}, {"date": "2026-05-09", "type": "breakfast", "name": "早餐推荐", "reason": "unknown_food_semantics"}, {"date": "2026-05-09", "type": "dinner", "name": "无", "reason": "empty_or_none"}]}]`

### v3_harder_eval_000009
- request: 苏州 2026-04-26->2026-04-29 days=4 transport=打车 hotel=亲子酒店 prefs=['亲子', '老人友好', '博物馆', '城市公园', '特色餐厅']
- errors: `[{"stage": "rule", "type": "hotel_distance_placeholder", "details": [{"date": "2026-04-26", "day_index": 0, "name": "苏州凯悦酒店", "distance": "距离景点2公里"}, {"date": "2026-04-27", "day_index": 1, "name": "苏州凯悦酒店", "distance": "距离景点2公里"}, {"date": "2026-04-28", "day_index": 2, "name": "苏州凯悦酒店", "distance": "距离景点2公里"}]}]`

### v3_harder_eval_000014
- request: 成都 2026-06-02->2026-06-04 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆']
- errors: `[{"stage": "rule", "type": "hotel_distance_placeholder", "details": [{"date": "2026-06-02", "day_index": 0, "name": "栖樾酒店(成都新会展中心世豪广场店)", "distance": "距离景点2公里"}, {"date": "2026-06-03", "day_index": 1, "name": "栖樾酒店(成都新会展中心世豪广场店)", "distance": "距离景点2公里"}]}, {"stage": "rule", "type": "meal_placeholder", "details": [{"date": "2026-06-02", "type": "breakfast", "name": "早餐推荐"}, {"date": "2026-06-02", "type": "lunch", "name": "午餐推荐"}, {"date": "2026-06-03", "type": "breakfast", "name": "早餐推荐"}, {"date": "2026-06-03", "type": "lunch", "name": "午餐推荐"}, {"date": "2026-06-04", "type": "breakfast", "name": "早餐推荐"}, {"date": "2026-06-04", "type": "lunch", "name": "午餐推荐"}]}, {"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-06-02", "type": "breakfast", "name": "早餐推荐", "reason": "unknown_food_semantics"}, {"date": "2026-06-02", "type": "lunch", "name": "午餐推荐", "reason": "unknown_food_semantics"}, {"date": "2026-06-03", "type": "breakfast", "name": "早餐推荐", "reason": "unknown_food_semantics"}, {"date": "2026-06-03", "type": "lunch", "name": "午餐推荐", "reason": "unknown_food_semantics"}, {"date": "2026-06-04", "type": "breakfast", "name": "早餐推荐", "reason": "unknown_food_semantics"}, {"date": "2026-06-04", "type": "lunch", "name": "午餐推荐", "reason": "unknown_food_semantics"}]}]`

### v3_harder_eval_000013
- request: 武汉 2026-05-05->2026-05-09 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食']
- errors: `[{"stage": "rule", "type": "hotel_distance_placeholder", "details": [{"date": "2026-05-05", "day_index": 0, "name": "全季酒店(武汉汉口火车站常青路店)", "distance": "距离景点2公里"}, {"date": "2026-05-06", "day_index": 1, "name": "全季酒店(武汉汉口火车站常青路店)", "distance": "距离景点2公里"}, {"date": "2026-05-07", "day_index": 2, "name": "全季酒店(武汉汉口火车站常青路店)", "distance": "距离景点2公里"}, {"date": "2026-05-08", "day_index": 3, "name": "全季酒店(武汉汉口火车站常青路店)", "distance": "距离景点2公里"}]}, {"stage": "rule", "type": "meal_placeholder", "details": [{"date": "2026-05-05", "type": "breakfast", "name": "早餐推荐"}, {"date": "2026-05-05", "type": "lunch", "name": "午餐推荐"}, {"date": "2026-05-05", "type": "dinner", "name": "晚餐推荐"}, {"date": "2026-05-06", "type": "breakfast", "name": "早餐推荐"}, {"date": "2026-05-06", "type": "lunch", "name": "午餐推荐"}, {"date": "2026-05-06", "type": "dinner", "name": "晚餐推荐"}, {"date": "2026-05-07", "type": "breakfast", "name": "早餐推荐"}, {"date": "2026-05-07", "type": "lunch", "name": "午餐推荐"}, {"date": "2026-05-07", "type": "dinner", "name": "晚餐推荐"}, {"date": "2026-05-08", "type": "breakfast", "name": "早餐推荐"}]}, {"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-05-05", "type": "breakfast", "name": "早餐推荐", "reason": "unknown_food_semantics"}, {"date": "2026-05-05", "type": "lunch", "name": "午餐推荐", "reason": "unknown_food_semantics"}, {"date": "2026-05-05", "type": "dinner", "name": "晚餐推荐", "reason": "unknown_food_semantics"}, {"date": "2026-05-06", "type": "breakfast", "name": "早餐推荐", "reason": "unknown_food_semantics"}, {"date": "2026-05-06", "type": "lunch", "name": "午餐推荐", "reason": "unknown_food_semantics"}, {"date": "2026-05-06", "type": "dinner", "name": "晚餐推荐", "reason": "unknown_food_semantics"}, {"date": "2026-05-07", "type": "breakfast", "name": "早餐推荐", "reason": "unknown_food_semantics"}, {"date": "2026-05-07", "type": "lunch", "name": "午餐推荐", "reason": "unknown_food_semantics"}, {"date": "2026-05-07", "type": "dinner", "name": "晚餐推荐", "reason": "unknown_food_semantics"}, {"date": "2026-05-08", "type": "breakfast", "name": "早餐推荐", "reason": "unknown_food_semantics"}]}]`

### v3_harder_eval_000010
- request: 西安 2026-04-19->2026-04-23 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "hotel_distance_placeholder", "details": [{"date": "2026-04-19", "day_index": 0, "name": "坤逸·精品酒店(西安阿房宫南地铁站赳赳大秦剧院店)", "distance": "距离景点2公里"}, {"date": "2026-04-20", "day_index": 1, "name": "坤逸·精品酒店(西安阿房宫南地铁站赳赳大秦剧院店)", "distance": "距离景点2公里"}, {"date": "2026-04-21", "day_index": 2, "name": "坤逸·精品酒店(西安阿房宫南地铁站赳赳大秦剧院店)", "distance": "距离景点2公里"}, {"date": "2026-04-22", "day_index": 3, "name": "坤逸·精品酒店(西安阿房宫南地铁站赳赳大秦剧院店)", "distance": "距离景点2公里"}]}, {"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-04-19", "type": "lunch", "name": "陕西历史博物馆附近餐厅", "reason": "non_food_poi_name"}, {"date": "2026-04-19", "type": "dinner", "name": "陕西历史博物馆附近餐厅", "reason": "non_food_poi_name"}, {"date": "2026-04-20", "type": "lunch", "name": "秦始皇兵马俑博物馆附近餐厅", "reason": "non_food_poi_name"}, {"date": "2026-04-20", "type": "dinner", "name": "秦始皇兵马俑博物馆附近餐厅", "reason": "non_food_poi_name"}, {"date": "2026-04-23", "type": "lunch", "name": "青龙寺遗址博物馆附近餐厅", "reason": "non_food_poi_name"}, {"date": "2026-04-23", "type": "dinner", "name": "青龙寺遗址博物馆附近餐厅", "reason": "non_food_poi_name"}]}]`

### v3_harder_eval_000011
- request: 福州 2026-06-17->2026-06-20 days=4 transport=打车 hotel=高端酒店 prefs=['高端酒店', '艺术', '特色餐厅', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "hotel_distance_placeholder", "details": [{"date": "2026-06-17", "day_index": 0, "name": "福州金融街万达连江中路亚朵酒店", "distance": "距离景点2公里"}, {"date": "2026-06-18", "day_index": 1, "name": "福州金融街万达连江中路亚朵酒店", "distance": "距离景点2公里"}, {"date": "2026-06-19", "day_index": 2, "name": "福州金融街万达连江中路亚朵酒店", "distance": "距离景点2公里"}, {"date": "2026-06-20", "day_index": 3, "name": "福州金融街万达连江中路亚朵酒店", "distance": "距离景点2公里"}]}, {"stage": "rule", "type": "meal_placeholder", "details": [{"date": "2026-06-17", "type": "breakfast", "name": "早餐推荐"}, {"date": "2026-06-17", "type": "lunch", "name": "午餐推荐"}, {"date": "2026-06-18", "type": "breakfast", "name": "早餐推荐"}, {"date": "2026-06-18", "type": "lunch", "name": "午餐推荐"}, {"date": "2026-06-19", "type": "breakfast", "name": "早餐推荐"}, {"date": "2026-06-19", "type": "lunch", "name": "午餐推荐"}, {"date": "2026-06-20", "type": "breakfast", "name": "早餐推荐"}, {"date": "2026-06-20", "type": "lunch", "name": "午餐推荐"}]}, {"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-06-17", "type": "breakfast", "name": "早餐推荐", "reason": "unknown_food_semantics"}, {"date": "2026-06-17", "type": "lunch", "name": "午餐推荐", "reason": "unknown_food_semantics"}, {"date": "2026-06-18", "type": "breakfast", "name": "早餐推荐", "reason": "unknown_food_semantics"}, {"date": "2026-06-18", "type": "lunch", "name": "午餐推荐", "reason": "unknown_food_semantics"}, {"date": "2026-06-19", "type": "breakfast", "name": "早餐推荐", "reason": "unknown_food_semantics"}, {"date": "2026-06-19", "type": "lunch", "name": "午餐推荐", "reason": "unknown_food_semantics"}, {"date": "2026-06-20", "type": "breakfast", "name": "早餐推荐", "reason": "unknown_food_semantics"}, {"date": "2026-06-20", "type": "lunch", "name": "午餐推荐", "reason": "unknown_food_semantics"}]}]`

### v3_harder_eval_000016
- request: 苏州 2026-06-02->2026-06-05 days=4 transport=自驾 hotel=亲子酒店 prefs=['亲子', '动物园', '海洋馆', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "hotel_distance_placeholder", "details": [{"date": "2026-06-02", "day_index": 0, "name": "苏州石湖金陵花园酒店", "distance": "距离景点2公里"}, {"date": "2026-06-03", "day_index": 1, "name": "苏州石湖金陵花园酒店", "distance": "距离景点2公里"}, {"date": "2026-06-04", "day_index": 2, "name": "苏州石湖金陵花园酒店", "distance": "距离景点2公里"}]}, {"stage": "rule", "type": "meal_placeholder", "details": [{"date": "2026-06-02", "type": "breakfast", "name": "早餐推荐"}, {"date": "2026-06-02", "type": "lunch", "name": "午餐推荐"}, {"date": "2026-06-02", "type": "dinner", "name": "晚餐推荐"}, {"date": "2026-06-03", "type": "breakfast", "name": "早餐推荐"}, {"date": "2026-06-03", "type": "lunch", "name": "午餐推荐"}, {"date": "2026-06-03", "type": "dinner", "name": "晚餐推荐"}, {"date": "2026-06-04", "type": "breakfast", "name": "早餐推荐"}, {"date": "2026-06-04", "type": "lunch", "name": "午餐推荐"}, {"date": "2026-06-04", "type": "dinner", "name": "晚餐推荐"}, {"date": "2026-06-05", "type": "breakfast", "name": "早餐推荐"}]}, {"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-06-02", "type": "breakfast", "name": "早餐推荐", "reason": "unknown_food_semantics"}, {"date": "2026-06-02", "type": "lunch", "name": "午餐推荐", "reason": "unknown_food_semantics"}, {"date": "2026-06-02", "type": "dinner", "name": "晚餐推荐", "reason": "unknown_food_semantics"}, {"date": "2026-06-03", "type": "breakfast", "name": "早餐推荐", "reason": "unknown_food_semantics"}, {"date": "2026-06-03", "type": "lunch", "name": "午餐推荐", "reason": "unknown_food_semantics"}, {"date": "2026-06-03", "type": "dinner", "name": "晚餐推荐", "reason": "unknown_food_semantics"}, {"date": "2026-06-04", "type": "breakfast", "name": "早餐推荐", "reason": "unknown_food_semantics"}, {"date": "2026-06-04", "type": "lunch", "name": "午餐推荐", "reason": "unknown_food_semantics"}, {"date": "2026-06-04", "type": "dinner", "name": "晚餐推荐", "reason": "unknown_food_semantics"}, {"date": "2026-06-05", "type": "breakfast", "name": "早餐推荐", "reason": "unknown_food_semantics"}]}]`

### v3_harder_eval_000015
- request: 南京 2026-04-03->2026-04-07 days=5 transport=公共交通 hotel=民宿 prefs=['摄影', '自然风光', '城市漫步', '本地菜']
- errors: `[{"stage": "json_extract", "message": "响应中未找到完整的顶层TripPlan JSON对象"}]`

### v3_harder_eval_000012
- request: 洛阳 2025-05-03->2025-05-06 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '夜市', '老字号', '城市漫步']
- errors: `[{"stage": "rule", "type": "hotel_distance_placeholder", "details": [{"date": "2025-05-03", "day_index": 0, "name": "栾川一家人宾馆", "distance": "距离景点2公里"}, {"date": "2025-05-04", "day_index": 1, "name": "宜阳君临宾馆", "distance": "距离景点2公里"}, {"date": "2025-05-05", "day_index": 2, "name": "鑫升宾馆(宜阳流泉镇店)", "distance": "距离景点2公里"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "方中山胡辣汤", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2025-05-03", "type": "breakfast", "name": "方中山胡辣汤(洛阳一店)"}, {"date": "2025-05-04", "type": "breakfast", "name": "方中山胡辣汤(洛阳一店)"}, {"date": "2025-05-05", "type": "breakfast", "name": "方中山胡辣汤(洛阳一店)"}, {"date": "2025-05-06", "type": "breakfast", "name": "方中山胡辣汤(洛阳一店)"}]}, {"name_key": "小秦川", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2025-05-03", "type": "lunch", "name": "小秦川(政和路总店)"}, {"date": "2025-05-04", "type": "lunch", "name": "小秦川(政和路总店)"}, {"date": "2025-05-05", "type": "lunch", "name": "小秦川(政和路总店)"}, {"date": "2025-05-06", "type": "lunch", "name": "小秦川(政和路总店)"}]}, {"name_key": "十字街夜市", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2025-05-03", "type": "dinner", "name": "十字街夜市"}, {"date": "2025-05-04", "type": "dinner", "name": "十字街夜市"}, {"date": "2025-05-05", "type": "dinner", "name": "十字街夜市"}, {"date": "2025-05-06", "type": "dinner", "name": "十字街夜市"}]}]}]`

### v3_harder_eval_000018
- request: 天津 2026-07-02->2026-07-04 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物']
- errors: `[{"stage": "rule", "type": "hotel_distance_placeholder", "details": [{"date": "2026-07-02", "day_index": 0, "name": "天津津湾广场桔子水晶酒店", "distance": "距离景点2公里"}, {"date": "2026-07-03", "day_index": 1, "name": "天津津湾广场桔子水晶酒店", "distance": "距离景点2公里"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "南楼煎饼", "count": 3, "max_allowed": 2, "occurrences": [{"date": "2026-07-02", "type": "breakfast", "name": "南楼煎饼"}, {"date": "2026-07-03", "type": "breakfast", "name": "南楼煎饼"}, {"date": "2026-07-04", "type": "breakfast", "name": "南楼煎饼"}]}, {"name_key": "太守宴·蘭院", "count": 3, "max_allowed": 2, "occurrences": [{"date": "2026-07-02", "type": "lunch", "name": "太守宴·蘭院"}, {"date": "2026-07-03", "type": "lunch", "name": "太守宴·蘭院"}, {"date": "2026-07-04", "type": "lunch", "name": "太守宴·蘭院"}]}, {"name_key": "苏焰·地标天津菜", "count": 3, "max_allowed": 2, "occurrences": [{"date": "2026-07-02", "type": "dinner", "name": "苏焰·地标天津菜(金海道店)"}, {"date": "2026-07-03", "type": "dinner", "name": "苏焰·地标天津菜(金海道店)"}, {"date": "2026-07-04", "type": "dinner", "name": "苏焰·地标天津菜(金海道店)"}]}]}]`

### v3_harder_eval_000019
- request: 丽江 2026-05-07->2026-05-10 days=4 transport=打车 hotel=亲子酒店 prefs=['亲子', '老人友好', '博物馆', '城市公园', '特色餐厅']
- errors: `[{"stage": "rule", "type": "hotel_distance_placeholder", "details": [{"date": "2026-05-07", "day_index": 0, "name": "静隅花间·与诗同眠", "distance": "距离景点2公里"}, {"date": "2026-05-08", "day_index": 1, "name": "静隅花间·与诗同眠", "distance": "距离景点2公里"}, {"date": "2026-05-09", "day_index": 2, "name": "静隅花间·与诗同眠", "distance": "距离景点2公里"}]}, {"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-05-07", "type": "breakfast", "name": "丽江古城特色早餐", "reason": "unknown_food_semantics"}, {"date": "2026-05-07", "type": "lunch", "name": "丽江古城特色午餐", "reason": "unknown_food_semantics"}, {"date": "2026-05-07", "type": "dinner", "name": "丽江古城特色晚餐", "reason": "unknown_food_semantics"}, {"date": "2026-05-08", "type": "breakfast", "name": "束河古镇特色早餐", "reason": "unknown_food_semantics"}, {"date": "2026-05-08", "type": "lunch", "name": "束河古镇特色午餐", "reason": "unknown_food_semantics"}, {"date": "2026-05-08", "type": "dinner", "name": "束河古镇特色晚餐", "reason": "unknown_food_semantics"}, {"date": "2026-05-09", "type": "breakfast", "name": "文华公园特色早餐", "reason": "non_food_poi_name"}, {"date": "2026-05-09", "type": "lunch", "name": "文华公园特色午餐", "reason": "non_food_poi_name"}, {"date": "2026-05-09", "type": "dinner", "name": "文华公园特色晚餐", "reason": "non_food_poi_name"}, {"date": "2026-05-10", "type": "breakfast", "name": "丽江之眼观景台特色早餐", "reason": "unknown_food_semantics"}]}]`

### v3_harder_eval_000024
- request: 济南 2026-05-06->2026-05-08 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆']
- errors: `[{"stage": "rule", "type": "hotel_distance_placeholder", "details": [{"date": "2026-05-06", "day_index": 0, "name": "城市便捷酒店(济南奥体中心店)", "distance": "距离景点2公里"}, {"date": "2026-05-07", "day_index": 1, "name": "城市便捷酒店(济南奥体中心店)", "distance": "距离景点2公里"}]}, {"stage": "rule", "type": "meal_placeholder", "details": [{"date": "2026-05-06", "type": "breakfast", "name": "早餐推荐"}, {"date": "2026-05-06", "type": "lunch", "name": "午餐推荐"}, {"date": "2026-05-06", "type": "dinner", "name": "晚餐推荐"}, {"date": "2026-05-07", "type": "breakfast", "name": "早餐推荐"}, {"date": "2026-05-07", "type": "lunch", "name": "午餐推荐"}, {"date": "2026-05-07", "type": "dinner", "name": "晚餐推荐"}, {"date": "2026-05-08", "type": "breakfast", "name": "早餐推荐"}, {"date": "2026-05-08", "type": "lunch", "name": "午餐推荐"}, {"date": "2026-05-08", "type": "dinner", "name": "晚餐推荐"}]}, {"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-05-06", "type": "breakfast", "name": "早餐推荐", "reason": "unknown_food_semantics"}, {"date": "2026-05-06", "type": "lunch", "name": "午餐推荐", "reason": "unknown_food_semantics"}, {"date": "2026-05-06", "type": "dinner", "name": "晚餐推荐", "reason": "unknown_food_semantics"}, {"date": "2026-05-07", "type": "breakfast", "name": "早餐推荐", "reason": "unknown_food_semantics"}, {"date": "2026-05-07", "type": "lunch", "name": "午餐推荐", "reason": "unknown_food_semantics"}, {"date": "2026-05-07", "type": "dinner", "name": "晚餐推荐", "reason": "unknown_food_semantics"}, {"date": "2026-05-08", "type": "breakfast", "name": "早餐推荐", "reason": "unknown_food_semantics"}, {"date": "2026-05-08", "type": "lunch", "name": "午餐推荐", "reason": "unknown_food_semantics"}, {"date": "2026-05-08", "type": "dinner", "name": "晚餐推荐", "reason": "unknown_food_semantics"}]}]`
