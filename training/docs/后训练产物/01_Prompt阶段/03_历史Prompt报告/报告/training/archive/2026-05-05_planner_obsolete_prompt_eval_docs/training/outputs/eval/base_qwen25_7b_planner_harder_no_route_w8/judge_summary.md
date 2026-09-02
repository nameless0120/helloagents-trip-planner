# LLM Judge Summary

```json
{
  "total": 300,
  "judged": 283,
  "skipped": 17,
  "judge_coverage": 0.9433,
  "skip_reason_counts": {
    "json_extract": 2,
    "judge_failed": 15
  },
  "scores_avg": {
    "preference_satisfaction": 2.4982,
    "practicality": 2.1625,
    "grounding_faithfulness": 3.4099,
    "budget_reasonableness": 1.5442,
    "coherence": 2.3039,
    "overall_quality": 1.8834
  }
}
```

## Low Score Examples

### v3_harder_eval_000015
- overall: 0
- request: 南京 2026-04-03->2026-04-07 days=5 transport=公共交通 hotel=民宿 prefs=['摄影', '自然风光', '城市漫步', '本地菜']
- issues: ['响应中未找到完整的顶层TripPlan JSON对象']
- rationale: 输出未通过 JSON/schema 基础解析，直接记为无效输出。

### v3_harder_eval_000068
- overall: 0
- request: 福州 2026-08-31->2026-09-02 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物']
- issues: ['模型输出中没有 JSON 起始符']
- rationale: LLM judge 多次未返回可解析 JSON 或调用失败，本条记为 judge_failed。

### v3_harder_eval_000140
- overall: 0
- request: 杭州 2026-06-02->2026-06-06 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- issues: ['响应中未找到完整的顶层TripPlan JSON对象']
- rationale: 输出未通过 JSON/schema 基础解析，直接记为无效输出。

### v3_harder_eval_000092
- overall: 0
- request: 大理 2026-08-01->2026-08-04 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '夜市', '老字号', '城市漫步']
- issues: ["Expecting ',' delimiter: line 9 column 4 (char 186)"]
- rationale: LLM judge 多次未返回可解析 JSON 或调用失败，本条记为 judge_failed。

### v3_harder_eval_000100
- overall: 0
- request: 西安 2026-08-01->2026-08-05 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- issues: ['模型输出中没有 JSON 起始符']
- rationale: LLM judge 多次未返回可解析 JSON 或调用失败，本条记为 judge_failed。

### v3_harder_eval_000103
- overall: 0
- request: 扬州 2026-05-04->2026-05-08 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食']
- issues: ["Expecting ',' delimiter: line 14 column 4 (char 353)"]
- rationale: LLM judge 多次未返回可解析 JSON 或调用失败，本条记为 judge_failed。

### v3_harder_eval_000111
- overall: 0
- request: 珠海 2026-08-31->2026-09-03 days=4 transport=打车 hotel=高端酒店 prefs=['高端酒店', '艺术', '特色餐厅', '城市地标', '休闲慢游']
- issues: ['模型输出中没有 JSON 起始符']
- rationale: LLM judge 多次未返回可解析 JSON 或调用失败，本条记为 judge_failed。

### v3_harder_eval_000151
- overall: 0
- request: 杭州 2026-07-02->2026-07-05 days=4 transport=打车 hotel=高端酒店 prefs=['高端酒店', '艺术', '特色餐厅', '城市地标', '休闲慢游']
- issues: ['模型输出中没有 JSON 起始符']
- rationale: LLM judge 多次未返回可解析 JSON 或调用失败，本条记为 judge_failed。

### v3_harder_eval_000183
- overall: 0
- request: 南京 2026-08-31->2026-09-04 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食']
- issues: ['模型输出中没有 JSON 起始符']
- rationale: LLM judge 多次未返回可解析 JSON 或调用失败，本条记为 judge_failed。

### v3_harder_eval_000188
- overall: 0
- request: 泉州 2026-07-02->2026-07-04 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物']
- issues: ['模型输出中没有 JSON 起始符']
- rationale: LLM judge 多次未返回可解析 JSON 或调用失败，本条记为 judge_failed。

### v3_harder_eval_000222
- overall: 0
- request: 深圳 2026-01-03->2026-01-06 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '夜市', '老字号', '城市漫步']
- issues: ["Expecting ',' delimiter: line 9 column 4 (char 186)"]
- rationale: LLM judge 多次未返回可解析 JSON 或调用失败，本条记为 judge_failed。

### v3_harder_eval_000269
- overall: 0
- request: 青岛 2026-05-06->2026-05-09 days=4 transport=打车 hotel=亲子酒店 prefs=['亲子', '老人友好', '博物馆', '城市公园', '特色餐厅']
- issues: ['模型输出中没有完整 JSON']
- rationale: LLM judge 多次未返回可解析 JSON 或调用失败，本条记为 judge_failed。

