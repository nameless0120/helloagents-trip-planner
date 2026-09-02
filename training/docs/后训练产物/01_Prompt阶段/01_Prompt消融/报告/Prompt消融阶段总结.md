# Planner Prompt 消融全阶段总结

更新时间：2026-05-11

这份文档记录 Planner Planner prompt 阶段的搜索过程、主要消融和最终结论。2026-05-05 重新修正并重跑了最终 12 组 A/B/C/D prompt ablation 的 rule eval；2026-05-11 补写前面三十多版 prompt 的探索过程，避免把整个阶段误读成只做了最后十几版。

结论先行：**当前 7B Planner 的 prompt-only 收益已经基本摸到上限，后续主线不再继续调 prompt**。最终冻结的 prompt baseline 仍是 `A_C`。

冻结 prompt sha256：

```text
dbe3f951082929b5de41e3de38f823356dd94a01896d81246e447d80a196e5c0
```

报告入口：

- 这里保留主要表格和阶段结论；原始 generations、batch summary、旧 self-check/context 报告已经作为历史实验资产归档，不作为当前主线入口。
- 当前 prompt：`backend/app/agents/prompts.py::PLANNER_AGENT_PROMPT`
- 旧版过程汇总可参考归档：
  - `training/archive/2026-05-05_v3_obsolete_prompt_eval_docs/training/outputs/eval/planner_context_ablation_summary.md`
  - `training/archive/2026-05-05_v3_obsolete_prompt_eval_docs/training/outputs/eval/planner_prompt_two_stage_pass_all_history.md`
  - `training/archive/2026-05-05_v3_obsolete_prompt_eval_docs/training/outputs/eval/planner_prompt_budget_ablation_summary.md`
  - `training/archive/2026-05-05_v3_obsolete_prompt_eval_docs/training/outputs/eval/planner_meal_prompt_ablation_summary.md`
  - `training/archive/2026-05-07_v3_obsolete_experiment_records/outputs_eval/prompt_ablation_20260505/batch_summary.md`

## 1. 评估口径更新

本次最终重评只重新跑了本地历史 prompt ablation 输出中有完整 `records_path + generations_path` 的 12 组现役 eval，没有重新调用模型生成。早期 context/self-check/预算/餐饮/景点阶段只保留历史结论，用来说明 prompt 搜索路径。

`meal_grounding_ok` 现在是更严格的样本级指标：

- 每条行程里所有 `meals` 都必须 grounding 成功。
- `lunch` 和 `dinner` 必须命中 `PlannerContext.tool_snapshot.food_pois`。
- 只有 `type=breakfast` 且名字为酒店/民宿/客栈/住宿早餐时，才允许不命中 `food_pois`。
- 任意一餐 miss，整条样本的 `meal_grounding_ok` 就失败。
- 因此这里同时加入餐次级 `meal_grounding_rate`，用来观察模型逐餐复制候选的真实能力。

这个口径会更严厉地惩罚“酒店晚餐”“客栈晚餐”“午餐写住宿早餐”这类输出。它让部分 C 相关组合的 `meal_grounding_ok` 下降，但不改变 prompt 阶段总判断。

## 2. Prompt 阶段怎么推进

这个阶段不是一开始就得到 A/B/C/D 12 组。实际过程更接近“先定考试标准，再按问题家族逐轮收敛”：

1. 先用小样本 smoke 跑判断 prompt 是否破 schema、是否引入明显污染或退化。
2. 通过 smoke 的版本再跑 300 条全量，比较 schema、grounding、预算、餐饮、延迟。
3. 每次指标定义变化后，优先重评已有 generations，避免把模型随机性和评测口径混在一起。
4. 当发现某类问题不是 prompt 能稳定解决的，就把它转为工程重算、数据清洗、SFT 或 DPO 目标。

按版本家族看，阶段里至少包含这些探索：

