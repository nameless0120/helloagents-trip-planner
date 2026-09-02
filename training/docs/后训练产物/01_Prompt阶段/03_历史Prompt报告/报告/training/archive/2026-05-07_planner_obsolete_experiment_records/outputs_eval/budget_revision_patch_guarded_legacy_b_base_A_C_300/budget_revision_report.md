# Budget Revision Eval: budget_revision_patch_guarded_v2_base_A_C_300

- records: `training/data/v3/eval_harder_prompt_ablation_20260505/A_C/records.jsonl`
- first_generations: `training/outputs/eval/prompt_ablation_20260505/base_qwen25_7b_prompt_ablation_20260505_A_C/generations.jsonl`
- output_file: `training/outputs/eval/budget_revision_patch_guarded_v2_base_A_C_300/budget_revision_generations.postprocessed.jsonl`
- raw_output_file: `training/outputs/eval/budget_revision_patch_guarded_v2_base_A_C_300/budget_revision_generations.raw.jsonl`
- base_url: `http://127.0.0.1:4396/v1`
- workers: 10
- revision_mode: `patch`
- accept_guard: True
- total compared: 300
- revision_attempted: 226
- patch_accepted: 10
- skipped_budget_already_fit: 72
- failed_or_unparseable_after_postprocess: 2

## Before vs After

| Metric | Before | After | Delta |
| --- | ---: | ---: | ---: |
| `planner_draft_hard_pass` | 134/300 = 44.67% | 136/300 = 45.33% | +0.66% |
| `budget_selection_ok` | 72/300 = 24.00% | 82/300 = 27.33% | +3.33% |
| `draft_budget_fit_pass` | 28/300 = 9.33% | 35/300 = 11.67% | +2.34% |
| `recomputed_budget_hard_ok` | 115/300 = 38.33% | 119/300 = 39.67% | +1.34% |
| `meal_grounding_ok` | 157/300 = 52.33% | 157/300 = 52.33% | +0.00% |
| `attraction_grounding_ok` | 296/300 = 98.67% | 296/300 = 98.67% | +0.00% |
| `attraction_diversity_ok` | 265/300 = 88.33% | 265/300 = 88.33% | +0.00% |
| `meal_diversity_ok` | 197/300 = 65.67% | 197/300 = 65.67% | +0.00% |
