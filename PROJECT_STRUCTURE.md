# 项目目录索引

更新时间：2026-05-22

这个文件解释 `helloagents-trip-planner/` 根目录下每一类目录和文件的用途。它和 `training/docs/后训练产物/本地资产索引.md` 的关系是：这里管整个项目，后者只细讲后训练工作台。

当前工作区约 72G。主要体量来自本地训练产物和环境：`training/outputs/` 约 56G，`.venv-training-py311/` 约 6.7G，`.git/` 约 6G。源码本身很小，大文件默认都不该进公开仓库。

## 顶层目录

| 路径 | 类型 | 是否提交 | 说明 |
| --- | --- | --- | --- |
| `backend/` | 后端应用 | 是 | FastAPI 服务、PlannerContext 构建、工具候选、预算/票价/rerank 规则、LLM 和高德服务封装。 |
| `frontend/` | 前端应用 | 是 | Vue 3 + TypeScript + Vite + Ant Design Vue 的旅行助手 Web 界面。 |
| `training/` | 后训练工作台 | 部分提交 | 数据生成、SFT/DPO、评测、报告、模型输出和本地实验资产。详细看 `training/README.md` 与 `training/docs/后训练产物/本地资产索引.md`。 |
| `docs/` | 根 README 图片 | 是 | 项目首页截图，目前主要是 `docs/images/`。训练教程图片放在 `training/docs/教程/images/`。 |
| `skills/` | Codex 本地工作流技能 | 部分提交 | `trip-planner-eval-compare` 和 `trip-planner-sft-data-loop` 是可复用项目技能；`trip-planner-model-eval` 是本地临时评测 skill，默认忽略。 |
| `.git/` | Git 历史 | 否 | 本地仓库历史，不手动改。当前较大是因为训练/文档多轮提交历史。 |
| `.uv-cache/` | uv 缓存 | 否 | Python 包缓存，可删除再生成。 |
| `.venv-training-py311/` | 训练虚拟环境 | 否 | 后训练脚本用的 Python 3.11 环境，可按 `training/requirements-training.txt` 重建。 |

## 顶层文件

| 路径 | 说明 |
| --- | --- |
| `README.md` | 项目首页：产品介绍、启动方式、后训练入口。 |
| `PROJECT_STRUCTURE.md` | 当前文件：根目录级资产地图。 |
| `TODO.md` | 项目过程中的任务和想法记录，提交前需要确认是否仍适合公开。 |
| `.gitignore` | 忽略本地密钥、环境、日志、模型权重、训练输出和本地生成物。 |

## Backend 目录

| 路径 | 类型 | 说明 |
| --- | --- | --- |
| `backend/run.py` | 启动入口 | 本地启动 FastAPI 服务。 |
| `backend/requirements.txt` | 依赖 | 后端运行依赖。 |
| `backend/.env.example` | 配置模板 | 可提交；真实 `backend/.env` 被忽略。 |
| `backend/app/api/` | API 层 | FastAPI app 和 `trip`、`map`、`poi` 路由。 |
| `backend/app/models/` | Schema | `TripRequest`、`TripPlan` 等 Pydantic 模型。 |
| `backend/app/agents/` | Planner Agent | Prompt、Planner query、生成失败反馈和 agent 封装。 |
| `backend/app/planner/` | 规划核心 | `PlannerContext`、候选压缩、日期、天气、POI、预算、价格、路线、输出校验和 rerank。 |
| `backend/app/services/` | 服务封装 | LLM、高德、Unsplash、MCP 环境等外部服务适配。 |
| `backend/.venv/` | 本地环境 | 忽略，可重建。 |
| `backend/v3_backend_dev.log` | 本地日志 | 忽略，可删除。 |

`backend/app/planner/` 是这个项目最关键的产品逻辑目录。后训练不是让模型凭空猜旅行事实，而是依赖这里把请求和工具候选编译成可审计上下文。

## Frontend 目录

| 路径 | 类型 | 说明 |
| --- | --- | --- |
| `frontend/package.json` | 前端依赖和命令 | Vite 开发、构建入口。 |
| `frontend/package-lock.json` | 锁文件 | 固定 npm 依赖版本。 |
| `frontend/.env.example` | 配置模板 | 可提交；真实 `frontend/.env` 被忽略。 |
| `frontend/src/main.ts` | 应用入口 | Vue app 初始化。 |
| `frontend/src/App.vue` | 根组件 | 页面框架。 |
| `frontend/src/views/Home.vue` | 输入页 | 旅行需求填写。 |
| `frontend/src/views/Result.vue` | 结果页 | TripPlan 展示。 |
| `frontend/src/services/api.ts` | API client | 调后端接口。 |
| `frontend/src/types/` | 前端类型 | TripRequest / TripPlan 等类型定义。 |
| `frontend/dist/` | 构建产物 | 忽略，可重建。 |
| `frontend/node_modules/`、`frontend/.nodeenv*` | 本地依赖环境 | 忽略，可重建。 |
| `frontend/v3_frontend_dev.log` | 本地日志 | 忽略，可删除。 |