### v3_harder_eval_000283
- overall: 0
- request: 长沙 2025-11-04->2025-11-08 days=5 transport=公共交通 hotel=舒适型酒店 prefs=['自然风光', '历史文化', '公园', '本地美食']
- issues: ['模型输出中没有 JSON 起始符']
- rationale: LLM judge 多次未返回可解析 JSON 或调用失败，本条记为 judge_failed。

### v3_harder_eval_000288
- overall: 0
- request: 深圳 2026-05-07->2026-05-09 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物']
- issues: ['模型输出中没有 JSON 起始符']
- rationale: LLM judge 多次未返回可解析 JSON 或调用失败，本条记为 judge_failed。

### v3_harder_eval_000292
- overall: 0
- request: 济南 2026-04-19->2026-04-22 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '夜市', '老字号', '城市漫步']
- issues: ['模型输出中没有 JSON 起始符']
- rationale: LLM judge 多次未返回可解析 JSON 或调用失败，本条记为 judge_failed。

### v3_harder_eval_000298
- overall: 0
- request: 上海 2026-05-04->2026-05-06 days=3 transport=打车 hotel=高端酒店 prefs=['城市地标', '美食', '夜景', '购物']
- issues: ['模型输出中没有 JSON 起始符']
- rationale: LLM judge 多次未返回可解析 JSON 或调用失败，本条记为 judge_failed。

### v3_harder_eval_000294
- overall: 0
- request: 三亚 2026-07-02->2026-07-04 days=3 transport=打车 hotel=舒适型酒店 prefs=['城市地标', '特色餐厅', '自由活动多', '博物馆']
- issues: ["Expecting ',' delimiter: line 16 column 4 (char 376)"]
- rationale: LLM judge 多次未返回可解析 JSON 或调用失败，本条记为 judge_failed。

### v3_harder_eval_000022
- overall: 1.0
- request: 桂林 2026-04-03->2026-04-06 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '夜市', '老字号', '城市漫步']
- issues: ['酒店位于兴安县，距离每天游览的桂林市区/阳朔景点超过60公里，地铁+步行不可达，每日通勤完全不现实', '总预算超出2400元硬约束（计划自称2480元），且分项（景点、餐饮）与明细严重不一致，门票总价错误', '完全未安排老字号餐饮（如椿记烧鹅、阿甘酒家），与‘老字号’偏好相悖', '景点跨区跳跃严重（如象鼻山与资源县夜市、一天的日月双塔与阳朔千古情），导致行程无法执行', '全程只有‘桂林米粉’作为三餐，极度单调且不具体，未从候选餐厅中选取美食选项', '第一天大雨户外游览象鼻山无备选方案，第三天枫林夜市与住宿兴安距离过远']
- rationale: 计划在酒店选址、交通衔接、预算合规和偏好满足方面均存在致命缺陷，实质上无法执行，整体质量极低。

### v3_harder_eval_000030
- overall: 1.0
- request: 三亚 2026-05-07->2026-05-11 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '历史文化', '城市公园', '本地美食']
- issues: ['每日更换酒店且酒店与景点跨区明显，交通负担大，不适合老人和儿童，实际无法执行', '餐饮全为海鲜大餐/火锅，不符合清淡饮食偏好和本地美食要求，且成本估算偏低', '总预算仅4600元，远低于舒适型硬约束下限6800元，严重违约', '未体现历史文化、城市公园等用户强调的偏好，行程内容单调重复']
- rationale: 计划看似选了幼儿友好景点，但实际操作中酒店频繁变动、长途通勤违背轻松原则；餐食与预算严重不符要求，整体不可行。

### v3_harder_eval_000002
- overall: 1.0
- request: 杭州 2026-04-27->2026-04-30 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['美食', '夜市', '老字号', '城市漫步']
- issues: ['酒店选址在建德市，距离杭州市区景点极远，与地铁+步行交通方式完全矛盾，且与“经济型酒店”市区属性不符，严重违反“太偏远的景点”规避要求', '餐饮安排极度重复，每天早餐、午餐完全相同，城市漫步、老字号等偏好基本未体现，美食体验单调', '预算汇总严重错误，实际餐饮费远超total_meals的480元，且总预算1860元远低于政策下限2200元，不满足hard budget约束', '酒店位置描述“距离景点2公里”虚构，与建德市实际距离矛盾，缺乏可执行性']
- rationale: 计划未能满足用户核心偏好，酒店选址荒谬，餐饮安排缺乏多样性和老字号特色，预算计算自相矛盾，整体不可执行。
