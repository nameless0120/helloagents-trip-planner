# Rule Eval Report: base_qwen25_7b_v3_harder_ablation_meal_rotation_symbolic_w12

- records: 300
- generations: `training/outputs/eval/base_qwen25_7b_v3_harder_ablation_meal_rotation_symbolic_w12/generations.jsonl`
- records_path: `training/data/v3/eval_harder_food_bucket_meal_diversity_ablation_meal_rotation_symbolic_no_route/records.jsonl`

## Boolean Metrics

| Metric | Pass | Total | Rate |
| --- | ---: | ---: | ---: |
| attraction_count_ok | 294 | 294 | 100.00% |
| attraction_grounding_ok | 290 | 294 | 98.64% |
| budget_arithmetic_consistent | 265 | 294 | 90.14% |
| budget_consistent | 265 | 294 | 90.14% |
| budget_level_aligned | 292 | 294 | 99.32% |
| budget_preference_aligned | 292 | 294 | 99.32% |
| budget_within_user_budget | 294 | 294 | 100.00% |
| city_ok | 294 | 294 | 100.00% |
| date_range_ok | 293 | 294 | 99.66% |
| day_dates_ok | 294 | 294 | 100.00% |
| day_index_ok | 294 | 294 | 100.00% |
| days_len_ok | 294 | 294 | 100.00% |
| dpo_soft_pass | 127 | 294 | 43.20% |
| hard_pass | 229 | 294 | 77.89% |
| hotel_budget_covers_nights | 291 | 294 | 98.98% |
| hotel_distance_placeholder_ok | 294 | 294 | 100.00% |
| hotel_grounding_ok | 293 | 294 | 99.66% |
| invalid_hotel_name_ok | 294 | 294 | 100.00% |
| json_extract_ok | 298 | 300 | 99.33% |
| legacy_hard_pass | 130 | 294 | 44.22% |
| location_object_ok | 294 | 294 | 100.00% |
| meal_complete | 294 | 294 | 100.00% |
| meal_diversity_ok | 164 | 294 | 55.78% |
| meal_grounding_ok | 263 | 294 | 89.46% |
| meal_lunch_dinner_same_day_ok | 206 | 294 | 70.07% |
| meal_repeat_limit_ok | 207 | 294 | 70.41% |
| meal_specific_ok | 294 | 294 | 100.00% |
| meal_valid_semantics_ok | 266 | 294 | 90.48% |
| middle_hotel_ok | 294 | 294 | 100.00% |
| schema_ok | 294 | 300 | 98.00% |
| sft_hard_pass | 229 | 294 | 77.89% |
| weather_dates_ok | 294 | 294 | 100.00% |
| weather_match | 294 | 294 | 100.00% |

## Numeric Metrics

```json
{
  "attraction_grounding_rate": {
    "avg": 0.9979,
    "p50": 1.0,
    "p90": 1.0
  },
  "hotel_grounding_rate": {
    "avg": 0.9966,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_diversity_unique_rate": {
    "avg": 0.7429,
    "p50": 0.8,
    "p90": 1.0
  },
  "meal_food_pois_grounding_rate": {
    "avg": 0.9886,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_grounding_rate": {
    "avg": 0.9886,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_semantic_valid_rate": {
    "avg": 0.99,
    "p50": 1.0,
    "p90": 1.0
  }
}
```

## Failure Types

```json
{
  "meal_same_day_lunch_dinner_repeat": 88,
  "meal_repeat_too_many": 87,
  "budget_arithmetic_inconsistent": 29,
  "meal_invalid_name": 28,
  "schema": 4,
  "hotel_budget_underestimated": 3,
  "meal_grounding_miss": 3,
  "budget_preference_mismatch": 2,
  "json_extract": 2
}
```

## Failure Examples

