# V3 上下文消融评估汇总

本次使用 Qwen2.5-7B-Instruct 基模，本地 vLLM 4 卡服务，GPU 4/5/6/7，每组 300 条，`workers=10`，不调用强模型 judge。

## 关键结论

- 2026-05-05 重新收紧预算评测后，`sft_hard_pass` 在基模上几乎归零：旧口径允许预算总额和分项有 20% 误差，且没有检查景点/餐饮分项口径；新口径要求整数精确加总、景点门票乘同行人数、餐饮逐餐加总，并且 `strictness=hard` 不得超过结构化预算上限。之前八九十的 hardpass 明显偏乐观。
- `hard` 提示词族仍更适合守住格式、grounding、餐饮语义等确定性约束，但真实短板变成预算算术和酒店总价覆盖，而不只是餐饮重复。
- `balanced` 提示词族仍显著改善餐饮多样性，但严格预算、景点预算、餐饮预算和酒店总价问题没有自然消失；它更适合作为 DPO soft baseline，而不是 SFT 硬约束 baseline。
- 景点多样性已纳入 DPO softpass：只检查同一个景点名不要重复安排，不强制景点类别多样化。
- 上下文变短能明显降低延迟，但单纯 topK 不一定提升质量；如果优先做 SFT/格式/算术/grounding，`compact` 比 `topk` 更稳。
- `policy_first_topk` 在新口径下 softpass 数字最高，但它仍有候选语义损失；正式基线不建议只按 softpass 排名选 topK。

## 指标表

| 提示词族 | 上下文版本 | 平均prompt字符 | JSON | schema | SFT硬约束 | DPO软约束 | 预算算术 | 景点预算 | 餐饮预算 | hard预算 | 酒店总价 | 餐饮grounding | 餐饮语义 | 餐饮多样性 | 景点多样性 | 景点grounding | 平均延迟s |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| hard | full | 29616 | 100.00% | 98.00% | 0.00% | 0.00% | 60.54% | 15.65% | 0.00% | 82.31% | 84.69% | 97.28% | 98.30% | 8.16% | 87.41% | 98.98% | 64.95 |
| hard | compact | 22573 | 99.33% | 98.67% | 0.00% | 0.00% | 69.59% | 13.85% | 0.34% | 81.42% | 81.76% | 96.62% | 97.30% | 6.76% | 87.84% | 97.30% | 60.85 |
| hard | topk | 16177 | 99.33% | 99.33% | 0.00% | 0.00% | 64.09% | 10.40% | 0.00% | 83.89% | 84.56% | 94.97% | 95.97% | 7.05% | 84.90% | 95.97% | 53.35 |
| hard | policy_first_topk | 16976 | 99.33% | 99.00% | 0.00% | 0.00% | 64.65% | 11.45% | 1.01% | 83.84% | 83.50% | 95.96% | 95.96% | 14.48% | 83.50% | 97.64% | 54.19 |
| balanced | full | 28109 | 100.00% | 97.33% | 0.00% | 0.00% | 62.67% | 13.01% | 1.03% | 85.62% | 73.29% | 87.33% | 88.36% | 51.03% | 85.96% | 96.92% | 65.10 |
| balanced | compact | 21066 | 99.67% | 98.67% | 0.00% | 0.00% | 66.22% | 11.15% | 0.00% | 82.77% | 77.03% | 90.54% | 90.88% | 48.99% | 89.86% | 98.65% | 60.78 |
| balanced | topk | 14670 | 99.67% | 98.67% | 0.00% | 0.00% | 67.57% | 6.08% | 0.00% | 83.45% | 80.07% | 86.15% | 87.50% | 56.42% | 85.81% | 97.30% | 50.57 |
| balanced | policy_first_topk | 15469 | 99.67% | 99.00% | 0.34% | 0.00% | 65.99% | 8.42% | 0.34% | 88.89% | 85.19% | 85.52% | 86.87% | 51.18% | 86.87% | 95.62% | 50.71 |

## 推荐基线

- 硬约束基线：`base_qwen25_7b_v3_ctx_hard_compact_w10`。虽然 `topk` 的硬约束数值略高，但差距很小，且 topK 会截掉 30%-50% 候选；正式 baseline 更需要保留语义覆盖。
- 软约束基线：`base_qwen25_7b_v3_ctx_balanced_compact_w10`。`policy_first_topk` 的 softpass 数字最高，但候选截断会影响真实业务判断；如果要做简历报告，compact 更能说明“完整工具上下文下的模型能力”。
- 后续训练建议：不能直接跳过 SFT。至少要先通过 SFT 或更强的生成/校验链路解决预算口径：景点预算、餐饮预算、酒店总价、hard 预算不超。餐饮多样性、景点不重复、预算档位贴合再作为 DPO 偏好项，不建议混回 hardpass。

## 报告路径

- `base_qwen25_7b_v3_ctx_hard_full_w10`: `training/outputs/eval/base_qwen25_7b_v3_ctx_hard_full_w10/rule_eval_report.md`
- `base_qwen25_7b_v3_ctx_hard_compact_w10`: `training/outputs/eval/base_qwen25_7b_v3_ctx_hard_compact_w10/rule_eval_report.md`
- `base_qwen25_7b_v3_ctx_hard_topk_w10`: `training/outputs/eval/base_qwen25_7b_v3_ctx_hard_topk_w10/rule_eval_report.md`
- `base_qwen25_7b_v3_ctx_hard_policy_first_topk_w10`: `training/outputs/eval/base_qwen25_7b_v3_ctx_hard_policy_first_topk_w10/rule_eval_report.md`
- `base_qwen25_7b_v3_ctx_balanced_full_w10`: `training/outputs/eval/base_qwen25_7b_v3_ctx_balanced_full_w10/rule_eval_report.md`
- `base_qwen25_7b_v3_ctx_balanced_compact_w10`: `training/outputs/eval/base_qwen25_7b_v3_ctx_balanced_compact_w10/rule_eval_report.md`
- `base_qwen25_7b_v3_ctx_balanced_topk_w10`: `training/outputs/eval/base_qwen25_7b_v3_ctx_balanced_topk_w10/rule_eval_report.md`
- `base_qwen25_7b_v3_ctx_balanced_policy_first_topk_w10`: `training/outputs/eval/base_qwen25_7b_v3_ctx_balanced_policy_first_topk_w10/rule_eval_report.md`
