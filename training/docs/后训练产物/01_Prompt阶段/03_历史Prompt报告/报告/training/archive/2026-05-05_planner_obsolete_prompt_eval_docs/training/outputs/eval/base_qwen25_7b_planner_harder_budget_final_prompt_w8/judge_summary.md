# LLM Judge Summary

```json
{
  "total": 300,
  "judged": 290,
  "skipped": 10,
  "judge_coverage": 0.9667,
  "skip_reason_counts": {
    "json_extract": 2,
    "judge_failed": 7,
    "schema": 1
  },
  "scores_avg": {
    "preference_satisfaction": 2.3138,
    "practicality": 1.9069,
    "grounding_faithfulness": 3.3552,
    "budget_reasonableness": 1.5931,
    "coherence": 2.0828,
    "overall_quality": 1.8241
  }
}
```

## Low Score Examples

### v3_harder_eval_000010
- overall: 0
- request: 西安 2026-04-19->2026-04-23 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- issues: ['响应中未找到完整的顶层TripPlan JSON对象']
- rationale: 输出未通过 JSON/schema 基础解析，直接记为无效输出。

### v3_harder_eval_000032
- overall: 0
- request: 丽江 2026-05-06->2026-05-09 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '夜市', '老字号', '城市漫步']
- issues: ['模型输出中没有 JSON 起始符']
- rationale: LLM judge 多次未返回可解析 JSON 或调用失败，本条记为 judge_failed。

### v3_harder_eval_000072
- overall: 0
- request: 哈尔滨 2026-05-04->2026-05-07 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '夜市', '老字号', '城市漫步']
- issues: ['模型输出中没有 JSON 起始符']
- rationale: LLM judge 多次未返回可解析 JSON 或调用失败，本条记为 judge_failed。

### v3_harder_eval_000201
- overall: 0
- request: 贵阳 2026-02-02->2026-02-05 days=4 transport=打车 hotel=高端酒店 prefs=['高端酒店', '艺术', '特色餐厅', '城市地标', '休闲慢游']
- issues: ['8 validation errors for TripPlan\ndays.3.hotel.name\n  Input should be a valid string [type=string_type, input_value=None, input_type=NoneType]\n    For further information visit https://errors.pydantic.dev/2.12/v/string_type\ndays.3.hotel.address\n  Input should be a valid string [type=string_type, input_value=None, input_type=NoneType]\n    For further information visit https://errors.pydantic.dev/2.12/v/string_type\ndays.3.hotel.location.longitude\n  Input should be a valid number [type=float_type, input_value=None, input_type=NoneType]\n    For further information visit https://errors.pydantic.dev/2.12/v/float_type\ndays.3.hotel.location.latitude\n  Input should be a valid number [type=float_type, input_value=None, input_type=NoneType]\n    For further information visit https://errors.pydantic.dev/2.12/v/float_type\ndays.3.hotel.price_range\n  Input should be a valid string [type=string_type, input_value=None, input_type=NoneType]\n    For further information visit https://errors.pydantic.dev/2.12/v/string_type\ndays.3.hotel.rating\n  Input should be a valid string [type=string_type, input_value=None, input_type=NoneType]\n    For further information visit https://errors.pydantic.dev/2.12/v/string_type\ndays.3.hotel.distance\n  Input should be a valid string [type=string_type, input_value=None, input_type=NoneType]\n    For further information visit https://errors.pydantic.dev/2.12/v/string_type\ndays.3.hotel.type\n  Input should be a valid string [type=string_type, input_value=None, input_type=NoneType]\n    For further information visit https://errors.pydantic.dev/2.12/v/string_type']
- rationale: 输出未通过 JSON/schema 基础解析，直接记为无效输出。

### v3_harder_eval_000220
- overall: 0
- request: 大连 2026-06-02->2026-06-06 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- issues: ['响应中未找到完整的顶层TripPlan JSON对象']
- rationale: 输出未通过 JSON/schema 基础解析，直接记为无效输出。

