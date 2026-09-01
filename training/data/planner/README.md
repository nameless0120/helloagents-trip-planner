# planner 数据目录

更新时间：2026-05-12

planner 数据从新的 PlannerContext 协议重新生成，不再直接沿用 legacy clean records。目录边界以 `training/STRUCTURE.md` 为准。

当前主入口是 `training/scripts/run_pipeline.py`。例如从已有 SFT records 收集景点候选并分桶：

```bash
.venv-training-py311/bin/python3 training/scripts/run_pipeline.py \
  --stage pricing \
  --records training/data/planner/eval/records.jsonl \
  --pricing-dir training/data/planner/attraction_prices/pipeline
```

底层脚本仍可单独运行，用于定位某一步。目录结构如下：

```text
training/data/planner/
  eval/
    requests.jsonl
    records.jsonl
    errors.jsonl
    summary.json
    数据集说明.md
    评估集摘要.md
    上下文重建说明.md
  eval_hard/
    ...                 # hard split，结构同 eval/
  attraction_prices/
    pipeline/           # 总入口运行目录，默认忽略
      reports/          # 本轮审核说明
      snapshots/        # 本轮小体积票价表快照
      generated/        # 本轮候选/估价 JSONL 和日志
    reports/            # 已整理的公开审核说明
    snapshots/          # 已整理的小体积票价表快照
    generated/          # 旧单脚本运行产物，默认忽略
  SFT已归档说明.md
```

`sft/`、`sft_realbudget_runs/`、`dpo/`、`bestofn/` 和 `archive/` 默认是本地生成或归档资产，不作为公开主入口。新 SFT 数据应写入 `sft_runs/<YYMMDD>_<run_slug>/`，并保留 usage 统计、manifest 和审计摘要。

planner clean SFT 样本必须显式包含：

- `party`
- `budget_constraint`
- `preference_profile`
- `lodging_policy`
- hotel/food `estimated_cost_hint`
- `cost_source`

legacy 数据只作为历史反例库和 pipeline baseline，不进入 planner 主训练集。

## 当前状态

- 当前冻结评估输入为 `eval/records.jsonl` 和 `eval_hard/records.jsonl`。
- 旧名 `eval_harder` 不再作为主入口。
- planner SFT 造数脚本由 `training/scripts/run_pipeline.py --stage sft` 统一调度；底层入口 `training/scripts/planner/data/generate_sft_data.py` 只用于定位单步问题。
- 2026-05-08 之前的旧 Planner SFT 已归档；不要把新 realbudget 数据混写回旧 `sft/`，新 run 使用 `sft_runs/`。
- LLaMA-Factory 入口在 `training/data/llamafactory/`；大体积 train/val JSON/YAML 放在 `generated/`，默认由 `.gitignore` 排除。
