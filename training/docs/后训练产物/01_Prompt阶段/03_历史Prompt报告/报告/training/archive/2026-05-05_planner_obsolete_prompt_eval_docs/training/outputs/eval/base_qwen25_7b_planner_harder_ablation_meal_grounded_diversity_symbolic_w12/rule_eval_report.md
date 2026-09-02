# Rule Eval Report: base_qwen25_7b_v3_harder_ablation_meal_grounded_diversity_symbolic_w12

- records: 300
- generations: `training/outputs/eval/base_qwen25_7b_v3_harder_ablation_meal_grounded_diversity_symbolic_w12/generations.jsonl`
- records_path: `training/data/v3/eval_harder_food_bucket_meal_diversity_ablation_meal_grounded_diversity_symbolic_no_route/records.jsonl`

## Boolean Metrics

| Metric | Pass | Total | Rate |
| --- | ---: | ---: | ---: |
| attraction_count_ok | 296 | 298 | 99.33% |
| attraction_grounding_ok | 293 | 298 | 98.32% |
| budget_arithmetic_consistent | 271 | 298 | 90.94% |
| budget_consistent | 271 | 298 | 90.94% |
| budget_level_aligned | 290 | 298 | 97.32% |
| budget_preference_aligned | 290 | 298 | 97.32% |
| budget_within_user_budget | 298 | 298 | 100.00% |
| city_ok | 298 | 298 | 100.00% |
| date_range_ok | 298 | 298 | 100.00% |
| day_dates_ok | 298 | 298 | 100.00% |
| day_index_ok | 298 | 298 | 100.00% |
| days_len_ok | 298 | 298 | 100.00% |
| dpo_soft_pass | 119 | 298 | 39.93% |
| hard_pass | 241 | 298 | 80.87% |
| hotel_budget_covers_nights | 297 | 298 | 99.66% |
| hotel_distance_placeholder_ok | 298 | 298 | 100.00% |
| hotel_grounding_ok | 297 | 298 | 99.66% |
| invalid_hotel_name_ok | 298 | 298 | 100.00% |
| json_extract_ok | 300 | 300 | 100.00% |
| legacy_hard_pass | 124 | 298 | 41.61% |
| location_object_ok | 298 | 298 | 100.00% |
| meal_complete | 297 | 298 | 99.66% |
| meal_diversity_ok | 150 | 298 | 50.34% |
| meal_grounding_ok | 270 | 298 | 90.60% |
| meal_lunch_dinner_same_day_ok | 208 | 298 | 69.80% |
| meal_repeat_limit_ok | 191 | 298 | 64.09% |
| meal_specific_ok | 298 | 298 | 100.00% |
| meal_valid_semantics_ok | 275 | 298 | 92.28% |
| middle_hotel_ok | 296 | 298 | 99.33% |
| schema_ok | 298 | 300 | 99.33% |
| sft_hard_pass | 241 | 298 | 80.87% |
| weather_dates_ok | 298 | 298 | 100.00% |
| weather_match | 298 | 298 | 100.00% |

## Numeric Metrics

```json
{
  "attraction_grounding_rate": {
    "avg": 0.998,
    "p50": 1.0,
    "p90": 1.0
  },
  "hotel_grounding_rate": {
    "avg": 0.9966,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_diversity_unique_rate": {
    "avg": 0.689,
    "p50": 0.75,
    "p90": 1.0
  },
  "meal_food_pois_grounding_rate": {
    "avg": 0.9906,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_grounding_rate": {
    "avg": 0.9906,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_semantic_valid_rate": {
    "avg": 0.992,
    "p50": 1.0,
    "p90": 1.0
  }
}
```

## Failure Types

```json
{
  "meal_repeat_too_many": 107,
  "meal_same_day_lunch_dinner_repeat": 90,
  "budget_arithmetic_inconsistent": 27,
  "meal_invalid_name": 23,
  "budget_preference_mismatch": 8,
  "meal_grounding_miss": 5,
  "schema": 2,
  "middle_hotel_null": 2,
  "hotel_budget_underestimated": 1
}
```

## Failure Examples

