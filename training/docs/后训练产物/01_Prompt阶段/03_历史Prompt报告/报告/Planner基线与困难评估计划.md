# V3 基线与困难评估计划

更新时间：2026-05-04

## 1. 当前正式 Baseline

当前冻结以下版本为 v3 prompt baseline：

```text
base_qwen25_7b_v3_harder_no_route_w8
```

产物目录：

```text
training/outputs/eval/base_qwen25_7b_v3_harder_no_route_w8/
```

对应 frozen eval 输入：

```text
training/data/v3/eval_harder_prompt_budget_final_no_route/records.jsonl
```

这版 baseline 继承了前一版“每天景点数 1-3”的硬约束和预算 JSON 数值表达修复，并去掉了粗糙的直线距离 `route_hints`。当前策略是把候选 POI 的区域、地址、坐标给模型，由模型自行做动线取舍；真实路线 API 留作后续工程增强。

```text
每天 attractions 必须包含 1-3 个景点。
到达日、返程日、慢节奏、亲子、老人场景也至少安排 1 个轻量景点。
不能用休息、自由活动、返程替代景点。

所有金额字段必须输出最终整数数字字面量。
不能在 JSON 数值字段里写算式、小数、括号或解释。
prompt 中不放具体预算数字示例，避免模型复用示例数字。
```

## 2. Baseline 结果

当前正式 baseline 的规则指标：

| 指标 | 结果 |
| --- | ---: |
| API 调用成功 | 300/300 |
| JSON 可解析 | 99.33% |
| Schema 通过 | 99.33% |
| hard_pass | 95.30% |
| attraction_count_ok | 100.00% |
| budget_arithmetic_consistent | 96.64% |
| budget_preference_aligned | 96.31% |
| budget_within_user_budget | 100.00% |
| hotel_budget_covers_nights | 99.33% |
| weather_match | 99.66% |

8 并发评估稳定完成：

```text
API ok = 300/300
failed = 0
```

## 3. 阶段判断

这版结果说明：

- 当前 base + v3 prompt 已经能稳定执行大部分确定性业务协议。
- JSON、schema、日期、天气、住宿晚数、酒店名、预算不超、POI grounding 等问题不再是主要瓶颈。
- SFT 不应继续以“补格式、补硬规则”为主目标，否则容易把强 baseline 训退化。

因此后续策略调整为：

```text
当前 baseline 已经可以作为正式对照组。
下一阶段主线转向 DPO，用来优化合法计划之间的偏好质量。
```

## 4. 更难评估集要测什么

当前 hard eval 已经证明 prompt 能解决很多硬规则。下一版 harder eval 不应该只是重复测 JSON，而要专门构造更接近 DPO 价值的复杂决策场景。

### 4.1 预算冲突

目标：看模型是否能在预算、住宿类型、人数和体验档位之间做合理取舍。

样例类型：

- 高端酒店 + 低预算 + 多人同行。
- premium 预算但用户又说“别乱花钱”。
- limited 预算但城市/门票/酒店都偏贵。
- soft 预算要求贴近档位，不要显著过省。

重点指标：

- `budget_usage_ratio`
- `budget_quality`
- `hotel_budget_covers_nights`
- `premium_not_too_cheap_rate`
- `limited_not_over_budget_rate`

### 4.2 负向约束优先级

目标：看模型是否把明确约束放在正向偏好之前。

样例类型：

- 喜欢美食但海鲜过敏。
- 喜欢自然风光但老人不爬山、少走路。
- 喜欢夜景但带小孩，不适合太晚。
- 喜欢网红地但要求避开排队和过度商业化。

重点指标：

- `negative_constraint_violation_rate`
- `constraint_satisfaction`
- `preference_alignment`

### 4.3 天气和日期压力

目标：看模型是否真的根据每天的天气调整活动，而不是机械复制天气。

样例类型：