| 家族 | 代表版本 | 主要目的 | 阶段判断 |
| --- | --- | --- | --- |
| 基础 Planner / harder / no-route | `planner_hard`、`hard_attr_prompt_w8`、`harder_w8`、`no_route_w8`、`food_bucket_return_dinner_prompt_w8` | 建立 Planner 结构协议，处理景点数量、粗 route_hints、返程晚餐、餐饮桶 | 粗 route_hints 不可靠；去掉后让模型用 POI 的 district/address/location 自行组合更稳 |
| 上下文形态 | `hard/balanced × full/compact/topk/policy_first_topk` 共 8 组 | 比较候选覆盖、上下文长度、硬约束和软质量 | `hard_compact` 更适合作为硬约束 baseline；`balanced_*` 软质量更好但硬约束弱 |
| 预算算术规则 | `budget_hard`、`budget_order`、`budget_fewshot`、`budget_symbolic`、`budget_ledger`、`budget_ledger_no_schema_numbers` | 看 prompt 能否让 7B 机械回扫 days 并精确汇总预算 | few-shot 数字污染明显；symbolic 更安全；ledger 类规则仍不能稳定解决长 JSON 算术 |
| 预算业务口径 | `budget_relation_lite/priority/self_check`、`room_person_price_lite/full/self_check` | 明确房间数、同行人数、餐饮人均价、景点单人票价 | 口径修正是必要的，但 prompt 收益不稳定，预算仍要后端重算 |
| 景点来源和去重 | `attraction_dedupe_only`、`attraction_source_guard_only`、`dedupe_source_guard`、`dedupe_source_self_check` | 防止把餐厅/酒店写进景点，减少跨天重复景点 | source guard 有价值；去重更像 DPO soft 目标，不适合继续压进 hard prompt |
| 餐饮兜底和多样性 | `meal_diversity_symbolic`、`meal_count_limit_symbolic`、`meal_rotation_symbolic`、`meal_grounded_diversity_symbolic`、`budget_symbolic_meal_semantic` | 平衡真实 `food_pois` grounding、午晚餐不重复、跨天多样性、返程晚餐 | `meal_rotation` 软质量最好，但硬约束下降；严格 grounding 与多样性存在拉扯 |
| 自检类 prompt | `room_person_price_self_check`、最终块 `D` | 输出前内部检查 schema、预算、餐饮和重复项 | 自检能改善个别局部指标，但会拉低其他硬约束 |
| 最终 A/B/C/D 重点组合 | `baseline/A/B/C/D/A_C/.../B_C_D` 12 组 | 对最后留下的四类规则做可重评组合消融 | `A_C` 是最适合冻结的折中点 |

所以，最后 12 组只是“可重评、可冻结”的终局集合，不是 prompt 阶段的全部版本。前面的三十多版主要负责确认边界：哪些规则值得留下，哪些规则会互相干扰，哪些问题应该交给后处理或训练。

## 3. 上下文与基础口径消融

第一阶段主要解决的是：用什么上下文形态和基础约束作为后续 prompt 实验起点。

当时对比了 `hard_*` 和 `balanced_*`，以及 `full / compact / topk / policy_first_topk` 等上下文组织方式。重点不是最终 prompt 文案，而是确认 Planner 输入在结构、候选覆盖和预算口径上怎样最稳。

历史表格：

| 版本 | schema | SFT语义硬过 | 预算关系 | 酒店关系 | 景点关系 | 餐饮尺度 | 用户预算 | 预算加总 | 餐饮ground | 餐饮多样 | avg秒 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| hard_full | 98.0% | 3.4% | 5.4% | 41.8% | 27.6% | 81.0% | 82.3% | 60.5% | 97.3% | 8.2% | 64.9 |
| hard_compact | 98.7% | 4.4% | 6.8% | 39.5% | 28.0% | 87.2% | 81.4% | 69.6% | 96.6% | 6.8% | 60.9 |
| hard_topk | 99.3% | 6.4% | 9.1% | 41.6% | 28.5% | 88.3% | 83.9% | 64.1% | 95.0% | 7.0% | 53.3 |
| hard_policy_topk | 99.0% | 5.1% | 7.7% | 40.1% | 32.3% | 84.5% | 83.8% | 64.6% | 96.0% | 14.5% | 54.2 |
| balanced_full | 97.3% | 4.1% | 6.5% | 39.4% | 28.8% | 61.6% | 85.6% | 62.7% | 87.3% | 51.0% | 65.1 |
| balanced_compact | 98.7% | 3.7% | 6.1% | 40.5% | 24.3% | 76.7% | 82.8% | 66.2% | 90.5% | 49.0% | 60.8 |
| balanced_topk | 98.7% | 4.0% | 6.1% | 39.9% | 25.0% | 78.0% | 83.5% | 67.6% | 86.2% | 56.4% | 50.6 |
| balanced_policy_topk | 99.0% | 3.0% | 7.1% | 38.7% | 26.6% | 78.8% | 88.9% | 66.0% | 85.5% | 51.2% | 50.7 |

