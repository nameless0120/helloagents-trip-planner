# V3 SFT CP2 重算预算选择能力对比

日期：2026-05-06

## 目标

验证一个新的预算评测思路：

不看模型自己写的 `budget.total` 是否算对，而是根据模型已经选出来的
酒店、景点、餐饮分项价格重新计算真实总预算，再判断这个选择组合是否贴合用户预算。

这回答的是：

> 模型虽然算不明白总账，但它有没有学会选择一个预算合理的方案？

## 重算口径

从模型输出中读取已选 item 的价格：

- `hotel.estimated_cost`：单间每晚价。
- `attraction.ticket_price`：成人单人票价。
- `meal.estimated_cost`：人均单餐价。
- `budget.total_transportation`：整趟本地交通估算，暂时沿用模型输出。

然后按确定性公式重算：

```text
rooms = ceil(party.total / 2)
recomputed_total_hotels = sum(day.hotel.estimated_cost * rooms)
recomputed_total_attractions = sum(attraction.ticket_price) * party.total
recomputed_total_meals = sum(meal.estimated_cost) * party.total
recomputed_total = recomputed_total_hotels
                 + recomputed_total_attractions
                 + recomputed_total_meals
                 + total_transportation
```

## 对比对象

- Eval 集：`training/data/v3/eval_harder_prompt_ablation_20260505/A_C/records.jsonl`
- Base 生成：`training/outputs/eval/prompt_ablation_20260505/base_qwen25_7b_prompt_ablation_20260505_A_C/generations.jsonl`
- SFT 生成：`training/outputs/eval/sft_qwen25_7b_v3_1000_cp2_v1_A_C_w8/generations.jsonl`
- Base 报告：`training/outputs/eval/base_qwen25_7b_prompt_ablation_20260505_A_C_recomputed_budget/rule_eval_report.md`
- SFT 报告：`training/outputs/eval/sft_qwen25_7b_v3_1000_cp2_v1_A_C_w8_recomputed_budget/rule_eval_report.md`

## 核心指标

| 指标 | 含义 | Base A_C | SFT CP2 | 变化 |
| --- | --- | ---: | ---: | ---: |
| `recomputed_budget_hard_ok` | hard budget 下，重算后不超预算 | 38.59% | 41.95% | +3.36pp |
| `recomputed_budget_within_user_budget` | 重算后不明显超用户预算 | 51.34% | 48.99% | -2.35pp |
| `recomputed_budget_level_aligned` | 重算后落在预算档位/target 区间 | 24.16% | 28.52% | +4.36pp |
| `recomputed_budget_fit_ok` | hard 不超 + 档位贴合 | 24.16% | 28.52% | +4.36pp |
| `budget_selection_ok` | 同 `recomputed_budget_fit_ok` | 24.16% | 28.52% | +4.36pp |
| `dpo_soft_recomputed_budget_pass` | hard pass + 餐饮/景点软项 + 重算预算贴合 | 5.03% | 11.74% | +6.71pp |

## 重算预算分布

| 指标 | Base A_C | SFT CP2 | 变化 |
| --- | ---: | ---: | ---: |
| 平均 `recomputed_budget_total` | 7879.46 | 7746.97 | -132.49 |
| P50 `recomputed_budget_total` | 6680.00 | 6758.00 | +78.00 |
| P90 `recomputed_budget_total` | 13244.00 | 13375.00 | +131.00 |
| 平均 `recomputed_budget_per_person_day` | 698.38 | 680.05 | -18.34 |
| P50 `recomputed_budget_per_person_day` | 632.00 | 603.78 | -28.22 |
| P90 `recomputed_budget_per_person_day` | 1117.75 | 1147.00 | +29.25 |

## 对照：模型自报预算

| 指标 | Base A_C | SFT CP2 | 变化 |
| --- | ---: | ---: | ---: |
| `budget_preference_aligned` | 34.56% | 57.05% | +22.49pp |
| `budget_user_constraint_ok` | 82.21% | 77.18% | -5.03pp |
| `budget_arithmetic_consistent` | 58.72% | 74.16% | +15.44pp |
| `meal_budget_consistent` | 0.34% | 0.00% | -0.34pp |

注意：模型自报预算看起来提升很大，但用已选 item 重算后，预算贴合只从
24.16% 到 28.52%。这说明 SFT 学会了一部分“把 budget 字段写得更像样”，但还没有充分学会“选择本身贴预算”。

## 结论

1. 这个评测思路是必要的：它把“模型算不算得对”和“模型选得贵不贵”拆开了。
2. SFT CP2 在真实预算选择上有小幅提升，但不够强：
   - `recomputed_budget_fit_ok` 只提升 +4.36pp。
   - `recomputed_budget_hard_ok` 只提升 +3.36pp。
3. 因此，仅靠现有 SFT 数据还不能证明模型真正学会预算贴合。
4. 线上如果只做工程重算，可以修正展示数字，但不能保证不超支/不少用。
5. 下一步若预算贴合是核心业务目标，需要让模型更容易感知“选择成本”，或用 rerank/repair 兜底。

## 建议

短期：

- 主报告保留 `recomputed_budget_fit_ok` 和 `budget_selection_ok`。
- 预算展示用工程重算。
- hard budget 场景上线前加 deterministic repair 或候选 rerank。

中期：

- PlannerContext 增加成本提示，减少模型心算压力：
  - `rooms`
  - `lodging_nights`
  - `target_min_total`
  - `target_max_total`
  - hotel 的整趟住宿成本 hint
  - attraction 的团体门票成本 hint
  - meal 的团体单餐成本 hint
- SFT 数据可本地重算 budget，不必重新花钱生成整条行程。

长期：

- 预算贴合更适合做多候选 rerank / repair：
  - 先让模型生成合法候选。
  - 工程重算真实成本。
  - 超预算或过省时替换酒店、餐饮、高价景点。
  - DPO 学“预算贴合但体验不差”的偏好，而不是学精确乘法。
