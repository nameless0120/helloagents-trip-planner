# Planner 后训练脚本

这里放与 Planner 数据和评测直接相关的脚本。推荐从 `training/scripts/run_pipeline.py` 调度。

## SFT

```text
planner/data/generate_sft_data.py
  -> planner/audit/audit_sft_budget_fit.py
  -> planner/audit/classify_sft_budget_usability.py
  -> planner/data/export_sft_budget_clean_subset.py
  -> validation/validate_trip_plan.py
```

生成 SFT records：

```bash
.venv-training-py311/bin/python3 training/scripts/run_pipeline.py \
  --stage sft-data \
  --count 20 \
  --request-source controlled \
  --date-mode mixed \
  --workers 1 \
  --sft-dir training/data/planner/sft_runs/<run>
```

审计、分类、导出和校验：

```bash
.venv-training-py311/bin/python3 training/scripts/run_pipeline.py \
  --stage sft-audit \
  --records training/data/planner/sft_runs/<run>/records.jsonl \
  --sft-dir training/data/planner/sft_runs/<run> \
  --sft-dataset-prefix trip_planner_sft_<run>
```

`generate_sft_data.py` 可用 `--dry-run-requests` 检查请求分布，也可用 `--dry-run-context` 检查 PlannerContext；这两个模式不生成模型答案。

## 票价和评测输入

`pricing/` 负责收集 PlannerContext 中的景点候选、按请求频次分桶，并可选调用强模型估算训练用票价。`eval/` 负责构建 standard / hard 冻结评测输入。评测输入固定在：

```text
training/data/planner/eval/records.jsonl
training/data/planner/eval_hard/records.jsonl
```

## Best-of-N

```text
planner/bestofn/build_prompts.py
  -> planner/bestofn/generate_candidates.py
  -> planner/bestofn/select_best.py
  -> SFT / DPO 导出
```

这条流程需要 Planner 模型服务。完整命令见 `planner/bestofn/README.md`。
