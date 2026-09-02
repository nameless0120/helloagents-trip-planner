# Planner SFT 阶段总结

更新时间：2026-05-14

结论先写在前面：

**Planner 的 SFT 阶段到这里可以收束。后续默认不再继续堆 SFT 轮次，除非出现新的高质量失败样本或明确的新协议字段。**

这个阶段最有价值的产物不是某一个 checkpoint，而是完整的实验账本、评测集、数据生成链路和可复现实验路径。作为个人项目，这部分已经能说明：我们不是只跑了一次 LoRA，而是把旅行规划任务拆成了可验证的协议、预算、grounding、餐饮、候选选择和 rerank 问题，并且一路保留了反例和回退节点。

## 1. 当前阶段判断

SFT 已经完成了它最应该完成的事：

- 把模型从“能写行程”推到“能稳定输出可解析、可重算、可验证的结构化 `TripPlan`”。
- 大幅提高预算关系、餐饮价格尺度、hard case 稳定性和 schema 稳定性。
- 证明继续扩大 SFT 数据会进入边际收益变钝区间：不同 checkpoint 各有强项，但没有一个版本在所有核心指标上全面胜出。
- 证明主增益已经转向推理时 rerank，而不是继续训练更多 SFT epoch。

所以这里的工程决策是：

| 事项 | 决策 |
| --- | --- |
| SFT 训练 | 阶段冻结，不继续常规追加训练 |
| 默认线上方向 | `final1200 + rerank` 作为默认主线候选 |
| 预算保守方向 | `old600final + rerank` 保留为重算预算更强的对照 |
| ckpt104 定位 | 预算算术较好，但不是 rerank 口径下的整体最优 |
| 下一阶段 | rerank、规则化预算修正、候选质量、必要时 DPO/偏好学习 |

## 2. 关键实验结论

### 2.1 SFT 的主要收益

第一轮干净 SFT 已经把任务从 prompt 调优带到模型行为层面。最关键的变化不是硬通过涨了几点，而是 `softpass`、预算关系和餐饮尺度从低位跳到可用区间。

代表性收益：

| 评测集 | 指标 | base | LoRA SFT | 变化 |
| --- | --- | ---: | ---: | ---: |
| standard | `hardpass` | 89.90 | 96.46 | +6.56pp |
| standard | `softpass` | 5.56 | 61.11 | +55.55pp |
| standard | 重算预算 `softpass` | 13.13 | 45.45 | +32.32pp |
| standard | 预算关系 | 6.06 | 56.57 | +50.51pp |
| standard | 餐饮尺度 | 35.35 | 73.23 | +37.88pp |
| hard | `hardpass` | 83.28 | 91.97 | +8.69pp |
| hard | `softpass` | 3.34 | 46.15 | +42.81pp |
| hard | 预算关系 | 5.69 | 45.15 | +39.46pp |
| hard | 餐饮尺度 | 38.80 | 68.56 | +29.76pp |

这说明 SFT 的价值是“学会协议和结构化规划习惯”，不是解决所有旅行质量问题。

### 2.2 继续加 SFT 数据后的边际收益

`usage700 replay`、`patch700-only`、`Best-of-N 600`、`Best-of-N 1200` 都跑过以后，趋势很清楚：

- `usage700 replay` 提升 hard split 鲁棒性，但 standard 有小幅回落。
- `patch700-only` 会偏科，不能单独作为主线。
- `Best-of-N 600` 是健康补强，但没有解决重算预算 fit 的根问题。
- `Best-of-N 1200` 后 checkpoint 选择变重要，最终 checkpoint 不一定最好。

非 rerank 的 500 条合并口径如下：

| 版本 | JSON | hardpass | softpass | 重算预算 softpass | 预算合计/算术 | 预算偏好 | 预算关系 | 餐饮尺度 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| ckpt104 | 99.8 | 97.4 | 56.9 | 43.1 | 66.5 | 71.3 | 78.8 | 81.8 |
| final1200 | 99.8 | 97.4 | 54.9 | 42.3 | 64.3 | 71.7 | 79.6 | 82.6 |
| old600final | 100.0 | 98.6 | 55.9 | 40.5 | 67.3 | 70.5 | 79.6 | 83.2 |

这张表的信号是：继续 SFT 可以调风格和子指标，但没有出现“1200 全面压过 600”的稳定结论。

