# SFT 模型评估标准

本文档记录 v2 Planner SFT 模型的评估标准。评估目标不是让模型逐字复现 GT，而是从工程可用性、模型质量、偏好满足和泛化能力四个层面证明后训练确实带来了收益。

## 评估对象

- Base：`Qwen2.5-7B-Instruct`
- SFT：`training/outputs/qwen25_7b/sft_v2_clean`
- 后续 DPO / SFT+DPO：沿用同一套 eval 集横向比较
- Teacher：强模型生成的蒸馏答案，用作质量上界参考，而不是训练目标复现标准

冻结评估集：

- `training/data/v2/sft/records_eval.jsonl`
- `training/data/llamafactory/trip_v2_sft_clean_eval.json`

eval 集不参与训练和调参。

## 评估总览

评估分成四层：

1. 工程可用性：是否能生成后端和前端可消费的 `TripPlan`。
2. 结构与工具遵循：是否遵守日期、天气、酒店、POI grounding 等硬约束。
3. 规划质量：是否满足用户偏好、预算、节奏、同行类型和饮食要求。
4. 泛化能力：是否能在未训练分布、长行程、小众城市、极端约束下保持稳定。

简历或项目报告里不要只写 loss，应重点报告 `Base -> SFT -> DPO/SFT+DPO` 的指标变化。

## 硬门槛指标

这些指标直接决定输出能否在线上使用。

| 指标 | 判定方式 | 目标 |
| --- | --- | --- |
| 调用成功率 | 本地/线上模型接口未超时、未 5xx、未 4xx 拒绝 | 越高越好，低于 95% 需要排查服务或上下文 |
| 顶层 JSON 提取成功率 | 复用 `extract_json_object()`，只接受完整顶层 `TripPlan` JSON | 接近 100% |
| Pydantic schema 通过率 | `TripPlan(**data)` 成功 | 接近 100% |
| 基础形状通过率 | 复用 `validate_trip_plan_shape()` 的 city/date/days/weather/meals 等硬校验 | 接近 100% |
| 日期对齐率 | `days[*].date` 和 `weather_info[*].date` 等于请求日期序列 | 100% |
| 天气遵循率 | `weather_info` 逐字段来自 `PlannerContext.tool_snapshot.trip_weather`，远期未知不编造 | 100% |
| 中间天酒店合法率 | 非最后一天 `hotel != null`，且 `hotel.name` 不是“无/返程”等占位词 | 接近 100% |
| 景点数量合规率 | 每天 `attractions` 为 1-3 个；其中 `>3` 视为脏输出 | 接近 100% |
| 三餐完整率 | 每天包含 `breakfast/lunch/dinner` | 接近 100% |

说明：训练数据里保留了 1 个景点的 day，因为慢游、到达日、老人/亲子场景可能合理；但 `>3` 会导致前端展示和行程密度失控，评估时记为失败。

## Grounding 指标

这些指标衡量模型是否使用工具结果，而不是自己编。

| 指标 | 判定方式 | 目标 |
| --- | --- | --- |
| 景点 grounding 命中率 | 景点名用 `name_in_candidates()` 在 `classic_pois/preference_pois/scenic_pois/experience_pois` 中宽松匹配 | > 98% |
| 酒店 grounding 命中率 | `hotel.name` 在 `hotel_pois` 中宽松匹配 | > 98% |
| 餐饮 grounding 参考率 | 餐厅优先来自 `food_pois`；早餐/便利店/酒店早餐可放宽 | 作为软指标观察 |
| 位置字段合法率 | 所有 attraction/hotel/meal location 若存在，必须为 `{longitude, latitude}` 对象 | 100% |

线上代码目前对 grounding 是软告警：`warn_plan_grounding()` 只打印 warning，不硬拦。离线评估中可以同时统计 warning 数和命中率。

## Baseline 对比

每次模型评估都至少跑以下对象：

| 模型 | 目的 |
| --- | --- |
| `base_qwen25_7b` | 衡量原始 instruct 模型在长 PlannerContext 下的格式和约束能力 |
| `sft_v2_clean` | 衡量 SFT 是否提升结构化输出、工具遵循和约束稳定性 |
| `teacher_deepseek` 或其他强模型 | 提供质量上界参考，观察小模型和强模型的差距 |
| `sft_dpo` / `dpo` | 后续用于判断偏好优化是否带来质量收益 |

报告里需要给出：

