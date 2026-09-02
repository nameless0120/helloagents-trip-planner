# V3 SFT CP2 Base vs SFT 对比看板

日期：2026-05-06

## 评测设置

- Eval 集：`training/data/v3/eval_harder_prompt_ablation_20260505/A_C/records.jsonl`
- 样本数：300
- Base 生成：`training/outputs/eval/prompt_ablation_20260505/base_qwen25_7b_prompt_ablation_20260505_A_C/generations.jsonl`
- SFT 生成：`training/outputs/eval/sft_qwen25_7b_v3_1000_cp2_v1_A_C_w8/generations.jsonl`
- 对比方式：只重算 rule eval，不重新调用模型。

## 一句话结论

如果仍把预算精确加和放进 hard pass，Base 和 SFT 都是 0。

把预算加和从当前 SFT 主目标里拿掉后，SFT CP2 的 hard pass 从 Base 的
48.66% 提升到 70.81%，说明这轮 SFT 确实学到了协议、grounding 和餐饮约束。

## 总体指标

| 指标 | Base A_C | SFT CP2 | 变化 |
| --- | ---: | ---: | ---: |
| API 调用成功 | 300/300 | 300/300 | 0 |
| `json_extract_ok` | 100.00% | 100.00% | 0.00pp |
| `schema_ok` | 99.33% | 99.33% | 0.00pp |
| strict `sft_hard_pass` | 0.00% | 0.00% | 0.00pp |
| no-budget-sum `sft_hard_pass` | 48.66% | 70.81% | +22.15pp |
| `dpo_soft_pass` under no-budget-sum | 6.04% | 21.48% | +15.44pp |
| `legacy_hard_pass` | 6.71% | 20.13% | +13.42pp |
| 平均延迟 | 61.35s | 40.71s | -20.64s |

## SFT 主要收益

| 指标 | Base A_C | SFT CP2 | 变化 | 解释 |
| --- | ---: | ---: | ---: | --- |
| `accommodation_type_ok` | 82.89% | 100.00% | +17.11pp | 住宿类型固定规则学得很明显 |
| `hotel_grounding_ok` | 98.66% | 100.00% | +1.34pp | 酒店候选命中更稳 |
| `meal_specific_ok` | 95.97% | 97.99% | +2.02pp | 餐饮占位词减少 |
| `meal_valid_semantics_ok` | 57.38% | 77.52% | +20.14pp | 泛化餐厅/非法餐名明显减少 |
| `meal_grounding_ok` | 52.68% | 70.13% | +17.45pp | 餐饮命中 food_pois 明显提升 |
| `meal_diversity_ok` | 66.11% | 74.83% | +8.72pp | 餐饮重复问题缓解 |
| `budget_arithmetic_consistent` | 58.72% | 74.16% | +15.44pp | 预算总分项加和也有改善，但仍只当诊断项 |
| `hotel_budget_covers_nights` | 40.27% | 53.69% | +13.42pp | 酒店晚数/房间数关系有改善 |
| `budget_preference_aligned` | 34.56% | 57.05% | +22.49pp | 预算档位贴合更自然 |

## SFT 明显回退

| 指标 | Base A_C | SFT CP2 | 变化 | 风险 |
| --- | ---: | ---: | ---: | --- |
| `attraction_count_ok` | 100.00% | 97.99% | -2.01pp | 少量样本景点数超标 |
| `attraction_grounding_ok` | 99.33% | 93.96% | -5.37pp | 个别景点变成泛化/非候选 |
| `attraction_diversity_ok` | 88.93% | 70.13% | -18.80pp | 景点重复明显变多 |
| `budget_user_constraint_ok` | 82.21% | 77.18% | -5.03pp | 模型上报 budget 有更多 hard budget 超支 |
| `weather_match` | 99.66% | 98.99% | -0.67pp | 小幅天气字段偏差 |

## 为什么 strict 还是 0

严格口径把这些预算账本指标放进一票否决：

- `budget.total = total_attractions + total_hotels + total_meals + total_transportation`
- `total_attractions = sum(ticket_price) * party.total`
- `total_meals = sum(meal.estimated_cost) * party.total`
- `total_hotels = room_price * lodging_nights * ceil(party.total / 2)`
- hard budget 不超用户预算

这类跨字段乘法和加和仍然不是 7B 在长 JSON 里稳定能做好的事情。
所以当前保留 `sft_strict_hard_pass` 观察模型原生能力，但不把它作为 SFT 主验收。

## SFT 当前主要非预算失败

从 SFT CP2 no-budget-sum 报告看，剔除预算账本之后仍需要关注：

| 失败类型 | 数量 | 说明 |
| --- | ---: | --- |
| `attraction_repeat_too_many` | 89 | 景点重复是最大非预算问题 |
| `meal_invalid_name` | 67 | 餐饮仍会出现非候选/语义不合法名称 |
| `meal_repeat_too_many` | 65 | 餐厅复用仍偏多 |
| `meal_same_day_lunch_dinner_repeat` | 34 | 同一天午晚餐仍有重复 |
| `meal_grounding_miss` | 22 | 餐饮 grounding 仍不够稳 |
| `too_many_attractions` | 6 | 少量每天景点超过 3 个 |
| `meal_placeholder` | 6 | 少量餐饮占位词残留 |
| `schema` | 2 | 两条 schema 失败，主要是 POI 类型混淆/字段缺失 |

## 判断

这版 SFT CP2 有训练价值，不是“白跑”：

- 它没有提升预算精确乘法，这是预期内的模型能力边界。
- 它显著提升了 SFT 真正该学的协议项：住宿类型、餐饮语义、餐饮 grounding、餐饮多样性、酒店 grounding。
- 它也带来新的副作用：景点重复和景点 grounding 回退，需要单独修。

## 下一步建议

1. 当前主报告看 `sft_no_budget_sum_hard_pass`，严格账本看 `sft_strict_hard_pass` 诊断即可。
2. 预算最终走工程重算和超预算 repair，不再继续把精确 budget 乘法压给 SFT。
3. 下一轮数据/规则修正优先补：
   - 景点重复；
   - 景点 grounding；
   - 餐饮 grounding；
   - 餐饮同日重复；
   - POI 类型混淆。
