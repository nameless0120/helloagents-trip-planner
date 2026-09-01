# 后训练与评测说明

本目录保存旅行助手的后训练资产。公开仓库只保留当前主线：训练数据、脚本、协议文档、轻量评测报告和可复现配置。历史数据、旧脚本、废弃 prompt 消融、过程日志、模型权重、checkpoint 和大规模生成明细不会上传。

当前目标不是让模型凭空知道更多旅行事实，而是让后端先把事实和约束编译成结构化 `PlannerContext`，再让 Planner 模型稳定生成符合业务协议的 `TripPlan JSON`。

更新时间：2026-08-31。文件结构和生命周期规则见 [STRUCTURE.md](STRUCTURE.md)，长期文档索引见 [docs/README.md](docs/README.md)，本机完整后训练资产地图见 [docs/后训练产物/本地资产索引.md](docs/后训练产物/本地资产索引.md)。

## 分工

```text
前端收集用户意图
  -> 后端结构化人数、预算、偏好、住宿和工具候选
  -> PlannerContext 冻结模型可见事实
  -> Planner 模型生成 TripPlan JSON
  -> 规则评测脚本检查 schema、grounding、预算和偏好指标
```

SFT 主要学习确定性协议：

- JSON 可解析，`TripPlan` schema 通过。
- 日期、天数、天气和住宿晚数正确。
- 景点、酒店、餐饮尽量来自工具候选。
- 酒店、门票、餐饮预算口径稳定。
- `budget.total` 和预算分项关系可校验。

DPO 主要学习合法候选之间的偏好：

- 更符合预算档位。
- 更贴合同行人、饮食、节奏和负向约束。
- 更可执行、更少重复、更适合真实用户。

## 公开目录

```text
training/
├── STRUCTURE.md          # 数据、脚本、文档、报告的目录边界
├── configs/              # 按模型分组的训练配置
├── data/
│   ├── llamafactory/     # LLaMA-Factory 数据入口
│   └── planner/               # 当前训练、评估和票价数据
├── patches/              # 第三方训练依赖补丁
├── docs/                 # 教程、内部协议、指标、预算报告和 DPO 计划
├── outputs/eval/         # 轻量评测报告、comparison 和 manifest
├── prompts/              # 数据生成 prompt
├── scripts/
│   ├── run_pipeline.py    # 后训练总入口
│   ├── shared/           # 公共 helper 和 LLM 客户端
│   ├── serving/          # 本地 Planner 模型服务
│   ├── validation/       # TripPlan schema 校验
│   └── planner/               # 当前脚本按 data/eval/audit/pricing/training 分组
└── requirements-training.txt
```

重要入口：

- `docs/教程/旅行助手后训练实战教程.md`
- `STRUCTURE.md`
- `docs/README.md`
- `docs/内部文档/SFT阶段总结.md`
- `docs/内部文档/规划上下文协议.md`
- `docs/内部文档/评测指标.md`
- `docs/内部文档/Prompt消融阶段总结.md`
- `docs/内部文档/SFT目标与边界.md`
- `docs/内部文档/SFT数据生成口径审核.md`
- `docs/内部文档/全参微调实验备忘录.md`
- `docs/内部文档/DPO分块LogProb方案说明.md`
- `docs/内部文档/典型旅游预算报告.md`
- `docs/内部文档/预算分档与实际数据预算对比.md`
- `docs/内部文档/新预算评估集重建与SFT预算审计.md`
- `data/planner/SFT已归档说明.md`
- `outputs/eval/README.md`
- `outputs/eval/reports/260512_bestofn_replay_extended_w10/bestofn_replay_extended_comparison.md`

## 环境

训练脚本会读取 `backend/.env` 或项目根 `.env`。至少需要：

```bash
AMAP_API_KEY=your_amap_api_key
```

如果要调用强模型生成 SFT 数据、估算票价或做 judge，还需要配置 OpenAI-compatible 或 DeepSeek 风格变量。推荐使用数据生成专用变量，避免影响后端服务：

```bash
DATA_GEN_API_KEY=your_data_generation_key
DATA_GEN_BASE_URL=your_openai_compatible_base_url
DATA_GEN_MODEL=your_model_name
DATA_GEN_REASONING_EFFORT=low
DATA_GEN_THINKING=false
```