- 连续中雨/大雨。
- 高温日安排户外活动是否过密。
- 冷空气/低温日是否提醒保暖并减少夜间户外。
- 部分日期有历史天气，部分日期远期未知。

重点指标：

- `weather_match`
- `weather_awareness`
- 雨天室内活动比例
- 高温户外密度

### 4.4 动线可执行性

目标：看模型是否能基于候选 POI 的 `district`、`address`、`location` 自主安排相对顺路的行程，而不是只选看起来好的 POI。当前不再使用粗直线距离 `route_hints`，后续真实路线 API 才重新进入上下文。

样例类型：

- 同城跨区候选很多。
- 经典景点和偏好景点距离很远。
- 返程日必须轻量安排。
- 自驾和公共交通策略不同。

重点指标：

- `route_quality`
- `feasibility`
- 同日跨区跳跃处罚
- 跨区跳跃次数

### 4.5 多人同行成本

目标：看模型是否把人数真正带入预算账本和体验安排。

样例类型：

- 2 成人 + 2 儿童。
- 2 成人 + 2 老人。
- 朋友 4-5 人。
- 商务 1-3 人但每日可玩时间有限。

重点指标：

- `attraction_budget_ok`
- `meal_budget_ok`
- `budget_usage_ratio`
- 亲子/老人友好场景 judge 分

## 5. 更难评估集建议规模

第一版 harder eval 不需要太大：

| 阶段 | 样本数 | 用途 |
| --- | ---: | --- |
| smoke | 30 | 快速看是否能拉开差异 |
| baseline run | 100-150 | 跑 base prompt baseline |
| DPO eval | 150-200 | 后续固定对比 base/SFT/DPO |

建议切片尽量均衡：

- 预算冲突：30%
- 负向约束：25%
- 天气压力：20%
- 动线压力：15%
- 多人同行成本：10%

## 6. 是否进入 DPO 的判断

如果 base 在 harder eval 上仍满足：

```text
schema_ok >= 98%
hard_pass >= 90%
budget_arithmetic_consistent >= 95%
grounding avg >= 95%
weather_match >= 98%
```

则不再优先做大规模 SFT，而是直接进入 DPO 数据构造。

DPO 目标不再是修硬错误，而是优化：

- 预算花得是否合理。
- 偏好和负向约束是否更自然地权衡。
- 路线是否更顺、更符合同行人群。
- 天气和节奏是否更像真实旅行顾问。
- 输出文本是否更具体、更能直接给用户看。

## 7. 下一步建议

1. 固化当前 baseline。
2. 构建 `eval_harder`，先 30 条 smoke。
3. 用当前 baseline 跑 `eval_harder`。
4. 如果 hard 指标仍稳定，开始 v3 DPO prompt/candidate/judge/pair 流程。
5. SFT 暂时降级为可选实验，只在 harder eval 暴露明确协议硬错时再补。

## 8. Eval Harder 冻结结果

2026-05-03 已冻结 300 条 `eval_harder`：

```text
training/data/v3/eval_harder/records.jsonl
```

构建结果：

```text
count = 300
failed = 0
difficulty = harder
```

当前 base prompt baseline 评估目录：

```text
training/outputs/eval/base_qwen25_7b_v3_harder_w8/
```

核心指标：

| 指标 | 结果 |
| --- | ---: |
| API 调用成功 | 300/300 |
| JSON 可解析 | 98.00% |
| Schema 通过 | 97.33% |
| hard_pass | 92.12% |
| attraction_count_ok | 99.66% |
| budget_arithmetic_consistent | 93.49% |
| budget_within_user_budget | 100.00% |
| hotel_budget_covers_nights | 100.00% |
| weather_match | 99.66% |

结论：

```text
base + v3 prompt 在 harder eval 上仍守住 hard_pass >= 90%。
当前不需要立刻大规模 SFT。
下一步可以转向 DPO，但在 DPO 前应先把预算算术闭合和 JSON 数值字段算式问题作为硬过滤处理掉。
```

