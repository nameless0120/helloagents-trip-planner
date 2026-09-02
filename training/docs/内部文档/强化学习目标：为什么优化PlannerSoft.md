# Planner Soft 作为下一轮强化学习目标的说明

## 结论

下一轮 DPO / RL 的主目标建议定为优化 `planner_soft_pass`。

原因很简单：我们现在真正想提升的不是“模型会不会输出一个格式正确的行程”，而是“这个行程作为旅行计划是否真的可用、合适、体验好”。`planner_soft_pass` 比之前的 soft 指标更接近这个目标，因为它同时约束了行程可执行性、实际预算匹配、餐饮价格尺度、餐饮/景点多样性。

当前评估里也能看到这个方向是有效的：

| 模型 | PlannerSoft combined |
|---|---:|
| SFT final | 35.2% |
| DPO initial 260517 | 38.0% |
| 本轮 ckpt-25 | 44.7% |

也就是说，本轮 DPO 已经把 planner soft 从 SFT final 拉高了约 9.5pp，说明这个信号是能被模型学到的。

## 指标定义

当前评估脚本里的定义是：

```text
planner_soft_pass =
  sft_hard_pass
  && attraction_diversity_ok
  && meal_diversity_ok
  && meal_cost_scale_ok
  && recomputed_budget_user_constraint_ok
  && recomputed_budget_fit_ok
```

其中 `sft_hard_pass` 负责保证基本可用性，例如 JSON 可解析、schema 正确、城市/日期/天气正确、酒店/餐饮/景点 grounding 正确、每天结构完整、没有明显非法 POI 等。

`planner_soft_pass` 在 hard pass 之上，再要求：

- `attraction_diversity_ok`：景点不要高度重复，行程内容要有变化。
- `meal_diversity_ok`：餐饮不要高度重复，不能每天用同类餐食糊过去。
- `meal_cost_scale_ok`：餐饮价格尺度要和预算档位匹配，尤其是高预算档位不能长期安排过便宜的正餐。
- `recomputed_budget_user_constraint_ok`：按实际选择的酒店、餐饮、景点重算后，不能突破用户硬预算。
- `recomputed_budget_fit_ok`：按实际选择内容重算后，总体预算档位要符合用户偏好。

## 和之前 soft 指标的区别

之前主要看的是 `dpo_soft_pass`：

```text
dpo_soft_pass =
  sft_hard_pass
  && attraction_diversity_ok
  && meal_diversity_ok
  && budget_preference_aligned
```

这个指标有用，但它的问题是 `budget_preference_aligned` 偏粗。它更像是在看“模型报出来的预算/档位是否看起来符合偏好”，不完全等价于“行程实际花费是否合适”。

后来我们又看 `dpo_soft_recomputed_budget_pass`：

```text
dpo_soft_recomputed_budget_pass =
  sft_hard_pass
  && attraction_diversity_ok
  && meal_diversity_ok
  && recomputed_budget_fit_ok
```

这一步比 `dpo_soft_pass` 更好，因为它开始使用重算预算，不再只相信模型自己写的预算表。但它仍然少了两个关键点：

- 它没有单独约束 `recomputed_budget_user_constraint_ok`。用户硬预算应该是底线，不能只看档位 fit。
- 它没有约束 `meal_cost_scale_ok`。预算总体接近，不代表餐饮体验合理；模型可能用贵酒店/贵景点把总价抬上去，但午餐晚餐仍然大量安排很便宜的东西。

`planner_soft_pass` 相当于把这两类缺口补上了。

## 为什么 planner soft 更能衡量旅行好坏

一个旅行计划好不好，不只是看它有没有合法 JSON，也不只是看预算数字表写得对不对。用户真正体验到的是这些东西：

1. 行程是否能执行
   城市、日期、天气、酒店、餐厅、景点都要对得上，结构要完整。这由 `sft_hard_pass` 兜底。

2. 预算是否真的合适
   我们更应该相信“按实际选中的 POI 和酒店价格重算出来的预算”，而不是模型自己写的预算小结。`recomputed_budget_user_constraint_ok` 和 `recomputed_budget_fit_ok` 更接近真实成本。

3. 消费尺度是否符合用户预期
   高预算用户不是一定要顿顿贵，但长期安排过便宜的正餐会让计划显得不懂预算偏好。`meal_cost_scale_ok` 解决的就是这个问题。它不是惩罚当地小吃、夜市、早点、特色面馆这类体验，而是防止模型在高预算档位用低价餐饮偷懒。

4. 行程是否有体验丰富度
   旅行不是填格子。景点重复、餐饮重复，用户会觉得计划单薄。`attraction_diversity_ok` 和 `meal_diversity_ok` 是体验丰富度的最低约束。

所以 `planner_soft_pass` 衡量的是“一个 hard-valid 的计划，是否进一步像一个合格旅行规划师做出来的计划”。

## 为什么不继续只优化 dpo_soft_pass

`dpo_soft_pass` 可以作为辅助指标，但不适合作为下一轮主目标。

主要原因：

- 它依赖 `budget_preference_aligned`，这个指标容易和用户硬预算、重算预算产生张力。
- 它没有显式看餐饮价格尺度，容易漏掉“预算看起来对，但体验不对”的 case。
- 它更像偏好粗筛，不够像最终用户体验指标。

下一轮如果继续只优化它，模型可能学会“把预算描述写得更像正确答案”，但不一定真正学会“选择更合适的酒店、餐饮、景点组合”。

## 训练数据应该怎么围绕 planner soft 做

下一批数据建议围绕 planner soft 的失败维度来做强信号 pair，但不要直接拿 eval 失败 case 训练，避免数据泄漏。可以用 train-only prompts / contexts 做同分布压力构造。

推荐的 pair 设计：

- chosen：必须 hard pass，并且尽量 planner soft pass。
- rejected：最好 hard pass，但在一个明确 planner soft 维度上失败。
- 每个 pair 尽量只有一个主要差异，避免 chosen/rejected 同时差在很多地方，导致 DPO 信号不干净。

重点覆盖这些失败类型：

- 预算重算不匹配：实际行程价格低于/高于目标档位。
- 用户硬预算冲突：重算后超过用户预算。
- 餐饮价格尺度不对：高预算档位安排过多低价正餐。
- 餐饮重复：连续几天餐饮类型或地点太重复。
- 景点重复或体验单薄：景点选择变化不足。

## 训练时的保护指标

虽然主目标是 `planner_soft_pass`，但训练过程中还要盯住这些 guardrail：

- `hard_pass` 不能掉。planner soft 的前提是行程必须先可用。
- `recomputed_budget_user_constraint_ok` 不能掉。用户硬预算是底线。
- `meal_grounding_ok` / `attraction_grounding_ok` 不能掉。不能为了预算好看而选不存在或不在候选里的 POI。
- standard / hard split 都要看，不能只看 combined。

## 下一轮推荐口径

下一轮模型选择时，建议按下面优先级判断：

1. `planner_soft_pass` combined 最高优先。
2. hard split 的 `planner_soft_pass` 不能明显回落。
3. `hard_pass` 基本持平或提升。
4. `meal_cost_scale_ok` 保持高位。
5. `recomputed_budget_fit_ok` 和 `recomputed_budget_user_constraint_ok` 不要互相打架。

如果两个 checkpoint 的 `planner_soft_pass` 接近，优先选 hard split 更稳、`recomputed_budget_fit_ok` 更高的版本。
