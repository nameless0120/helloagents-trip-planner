# SFT 与 Base 阶段评估报告

更新时间：2026-05-02

本文记录当前 `Base Qwen2.5-7B-Instruct + Planner Prompt v3` 与 `sft_v2_clean + Planner Prompt v3` 在同一套 v2 eval 集上的阶段性结论。当前结论用于阶段复盘和后续 DPO 方案设计，不代表最终模型效果。

## 1. 评估对象

| 实验 | 模型 | Prompt | 评估集 | 输出目录 |
| --- | --- | --- | --- | --- |
| Base baseline | `Qwen2.5-7B-Instruct` | `backend/app/agents/prompts.py:PLANNER_AGENT_PROMPT` | `training/data/v2/sft/records_eval.jsonl` | `training/outputs/eval/base_qwen25_7b_prompt_v3` |
| SFT v2 clean | `Qwen2.5-7B-Instruct + LoRA sft_v2_clean` | 同上 | 同上 | `training/outputs/eval/sft_v2_clean_prompt_v3` |

本轮评估使用同一套 91 条 eval 样本，temperature 为 `0.2`，单 worker 顺序生成，规则评估口径对应当前 `training/scripts/eval/eval_rule_metrics.py`。

## 2. Baseline 是否已经落盘

已经落盘。

Base baseline 的关键产物：

- `training/outputs/eval/base_qwen25_7b_prompt_v3/generation_config.json`
- `training/outputs/eval/base_qwen25_7b_prompt_v3/generations.jsonl`
- `training/outputs/eval/base_qwen25_7b_prompt_v3/rule_eval_report.md`
- `training/outputs/eval/base_qwen25_7b_prompt_v3/rule_eval_report.json`
- `training/outputs/eval/base_qwen25_7b_prompt_v3/prompts.py.snapshot`

其中 `generation_config.json` 记录了：

- `model_name`: `base_qwen25_7b_prompt_v3`
- `api_model`: `trip-planner-base`
- `records`: `training/data/v2/sft/records_eval.jsonl`
- `system_prompt_source`: `backend/app/agents/prompts.py:PLANNER_AGENT_PROMPT`

同时已经保存当前 `prompts.py` 快照，避免后续 prompt 修改后无法复现本轮 baseline。

## 3. 核心结果对比

| 指标 | Base + prompt v3 | SFT + prompt v3 | 判断 |
| --- | ---: | ---: | --- |
| JSON 提取成功率 | 91/91，100.00% | 91/91，100.00% | 持平 |
| Schema 通过率 | 91/91，100.00% | 90/91，98.90% | SFT 略差 |
| Hard pass | 84/91，92.31% | 89/90，98.89% | SFT 更好 |
| 景点数量合规 | 84/91，92.31% | 90/90，100.00% | SFT 更好 |
| 中间天酒店合法 | 91/91，100.00% | 90/90，100.00% | 持平 |
| 酒店 grounding | avg 1.0000 | avg 0.9889 | SFT 略差 |
| 景点 grounding | avg 0.9963 | avg 0.9981 | 基本持平 |
| 日期范围正确 | 91/91，100.00% | 89/90，98.89% | SFT 略差 |
| 天气匹配 | 91/91，100.00% | 90/90，100.00% | 持平 |
| 预算算术一致 | 89/91，97.80% | 79/90，87.78% | SFT 明显更差 |
| 预算不超用户预算 | 89/91，97.80% | 89/90，98.89% | 基本持平 |
| 预算档位对齐 | 77/91，84.62% | 61/90，67.78% | SFT 明显更差 |
| 预算偏好对齐 | 76/91，83.52% | 60/90，66.67% | SFT 明显更差 |
| 平均延迟 | 41.18s | 51.99s | SFT 更慢 |

## 4. 当前 SFT 学到了什么

当前 SFT 不是完全无效。它确实学到了一部分任务协议：

- 更稳定地控制每天景点数量，`attraction_count_ok` 从 92.31% 提升到 100.00%。
- 能稳定输出旅行计划 JSON，`json_extract_ok` 为 100.00%。
- 大部分后端 schema 字段、天气日期、餐饮完整性、中间天酒店约束都能遵守。
- 输出风格更接近强模型蒸馏数据，文本更长、更像完整旅行方案。

因此，这版 SFT 可以证明：

```text
模型能够通过 SFT 学会 TripPlan 结构和部分硬规则。
```

## 5. 当前 SFT 失败在哪里

当前 SFT 的主要失败不在 JSON 格式，而在预算和决策质量。

Base 的失败类型：

