# Rule Eval Report: base_qwen25_7b_v3_harder_no_route_meal_hotel_prompt_w8

- records: 300
- generations: `training/outputs/eval/base_qwen25_7b_v3_harder_no_route_meal_hotel_prompt_w8/generations.jsonl`
- records_path: `training/data/v3/eval_harder_prompt_meal_hotel_fixed_no_route/records.jsonl`

## Boolean Metrics

| Metric | Pass | Total | Rate |
| --- | ---: | ---: | ---: |
| attraction_count_ok | 291 | 291 | 100.00% |
| attraction_grounding_ok | 287 | 291 | 98.63% |
| budget_arithmetic_consistent | 280 | 291 | 96.22% |
| budget_consistent | 280 | 291 | 96.22% |
| budget_level_aligned | 280 | 291 | 96.22% |
| budget_preference_aligned | 280 | 291 | 96.22% |
| budget_within_user_budget | 291 | 291 | 100.00% |
| city_ok | 291 | 291 | 100.00% |
| date_range_ok | 291 | 291 | 100.00% |
| day_dates_ok | 291 | 291 | 100.00% |
| day_index_ok | 291 | 291 | 100.00% |
| days_len_ok | 291 | 291 | 100.00% |
| dpo_soft_pass | 97 | 291 | 33.33% |
| hard_pass | 166 | 291 | 57.04% |
| hotel_budget_covers_nights | 287 | 291 | 98.63% |
| hotel_distance_placeholder_ok | 291 | 291 | 100.00% |
| hotel_grounding_ok | 291 | 291 | 100.00% |
| invalid_hotel_name_ok | 291 | 291 | 100.00% |
| json_extract_ok | 297 | 300 | 99.00% |
| legacy_hard_pass | 114 | 291 | 39.18% |
| location_object_ok | 291 | 291 | 100.00% |
| meal_complete | 287 | 291 | 98.63% |
| meal_diversity_ok | 216 | 291 | 74.23% |
| meal_grounding_ok | 170 | 291 | 58.42% |
| meal_lunch_dinner_same_day_ok | 251 | 291 | 86.25% |
| meal_repeat_limit_ok | 228 | 291 | 78.35% |
| meal_specific_ok | 282 | 291 | 96.91% |
| meal_valid_semantics_ok | 181 | 291 | 62.20% |
| middle_hotel_ok | 291 | 291 | 100.00% |
| schema_ok | 291 | 300 | 97.00% |
| sft_hard_pass | 166 | 291 | 57.04% |
| weather_dates_ok | 291 | 291 | 100.00% |
| weather_match | 290 | 291 | 99.66% |

## Numeric Metrics

```json
{
  "attraction_grounding_rate": {
    "avg": 0.9976,
    "p50": 1.0,
    "p90": 1.0
  },
  "hotel_grounding_rate": {
    "avg": 1.0,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_diversity_unique_rate": {
    "avg": 0.5478,
    "p50": 0.5,
    "p90": 1.0
  },
  "meal_food_pois_grounding_rate": {
    "avg": 0.8386,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_grounding_rate": {
    "avg": 0.8386,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_semantic_valid_rate": {
    "avg": 0.9045,
    "p50": 1.0,
    "p90": 1.0
  }
}
```

## Failure Types

```json
{
  "meal_invalid_name": 110,
  "meal_repeat_too_many": 63,
  "meal_same_day_lunch_dinner_repeat": 40,
  "budget_preference_mismatch": 11,
  "meal_grounding_miss": 11,
  "budget_arithmetic_inconsistent": 11,
  "meal_placeholder": 9,
  "schema": 6,
  "hotel_budget_underestimated": 4,
  "json_extract": 3,
  "weather_mismatch": 1
}
```

## Failure Examples

