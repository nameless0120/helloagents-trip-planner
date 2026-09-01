# Best-of-N Pipeline

Best-of-N is the first RL-adjacent step for the current planner. It samples multiple TripPlan
candidates for the same `PlannerContext`, scores them with the existing rule
evaluator, and exports the best response for later SFT, SimPO, DPO, or GRPO
smoke runs.

Recommended smoke:

```bash
.venv-training-py311/bin/python3 training/scripts/run_pipeline.py \
  --stage bestofn \
  --records training/data/planner/sft_runs/<YYMMDD>_<run_slug>/records.jsonl \
  --bestofn-dir training/data/planner/bestofn/260831_smoke20 \
  --bestofn-api-model trip-planner-sft \
  --bestofn-spec t02:0.2:1 \
  --bestofn-spec t05:0.5:2 \
  --bestofn-spec t08:0.8:1 \
  --limit 20 \
  --bestofn-shuffle
```

这一个命令会依次构建 prompt、生成候选、选择 winner，并导出 SFT/DPO 文件。需要定位单个步骤时，再直接运行对应的底层脚本。

Selection uses a conservative reward:

- hard protocol items are heavily penalized when false;
- `sft_hard_pass` is preferred whenever any candidate passes it;
- soft rewards include recomputed budget fit, budget relationship, meal cost
  scale, meal diversity, attraction diversity, and user budget constraints.

Do not use `eval` or `eval_hard` records as training prompts. Keep those frozen
for final comparison.
