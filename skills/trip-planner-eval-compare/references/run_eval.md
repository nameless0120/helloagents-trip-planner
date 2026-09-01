# 运行评测

单模型评测推荐使用总入口：

```bash
.venv-training-py311/bin/python3 training/scripts/run_pipeline.py \
  --stage eval \
  --records training/data/planner/eval/records.jsonl \
  --eval-dir training/outputs/eval/<run> \
  --model-name <model_name> \
  --api-model <api_model> \
  --base-url http://127.0.0.1:4396/v1 \
  --workers 1
```

hard split 只需把 records 换成 `training/data/planner/eval_hard/records.jsonl`，并使用新的输出目录。

已有生成结果时，可以直接运行：

```bash
.venv-training-py311/bin/python3 training/scripts/eval/eval_rule_metrics.py --help
```

先查看参数，再对同一轮 `generations.jsonl` 重算规则指标。