- 绝对指标：每个模型的 JSON/schema/weather/grounding/偏好分数。
- 相对提升：`SFT - Base` 的提升幅度。
- 失败类型变化：比如 base 常见错误是 markdown/截断/中间天 hotel=null，SFT 是否减少。
- 成本和速度：平均耗时、输出 token 长度、失败重试次数。

推荐表格：

| Model | JSON Valid | Schema Pass | Weather Match | Attraction Grounding | Hotel Grounding | Judge Score | Avg Latency |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Base | TBD | TBD | TBD | TBD | TBD | TBD | TBD |
| SFT | TBD | TBD | TBD | TBD | TBD | TBD | TBD |
| Teacher | TBD | TBD | TBD | TBD | TBD | TBD | TBD |

## 质量指标

这些不一定一票否决，但用于比较模型效果。

| 指标 | 关注点 |
| --- | --- |
| 预算一致性 | `budget.total` 是否大致等于景点、酒店、餐饮、交通分项之和 |
| 住宿费用一致性 | 酒店天数和 `total_hotels` 是否大致匹配 |
| 用户偏好满足 | 亲子、老人友好、清真/素食/过敏、慢节奏、避开项是否被体现 |
| 行程密度 | 每日景点数、visit_duration、交通方式是否和 pace/companion 匹配 |
| 文本可用性 | description / overall_suggestions 是否具体，不是模板废话 |
| 前端可渲染性 | 输出能被现有 Result.vue 使用，不缺关键展示字段 |

这些指标可以先用规则和切片统计，后续再引入强模型 judge。

## LLM Judge 评估

规则指标能判断“能不能用”，但不能充分判断“好不好”。因此需要引入强模型 judge，对每个通过硬校验的输出打分。

### Judge 输入

每条样本给 judge：

- 原始 `TripRequest`
- 压缩后的 `PlannerContext`
- 待评估模型输出的 `TripPlan`
- 必要时提供 Teacher 输出作为参考，但不要要求逐字一致

### Judge 维度

每个维度 1-5 分，并要求 judge 给出简短理由：

| 维度 | 说明 |
| --- | --- |
| Preference Satisfaction | 是否满足偏好、同行类型、节奏、饮食、规避项 |
| Practicality | 景点密度、交通、酒店位置、每日安排是否现实 |
| Grounding Faithfulness | 是否主要基于工具候选和天气事实 |
| Budget Reasonableness | 预算分项和总价是否自洽，是否符合住宿/餐饮/交通偏好 |
| Coherence | 每天安排是否顺畅，描述是否具体，是否存在重复/矛盾 |
| Overall Quality | 综合旅行计划质量 |

### Pairwise Judge

除单独打分外，还建议做 pairwise 比较：

- Base vs SFT
- SFT vs Teacher
- SFT vs DPO

输出：

- win / tie / lose 数量
- win rate
- 按切片的 win rate

推荐问题形式：

> 给定同一个 TripRequest 和 PlannerContext，A/B 两个 TripPlan 哪个更适合作为最终旅行计划？请优先考虑约束满足、工具 grounding、可执行性和用户偏好，不要因为文字更长就判胜。

### Judge 防偏措施

- 随机交换 A/B 顺序，避免位置偏差。
- 对无效 JSON 或硬校验失败的输出直接判负，不交给 judge 粉饰。
- 保存 judge rationale，便于人工抽查。
- 对少量样本人工复核 judge 是否靠谱。

## 切片评估

总分之外必须看分组表现，避免平均值掩盖问题。

- `companion_type`：family_child / friends / couple / solo / family_elder / unspecified
- `city_tier`：major / popular / long_tail
- `travel_days`：2 / 3 / 4 / 5
- `weather_bucket`：historical / amap_forecast / future_unavailable
- `budget_level`：limited / medium / upper / luxury
- `diet`：无 / 清淡饮食 / 少辣 / 海鲜过敏 / 清真 / 素食

这些切片来自 `records_eval.jsonl` 中的 `control_spec` 和 `PlannerContext`。

切片报告需要同时输出规则指标和 judge 指标。例如：

| Slice | Count | Schema Pass | Weather Match | Grounding | Judge Overall | SFT Win Rate |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| family_child | TBD | TBD | TBD | TBD | TBD | TBD |
| family_elder | TBD | TBD | TBD | TBD | TBD | TBD |
| diet=海鲜过敏 | TBD | TBD | TBD | TBD | TBD | TBD |
| weather=future_unavailable | TBD | TBD | TBD | TBD | TBD | TBD |
| city_tier=long_tail | TBD | TBD | TBD | TBD | TBD | TBD |

