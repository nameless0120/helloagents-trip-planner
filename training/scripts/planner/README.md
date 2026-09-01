# 当前脚本目录

更新时间：2026-08-31

当前脚本按 `data/`、`eval/`、`audit/`、`pricing/`、`bestofn/`、`training/` 分组；目录生命周期规则见 `training/STRUCTURE.md`。旧脚本只作为参考，不再继续堆补丁。

第一批要迁移/重写的能力：

1. `PlannerContext` 构造
   - 显式生成 `party`
   - 显式生成 `budget_constraint`
   - 显式生成 `preference_profile`
   - 显式生成 `lodging_policy`
   - 给酒店/餐饮补 `estimated_cost_hint` 和 `cost_source`

2. SFT 数据生成
   - 生成 requests
   - 获取工具快照
   - 用强模型生成 TripPlan
   - 严格校验酒店价格复制、住宿晚数和预算账本

3. SFT 数据审计和切分
   - 清洗 dirty 数据
   - 固定 train/val/eval
   - 输出 LLaMA-Factory 格式

4. DPO 数据生成
   - 复用 PlannerContext
   - 多模型自然候选
   - 规则硬过滤
   - LLM judge
   - chosen/rejected pair 构造

## 分类

- `data/`：SFT/realbudget 数据生成、预览和清洗导出。
- `pricing/`：景点候选收集、票价分桶和强模型估价。
- `eval/`：frozen eval 构建、prompt/context 刷新和预算修正实验。
- `audit/`：预算贴合度、上下文可达性和 SFT 可用性审计。
- `training/`：本地训练启动/恢复脚本。
- `bestofn/`：多候选采样、规则 reward 选择和偏好/SFT 数据导出。

## 推荐入口

后训练流程统一从 `training/scripts/run_pipeline.py` 进入。当前 SFT 一条命令会完成生成、预算审计、可用性分类和 LLaMA-Factory 导出：

```bash
.venv-training-py311/bin/python3 training/scripts/run_pipeline.py \
  --stage sft \
  --count 20 \
  --request-source controlled \
  --date-mode mixed \
  --workers 1 \
  --output-dir training/data/planner/sft_runs/260831_smoke
```

流程可以按下面理解：

```text
planner/data/generate_sft_data.py
  -> planner/audit/audit_sft_budget_fit.py
  -> planner/audit/classify_sft_budget_usability.py
  -> planner/data/export_sft_budget_clean_subset.py
  -> training/data/llamafactory/generated/<dataset>_train.json
  -> validation/validate_trip_plan.py
```

生成前可以先把 `--stage` 改成 `sft-request` 或 `sft-context` 做检查。前者不调用外部服务，后者只查询高德和构建 PlannerContext，不调用 Planner 强模型。各个子脚本仍然可以单独运行，但主要用于定位某一步的问题。

## 已迁入脚本

### `data/generate_sft_data.py`

生成 SFT 数据，默认使用受控真实分布，不再复用旧数据。

单独调试时，先看请求分布，不调用高德和强模型：

```bash
.venv-training-py311/bin/python3 training/scripts/planner/data/generate_sft_data.py \
  --count 100 \
  --request-source controlled \
  --date-mode mixed \
  --dry-run-requests \
  --dry-run-summary
```

单独调试时，只跑 PlannerContext smoke，不调用 Planner 强模型：

```bash
.venv-training-py311/bin/python3 training/scripts/planner/data/generate_sft_data.py \
  --count 20 \
  --request-source controlled \
  --date-mode mixed \
  --workers 1 \
  --dry-run-context
```

正式小批量生成请使用上面的总入口。底层脚本单独运行只用于定位请求、上下文或
teacher 生成的问题，正式数据仍要经过总入口里的审计、分类、导出和格式校验。

输出：

- `training/data/planner/sft_runs/<YYMMDD>_<run_slug>/requests.jsonl`
- `training/data/planner/sft_runs/<YYMMDD>_<run_slug>/records.jsonl`
- `training/data/planner/sft_runs/<YYMMDD>_<run_slug>/errors.jsonl`
- `training/data/llamafactory/generated/<dataset>_train.json`
- `training/data/llamafactory/generated/<dataset>_val.json`
- `training/data/llamafactory/dataset_info.json`

当前 SFT 写入前会硬校验：

- `party.total` 和预算结构必须合法。
- 中间住宿日 `hotel` 不能为空。
- `hotel.estimated_cost` 必须复制候选 `estimated_cost_hint`。
- `attraction.ticket_price` 必须复制候选 `ticket_price_hint`。
- `budget.total_hotels` 必须覆盖逐日住宿晚数。
- `budget.total_attractions` 必须按 `party.total` 汇总门票。
- `budget.total` 必须等于四个预算分项之和。

### `pricing/collect_attraction_candidates.py`

收集 PlannerContext 中出现过的景点候选，用于补本地票价表。这个脚本不调用 Planner 强模型。

