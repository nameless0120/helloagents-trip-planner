# V3 Harder Baseline

本目录冻结为当前 V3 harder eval 的 base baseline。

## 基本信息

- baseline_name: `base_qwen25_7b_v3_harder_budget_final_prompt_w8`
- model: `Qwen2.5-7B-Instruct`
- prompt: V3 prompt，加入“金额字段必须输出最终整数数字字面量，不能写算式/小数/解释，且不要复用提示词示例预算数字”的约束
- eval_set: `training/data/v3/eval_harder_prompt_budget_final_integer/records.jsonl`
- records: 300
- workers: 8
- temperature: 0.2
- post_validation: 未启用

## 核心指标

| 指标 | 结果 |
| --- | ---: |
| API 调用成功 | 300/300 |
| JSON 可解析 | 99.33% |
| Schema 通过 | 99.00% |
| hard_pass | 93.27% |
| budget_arithmetic_consistent | 93.94% |
| budget_preference_aligned | 97.64% |
| budget_within_user_budget | 100.00% |
| attraction_count_ok | 99.66% |
| hotel_budget_covers_nights | 100.00% |
| weather_match | 100.00% |

## 失败类型

```json
{
  "budget_arithmetic_inconsistent": 18,
  "budget_preference_mismatch": 7,
  "json_extract": 2,
  "schema": 1
}
```

## 结论

这版 baseline 已经足够作为后续 DPO 的参照点：结构、grounding、天气、酒店晚数和预算上限都比较稳。

剩余问题主要不是“能否按协议输出”，而是：

- 预算分项和 `budget.total` 偶发没有闭合。
- 预算花费和预算档位的贴合还可以更自然。
- 路线、节奏、偏好权衡和文本可用性仍有 DPO 优化空间。

因此后续优先进入 DPO；SFT 暂时不作为主线，除非新的评估集暴露出系统性 schema/协议硬错误。
