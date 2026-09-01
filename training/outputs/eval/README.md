# 评测输出

评测结果默认写入 `training/outputs/eval/<run>/`，包括模型生成、规则指标、切片报告和可选 judge 结果。这些内容是运行产物，默认不提交到仓库。

运行评测：

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

standard 和 hard 评测输入固定在 `training/data/planner/eval/` 与 `training/data/planner/eval_hard/`。不同模型对比时必须使用同一份输入。
