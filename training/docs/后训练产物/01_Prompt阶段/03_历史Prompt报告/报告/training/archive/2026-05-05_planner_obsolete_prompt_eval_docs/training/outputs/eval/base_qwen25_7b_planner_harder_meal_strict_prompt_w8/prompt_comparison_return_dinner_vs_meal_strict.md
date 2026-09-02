# Prompt 对比：return_dinner vs meal_strict

- 旧版：`training/outputs/eval/base_qwen25_7b_v3_harder_food_bucket_return_dinner_prompt_w8`
- 新版：`training/outputs/eval/base_qwen25_7b_v3_harder_meal_strict_prompt_w8`
- 共同 record 数：300

## 总体结论

- hard_pass：84.98% (249/293) -> 81.16% (237/292)
- 旧版通过新版失败：45 条
- 旧版失败新版通过：33 条
- 两版都通过：204 条
- 两版都失败：18 条

新版的主收益是压低 `酒店晚餐/酒店午餐`，但副作用是 `无/空值` 和 `meal_complete` 问题变多，同时预算算术错误明显增多，所以 hard_pass 下降。

## 核心指标

| 指标 | 旧版 | 新版 | 旧过新不过 | 新过旧不过 |
| --- | ---: | ---: | ---: | ---: |
| `json_extract_ok` | 99.67% (299/300) | 100.00% (300/300) | 0 | 1 |
| `schema_ok` | 97.67% (293/300) | 97.33% (292/300) | 7 | 6 |
| `hard_pass` | 84.98% (249/293) | 81.16% (237/292) | 45 | 33 |
| `meal_complete` | 99.66% (292/293) | 97.95% (286/292) | 12 | 6 |
| `meal_specific_ok` | 100.00% (293/293) | 100.00% (292/292) | 7 | 6 |
| `meal_grounding_ok` | 88.74% (260/293) | 90.07% (263/292) | 27 | 30 |
| `budget_arithmetic_consistent` | 96.25% (282/293) | 92.12% (269/292) | 25 | 12 |
| `budget_level_aligned` | 98.63% (289/293) | 97.95% (286/292) | 11 | 8 |
| `budget_preference_aligned` | 98.63% (289/293) | 97.95% (286/292) | 11 | 8 |
| `hotel_budget_covers_nights` | 100.00% (293/293) | 99.66% (291/292) | 8 | 6 |
| `weather_match` | 100.00% (293/293) | 100.00% (292/292) | 7 | 6 |
| `attraction_count_ok` | 99.66% (292/293) | 100.00% (292/292) | 7 | 7 |

## Failure Types

| 类型 | 旧版 | 新版 |
| --- | ---: | ---: |
| `budget_arithmetic_inconsistent` | 11 | 23 |
| `budget_preference_mismatch` | 4 | 6 |
| `hotel_budget_underestimated` | 0 | 1 |
| `json_extract` | 1 | 0 |
| `meal_grounding_miss` | 33 | 29 |
| `schema` | 6 | 8 |

## 餐饮 Miss 细分

| 类型 | 旧版 miss 餐次 | 新版 miss 餐次 |
| --- | ---: | ---: |
| 其他未命中 | 13 | 13 |
| 无/空值 | 5 | 18 |
| 明确住宿类午晚餐 | 22 | 6 |
| 误用住宿名称 | 3 | 1 |
| 附近餐厅 | 2 | 0 |

### Top Miss Names

| 旧版 | 次数 | 新版 | 次数 |
| --- | ---: | --- | ---: |
| 酒店晚餐 | 21 | 无 | 18 |
| 无 | 5 | 酒店晚餐 | 5 |
| 门黔树老贵阳家常菜(遵义路店) | 2 | 随园食单(善德居店) | 3 |
| 秀宴•齐鲁文化美食剧场(高新店) | 2 | 门黔树老贵阳家常菜(遵义路店) | 3 |
| 民俗街夜市 | 1 | 秀宴•齐鲁文化美食剧场(高新店) | 2 |
| 长沙海底世界 | 1 | 舂Chong coffee | 1 |
| 不白吃有文化中心 | 1 | 大理古城荷花苑民宿 | 1 |
| 鼓浪屿风琴博物馆附近餐厅 | 1 | 三亚湾海居铂尔曼度假酒店餐厅 | 1 |
| 厦门园林博览苑附近餐厅 | 1 | 超级萌猩亲子乐园 | 1 |
| 酒店午餐 | 1 | Crave Bakery&Coffee | 1 |
| 舂Chong coffee | 1 | 鑫宏公寓 | 1 |
| 如愿青年旅舍(贵阳北站店) | 1 | 四季梦幻亲子乐园 | 1 |