```json
{
  "budget_preference_mismatch": 15,
  "budget_arithmetic_inconsistent": 2
}
```

SFT 的失败类型：

```json
{
  "budget_preference_mismatch": 30,
  "budget_arithmetic_inconsistent": 11,
  "schema": 1
}
```

可以看到，SFT 在预算相关指标上明显退化。具体表现包括：

- 高预算、豪华预算用户仍然得到偏廉价方案。
- `budget.total` 与分项加总在生成时更容易出现偏差。
- 有一条样本出现日期复制错误，将 `2026-05-06` 写成了 `2026-06-06`。
- SFT 输出平均更长，推理速度更慢。

这说明当前 SFT 更像是在模仿训练数据的“行程模板”，但没有稳定学到“按预算和用户偏好做更好决策”。

## 6. 数据侧排查结论

对当前 v2 SFT 数据预算做了检查：

| 数据 | 样本数 | 严格预算加总不等 | 评估容差下预算算术不一致 | 预算偏好不对齐 |
| --- | ---: | ---: | ---: | ---: |
| `records_clean.jsonl` | 909 | 4，0.44% | 0 | 172，18.92% |
| `records_train.jsonl` | 773 | 2，0.26% | 0 | 145，18.76% |
| `records_val.jsonl` | 45 | 0 | 0 | 12，26.67% |
| `records_eval.jsonl` | 91 | 2，2.20% | 0 | 15，16.48% |

结论：

- `budget.total != 各项之和` 不是训练数据里的主要污染源。
- 训练数据里的预算算术整体较干净。
- 更大的问题是预算偏好信号不够干净，约 18.9% 的 clean 样本与预算档位不对齐。
- SFT 生成阶段预算算术退化，更像是 LoRA 对基模原有计算/汇总能力造成了损伤，而不是简单模仿了错误加总。

## 7. 当前阶段判断

当前最合理的阶段结论是：

```text
Base Qwen2.5-7B-Instruct + Planner Prompt v3 已经是强 baseline。
当前 SFT v2 clean 证明了结构学习有效，但没有证明整体决策质量优于 baseline。
```

这版 SFT 适合作为：

- 后训练工程链路跑通证明。
- TripPlan 结构学习和硬规则学习的实验样本。
- 后续 DPO 的候选模型之一。

它暂时不适合作为：

- 线上默认 Planner 模型。
- “SFT 显著优于 Base” 的效果证明。

## 8. 后续方向

### 8.1 冻结强 baseline

将 `base_qwen25_7b_prompt_v3` 作为当前正式 baseline。后续所有 SFT、DPO、SFT+DPO 都应和它对比。

Baseline 的优势是：

- JSON/schema 稳定。
- grounding 和天气匹配稳定。
- 预算算术和预算偏好目前优于 SFT。
- 不需要 adapter，推理更快。

### 8.2 SFT 不再作为主要提效路线

SFT 可以小修，但不建议继续大规模堆数据硬训。

如果后续要再训 SFT，建议只做保守改动：

- 清掉预算偏好明显不对齐样本。
- 清掉日期复制、schema、酒店异常样本。
- 降低 epoch 或学习率，减少对基模能力的损伤。
- 让 SFT 继续承担“任务格式 warm-up”，不要期待它单独学会复杂决策偏好。

### 8.3 DPO 阶段学习决策质量

当前项目仍有 DPO 阶段，DPO 更适合学习：

- 高预算时如何提升酒店、餐饮和体验质量。
- 低预算时如何控制总价但不牺牲核心体验。
- 亲子、老人、情侣、朋友、独行等同行类型下的节奏差异。
- 雨天、高温、历史天气、远期天气不可用时的行程取舍。
- 多候选计划中哪个更符合用户偏好。

推荐的 DPO 数据构造方式：

```text
同一个 PlannerContext
  -> Base 生成候选
  -> SFT 生成候选
  -> 强模型低温生成候选
  -> 强模型高温生成候选
  -> Judge 按预算、偏好、grounding、天气、节奏、可执行性评分
  -> chosen = 高分且结构合法的自然候选
  -> rejected = 低分但结构合法的自然候选
```

DPO 不应该再使用“手工把一个字段改坏”的偏好对。那种数据只能证明训练链路能跑，不能证明模型学到了真实偏好。

## 9. 一句话总结

```text
Prompt v3 已经把 Base 打造成强 baseline；当前 SFT 学会了结构和部分硬规则，但预算/偏好决策退化。下一阶段应冻结 Base baseline，把主要改进目标转向 DPO 的多候选偏好学习。
```