正式流程从已有 records 收集候选并分桶：

```bash
.venv-training-py311/bin/python3 training/scripts/run_pipeline.py \
  --stage pricing \
  --records training/data/planner/eval/records.jsonl \
  --pricing-dir training/data/planner/attraction_prices/pipeline
```

直接按受控分布查询 PlannerContext，并完成候选分桶：

```bash
.venv-training-py311/bin/python3 training/scripts/run_pipeline.py \
  --stage pricing \
  --collect-context \
  --count 200 \
  --request-source controlled \
  --date-mode mixed \
  --workers 1 \
  --pricing-dir training/data/planner/attraction_prices/pipeline
```

要继续用强模型估价，在命令中加 `--estimate-prices`。上面列出的三个 pricing 子脚本仍可单独运行，但只建议用于定位某一步。

输出：

- `training/data/planner/attraction_prices/pipeline/generated/attraction_candidates.jsonl`
- `training/data/planner/attraction_prices/pipeline/reports/景点票价候选收集报告.md`
- `training/data/planner/attraction_prices/pipeline/snapshots/attraction_price_table_todo.json`

判断口径：

- 高德已有 `cost` 的景点不需要进入本地表。
- 命中 `backend/app/planner/attraction_price_table.json` 的景点不需要重复补。
- 高德无 `cost` 且没有命中本地表的景点，会进入待补模板。

### `pricing/bucket_attraction_price_candidates.py`

把高频景点候选按票价处理方式分桶，方便人工审核哪些景点应进入本地票价画像表。

```bash
.venv-training-py311/bin/python3 training/scripts/planner/pricing/bucket_attraction_price_candidates.py \
  --min-request-count 5
```

输出：

- `training/data/planner/attraction_prices/pipeline/generated/request_count_ge5_bucketed_candidates.jsonl`
- `training/data/planner/attraction_prices/pipeline/reports/request_count_ge5_景点票价分桶审核.md`
- `training/data/planner/attraction_prices/pipeline/snapshots/request_count_ge5_price_table_review_draft.json`

### `pricing/estimate_attraction_prices_with_llm.py`

对 `request_count >= 5` 的高频景点统一调用强模型估算成人全价票价，并明确标记为 `llm_estimated`。这批价格只用于 SFT 的预算账本训练，不是官方票价或实时票价。

只想检查估价 prompt，可以直接运行底层脚本的 `--dry-run-prompt`；正式估价建议从总入口调用：

```bash
.venv-training-py311/bin/python3 training/scripts/planner/pricing/estimate_attraction_prices_with_llm.py \
  --input training/data/planner/attraction_prices/pipeline/generated/request_count_ge5_bucketed_candidates.jsonl \
  --output-dir training/data/planner/attraction_prices/pipeline \
  --min-request-count 5 \
  --batch-size 5 \
  --limit 5 \
  --dry-run-prompt
```

```bash
.venv-training-py311/bin/python3 training/scripts/run_pipeline.py \
  --stage pricing \
  --records training/data/planner/eval/records.jsonl \
  --pricing-dir training/data/planner/attraction_prices/pipeline \
  --estimate-prices \
  --resume
```

单独运行底层估算脚本时：

```bash
nohup .venv-training-py311/bin/python3 -u training/scripts/planner/pricing/estimate_attraction_prices_with_llm.py \
  --input training/data/planner/attraction_prices/pipeline/generated/request_count_ge5_bucketed_candidates.jsonl \
  --output-dir training/data/planner/attraction_prices/pipeline \
  --min-request-count 5 \
  --batch-size 20 \
  --resume \
  > training/data/planner/attraction_prices/pipeline/generated/estimate_prices_llm.log 2>&1 &
```

输出：

- `training/data/planner/attraction_prices/pipeline/generated/request_count_ge5_llm_price_estimates.jsonl`
- `training/data/planner/attraction_prices/pipeline/snapshots/request_count_ge5_attraction_price_table_llm_estimated.json`
- `training/data/planner/attraction_prices/pipeline/reports/景点票价强模型估算说明.md`

后续如果要用于线上 Planner，需要把估价表审核后合并到：

- `backend/app/planner/attraction_price_table.json`

### `eval/build_eval_set.py`

构建 frozen 评估集。这个脚本只生成请求、获取 PlannerContext、
写入压缩上下文和最终 Planner prompt，不调用模型生成 TripPlan。

先小批量 smoke：

```bash
.venv-training-py311/bin/python3 training/scripts/run_pipeline.py \
  --stage eval-data \
  --count 10 \
  --start-index 0 \
  --request-source controlled \
  --date-mode mixed \
  --workers 2 \
  --eval-data-dir training/data/planner/eval_smoke
```

正式构建评估集：

```bash
.venv-training-py311/bin/python3 training/scripts/run_pipeline.py \
  --stage eval-data \
  --count 200 \
  --start-index 0 \
  --id-prefix standard200_eval \
  --request-source controlled \
  --date-mode mixed \
  --workers 4 \
  --eval-data-dir training/data/planner/eval \
  --resume
```