## Hard Pass 下降主因

### 旧版通过、新版失败的错误类型

| 类型 | 条数 |
| --- | ---: |
| `meal_grounding_miss` | 21 |
| `budget_arithmetic_inconsistent` | 16 |
| `schema` | 6 |
| `unknown` | 4 |
| `hotel_budget_underestimated` | 1 |

### 旧版失败、新版通过时旧版错误类型

| 类型 | 条数 |
| --- | ---: |
| `meal_grounding_miss` | 23 |
| `budget_arithmetic_inconsistent` | 7 |
| `schema` | 2 |
| `json_extract` | 1 |

## 旧版通过、新版失败：逐条列表

| record_id | request | 新版错误 | 旧版错误 |
| --- | --- | --- | --- |
| `v3_harder_eval_000005` | 广州 2026-07-03->2026-07-07 days=5 transport=公共交通 hotel=民宿 prefs=['摄影', '自然风光', '城市漫步', '本地菜'] | meal_grounding_miss(2026-07-07:dinner:无)<br>budget_arithmetic_inconsistent(diff=930, total=2060, part_sum=2990, level=standard) | 无 |
| `v3_harder_eval_000006` | 南京 2026-07-03->2026-07-06 days=4 transport=自驾 hotel=亲子酒店 prefs=['亲子', '动物园', '海洋馆', '城市公园', '本地美食'] | meal_grounding_miss(2026-07-06:dinner:无) | 无 |
| `v3_harder_eval_000023` | 大理 2026-09-01->2026-09-05 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食'] | meal_grounding_miss(2026-09-02:dinner:随园食单(善德居店); 2026-09-05:lunch:随园食单(善德居店)) | 无 |
| `v3_harder_eval_000027` | 杭州 2026-05-06->2026-05-10 days=5 transport=公共交通 hotel=民宿 prefs=['小众展馆', '咖啡', '艺术', '城市漫步', '特色餐厅'] | meal_grounding_miss(2026-05-10:dinner:无) | 无 |
| `v3_harder_eval_000032` | 丽江 2026-05-07->2026-05-10 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '夜市', '老字号', '城市漫步'] | meal_grounding_miss(2026-05-10:dinner:酒店晚餐) | 无 |
| `v3_harder_eval_000037` | 贵阳 2026-01-04->2026-01-08 days=5 transport=公共交通 hotel=民宿 prefs=['小众展馆', '咖啡', '艺术', '城市漫步', '特色餐厅'] | budget_arithmetic_inconsistent(diff=1020, total=2060, part_sum=3080, level=comfortable) | 无 |
| `v3_harder_eval_000039` | 深圳 2025-11-05->2025-11-08 days=4 transport=打车 hotel=亲子酒店 prefs=['亲子', '老人友好', '博物馆', '城市公园', '特色餐厅'] | meal_grounding_miss(2025-11-08:dinner:无) | 无 |
| `v3_harder_eval_000051` | 昆明 2026-06-18->2026-06-21 days=4 transport=打车 hotel=高端酒店 prefs=['高端酒店', '艺术', '特色餐厅', '城市地标', '休闲慢游'] | meal_grounding_miss(2026-06-21:dinner:无) | 无 |
| `v3_harder_eval_000059` | 宁波 2026-02-03->2026-02-06 days=4 transport=打车 hotel=亲子酒店 prefs=['亲子', '老人友好', '博物馆', '城市公园', '特色餐厅'] | 无 | 无 |
| `v3_harder_eval_000085` | 北京 2026-05-06->2026-05-10 days=5 transport=公共交通 hotel=民宿 prefs=['摄影', '自然风光', '城市漫步', '本地菜'] | meal_grounding_miss(2026-05-10:dinner:无) | 无 |
| `v3_harder_eval_000089` | 深圳 2026-06-18->2026-06-21 days=4 transport=打车 hotel=亲子酒店 prefs=['亲子', '老人友好', '博物馆', '城市公园', '特色餐厅'] | meal_grounding_miss(2026-06-21:dinner:无) | 无 |
| `v3_harder_eval_000095` | 广州 2026-06-18->2026-06-22 days=5 transport=公共交通 hotel=民宿 prefs=['摄影', '自然风光', '城市漫步', '本地菜'] | budget_arithmetic_inconsistent(diff=920, total=2065, part_sum=2985, level=standard) | 无 |
| `v3_harder_eval_000097` | 张家界 2026-08-02->2026-08-06 days=5 transport=公共交通 hotel=民宿 prefs=['小众展馆', '咖啡', '艺术', '城市漫步', '特色餐厅'] | meal_grounding_miss(2026-08-06:dinner:无) | 无 |
| `v3_harder_eval_000099` | 厦门 2026-05-07->2026-05-10 days=4 transport=打车 hotel=亲子酒店 prefs=['亲子', '老人友好', '博物馆', '城市公园', '特色餐厅'] | meal_grounding_miss(2026-05-10:dinner:无) | 无 |
| `v3_harder_eval_000113` | 重庆 2026-08-02->2026-08-06 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食'] | budget_arithmetic_inconsistent(diff=1000, total=3248, part_sum=4248, level=standard) | 无 |
| `v3_harder_eval_000117` | 大理 2026-06-03->2026-06-07 days=5 transport=公共交通 hotel=民宿 prefs=['小众展馆', '咖啡', '艺术', '城市漫步', '特色餐厅'] | hotel_budget_underestimated(diff=-900, total=None, part_sum=None, level=None)<br>budget_arithmetic_inconsistent(diff=860, total=2060, part_sum=2920, level=comfortable) | 无 |
| `v3_harder_eval_000122` | 广州 2026-05-07->2026-05-10 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '夜市', '老字号', '城市漫步'] | budget_arithmetic_inconsistent(diff=1000, total=2270, part_sum=3270, level=limited) | 无 |
| `v3_harder_eval_000129` | 呼和浩特 2026-08-02->2026-08-05 days=4 transport=打车 hotel=亲子酒店 prefs=['亲子', '老人友好', '博物馆', '城市公园', '特色餐厅'] | schema(1 validation error for TripPlan<br>days.3.accommodation<br>  Input should be a valid string [type=string_type, input_value=Non) | 无 |
| `v3_harder_eval_000130` | 天津 2026-06-18->2026-06-22 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食'] | budget_arithmetic_inconsistent(diff=1000, total=3100, part_sum=4100, level=comfortable) | 无 |
| `v3_harder_eval_000147` | 桂林 2026-06-18->2026-06-22 days=5 transport=公共交通 hotel=民宿 prefs=['小众展馆', '咖啡', '艺术', '城市漫步', '特色餐厅'] | budget_arithmetic_inconsistent(diff=1100, total=2060, part_sum=3160, level=comfortable) | 无 |
| `v3_harder_eval_000162` | 上海 2026-05-05->2026-05-08 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '夜市', '老字号', '城市漫步'] | budget_arithmetic_inconsistent(diff=1000, total=2600, part_sum=3600, level=limited) | budget_preference_mismatch(diff=0, total=3480, part_sum=3480, level=limited) |
| `v3_harder_eval_000163` | 呼和浩特 2026-06-03->2026-06-07 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食'] | meal_grounding_miss(2026-06-04:dinner:酒店晚餐; 2026-06-05:dinner:酒店晚餐; 2026-06-06:dinner:酒店晚餐; 2026-06-07:dinner:酒店晚餐) | 无 |
| `v3_harder_eval_000173` | 大理 2026-09-01->2026-09-05 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食'] | schema(1 validation error for TripPlan<br>days.4.accommodation<br>  Input should be a valid string [type=string_type, input_value=Non) | 无 |
| `v3_harder_eval_000184` | 郑州 2025-08-07->2025-08-09 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆'] | schema(1 validation error for TripPlan<br>days.2.accommodation<br>  Input should be a valid string [type=string_type, input_value=Non) | 无 |
| `v3_harder_eval_000185` | 广州 2025-08-07->2025-08-11 days=5 transport=公共交通 hotel=民宿 prefs=['摄影', '自然风光', '城市漫步', '本地菜'] | meal_grounding_miss(2025-08-11:dinner:无)<br>budget_arithmetic_inconsistent(diff=930, total=2060, part_sum=2990, level=standard) | 无 |
| `v3_harder_eval_000189` | 三亚 2026-09-01->2026-09-04 days=4 transport=打车 hotel=亲子酒店 prefs=['亲子', '老人友好', '博物馆', '城市公园', '特色餐厅'] | meal_grounding_miss(2026-09-04:dinner:三亚湾海居铂尔曼度假酒店餐厅) | 无 |
| `v3_harder_eval_000195` | 广州 2026-07-03->2026-07-07 days=5 transport=公共交通 hotel=民宿 prefs=['摄影', '自然风光', '城市漫步', '本地菜'] | budget_arithmetic_inconsistent(diff=1000, total=2030, part_sum=3030, level=standard) | 无 |
| `v3_harder_eval_000196` | 深圳 2026-09-01->2026-09-04 days=4 transport=自驾 hotel=亲子酒店 prefs=['亲子', '动物园', '海洋馆', '城市公园', '本地美食'] | 无 | 无 |
| `v3_harder_eval_000203` | 昆明 2026-05-08->2026-05-12 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食'] | meal_grounding_miss(2026-05-12:dinner:无) | 无 |
| `v3_harder_eval_000204` | 杭州 2026-06-18->2026-06-20 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆'] | meal_grounding_miss(2026-06-20:dinner:无) | 无 |
| `v3_harder_eval_000215` | 桂林 2026-05-05->2026-05-09 days=5 transport=公共交通 hotel=民宿 prefs=['摄影', '自然风光', '城市漫步', '本地菜'] | budget_arithmetic_inconsistent(diff=1020, total=2060, part_sum=3080, level=standard) | 无 |
| `v3_harder_eval_000217` | 上海 2025-05-04->2025-05-08 days=5 transport=公共交通 hotel=民宿 prefs=['小众展馆', '咖啡', '艺术', '城市漫步', '特色餐厅'] | meal_grounding_miss(2025-05-05:dinner:Crave Bakery&Coffee; 2025-05-08:dinner:无) | 无 |
| `v3_harder_eval_000243` | 厦门 2025-08-07->2025-08-11 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食'] | meal_grounding_miss(2025-08-11:dinner:无) | 无 |
| `v3_harder_eval_000244` | 广州 2026-05-07->2026-05-09 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆'] | meal_grounding_miss(2026-05-09:dinner:无) | 无 |
| `v3_harder_eval_000247` | 成都 2026-02-03->2026-02-07 days=5 transport=公共交通 hotel=民宿 prefs=['小众展馆', '咖啡', '艺术', '城市漫步', '特色餐厅'] | meal_grounding_miss(2026-02-07:dinner:无) | 无 |
| `v3_harder_eval_000249` | 深圳 2026-08-02->2026-08-05 days=4 transport=打车 hotel=亲子酒店 prefs=['亲子', '老人友好', '博物馆', '城市公园', '特色餐厅'] | schema(1 validation error for TripPlan<br>days.3.accommodation<br>  Input should be a valid string [type=string_type, input_value=Non) | 无 |
| `v3_harder_eval_000256` | 深圳 2026-07-03->2026-07-06 days=4 transport=自驾 hotel=亲子酒店 prefs=['亲子', '动物园', '海洋馆', '城市公园', '本地美食'] | schema(1 validation error for TripPlan<br>days.3.accommodation<br>  Input should be a valid string [type=string_type, input_value=Non) | 无 |
| `v3_harder_eval_000266` | 重庆 2026-07-03->2026-07-06 days=4 transport=自驾 hotel=亲子酒店 prefs=['亲子', '动物园', '海洋馆', '城市公园', '本地美食'] | schema(1 validation error for TripPlan<br>days.3.accommodation<br>  Input should be a valid string [type=string_type, input_value=Non) | 无 |
| `v3_harder_eval_000277` | 北京 2026-04-27->2026-05-01 days=5 transport=公共交通 hotel=民宿 prefs=['小众展馆', '咖啡', '艺术', '城市漫步', '特色餐厅'] | budget_arithmetic_inconsistent(diff=1000, total=3000, part_sum=4000, level=comfortable) | 无 |
| `v3_harder_eval_000283` | 长沙 2025-11-05->2025-11-09 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食'] | budget_arithmetic_inconsistent(diff=1000, total=2060, part_sum=3060, level=standard) | 无 |
| `v3_harder_eval_000285` | 北京 2026-06-03->2026-06-07 days=5 transport=公共交通 hotel=民宿 prefs=['摄影', '自然风光', '城市漫步', '本地菜'] | budget_arithmetic_inconsistent(diff=900, total=2290, part_sum=3190, level=standard) | 无 |
| `v3_harder_eval_000290` | 武汉 2026-05-05->2026-05-09 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食'] | budget_arithmetic_inconsistent(diff=-1000, total=4830, part_sum=3830, level=comfortable) | 无 |
| `v3_harder_eval_000291` | 洛阳 2026-02-03->2026-02-06 days=4 transport=打车 hotel=高端酒店 prefs=['高端酒店', '艺术', '特色餐厅', '城市地标', '休闲慢游'] | 无 | 无 |
| `v3_harder_eval_000296` | 广州 2025-11-05->2025-11-08 days=4 transport=自驾 hotel=亲子酒店 prefs=['亲子', '动物园', '海洋馆', '城市公园', '本地美食'] | meal_grounding_miss(2025-11-06:lunch:四季梦幻亲子乐园) | 无 |
| `v3_harder_eval_000298` | 上海 2026-05-05->2026-05-07 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物'] | 无 | 无 |

## 旧版失败、新版通过：逐条列表

| record_id | request | 旧版错误 |
| --- | --- | --- |
| `v3_harder_eval_000014` | 成都 2026-06-03->2026-06-05 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆'] | meal_grounding_miss(2026-06-05:dinner:酒店晚餐) |
| `v3_harder_eval_000022` | 桂林 2026-04-04->2026-04-07 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '夜市', '老字号', '城市漫步'] | meal_grounding_miss(2026-04-04:dinner:民俗街夜市) |
| `v3_harder_eval_000036` | 长沙 2026-06-03->2026-06-06 days=4 transport=自驾 hotel=亲子酒店 prefs=['亲子', '动物园', '海洋馆', '城市公园', '本地美食'] | meal_grounding_miss(2026-06-03:dinner:酒店晚餐; 2026-06-04:dinner:长沙海底世界; 2026-06-06:dinner:酒店晚餐) |
| `v3_harder_eval_000038` | 厦门 2026-05-07->2026-05-09 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物'] | meal_grounding_miss(2026-05-09:dinner:酒店晚餐) |
| `v3_harder_eval_000040` | 南京 2026-07-03->2026-07-07 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食'] | budget_arithmetic_inconsistent(diff=900, total=3150, part_sum=4050, level=comfortable) |
| `v3_harder_eval_000048` | 北京 2026-01-04->2026-01-06 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物'] | meal_grounding_miss(2026-01-06:dinner:不白吃有文化中心) |
| `v3_harder_eval_000056` | 昆明 2026-05-05->2026-05-08 days=4 transport=自驾 hotel=亲子酒店 prefs=['亲子', '动物园', '海洋馆', '城市公园', '本地美食'] | meal_grounding_miss(2026-05-08:dinner:酒店晚餐) |
| `v3_harder_eval_000058` | 洛阳 2026-05-06->2026-05-08 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物'] | meal_grounding_miss(2026-05-08:dinner:酒店晚餐) |
| `v3_harder_eval_000062` | 厦门 2026-05-07->2026-05-10 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '夜市', '老字号', '城市漫步'] | meal_grounding_miss(2026-05-08:dinner:鼓浪屿风琴博物馆附近餐厅; 2026-05-09:dinner:厦门园林博览苑附近餐厅) |
| `v3_harder_eval_000063` | 深圳 2026-05-06->2026-05-10 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食'] | meal_grounding_miss(2026-05-07:dinner:酒店晚餐; 2026-05-08:dinner:酒店晚餐; 2026-05-09:dinner:酒店晚餐; 2026-05-10:lunch:酒店午餐) |
| `v3_harder_eval_000069` | 桂林 2025-11-05->2025-11-08 days=4 transport=打车 hotel=亲子酒店 prefs=['亲子', '老人友好', '博物馆', '城市公园', '特色餐厅'] | budget_arithmetic_inconsistent(diff=1000, total=2260, part_sum=3260, level=comfortable) |
| `v3_harder_eval_000075` | 杭州 2025-05-04->2025-05-08 days=5 transport=公共交通 hotel=民宿 prefs=['摄影', '自然风光', '城市漫步', '本地菜'] | meal_grounding_miss(2025-05-08:dinner:无) |
| `v3_harder_eval_000102` | 上海 2026-07-03->2026-07-06 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '夜市', '老字号', '城市漫步'] | budget_arithmetic_inconsistent(diff=820, total=2060, part_sum=2880, level=limited) |
| `v3_harder_eval_000125` | 贵阳 2026-05-06->2026-05-10 days=5 transport=公共交通 hotel=民宿 prefs=['摄影', '自然风光', '城市漫步', '本地菜'] | meal_grounding_miss(2026-05-10:dinner:如愿青年旅舍(贵阳北站店)) |
| `v3_harder_eval_000131` | 上海 2026-05-06->2026-05-09 days=4 transport=打车 hotel=高端酒店 prefs=['高端酒店', '艺术', '特色餐厅', '城市地标', '休闲慢游'] | meal_grounding_miss(2026-05-09:dinner:酒店晚餐) |
| `v3_harder_eval_000134` | 北京 2026-05-07->2026-05-09 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆'] | meal_grounding_miss(2026-05-07:dinner:酒店晚餐; 2026-05-08:dinner:酒店晚餐; 2026-05-09:dinner:酒店晚餐) |
| `v3_harder_eval_000140` | 杭州 2026-06-03->2026-06-07 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食'] | meal_grounding_miss(2026-06-07:lunch:心芝麻开门亲子乐园(东兴天地店)) |
| `v3_harder_eval_000146` | 贵阳 2026-06-18->2026-06-21 days=4 transport=自驾 hotel=亲子酒店 prefs=['亲子', '动物园', '海洋馆', '城市公园', '本地美食'] | meal_grounding_miss(2026-06-21:lunch:门黔樹老贵阳家常菜(遵义路店)) |
| `v3_harder_eval_000164` | 三亚 2025-11-05->2025-11-07 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆'] | meal_grounding_miss(2025-11-07:dinner:酒店晚餐) |
| `v3_harder_eval_000170` | 成都 2026-04-27->2026-05-01 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食'] | schema(2 validation errors for TripPlan<br>days.2.meals.1.estimated_cost<br>  Input should be a valid integer, got a number with a fr) |
| `v3_harder_eval_000188` | 泉州 2026-07-03->2026-07-05 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物'] | meal_grounding_miss(2026-07-05:dinner:港湾宾馆(南山中路店)) |
| `v3_harder_eval_000193` | 厦门 2026-05-07->2026-05-11 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食'] | meal_grounding_miss(2026-05-11:dinner:无) |
| `v3_harder_eval_000208` | 济南 2026-07-03->2026-07-05 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物'] | meal_grounding_miss(2026-07-03:dinner:秀宴•齐鲁文化美食剧场(高新店)) |
| `v3_harder_eval_000209` | 三亚 2026-06-03->2026-06-06 days=4 transport=打车 hotel=亲子酒店 prefs=['亲子', '老人友好', '博物馆', '城市公园', '特色餐厅'] | meal_grounding_miss(2026-06-06:dinner:三亚七色海民宿) |
| `v3_harder_eval_000226` | 西安 2025-11-05->2025-11-08 days=4 transport=自驾 hotel=亲子酒店 prefs=['亲子', '动物园', '海洋馆', '城市公园', '本地美食'] | json_extract(响应中未找到完整的顶层TripPlan JSON对象) |
| `v3_harder_eval_000238` | 上海 2026-08-02->2026-08-04 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物'] | meal_grounding_miss(2026-08-04:dinner:酒店晚餐) |
| `v3_harder_eval_000240` | 重庆 2026-05-08->2026-05-12 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食'] | budget_arithmetic_inconsistent(diff=1000, total=3200, part_sum=4200, level=comfortable) |
| `v3_harder_eval_000248` | 杭州 2026-08-02->2026-08-04 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物'] | budget_arithmetic_inconsistent(diff=-1000, total=4980, part_sum=3980, level=comfortable) |
| `v3_harder_eval_000262` | 长沙 2026-05-08->2026-05-11 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '夜市', '老字号', '城市漫步'] | meal_grounding_miss(2026-05-09:dinner:酒店晚餐) |
| `v3_harder_eval_000268` | 丽江 2026-06-18->2026-06-20 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物'] | meal_grounding_miss(2026-06-19:lunch:兰岚·云南菜·bistro) |
| `v3_harder_eval_000269` | 青岛 2026-05-07->2026-05-10 days=4 transport=打车 hotel=亲子酒店 prefs=['亲子', '老人友好', '博物馆', '城市公园', '特色餐厅'] | budget_arithmetic_inconsistent(diff=-1620, total=7760, part_sum=6140, level=comfortable) |
| `v3_harder_eval_000279` | 昆明 2025-05-04->2025-05-07 days=4 transport=打车 hotel=亲子酒店 prefs=['亲子', '老人友好', '博物馆', '城市公园', '特色餐厅'] | schema(1 validation error for TripPlan<br>days.3.accommodation<br>  Input should be a valid string [type=string_type, input_value=Non) |
| `v3_harder_eval_000292` | 济南 2026-04-20->2026-04-23 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '夜市', '老字号', '城市漫步'] | budget_arithmetic_inconsistent(diff=1000, total=2264, part_sum=3264, level=limited) |

