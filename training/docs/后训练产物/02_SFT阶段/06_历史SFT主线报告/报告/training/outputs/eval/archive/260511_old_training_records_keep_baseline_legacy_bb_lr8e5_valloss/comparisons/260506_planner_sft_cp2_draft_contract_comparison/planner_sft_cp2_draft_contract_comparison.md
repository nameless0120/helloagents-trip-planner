# V3 SFT cp2：Draft 输出契约下的 Base vs SFT 对比

本版对比按“模型只输出行程草案，工程侧回填价格并计算预算”的契约重算指标：

- 模型不再负责输出 `budget.total_attractions / total_hotels / total_meals / total` 等预算加总字段。
- 模型也不需要证明自己会做“人数 * 单价 * 天数 * 房间数”的精确数学。
- 模型核心职责变成：结构正确、日期天气正确、住宿规则正确、景点/酒店/餐饮具体且可被工具候选解析。
- 预算相关只看“工程侧用模型选择的 POI 价格重算后，是否贴合用户预算”，这是选择质量，不是模型自报数学。

## 组合指标

| 指标 | Base A_C | SFT cp2 v1 A_C | 变化 |
|---|---:|---:|---:|
| `draft_core_pass` | 145/300 = 48.33% | 211/300 = 70.33% | +22.00 pp |
| `price_resolvable_ok` | 153/300 = 51.00% | 194/300 = 64.67% | +13.67 pp |
| `planner_draft_hard_pass` | 134/300 = 44.67% | 189/300 = 63.00% | +18.33 pp |
| `draft_budget_hard_pass` | 44/300 = 14.67% | 90/300 = 30.00% | +15.33 pp |
| `draft_budget_fit_pass` | 28/300 = 9.33% | 60/300 = 20.00% | +10.67 pp |
| `draft_dpo_soft_recomputed_budget_pass` | 17/300 = 5.67% | 35/300 = 11.67% | +6.00 pp |

## 指标定义

| 指标 | 含义 |
|---|---|
| `draft_core_pass` | 不看预算数学，只看 JSON/schema、城市日期、天数、天气、住宿、景点数量、景点 grounding、餐饮完整性、餐饮语义、位置对象等草案硬规则。 |
| `price_resolvable_ok` | 景点、酒店、餐饮都能命中工具候选，工程侧可以回填价格。 |
| `planner_draft_hard_pass` | `draft_core_pass + meal_grounding_ok`，即一条可以交给工程侧稳定回填价格的行程草案。 |
| `draft_budget_hard_pass` | 在 `planner_draft_hard_pass` 基础上，用回填价格重算后满足 hard 预算约束。 |
| `draft_budget_fit_pass` | 在 `planner_draft_hard_pass` 基础上，用回填价格重算后符合预算档位/偏好贴合。 |
| `draft_dpo_soft_recomputed_budget_pass` | 景点多样性、餐饮多样性、餐饮 grounding、重算预算贴合同时通过。 |

## 关键单项

| 指标 | Base A_C | SFT cp2 v1 A_C | 变化 |
|---|---:|---:|---:|
| `json_extract_ok` | 300/300 = 100.00% | 300/300 = 100.00% | +0.00 pp |
| `schema_ok` | 298/300 = 99.33% | 298/300 = 99.33% | +0.00 pp |
| `attraction_grounding_ok` | 296/300 = 98.67% | 280/300 = 93.33% | -5.33 pp |
| `attraction_diversity_ok` | 265/300 = 88.33% | 209/300 = 69.67% | -18.67 pp |
| `hotel_grounding_ok` | 294/300 = 98.00% | 298/300 = 99.33% | +1.33 pp |
| `meal_complete` | 298/300 = 99.33% | 298/300 = 99.33% | +0.00 pp |
| `meal_grounding_ok` | 157/300 = 52.33% | 209/300 = 69.67% | +17.33 pp |
| `meal_diversity_ok` | 197/300 = 65.67% | 223/300 = 74.33% | +8.67 pp |
| `recomputed_budget_hard_ok` | 115/300 = 38.33% | 125/300 = 41.67% | +3.33 pp |
| `recomputed_budget_fit_ok` | 72/300 = 24.00% | 85/300 = 28.33% | +4.33 pp |
| `budget_selection_ok` | 72/300 = 24.00% | 85/300 = 28.33% | +4.33 pp |

## 结论

如果采用 Draft 输出契约，SFT 是有效的：`planner_draft_hard_pass` 从 44.67% 提升到 63.00%，主要收益来自餐饮 grounding、餐饮多样性、住宿 grounding 和整体硬规则稳定性。

但 SFT 没有真正解决“按实际回填价格贴预算”的问题：`budget_selection_ok` 只从 24.00% 到 28.33%。这说明当前 7B 模型已经比较适合学格式、规则、工具引用和餐饮具体化，但不适合单独承担预算选择最优化。

因此更合理的职责边界是：

1. 模型输出 `TripPlanDraft`：日期、天气、景点、酒店、餐饮、理由/提示，不输出任何预算加总。
2. 工程侧解析候选 POI，回填 `ticket_price / hotel.estimated_cost / meal.estimated_cost`。
3. 工程侧计算 `computed_budget`，并对超预算或预算利用过低的草案做 repair/rerank。
4. SFT 主指标改成 `planner_draft_hard_pass`；预算选择作为独立工程指标 `budget_selection_ok`，不再和模型数学能力绑定。
