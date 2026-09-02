# V3 Prompt 预算账本消融小结

本轮目标：在不改工具、不改上下文、不做后处理的前提下，尝试用更强 prompt 约束修复预算分项算术问题。

## 消融版本

### budget_ledger

- 基于 hard compact records 追加“预算账本强约束”。
- 要求模型先写完 days，再回扫 days 计算 budget。
- 明确：
  - `total_hotels = sum(non-null day.hotel.estimated_cost)`
  - `total_attractions = sum(ticket_price) * party.total`
  - `total_meals = sum(day.meals[].estimated_cost)`
  - `budget.total = 四个分项相加`

smoke5 结果：

| 指标 | 结果 |
| --- | ---: |
| JSON 可解析 | 5/5 |
| schema 通过 | 5/5 |
| hotel_budget_covers_nights | 5/5 |
| budget_arithmetic_consistent | 2/5 |
| attraction_budget_consistent | 0/5 |
| meal_budget_consistent | 0/5 |
| sft_hard_pass | 0/5 |

观察：结构稳定，但模型仍会把 `budget.total_attractions` 和 `budget.total_meals` 当成单独估计值，而不是严格从 days 字段回扫。典型错误是酒店总价算对了，景点和餐饮分项没有按 schema 字段机械加总。

### budget_ledger_no_schema_numbers

- 在 `budget_ledger` 基础上移除了 system prompt 中带具体数字的字段结构示例，尝试避免示例数字污染预算。

smoke5 结果：

| 指标 | 结果 |
| --- | ---: |
| JSON 可解析 | 5/5 |
| schema 通过 | 0/5 |
| 失败阶段 | schema |

观察：删掉字段结构示例后，模型开始改字段名或漏字段，例如把 `meal.estimated_cost` 写成 `meal_cost`，景点缺少 `visit_duration` / `description`，部分 day 缺少 `transportation`。说明字段结构示例对 Qwen2.5-7B 的 schema 稳定性很关键，不能粗暴移除。

## 当前判断

预算账本类 prompt 对“酒店晚数”有帮助，但不足以让 7B 在长 PlannerContext 和多天多 POI 输出里稳定完成精确分项加总。

这更像模型能力与任务形态的边界：长 JSON 生成、候选选择、约束遵循、预算算术同时发生时，prompt 可以减少低级错误，但很难保证每个预算分项都严格等于 days 字段的派生值。

## 后续建议

1. schema 示例继续保留，不能删除。
2. prompt 可保留 `budget_symbolic` 或 `budget_ledger` 中较简洁的预算口径规则，但不要指望它单独解决精确预算分项。
3. 如果预算分项一致性是 SFT hardpass，建议用工程后处理重算 `budget`，或在生成训练数据时统一重写预算字段，再让 SFT 学习“最终输出形态”。
4. DPO 更适合优化软质量，例如餐饮/景点多样性、路线舒适度、预算档位贴合、偏好取舍，不适合兜底精确算术。