### v3_harder_eval_000112
- overall: 0
- request: 大连 2026-02-02->2026-02-05 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '夜市', '老字号', '城市漫步']
- issues: ['模型输出中没有 JSON 起始符']
- rationale: LLM judge 多次未返回可解析 JSON 或调用失败，本条记为 judge_failed。

### v3_harder_eval_000251
- overall: 0
- request: 济南 2026-07-02->2026-07-05 days=4 transport=打车 hotel=高端酒店 prefs=['高端酒店', '艺术', '特色餐厅', '城市地标', '休闲慢游']
- issues: ['模型输出中没有 JSON 起始符']
- rationale: LLM judge 多次未返回可解析 JSON 或调用失败，本条记为 judge_failed。

### v3_harder_eval_000283
- overall: 0
- request: 长沙 2025-11-04->2025-11-08 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食']
- issues: ["Expecting ',' delimiter: line 16 column 4 (char 432)"]
- rationale: LLM judge 多次未返回可解析 JSON 或调用失败，本条记为 judge_failed。

### v3_harder_eval_000288
- overall: 0
- request: 深圳 2026-05-07->2026-05-09 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物']
- issues: ['模型输出中没有 JSON 起始符']
- rationale: LLM judge 多次未返回可解析 JSON 或调用失败，本条记为 judge_failed。

### v3_harder_eval_000298
- overall: 0
- request: 上海 2026-05-04->2026-05-06 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物']
- issues: ['模型输出中没有 JSON 起始符']
- rationale: LLM judge 多次未返回可解析 JSON 或调用失败，本条记为 judge_failed。

### v3_harder_eval_000007
- overall: 1.0
- request: 成都 2026-05-07->2026-05-11 days=5 transport=公共交通 hotel=民宿 prefs=['小众展馆', '咖啡', '艺术', '城市漫步', '特色餐厅']
- issues: ['每日更换远离市区的民宿，交通极度不便且与现实脱节', '景点选择集中在热门经典（武侯祠、熊猫基地、宽窄巷子），完全未覆盖小众展馆和艺术偏好', '宽窄巷子属于过度商业化景点，与用户明确回避要求相悖', '正餐多为虚构的“宽窄巷子特色餐厅”或咖啡店简餐，缺乏真正的特色餐厅安排', '预算总额仅2220元，远低于7000元舒适预算，且门票分项计算错误，严重不符预算要求']
- rationale: 计划几乎未满足小众、艺术、咖啡、城市漫步等核心偏好，每日仅安排一个经典景点且频繁换宿，实际可执行性极低；大量餐饮虚构，预算严重偏离舒适档位，整体质量不合格。

### v3_harder_eval_000002
- overall: 1.0
- request: 杭州 2026-04-27->2026-04-30 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '夜市', '老字号', '城市漫步']
- issues: ['酒店选择在建德市，距离杭州核心景点超过100公里，地铁+步行完全不可行，违反 practicality', '午餐安排月龙吟（日本料理），人均349元，属于高价餐厅且极可能包含海鲜，触犯海鲜过敏和避免高价餐厅的约束', '总预算3502元超出3100元硬约束，且预算分项计算错误（如景点总费用仅270元却显示1150元）', '景点安排路线严重跳跃（如灵隐寺跨至萧山稻乡漫步街），不考虑实际交通时间和雨天影响，缺乏可执行性']
- rationale: 行程存在根本性缺陷：酒店位置极不合理导致每日通勤不可能；包含高价海鲜餐厅，违反核心偏好；总预算超标且内部数字不自洽；路线混乱不连贯，整体质量极低，无法执行。

### v3_harder_eval_000052
- overall: 1.0
- request: 苏州 2025-11-04->2025-11-07 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '夜市', '老字号', '城市漫步']
- issues: ['酒店选址在常熟市，距离市区核心景点超50公里，通勤时间单程超过16小时，完全不可行', '未安排任何夜市、老字号餐厅，未体现美食偏好，且未规避偏远住宿导致的行程无效', '预算总计与分项矛盾，景点门票合计应为155元却记为260元，餐费合计应为640元却记为480元，酒店实际应为750元却记为1000元', '连续雨天（11月6日小雨，7日中雨）未作任何室内调整或备选方案，与天气信息脱节']
- rationale: 计划严重忽视实际交通距离与时间，选择的酒店使行程无法执行；完全未落实夜市、老字号等核心偏好，饮食安排空洞；预算数字自相矛盾，缺乏可靠性；整体质量极低，无法作为可执行的穷游方案。

