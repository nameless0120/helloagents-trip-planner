# SFT 数据生成

## 请求分布

这一步不调用外部服务：

```bash
.venv-training-py311/bin/python3 training/scripts/run_pipeline.py \
  --stage sft-request \
  --count 20 \
  --request-source controlled \
  --date-mode mixed
```

也可以直接调用 `training/scripts/planner/data/generate_sft_data.py --dry-run-requests --dry-run-summary`。

## PlannerContext smoke

这一步会调用高德，但不会调用数据生成模型：

```bash
.venv-training-py311/bin/python3 training/scripts/run_pipeline.py \
  --stage sft-context \
  --count 20 \
  --request-source controlled \
  --date-mode mixed \
  --workers 1
```

重点检查 `party`、`budget_constraint`、酒店、景点、餐饮、天气和价格 hint。

## SFT run

```bash
RUN_DIR="training/data/planner/sft_runs/$(date +%Y%m%d_%H%M%S)_smoke"
.venv-training-py311/bin/python3 training/scripts/run_pipeline.py \
  --stage sft \
  --count 20 \
  --request-source controlled \
  --date-mode mixed \
  --workers 1 \
  --sft-dir "$RUN_DIR"
```

生成请求需要 `AMAP_MAPS_API_KEY` 和数据生成模型配置。`DATA_GEN_THINKING=false` 时不发送思考参数，直接生成 JSON。

完整链路由总入口调用：

```text
generate_sft_data.py
  -> audit_sft_budget_fit.py
  -> classify_sft_budget_usability.py
  -> export_sft_budget_clean_subset.py
  -> validate_trip_plan.py
```
