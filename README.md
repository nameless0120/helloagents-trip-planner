# HelloAgents Trip Planner

一个面向真实旅行规划场景的智能旅行助手。仓库里有可运行的 Web 应用、FastAPI 后端、基于高德地图的结构化工具快照，也保留了后训练数据和评测口径。

当前公开仓库聚焦稳定的 Planner 主线：后端把用户请求、人数、预算、住宿、天气、景点、酒店、餐饮和价格 hint 编译成可审计的 `PlannerContext`，Planner 模型再在这些约束内生成结构化 `TripPlan JSON`。历史实验管线、私有交流记录、模型权重、训练 checkpoint、运行日志和本地密钥不会上传。

## 功能

- 生成多日旅行计划：目的地、日期、同行人数、预算、交通、住宿和偏好共同约束输出。
- 结构化工具快照：后端收集景点、酒店、餐饮、天气、价格 hint 和候选计数，减少模型自由编造。
- 预算账本训练口径：显式区分酒店单房每晚价、景点成人票价、餐饮单人单餐价和同行人数。
- Web 交互界面：Vue 3 + TypeScript + Ant Design Vue，支持旅行需求填写和结果展示。
- 后训练资产：包含 SFT 数据、冻结评估集、规则评测指标和数据生成脚本。

## 界面预览

旅行请求填写：

<img src="docs/images/trip-request.png" alt="旅行请求填写界面" width="720">

旅行计划结果：

<img src="docs/images/trip-plan-result.png" alt="旅行计划结果界面" width="720">

## 技术栈

后端：

- FastAPI
- HelloAgents `SimpleAgent`
- 高德地图 HTTP API / amap MCP 辅助接口
- OpenAI-compatible LLM 服务
- Pydantic schema 校验

前端：

- Vue 3
- TypeScript
- Vite
- Ant Design Vue
- 高德地图 Web JS API

训练与评测：

- LLaMA-Factory 数据格式
- `PlannerContext` 协议
- 规则评测脚本
- SFT / DPO 数据准备脚本

## 目录结构

完整目录职责和本地/公开资产边界见 [PROJECT_STRUCTURE.md](PROJECT_STRUCTURE.md)。

```text
helloagents-trip-planner/
├── backend/
│   ├── app/
│   │   ├── agents/          # Planner Agent、prompt 和生成失败反馈
│   │   ├── api/             # FastAPI 路由
│   │   ├── models/          # TripRequest / TripPlan schema
│   │   ├── planner/         # PlannerContext、预算、票价、路线和输出校验
│   │   └── services/        # LLM、高德、图片等服务封装
│   ├── requirements.txt
│   └── run.py
├── docs/
│   └── images/              # README 展示截图
├── frontend/
│   ├── src/
│   │   ├── services/
│   │   ├── types/
│   │   └── views/
│   ├── package.json
│   └── vite.config.ts
├── skills/               # Codex 本地工作流技能
├── training/
│   ├── configs/             # 按模型分组的训练配置
│   ├── data/                # 训练/评估数据
│   ├── docs/                # 协议、指标和后训练说明
│   ├── outputs/eval/        # 评测输出入口说明
│   └── scripts/             # 训练脚本，按 shared/serving/validation 和当前任务分组
├── PROJECT_STRUCTURE.md  # 项目级目录索引
└── README.md
```

## 快速开始

### 前置条件

- Python 3.11
- Node.js 22 或兼容版本
- 高德地图 API Key
- OpenAI-compatible LLM API Key
- 可选：Unsplash API Key，用于景点图片

### 后端

```bash
cd helloagents-trip-planner/backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

编辑 `backend/.env`，至少配置：

```bash
AMAP_API_KEY=your_amap_api_key
LLM_MODEL_ID=your_model_name
LLM_API_KEY=your_llm_api_key
LLM_BASE_URL=your_openai_compatible_base_url
```

启动服务：

```bash
python run.py
```

默认地址：

- API: `http://localhost:7000`
- Swagger: `http://localhost:7000/docs`
- Health check: `http://localhost:7000/health`

### 前端

```bash
cd helloagents-trip-planner/frontend
npm ci
cp .env.example .env
```

编辑 `frontend/.env`：