切片分析的核心价值是暴露平均分掩盖的问题，例如：

- SFT 总体 schema 通过率高，但 5 天长行程容易截断。
- 总体 grounding 高，但 long-tail 城市更容易补常识。
- 总体偏好分高，但海鲜过敏样本仍推荐海鲜餐厅。
- 历史天气样本正确，远期未知天气样本容易编造温度。

## 泛化测试

冻结 eval 集来自当前 v2 数据分布，适合做同分布评估。为了展示模型泛化能力，需要额外构造一组不参与训练的 stress / generalization set。

### 泛化集类型

| 类型 | 示例 | 目的 |
| --- | --- | --- |
| 长行程 | 6-7 天、多城市附近景点 | 检查长输出是否截断、日期是否错位 |
| 小众城市 | 训练集中低频城市或新增城市 | 检查工具 grounding 和城市泛化 |
| 强约束饮食 | 清真、素食、海鲜过敏、少辣 | 检查饮食约束是否被真正遵守 |
| 特殊同行 | 带老人、低龄儿童、行动不便 | 检查行程密度和酒店/交通合理性 |
| 极端预算 | 很低预算、高端预算 | 检查预算和酒店餐饮是否一致 |
| 天气压力 | 全程下雨、远期未知、历史高温/低温 | 检查天气遵循和建议是否合理 |
| 工具缺口 | POI 候选少、酒店候选少、餐饮候选少 | 检查模型是否诚实处理缺口 |

### 泛化集规模

当前可以先做：

- dev eval：`records_eval.jsonl`，91 条，同分布冻结评估。
- stress eval：后续再造 100-200 条，专门覆盖难例。
- final eval：如果时间允许，扩到 200-300 条，作为简历/报告里的最终数字。

stress eval 只用于最终评估，不进入 SFT/DPO 训练。

## 报告建议格式

每次评估输出两份文件：

- `eval_report.json`：机器可读，包含逐样本结果和各类指标
- `eval_report.md`：人工可读，包含总览、切片、失败样本 TopN

报告中至少包含：

- 模型名称 / adapter 路径 / 服务地址
- eval 样本数
- 平均输入长度、平均输出长度、平均耗时
- 硬门槛通过率
- grounding 命中率
- LLM judge 平均分
- Pairwise win/tie/lose
- 切片指标
- 泛化集指标
- 失败样本列表：`record_id`、错误类型、请求摘要、输出摘要

建议目录结构：

```text
training/outputs/eval/
  base_qwen25_7b/
    eval_report.json
    eval_report.md
    generations.jsonl
  sft_v2_clean/
    eval_report.json
    eval_report.md
    generations.jsonl
  comparison/
    pairwise_base_vs_sft.jsonl
    judge_summary.md
```

## 当前推荐验收线

第一版 v2 SFT 可以先按以下标准验收：

- 顶层 JSON + schema 通过率：>= 98%
- 日期/天气对齐率：100%
- 中间天酒店合法率：>= 98%
- `attractions > 3` 失败率：<= 2%
- 景点 grounding 命中率：>= 98%
- 酒店 grounding 命中率：>= 98%
- 平均生成耗时：记录即可，先不作为硬门槛

如果 SFT 相比 base 在这些指标上明显提升，就进入 DPO 数据构造；如果格式指标仍不稳，继续补 SFT 数据或收紧 prompt/解码参数。

## 简历可写的指标口径

最终报告里优先沉淀这些结果：

- `Base -> SFT` 的 schema pass / weather match / grounding 提升。
- `Base -> SFT` 的无效酒店、天气编造、POI 幻觉下降。
- LLM judge 的平均质量分提升。
- Pairwise judge 中 SFT 相比 Base 的 win rate。
- 在亲子、老人、饮食约束、远期天气、小众城市等切片上的表现。
- stress eval 中长行程和工具缺口场景的稳定性。

可以形成类似表述：

> Built a data-centric post-training pipeline for a tool-grounded trip planning agent, including synthetic user generation, structured PlannerContext distillation, LoRA SFT, rule-based validation, LLM-as-judge preference evaluation, and stratified stress testing across family, elderly, dietary, weather, and long-tail city scenarios.