当前暴露的问题：

- `budget.total` 偶发不等于四个分项之和。
- JSON 数值字段里偶发输出 `450 * 4` 这类算式，导致不是合法 JSON。
- 少量 schema 类型问题，例如餐饮费用输出小数、meal 字段名缺失。

## 9. Prompt 修复后 Harder Baseline

2026-05-03 针对 harder eval 暴露的 JSON 数值算式问题，尝试了两版 prompt：

1. **错误数字示例版**：在规则里写了具体预算数字示例。
2. **最终无数字示例版**：只要求“所有金额字段必须写最终整数数字字面量，不能写算式/小数/解释，不要复用提示词或示例里的任何预算数字”。

错误数字示例版不采用。原因是模型会复用提示词里的具体预算数字，导致 `budget.total` 和分项加总更容易不一致。

最终采用的评估目录：

```text
training/outputs/eval/base_qwen25_7b_v3_harder_budget_final_prompt_w8/
```

核心指标：

| 指标 | 原 harder baseline | 最终无数字示例版 |
| --- | ---: | ---: |
| API 调用成功 | 300/300 | 300/300 |
| JSON 可解析 | 98.00% | 99.33% |
| Schema 通过 | 97.33% | 99.00% |
| hard_pass | 92.12% | 93.27% |
| attraction_count_ok | 99.66% | 99.66% |
| budget_arithmetic_consistent | 93.49% | 93.94% |
| budget_preference_aligned | 98.63% | 97.64% |
| budget_within_user_budget | 100.00% | 100.00% |
| hotel_budget_covers_nights | 100.00% | 100.00% |
| weather_match | 99.66% | 100.00% |

结论：

```text
去掉具体预算数字示例后，prompt 修复有效：
JSON/schema 更稳，hard_pass 略升，预算加总一致性略升。
但预算加总一致性仍未达到 95%，说明纯 prompt 只能缓解，不能彻底解决预算闭合问题。
下一步如果继续追求工程稳定性，预算 total 更适合由后置确定性重算；如果追求后训练收益，DPO 应聚焦预算花得是否合理、偏好权衡、路线质量和文本可用性。
```

## 10. LLM Judge 与 Baseline 问题画像

为了判断“规则指标已经不错的 baseline，真实旅行决策质量还有多少空间”，在当前 no-route baseline 上追加了 LLM-as-Judge 评估。

评分维度：

- `preference_satisfaction`
- `practicality`
- `grounding_faithfulness`
- `budget_reasonableness`
- `coherence`
- `overall_quality`

强模型 judge 每个维度 1-5 分，5 分最好。64 并发时 judge 自身 JSON 失败较多，后续调整为 32 并发，并通过失败队列重跑机制补评。

最终结果：

| 指标 | 结果 |
| --- | ---: |
| 样本总数 | 300 |
| judge 成功 | 283 |
| judge 覆盖率 | 94.33% |
| json_extract 跳过 | 2 |
| schema 跳过 | 0 |
| judge_failed 残留 | 15 |

均分：

| 维度 | 均分 / 5 |
| --- | ---: |
| 工具忠实 | 3.4099 |
| 偏好满足 | 2.4982 |
| 连贯性 | 2.3039 |
| 可执行性 | 2.1625 |
| 综合质量 | 1.8834 |
| 预算合理 | 1.5442 |

问题画像：

| 问题类别 | 多标签命中次数 |
| --- | ---: |
| 餐饮/美食 | 443 |
| 偏好/负向约束 | 424 |
| 预算/费用 | 348 |
| 酒店/住宿 | 328 |
| 交通/路线/位置 | 317 |

相关产物：

