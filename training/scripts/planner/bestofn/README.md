# Best-of-N

Best-of-N 为同一份 PlannerContext 生成多个候选，用当前规则计算分数，再导出选中的 SFT 样本和 DPO pair。

```bash
.venv-training-py311/bin/python3 training/scripts/run_pipeline.py \
  --stage bestofn \
  --records training/data/planner/sft_runs/<run>/records.jsonl \
  --bestofn-dir training/data/planner/bestofn/<run> \
  --bestofn-api-model trip-planner-sft \
  --bestofn-spec t02:0.2:1 \
  --bestofn-spec t05:0.5:2 \
  --bestofn-spec t08:0.8:1 \
  --limit 20
```

流程是：

```text
records
  -> build_prompts.py
  -> generate_candidates.py
  -> select_best.py
  -> LLaMA-Factory SFT/DPO 文件
```

Best-of-N 只使用当前 SFT records，不使用冻结评测集作为训练输入。正式训练前仍需运行 `validation/validate_trip_plan.py`。
