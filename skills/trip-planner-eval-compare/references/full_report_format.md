# 评测报告格式

报告由 `training/scripts/planner/eval/generate_full_report.py` 生成，建议写入本地 comparison 目录：

```bash
.venv-training-py311/bin/python3 training/scripts/planner/eval/generate_full_report.py \
  --current-label candidate \
  --primary-label reference \
  --baseline-label base \
  --standard-records training/data/planner/eval/records.jsonl \
  --hard-records training/data/planner/eval_hard/records.jsonl \
  --report standard/candidate=<candidate_standard.json> \
  --report hard/candidate=<candidate_hard.json> \
  --report standard/reference=<reference_standard.json> \
  --report hard/reference=<reference_hard.json> \
  --report standard/base=<base_standard.json> \
  --report hard/base=<base_hard.json> \
  --output-dir training/outputs/eval/comparisons/<run> \
  --comparison-slug <run>
```

报告先写口径和生成完整性，再写 hard/soft 指标、预算诊断、grounding、切片差异和结论。不能用不同 records 的报告直接比较。
