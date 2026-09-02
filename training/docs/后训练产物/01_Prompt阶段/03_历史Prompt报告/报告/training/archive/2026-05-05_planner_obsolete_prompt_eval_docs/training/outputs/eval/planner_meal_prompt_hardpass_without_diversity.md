# V3 Prompt 消融：不把餐饮多样性计入 hard_pass

口径：当前 hard_pass 去掉 `meal_diversity_ok`，其余硬指标不变。`meal_complete`、`meal_specific_ok`、`meal_valid_semantics_ok` 仍保留。

| 版本 | 原 hard_pass | 去掉多样性 hard_pass | 提升 | 通过数/schema_ok | 餐饮多样性 | 餐饮语义合法 | 预算算术 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 上一版 baseline / meal_diversity_symbolic | 40.54% | 76.01% | 35.47% | 225/296 | 52.70% | 88.51% | 88.51% |
| 次数限制版 / meal_count_limit_symbolic | 41.69% | 76.27% | 34.58% | 225/295 | 54.58% | 87.46% | 88.47% |
| 轮换版 / meal_rotation_symbolic | 44.22% | 79.25% | 35.03% | 233/294 | 55.78% | 90.48% | 90.14% |
| 强 grounding 多样性版 / meal_grounded_diversity_symbolic | 41.61% | 82.55% | 40.94% | 246/298 | 50.34% | 92.28% | 90.94% |

## 观察

- 去掉餐饮多样性后，四版 hard_pass 都会明显上升，说明当前主要瓶颈之一确实是质量偏好项，而不是 JSON/schema/日期/酒店/天气等基础格式。
- 轮换版依然最好，说明它不是单纯靠多样性指标取胜，而是在预算算术、餐饮语义、grounding 等指标上也比较稳。
- 餐饮多样性更适合进入 DPO/LLM judge 或作为软质量指标，而不是继续作为 SFT 前的硬过滤主门槛。