### v3_harder_eval_000007
- request: 成都 2026-05-07->2026-05-11 days=5 transport=公共交通 hotel=民宿 prefs=['小众展馆', '咖啡', '艺术', '城市漫步', '特色餐厅']
- errors: `[{"stage": "rule", "type": "meal_placeholder", "details": [{"date": "2026-05-08", "type": "lunch", "name": "M Stand(成都SKP店)"}, {"date": "2026-05-10", "type": "lunch", "name": "M Stand(成都SKP店)"}]}, {"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-05-08", "type": "lunch", "name": "M Stand(成都SKP店)", "reason": "unknown_food_semantics"}, {"date": "2026-05-10", "type": "lunch", "name": "M Stand(成都SKP店)", "reason": "unknown_food_semantics"}, {"date": "2026-05-11", "type": "dinner", "name": "无", "reason": "empty_or_none"}]}, {"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-05-09", "lunch": "星巴克(成都大魔方招商花园城店)", "dinner": "星巴克(成都环球中心II店)"}]}]`

### v3_harder_eval_000000
- request: 昆明 2026-04-03->2026-04-07 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-04-03", "type": "lunch", "name": "小人国主题公园附近的餐厅", "reason": "non_food_poi_name"}, {"date": "2026-04-03", "type": "dinner", "name": "昆明捞渔河湿地公园附近的餐厅", "reason": "non_food_poi_name"}, {"date": "2026-04-04", "type": "lunch", "name": "云南美术馆(五一路)附近的餐厅", "reason": "non_food_poi_name"}, {"date": "2026-04-04", "type": "dinner", "name": "云南民族博物馆附近的餐厅", "reason": "non_food_poi_name"}, {"date": "2026-04-05", "type": "lunch", "name": "昆明瀑布公园附近的餐厅", "reason": "non_food_poi_name"}, {"date": "2026-04-06", "type": "dinner", "name": "月牙潭公园附近的餐厅", "reason": "non_food_poi_name"}, {"date": "2026-04-07", "type": "lunch", "name": "守望山·治愈系城市露营公园附近的餐厅", "reason": "non_food_poi_name"}]}]`

### v3_harder_eval_000002
- request: 杭州 2026-04-27->2026-04-30 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '夜市', '老字号', '城市漫步']
- errors: `[{"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-04-30", "type": "lunch", "name": "久居(杭州来福士店)", "reason": "unknown_food_semantics"}]}, {"stage": "rule", "type": "budget_preference_mismatch", "details": {"part_sum": 2792, "total": 2892, "diff": -100, "requested_budget": {"available": false, "amount": 0, "scope": "unknown", "party_size": 2, "total": 0}, "per_person_day": 361.5, "budget_level": "limited", "arithmetic_consistent": true, "within_user_budget": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 3, "priced_nights": 3, "expected_min_total_hotels": 750, "reported_total_hotels": 1000, "diff": 250, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_harder_eval_000001
- request: 桂林 2026-08-31->2026-09-03 days=4 transport=打车 hotel=高端酒店 prefs=['高端酒店', '艺术', '特色餐厅', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-09-03", "type": "dinner", "name": "酒店晚餐", "reason": "generic_lodging_meal"}]}]`

### v3_harder_eval_000003
- request: 西安 2025-05-03->2025-05-07 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食']
- errors: `[{"stage": "schema", "message": "1 validation error for TripPlan\ndays.4.accommodation\n  Input should be a valid string [type=string_type, input_value=None, input_type=NoneType]\n    For further information visit https://errors.pydantic.dev/2.12/v/string_type"}]`

### v3_harder_eval_000008
- request: 大理 2026-05-07->2026-05-09 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物']
- errors: `[{"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-05-09", "type": "dinner", "name": "无", "reason": "empty_or_none"}]}]`

### v3_harder_eval_000014
- request: 成都 2026-06-02->2026-06-04 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-06-02", "lunch": "观锦餐厅(天廊店)", "dinner": "观锦餐厅(天府新谷店)"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "观锦餐厅", "count": 3, "max_allowed": 2, "occurrences": [{"date": "2026-06-02", "type": "lunch", "name": "观锦餐厅(天廊店)"}, {"date": "2026-06-02", "type": "dinner", "name": "观锦餐厅(天府新谷店)"}, {"date": "2026-06-03", "type": "dinner", "name": "观锦餐厅(天府新谷店)"}]}]}]`

### v3_harder_eval_000013
- request: 武汉 2026-05-05->2026-05-09 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-05-06", "type": "lunch", "name": "江城人家", "reason": "unknown_food_semantics"}, {"date": "2026-05-08", "type": "lunch", "name": "江城人家", "reason": "unknown_food_semantics"}, {"date": "2026-05-09", "type": "lunch", "name": "江城人家", "reason": "unknown_food_semantics"}, {"date": "2026-05-09", "type": "dinner", "name": "酒店晚餐", "reason": "generic_lodging_meal"}]}]`