阶段结论：

- `hard_compact` 被选为当时的推荐 baseline：schema、grounding、预算加总和延迟较均衡。
- `hard_topk` 更快，预算语义略高，但会牺牲候选覆盖，不适合作为 SFT 主数据 baseline。
- `balanced_*` 明显提升餐饮多样性，但住宿类型、餐饮 grounding 和硬约束更弱，更适合 DPO/软偏好参考。
- 这个阶段已经暴露出一个问题：预算精确算术不应该完全交给 prompt，后续要工程重算。

## 4. 预算规则与业务口径消融

预算相关 prompt 是中间耗时最多的一组。它先经历了“算术规则怎么写”的尝试，再经历了“业务口径到底是什么”的修正。

第一批预算版本包括：

```text
budget_hard
budget_order
budget_fewshot
budget_symbolic
budget_ledger
budget_ledger_no_schema_numbers
```

主要发现：

- `budget_fewshot` 在规则指标上最高，但会复用示例里的具体数字，存在污染风险。
- `budget_symbolic` 去掉具体数字后更安全，能保留大部分预算收益。
- `budget_ledger` 明确“先写 days、再回扫 budget”，但 7B 仍会把景点和餐饮预算当估计值，而不是严格从字段派生。
- `budget_ledger_no_schema_numbers` 破坏 schema 稳定性，说明字段结构示例不能粗暴删除。

随后评测口径修正为当前业务口径：

- `hotel.estimated_cost` 是单间每晚房价，酒店预算按 `rooms = ceil(party.total / 2)` 计算。
- `meal.estimated_cost` 是人均单餐费用，餐饮预算按 `party.total` 计算。
- `attraction.ticket_price` 是成人单人门票，景点预算按 `party.total` 计算。

这一轮又跑过：

```text
budget_relation_lite
budget_relation_priority
budget_relation_self_check
room_person_price_lite
room_person_price_full
room_person_price_self_check
```

阶段结论：

- 新业务口径是对的，尤其是餐饮按人均价后，模型的餐饮尺度解释更自然。
- prompt 能小幅提醒房间数、人数和人均价，但不能稳定把这些关系反映到最终 `budget.total_*`。
- 因此后续策略改为：prompt 只负责讲清价格字段语义，最终预算由后端或数据生成链路重算。

## 5. 景点与餐饮专题消融

景点专题主要是防污染和去重：

```text
attraction_dedupe_only
attraction_source_guard_only
attraction_dedupe_source_guard
attraction_dedupe_source_self_check
```

结论是：景点 source guard 值得吸收，因为它能减少把 `food_pois`、`hotel_pois` 写进 attractions 的硬错；跨天景点去重更偏软质量，不适合继续作为强 prompt 规则堆叠。

餐饮专题则是整个 prompt 阶段最典型的“局部收益和全局退化互相拉扯”。下表沿用当时餐饮消融报告的字段，只用于说明版本间相对变化，不和最终 A/B/C/D 新口径重评混排：

| 版本 | schema | hard_pass | 餐饮多样性 | 午晚餐不重复 | 跨天重复限制 | 餐饮grounding | 餐饮语义合法 | 预算算术 | 预算偏好 | 餐饮唯一率avg |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 上一版 baseline / meal_diversity_symbolic | 98.67% | 40.54% | 52.70% | 71.62% | 67.23% | 87.16% | 88.51% | 88.51% | 97.64% | 72.57% |
| 次数限制版 / meal_count_limit_symbolic | 98.33% | 41.69% | 54.58% | 73.56% | 69.49% | 86.10% | 87.46% | 88.47% | 96.95% | 73.13% |
| 轮换版 / meal_rotation_symbolic | 98.00% | 44.22% | 55.78% | 70.07% | 70.41% | 89.46% | 90.48% | 90.14% | 99.32% | 74.29% |
| 强 grounding 多样性版 / meal_grounded_diversity_symbolic | 99.33% | 41.61% | 50.34% | 69.80% | 64.09% | 90.60% | 92.28% | 90.94% | 97.32% | 68.90% |

阶段结论：

