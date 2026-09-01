# Planner 数据

这里保留可复用的评测输入和票价资产；SFT、Best-of-N、DPO 的运行数据由总入口写入独立目录，并默认不提交。

```text
training/data/planner/
├── eval/                    # standard 冻结评测输入
├── eval_hard/               # hard 冻结评测输入
├── attraction_prices/       # 票价阶段的本地运行目录
├── sft_runs/                # SFT run，运行时生成
├── bestofn/                 # Best-of-N run，运行时生成
└── dpo/                    # DPO run，运行时生成
```

评测集 records 必须包含结构化 `party`、`budget_constraint` 和 `PlannerContext`。SFT 数据生成统一从：

```text
training/scripts/run_pipeline.py --stage sft-data
```

开始。生成 `records.jsonl` 后，再用 `--stage sft-audit` 做预算审计、可用性分类、`TripPlan` 校验和 LLaMA-Factory 导出。
