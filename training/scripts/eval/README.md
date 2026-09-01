# 评测和 DPO 脚本

这里放当前仍在使用的通用评测和 DPO 工具。SFT 数据生成、预算审计、分类、导出和训练都不从这个目录开始，统一使用：

```bash
.venv-training-py311/bin/python3 training/scripts/run_pipeline.py \
  --stage sft \
  --count 20 \
  --request-source controlled \
  --date-mode mixed \
  --workers 1 \
  --sft-dir training/data/planner/sft_runs/<YYMMDD>_<run_slug>
```

当前后训练主线是：

```text
run_pipeline.py
  -> planner/data/generate_sft_data.py
  -> planner/audit/audit_sft_budget_fit.py
  -> planner/audit/classify_sft_budget_usability.py
  -> planner/data/export_sft_budget_clean_subset.py
  -> validation/validate_trip_plan.py
  -> LLaMA-Factory train
```

需要做偏好优化或多候选评测时，使用：

```text
当前 SFT records
  -> planner/bestofn/ 或 eval/dpo_build_prompts.py
  -> 候选生成和规则评测
  -> chosen / rejected
  -> LLaMA-Factory DPO
  -> run_pipeline.py --stage train
```

## 当前脚本

| 脚本 | 用途 |
| --- | --- |
| `eval_generate.py` | 调用 OpenAI-compatible 模型服务，对冻结评估集生成 TripPlan 候选 |
| `eval_rule_metrics.py` | 计算 JSON、schema、日期、天气、grounding、酒店、餐饮和预算指标 |
| `eval_pipeline.py` | 串联单模型生成、规则评测和可选 judge |
| `eval_llm_judge.py` | 用强模型评估偏好满足、可执行性、grounding、预算和整体质量 |
| `eval_pairwise_judge.py` | 对两个模型做 A/B 对比 |
| `eval_slice_report.py` | 按同行人、预算、天气、天数等切片汇总结果 |
| `eval_utils.py` | 评测、预算和 JSONL 共用 helper |
| `dpo_build_prompts.py` | 从当前 records 构造 DPO prompt |
| `dpo_generate_candidates.py` | 生成 Base、SFT、Strong 等多来源候选 |
| `dpo_judge_candidates.py` | 对候选做强模型多维评分 |
| `dpo_build_pairs.py` | 按阈值构造 chosen/rejected pair |
| `dpo_audit_pairs.py` | 检查 DPO pair 的来源、分数和过滤结果 |
| `dpo_utils.py` | DPO prompt、候选和 pair 共用 helper |

## 推荐入口

从当前 SFT records 继续生成 DPO 数据：

```bash
.venv-training-py311/bin/python3 training/scripts/run_pipeline.py \
  --stage dpo \
  --records training/data/planner/sft_runs/<YYMMDD>_<run_slug>/records.jsonl \
  --dpo-dir training/data/planner/dpo/<YYMMDD>_<run_slug> \
  --dpo-workers 1
```

直接评测冻结评估集：

```bash
.venv-training-py311/bin/python3 training/scripts/run_pipeline.py \
  --stage eval \
  --eval-data-dir training/data/planner/eval \
  --model-name <model_name> \
  --api-model <api_model> \
  --eval-dir training/outputs/eval/<model_name> \
  --workers 1
```

只做格式校验，不需要模型服务：

```bash
.venv-training-py311/bin/python3 training/scripts/run_pipeline.py \
  --stage validate \
  --validate-sft training/data/llamafactory/generated/<sft_train>.json
```

需要定位单一步骤时，可以直接调用上表中的脚本；正式流程和新数据仍应通过
`run_pipeline.py`，这样每个阶段的输入、输出和 manifest 会保持一致。

冻结评估集固定放在 `training/data/planner/eval/` 和
`training/data/planner/eval_hard/`。不要把评估集 records 作为训练数据输入。

历史天气 helper 已和当前 SFT 生成脚本放在
`training/scripts/planner/data/historical_weather.py`，因为它是数据生成依赖，不是评测入口。