### 2.3 rerank 是当前最值的增益层

多温度生成 + 规则 rerank 后，三条主线都明显变强。最新 500 条合并结果：

| 版本 | JSON | hardpass | softpass | 重算预算 softpass | 预算合计/算术 | 预算偏好 | 预算关系 | 餐饮尺度 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| ckpt104 + rerank | 100.0 | 98.0 | 65.6 | 54.6 | 81.2 | 77.0 | 86.4 | 88.8 |
| final1200 + rerank | 100.0 | 98.2 | 66.8 | 54.6 | 78.0 | 78.4 | 85.0 | 88.0 |
| old600final + rerank | 100.0 | 98.2 | 66.2 | 59.2 | 78.4 | 75.4 | 87.0 | 89.4 |

这里的判断：

- `final1200 + rerank` 的 `softpass` 最好，适合做默认主线。
- `old600final + rerank` 的重算预算 `softpass` 明显最好，适合作为预算保守对照。
- `ckpt104 + rerank` 的预算算术最好，但整体不再是第一选择。
- rerank 的收益大于 checkpoint 间差异，后续优先优化 rerank 特征和候选生成策略。

## 3. 最终保留版本

| 名称 | 定位 | 路径 |
| --- | --- | --- |
| `old600final` | 旧主线、重算预算强对照 | `training/outputs/qwen25_7b/sft_260512_replay_usage700_plus_bestofn600_from_replay_r32_b32_lr1e5_ctx24576_ep2_20260512` |
| `ckpt104` | 1200 retry 中间 checkpoint，预算算术好 | `training/outputs/qwen25_7b/sft_260513_replay_usage700_plus_bestofn1200_from_final_r32_b32_lr1e5_ctx24576_ep2_retry_20260513_1026/checkpoint-104/hf_model` |
| `final1200` | 当前默认主线候选，配合 rerank | `training/outputs/qwen25_7b/sft_260513_replay_usage700_plus_bestofn1200_from_final_r32_b32_lr1e5_ctx24576_ep2_retry_20260513_1026` |

不建议继续追新的 SFT checkpoint。要提升结果，优先做：

1. rerank 打分特征和权重。
2. 多温度候选的去重、互补性和失败兜底。
3. 确定性预算重算/修正。
4. 高质量 pairwise preference 数据。

## 4. 路径索引

### 4.1 文档入口

| 内容 | 路径 |
| --- | --- |
| 后训练教程主文档 | `training/docs/教程/旅行助手后训练实战教程.md` |
| 实验贡献账本 | `training/docs/教程/旅行助手后训练指标贡献补充.md` |
| 本阶段结题总结 | `training/docs/内部文档/SFT阶段总结.md` |
| SFT 目标与边界 | `training/docs/内部文档/SFT目标与边界.md` |
| 规划上下文协议 | `training/docs/内部文档/规划上下文协议.md` |
| 评测指标定义 | `training/docs/内部文档/评测指标.md` |
| 数据生成 skill | `skills/trip-planner-sft-data-loop/SKILL.md` |
| 评估对比 skill | `skills/trip-planner-eval-compare/SKILL.md` |

### 4.2 数据

| 内容 | 路径 |
| --- | --- |
| standard 评测集 | `training/data/planner/eval/records.jsonl` |
| hard 评测集 | `training/data/planner/eval_hard/records.jsonl` |
| usage700 replay LLaMA-Factory 数据 | `training/data/llamafactory/generated/trip_planner_260511_main_clean_plus_realbudget_usage700_train.json` |
| patch700-only 数据 | `training/data/llamafactory/generated/trip_planner_260511_realbudget_usage_patch700_train.json` |
| Best-of-N 600 replay 数据 | `training/data/llamafactory/generated/trip_planner_260512_replay_usage700_plus_bestofn600_x1p5_train.json` |
| Best-of-N 1200 replay 数据 | `training/data/llamafactory/generated/trip_planner_260513_replay_usage700_plus_bestofn1200_train.json` |
| Best-of-N 600 原始候选 | `training/data/planner/bestofn/260511_anti_leak600_vllm01/` |
| Best-of-N 1200 原始候选 | `training/data/planner/bestofn/260512_anti_leak1200_vllm23_w8/` |
| 数据 manifest | `training/data/llamafactory/manifests/` |

### 4.3 训练输出

