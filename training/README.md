# 后训练入口

后训练统一从 `training/scripts/run_pipeline.py` 开始。它把请求生成、PlannerContext、SFT 审计、LLaMA-Factory 数据导出、Best-of-N、DPO、评测、校验和训练接成一条可检查的流程。

## 当前主线

```text
请求分布
  -> PlannerContext
  -> SFT records
  -> 预算审计
  -> 可用性分类
  -> LLaMA-Factory train/val
  -> TripPlan 校验
  -> SFT 训练
  -> DPO / Best-of-N / 评测（按需）
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

先做不联网检查：

```bash
.venv-training-py311/bin/python3 training/scripts/run_pipeline.py \
  --stage preflight \
  --strict-preflight
```

## 一条命令生成并训练 SFT

```bash
RUN_DIR="training/data/planner/sft_runs/$(date +%Y%m%d_%H%M%S)_reader_train"
.venv-training-py311/bin/python3 training/scripts/run_pipeline.py \
  --stage sft \
  --stage train \
  --count 20 \
  --request-source controlled \
  --date-mode mixed \
  --workers 1 \
  --sft-dir "$RUN_DIR" \
  --config training/configs/qwen25_7b/sft_qwen25_7b_lora.yaml \
  --llamafactory-root ../LLaMA-Factory \
  --train-output-dir training/outputs/qwen25_7b/sft
```

正式运行会调用高德、数据生成模型和 GPU。只检查命令时追加 `--dry-run`，不会调用 API 或启动训练。

只生成和审计数据时，去掉 `--stage train` 与训练参数：

```bash
.venv-training-py311/bin/python3 training/scripts/run_pipeline.py \
  --stage sft \
  --count 20 \
  --request-source controlled \
  --date-mode mixed \
  --workers 1 \
  --output-dir training/data/planner/sft_runs/<run>
```

生成结果写入 run 目录，导出的 LLaMA-Factory 文件写入 `data/llamafactory/generated/`，并登记在 `dataset_info.json`。

## 一条命令启动模型服务

DPO 数据生成默认需要两个本地模型服务：

```text
base model -> http://127.0.0.1:4397/v1 -> trip-planner-base
SFT model  -> http://127.0.0.1:4396/v1 -> trip-planner-sft
```

启动这两个服务：

```bash
.venv-training-py311/bin/python3 training/scripts/serving/manage_planner_service.py \
  start-all \
  --services base,sft \
  --base-devices 4,5 \
  --sft-devices 6 \
  --sft-adapter-path training/outputs/qwen25_7b/sft
```

DPO 训练完成后，如果要同时评测 SFT 和 DPO，可以把 DPO 服务也起起来：

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

查看和停止服务：

```bash
.venv-training-py311/bin/python3 training/scripts/serving/manage_planner_service.py status-all
.venv-training-py311/bin/python3 training/scripts/serving/manage_planner_service.py stop-all --kill
```

`start-all` 只负责起模型服务，不会生成数据或训练。训练输出目录不是默认路径时，用
`--sft-adapter-path` 或 `--dpo-adapter-path` 指到实际 LoRA 目录。

## 其他阶段

| 阶段 | 作用 | 主要依赖 |
| --- | --- | --- |
| `sft-request` | 检查受控请求分布 | 无外部服务 |
| `sft-context` | 构建 PlannerContext smoke | 高德 API |
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