### v3_harder_eval_000067
- overall: 1.0
- request: 泉州 2026-08-01->2026-08-05 days=5 transport=公共交通 hotel=民宿 prefs=['小众展馆', '咖啡', '艺术', '城市漫步', '特色餐厅']
- issues: ['几乎没有满足小众展馆、艺术、特色餐厅等核心偏好，仅以咖啡厅和经典寺庙取代', '第二天酒店位于石狮黄金海岸，距离泉州古城等主要景点通勤时间超过140分钟，严重不合理且不可行', '每晚更换不同民宿，频繁搬迁不现实', '预算分项严重冲突：景点门票总额仅400元却列出1200元，餐饮每日152元5天应为760元却列出480元，总价2060元远低于舒适预算下限3100元']
- rationale: 计划完全偏离用户追求的小众艺术路线，重复使用经典寺庙和古城，餐饮单调且无特色餐厅；住宿位置荒谬、每日更换，缺乏可执行性；预算计算多处错误且未达到舒适档次预期，整体质量极低。

### v3_harder_eval_000051
- overall: 1.0
- request: 昆明 2026-06-17->2026-06-20 days=4 transport=打车 hotel=高端酒店 prefs=['高端酒店', '艺术', '特色餐厅', '城市地标', '休闲慢游']
- issues: ['石林风景区距离酒店243分钟车程，单日往返完全不现实，未考虑交通时间', '餐饮描述泛泛，未使用工具候选的特色餐厅，仅标“特色云南菜”，未满足品质用餐偏好', '预算总额3900元，严重低于用户7800元预算和5500元下限，且住宿3000元与每晚750元三晚不一致']
- rationale: 计划只粗略排列了景点，核心问题突出：石林一日游消耗8小时以上在路上，行程无法执行；餐饮推荐空洞，未体现高端特色；住宿计算有误，总预算比用户预期低一半，明显偏离premium定位，实用性和预算均不及格。

### v3_harder_eval_000057
- overall: 1.0
- request: 黄山 2026-06-02->2026-06-06 days=5 transport=公共交通 hotel=民宿 prefs=['小众展馆', '咖啡', '艺术', '城市漫步', '特色餐厅']
- issues: ["严重违反用户核心偏好：用户明确要求'小众展馆、咖啡、艺术、城市漫步、特色餐厅'，但行程中咖啡和特色餐厅仅以'黄山特色早餐/午餐/晚餐'笼统描述，无具体餐厅名和咖啡体验，完全未匹配planner_context中的咖啡厅和特色餐厅候选。", '行程地理跳跃与换宿混乱：每天更换民宿且酒店位置与游览地点脱节(如D1住屯溪却玩黄山风景区往返5小时;D2住歙县深山区阳产土楼但靠近徽州古城却写距离18km,次日跳至宏村再换酒店)。公共交通耗时长、极度不切实际，违反慢节奏情侣游需求。', '预算计算严重失真且未落进预算带: meals单价按单人计却未乘以2(总餐费应~960元非480元);景点门票重复计算黄山两次160元/人却仅纳入总价1600(如8张票应为640元/人合计1280元再推敲);交通费200元完全低估(五天频繁换宿跨区公交至少需600元以上)。实际合理总价远超3480元,表面数字虽低于4900但成分虚假。', "过度依赖经典商业化景点：D1/D6重复安排黄山风景区,宏村、西递、徽州古城全属经典大客流景点,与用户'避开过度商业化景点'的negative constraint冲突,且未充分使用planner_context给出的preference_pois如洋梨客厅、春茂艺术基地、应天齐西递村艺术馆等。", '每日描述无连贯叙事: D1抵达日竟安排全天爬山(4h+长途交通),逻辑矛盾;D6最后一天先游黄山再返程无交通时间预留。整体缺少城市漫步(citywalk)和文化流淌的慢节奏体验。']
- rationale: 行程表面罗列了部分景点，但本质上违反了几乎所有核心约束：用户偏好完全被忽视（咖啡、特色餐厅未具名），实用可行性极差（每日换宿+跨区公交不合理），预算虚假（计算单位错误、遗漏双人倍数、交通极度低估），且严重依赖用户明令避开的过度商业化景点。同时，未充分使用planner_context提供的候选pois与route_hints，造成住宿位置、游览顺序和预算项的不自洽。评为1分整体质量。

