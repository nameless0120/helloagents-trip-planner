# 后训练入口

后训练统一从 `training/scripts/run_pipeline.py` 开始。它把请求生成、PlannerContext、SFT 审计、LLaMA-Factory 数据导出、Best-of-N、DPO、评测、校验和训练接成一条可检查的流程。

## 当前主线

```text
SFT 数据生成
  -> SFT 数据审计/导出
  -> SFT 训练
  -> Best-of-N 数据增强 / 多候选 rerank（可选，但最终有效）
  -> DPO 数据构造和训练
  -> 模型评测出结果
```

底层 SFT 入口只有：

```text
training/scripts/planner/data/generate_sft_data.py
```

## 快速开始

从项目根目录执行：

```bash
python3 -m venv .venv-training-py311
source .venv-training-py311/bin/activate
python -m pip install -r training/requirements-training.txt
```

配置 `backend/.env` 或项目根 `.env`：

```bash
AMAP_MAPS_API_KEY=your_amap_api_key
DATA_GEN_API_KEY=your_data_generation_key
DATA_GEN_BASE_URL=https://api.deepseek.com
DATA_GEN_MODEL=your_model_name
DATA_GEN_THINKING=false
```

## 配套数据下载，可选

如果你想先看现成数据和评测产物，不想一上来就调用 API 生成，可以下载配套材料包：

- 名称：`helloagents-后训练数据`
- 链接：<https://pan.baidu.com/s/5oNsK7pwQnqzQEUg5ykb09Q>

这份数据适合先对照流程。真正复现 LoRA 时，仍然建议按下面命令自己跑一轮，并保留每轮的 `pipeline_manifest.json`、usage 日志和审计报告。

先做不联网检查：

```bash
.venv-training-py311/bin/python3 training/scripts/run_pipeline.py \
  --stage preflight \
  --strict-preflight
```

## 读者复现流程

```bash
export RUN_NAME="$(date +%Y%m%d_%H%M%S)_reader"
export SFT_RUN="training/data/planner/sft_runs/${RUN_NAME}"
export SFT_DATASET="trip_planner_sft_${RUN_NAME}"
export BESTOFN_RUN="training/data/planner/bestofn/${RUN_NAME}"
export BESTOFN_DATASET="trip_planner_bestofn_${RUN_NAME}"
export DPO_RUN="training/data/planner/dpo/${RUN_NAME}"
export DPO_DATASET="trip_planner_dpo_${RUN_NAME}"
```

### 1. 数据生成

```bash
.venv-training-py311/bin/python3 training/scripts/run_pipeline.py \
  --stage sft-data \
  --count 20 \
  --request-source controlled \
  --date-mode mixed \
  --workers 1 \
  --sft-dir "$SFT_RUN"
```

这一步会生成 `$SFT_RUN/records.jsonl`。

### 2. 数据审计

```bash
.venv-training-py311/bin/python3 training/scripts/run_pipeline.py \
  --stage sft-audit \
  --records "$SFT_RUN/records.jsonl" \
  --sft-dir "$SFT_RUN" \
  --sft-dataset-prefix "$SFT_DATASET"
```

这一步会生成预算审计、样本分类、干净子集和 LLaMA-Factory train/val 文件。导出的数据集名是 `${SFT_DATASET}_train` 和 `${SFT_DATASET}_val`。

### 3. SFT 微调

```bash
.venv-training-py311/bin/python3 training/scripts/run_pipeline.py \
  --stage train \
  --config training/configs/qwen25_7b/sft_qwen25_7b_lora.yaml \
  --train-dataset "${SFT_DATASET}_train" \
  --train-eval-dataset "${SFT_DATASET}_val" \
  --llamafactory-root ../LLaMA-Factory \
  --train-output-dir training/outputs/qwen25_7b/sft
```

这一步只训练，不会重新生成数据。

### 4. Best-of-N 数据增强

Best-of-N 是当前保留的有效阶段。它会让 SFT 模型对同一份 `PlannerContext` 生成多个候选，再用规则选出更好的答案，导出新的 SFT 样本和 DPO pair。历史报告里的日期化 `.sh` 启动脚本不再作为入口；当前入口是 `run_pipeline.py --stage bestofn`。

先启动 SFT 服务：

```bash
.venv-training-py311/bin/python3 training/scripts/serving/manage_planner_service.py \
  start-all \
  --services sft \
  --sft-devices 6 \
  --sft-adapter-path training/outputs/qwen25_7b/sft
```

然后生成并选择候选：

```bash
.venv-training-py311/bin/python3 training/scripts/run_pipeline.py \
  --stage bestofn \
  --records "$SFT_RUN/export_budget_clean/records.jsonl" \
  --bestofn-dir "$BESTOFN_RUN" \
  --bestofn-dataset-prefix "$BESTOFN_DATASET" \
  --bestofn-base-url http://127.0.0.1:4396/v1 \
  --bestofn-api-model trip-planner-sft \
  --bestofn-spec t02:0.2:1 \
  --bestofn-spec t05:0.5:2 \
  --bestofn-spec t08:0.8:1 \
  --workers 1
```

输出会登记为 `${BESTOFN_DATASET}_sft_train`、`${BESTOFN_DATASET}_sft_val`、`${BESTOFN_DATASET}_pair_train` 和 `${BESTOFN_DATASET}_pair_val`。要继续做 Best-of-N replay SFT 时，把训练命令里的数据集名换成 `${BESTOFN_DATASET}_sft_train` 和 `${BESTOFN_DATASET}_sft_val`。

