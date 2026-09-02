# V3 Prompt 酒店房间数与餐饮人均价消融小结

本轮调整评测口径：

- `hotel.estimated_cost` 解释为“单间每晚房价”。
- 酒店总价按“两人一间”估算：`rooms = ceil(party.total / 2)`，`total_hotels = sum(non-null day.hotel.estimated_cost) * rooms`。
- `meal.estimated_cost` 解释为“人均单餐费用”。
- 餐饮总价：`total_meals = sum(day.meals[].estimated_cost) * party.total`。
- 景点仍按成人单人门票：`total_attractions = sum(ticket_price) * party.total`。

## baseline 新口径重算

正式 300 条 baseline：`base_qwen25_7b_v3_ctx_hard_compact_w10_room_person_eval`

| 指标 | 结果 |
| --- | ---: |
| schema | 98.67% |
| budget_relationship_ok | 6.76% |
| hotel_budget_relation_ok | 39.53% |
| attraction_budget_party_relation_ok | 28.04% |
| meal_cost_scale_ok | 87.16% |
| budget_arithmetic_consistent | 69.59% |
| meal_budget_consistent | 0.00% |
| sft_budget_semantic_hard_pass | 4.39% |

观察：餐饮人均价口径更符合当前模型输出，`meal_cost_scale_ok` 明显变好；主要短板转为酒店房间数、景点人数和餐饮总预算分项没有乘人数。

## smoke20 prompt 消融

同一批 hard compact eval records，均为 `limit=20`，本地 Qwen2.5-7B vLLM，`temperature=0.2`。

| 版本 | schema | 预算语义通过 | 酒店两人一间 | 景点人数 | 餐饮人均尺度 | 预算总分项一致 | 餐饮多样性 | SFT语义硬约束 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| baseline | 95.00% | 5.26% | 36.84% | 26.32% | 94.74% | 63.16% | 0.00% | 5.26% |
| room_person_price_lite | 95.00% | 10.53% | 42.11% | 36.84% | 84.21% | 84.21% | 15.79% | 5.26% |
| room_person_price_full | 100.00% | 5.00% | 45.00% | 30.00% | 80.00% | 70.00% | 20.00% | 5.00% |
| room_person_price_self_check | 100.00% | 20.00% | 50.00% | 30.00% | 85.00% | 60.00% | 5.00% | 15.00% |

## 结论

1. 新口径是合理的：餐饮按人均价后，当前模型的餐饮尺度问题明显缓解。
2. Prompt 有小幅收益，但不稳定：
   - `self_check` 综合预算语义最好，`budget_relationship_ok` 到 20%。
   - `lite` 对景点人数和预算加总有帮助，但餐饮尺度下降。
   - `full` schema 稳，但综合收益一般。
3. 当前主要硬伤变成：
   - 酒店预算没有按房间数乘。
   - 景点预算没有稳定按人数乘。
   - `budget.total_meals` 仍没有按人均餐费乘人数。

## 建议

SFT 训练数据应采用这个新业务口径：

- 酒店：单间每晚价，预算按 `ceil(party.total / 2)` 间房计算。
- 餐饮：人均单餐价，预算按人数计算。
- 景点：成人单人票，预算按人数计算。

Prompt 可考虑吸收 `room_person_price_self_check` 中的简短自检规则，但不要指望 prompt-only 解决预算分项。
