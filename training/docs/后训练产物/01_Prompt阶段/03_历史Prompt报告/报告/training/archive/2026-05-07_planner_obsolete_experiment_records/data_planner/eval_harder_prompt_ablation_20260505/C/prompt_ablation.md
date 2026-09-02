# Prompt Ablation: C

- source records: `training/data/v3/eval_harder/records.jsonl`
- records: 300
- request / PlannerContext / planner_query: unchanged
- system_prompt: current backend PLANNER_AGENT_PROMPT with this variant applied
- blocks: C

## Blocks

### C

```text
餐饮选择是硬约束，每天必须有 breakfast、lunch、dinner 三餐。

餐厅来源：
- lunch 和 dinner 必须从 food_pois 中选择真实餐厅。
- meal.name 必须完全复制 food_pois.name。
- meal.estimated_cost 必须复制 food_pois.meal_cost_hint。
- 禁止使用 hotel_pois 作为 lunch 或 dinner。
- 禁止使用泛化名称，例如“附近餐厅”“当地小吃”“特色餐厅”“早餐推荐”“午餐推荐”“晚餐推荐”“无”。

餐厅去重算法必须在内部执行：
1. 先列出所有 food_pois 候选。
2. 过滤 avoid_risk_keywords 非空的候选。
3. 给每个候选维护 used_count，初始为 0。
4. 为每一天选择 lunch 时，优先选择 used_count 最少、适合 lunch、距离当天景点区域更接近的候选。
5. 为同一天 dinner 选择时，禁止选择当天 lunch 的同一个 name。
6. dinner 同样优先选择 used_count 最少的候选。
7. 每选择一次餐厅，就把该 name 的 used_count 加 1。
8. 只有当可用 food_pois 数量不足以覆盖所有 lunch/dinner 时，才允许复用；复用时必须选择 used_count 最少的真实 food_pois。
9. breakfast 可以使用适合早餐/小吃/简餐的 food_pois，也可以在合理场景使用“酒店早餐/民宿早餐/客栈早餐”；住宿早餐不参与 used_count。

强制校验：
- 同一天 lunch.name 和 dinner.name 绝不能相同。
- 连续两天 dinner.name 尽量不能相同。
- 如果 food_pois 数量 >= 行程天数 * 2，则整趟行程所有 lunch/dinner 的 name 必须全部不同。
- 如果 food_pois 数量不足，则 lunch/dinner 应平均分散复用，不能每天固定同一家。
```
