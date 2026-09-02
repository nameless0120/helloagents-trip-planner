# Planner 新预算评估集重建与 SFT 预算审计

更新时间：2026-05-07

> 2026-05-08 状态更新：这份文档是新预算口径切换时的历史审计记录。文中提到的旧 SFT 已经全量归档，后续不再按 clean 子集修补旧数据，而是按 realbudget-only 口径重新生成和审计。

## 本轮动作

- 按 `Planner典型旅游预算报告.md` 的新口径调整 eval 预算构造。
- 用低 QPS 方式重建两套评估集：
  - standard: `training/data/planner/eval/records.jsonl`
  - hard: `training/data/planner/eval_hard/records.jsonl`
- 旧评估集已归档到：
  - `training/data/planner/archive/legacy_eval_20260507/`
- 离线审计已有 SFT records 的预算是否贴合新预算表：
  - `training/outputs/eval/audits/260507_v3_sft_budget_fit_audit/sft_budget_fit_audit.md`

构建时使用：

```bash
AMAP_QPS_LIMIT=2.5
workers=2
```

高德客户端内部还有进程级锁，实际请求节奏低于 3 QPS。构建日志里绝大多数为缓存命中，本轮没有高德 QPS 错误。

## 预算口径改动

旧 eval 预算构造把多人预算压缩成：

```text
party_units = 1 + log2(party_total)
daily_total = per_person_day * party_units * travel_days
```

新 eval 预算构造改为：

```text
rooms = ceil(party_total / 2)
lodging_total = hotel_room_night * lodging_nights * rooms
person_total = per_person_day * party_total * travel_days
shared_transport_total = shared_transport_day * travel_days
budget_amount = round_100((lodging_total + person_total + shared_transport_total) * city_factor)
```

含义：

- 餐饮、门票、体验按真实人数线性增长。
- 住宿按两人一间计算。
- 打车/自驾等市内交通按队伍共享估算。
- 不再用 `group_discount` 压低整段非住宿预算。

同步调整了 `budget_fit_policy` 目标比例：

| budget_level | 新目标使用比例 |
|---|---:|
| limited | 72%-100% |
| standard | 60%-105% |
| comfortable | 70%-110% |
| premium | 75%-112% |
| luxury | 75%-118% |

## 新评估集构建结果

| 数据集 | 样本数 | 失败数 | records | 摘要 |
|---|---:|---:|---|---|
| standard realistic budget | 200 | 0 | `training/data/planner/eval/records.jsonl` | `training/data/planner/eval/评估集摘要.md` |
| hard realistic budget | 300 | 0 | `training/data/planner/eval_hard/records.jsonl` | `training/data/planner/eval_hard/评估集摘要.md` |

数据集说明：

- standard: `training/data/planner/eval/数据集说明.md`
- hard: `training/data/planner/eval_hard/数据集说明.md`

## 新旧预算分布对比

### standard 集

| level | 新 n | 新 p50 | 旧 p50 | 新 high_ratio p50 | 新 food_avg | 新 food=0 |
|---|---:|---:|---:|---:|---:|---:|
| limited | 53 | 3500 | 2900 | 1.34 | 29.4 | 0 |
| standard | 80 | 6600 | 5500 | 0.94 | 26.9 | 0 |
| comfortable | 45 | 9200 | 7800 | 1.21 | 35.3 | 0 |
| premium | 22 | 15400 | 11550 | 0.84 | 36.1 | 0 |

### hard 集

| level | 新 n | 新 p50 | 旧 p50 | 新 high_ratio p50 | 新 food_avg | 新 food=0 |
|---|---:|---:|---:|---:|---:|---:|
| limited | 30 | 5800 | 2800 | 1.52 | 25.0 | 0 |
| standard | 90 | 9550 | 4100 | 0.99 | 31.1 | 0 |
| comfortable | 150 | 10500 | 5200 | 1.37 | 35.3 | 0 |
| premium | 30 | 13100 | 7250 | 0.89 | 35.2 | 0 |

## 候选供给变化

旧 hard 的餐饮候选严重不足：

| 数据集 | food_pois avg | food=0 |
|---|---:|---:|
| old hard | limited 12.0 / standard 3.4 / comfortable 4.5 / premium 6.2 | standard 45, comfortable 13 |
| new hard | limited 25.0 / standard 31.1 / comfortable 35.3 / premium 35.2 | 0 |

新 hard 的 `food_pois` 已恢复到正常候选供给，之前餐饮 grounding 被打穿的问题不应再由数据侧造成。

## SFT 预算贴合审计

审计对象：

```text
training/data/planner/sft/records.jsonl
```

该路径是历史生成时的原始位置；2026-05-08 后旧 SFT 已归档，不再作为训练入口。

输出：

```text
training/outputs/eval/audits/260507_v3_sft_budget_fit_audit/sft_budget_fit_audit.md
training/outputs/eval/audits/260507_v3_sft_budget_fit_audit/summary.json
training/outputs/eval/audits/260507_v3_sft_budget_fit_audit/audit_rows.jsonl
```

总览：

| 项 | 结果 |
|---|---:|
| 样本数 | 1119 |
| 请求预算落在新分档范围 | 36.1% (404/1119) |
| teacher budget 落在请求目标区间 | 68.9% (771/1119) |
| 候选池高配可达请求预算 | 64.2% (718/1119) |
| food_pois=0 | 0 |

按档位：

| level | n | amount p50 | teacher p50 | 请求预算OK | teacher预算OK | 候选可达p50 |
|---|---:|---:|---:|---:|---:|---:|
| limited | 265 | 3200 | 2832 | 29.8% | 91.3% | 1.63 |
| standard | 455 | 5500 | 3932 | 34.7% | 73.0% | 1.12 |
| comfortable | 275 | 8800 | 6402 | 46.6% | 45.1% | 0.89 |
| premium | 113 | 12800 | 10016 | 31.9% | 62.8% | 1.14 |
| luxury | 11 | 18600 | 7673 | 27.3% | 18.2% | 0.39 |

## 结论

1. 新 standard/hard 已经按更现实的预算口径重建完成，且没有 API/QPS 失败。
2. 新 hard 的预算档位语义恢复正常：premium p50 从 7250 提到 13100，comfortable p50 从 5200 提到 10500，standard p50 从 4100 提到 9550。
3. 新 hard 的餐饮候选供给正常，`food_pois=0` 问题已消失。
4. 现有 SFT 数据按新预算表看，用户请求预算只有 36.1% 落在推荐分档范围，说明旧 SFT 请求分布和新预算表不完全对齐。
5. SFT teacher 预算只有 68.9% 落在自身目标区间，comfortable/luxury 最弱；这成为后续放弃修补旧 SFT、改走 realbudget-only 重建的主要证据之一。

## 下一步建议

- 旧建议曾是切出预算贴合子集或生成 budget supplement；2026-05-08 复审后已升级为：旧 SFT 全量归档，不再混用 clean 子集。
- 后续新 SFT 从 realbudget pipeline 重建，按 smoke 20 -> 100 -> 1000 的节奏逐轮审计。
- 新评估集可以作为下一轮 base/sftv1/legacy_a/legacy_b 横评输入。
- 若要把新评估集升级为主路径，建议先人工抽查每个档位 5-10 条 prompt，确认预算自由文本和候选池质量符合预期。
