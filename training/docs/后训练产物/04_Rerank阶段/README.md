# 04 Rerank阶段

这个目录归档“生成多个候选，再用规则或打分器选择最终答案”的实验。现在分成两条线：SFT 阶段的 rerank 主要验证多温度候选是否能补单生成短板；DPO 阶段的 rerank 则用于在 DPO 收尾模型之间选择最终展示版本。

## 当前批次

| 批次 | 读者视角 |
| --- | --- |
| [01_SFT多温度候选Rerank/](01_SFT多温度候选Rerank/) | 对 SFT checkpoint 做多温度候选生成和规则 rerank，比较 ckpt104、final1200、old600final 等版本。先看 `报告/实验记录卡.md`。 |
| [02_DPO多候选Rerank最终选择/](02_DPO多候选Rerank最终选择/) | 对 DPO 收尾后的 ckpt64 和 ckpt138 做多温度候选 rerank，确定最终展示版本。先看 `报告/实验记录卡.md`。 |

## 关键结论

- SFT rerank 证明了多候选 + 规则选择能显著补足单生成波动。
- DPO rerank 最终选择 `ckpt64_rerank_n4`：500 条 planner soft `80.6%`，hard split planner soft `77.0%`。
