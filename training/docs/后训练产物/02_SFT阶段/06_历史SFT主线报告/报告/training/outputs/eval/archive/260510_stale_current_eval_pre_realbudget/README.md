# 260510 Stale Current Eval Archive

本目录归档旧的 `260507_current_standard_w10` / `260507_current_hard_w10` 评估结果。

归档原因：

- 这些目录名字里带 `current`，但实际生成样本 ID 是旧口径：
  - 标准集：`v3_standard200_eval_*`
  - 困难集：`v3_harder_eval_*`
- 当前 260509 main clean 评估使用的是 realbudget 口径：
  - 标准集：`v3_standard200_realbudget_eval_*`
  - 困难集：`v3_hard_realbudget_eval_*`
- 旧 `current_*` 和当前 `realbudget_*` 不是同一批样本，不能直接做同口径对比。

保留原因：

- 这些结果仍可用于追溯早期 prompt / SFT 版本在旧评估集上的表现。
- 但默认横评、自动扫表和新文档不应再引用这些目录。

当前同口径历史基线应使用：

- `training/outputs/eval/by_model/*/260507_realbudget_standard_w10/`
- `training/outputs/eval/by_model/*/260507_realbudget_hard_w10/`

当前主对比文档：

- `training/outputs/eval/comparisons/260510_v3_260509_main_clean_vs_previous_current_w10_comparison/v3_260509_main_clean_vs_previous_current_w10_comparison.md`
