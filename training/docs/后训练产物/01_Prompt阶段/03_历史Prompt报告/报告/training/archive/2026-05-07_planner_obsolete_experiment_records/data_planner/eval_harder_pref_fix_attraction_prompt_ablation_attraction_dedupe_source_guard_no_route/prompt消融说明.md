# Prompt 消融记录：attraction_dedupe_source_guard

- 来源 records：`training/data/v3/eval_harder_attraction_pref_fix_20260506/A_C/records.jsonl`
- 样本数：300
- 改动范围：只追加 system_prompt 和 planner_query 规则，不改变 request/planner_context/tool_snapshot。
- 共同餐饮规则：lunch/dinner 宁可重复真实 food_pois，也不能写无、空、酒店晚餐或泛化餐厅。

## 附加规则

```text
景点全程去重补充:
- 不改变景点密度偏好：正常旅行每天可以安排 1-3 个景点；如果路线顺、体力允许、候选充足，安排 3 个景点是可以的。
- 但同一个景点 name 默认全程只能出现一次，不能跨天重复安排。
- 内部维护 used_attraction_names，不输出这个表；去重 key 忽略空格，并忽略中文/英文括号中的分店或补充说明。
- 每天选择 attractions 时，优先选择还没用过、并且来自 classic_pois/preference_pois/scenic_pois/experience_pois 的候选。
- 如果后续天想再次使用已用过的景点，必须改选另一个未使用的真实景点候选；宁可换成同区的轻量景点，也不要重复同名景点。
- 只有当真实景点候选已经不足以保证每天至少 1 个景点时，才允许复用；复用时必须在 description 里说明候选不足或返程/体力原因。

景点来源防污染补充:
- attractions 只能从 classic_pois、preference_pois、scenic_pois、experience_pois 选择真实 POI。
- attraction.name 必须完全复制这些景点候选中的 name；attraction.ticket_price 必须复制对应候选的 ticket_price_hint。
- 禁止把 food_pois、hotel_pois 写进 attractions；餐厅、咖啡馆、米粉店、火锅店、酒家、饭店、酒店、民宿、客栈、旅舍只能用于 meals 或 hotel，不能作为景点。
- 当用户偏好包含美食、夜市、老字号、城市漫步、购物、艺术街区时，可以选择 preference_pois/scenic_pois 中的步行街、夜市、老街、古街、历史街区、商业街、艺术街区等景点候选；不要用 food_pois 中的具体餐厅/咖啡馆来补 attractions。
- 如果某个常识上像景点的名字没有出现在四个景点候选桶中，也不要编进 attractions；改用候选桶里最接近的真实 POI。
```
