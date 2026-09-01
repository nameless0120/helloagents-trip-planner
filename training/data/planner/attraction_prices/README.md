# Attraction Price Assets

更新时间：2026-08-31

景点票价阶段只保留运行说明。候选、审核报告、快照和日志都由总入口在本地生成，
不作为仓库里的固定训练输入。

```text
attraction_prices/
└── pipeline/      # 总入口运行目录，默认忽略
    ├── reports/   # 本轮审核报告
    ├── snapshots/ # 本轮小体积快照
    └── generated/ # 本轮候选、估价 JSONL 和日志
```

## 推荐入口

从已有 records 收集候选、分桶，并可选调用强模型估价：

```bash
.venv-training-py311/bin/python3 training/scripts/run_pipeline.py \
  --stage pricing \
  --records training/data/planner/eval/records.jsonl \
  --pricing-dir training/data/planner/attraction_prices/pipeline
```

需要估价时加 `--estimate-prices`。已有运行目录要继续处理时加 `--resume`。

## 底层脚本

- `training/scripts/planner/pricing/collect_attraction_candidates.py`
- `training/scripts/planner/pricing/bucket_attraction_price_candidates.py`
- `training/scripts/planner/pricing/estimate_attraction_prices_with_llm.py`

这些脚本保留用于单步调试；正式流程优先使用总入口。

估算结果只用于训练预算账本，不代表官方或实时票价。线上使用前需要人工审核，
再按需合并到 `backend/app/planner/attraction_price_table.json`。
