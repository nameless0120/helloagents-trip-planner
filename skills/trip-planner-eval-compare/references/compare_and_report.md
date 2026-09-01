# 对比和报告

规则指标对比使用 `eval_slice_report.py`。两个模型必须来自同一份 records：

```bash
.venv-training-py311/bin/python3 training/scripts/eval/eval_slice_report.py \
  --records training/data/planner/eval_hard/records.jsonl \
  --model-report base=<base_rule_eval_report.json> \
  --model-report candidate=<candidate_rule_eval_report.json> \
  --output-dir training/outputs/eval/comparisons/<run>
```

需要主观质量判断时再运行 `eval_llm_judge.py` 或 `eval_pairwise_judge.py`，并先限制 `--limit` 和 `--workers`。

报告建议包含：

- records 路径和样本数。
- 生成成功、失败和截断数量。
- `sft_hard_pass`、`dpo_soft_pass`、预算、grounding 和餐饮多样性。
- standard 与 hard 的差异。
- 主要退化切片和下一步动作。