### v3_harder_eval_000001
- request: 桂林 2026-09-01->2026-09-04 days=4 transport=打车 hotel=高端酒店 prefs=['高端酒店', '艺术', '特色餐厅', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-09-04", "type": "dinner", "name": "无", "reason": "empty_or_none"}]}]`

### v3_harder_eval_000000
- request: 昆明 2026-04-04->2026-04-08 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "晨曦豆花米线", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-04-04", "type": "breakfast", "name": "晨曦豆花米线"}, {"date": "2026-04-05", "type": "breakfast", "name": "晨曦豆花米线"}, {"date": "2026-04-06", "type": "breakfast", "name": "晨曦豆花米线"}, {"date": "2026-04-07", "type": "breakfast", "name": "晨曦豆花米线"}, {"date": "2026-04-08", "type": "breakfast", "name": "晨曦豆花米线"}]}]}]`

### v3_harder_eval_000003
- request: 西安 2025-05-04->2025-05-08 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "魏家凉皮", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2025-05-04", "type": "breakfast", "name": "魏家凉皮(西大街店)"}, {"date": "2025-05-05", "type": "breakfast", "name": "魏家凉皮(西大街店)"}, {"date": "2025-05-06", "type": "breakfast", "name": "魏家凉皮(西大街店)"}, {"date": "2025-05-07", "type": "breakfast", "name": "魏家凉皮(西大街店)"}, {"date": "2025-05-08", "type": "breakfast", "name": "魏家凉皮(西大街店)"}]}, {"name_key": "崔少野猫耳朵炒面", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2025-05-04", "type": "dinner", "name": "崔少野猫耳朵炒面(十里锦绣店)"}, {"date": "2025-05-05", "type": "lunch", "name": "崔少野猫耳朵炒面(十里锦绣店)"}, {"date": "2025-05-07", "type": "lunch", "name": "崔少野猫耳朵炒面(十里锦绣店)"}, {"date": "2025-05-08", "type": "lunch", "name": "崔少野猫耳朵炒面(十里锦绣店)"}]}, {"name_key": "马洪小炒泡馍馆", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2025-05-05", "type": "dinner", "name": "马洪小炒泡馍馆"}, {"date": "2025-05-06", "type": "dinner", "name": "马洪小炒泡馍馆"}, {"date": "2025-05-07", "type": "dinner", "name": "马洪小炒泡馍馆"}, {"date": "2025-05-08", "type": "dinner", "name": "马洪小炒泡馍馆"}]}]}]`

### v3_harder_eval_000005
- request: 广州 2026-07-03->2026-07-07 days=5 transport=公共交通 hotel=民宿 prefs=['摄影', '自然风光', '城市漫步', '本地菜']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 3000, "total": 2000, "diff": 1000, "requested_budget": {"available": false, "amount": 0, "scope": "unknown", "party_size": 1, "total": 0}, "per_person_day": 400.0, "budget_level": "standard", "arithmetic_consistent": false, "within_user_budget": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 4, "priced_nights": 4, "expected_min_total_hotels": 1200, "reported_total_hotels": 1200, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_harder_eval_000007
- request: 成都 2026-05-08->2026-05-12 days=5 transport=公共交通 hotel=民宿 prefs=['小众展馆', '咖啡', '艺术', '城市漫步', '特色餐厅']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 3080, "total": 2060, "diff": 1020, "requested_budget": {"available": false, "amount": 0, "scope": "unknown", "party_size": 2, "total": 0}, "per_person_day": 206.0, "budget_level": "comfortable", "arithmetic_consistent": false, "within_user_budget": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 4, "priced_nights": 4, "expected_min_total_hotels": 1200, "reported_total_hotels": 1200, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_harder_eval_000012
- request: 洛阳 2025-05-04->2025-05-07 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '夜市', '老字号', '城市漫步']
- errors: `[{"stage": "rule", "type": "budget_preference_mismatch", "details": {"part_sum": 3380, "total": 3380, "diff": 0, "requested_budget": {"available": false, "amount": 0, "scope": "unknown", "party_size": 2, "total": 0}, "per_person_day": 422.5, "budget_level": "limited", "arithmetic_consistent": true, "within_user_budget": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 3, "priced_nights": 3, "expected_min_total_hotels": 700, "reported_total_hotels": 1200, "diff": 500, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_harder_eval_000014
- request: 成都 2026-06-03->2026-06-05 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-06-03", "lunch": "观锦餐厅(天府新谷店)", "dinner": "观锦餐厅(天廊店)"}, {"date": "2026-06-05", "lunch": "四妹钵钵鸡(望平街店)", "dinner": "四妹钵钵鸡(望平街店)"}]}]`

### v3_harder_eval_000013
- request: 武汉 2026-05-06->2026-05-10 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-05-10", "lunch": "刘聋子牛肉粉馆(汉阳龙兴东街店)", "dinner": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "刘聋子牛肉粉馆", "count": 6, "max_allowed": 3, "occurrences": [{"date": "2026-05-06", "type": "dinner", "name": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}, {"date": "2026-05-07", "type": "dinner", "name": "刘聋子牛肉粉馆(汉阳玫瑰街店)"}, {"date": "2026-05-08", "type": "dinner", "name": "刘聋子牛肉粉馆(光谷新竹路店)"}, {"date": "2026-05-09", "type": "dinner", "name": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}, {"date": "2026-05-10", "type": "lunch", "name": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}, {"date": "2026-05-10", "type": "dinner", "name": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}]}]}]`