```text
training/outputs/eval/base_qwen25_7b_v3_harder_no_route_w8/judge_summary.md
training/outputs/eval/base_qwen25_7b_v3_harder_no_route_w8/judge_top_bottom_readable_cases.md
training/outputs/eval/base_qwen25_7b_v3_harder_no_route_w8/baseline_strength_weakness_dashboard.md
training/outputs/eval/base_qwen25_7b_v3_harder_no_route_w8/baseline_strength_weakness_dashboard.svg
```

结论：

```text
baseline 的工程协议能力已经足够强，但旅行决策质量仍然偏弱。
DPO 的优化方向非常明确：交通路线、餐饮落地、预算使用、酒店位置、偏好和负向约束权衡。
```

## 11. Route Hints 消融结论

对比旧的 `base_qwen25_7b_v3_harder_budget_final_prompt_w8` 和当前 no-route baseline 后，结论很明确：

| 指标 | 旧 route_hints 版 | 当前 no-route 版 |
| --- | ---: | ---: |
| hard_pass | 93.27% | 95.30% |
| budget_arithmetic_consistent | 93.94% | 96.64% |
| budget_preference_aligned | 97.64% | 96.31% |
| overall_quality | 1.8241 | 1.8834 |
| practicality | 1.9069 | 2.1625 |
| preference_satisfaction | 2.3138 | 2.4982 |
| grounding_faithfulness | 3.3552 | 3.4099 |
| budget_reasonableness | 1.5931 | 1.5442 |

阶段判断：

```text
半成品 route_hints 会把模型带向粗糙路线解释，反而削弱自主规划。
当前正式 baseline 不启用粗 route_hints。
未来如果做路线增强，应接高德/地图真实路线 API，并带缓存、交通方式和时间口径，而不是继续使用直线距离估算。
```

## 12. 餐饮和酒店距离严格口径补评

人工审查 no-route baseline 的高分样本时发现两类占位问题：

1. 模型会输出 `早餐推荐/午餐推荐/晚餐推荐` 这类占位餐饮。旧规则只检查三餐类型完整，没有检查餐饮是否具体、是否来自 `food_pois`。
2. 模型会大量输出 `hotel.distance="距离景点2公里"`。旧规则没有检查酒店距离是否来自真实工具，导致一个伪精确字段看起来像真实路线信息。

已补充：

- prompt 禁止餐饮占位词。
- 线上校验把占位餐饮作为硬错误触发重试。
- 规则评估新增 `meal_specific_ok`、`meal_grounding_ok`、`meal_grounding_rate`，并纳入 `hard_pass`。
- LLM judge 和 DPO judge prompt 明确把占位餐饮作为 grounding/specificity/coherence 问题。
- prompt 要求当前没有真实路线/距离工具时 `hotel.distance=""`。
- 线上校验把 `距离景点2公里`、`距主要景点约X公里` 这类酒店距离占位作为硬错误触发重试。
- 规则评估新增 `hotel_distance_placeholder_ok`，并纳入 `hard_pass`。

用既有 no-route generations 重算严格餐饮口径：

```text
training/outputs/eval/base_qwen25_7b_v3_harder_no_route_w8_meal_strict/rule_eval_report.md
training/outputs/eval/base_qwen25_7b_v3_harder_no_route_w8_meal_hotel_strict/rule_eval_report.md
```

| 指标 | 餐饮严格 | 餐饮+酒店距离严格 |
| --- | ---: | ---: |
| meal_complete | 99.66% | 99.66% |
| meal_specific_ok | 50.67% | 50.67% |
| meal_grounding_ok | 35.23% | 35.23% |
| meal_grounding_rate.avg | 46.68% | 46.68% |
| hotel_distance_placeholder_ok | 未纳入 | 3.36% |
| hard_pass | 33.56% | 0.34% |

结论：

```text
当前 no-route baseline 的“老报告”仍可作为历史对比，但不能再作为最终质量结论。
下一步必须用修正后的 prompt 重新跑 baseline，确认餐饮 grounding 和酒店 distance 口径稳定后，再决定是否进入 DPO。
```
