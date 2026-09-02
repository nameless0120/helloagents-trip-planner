# V3 提示词阶段总结报告

更新时间：2026-05-05

本文总结 v3 阶段 prompt 调优的结果，并明确后续后训练 baseline 的选择。

## 1. 阶段结论

v3 prompt 调优已经可以收尾。

核心原因：

- base 模型在严格结构、日期、天气、住宿、预算账本等确定性协议上已经能达到较高水平。
- 继续调 prompt 会在“硬约束稳定性”和“软质量偏好”之间来回拉扯。
- 餐饮多样性、预算花得是否舒服、路线是否更自然、偏好权衡是否像真实旅行顾问，这些更适合进入 DPO，而不是继续塞进 system prompt。

当前评估口径已经拆成两层：

| 指标 | 阶段定位 | 说明 |
| --- | --- | --- |
| `sft_hard_pass` | 硬约束 | JSON/schema/日期/天气/酒店/预算算术/基础餐饮合法性等线上可用性指标 |
| `dpo_soft_pass` | 软质量 | 在硬约束通过基础上，进一步要求景点不重复、餐饮多样性、严格餐饮 grounding、预算偏好对齐 |
| `legacy_hard_pass` | 历史兼容 | 旧口径，把多样性也混入 hard pass，仅用于旧报告对比 |

## 2. 评估设置

主要评估集：

```text
training/data/v3/eval_harder_*/records.jsonl
```

主要模型：

```text
Qwen2.5-7B-Instruct base
```

主要评估输出：

```text
training/outputs/eval/v3_prompt_two_stage_pass_all_history.md
training/outputs/eval/v3_two_stage_pass_summary.md
```

所有 full-run prompt 报告已经用当前 `training/scripts/eval/eval_rule_metrics.py` 重算。

## 3. Prompt 调优过程中的关键发现

### 3.1 粗 route_hints 不适合作为上下文

早期 `route_hints` 只是直线距离或半成品路线信号，会让模型围绕不可靠信息解释行程。

阶段决策：

```text
当前 v3 先去掉粗 route_hints。
把酒店、景点、餐饮候选的地址、区域、坐标交给模型自行判断。
真实路线 API 作为后续工程增强，写入 TODO。
```

### 3.2 预算口径必须符号化，而不是放具体数字 few-shot

预算相关 prompt 修复后，模型对下面这些规则理解更稳定：

- `hotel.estimated_cost` 是整组人每晚住宿费用。
- `total_hotels = 每晚费用 × lodging_nights`。
- `meal.estimated_cost` 是整组人单餐费用，不再乘人数。
- `attraction.ticket_price` 是单人门票。
- `total_attractions = 门票和 × party.total`。
- `budget.total = attractions + hotels + meals + transportation`。

但带具体数字的 few-shot 有污染风险，模型可能复用示例数字或示例结构。

阶段决策：

```text
保留符号化预算规则。
避免在 system prompt 中放完整 TripPlan 示例和具体预算数字 few-shot。
```

### 3.3 餐饮问题是 prompt 上限最明显的部分

餐饮问题经历了几轮修复：

- 禁止 `早餐推荐/午餐推荐/晚餐推荐` 等占位名称。
- 禁止 `无/酒店晚餐/酒店午餐` 等非法 fallback。
- 允许酒店/民宿/客栈早餐作为 breakfast fallback。
- 午餐和晚餐尽量从真实 `food_pois` 里选择。
- 同一天午晚餐尽量不要同一家。
- 跨天不要高频重复同一家；酒店早餐不计入多样性。

结果说明：

```text
prompt 可以显著改善餐饮具体性和部分多样性，
但无法稳定同时保证硬约束、严格 grounding、多样性和预算算术。
```

因此餐饮多样性应进入 DPO 软质量，而不是继续作为 SFT 硬约束。

## 4. 历史 Prompt 对比

完整表见：

```text
training/outputs/eval/v3_prompt_two_stage_pass_all_history.md
```

关键版本：

| 版本 | `sft_hard_pass` | `dpo_soft_pass` | 说明 |
| --- | ---: | ---: | --- |
| `base_qwen25_7b_v3_harder_baseline_symbolic_w16_rerun` | 88.55% | 8.42% | 硬约束稳定，但餐饮重复严重 |
| `base_qwen25_7b_v3_harder_ablation_meal_rotation_symbolic_w12` | 77.89% | 43.20% | 软质量最好，但硬约束下降 |
| `base_qwen25_7b_v3_harder_ablation_meal_grounded_diversity_symbolic_w12` | 80.87% | 39.93% | 餐饮 grounding/语义较好，但重复问题仍明显 |
| `base_qwen25_7b_v3_harder_food_bucket_return_dinner_prompt_w8` | 82.59% | 38.57% | 折中版本 |

