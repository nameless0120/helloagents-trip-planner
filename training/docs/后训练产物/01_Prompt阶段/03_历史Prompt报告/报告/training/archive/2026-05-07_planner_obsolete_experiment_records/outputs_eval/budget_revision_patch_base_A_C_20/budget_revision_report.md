# Budget Revision Eval: budget_revision_patch_base_A_C_20

- records: `training/data/v3/eval_harder_prompt_ablation_20260505/A_C/records.jsonl`
- first_generations: `training/outputs/eval/prompt_ablation_20260505/base_qwen25_7b_prompt_ablation_20260505_A_C/generations.jsonl`
- output_file: `training/outputs/eval/budget_revision_patch_base_A_C_20/budget_revision_generations.postprocessed.jsonl`
- raw_output_file: `training/outputs/eval/budget_revision_patch_base_A_C_20/budget_revision_generations.raw.jsonl`
- base_url: `http://127.0.0.1:4396/v1`
- workers: 10
- revision_mode: `patch`
- total compared: 20
- revision_attempted: 15
- skipped_budget_already_fit: 5
- failed_or_unparseable_after_postprocess: 0

## Before vs After

| Metric | Before | After | Delta |
| --- | ---: | ---: | ---: |
| `planner_draft_hard_pass` | 10/20 = 50.00% | 10/20 = 50.00% | +0.00% |
| `budget_selection_ok` | 5/20 = 25.00% | 6/20 = 30.00% | +5.00% |
| `draft_budget_fit_pass` | 2/20 = 10.00% | 2/20 = 10.00% | +0.00% |
| `recomputed_budget_hard_ok` | 7/20 = 35.00% | 8/20 = 40.00% | +5.00% |
| `meal_grounding_ok` | 10/20 = 50.00% | 10/20 = 50.00% | +0.00% |
| `attraction_grounding_ok` | 20/20 = 100.00% | 20/20 = 100.00% | +0.00% |
| `attraction_diversity_ok` | 18/20 = 90.00% | 16/20 = 80.00% | -10.00% |
| `meal_diversity_ok` | 15/20 = 75.00% | 16/20 = 80.00% | +5.00% |
