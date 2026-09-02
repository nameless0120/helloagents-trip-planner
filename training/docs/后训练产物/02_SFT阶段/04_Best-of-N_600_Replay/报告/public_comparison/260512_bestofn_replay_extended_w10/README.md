# 260512 Best-of-N Replay Extended Eval Report

This report package summarizes the 2026-05-12 Best-of-N replay LoRA checkpoints against the lr8e-5 valloss checkpoint, the previous usage700 mainline, the historical legacy_b reference, and the external Mimo reference.

Files:

- `中文结果摘要.md`: human-facing Chinese decision report.
- `bestofn_replay_extended_comparison.md`: metric tables and split-level notes for the current report package.
- `comparison_metrics.json`: compact machine-readable copy of the headline metrics.

Source comparison artifacts were generated under `training/outputs/eval/comparisons/260512_bestofn_replay_extended_vs_legacy_b_replay_mimo_w10/`, but only lightweight GitHub-facing reports are included here.

Large artifacts such as `generations.jsonl`, full `rule_eval_report.json`, service logs, model checkpoints, and regenerated train/val JSON files are intentionally not copied into this report package.