### v3_harder_eval_000017
- request: 苏州 2026-05-06->2026-05-10 days=5 transport=公共交通 hotel=民宿 prefs=['小众展馆', '咖啡', '艺术', '城市漫步', '特色餐厅']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "秋娟馄饨店", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-05-06", "type": "breakfast", "name": "秋娟馄饨店"}, {"date": "2026-05-07", "type": "breakfast", "name": "秋娟馄饨店"}, {"date": "2026-05-08", "type": "breakfast", "name": "秋娟馄饨店"}, {"date": "2026-05-09", "type": "breakfast", "name": "秋娟馄饨店"}, {"date": "2026-05-10", "type": "breakfast", "name": "秋娟馄饨店"}]}, {"name_key": "江南雅厨·非遗苏州菜", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-05-06", "type": "lunch", "name": "江南雅厨·非遗苏州菜(李公堤店)"}, {"date": "2026-05-08", "type": "lunch", "name": "江南雅厨·非遗苏州菜(李公堤店)"}, {"date": "2026-05-09", "type": "lunch", "name": "江南雅厨·非遗苏州菜(李公堤店)"}, {"date": "2026-05-10", "type": "lunch", "name": "江南雅厨·非遗苏州菜(李公堤店)"}]}, {"name_key": "哑巴生煎", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-05-06", "type": "dinner", "name": "哑巴生煎(临顿路店)"}, {"date": "2026-05-07", "type": "dinner", "name": "哑巴生煎(临顿路店)"}, {"date": "2026-05-08", "type": "dinner", "name": "哑巴生煎(临顿路店)"}, {"date": "2026-05-09", "type": "dinner", "name": "哑巴生煎(临顿路店)"}, {"date": "2026-05-10", "type": "dinner", "name": "哑巴生煎(临顿路店)"}]}]}]`

### v3_harder_eval_000018
- request: 天津 2026-07-03->2026-07-05 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-07-05", "lunch": "天津卫码头(水上公园店)", "dinner": "天津卫码头(水上公园店)"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "天津卫码头", "count": 4, "max_allowed": 2, "occurrences": [{"date": "2026-07-03", "type": "dinner", "name": "天津卫码头(水上公园店)"}, {"date": "2026-07-04", "type": "dinner", "name": "天津卫码头(水上公园店)"}, {"date": "2026-07-05", "type": "lunch", "name": "天津卫码头(水上公园店)"}, {"date": "2026-07-05", "type": "dinner", "name": "天津卫码头(水上公园店)"}]}]}]`

### v3_harder_eval_000019
- request: 丽江 2026-05-08->2026-05-11 days=4 transport=打车 hotel=亲子酒店 prefs=['亲子', '老人友好', '博物馆', '城市公园', '特色餐厅']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-05-11", "lunch": "则瓦米线·云南小吃集合(一中店)", "dinner": "则瓦米线·云南小吃集合(花巷店)"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "则瓦米线·云南小吃集合", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-05-08", "type": "lunch", "name": "则瓦米线·云南小吃集合(花巷店)"}, {"date": "2026-05-09", "type": "lunch", "name": "则瓦米线·云南小吃集合(一中店)"}, {"date": "2026-05-10", "type": "dinner", "name": "则瓦米线·云南小吃集合(花巷店)"}, {"date": "2026-05-11", "type": "lunch", "name": "则瓦米线·云南小吃集合(一中店)"}, {"date": "2026-05-11", "type": "dinner", "name": "则瓦米线·云南小吃集合(花巷店)"}]}]}, {"stage": "rule", "type": "hotel_budget_underestimated", "details": {"available": true, "lodging_nights": 3, "priced_nights": 3, "expected_min_total_hotels": 2200, "reported_total_hotels": 1500, "diff": -700, "covers_nights": false}}]`

### v3_harder_eval_000022
- request: 桂林 2026-04-04->2026-04-07 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '夜市', '老字号', '城市漫步']
- errors: `[{"stage": "rule", "type": "meal_grounding_miss", "details": [{"date": "2026-04-04", "type": "dinner", "name": "民俗街夜市"}]}, {"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-04-05", "lunch": "阿甘酒家(依仁店)", "dinner": "阿甘酒家(解西店)"}, {"date": "2026-04-07", "lunch": "麦当劳(桂林临桂万达餐厅)", "dinner": "麦当劳(桂林西城南路餐厅)"}]}]`

### v3_harder_eval_000020
- request: 杭州 2026-06-18->2026-06-22 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-06-22", "lunch": "老秦凉都黄牛肉馆(滨江总店)", "dinner": "老秦凉都黄牛肉馆(滨江总店)"}]}]`