## Training 目录

| 路径 | 类型 | 说明 |
| --- | --- | --- |
| `training/README.md` | 后训练入口 | 后训练目标、环境、SFT/DPO/评测状态。 |
| `training/STRUCTURE.md` | 结构约定 | 数据、脚本、报告和输出的生命周期规则。 |
| `training/configs/` | 训练配置 | SFT/DPO/export/DeepSpeed 配置；临时 serve 配置默认忽略。 |
| `training/data/` | 训练和评测数据 | 冻结 eval 可提交；SFT/DPO/generated 大数据默认本地保留。 |
| `training/docs/` | 后训练文档 | 教程、内部文档、读者版实验归档、本地资产索引。 |
| `training/scripts/` | 后训练脚本 | 数据生成、审计、评测、serve、训练 launcher、rerank 工具。 |
| `training/scripts/run_pipeline.py` | 后训练总入口 | 按阶段串联 SFT、票价候选、Best-of-N、DPO、评测、校验和训练。 |
| `training/outputs/` | 模型和评测输出 | 大体积本地产物，默认忽略；轻量 reports 可选择性提交。 |
| `training/archive/` | 历史归档 | 旧 pipeline、旧评测集和旧 prompt 实验，本地保留。 |
| `training/post_training_artifacts/` | 旧版产物镜像 | 早期英文路径版归档；新主入口已迁到 `training/docs/后训练产物/`。 |
| `training/private-docs/` | 私有草稿 | 本地保留，不公开。 |
| `training/prompts/` | 数据生成 prompt | 后训练数据生成使用。 |
| `training/.hf_cache/`、`training/data/cache/` | 缓存 | 可再生成，缺空间时优先清。 |

后训练完整资产地图见：`training/docs/后训练产物/本地资产索引.md`。

## Skills 目录

| 路径 | 状态 | 说明 |
| --- | --- | --- |
| `skills/trip-planner-eval-compare/` | 已跟踪 | 横评报告、指标解释和结果决策辅助 skill。 |
| `skills/trip-planner-sft-data-loop/` | 已跟踪 | SFT 数据生成、审计、导出和训练交接辅助 skill。 |
| `skills/trip-planner-model-eval/` | 本地忽略 | 启动 vLLM、checkpoint sweep、服务管理的本地工作流 skill；不作为公开项目资产。 |

## 本地环境和生成物

这些目录或文件可以出现在工作区，但不应该提交：

- `backend/.env`、`frontend/.env`
- `backend/.venv/`、`.venv-training-py311/`
- `frontend/node_modules/`、`frontend/.nodeenv*`、`frontend/dist/`
- `.uv-cache/`
- `training/outputs/` 下的模型权重、checkpoint、long logs、generations
- `training/data/llamafactory/generated/`
- `training/data/planner/dpo/`、`training/data/planner/bestofn/`、`training/data/planner/sft*`
- `training/private-docs/`
- `skills/trip-planner-model-eval/`

## 新增文件放哪里

| 你要新增的东西 | 应该放到 |
| --- | --- |
| 后端 Planner 规则、预算、票价、rerank | `backend/app/planner/` |
| 后端 API 路由 | `backend/app/api/routes/` |
| 后端外部服务封装 | `backend/app/services/` |
| 前端页面 | `frontend/src/views/` |
| 前端 API 调用 | `frontend/src/services/` |
| 前端类型 | `frontend/src/types/` |
| 训练配置 | `training/configs/<model_family>/` |
| 后训练数据生成/评测脚本 | `training/scripts/planner/` 或 `training/scripts/eval/` |
| 长期教程和公开说明 | `training/docs/教程/` |
| 实验记录卡和阶段归档 | `training/docs/后训练产物/` |
| 内部协议、指标、方案备忘 | `training/docs/内部文档/` |
| 轻量公开评测报告 | `training/outputs/eval/reports/<YYMMDD>_<slug>/` |
| 完整评测输出 | `training/outputs/eval/by_model/`，默认本地保留 |
| 大模型/adapter/checkpoint | `training/outputs/qwen25_7b/`，默认本地保留 |

## 提交前检查

1. `git status --short` 看有没有误入的本地环境、日志或大文件。
2. 确认真实 `.env`、API key、模型权重、checkpoint 没有被 staged。
3. Python 改动至少跑 `python3 -m py_compile`。
4. 文档改动检查相对链接。
5. 后训练数据或评测结论改路径时，同步更新 `training/README.md`、`training/STRUCTURE.md`、`training/docs/README.md` 和 `training/docs/后训练产物/本地资产索引.md`。