### v3_harder_eval_000001
- request: 桂林 2026-09-01->2026-09-04 days=4 transport=打车 hotel=高端酒店 prefs=['高端酒店', '艺术', '特色餐厅', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-09-02", "type": "dinner", "name": "桂林山水甲天下", "reason": "unknown_food_semantics"}, {"date": "2026-09-03", "type": "dinner", "name": "桂林山水甲天下", "reason": "unknown_food_semantics"}, {"date": "2026-09-04", "type": "dinner", "name": "酒店晚餐", "reason": "generic_lodging_meal"}]}]`

### v3_harder_eval_000005
- request: 广州 2026-07-03->2026-07-07 days=5 transport=公共交通 hotel=民宿 prefs=['摄影', '自然风光', '城市漫步', '本地菜']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-07-07", "lunch": "滋粥楼·顺德菜(南村万博长隆商圈店)", "dinner": "滋粥楼·顺德菜(番禺广场总店)"}]}, {"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 2980, "total": 2080, "diff": 900, "requested_budget": {"available": false, "amount": 0, "scope": "unknown", "party_size": 1, "total": 0}, "per_person_day": 416.0, "budget_level": "standard", "arithmetic_consistent": false, "within_user_budget": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 4, "priced_nights": 4, "expected_min_total_hotels": 1200, "reported_total_hotels": 1200, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_harder_eval_000000
- request: 昆明 2026-04-04->2026-04-08 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "晨曦豆花米线", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-04-04", "type": "breakfast", "name": "晨曦豆花米线"}, {"date": "2026-04-05", "type": "breakfast", "name": "晨曦豆花米线"}, {"date": "2026-04-06", "type": "breakfast", "name": "晨曦豆花米线"}, {"date": "2026-04-07", "type": "breakfast", "name": "晨曦豆花米线"}, {"date": "2026-04-08", "type": "breakfast", "name": "晨曦豆花米线"}]}]}]`

### v3_harder_eval_000003
- request: 西安 2025-05-04->2025-05-08 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "魏家凉皮", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2025-05-04", "type": "breakfast", "name": "魏家凉皮(西大街店)"}, {"date": "2025-05-05", "type": "breakfast", "name": "魏家凉皮(西大街店)"}, {"date": "2025-05-06", "type": "breakfast", "name": "魏家凉皮(西大街店)"}, {"date": "2025-05-07", "type": "breakfast", "name": "魏家凉皮(西大街店)"}, {"date": "2025-05-08", "type": "breakfast", "name": "魏家凉皮(西大街店)"}]}, {"name_key": "李志贤灌汤包子", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2025-05-04", "type": "lunch", "name": "李志贤灌汤包子"}, {"date": "2025-05-05", "type": "lunch", "name": "李志贤灌汤包子"}, {"date": "2025-05-06", "type": "lunch", "name": "李志贤灌汤包子"}, {"date": "2025-05-07", "type": "lunch", "name": "李志贤灌汤包子"}, {"date": "2025-05-08", "type": "lunch", "name": "李志贤灌汤包子"}]}, {"name_key": "崔少野猫耳朵炒面", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2025-05-04", "type": "dinner", "name": "崔少野猫耳朵炒面(十里锦绣店)"}, {"date": "2025-05-05", "type": "dinner", "name": "崔少野猫耳朵炒面(十里锦绣店)"}, {"date": "2025-05-06", "type": "dinner", "name": "崔少野猫耳朵炒面(十里锦绣店)"}, {"date": "2025-05-07", "type": "dinner", "name": "崔少野猫耳朵炒面(十里锦绣店)"}, {"date": "2025-05-08", "type": "dinner", "name": "崔少野猫耳朵炒面(十里锦绣店)"}]}]}]`

### v3_harder_eval_000010
- request: 西安 2026-04-20->2026-04-24 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-04-24", "lunch": "清真刚刚烤肉(芙蓉街店)", "dinner": "清真刚刚烤肉(芙蓉街店)"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "清真刚刚烤肉", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-04-22", "type": "dinner", "name": "清真刚刚烤肉(芙蓉街店)"}, {"date": "2026-04-23", "type": "dinner", "name": "清真刚刚烤肉(芙蓉街店)"}, {"date": "2026-04-24", "type": "lunch", "name": "清真刚刚烤肉(芙蓉街店)"}, {"date": "2026-04-24", "type": "dinner", "name": "清真刚刚烤肉(芙蓉街店)"}]}]}]`

### v3_harder_eval_000012
- request: 洛阳 2025-05-04->2025-05-07 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '夜市', '老字号', '城市漫步']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2025-05-04", "lunch": "洛阳十字街小吃一条街", "dinner": "洛阳十字街小吃一条街"}, {"date": "2025-05-05", "lunch": "小街天府", "dinner": "小街天府"}, {"date": "2025-05-06", "lunch": "光头东烙馍村·水席洛阳菜(火车站店)", "dinner": "光头东烙馍村·水席洛阳菜(火车站店)"}, {"date": "2025-05-07", "lunch": "必胜客(正大广场店)", "dinner": "必胜客(正大广场店)"}]}, {"stage": "rule", "type": "budget_preference_mismatch", "details": {"part_sum": 3440, "total": 3440, "diff": 0, "requested_budget": {"available": false, "amount": 0, "scope": "unknown", "party_size": 2, "total": 0}, "per_person_day": 430.0, "budget_level": "limited", "arithmetic_consistent": true, "within_user_budget": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 3, "priced_nights": 3, "expected_min_total_hotels": 700, "reported_total_hotels": 1200, "diff": 500, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_harder_eval_000019
- request: 丽江 2026-05-08->2026-05-11 days=4 transport=打车 hotel=亲子酒店 prefs=['亲子', '老人友好', '博物馆', '城市公园', '特色餐厅']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-05-08", "lunch": "则瓦米线·云南小吃集合(花巷店)", "dinner": "则瓦米线·云南小吃集合(花巷店)"}, {"date": "2026-05-09", "lunch": "则瓦米线·云南小吃集合(花巷店)", "dinner": "则瓦米线·云南小吃集合(花巷店)"}, {"date": "2026-05-10", "lunch": "则瓦米线·云南小吃集合(花巷店)", "dinner": "则瓦米线·云南小吃集合(花巷店)"}, {"date": "2026-05-11", "lunch": "则瓦米线·云南小吃集合(花巷店)", "dinner": "则瓦米线·云南小吃集合(花巷店)"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "则瓦米线·云南小吃集合", "count": 8, "max_allowed": 3, "occurrences": [{"date": "2026-05-08", "type": "lunch", "name": "则瓦米线·云南小吃集合(花巷店)"}, {"date": "2026-05-08", "type": "dinner", "name": "则瓦米线·云南小吃集合(花巷店)"}, {"date": "2026-05-09", "type": "lunch", "name": "则瓦米线·云南小吃集合(花巷店)"}, {"date": "2026-05-09", "type": "dinner", "name": "则瓦米线·云南小吃集合(花巷店)"}, {"date": "2026-05-10", "type": "lunch", "name": "则瓦米线·云南小吃集合(花巷店)"}, {"date": "2026-05-10", "type": "dinner", "name": "则瓦米线·云南小吃集合(花巷店)"}, {"date": "2026-05-11", "type": "lunch", "name": "则瓦米线·云南小吃集合(花巷店)"}, {"date": "2026-05-11", "type": "dinner", "name": "则瓦米线·云南小吃集合(花巷店)"}]}]}]`