解读：

- 硬约束最强版本和软质量最强版本不是同一版。
- 这说明 prompt 已经接近上限：继续调 prompt 会牺牲某一侧。
- 后训练阶段应该利用这个差异构造偏好数据，而不是继续追求一个万能 prompt。

## 5. Baseline 决策

后续报告和训练中固定两类 baseline。

### 5.1 硬约束 baseline

```text
base_qwen25_7b_v3_harder_baseline_symbolic_w16_rerun
```

用途：

- 作为 base 模型协议执行能力的主要对照。
- 证明 base + v3 prompt 能稳定执行旅行计划结构协议。
- DPO 训练后，`sft_hard_pass` 不应低于这类硬约束 baseline 太多。

选择理由：

- `sft_hard_pass = 88.55%`
- `schema_ok = 99.00%`
- `budget_arithmetic_consistent = 93.94%`
- 餐饮重复严重，正好说明它不是软质量终点。

### 5.2 软质量 prompt-only baseline

```text
base_qwen25_7b_v3_harder_ablation_meal_rotation_symbolic_w12
```

用途：

- 作为 prompt-only 软质量上限对照。
- DPO 需要超过它，或者在不牺牲硬约束的情况下接近它。

选择理由：

- `dpo_soft_pass = 43.20%`，当前最高。
- 餐饮多样性、预算偏好和整体软质量明显优于硬约束 baseline。
- 但 `sft_hard_pass = 77.89%`，不适合作为唯一正式 baseline。

### 5.3 折中参考版本

```text
base_qwen25_7b_v3_harder_food_bucket_return_dinner_prompt_w8
```

用途：

- 作为工程折中参考。
- 如果需要一版“线上可看”的 prompt，可参考它的折中策略。

但后训练主线不以它为唯一基线。

## 6. 后训练怎么接

### 6.1 不建议继续大规模 SFT

当前 SFT 的收益不明确：

- 之前 v2 SFT 已经暴露过，数据稍脏会把 base 能力训窄。
- 当前 base + prompt 已经能解决大部分结构协议。
- 剩余主要问题不是“不会输出格式”，而是“合法候选里哪个更好”。

因此 SFT 暂时作为可选补充：

```text
只有当 DPO 数据池里发现大量稳定硬错，才回头补小规模 SFT。
```

### 6.2 DPO 数据构造原则

DPO 不训练坏 JSON 或坏 schema。

候选进入 pair 之前，必须先通过 `sft_hard_pass` 或等价硬过滤：

- JSON/schema 通过。
- 日期、天气、酒店、预算算术正确。
- 餐饮不是占位/无/酒店晚餐等非法名称。
- 中间住宿日酒店不为空。
- 基础 grounding 不严重越界。

然后再用软质量分选择 chosen/rejected：

- 餐饮多样性。
- 餐饮是否更像真实旅游用餐。
- 预算是否用得舒服，不穷游也不乱花。
- 酒店位置和住宿类型是否合理。
- 天气、同行人群、负向约束是否处理自然。
- 行程节奏和路线是否可执行。

### 6.3 候选来源建议

第一版 DPO 使用多路候选：

| 候选来源 | 用途 |
| --- | --- |
| hard baseline prompt + low temperature | 稳定但可能保守，常作 rejected 或保底候选 |
| hard baseline prompt + high temperature | 提供更多变化 |
| meal rotation prompt | 提供软质量较好的 prompt-only 候选 |
| strong model low/high temperature | 提供 teacher 上限候选 |

每个 prompt 最终只保留 1-2 对高置信 pair，避免一条请求贡献太多相似样本。

## 7. 下一步计划

1. 固定本文两类 baseline。
2. 更新 `V3_DPO启动计划.md`，把旧 hard_pass 口径标记为历史。
3. 生成 DPO prompt 池，规模先 300-500。
4. 用多路候选生成 `candidates.jsonl`。
5. 规则硬过滤：只让 `sft_hard_pass` 通过的候选进入 judge。
6. LLM judge 打分，生成 chosen/rejected。
7. 先 smoke 20，再扩到 200-500 pair。
8. 训练 DPO 后同时对比：
   - hard baseline 的 `sft_hard_pass`
   - soft prompt-only baseline 的 `dpo_soft_pass`
   - LLM judge / pairwise win rate

阶段目标：

```text
DPO 不牺牲硬约束稳定性，
同时在餐饮多样性、预算质量、偏好满足和可执行性上超过 prompt-only baseline。
```
