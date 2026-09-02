# Budget Revision Eval: budget_revision_patch_sft_cp2_A_C_300

- records: `training/data/v3/eval_harder_prompt_ablation_20260505/A_C/records.jsonl`
- first_generations: `training/outputs/eval/sft_qwen25_7b_v3_1000_cp2_v1_A_C_w8/generations.jsonl`
- output_file: `training/outputs/eval/budget_revision_patch_sft_cp2_A_C_300/budget_revision_generations.postprocessed.jsonl`
- raw_output_file: `training/outputs/eval/budget_revision_patch_sft_cp2_A_C_300/budget_revision_generations.raw.jsonl`
- base_url: `http://127.0.0.1:4397/v1`
- workers: 10
- revision_mode: `patch`
- total compared: 300
- revision_attempted: 213
- skipped_budget_already_fit: 85
- failed_or_unparseable_after_postprocess: 8

## Before vs After

| Metric | Before | After | Delta |
| --- | ---: | ---: | ---: |
| `planner_draft_hard_pass` | 189/300 = 63.00% | 188/300 = 62.67% | -0.33% |
| `budget_selection_ok` | 85/300 = 28.33% | 97/300 = 32.33% | +4.00% |
| `draft_budget_fit_pass` | 60/300 = 20.00% | 69/300 = 23.00% | +3.00% |
| `recomputed_budget_hard_ok` | 125/300 = 41.67% | 126/300 = 42.00% | +0.33% |
| `meal_grounding_ok` | 209/300 = 69.67% | 204/300 = 68.00% | -1.67% |
| `attraction_grounding_ok` | 280/300 = 93.33% | 278/300 = 92.67% | -0.66% |
| `attraction_diversity_ok` | 209/300 = 69.67% | 161/300 = 53.67% | -16.00% |
| `meal_diversity_ok` | 223/300 = 74.33% | 207/300 = 69.00% | -5.33% |
