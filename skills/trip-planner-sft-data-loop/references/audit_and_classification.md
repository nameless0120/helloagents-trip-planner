# SFT 审计和分类

总入口会自动执行下面两步。需要单独定位时使用对应脚本。

```bash
.venv-training-py311/bin/python3 training/scripts/planner/audit/audit_sft_budget_fit.py \
  --records training/data/planner/sft_runs/<run>/records.jsonl \
  --output-dir training/data/planner/sft_runs/<run>/audit_budget

.venv-training-py311/bin/python3 training/scripts/planner/audit/classify_sft_budget_usability.py \
  --audit-rows training/data/planner/sft_runs/<run>/audit_budget/audit_rows.jsonl \
  --output-dir training/data/planner/sft_runs/<run>/classification
```

重点检查：

- 请求预算和 `budget_fit_policy` 是否一致。
- `party.total`、住宿晚数、酒店价格和餐饮/门票单位是否正确。
- 候选池是否可达，失败是否集中在某个城市、预算档位或同行类型。
- 分类结果中哪些样本可以导出，哪些需要重生成。