构建更难的 hard eval，用于拉开 base/SFT/DPO 能力差异：

当前 hard eval 使用原 `harder` 压力分布构建，主路径统一命名为 `eval_hard`。

```bash
.venv-training-py311/bin/python3 training/scripts/run_pipeline.py \
  --stage eval-data \
  --count 300 \
  --start-index 0 \
  --id-prefix harder_eval \
  --request-source controlled \
  --date-mode mixed \
  --difficulty harder \
  --workers 2 \
  --eval-data-dir training/data/planner/eval_hard \
  --resume
```

输出：

- `training/data/planner/eval/records.jsonl`
- `training/data/planner/eval/requests.jsonl`
- `training/data/planner/eval/errors.jsonl`
- `training/data/planner/eval/summary.json`
- `training/data/planner/eval/评估集摘要.md`
- `training/data/planner/eval_hard/records.jsonl`
- `training/data/planner/eval_hard/requests.jsonl`
- `training/data/planner/eval_hard/errors.jsonl`
- `training/data/planner/eval_hard/summary.json`
- `training/data/planner/eval_hard/评估集摘要.md`

后续所有 baseline/SFT/DPO 评估都应优先使用这两份固定输入，避免请求分布、
工具快照、天气来源变化影响模型对比。

如果后端 PlannerContext 检索能力发生变化，但仍希望保留同一批请求和
`record_id` 做横向比较，不要重采样请求，改用 context rebuild：

```bash
.venv-training-py311/bin/python3 training/scripts/planner/eval/rebuild_eval_contexts.py \
  --input-records training/data/planner/archive/eval_pre_high_end_context_20260511/eval/records.jsonl \
  --output-dir training/data/planner/eval \
  --workers 2 \
  --source-label 260511_high_end_poi_context_rebuild

.venv-training-py311/bin/python3 training/scripts/planner/eval/rebuild_eval_contexts.py \
  --input-records training/data/planner/archive/eval_pre_high_end_context_20260511/eval_hard/records.jsonl \
  --output-dir training/data/planner/eval_hard \
  --workers 2 \
  --source-label 260511_high_end_poi_context_rebuild
```

这会保留请求分布和样本 ID，只重新调用当前后端的 POI/天气/价格 hint
链路，并重建 `compact_planner_context` 与 `planner_query`。后续同一轮
baseline/SFT/DPO 评测必须使用同一份 rebuild 后的 records，避免新旧工具
快照混在一次模型对比里。

## DPO 流程

当前 DPO 是在合法候选之间学习偏好，不负责修复坏 JSON 或坏 schema。输入来自
SFT 或其他当前训练数据的 records，但 prompt 只保留 request、PlannerContext
和 planner_query，不使用 teacher answer。

当前主线可以按下面理解：

```text
当前 SFT records（只取 train，排除 frozen eval）
  -> prepare_high_confidence_dpo_contexts.py
     或 prepare_planner_soft_dpo_contexts.py
  -> eval/dpo_build_prompts.py
  -> eval/dpo_generate_candidates.py
     （Base / SFT / Strong / MIMO 多候选，并做规则评估）
  -> planner/bestofn/build_high_confidence_dpo_pairs.py
     或 planner/build_planner_soft_*_dpo.py
  -> chosen / rejected
  -> LLaMA-Factory ranking JSON + dataset_info.json
  -> configs/qwen25_7b/dpo_*.yaml
  -> planner/training/*.sh
```

训练时要使用项目记录的 LLaMA-Factory 基础 commit 和本地补丁。推荐通过
`training/scripts/run_pipeline.py --stage train` 启动，它会检查 checkout、补丁和源码路径；补丁内容和准备命令见
`training/docs/内部文档/DPO分块LogProb方案说明.md`。旧的实验 shell 脚本保留了当时机器上的绝对路径，不作为新环境的默认入口。

其中，pair 构造脚本会按 schema、生成是否完整、hard pass、planner soft、预算和
餐饮等规则筛选 chosen/rejected。当前主线一般直接使用这些规则指标，不一定调用
`eval/dpo_judge_candidates.py`。

只想验证通用 DPO 工具链时，才使用下面这条 smoke 链：

```text
eval/dpo_build_prompts.py
  -> eval/dpo_generate_candidates.py
  -> eval/dpo_judge_candidates.py
  -> eval/dpo_build_pairs.py
  -> eval/dpo_audit_pairs.py
```

这组脚本的默认路径仍是 `training/data/legacy`。如果传入
`training/data/planner/dpo`，需要自己显式指定输入、输出和 LLaMA-Factory 数据集名。
Best-of-N 的通用 prompt、候选生成和选择说明见：

```text
training/scripts/planner/bestofn/README.md
training/docs/内部文档/DPO分块LogProb方案说明.md
```
