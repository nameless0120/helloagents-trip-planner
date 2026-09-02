# V3 两层 Pass 口径对比

| 版本 | sft_hard_pass | dpo_soft_pass | legacy_hard_pass | schema | 预算算术 | 餐饮语义合法 | 餐饮grounding | 餐饮多样性 | 预算偏好 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 上一版 baseline / meal_diversity_symbolic | 75.34% | 38.85% | 40.54% | 98.67% | 88.51% | 88.51% | 87.16% | 52.70% | 97.64% |
| 次数限制版 / meal_count_limit_symbolic | 75.93% | 39.66% | 41.69% | 98.33% | 88.47% | 87.46% | 86.10% | 54.58% | 96.95% |
| 轮换版 / meal_rotation_symbolic | 77.89% | 43.20% | 44.22% | 98.00% | 90.14% | 90.48% | 89.46% | 55.78% | 99.32% |
| 强 grounding 多样性版 / meal_grounded_diversity_symbolic | 80.87% | 39.93% | 41.61% | 99.33% | 90.94% | 92.28% | 90.60% | 50.34% | 97.32% |

## 口径

- `sft_hard_pass`：SFT 阶段可训练/可过滤的硬约束，不包含餐饮多样性、预算档位偏好等软质量项。
- `dpo_soft_pass`：在 `sft_hard_pass` 基础上进一步要求餐饮多样性、严格餐饮 grounding、预算偏好对齐，用于衡量 DPO 该优化的空间。
- `legacy_hard_pass`：旧口径，保留用于和历史报告对齐。