### v3_harder_eval_000017
- overall: 1.0
- request: 苏州 2026-05-05->2026-05-09 days=5 transport=公共交通 hotel=民宿 prefs=['小众展馆', '咖啡', '艺术', '城市漫步', '特色餐厅']
- issues: ['住宿每日更换且均位于远郊（昆山、吴中金庭、周庄、张家港），距离核心景区30公里以上，依赖公共交通极度不现实', '行程以平江路、七里山塘、拙政园、寒山寺等经典商业化景点为主，严重偏离“小众展馆、艺术、咖啡”偏好，缺少特色餐厅推荐', '餐饮描述全是“推荐”但无具体餐厅名，未体现特色餐厅与咖啡偏好，且星巴克被错误列为景点并收取门票', '预算计算存在明显错误且总花费仅2190元，远低于舒适档6700元，丧失合理性']
- rationale: 计划严重背离用户对审美、小众、舒适的核心诉求，住宿安排完全不切实际，预算自相矛盾且远未达到comfortable水平，整体质量极差。

### v3_harder_eval_000074
- overall: 1.0
- request: 桂林 2026-06-02->2026-06-04 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆']
- issues: ['未安排任何博物馆，未满足偏好', '缺少自由活动安排，行程没有体现慢节奏和灵活度', '第三天景点桂林千古情景区距离酒店约3小时车程，完全不适合半天行程', '餐饮地点与住宿地点严重不匹配，如每天早餐在阳朔的山野间餐厅，距酒店极远', '预算严重超支（总价2234元，硬限额1800元），住宿按3晚计算错误，应只计2晚', '住宿选择青年旅舍，不符合舒适型酒店要求']
- rationale: 计划缺失博物馆和自由活动，第三天安排无法落地，餐饮位置不合理，预算计算错误且超硬约束，整体不可用。

### v3_harder_eval_000022
- overall: 1.0
- request: 桂林 2026-04-03->2026-04-06 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '夜市', '老字号', '城市漫步']
- issues: ['总预算2588元超出2400元硬约束', "酒店'桂林兴安家家福宾馆'位于兴安县，距离市区景点超过50公里，属于用户明确规避的'太偏远的景点/地点'，且地铁+步行方式无法实现如此长途通勤，每日安排完全不可行", '预算科目内部矛盾：attractions列1120元但仅千古情景区单人280元，未正确计算多景点门票总和，账目混乱', "全程度假节奏慢但未安排任何老字号餐厅，未充分满足'老字号'偏好"]
- rationale: 计划使用了工具内候选内容，但选择了极度偏远的酒店，导致实际可行性为零；预算明细混乱且超出限额，虽满足夜市和海鲜规避等部分偏好，但整体不可用。

### v3_harder_eval_000065
- overall: 1.0
- request: 天津 2026-07-02->2026-07-06 days=5 transport=公共交通 hotel=民宿 prefs=['摄影', '自然风光', '城市漫步', '本地菜']
- issues: ['预算总价2330元，超出2000元硬约束', '住宿全选在滨海、北辰等偏远区域，每日通勤超1.5小时，违背‘不要太偏远’和‘避免密集赶景点’的要求', '餐饮每天重复相同三家餐厅，且餐厅位置与当日行程严重不符，无法落地', '安排了偏远国家海洋博物馆，与‘避开太偏远的景点’冲突', '酒店频繁更换且第一天与后续住宿不统一，增加不必要的奔波']
- rationale: 计划严重违反预算硬约束，住宿和餐饮安排均缺乏现实可行性，每日通勤时间过长，与用户‘不要太偏远’‘不要密集赶景点’的诉求背道而驰，整体质量不可接受。