## 两版都失败但错误变化

| record_id | request | 旧版错误 | 新版错误 |
| --- | --- | --- | --- |
| `v3_harder_eval_000083` | 成都 2026-08-02->2026-08-06 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食'] | schema(1 validation error for TripPlan<br>days.4.accommodation<br>  Input should be a valid string [type=string_type, input_value=Non) | budget_arithmetic_inconsistent(diff=1000, total=3730, part_sum=4730, level=standard) |
| `v3_harder_eval_000093` | 贵阳 2026-05-07->2026-05-11 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食'] | meal_grounding_miss(2026-05-08:dinner:门黔树老贵阳家常菜(遵义路店); 2026-05-10:lunch:门黔树老贵阳家常菜(遵义路店)) | meal_grounding_miss(2026-05-09:lunch:门黔树老贵阳家常菜(遵义路店); 2026-05-10:lunch:门黔树老贵阳家常菜(遵义路店); 2026-05-11:lunch:门黔树老贵阳家常菜(遵义路店)) |
| `v3_harder_eval_000103` | 扬州 2026-05-05->2026-05-09 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食'] | meal_grounding_miss(2026-05-09:dinner:酒店晚餐) | budget_arithmetic_inconsistent(diff=1200, total=3840, part_sum=5040, level=standard) |
| `v3_harder_eval_000128` | 济南 2026-05-08->2026-05-10 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物'] | meal_grounding_miss(2026-05-08:dinner:秀宴•齐鲁文化美食剧场(高新店)) | meal_grounding_miss(2026-05-08:lunch:秀宴•齐鲁文化美食剧场(高新店); 2026-05-08:dinner:秀宴•齐鲁文化美食剧场(高新店)) |
| `v3_harder_eval_000139` | 大理 2026-06-18->2026-06-21 days=4 transport=打车 hotel=亲子酒店 prefs=['亲子', '老人友好', '博物馆', '城市公园', '特色餐厅'] | meal_grounding_miss(2026-06-19:dinner:步云山·大理白族特色餐厅; 2026-06-20:lunch:随园食单(善德居店); 2026-06-21:dinner:酒店晚餐) | meal_grounding_miss(2026-06-20:dinner:随园食单(善德居店); 2026-06-21:dinner:大理古城荷花苑民宿) |
| `v3_harder_eval_000150` | 张家界 2026-05-08->2026-05-12 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食'] | budget_arithmetic_inconsistent(diff=1000, total=3200, part_sum=4200, level=comfortable) | budget_arithmetic_inconsistent(diff=1000, total=3050, part_sum=4050, level=comfortable) |
| `v3_harder_eval_000161` | 杭州 2026-04-04->2026-04-07 days=4 transport=打车 hotel=高端酒店 prefs=['高端酒店', '艺术', '特色餐厅', '城市地标', '休闲慢游'] | meal_grounding_miss(2026-04-07:dinner:无) | schema(1 validation error for TripPlan<br>days.3.accommodation<br>  Input should be a valid string [type=string_type, input_value=Non) |
| `v3_harder_eval_000179` | 大理 2026-06-18->2026-06-21 days=4 transport=打车 hotel=亲子酒店 prefs=['亲子', '老人友好', '博物馆', '城市公园', '特色餐厅'] | schema(1 validation error for TripPlan<br>days.3.accommodation<br>  Input should be a valid string [type=string_type, input_value=Non) | meal_grounding_miss(2026-06-21:dinner:无) |
| `v3_harder_eval_000206` | 北京 2026-04-30->2026-05-03 days=4 transport=自驾 hotel=亲子酒店 prefs=['亲子', '动物园', '海洋馆', '城市公园', '本地美食'] | meal_grounding_miss(2026-05-03:dinner:酒店晚餐) | meal_grounding_miss(2026-05-03:dinner:超级萌猩亲子乐园) |
| `v3_harder_eval_000222` | 深圳 2026-01-04->2026-01-07 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '夜市', '老字号', '城市漫步'] | meal_grounding_miss(2026-01-07:dinner:酒店晚餐)<br>budget_arithmetic_inconsistent(diff=1000, total=3000, part_sum=4000, level=limited)<br>budget_preference_mismatch(diff=1000, total=3000, part_sum=4000, level=limited) | budget_arithmetic_inconsistent(diff=1008, total=2496, part_sum=3504, level=limited) |
| `v3_harder_eval_000231` | 杭州 2026-07-03->2026-07-06 days=4 transport=打车 hotel=高端酒店 prefs=['高端酒店', '艺术', '特色餐厅', '城市地标', '休闲慢游'] | schema(1 validation error for TripPlan<br>days.3.accommodation<br>  Input should be a valid string [type=string_type, input_value=Non) | meal_grounding_miss(2026-07-06:dinner:无) |
| `v3_harder_eval_000235` | 广州 2026-08-02->2026-08-06 days=5 transport=公共交通 hotel=民宿 prefs=['摄影', '自然风光', '城市漫步', '本地菜'] | meal_grounding_miss(2026-08-06:dinner:无) | budget_arithmetic_inconsistent(diff=1000, total=2030, part_sum=3030, level=standard) |
| `v3_harder_eval_000255` | 厦门 2026-06-03->2026-06-07 days=5 transport=公共交通 hotel=民宿 prefs=['摄影', '自然风光', '城市漫步', '本地菜'] | meal_grounding_miss(2026-06-07:dinner:无) | meal_grounding_miss(2026-06-07:dinner:鑫宏公寓) |
| `v3_harder_eval_000280` | 重庆 2026-08-02->2026-08-06 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食'] | budget_arithmetic_inconsistent(diff=1000, total=3440, part_sum=4440, level=comfortable) | budget_arithmetic_inconsistent(diff=1000, total=3200, part_sum=4200, level=comfortable) |