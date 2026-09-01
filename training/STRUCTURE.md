# Training Asset Structure

更新时间：2026-08-31

这个文件定义 `training/` 下数据、脚本、文档和评测产物的边界。后续整理文件时先遵守这里的生命周期规则，再决定是否移动或归档。

## 总原则

- `docs/` 放长期有效的教程、协议、指标、审计口径和阶段结论；面向读者的内容在 `docs/教程/`，支撑材料在 `docs/内部文档/`。
- `data/` 放可复用输入、冻结评估集、训练数据入口和轻量 manifest。
- `scripts/` 放当前仍可能运行的入口；旧实验脚本只保留在本地 legacy/archive 中。
- `outputs/eval/reports/` 放可公开提交的轻量报告包；完整 generations、日志、rule eval 明细和模型输出留在本地忽略目录。

## 目录边界

| 路径 | 状态 | 说明 |
| --- | --- | --- |
| `configs/qwen25_7b/` | 主线配置 | 保留可复现训练配置；`.serve_*.yaml` 和旧归档配置由 `.gitignore` 排除。 |
| `data/planner/eval/` | 冻结输入 | standard 评估集，公开保留 `records.jsonl`、`requests.jsonl`、摘要和重建说明。 |
| `data/planner/eval_hard/` | 冻结输入 | hard 评估集。旧名 `eval_harder` 不再作为主入口。 |
| `data/planner/attraction_prices/` | 票价资产 | `reports/` 放审核说明，`snapshots/` 放小体积票价表快照，`generated/` 放候选/估价 JSONL 和日志。 |
| `data/planner/sft*/` | 本地生成 | SFT run、realbudget run、best-of-n 数据默认按明确 run 目录生成并忽略，不能混写到旧目录。 |
| `data/planner/dpo/` | 本地生成 | prompt/candidate/pair/judge 数据默认本地保留；公开文档只描述口径。 |
| `data/llamafactory/` | 训练入口 | `dataset_info.json` 和 `manifests/` 可提交；大体积 train/val JSON/YAML 放 `generated/` 并默认忽略。 |
| `patches/` | 第三方依赖补丁 | 记录 LLaMA-Factory 的固定基础 commit 和本项目需要的源码改动。 |
| `docs/` | 长期文档 | 需要有索引；教程放 `教程/`，协议、指标、审计和实验记录放 `内部文档/`；旧阶段结论如果不再代表主线，应在索引中标注历史/参考。 |
| `scripts/shared/` | 公共 helper | JSONL、路径、环境变量和 LLM client 等复用代码。 |
| `scripts/run_pipeline.py` | 后训练总入口 | 按阶段调度当前 SFT、票价候选、Best-of-N、DPO、评测和训练脚本。 |
| `scripts/serving/` | 服务入口 | 本地 Planner 模型服务和服务管理脚本。 |
| `scripts/validation/` | 校验入口 | SFT/DPO/Eval 输出 schema 与格式校验。 |
| `scripts/planner/` | 当前主线 | 按 `data/`、`eval/`、`audit/`、`pricing/`、`bestofn/`、`training/` 分组。 |
| `scripts/eval/` | 兼容与评测 | 旧 SFT 生成/清洗/切分、评测和通用 DPO helper；不作为当前 SFT 主线入口。 |
| `scripts/archive/` | legacy | 只作为迁移参考或本地 DPO helper 来源，不作为当前公开主线。 |
| `outputs/eval/reports/` | 公开报告 | 只放 Markdown 和小体积指标 JSON。 |
| `docs/后训练产物/本地资产索引.md` | 本地地图 | 记录本机模型、数据、评测输出、缓存和归档的归属；不等于公开提交清单。 |
| `outputs/eval/by_model/`、`comparisons/`、`audits/`、`logs/` | 本地生成 | 完整评测产物默认忽略；需要公开时整理成 `reports/<YYMMDD>_<slug>/`。 |

## 新增资产命名

- 新 run 目录用 `YYMMDD_<slug>`，例如 `260512_bestofn_replay_extended_w10`。
- 新 SFT/DPO 数据必须写入明确 run 目录，并带 manifest 或摘要；不要复用旧 `data/planner/sft/` 作为长期混合池。
- 评测输入只使用 `data/planner/eval/` 和 `data/planner/eval_hard/`。如果后端检索逻辑变了，先 rebuild context，保留同一批 request 和 record id。
- 大体积产物不直接加入公开仓库。公开结论先压缩到 `outputs/eval/reports/`。

## 文档维护规则

- 根 README 只链接当前入口，不链接本地 ignored 产物。
- `training/README.md` 说明当前主线状态和常用命令。
- `training/docs/README.md` 维护长期文档索引和文档状态。
- 改数据、脚本或报告路径时，同步更新这三个入口和 `.gitignore`。
- 旧名保留时要写明“历史名/本地旧产物”，不要让新人误以为仍是主线。

## 后续整理顺序

1. 修文档入口和失效链接。
2. 给当前数据、脚本、报告建立索引。
3. 只移动不会影响命令的归档/私有材料。
4. 对脚本路径做批量迁移前，先用 `rg` 找引用，再分批改命令和 README。