```bash
VITE_API_BASE_URL=http://localhost:7000
VITE_AMAP_WEB_KEY=your_amap_web_key
VITE_AMAP_WEB_JS_KEY=your_amap_web_js_key
```

启动开发服务：

```bash
npm run dev -- --host 0.0.0.0 --port 5173
```

默认地址：

- Web: `http://localhost:5173`

## 后训练快速开始

如果你要复现 SFT 或继续做 DPO，不需要先启动 backend 和 frontend。后训练从下面这个总入口开始：

```text
SFT 数据生成
  -> SFT 数据审计/导出
  -> SFT 训练
  -> DPO 数据构造和训练
  -> 模型评测出结果
```

当前后训练统一从 `training/scripts/run_pipeline.py` 开始。SFT 数据生成的底层脚本是 `training/scripts/planner/data/generate_sft_data.py`。

### 1. 准备环境和配置

在项目根目录创建训练环境并安装依赖。已有可用的 CUDA PyTorch 环境时，沿用现有环境，不要为了安装训练依赖重复替换 PyTorch：

```bash
cd helloagents-trip-planner
python3 -m venv .venv-training-py311
source .venv-training-py311/bin/activate
python -m pip install -r training/requirements-training.txt
```

训练数据生成至少需要在 `backend/.env` 或项目根 `.env` 中配置：

```bash
AMAP_MAPS_API_KEY=your_amap_key
DATA_GEN_API_KEY=your_data_generation_key
DATA_GEN_BASE_URL=https://api.deepseek.com
DATA_GEN_MODEL=deepseek-v4-pro
DATA_GEN_THINKING=false
```

也可以继续使用 `DEEPSEEK_API_KEY`、`DEEPSEEK_BASE_URL` 等变量。数据生成默认关闭 thinking；关闭时不会发送 `reasoning_effort` 或 `thinking` 参数，适合直接生成后端需要的 JSON。

如果要训练，还要准备项目指定的 LLaMA-Factory checkout。已经准备好的可以跳过 clone：

```bash
cd ..
git clone https://github.com/hiyouga/LLaMA-Factory.git LLaMA-Factory
cd LLaMA-Factory
git checkout 9a0cfdccfa234304879f83e0c2c17b5ede8121fe
git apply ../helloagents-trip-planner/training/patches/llamafactory-9a0cfdcc-local.patch
cd ../helloagents-trip-planner
.venv-training-py311/bin/python3 -m pip install -e ../LLaMA-Factory --no-deps
```

### 2. 先检查，不调用 API

```bash
.venv-training-py311/bin/python3 training/scripts/run_pipeline.py \
  --stage preflight \
  --strict-preflight
```

只想看完整命令、不生成数据和不训练时，在正式命令末尾加 `--dry-run`。

### 3. 设置本轮路径

下面的 5 条主命令会复用这几个变量，变量名只为少写重复路径：

```bash
export RUN_NAME="$(date +%Y%m%d_%H%M%S)_reader"
export SFT_RUN="training/data/planner/sft_runs/${RUN_NAME}"
export SFT_DATASET="trip_planner_sft_${RUN_NAME}"
export DPO_RUN="training/data/planner/dpo/${RUN_NAME}"
export DPO_DATASET="trip_planner_dpo_${RUN_NAME}"
```

### 4. 数据生成，一个命令

```bash
.venv-training-py311/bin/python3 training/scripts/run_pipeline.py \
  --stage sft-data \
  --count 20 \
  --request-source controlled \
  --date-mode mixed \
  --workers 1 \
  --sft-dir "$SFT_RUN"
```

这一步会调用高德和数据生成模型，输出 `$SFT_RUN/records.jsonl`。如果只是看请求分布，用 `--stage sft-request`，不会调用外部服务。

### 5. 数据审计，一个命令

```bash
.venv-training-py311/bin/python3 training/scripts/run_pipeline.py \
  --stage sft-audit \
  --records "$SFT_RUN/records.jsonl" \
  --sft-dir "$SFT_RUN" \
  --sft-dataset-prefix "$SFT_DATASET"
```

这一步会完成预算审计、可用性分类、干净子集导出和格式校验。通过审计的数据会写入 `training/data/llamafactory/generated/`，并登记到 `training/data/llamafactory/dataset_info.json`。

### 6. SFT 微调，一个命令

