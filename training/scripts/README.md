# Training Scripts Index

更新时间：2026-08-31

这个目录只放当前还可能直接运行的训练、服务、校验入口。旧实验脚本默认作为本地参考或归档资产处理，不作为公开主线入口。

## 统一入口

`run_pipeline.py` 是后训练总入口。它按阶段调用下面的现有脚本，并在阶段之间传递明确的输入输出。最常用的 SFT 流程是：

```text
SFT 请求 smoke
  -> PlannerContext smoke
  -> SFT 生成
  -> 预算审计
  -> 可用性分类
  -> 预算干净子集导出
  -> TripPlan 格式校验
  -> （可选）LLaMA-Factory
```

如果要让数据生成完成后自动接到训练，使用同一个入口并同时传 `--stage sft --stage train`：

```bash
.venv-training-py311/bin/python3 training/scripts/run_pipeline.py \
  --stage sft \
  --stage train \
  --count 20 \
  --request-source controlled \
  --date-mode mixed \
  --workers 1 \
  --sft-dir training/data/planner/sft_runs/260901_reader_smoke \
  --config training/configs/qwen25_7b/sft_qwen25_7b_lora.yaml \
  --llamafactory-root ../LLaMA-Factory
```

`run_pipeline.py` 会把本轮生成的 train/val 数据集名自动覆盖到训练命令中，并在启动训练前检查 `dataset_info.json` 和实际文件。`--dry-run` 只打印这些命令，不会调用子脚本、API 或 GPU。

直接运行当前 SFT 数据链路：

```bash
.venv-training-py311/bin/python3 training/scripts/run_pipeline.py \
  --stage sft \
  --count 20 \
  --request-source controlled \
  --date-mode mixed \
  --workers 1 \
  --output-dir training/data/planner/sft_runs/260831_smoke
```

只看总入口会执行哪些子命令：

```bash
.venv-training-py311/bin/python3 training/scripts/run_pipeline.py \
  --stage sft \
  --output-dir /tmp/trip-planner-sft-smoke \
  --dry-run
```

`--stage` 可以重复传入。可用阶段是 `sft-request`、`sft-context`、`sft`、`pricing`、`eval-data`、`bestofn`、`dpo`、`eval`、`validate` 和 `train`。需要 API、模型服务或 GPU 的阶段不会被默认执行；已有中间结果要继续使用时传 `--resume`。

`train` 阶段会校验项目固定的 LLaMA-Factory 基础 commit 和补丁，并把指定 checkout 的 `src/` 放到 `PYTHONPATH`。准备方法见 `training/docs/内部文档/DPO分块LogProb方案说明.md`。

## 目录结构

| Path | Purpose |
| --- | --- |
| `shared/` | JSONL、路径、环境变量、LLM 客户端等公共 helper |
| `serving/` | 本地 Planner 模型服务启动、停止和 LLaMA-Factory API 配置生成 |
| `validation/` | SFT/DPO/Eval 输出 schema 校验 |
| `planner/data/` | SFT/realbudget 数据生成、预览和清洗导出 |
| `planner/pricing/` | 景点候选收集、票价分桶和强模型估价 |
| `planner/eval/` | frozen eval 构建、prompt/context 刷新和预算修正实验 |
| `planner/audit/` | SFT 预算贴合度、上下文可达性和可用性审计 |
| `planner/training/` | 本地训练启动/恢复脚本 |
| `planner/bestofn/` | 多候选采样、规则 reward 选择和偏好/SFT 数据导出 |
| `eval/` | 旧 SFT 链路、评测脚本和通用 DPO 辅助工具；不作为当前 SFT 主线入口 |
| `archive/` | legacy helper 和实验脚本归档，公开仓库默认忽略 |

## 当前入口

| Script | Purpose |
| --- | --- |
| `run_pipeline.py` | 统一调度 SFT、票价候选、Best-of-N、通用 DPO、评测和训练阶段 |
| `planner/data/generate_sft_data.py` | SFT / realbudget 数据生成、request dry-run 和 PlannerContext smoke |
| `planner/eval/build_eval_set.py` | 构建 standard / hard frozen eval 输入 |
| `planner/eval/rebuild_eval_contexts.py` | 保留 request 与 record id，按当前后端重建 eval context |
| `planner/eval/generate_full_report.py` | 汇总评测指标并生成报告 |
| `planner/audit/audit_sft_budget_fit.py` | SFT 预算贴合度审计 |
| `planner/audit/classify_sft_budget_usability.py` | SFT 预算可用性分类 |
| `planner/pricing/collect_attraction_candidates.py` | 从 PlannerContext 收集景点候选，用于票价表补全 |
| `planner/pricing/estimate_attraction_prices_with_llm.py` | 高频景点票价估算，只用于训练预算口径 |
| `planner/bestofn/` | Best-of-N prompt、候选生成、review 和选择流程 |
| `serving/serve_planner_model.py` | 启动本地 OpenAI-compatible Planner 推理服务，用于 base/SFT/DPO/SFT+DPO 结果对比 |
| `serving/manage_planner_service.py` | 管理本地 Planner 模型服务 |
| `validation/validate_trip_plan.py` | 校验 SFT/DPO/Eval JSONL 是否符合后端 `TripPlan` schema |

## 共享 helper

| Script | Purpose |
| --- | --- |
| `shared/common.py` | JSONL、路径、环境变量、日期等通用工具；旧数据目录常量使用前需要确认语义 |
| `shared/llm_client.py` | DeepSeek/OpenAI-compatible 数据生成客户端；可作为强模型生成和 judge 的基础封装 |

## 旧规则

旧脚本只作为工程参考或本地 helper，不要直接复用旧产物作为当前训练数据。新增能力优先放入当前脚本分组，并同步更新 `training/README.md`、`training/STRUCTURE.md` 和这份 README。
