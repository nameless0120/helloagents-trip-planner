# V3 预算二次修正实验：Patch + 工程验收

本实验验证“调两次模型”的可行性，但第二次模型不再重写完整计划，而是只输出替换 patch：

1. 第一轮使用已有 base / SFT 生成结果。
2. 工程侧按选中酒店、景点、餐饮价格重算预算。
3. 对预算不贴合样本，第二轮模型只输出 `replace_hotel / replace_meal / replace_attraction` patch。
4. 工程侧应用 patch、回填预算、重新评测。
5. 只有当预算 hard/fit 变成通过，且 schema、grounding、多样性等已通过项不回退时，patch 才被接受；否则回滚原计划。

## 最终口径：Guarded Patch

| 模型 | revision_attempted | patch_accepted | budget 已贴合跳过 | postprocess 失败 |
|---|---:|---:|---:|---:|
| Base A_C | 226 | 10 | 72 | 2 |
| SFT cp2 A_C | 213 | 6 | 85 | 2 |

| 指标 | Base Before | Base After | 变化 | SFT Before | SFT After | 变化 |
|---|---:|---:|---:|---:|---:|---:|
| `planner_draft_hard_pass` | 134/300 = 44.67% | 136/300 = 45.33% | +0.66 pp | 189/300 = 63.00% | 189/300 = 63.00% | +0.00 pp |
| `budget_selection_ok` | 72/300 = 24.00% | 82/300 = 27.33% | +3.33 pp | 85/300 = 28.33% | 91/300 = 30.33% | +2.00 pp |
| `draft_budget_fit_pass` | 28/300 = 9.33% | 35/300 = 11.67% | +2.34 pp | 60/300 = 20.00% | 64/300 = 21.33% | +1.33 pp |
| `recomputed_budget_hard_ok` | 115/300 = 38.33% | 119/300 = 39.67% | +1.34 pp | 125/300 = 41.67% | 127/300 = 42.33% | +0.66 pp |
| `meal_grounding_ok` | 157/300 = 52.33% | 157/300 = 52.33% | +0.00 pp | 209/300 = 69.67% | 209/300 = 69.67% | +0.00 pp |
| `attraction_grounding_ok` | 296/300 = 98.67% | 296/300 = 98.67% | +0.00 pp | 280/300 = 93.33% | 280/300 = 93.33% | +0.00 pp |
| `attraction_diversity_ok` | 265/300 = 88.33% | 265/300 = 88.33% | +0.00 pp | 209/300 = 69.67% | 209/300 = 69.67% | +0.00 pp |
| `meal_diversity_ok` | 197/300 = 65.67% | 197/300 = 65.67% | +0.00 pp | 223/300 = 74.33% | 223/300 = 74.33% | +0.00 pp |

## 对照观察

完整重写 TripPlan 的二次模型修正不可取。20 条 smoke 中，full-plan rewrite 大量丢 schema、丢 `overall_suggestions`、把 `day.accommodation` 写成 null，导致草案质量明显下降。

不加验收门的 patch 也不可直接上线。它能更积极地提升预算贴合：

- Base `budget_selection_ok`: 24.00% -> 27.67%
- SFT `budget_selection_ok`: 28.33% -> 32.33%

但代价是多样性明显回退：

- Base `attraction_diversity_ok`: 88.33% -> 78.00%
- SFT `attraction_diversity_ok`: 69.67% -> 53.67%
- SFT `meal_diversity_ok`: 74.33% -> 69.00%

所以工程侧必须有 accept/reject guard。

## 结论

二次模型 patch 能安全带来小幅预算改善，但幅度有限：

- Base `budget_selection_ok` 提升 +3.33 pp。
- SFT `budget_selection_ok` 提升 +2.00 pp。
- SFT 的草案硬通过率保持 63.00%，没有被预算修正破坏。

这说明“二次模型修正”可以作为一个保守增强层，但不能单独解决预算贴合。模型经常能意识到应该换便宜/更贵的候选，但给出的 patch 被工程验收门拒绝很多，原因通常是预算没有真正变成通过，或会破坏 grounding / 多样性 / schema。

## 推荐工程方案

线上预算链路建议定为：

1. SFT 模型生成 `TripPlanDraft`。
2. 工程侧从候选 POI 回填价格并计算 `computed_budget`。
3. 如果预算不贴合，调用模型输出 patch，而不是重写完整计划。
4. 工程侧应用 patch 到原计划副本。
5. 重新计算预算和规则指标。
6. 只有预算变好且硬规则不回退，才接受 patch。
7. 如果仍不贴合，进入 deterministic greedy repair/rerank。

短期不需要重新造 SFT 数据。现有 SFT 仍然负责草案质量；预算修正作为推理时工程闭环。后续如果要训练 revision 模型，可以把本实验中 `patch_accepted=true` 的样本沉淀成低成本 revision SFT 数据。

## 产物

- Base guarded report: `training/outputs/eval/budget_revision_patch_guarded_v2_base_A_C_300/budget_revision_report.md`
- SFT guarded report: `training/outputs/eval/budget_revision_patch_guarded_v2_sft_cp2_A_C_300/budget_revision_report.md`
- 当前评测入口：`training/scripts/run_pipeline.py --stage eval`；产品侧预算修正和候选选择逻辑见 `backend/app/planner/`。
