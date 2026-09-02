# Planner SFT 全量数据审计 20260508

## 口径

- active raw：当前可考虑进入 SFT 的真实生成 records，排除 clean/merged/llamafactory 等派生文件。
- archive：早期实验 smoke，单独统计，默认隔离不进训练。
- 本审计只读本地文件，不调用外部模型。

## Active Raw 总览

- 样本数：1615
- 重复 record_id 组：0

| 类别 | 含义 | 数量 | 建议 |
|---|---|---:|---|
| usable_budget_clean | 预算主集可用 | 24.5% (395) | 直接可进预算主训练池，合并前按 record_id 去重。 |
| usable_budget_candidate_tight | 预算可用但候选偏紧 | 4.6% (74) | 可用于预算遵循/保守规划，不用于训练“用足预算”。 |
| repair_request_rebudget | 需重标请求预算 | 49.0% (791) | 保留 teacher/上下文，重标请求预算档位、amount 和 free_text 后再用。 |
| repair_teacher_regen | 需重生成 teacher | 7.4% (119) | 保留请求和上下文，重生成 teacher。 |
| nonbudget_only | 仅适合非预算 SFT | 5.8% (94) | 只进入非预算 schema/grounding 池。 |
| drop_or_full_regen | 预算训练淘汰或整条重做 | 8.8% (142) | 隔离；需要时整条重做。 |

## 按 Active 批次

| 批次 | n | clean | candidate_tight | rebudget | teacher_regen | nonbudget | drop |
|---|---:|---:|---:|---:|---:|---:|---:|
| budget_supplement_bg503_20260507_overnight | 503 | 34.6% (174) | 0.0% (0) | 65.4% (329) | 0.0% (0) | 0.0% (0) | 0.0% (0) |
| budget_supplement_smoke20_20260507_afternoon | 20 | 25.0% (5) | 0.0% (0) | 75.0% (15) | 0.0% (0) | 0.0% (0) | 0.0% (0) |
| budget_supplement_smoke22_20260507_noon | 22 | 22.7% (5) | 13.6% (3) | 31.8% (7) | 9.1% (2) | 0.0% (0) | 22.7% (5) |
| legacy_controlled_1000_20260506 | 1000 | 15.2% (152) | 6.7% (67) | 44.0% (440) | 11.6% (116) | 8.8% (88) | 13.7% (137) |
| realistic_partial41_w20_20260508 | 41 | 85.4% (35) | 9.8% (4) | 0.0% (0) | 0.0% (0) | 4.9% (2) | 0.0% (0) |
| realistic_smoke23_w20_20260507 | 23 | 87.0% (20) | 0.0% (0) | 0.0% (0) | 4.3% (1) | 8.7% (2) | 0.0% (0) |
| realistic_smoke6_20260507_low_concurrency | 6 | 66.7% (4) | 0.0% (0) | 0.0% (0) | 0.0% (0) | 33.3% (2) | 0.0% (0) |

## Archive 总览

- archive 样本数：258
- 默认处理：全部隔离，不进入当前 SFT；如要复用，按 archive 批次另开修复。

## 输出文件

- active 分类：`training/outputs/eval/v3_sft_full_data_audit_20260508/active_record_classification.csv`
- archive 分类：`training/outputs/eval/v3_sft_full_data_audit_20260508/archive_record_classification.csv`
- summary：`training/outputs/eval/v3_sft_full_data_audit_20260508/summary.json`
- active id lists：`training/outputs/eval/v3_sft_full_data_audit_20260508/active_id_lists`