新数据生成默认关闭 thinking。`DATA_GEN_THINKING=false` 时不会向模型发送 `reasoning_effort` 或 `thinking` 参数，模型可以直接生成 TripPlan JSON。需要开启思考时再显式设置 `DATA_GEN_THINKING=true`。

安装依赖：

```bash
cd helloagents-trip-planner
python -m venv .venv-training-py311
source .venv-training-py311/bin/activate
pip install -r training/requirements-training.txt
```

其中 PyTorch、torchvision 和 torchaudio 要使用与机器 CUDA 相匹配的一组版本；已有可用的 CUDA PyTorch 环境时，不要为了重装训练栈替换它。

如果本地已经有可用训练环境，可以把下面命令里的 `.venv-training-py311/bin/python3` 换成对应解释器。

训练使用的 LLaMA-Factory 不是任意安装版本。项目记录了基础 commit 和本地补丁，准备方法、环境变量和版本检查见 [LLaMA-Factory 本地改动说明](docs/内部文档/DPO分块LogProb方案说明.md)。统一入口的 `train` 阶段默认查找主项目同级的 `../LLaMA-Factory`，也可以通过 `--llamafactory-root` 或 `LLAMAFACTORY_ROOT` 指定。

## 一个脚本跑当前流程

总入口是 `training/scripts/run_pipeline.py`。它只调度已有后训练脚本，不复制数据生成和评测逻辑；每个阶段单独保留输出目录，失败时会停在具体步骤。Backend、Frontend 和常驻模型服务仍按各自文档启动。

```text
请求分布 smoke
  -> PlannerContext smoke
  -> SFT 数据
  -> 预算审计
  -> 可用性分类
  -> 导出预算干净子集
  -> TripPlan 格式校验
  -> （可选）LLaMA-Factory 训练
```

先看请求分布，不调用高德或强模型：

```bash
.venv-training-py311/bin/python3 training/scripts/run_pipeline.py \
  --stage sft-request \
  --count 20 \
  --request-source controlled \
  --date-mode mixed
```

再检查 PlannerContext 候选池。这个阶段会调用高德，但不会调用 Planner 强模型，也不会写训练 records：

```bash
.venv-training-py311/bin/python3 training/scripts/run_pipeline.py \
  --stage sft-context \
  --count 20 \
  --request-source controlled \
  --date-mode mixed \
  --workers 1
```

确认分布和上下文都没问题后，用同一个入口完成 SFT 生成、审计、分类和导出：

```bash
.venv-training-py311/bin/python3 training/scripts/run_pipeline.py \
  --stage sft \
  --count 20 \
  --request-source controlled \
  --date-mode mixed \
  --workers 1 \
  --output-dir training/data/planner/sft_runs/260831_smoke
```

这个命令会依次调用：

```text
planner/data/generate_sft_data.py
  -> planner/audit/audit_sft_budget_fit.py
  -> planner/audit/classify_sft_budget_usability.py
  -> planner/data/export_sft_budget_clean_subset.py
  -> validation/validate_trip_plan.py
```

输出主要在 `training/data/planner/sft_runs/260831_smoke/`：

- `records.jsonl`、`errors.jsonl`：原始成功记录和失败记录。
- `audit_budget/`：预算贴合审计。
- `classification/`：样本可用性分类。
- `export_budget_clean/`：导出的审计子集和说明。
- `llm_usage.jsonl`：强模型调用的 usage 记录（服务返回时才有内容）。
- `pipeline_manifest.json`：本次总入口的参数记录。

导出的 LLaMA-Factory 文件在 `training/data/llamafactory/generated/`，并会更新 `dataset_info.json`。已有 run 需要接着跑时显式加 `--resume`；不加时如果目录已有 records，脚本会停止，避免把两个实验混在一起。

如果希望从生成数据直接接到 SFT 训练，可以只执行下面这一条命令：

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

入口会按本轮 `--sft-dir` 自动生成数据集名，检查 `dataset_info.json` 和 train/val 文件，再把 `dataset`、`eval_dataset`、`dataset_dir` 和独立的 `output_dir` 传给 LLaMA-Factory，同时为 DeepSpeed 自动设置 `FORCE_TORCHRUN=1`。读者不需要手动改训练 YAML 或复制数据文件。这个命令会调用高德和数据生成模型，并在最后启动 GPU 训练；只想确认命令时，在末尾加 `--dry-run`。