### v3_harder_eval_000010
- request: 西安 2026-04-19->2026-04-23 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-04-19", "type": "dinner", "name": "陕西历史博物馆附近餐厅", "reason": "non_food_poi_name"}, {"date": "2026-04-20", "type": "lunch", "name": "莲湖公园附近餐厅", "reason": "non_food_poi_name"}, {"date": "2026-04-20", "type": "dinner", "name": "莲湖公园附近餐厅", "reason": "non_food_poi_name"}, {"date": "2026-04-21", "type": "lunch", "name": "莲湖公园附近餐厅", "reason": "non_food_poi_name"}, {"date": "2026-04-21", "type": "dinner", "name": "莲湖公园附近餐厅", "reason": "non_food_poi_name"}, {"date": "2026-04-22", "type": "lunch", "name": "莲湖公园附近餐厅", "reason": "non_food_poi_name"}, {"date": "2026-04-22", "type": "dinner", "name": "莲湖公园附近餐厅", "reason": "non_food_poi_name"}, {"date": "2026-04-23", "type": "lunch", "name": "莲湖公园附近餐厅", "reason": "non_food_poi_name"}, {"date": "2026-04-23", "type": "dinner", "name": "莲湖公园附近餐厅", "reason": "non_food_poi_name"}]}]`

### v3_harder_eval_000015
- request: 南京 2026-04-03->2026-04-07 days=5 transport=公共交通 hotel=民宿 prefs=['摄影', '自然风光', '城市漫步', '本地菜']
- errors: `[{"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-04-07", "type": "dinner", "name": "无", "reason": "empty_or_none"}]}]`

### v3_harder_eval_000016
- request: 苏州 2026-06-02->2026-06-05 days=4 transport=自驾 hotel=亲子酒店 prefs=['亲子', '动物园', '海洋馆', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_grounding_miss", "details": [{"date": "2026-06-02", "type": "lunch", "name": "苏州乐园森林世界附近的餐厅"}, {"date": "2026-06-02", "type": "dinner", "name": "苏州乐园森林世界附近的餐厅"}, {"date": "2026-06-03", "type": "lunch", "name": "苏州乐园森林世界附近的餐厅"}, {"date": "2026-06-03", "type": "dinner", "name": "苏州乐园森林世界附近的餐厅"}, {"date": "2026-06-04", "type": "lunch", "name": "苏州乐园森林世界附近的餐厅"}, {"date": "2026-06-04", "type": "dinner", "name": "苏州乐园森林世界附近的餐厅"}, {"date": "2026-06-05", "type": "lunch", "name": "苏州乐园森林世界附近的餐厅"}, {"date": "2026-06-05", "type": "dinner", "name": "苏州乐园森林世界附近的餐厅"}]}]`

### v3_harder_eval_000012
- request: 洛阳 2025-05-03->2025-05-06 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '夜市', '老字号', '城市漫步']
- errors: `[{"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2025-05-06", "type": "dinner", "name": "无", "reason": "empty_or_none"}]}]`

### v3_harder_eval_000019
- request: 丽江 2026-05-07->2026-05-10 days=4 transport=打车 hotel=亲子酒店 prefs=['亲子', '老人友好', '博物馆', '城市公园', '特色餐厅']
- errors: `[{"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "priced_nights": 3, "expected_min_total_hotels": 2200, "reported_total_hotels": 1500, "diff": -700, "covers_nights": false}}]`

### v3_harder_eval_000024
- request: 济南 2026-05-06->2026-05-08 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆']
- errors: `[{"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-05-08", "type": "dinner", "name": "酒店晚餐", "reason": "generic_lodging_meal"}]}]`

