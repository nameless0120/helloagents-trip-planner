# V3 餐饮 Prompt 消融对比

| 版本 | schema | hard_pass | 餐饮多样性 | 午晚餐不重复 | 跨天重复限制 | 餐饮grounding | 餐饮语义合法 | 预算算术 | 预算偏好 | 餐饮唯一率avg |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 上一版 baseline / meal_diversity_symbolic | 98.67% | 40.54% | 52.70% | 71.62% | 67.23% | 87.16% | 88.51% | 88.51% | 97.64% | 72.57% |
| 次数限制版 / meal_count_limit_symbolic | 98.33% | 41.69% | 54.58% | 73.56% | 69.49% | 86.10% | 87.46% | 88.47% | 96.95% | 73.13% |
| 轮换版 / meal_rotation_symbolic | 98.00% | 44.22% | 55.78% | 70.07% | 70.41% | 89.46% | 90.48% | 90.14% | 99.32% | 74.29% |
| 强 grounding 多样性版 / meal_grounded_diversity_symbolic | 99.33% | 41.61% | 50.34% | 69.80% | 64.09% | 90.60% | 92.28% | 90.94% | 97.32% | 68.90% |

## 初步结论

- 轮换版 hard_pass 最高，预算算术、预算偏好也最好，是当前规则指标下最值得进 judge100 的候选。
- 强 grounding 多样性版提升了餐饮 grounding 和语义合法率，但重复问题更严重，hard_pass 反而下降。
- 次数限制版略优于上一版 baseline，但收益不如轮换版。

## 报告路径

- 上一版 baseline / meal_diversity_symbolic: `training/outputs/eval/base_qwen25_7b_v3_harder_meal_diversity_symbolic_w16/rule_eval_report.json`
- 次数限制版 / meal_count_limit_symbolic: `training/outputs/eval/base_qwen25_7b_v3_harder_ablation_meal_count_limit_symbolic_w12/rule_eval_report.json`
- 轮换版 / meal_rotation_symbolic: `training/outputs/eval/base_qwen25_7b_v3_harder_ablation_meal_rotation_symbolic_w12/rule_eval_report.json`
- 强 grounding 多样性版 / meal_grounded_diversity_symbolic: `training/outputs/eval/base_qwen25_7b_v3_harder_ablation_meal_grounded_diversity_symbolic_w12/rule_eval_report.json`