总入口还提供 `pricing`、`eval-data`、`bestofn`、`dpo`、`eval`、`validate` 和 `train` 阶段。可以重复传 `--stage`，例如：

```bash
.venv-training-py311/bin/python3 training/scripts/run_pipeline.py \
  --stage sft \
  --stage dpo \
  --sft-dir training/data/planner/sft_runs/260831_smoke \
  --dpo-dir training/data/planner/dpo/260831_smoke
```

`dpo`、`eval` 和 `train` 需要本地模型服务、强模型配置或 GPU 训练环境，必须按参数显式开启。`train` 使用本轮数据时会自动覆盖配置中的数据集参数；如果训练已有数据，可以只传 `--stage train`，但配置里的数据集必须已经登记在 `training/data/llamafactory/dataset_info.json` 中。只想查看将要执行的子命令时，加 `--dry-run`。

各阶段的作用如下：

| 阶段 | 作用 | 需要的输入或服务 |
| --- | --- | --- |
| `pricing` | 收集景点候选并分桶，可选强模型估价 | `--records` 或 `--collect-context` |
| `eval-data` | 构建冻结评估集 | 高德 API |
| `bestofn` | 多温度候选、规则选择和 SFT/DPO 导出 | Planner 模型服务和 `--records` |
| `dpo` | prompt、多候选、judge、pair 和审计 | Base/SFT 服务、强模型配置和 `--records` |
| `eval` | 单模型生成、规则评测和可选 judge | `--records`、`--model-name`、`--api-model` |
| `validate` | 校验已有 SFT、DPO 或 Eval GT 文件 | `--validate-sft` 等文件参数 |
| `train` | 使用项目固定补丁调用 LLaMA-Factory 训练 | `--config`、`--llamafactory-root` 和训练环境 |

## SFT 数据状态

2026-05-08 之前生成的 SFT 数据已经全量归档，不再作为当前训练入口：

- 旧 `training/data/planner/sft/` 和 `training/data/planner/sft_current/` 已移入 `training/data/planner/archive/`。
- 旧 LLaMAFactory SFT 导出已移入 `training/data/llamafactory/archive/`。
- `training/data/llamafactory/dataset_info.json` 只保留当前明确训练入口；大体积 train/val JSON/YAML 放在 `training/data/llamafactory/generated/`，默认由 `.gitignore` 排除。

后续 SFT 只按 realbudget 新口径重建。建议流程是：

```text
smoke 20 -> 审计 -> 100 条 -> 审计 -> 1000 条 -> 导出 LLaMAFactory
```

新数据必须写入明确的 run 目录，例如 `training/data/planner/sft_runs/<YYMMDD>_<run_slug>/`，不再混写旧 `training/data/planner/sft/`。外部强模型调用必须记录 provider 返回的 `response.usage`，并保留 run manifest，避免 token 成本不可追踪。

## 数据构建脚本

请求和上下文构建脚本仍保留，但推荐从总入口调用。先 dry-run 请求分布，不调用高德或强模型：

```bash
.venv-training-py311/bin/python3 training/scripts/run_pipeline.py \
  --stage sft-request \
  --count 100 \
  --request-source controlled \
  --date-mode mixed
```

只构建 `PlannerContext` smoke，不调用 Planner 强模型：

```bash
.venv-training-py311/bin/python3 training/scripts/run_pipeline.py \
  --stage sft-context \
  --count 20 \
  --request-source controlled \
  --date-mode mixed \
  --workers 1
```

写入训练集前必须做硬校验，包括人数、预算结构、酒店住宿晚数、酒店价格复制、景点票价复制、门票按人数汇总、住宿预算覆盖晚数和预算分项加总。

## 票价表

高德 POI 不一定给出景点票价。当前流程会把高频候选景点收集出来，形成本地票价表候选，用于预算账本训练。

从已有 records 收集候选并分桶：

```bash
.venv-training-py311/bin/python3 training/scripts/run_pipeline.py \
  --stage pricing \
  --records training/data/planner/eval/records.jsonl \
  --pricing-dir training/data/planner/attraction_prices/pipeline
```