```bash
.venv-training-py311/bin/python3 training/scripts/run_pipeline.py \
  --stage train \
  --config training/configs/qwen25_7b/sft_qwen25_7b_lora.yaml \
  --train-dataset "${SFT_DATASET}_train" \
  --train-eval-dataset "${SFT_DATASET}_val" \
  --llamafactory-root ../LLaMA-Factory \
  --train-output-dir training/outputs/qwen25_7b/sft
```

训练阶段需要本地模型缓存、CUDA GPU 和已经应用项目补丁的 LLaMA-Factory。这里不会重新生成数据，只读取上一步登记好的数据集。

### 7. DPO 微调，一个命令

DPO 需要先启动 base 和 SFT 模型服务：

```bash
.venv-training-py311/bin/python3 training/scripts/serving/manage_planner_service.py \
  start-all \
  --services base,sft \
  --base-devices 4,5 \
  --sft-devices 6 \
  --sft-adapter-path training/outputs/qwen25_7b/sft
```

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

DPO 这一条命令会生成 prompt、调用 base/SFT 生成候选、用强模型 judge、构造 chosen/rejected pair、做 DPO 数据审计，然后启动 DPO 训练。

### 8. 评测出结果，一个命令

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

默认端口和模型名：

```text
base -> http://127.0.0.1:4397/v1 -> trip-planner-base
sft  -> http://127.0.0.1:4396/v1 -> trip-planner-sft
dpo  -> http://127.0.0.1:4398/v1 -> trip-planner-dpo
```

查看和停止模型服务：

```bash
.venv-training-py311/bin/python3 training/scripts/serving/manage_planner_service.py status-all
.venv-training-py311/bin/python3 training/scripts/serving/manage_planner_service.py stop-all --kill
```

详细参数见 [training/README.md](training/README.md) 和 [LLaMA-Factory 本地改动说明](training/docs/内部文档/DPO分块LogProb方案说明.md)。

## API 概览

启动后端后可以访问 `http://localhost:7000/docs` 查看完整 OpenAPI 文档。主要接口：

- `POST /api/trip/plan`：生成旅行计划
- `GET /api/trip/health`：检查 Planner 服务
- `GET /api/map/poi`：搜索 POI
- `GET /api/map/weather`：查询天气
- `POST /api/map/route`：规划路线
- `GET /api/poi/detail/{poi_id}`：获取 POI 详情
- `GET /api/poi/photo`：获取景点图片

## 后训练资产

`training/` 目录记录训练和评测主线。这里的做法是先由后端生成稳定、可审计的 `PlannerContext`，再让模型学习把它转换成合法的 `TripPlan JSON`。

推荐入口：

- [CHANGELOG.md](CHANGELOG.md)：版本变更记录和贡献者致谢
- [training/scripts/run_pipeline.py](training/scripts/run_pipeline.py)：统一调度数据生成、审计、DPO、评测和训练阶段
- [training/docs/教程/旅行助手后训练实战教程.md](training/docs/教程/旅行助手后训练实战教程.md)：从 PlannerContext 到 SFT、Best-of-N 和评测的实战教程
- [training/README.md](training/README.md)：后训练目录说明
- [training/STRUCTURE.md](training/STRUCTURE.md)：训练资产、数据、脚本、报告的目录边界
- [training/docs/README.md](training/docs/README.md)：长期文档索引
- [training/outputs/eval/README.md](training/outputs/eval/README.md)：评测输出说明

当前仓库保留主线材料，不上传历史数据、私有交流记录、模型权重、checkpoint 和大规模运行产物。

## 安全与忽略规则

不要提交真实密钥。`.gitignore` 已经排除了这些内容：

- `backend/.env`、`frontend/.env`
- Python / Node 本地环境
- `node_modules/`、构建产物、日志
- 训练输出、模型权重、checkpoint
- 本地实验目录和临时 prompt 文件
- 私有作者交流、会话记忆和临时文档

`.env.example` 会保留在仓库中，作为配置模板。

## 许可证

CC BY-NC-SA 4.0

## 致谢

- [HelloAgents](https://github.com/datawhalechina/Hello-Agents)
- [高德地图开放平台](https://lbs.amap.com/)
- [amap-mcp-server](https://github.com/sugarforever/amap-mcp-server)