产品侧的多候选 rerank 在 `backend/app/planner/rerank.py`，默认由 `PLANNER_ENABLE_RERANK=1` 开启，`PLANNER_RERANK_CANDIDATE_COUNT` 控制候选数。

### 5. DPO 微调

DPO 数据构造要先启动 base 和 SFT 服务：

```bash
.venv-training-py311/bin/python3 training/scripts/serving/manage_planner_service.py \
  start-all \
  --services base,sft \
  --base-devices 4,5 \
  --sft-devices 6 \
  --sft-adapter-path training/outputs/qwen25_7b/sft
```

然后用一条命令生成 DPO 数据并训练：

```bash
.venv-training-py311/bin/python3 training/scripts/run_pipeline.py \
  --stage dpo \
  --stage train \
  --records "$SFT_RUN/export_budget_clean/records.jsonl" \
  --dpo-dir "$DPO_RUN" \
  --dpo-dataset-prefix "$DPO_DATASET" \
  --dpo-workers 1 \
  --judge-workers 1 \
  --config training/configs/qwen25_7b/dpo_qwen25_7b_lora.yaml \
  --llamafactory-root ../LLaMA-Factory \
  --train-output-dir training/outputs/qwen25_7b/dpo
```

这一步会构造 prompt、生成多来源候选、judge、导出 pair、审计 DPO 数据，再进入 LLaMA-Factory DPO。

### 6. 评测出结果

DPO 训练完成后，启动 DPO 服务：

```bash
.venv-training-py311/bin/python3 training/scripts/serving/manage_planner_service.py \
  start-all \
  --services dpo \
  --dpo-devices 7 \
  --dpo-adapter-path training/outputs/qwen25_7b/dpo
```

然后跑冻结评测集：

```bash
.venv-training-py311/bin/python3 training/scripts/run_pipeline.py \
  --stage eval \
  --records training/data/planner/eval/records.jsonl \
  --model-name trip_planner_dpo \
  --api-model trip-planner-dpo \
  --base-url http://127.0.0.1:4398/v1 \
  --eval-dir training/outputs/eval/dpo \
  --workers 1
```

评测结果写入 `training/outputs/eval/dpo/trip_planner_dpo/`。

## 模型服务

默认端口和模型名：

```text
base -> http://127.0.0.1:4397/v1 -> trip-planner-base
sft  -> http://127.0.0.1:4396/v1 -> trip-planner-sft
dpo  -> http://127.0.0.1:4398/v1 -> trip-planner-dpo
```

启动 base、SFT 和 DPO：

```bash
.venv-training-py311/bin/python3 training/scripts/serving/manage_planner_service.py \
  start-all \
  --services base,sft,dpo \
  --base-devices 4,5 \
  --sft-devices 6 \
  --dpo-devices 7 \
  --sft-adapter-path training/outputs/qwen25_7b/sft \
  --dpo-adapter-path training/outputs/qwen25_7b/dpo
```

查看和停止：

```bash
.venv-training-py311/bin/python3 training/scripts/serving/manage_planner_service.py status-all
.venv-training-py311/bin/python3 training/scripts/serving/manage_planner_service.py stop-all --kill
```

`start-all` 只负责起模型服务，不会生成数据或训练。训练输出目录不是默认路径时，用
`--sft-adapter-path` 或 `--dpo-adapter-path` 指到实际 LoRA 目录。

正式运行会调用高德、数据生成模型、模型服务和 GPU。只检查命令时追加 `--dry-run`，不会调用 API 或启动训练。

## 其他阶段

| 阶段 | 作用 | 主要依赖 |
| --- | --- | --- |
| `sft-request` | 检查受控请求分布 | 无外部服务 |
| `sft-context` | 构建 PlannerContext smoke | 高德 API |
| `sft-data` | 生成 SFT records | 高德 API、数据生成模型 |
| `sft-audit` | 审计、分类、导出和校验 SFT 数据 | 本地 records |
| `pricing` | 收集和估算景点票价候选 | records、高德，估价时需要强模型 |
| `eval-data` | 构建冻结评测输入 | 高德 API |
| `bestofn` | 多候选采样、规则选择、导出数据 | Planner 模型服务 |
| `dpo` | 候选生成、judge、pair 和审计 | Base/SFT 服务、强模型 |
| `eval` | 模型生成和规则评测 | Planner 模型服务 |
| `validate` | 校验 SFT、DPO 或评测文件 | 本地文件 |
| `train` | 调用 LLaMA-Factory 训练 | LLaMA-Factory、GPU |

阶段可以重复传入。多阶段运行时用 `--sft-dir`、`--dpo-dir` 等明确指定各阶段目录。

## 目录

```text
training/
├── configs/                  # 当前通用训练配置
├── data/
│   ├── llamafactory/         # dataset_info 和本地生成数据入口
│   └── planner/              # 冻结评测集、票价资产和本地 run 目录
├── docs/                     # 教程、协议、审计口径和指标
├── patches/                  # LLaMA-Factory 补丁
└── scripts/
    ├── run_pipeline.py       # 总入口
    ├── planner/              # SFT、评测、审计、票价、Best-of-N
    ├── eval/                 # 通用评测和 DPO
    ├── serving/              # 模型服务
    ├── validation/           # 输出校验
    └── shared/               # 公共 helper
```

详细命令见 [后训练实战教程](docs/教程/旅行助手后训练实战教程.md)，目录边界见 [STRUCTURE.md](STRUCTURE.md)，LLaMA-Factory 准备见 [本地改动说明](docs/内部文档/DPO分块LogProb方案说明.md)。