### v3_harder_eval_000017
- request: 苏州 2026-05-06->2026-05-10 days=5 transport=公共交通 hotel=民宿 prefs=['小众展馆', '咖啡', '艺术', '城市漫步', '特色餐厅']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "秋娟馄饨店", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-05-06", "type": "breakfast", "name": "秋娟馄饨店"}, {"date": "2026-05-07", "type": "breakfast", "name": "秋娟馄饨店"}, {"date": "2026-05-08", "type": "breakfast", "name": "秋娟馄饨店"}, {"date": "2026-05-09", "type": "breakfast", "name": "秋娟馄饨店"}, {"date": "2026-05-10", "type": "breakfast", "name": "秋娟馄饨店"}]}, {"name_key": "江南雅厨·非遗苏州菜", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-05-06", "type": "lunch", "name": "江南雅厨·非遗苏州菜(李公堤店)"}, {"date": "2026-05-08", "type": "lunch", "name": "江南雅厨·非遗苏州菜(李公堤店)"}, {"date": "2026-05-09", "type": "lunch", "name": "江南雅厨·非遗苏州菜(李公堤店)"}, {"date": "2026-05-10", "type": "lunch", "name": "江南雅厨·非遗苏州菜(李公堤店)"}]}, {"name_key": "哑巴生煎", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-05-06", "type": "dinner", "name": "哑巴生煎(临顿路店)"}, {"date": "2026-05-07", "type": "dinner", "name": "哑巴生煎(临顿路店)"}, {"date": "2026-05-08", "type": "dinner", "name": "哑巴生煎(临顿路店)"}, {"date": "2026-05-09", "type": "dinner", "name": "哑巴生煎(临顿路店)"}, {"date": "2026-05-10", "type": "dinner", "name": "哑巴生煎(临顿路店)"}]}]}]`

### v3_harder_eval_000013
- request: 武汉 2026-05-06->2026-05-10 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-05-08", "lunch": "刘聋子牛肉粉馆(汉阳龙兴东街店)", "dinner": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}, {"date": "2026-05-09", "lunch": "刘聋子牛肉粉馆(汉阳龙兴东街店)", "dinner": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}, {"date": "2026-05-10", "lunch": "刘聋子牛肉粉馆(汉阳龙兴东街店)", "dinner": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "刘聋子牛肉粉馆", "count": 8, "max_allowed": 3, "occurrences": [{"date": "2026-05-06", "type": "dinner", "name": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}, {"date": "2026-05-07", "type": "dinner", "name": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}, {"date": "2026-05-08", "type": "lunch", "name": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}, {"date": "2026-05-08", "type": "dinner", "name": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}, {"date": "2026-05-09", "type": "lunch", "name": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}, {"date": "2026-05-09", "type": "dinner", "name": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}, {"date": "2026-05-10", "type": "lunch", "name": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}, {"date": "2026-05-10", "type": "dinner", "name": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}]}]}]`

### v3_harder_eval_000018
- request: 天津 2026-07-03->2026-07-05 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "天津卫码头", "count": 3, "max_allowed": 2, "occurrences": [{"date": "2026-07-03", "type": "dinner", "name": "天津卫码头(水上公园店)"}, {"date": "2026-07-04", "type": "dinner", "name": "天津卫码头(水上公园店)"}, {"date": "2026-07-05", "type": "dinner", "name": "天津卫码头(水上公园店)"}]}]}]`

### v3_harder_eval_000022
- request: 桂林 2026-04-04->2026-04-07 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '夜市', '老字号', '城市漫步']
- errors: `[{"stage": "rule", "type": "meal_grounding_miss", "details": [{"date": "2026-04-04", "type": "dinner", "name": "民俗街夜市"}]}, {"stage": "rule", "type": "budget_preference_mismatch", "details": {"part_sum": 3800, "total": 3800, "diff": 0, "requested_budget": {"available": false, "amount": 0, "scope": "unknown", "party_size": 2, "total": 0}, "per_person_day": 475.0, "budget_level": "limited", "arithmetic_consistent": true, "within_user_budget": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 3, "priced_nights": 3, "expected_min_total_hotels": 600, "reported_total_hotels": 600, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_harder_eval_000020
- request: 杭州 2026-06-18->2026-06-22 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-06-20", "lunch": "老姑东北人(立涛园店)", "dinner": "老姑东北人(立涛园店)"}, {"date": "2026-06-21", "lunch": "老姑东北人(立涛园店)", "dinner": "老姑东北人(立涛园店)"}, {"date": "2026-06-22", "lunch": "老姑东北人(立涛园店)", "dinner": "老姑东北人(立涛园店)"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "老姑东北人", "count": 8, "max_allowed": 3, "occurrences": [{"date": "2026-06-18", "type": "dinner", "name": "老姑东北人(立涛园店)"}, {"date": "2026-06-19", "type": "dinner", "name": "老姑东北人(立涛园店)"}, {"date": "2026-06-20", "type": "lunch", "name": "老姑东北人(立涛园店)"}, {"date": "2026-06-20", "type": "dinner", "name": "老姑东北人(立涛园店)"}, {"date": "2026-06-21", "type": "lunch", "name": "老姑东北人(立涛园店)"}, {"date": "2026-06-21", "type": "dinner", "name": "老姑东北人(立涛园店)"}, {"date": "2026-06-22", "type": "lunch", "name": "老姑东北人(立涛园店)"}, {"date": "2026-06-22", "type": "dinner", "name": "老姑东北人(立涛园店)"}]}]}]`

### v3_harder_eval_000023
- request: 大理 2026-09-01->2026-09-05 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-09-02", "type": "dinner", "name": "随园食单(善德居店)", "reason": "unknown_food_semantics"}, {"date": "2026-09-04", "type": "dinner", "name": "随园食单(善德居店)", "reason": "unknown_food_semantics"}]}]`

### v3_harder_eval_000026
- request: 扬州 2026-05-08->2026-05-11 days=4 transport=自驾 hotel=亲子酒店 prefs=['亲子', '动物园', '海洋馆', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-05-09", "lunch": "大毛.淮扬菜(瘦西湖店)", "dinner": "大毛.淮扬菜(何园店)"}, {"date": "2026-05-11", "lunch": "大毛·淮扬菜(兴城东路店)", "dinner": "大毛·淮扬菜(兴城东路店)"}]}]`

### v3_harder_eval_000031
- request: 成都 2026-05-08->2026-05-11 days=4 transport=打车 hotel=高端酒店 prefs=['高端酒店', '艺术', '特色餐厅', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "meal_invalid_name", "details": [{"date": "2026-05-11", "type": "dinner", "name": "酒店晚餐", "reason": "generic_lodging_meal"}]}]`

### v3_harder_eval_000027
- request: 杭州 2026-05-06->2026-05-10 days=5 transport=公共交通 hotel=民宿 prefs=['小众展馆', '咖啡', '艺术', '城市漫步', '特色餐厅']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "杭州酒家", "count": 5, "max_allowed": 3, "occurrences": [{"date": "2026-05-06", "type": "dinner", "name": "杭州酒家(延安路店)"}, {"date": "2026-05-07", "type": "dinner", "name": "杭州酒家(延安路店)"}, {"date": "2026-05-08", "type": "dinner", "name": "杭州酒家(延安路店)"}, {"date": "2026-05-09", "type": "dinner", "name": "杭州酒家(延安路店)"}, {"date": "2026-05-10", "type": "dinner", "name": "杭州酒家(延安路店)"}]}]}]`

### v3_harder_eval_000030
- request: 三亚 2026-05-08->2026-05-12 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-05-09", "lunch": "创味·民间海南菜(南山店)", "dinner": "创味·民间海南菜(南山店)"}, {"date": "2026-05-11", "lunch": "创味·民间海南菜(南山店)", "dinner": "创味·民间海南菜(南山店)"}, {"date": "2026-05-12", "lunch": "疍家佬味道·海南船家菜(亚龙湾店)", "dinner": "疍家佬味道·海南船家菜(亚龙湾店)"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "创味·民间海南菜", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-05-09", "type": "lunch", "name": "创味·民间海南菜(南山店)"}, {"date": "2026-05-09", "type": "dinner", "name": "创味·民间海南菜(南山店)"}, {"date": "2026-05-11", "type": "lunch", "name": "创味·民间海南菜(南山店)"}, {"date": "2026-05-11", "type": "dinner", "name": "创味·民间海南菜(南山店)"}]}]}]`

### v3_harder_eval_000032
- request: 丽江 2026-05-07->2026-05-10 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '夜市', '老字号', '城市漫步']
- errors: `[{"stage": "rule", "type": "budget_arithmetic_inconsistent", "details": {"part_sum": 2492, "total": 1692, "diff": 800, "requested_budget": {"available": false, "amount": 0, "scope": "unknown", "party_size": 2, "total": 0}, "per_person_day": 211.5, "budget_level": "limited", "arithmetic_consistent": false, "within_user_budget": true, "level_aligned": true, "preference_aligned": true, "hotel_budget": {"available": true, "lodging_nights": 3, "priced_nights": 3, "expected_min_total_hotels": 900, "reported_total_hotels": 900, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`

### v3_harder_eval_000034
- request: 武汉 2026-06-03->2026-06-05 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆']
- errors: `[{"stage": "rule", "type": "meal_same_day_lunch_dinner_repeat", "details": [{"date": "2026-06-05", "lunch": "刘聋子牛肉粉馆(汉阳龙兴东街店)", "dinner": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}]}, {"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "刘聋子牛肉粉馆", "count": 4, "max_allowed": 2, "occurrences": [{"date": "2026-06-03", "type": "lunch", "name": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}, {"date": "2026-06-04", "type": "dinner", "name": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}, {"date": "2026-06-05", "type": "lunch", "name": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}, {"date": "2026-06-05", "type": "dinner", "name": "刘聋子牛肉粉馆(汉阳龙兴东街店)"}]}]}]`

### v3_harder_eval_000036
- request: 长沙 2026-06-03->2026-06-06 days=4 transport=自驾 hotel=亲子酒店 prefs=['亲子', '动物园', '海洋馆', '城市公园', '本地美食']
- errors: `[{"stage": "rule", "type": "meal_repeat_too_many", "details": [{"name_key": "四方坪三十栋饭店", "count": 4, "max_allowed": 3, "occurrences": [{"date": "2026-06-03", "type": "dinner", "name": "四方坪三十栋饭店(五一广场店)"}, {"date": "2026-06-04", "type": "lunch", "name": "四方坪三十栋饭店(五一广场店)"}, {"date": "2026-06-05", "type": "lunch", "name": "四方坪三十栋饭店(五一广场店)"}, {"date": "2026-06-06", "type": "lunch", "name": "四方坪三十栋饭店(五一广场店)"}]}]}]`
