# Budget Revision Eval: budget_revision_patch_base_A_C_300

- records: `training/data/v3/eval_harder_prompt_ablation_20260505/A_C/records.jsonl`
- first_generations: `training/outputs/eval/prompt_ablation_20260505/base_qwen25_7b_prompt_ablation_20260505_A_C/generations.jsonl`
- output_file: `training/outputs/eval/budget_revision_patch_base_A_C_300/budget_revision_generations.postprocessed.jsonl`
- raw_output_file: `training/outputs/eval/budget_revision_patch_base_A_C_300/budget_revision_generations.raw.jsonl`
- base_url: `http://127.0.0.1:4396/v1`
- workers: 10
- revision_mode: `patch`
- total compared: 300
- revision_attempted: 226
- skipped_budget_already_fit: 72
- failed_or_unparseable_after_postprocess: 3

## Before vs After

| Metric | Before | After | Delta |
| --- | ---: | ---: | ---: |
| `planner_draft_hard_pass` | 134/300 = 44.67% | 153/300 = 51.00% | +6.33% |
| `budget_selection_ok` | 72/300 = 24.00% | 83/300 = 27.67% | +3.67% |
| `draft_budget_fit_pass` | 28/300 = 9.33% | 35/300 = 11.67% | +2.34% |
| `recomputed_budget_hard_ok` | 115/300 = 38.33% | 120/300 = 40.00% | +1.67% |
| `meal_grounding_ok` | 157/300 = 52.33% | 159/300 = 53.00% | +0.67% |
| `attraction_grounding_ok` | 296/300 = 98.67% | 295/300 = 98.33% | -0.34% |
| `attraction_diversity_ok` | 265/300 = 88.33% | 234/300 = 78.00% | -10.33% |
| `meal_diversity_ok` | 197/300 = 65.67% | 191/300 = 63.67% | -2.00% |
