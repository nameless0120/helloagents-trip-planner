# 指标和判断

主要指标：

| 指标 | 含义 |
| --- | --- |
| `sft_hard_pass` | 基础协议、schema、日期、天气、grounding 和硬约束 |
| `sft_strict_hard_pass` | 额外要求模型上报预算分项严格闭合 |
| `dpo_soft_pass` | 合法输出的多样性和预算偏好 |
| `planner_soft_pass` | 重算预算、餐饮尺度和多样性 |

判断顺序：

1. 确认两边 records、context 和规则版本一致。
2. 检查 API 失败、空输出和 `finish_reason=length`。
3. 先比较 `sft_hard_pass`，确认协议没有退化。
4. 再看预算重算、grounding、餐饮多样性和切片。
5. 如果规则指标接近，再使用 judge 判断合法方案的旅行质量。