- `meal_rotation_symbolic` 的软质量最好，但硬约束低于硬 baseline。
- 强化 grounding 会提升餐饮真实候选复制，但会压低多样性。
- 强化多样性又容易让模型编造泛化餐厅或牺牲预算/格式。
- 所以餐饮最终拆分：午晚餐真实候选、非空、非酒店晚餐属于 hard；多样性、菜系丰富、路线舒服属于 DPO 或后处理。

## 6. Self-check prompt 消融

这一轮测试了一个更强的自检 prompt：`room_person_price_self_check`。目标是看输出前内部自检能不能改善预算关系和餐饮重复。

历史对比对象：`hard_compact` vs `self_check_300`，全量 300 条。

| 指标 | baseline_hard_compact | self_check_300 | 变化 |
| --- | ---: | ---: | ---: |
| schema_ok | 98.7% | 97.7% | -1.0pp |
| sft_semantic | 4.4% | 4.8% | +0.4pp |
| budget_rel | 6.8% | 8.2% | +1.4pp |
| hotel_rel | 39.5% | 42.3% | +2.8pp |
| attraction_rel | 28.0% | 30.0% | +2.0pp |
| meal_scale | 87.2% | 79.5% | -7.6pp |
| budget_user | 81.4% | 78.8% | -2.6pp |
| budget_arith | 69.6% | 56.3% | -13.3pp |
| accommodation_type | 90.5% | 85.3% | -5.2pp |
| meal_ground | 96.6% | 91.8% | -4.8pp |
| meal_semantic | 97.3% | 92.8% | -4.5pp |
| meal_diversity | 6.8% | 22.2% | +15.4pp |
| same_day_meal_ok | 55.1% | 67.9% | +12.9pp |

阶段结论：

- self-check 对预算关系、酒店关系、景点关系有小幅帮助。
- 餐饮多样性明显改善，是这个块最亮的收益。
- 但它拉低了 schema、预算加总、住宿类型、餐饮 grounding 和餐饮语义合法性。
- 因此 self-check 不适合作为主 baseline，只能作为后续规则来源或 DPO 软偏好的参考。

这一步说明“让模型自己检查自己”不等于真实修复。自检会增加约束感，但也会让小模型在长 prompt、多目标和长 JSON 输出里牺牲其他硬指标。

## 7. A/B/C/D 重点组合消融重评

最后一轮围绕大模型建议的四个重点 prompt 块做单块和筛选组合消融，每组 300 条。本节数据已按新的 `meal_grounding_ok` 口径重评。

```text
baseline
A
B
C
D
A + C
A + D
B + C
B + D
C + D
A + C + D
B + C + D
```

四个块的含义：

- `A`：预算台账优先版，强化预算计算顺序、人数、房间数、分项加总。
- `B`：酒店住宿专治版，强化 `day.hotel` 是否代表当晚住宿，以及非 null hotel 计一晚。
- `C`：餐厅去重专治版，强化 lunch/dinner 必须来自 `food_pois`，并要求 used_count 去重。
- `D`：最终自检修复版，输出前内部检查 schema、天数、餐饮、预算和重复项。

重评主要结果：

| variant | schema_ok | budget_arithmetic | hotel_budget_covers | meal_budget | meal_diversity_ok | meal_grounding_ok | meal_grounding_rate |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| baseline | 99.00% | 50.51% | 36.36% | 0.00% | 71.38% | 56.23% | 83.28% |
| A | 98.67% | 55.07% | 35.81% | 0.00% | 70.27% | 56.08% | 82.90% |
| B | 96.00% | 46.53% | 38.54% | 0.00% | 72.57% | 60.76% | 85.16% |
| C | 98.33% | 46.10% | 37.63% | 0.00% | 68.14% | 49.15% | 82.67% |
| D | 98.67% | 49.66% | 36.49% | 0.00% | 73.65% | 58.11% | 84.09% |
| A_C | 99.33% | 58.72% | 40.27% | 0.34% | 66.11% | 52.68% | 82.95% |
| A_D | 100.00% | 49.67% | 36.00% | 0.33% | 71.67% | 59.33% | 83.65% |
| B_C | 76.67% | 46.96% | 42.17% | 0.00% | 60.00% | 59.57% | 87.38% |
| B_D | 99.33% | 48.32% | 37.92% | 0.00% | 74.83% | 58.72% | 83.99% |
| C_D | 100.00% | 45.00% | 37.00% | 0.00% | 71.00% | 51.00% | 82.88% |
| A_C_D | 99.67% | 54.18% | 38.13% | 0.00% | 68.90% | 56.19% | 83.21% |
| B_C_D | 94.33% | 45.23% | 36.40% | 0.00% | 66.43% | 51.59% | 82.96% |

