# Prompt Baseline Freeze

冻结日期：2026-05-05

## 冻结结论

后续 Planner prompt baseline 使用 `A_C`。

- 来源评估：`training/outputs/eval/prompt_ablation_20260505/batch_summary.md`
- 评估记录：`training/data/v3/eval_harder_prompt_ablation_20260505/A_C/records.jsonl`
- 后端入口：`backend/app/agents/prompts.py::PLANNER_AGENT_PROMPT`
- prompt_sha256：`dbe3f951082929b5de41e3de38f823356dd94a01896d81246e447d80a196e5c0`

## 关键指标

| variant | records | schema_ok | budget_arithmetic_consistent | hotel_budget_covers_nights | meal_budget_consistent | meal_diversity_ok | meal_grounding_ok | meal_grounding_rate |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| A_C | 300 | 99.33% | 58.72% | 40.27% | 0.34% | 66.11% | 52.68% | 82.95% |

## 后续取舍

- 不再继续主线调 prompt；这轮消融显示 7B 在长 prompt、餐厅去重和预算算术上已经接近 prompt-only 上限。
- `budget` 生产侧继续以后端重算兜底，SFT 数据也使用当前 `recompute_budget()` 写入重算后的预算。
- C 块会拉低餐饮多样性，但 A+C 是预算收益最明确且 schema 风险可控的组合，适合作为下一轮 SFT 起点。
- 当前 `training/data/v3/sft/records.jsonl` 里的 smoke records 不是这个 prompt hash；正式 SFT 前应先归档旧 smoke，再用本 baseline 重新生成。