### v3_harder_eval_000021
- request: 上海 2026-06-17->2026-06-20 days=4 transport=打车 hotel=高端酒店 prefs=['高端酒店', '艺术', '特色餐厅', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "3号仓库·餐厅", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-06-17", "type": "dinner", "name": "3号仓库·餐厅(上海首店)"}, {"date": "2026-06-18", "type": "dinner", "name": "3号仓库·餐厅(徐汇绿地缤纷城店)"}, {"date": "2026-06-19", "type": "lunch", "name": "3号仓库·餐厅(徐汇绿地缤纷城店)"}, {"date": "2026-06-20", "type": "lunch", "name": "3号仓库·餐厅(徐汇绿地缤纷城店)"}]}]}]`

### v3_harder_eval_000023
- request: 大理 2026-08-31->2026-09-04 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-09-01", "type": "lunch", "name": "洱海公园附近餐厅", "reason": "non_food_poi_name"}, {"date": "2026-09-01", "type": "dinner", "name": "洱海公园附近餐厅", "reason": "non_food_poi_name"}, {"date": "2026-09-04", "type": "lunch", "name": "大理苍山世界地质公园附近餐厅", "reason": "non_food_poi_name"}, {"date": "2026-09-04", "type": "dinner", "name": "大理苍山世界地质公园附近餐厅", "reason": "non_food_poi_name"}]}]`

### v3_harder_eval_000020
- request: 杭州 2026-06-17->2026-06-21 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "友好饭店·道乐日式拉面·烧鸟·酒场", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-06-17", "type": "lunch", "name": "友好饭店·道乐日式拉面·烧鸟·酒场(湖滨店)"}, {"date": "2026-06-19", "type": "lunch", "name": "友好饭店·道乐日式拉面·烧鸟·酒场(湖滨店)"}, {"date": "2026-06-20", "type": "dinner", "name": "友好饭店·道乐日式拉面·烧鸟·酒场(湖滨店)"}, {"date": "2026-06-21", "type": "dinner", "name": "友好饭店·道乐日式拉面·烧鸟·酒场(湖滨店)"}]}]}]`

### v3_harder_eval_000017
- request: 苏州 2026-05-05->2026-05-09 days=5 transport=公共交通 hotel=民宿 prefs=['小众展馆', '咖啡', '艺术', '城市漫步', '特色餐厅']
- errors: `[{"stage": "rule", "type": "meal_placeholder", "details": [{"date": "2026-05-07", "type": "lunch", "name": "LIM Café(运河公园店)"}]}, {"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-05-07", "type": "lunch", "name": "LIM Café(运河公园店)", "reason": "non_food_poi_name"}]}]`

### v3_harder_eval_000026
- request: 扬州 2026-05-07->2026-05-10 days=4 transport=自驾 hotel=亲子酒店 prefs=['亲子', '动物园', '海洋馆', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-05-07", "type": "lunch", "name": "扬州炒饭", "reason": "unknown_food_semantics"}, {"date": "2026-05-07", "type": "dinner", "name": "扬州炒面", "reason": "unknown_food_semantics"}, {"date": "2026-05-08", "type": "lunch", "name": "扬州炒饭", "reason": "unknown_food_semantics"}, {"date": "2026-05-08", "type": "dinner", "name": "扬州炒面", "reason": "unknown_food_semantics"}, {"date": "2026-05-09", "type": "lunch", "name": "扬州炒饭", "reason": "unknown_food_semantics"}, {"date": "2026-05-09", "type": "dinner", "name": "扬州炒面", "reason": "unknown_food_semantics"}, {"date": "2026-05-10", "type": "lunch", "name": "扬州炒饭", "reason": "unknown_food_semantics"}, {"date": "2026-05-10", "type": "dinner", "name": "扬州炒面", "reason": "unknown_food_semantics"}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "priced_nights": 3, "expected_min_total_hotels": 2200, "reported_total_hotels": 1500, "diff": -700, "covers_nights": false}}]`

### v3_harder_eval_000025
- request: 上海 2026-08-01->2026-08-05 days=5 transport=公共交通 hotel=民宿 prefs=['摄影', '自然风光', '城市漫步', '本地菜']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "农家菜老大", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-08-01", "type": "dinner", "name": "农家菜老大(松江店)"}, {"date": "2026-08-02", "type": "dinner", "name": "农家菜老大(九亭店)"}, {"date": "2026-08-03", "type": "dinner", "name": "农家菜老大(松江店)"}, {"date": "2026-08-04", "type": "dinner", "name": "农家菜老大(松江店)"}, {"date": "2026-08-05", "type": "dinner", "name": "农家菜老大(松江店)"}]}]}]`
