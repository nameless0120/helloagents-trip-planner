# V3 Prompt Baseline

更新时间：2026-05-03

这一版正式冻结为 v3 prompt baseline，用于后续 SFT、DPO 和更难评估集对比。

## Baseline 身份

- baseline 名称：`base_qwen25_7b_v3_hard_attr_prompt_w8`
- 基座模型：Qwen2.5-7B-Instruct
- adapter：无
- prompt：当前 `backend/app/agents/prompts.py` + `backend/app/agents/planner_query.py`
- 关键 prompt 修复：每天 `attractions` 必须包含 1-3 个景点；到达日、返程日、慢节奏、老人/亲子场景也至少安排 1 个轻量景点，不允许用休息、自由活动、返程替代景点。
- eval records：`training/data/v3/eval_hard_prompt_attraction_required/records.jsonl`
- 生成后端：vLLM
- 并发：8 workers
- 温度：0.2

## 关键指标

| 指标 | 结果 |
| --- | ---: |
| API 调用成功 | 120/120 |
| JSON 可解析 | 119/120 = 99.17% |
| Schema 通过 | 118/120 = 98.33% |
| hard_pass | 115/118 = 97.46% |
| attraction_count_ok | 117/118 = 99.15% |
| budget_arithmetic_consistent | 116/118 = 98.31% |
| budget_within_user_budget | 118/118 = 100.00% |
| hotel_budget_covers_nights | 118/118 = 100.00% |
| weather_match | 118/118 = 100.00% |
| attraction_grounding_rate 平均 | 99.89% |
| hotel_grounding_rate 平均 | 100.00% |

## 与上一版 hard baseline 对比

| 指标 | 旧版 `base_qwen25_7b_v3_hard` | 当前 baseline |
| --- | ---: | ---: |
| JSON 可解析 | 98.33% | 99.17% |
| Schema 通过 | 97.50% | 98.33% |
| hard_pass | 64.96% | 97.46% |
| attraction_count_ok | 69.23% | 99.15% |
| budget_arithmetic_consistent | 97.44% | 98.31% |
| weather_match | 99.15% | 100.00% |

## 结论

当前 base + v3 prompt 已经满足 v3 baseline 验收线。后续不应再把 SFT 的主要目标设为“修 JSON/修 schema/修每天景点数”。

下一阶段更适合转向：

- 更难评估集：验证复杂约束、预算冲突、雨天路线、多人同行和长上下文下的稳定性。
- DPO：在结构合法的候选之间学习预算质量、偏好对齐、路线舒适度、天气意识和文本可用性。
