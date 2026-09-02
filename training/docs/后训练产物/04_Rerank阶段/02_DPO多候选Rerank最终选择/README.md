# 02 DPO 多候选 Rerank 最终选择

这一批记录 DPO 收尾后的多温度候选 rerank：比较 `260521 ckpt64` 和 `260519 ckpt138` 在同一批评测记录上的候选质量。结论是：单生成看 ckpt138，最终展示看 ckpt64 rerank n4。

- 实验记录卡：`报告/实验记录卡.md`
- 评估记录：`报告/评估记录.md`
- 输出目录：`training/outputs/eval/by_model/dpo_260521_ckpt64_260519_ckpt138_rerank_n4_gpu0_2_w8/`
- 对比报告：`training/outputs/eval/by_model/dpo_260521_ckpt64_260519_ckpt138_rerank_n4_gpu0_2_w8/ckpt64_vs_ckpt138_rerank_n4_report/ckpt64_vs_ckpt138_rerank_n4_full_report.md`
