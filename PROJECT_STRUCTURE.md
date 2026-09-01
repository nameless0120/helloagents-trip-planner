# 项目目录索引

这个文件只描述当前会出现在仓库中的代码、配置和文档。运行环境、模型权重、日志和生成数据按 `.gitignore` 处理。

## 顶层目录

| 路径 | 用途 |
| --- | --- |
| `backend/` | FastAPI 服务、PlannerContext、预算和外部工具封装 |
| `frontend/` | Vue 旅行助手界面 |
| `training/` | SFT、DPO、评测和训练入口 |
| `docs/` | 项目首页截图 |
| `skills/` | 项目工作流技能 |

## Training

```text
training/
├── configs/qwen25_7b/       # 当前通用训练配置
├── data/
│   ├── planner/eval/        # standard 冻结评测输入
│   ├── planner/eval_hard/   # hard 冻结评测输入
│   ├── planner/attraction_prices/
│   └── llamafactory/        # 数据集登记
├── docs/                    # 教程、协议、审计和指标
├── patches/                # LLaMA-Factory 补丁
└── scripts/
    ├── run_pipeline.py     # 后训练总入口
    ├── planner/             # SFT、审计、票价、评测输入、Best-of-N
    ├── eval/               # DPO 和通用评测
    ├── serving/            # Planner 模型服务
    ├── validation/         # 输出校验
    └── shared/              # 公共 helper
```

## 后训练开始位置

```text
training/scripts/run_pipeline.py
  -> training/scripts/planner/data/generate_sft_data.py
  -> 预算审计和可用性分类
  -> training/data/llamafactory/generated/
  -> LLaMA-Factory
```

读者版命令见 [README.md](README.md) 的“后训练快速开始”，完整步骤见 [后训练实战教程](training/docs/教程/旅行助手后训练实战教程.md)。

## 不进入仓库的本地产物

- `.env`、虚拟环境、Node 依赖和缓存。
- `training/data/planner` 下的 SFT、Best-of-N、DPO run。
- `training/data/llamafactory/generated/`。
- `training/outputs/` 下的模型、checkpoint、生成结果和日志。