### v3_harder_eval_000025
- request: 上海 2026-08-02->2026-08-06 days=5 transport=公共交通 hotel=民宿 prefs=['摄影', '自然风光', '城市漫步', '本地菜']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-08-03", "lunch": "农家菜老大(松江店)", "dinner": "农家菜老大(九亭店)"}, {"date": "2026-08-04", "lunch": "浩海火烧云傣家菜(新天地广场店)", "dinner": "浩海火烧云傣家菜(静安芮欧店)"}]}]`

### v3_harder_eval_000023
- request: 大理 2026-09-01->2026-09-05 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-09-02", "type": "dinner", "name": "随园食单(善德居店)", "reason": "unknown_food_semantics"}, {"date": "2026-09-05", "type": "dinner", "name": "随园食单(善德居店)", "reason": "unknown_food_semantics"}]}]`

### v3_harder_eval_000028
- request: 深圳 2026-03-05->2026-03-07 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-03-05", "lunch": "欧记大排档·江西景德菜(深圳首店)", "dinner": "欧记大排档·江西景德菜(南山保利店)"}]}]`

### v3_harder_eval_000026
- request: 扬州 2026-05-08->2026-05-11 days=4 transport=自驾 hotel=亲子酒店 prefs=['亲子', '动物园', '海洋馆', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-05-09", "lunch": "大毛.淮扬菜(瘦西湖店)", "dinner": "大毛.淮扬菜(何园店)"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "大毛.淮扬菜", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-05-09", "type": "lunch", "name": "大毛.淮扬菜(瘦西湖店)"}, {"date": "2026-05-09", "type": "dinner", "name": "大毛.淮扬菜(何园店)"}, {"date": "2026-05-10", "type": "lunch", "name": "大毛.淮扬菜(兴城东路店)"}, {"date": "2026-05-11", "type": "lunch", "name": "大毛.淮扬菜(兴城东路店)"}]}]}]`

### v3_harder_eval_000029
- request: 长沙 2026-03-05->2026-03-08 days=4 transport=打车 hotel=亲子酒店 prefs=['亲子', '老人友好', '博物馆', '城市公园', '特色餐厅']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 2900, "total": 2060, "diff": 840, "requested_budget": {"available": false, "amount": 0, "scope": "unknown", "party_size": 3, "total": 0}, "per_person_day": 171.67, "budget_level": "comfortable", "arithmetic_consistent": false, "within_user_budget": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 3, "priced_nights": 3, "expected_min_total_hotels": 1500, "reported_total_hotels": 1500, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_harder_eval_000027
- request: 杭州 2026-05-06->2026-05-10 days=5 transport=公共交通 hotel=民宿 prefs=['小众展馆', '咖啡', '艺术', '城市漫步', '特色餐厅']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "杭州酒家", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-05-06", "type": "dinner", "name": "杭州酒家(延安路店)"}, {"date": "2026-05-07", "type": "dinner", "name": "杭州酒家(延安路店)"}, {"date": "2026-05-08", "type": "dinner", "name": "杭州酒家(延安路店)"}, {"date": "2026-05-09", "type": "dinner", "name": "杭州酒家(延安路店)"}, {"date": "2026-05-10", "type": "dinner", "name": "杭州酒家(延安路店)"}]}]}]`

### v3_harder_eval_000030
- request: 三亚 2026-05-08->2026-05-12 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-05-11", "type": "dinner", "name": "天涯海角游览区", "reason": "unknown_food_semantics"}, {"date": "2026-05-12", "type": "lunch", "name": "三亚湾", "reason": "unknown_food_semantics"}, {"date": "2026-05-12", "type": "dinner", "name": "三亚湾", "reason": "unknown_food_semantics"}]}, {"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-05-12", "lunch": "三亚湾", "dinner": "三亚湾"}]}]`