阶段结论：

- `A_C` 仍是预算表现最好的组合：`budget_arithmetic_consistent = 58.72%`，`hotel_budget_covers_nights = 40.27%`。
- `A` 是唯一稳定提升预算加总的单块，从 baseline 的 50.51% 提升到 55.07%。
- `B` 对酒店预算覆盖有局部帮助，但 schema 风险明显；`B_C` 的 schema 只有 76.67%。
- `C` 没有稳定兑现餐厅去重收益，反而在新口径下暴露更多 grounding 问题；单独 `C` 的 `meal_grounding_ok` 为 49.15%。
- `D` 更像格式保险，不是能力提升；`A_C_D` 的预算加总低于 `A_C`。
- `meal_budget_consistent` 仍几乎全军覆没，说明餐饮总预算这种跨天、跨餐、乘人数的长 JSON 算术，已经超出 prompt-only 稳定能力。
- `meal_grounding_ok` 与 `meal_grounding_rate` 必须一起看：`A_C` 样本级只有 52.68%，但餐次级仍有 82.95%，说明模型大多数餐能复制候选，失败集中在少量餐次污染整条样本。

## 8. 最终冻结 baseline

最终冻结 `A_C`。

选择原因：

- schema 风险可控：`schema_ok = 99.33%`。
- 预算加总最佳：`budget_arithmetic_consistent = 58.72%`。
- 酒店预算覆盖相对最好的一档：`hotel_budget_covers_nights = 40.27%`。
- `meal_budget_consistent = 0.34%`，直接暴露 prompt-only 无法稳定处理餐饮预算乘人数。
- 新口径下 `meal_grounding_ok = 52.68%`，但 `meal_grounding_rate = 82.95%`，说明后续更适合用 deterministic meal repair 和 SFT 数据纠偏，而不是继续加 prompt。

没有改选 `B` 或 `A_D` 的原因也很清楚：`B` 的餐饮 grounding 较高，但 schema 和预算弱；`A_D` schema 更漂亮，但预算加总明显低于 `A_C`。本阶段的主目标是冻结一个能代表 prompt 上限、又方便后续 SFT/后处理接力的 baseline，`A_C` 仍然最合适。

## 9. Prompt 阶段总判断

整个 prompt 消融阶段走过七类尝试：

1. 调基础 Planner 协议、harder eval 和 no-route 口径。
2. 调上下文形态：确认 `hard_compact` 这类结构更适合作为稳定输入。
3. 调预算算术规则：确认 symbolic 比数字 few-shot 更安全，但 prompt 无法稳定精确回扫。
4. 调业务预算口径：确认房间数、人均餐费、景点单人票价必须写清楚，但预算要工程重算。
5. 调景点来源和去重：确认 source guard 是 hard，景点多样性/去重更适合 soft。
6. 调餐饮 grounding、兜底和多样性：确认午晚餐真实候选是 hard，多样性是 soft。
7. 调 self-check 和最终 A/B/C/D 组合：确认继续堆规则会产生约束淹没。

因此现在的判断很明确：

- prompt 能把任务边界、字段语义、候选来源、价格 hint 和预算口径讲清楚。
- prompt 不能稳定承担长 JSON 内部的跨字段算术和全局组合优化。
- 继续加规则会产生约束淹没，收益变小，副作用变大。
- 当前 7B base 在 prompt-only 条件下已经接近上限。

## 10. 后续方向

prompt 阶段结束后，主线切到工程和训练：

- 后端最终重算 `budget`，不要相信模型原始预算加总。
- 增加 deterministic `repair_meals(plan, context)`：午晚餐未命中 `food_pois` 时自动替换为真实候选，同一天午晚餐去重，替换后复制 `meal_cost_hint`。
- SFT 数据写入重算预算和 repair 后餐饮，让模型学习最终协议，而不是学习强模型算术错误或泛化餐名。
- SFT 重点学习 schema、字段口径、候选 grounding、价格 hint 和结构完整性。
- 餐饮多样性、路线质量、预算偏好贴合放到 DPO、规则后处理或候选选择策略里。

一句话总结：**`A_C` 是 Planner prompt 阶段的终版 baseline；prompt 已经尽责，真正的增量空间转向后端兜底和训练数据。**
