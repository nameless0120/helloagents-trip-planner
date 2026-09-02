# 01 SFT 多温度候选 Rerank

这一批记录 SFT 阶段的多温度候选 rerank：先让同一个模型用不同温度生成多个候选，再用规则评测或 pipeline 选择更可靠的一条。

- `报告/实验记录卡.md`：这一批 rerank 的目标、设置、关键结果和结论。
- `配置/`：候选生成、规则 rerank、规则评测、pipeline 和切片报告脚本口径。
- `报告/`：ckpt104、final1200、old600final 在 standard / hard split 上的 rerank 结果。

这一步的价值是证明：即使单生成有波动，多候选搜索空间里经常已经包含更好的计划，rerank 可以把它捞出来。