按受控请求分布直接收集、分桶：

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

如果要在同一轮继续调用强模型估算票价，在上面的命令中加 `--estimate-prices`：

```bash
.venv-training-py311/bin/python3 training/scripts/run_pipeline.py \
  --stage pricing \
  --records training/data/planner/eval/records.jsonl \
  --pricing-dir training/data/planner/attraction_prices/pipeline \
  --estimate-prices \
  --resume
```

估算结果只用于训练预算口径，不代表官方实时票价。线上使用前需要人工审核并合并到 `backend/app/planner/attraction_price_table.json`。

## 评估集

构建 standard eval：

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

构建 hard eval：

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

公开仓库保留的评估入口：

- `training/data/planner/eval/records.jsonl`
- `training/data/planner/eval_hard/records.jsonl`

所有 baseline、SFT、DPO 对比都应复用这些冻结输入，避免请求分布、工具快照或天气来源变化影响模型对比。

## 当前评测口径

评测固定输出两层主要 pass：

- `sft_hard_pass`：线上可用的确定性协议，包括 schema、日期、天气、住宿、grounding、预算账本和硬预算约束。
- `dpo_soft_pass`：在合法输出基础上看餐饮多样性、餐饮 grounding、预算偏好和整体可用性。

阶段性还记录：

- `sft_budget_semantic_hard_pass`
- `hotel_budget_relation_ok`
- `attraction_budget_party_relation_ok`
- `meal_cost_scale_ok`
- `budget_relationship_ok`

完整口径见评测指标文档。

## 当前公开结果

当前评测输出统一按新目录组织：

```text
training/outputs/eval/by_model/<model>/<YYMMDD>_<run_slug>/
training/outputs/eval/comparisons/<YYMMDD>_<comparison_slug>/
training/outputs/eval/audits/<YYMMDD>_<audit_slug>/
training/outputs/eval/logs/<YYMMDD>_<log_slug>/
training/outputs/eval/reports/<YYMMDD>_<report_slug>/
```

当前可公开引用的报告都整理到 `reports/`：

- `outputs/eval/reports/260512_bestofn_replay_extended_w10/`：2026-05-12 Best-of-N replay 扩展对比，包含多个 checkpoint、上一轮 replay、前序 LoRA、旧路线对照与外部 Mimo reference 的 500 条合并/standard/hard 主要指标。
- `outputs/eval/reports/260511_usage700_followup_w10/`：usage700 SFT follow-up 对比。
- `outputs/eval/reports/260511_high_end_context_mainline/`：高端 POI 上下文重构后三模型主线对比。

`by_model/`、`comparisons/`、`audits/`、`logs/` 默认视为本地生成产物；需要公开的评估结论先整理成 `reports/<YYMMDD>_<slug>/`。

## DPO 状态

当前主线把 DPO 定位为偏好训练，而不是修坏 JSON 或坏 schema。DPO prompt source 来自 `PlannerContext` 和 `planner_query`，不直接使用 teacher answer。

当前 DPO prompt source 只在本地保留，不进入公开仓库：

- `training/data/planner/dpo/prompts.jsonl`
- `training/data/planner/dpo/prompt_source/records.jsonl`

公开仓库只保留 DPO 口径和轻量说明。pair 构造、judge、prompt source 和训练产物仍按本地实验资产处理；当前公开参考为 `docs/后训练产物/03_DPO阶段/README.md`、`docs/后训练产物/04_Rerank阶段/README.md`、`scripts/planner/README.md` 和 `scripts/planner/bestofn/README.md`。单生成最佳点是 `260519 checkpoint-138`；最终展示版本是 `260521 checkpoint-64 rerank n4`。

## 不上传的内容

这些内容是本地实验资产，不进入 GitHub：

- 历史数据和脚本
- 废弃 prompt 消融归档
- 推进记录、踩坑记录、面试速记、作者交流、会话记忆和临时 HTML
- `training/outputs/` 下的大规模 generations、日志和模型输出明细
- `training/data/planner/archive/` 和 `training/data/llamafactory/archive/`
- LoRA 权重、checkpoint、`.safetensors`、`.pt`、`.bin`
- `.venv-training-py311/`、`.uv-cache/` 等本地环境
