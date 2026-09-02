# V3 Prompt 预算语义关系消融小结

本轮目标：不再强行要求模型先解决所有预算分项精确加总，而是观察 prompt 能否让 Qwen2.5-7B 先学会三类业务关系：

- 天数 -> 住宿晚数：`hotel.estimated_cost` 应覆盖实际入住晚数。
- 人数 -> 景点门票：`attraction.ticket_price` 是单人票价，景点预算应体现 `party.total`。
- 人数/档位 -> 餐饮尺度：`meal.estimated_cost` 是整组人单餐费用，不应明显写成单人价。

## 新增评测指标

- `hotel_budget_relation_ok`：酒店预算大致覆盖所有非 null `day.hotel.estimated_cost`。
- `attraction_budget_party_relation_ok`：景点预算大致体现单人门票 × 同行人数。
- `meal_cost_scale_ok`：午餐/晚餐费用不明显低于同行人数和预算档位对应的整组费用。
- `budget_relationship_ok`：上面三项同时通过。
- `sft_budget_semantic_hard_pass`：用预算语义关系替代精确预算分项一致性的 SFT 硬约束口径。

## smoke20 对比

同一批 hard compact eval records，均为 `limit=20`，本地 Qwen2.5-7B vLLM，`temperature=0.2`。

| 版本 | schema | 预算语义通过 | 酒店晚数关系 | 景点人数关系 | 餐饮尺度 | 预算总分项一致 | 餐饮多样性 | SFT语义硬约束 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| baseline | 95.00% | 10.53% | 78.95% | 26.32% | 52.63% | 63.16% | 0.00% | 5.26% |
| budget_relation_lite | 100.00% | 5.00% | 85.00% | 45.00% | 30.00% | 50.00% | 15.00% | 5.00% |
| budget_relation_priority | 100.00% | 5.00% | 85.00% | 30.00% | 30.00% | 55.00% | 25.00% | 5.00% |
| budget_relation_self_check | 100.00% | 5.00% | 90.00% | 30.00% | 35.00% | 65.00% | 25.00% | 5.00% |

## 观察

1. `budget_relation_lite` 对“景点门票乘人数”有改善：26.32% -> 45.00%，但餐饮尺度明显变差。
2. `budget_relation_self_check` 对 schema、酒店晚数关系和预算总分项一致性稍有帮助，但没有解决景点人数和餐饮尺度。
3. 三版 prompt 的综合 `budget_relationship_ok` 都低于 baseline，说明追加规则容易让模型在不同约束间互相挤压。
4. `sft_budget_semantic_hard_pass` 基本不动，说明这不是再加几句 prompt 就能解决的问题。

## 结论

不建议继续把时间花在预算关系 prompt 微调上。当前最稳定的路径是：

1. prompt 保留当前线上主规则，最多吸收少量“预算语义关系”表述。
2. SFT 数据生成阶段显式构造预算关系正确的样本，让模型学会住宿晚数、景点人数、餐饮整组费用这些业务口径。
3. 预算精确加总可以后续用工程后处理或数据清洗统一重算，不应该作为 prompt-only 的目标。
