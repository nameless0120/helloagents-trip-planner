# Best-of-N 配置说明

这里保留历史 Best-of-N 1200 retry 实验的配置说明。当前流程统一从总入口开始：它为同一份
`PlannerContext` 生成多个 `TripPlan` 候选，用现有规则打分，再导出选中的 SFT 样本和 DPO pair。

当前复现命令：

```bash
.venv-training-py311/bin/python3 training/scripts/run_pipeline.py \
  --stage bestofn \
  --records training/data/planner/sft_runs/<run>/export_budget_clean/records.jsonl \
  --bestofn-dir training/data/planner/bestofn/<run> \
  --bestofn-dataset-prefix trip_planner_bestofn_<run> \
  --bestofn-base-url http://127.0.0.1:4396/v1 \
  --bestofn-api-model trip-planner-sft \
  --bestofn-spec t02:0.2:1 \
  --bestofn-spec t05:0.5:2 \
  --bestofn-spec t08:0.8:1 \
  --workers 1
```

这条命令会生成 prompts、候选和 selected 结果，并登记四个 LLaMA-Factory 数据集：

```text
trip_planner_bestofn_<run>_sft_train
trip_planner_bestofn_<run>_sft_val
trip_planner_bestofn_<run>_pair_train
trip_planner_bestofn_<run>_pair_val
```

选择规则包括：

- hard protocol 不通过时大幅扣分；
- 有候选通过 `sft_hard_pass` 时优先选择通过者；
- 软分数包含重算预算贴合、预算关系、餐饮价格尺度、餐饮多样性、景点多样性和用户预算约束。

不要使用 `eval` 或 `eval_hard` records 作为训练 prompt，它们要保留为冻结评测集。
底层三个脚本仍可用于定位单步问题，但新一轮流程应使用上面的总入口。