| 阶段 | 路径 |
| --- | --- |
| main clean SFT | `training/outputs/qwen25_7b/sft_260509_main_clean_cp2_legacy_b_r32_b32_lr8e5_ctx24576_valloss_20260510` |
| usage700 replay | `training/outputs/qwen25_7b/sft_260511_main_clean_plus_realbudget_usage700_from_lr6e5_r32_b32_lr2e5_ctx24576_20260511` |
| patch700-only | `training/outputs/qwen25_7b/sft_260511_realbudget_usage_patch700_only_from_lr6e5_r32_b32_lr1e5_ctx24576_20260511` |
| Best-of-N 600 final | `training/outputs/qwen25_7b/sft_260512_replay_usage700_plus_bestofn600_from_replay_r32_b32_lr1e5_ctx24576_ep2_20260512` |
| Best-of-N 1200 retry final | `training/outputs/qwen25_7b/sft_260513_replay_usage700_plus_bestofn1200_from_final_r32_b32_lr1e5_ctx24576_ep2_retry_20260513_1026` |

### 4.4 评估与对比报告

| 内容 | 路径 |
| --- | --- |
| 1200 vs 600 全量对比 | `training/outputs/eval/comparisons/260513_bestofn1200_vs_600final_w10/260513_bestofn1200_vs_600final_w10_full_report.md` |
| 1200 vs 600 standard 切片 | `training/outputs/eval/comparisons/260513_bestofn1200_vs_600final_w10/slice_standard/slice_report.md` |
| 1200 vs 600 hard 切片 | `training/outputs/eval/comparisons/260513_bestofn1200_vs_600final_w10/slice_hard/slice_report.md` |
| ckpt104 rerank standard/hard | `training/outputs/eval/by_model/sft_qwen25_7b_planner_260513_rerank_ckpt104/` |
| final1200 rerank standard/hard | `training/outputs/eval/by_model/sft_qwen25_7b_planner_260513_rerank_final1200/` |
| old600final rerank standard/hard | `training/outputs/eval/by_model/sft_qwen25_7b_planner_260513_rerank_old600final/` |

### 4.5 关键脚本

| 用途 | 路径 |
| --- | --- |
| vLLM/LoRA 服务 | `training/scripts/serving/serve_planner_model.py` |
| 单模型生成评估 | `training/scripts/eval/eval_generate.py` |
| 规则指标计算 | `training/scripts/eval/eval_rule_metrics.py` |
| 训练侧 Best-of-N | `training/scripts/run_pipeline.py --stage bestofn` |
| 产品侧多候选 rerank | `backend/app/planner/rerank.py` |
| Best-of-N prompt 构造 | `training/scripts/planner/bestofn/build_prompts.py` |
| Best-of-N 候选生成 | `training/scripts/planner/bestofn/generate_candidates.py` |
| Best-of-N 选择 | `training/scripts/planner/bestofn/select_best.py` |
| Best-of-N 导出 SFT / DPO 数据 | `training/scripts/run_pipeline.py --stage bestofn` |

## 5. 后续路线

SFT 阶段结束后，项目重心切到下面几件事：

1. **rerank 工程化**
   - 固定 `n=3` 多温度候选。
   - 保留 schema、hardpass、预算、餐饮、多样性等可解释特征。
   - 做线上延迟和兜底策略。

2. **预算确定性修正**
   - 不再相信模型自报总预算。
   - 以结构化 POI、人数、房间数和餐饮单价重算预算。
   - 只接受不会破坏 grounding/schema 的预算修正。

3. **高质量偏好数据**
   - 如果做 DPO，不拿格式错当 rejected。
   - rejected 应该是合法 JSON 但路线、预算、偏好或体验明显更差。

4. **项目公开叙述**
   - 对外重点讲数据闭环、规则评估、Best-of-N、rerank 和实验反例。
   - 不把项目包装成“训练一个模型就解决旅行规划”，而是展示一套可验证的后训练工程方法。

## 6. 结束语

这轮 SFT 的价值已经兑现：协议稳定、预算语义明显改善、hard case 能打，实验记录也足够完整。继续做 SFT 不是不能涨，而是投入产出已经不如 rerank 和候选策略。

因此这里正式把 Planner SFT 阶段收束为：

```text
SFT: closed / frozen
Default next step: rerank-first inference pipeline
Primary asset: data + eval + experiment record
```
