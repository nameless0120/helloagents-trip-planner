# Budget Revision Eval: budget_revision_patch_guarded_sft_cp2_A_C_300

- records: `training/data/v3/eval_harder_prompt_ablation_20260505/A_C/records.jsonl`
- first_generations: `training/outputs/eval/sft_qwen25_7b_v3_1000_cp2_v1_A_C_w8/generations.jsonl`
- output_file: `training/outputs/eval/budget_revision_patch_guarded_sft_cp2_A_C_300/budget_revision_generations.postprocessed.jsonl`
- raw_output_file: `training/outputs/eval/budget_revision_patch_guarded_sft_cp2_A_C_300/budget_revision_generations.raw.jsonl`
- base_url: `http://127.0.0.1:4397/v1`
- workers: 10
- revision_mode: `patch`
- accept_guard: True
- total compared: 300
- revision_attempted: 213
- patch_accepted: 6
- skipped_budget_already_fit: 85
- failed_or_unparseable_after_postprocess: 8

## Before vs After

| Metric | Before | After | Delta |
| --- | ---: | ---: | ---: |
| `planner_draft_hard_pass` | 189/300 = 63.00% | 185/300 = 61.67% | -1.33% |
| `budget_selection_ok` | 85/300 = 28.33% | 91/300 = 30.33% | +2.00% |
| `draft_budget_fit_pass` | 60/300 = 20.00% | 65/300 = 21.67% | +1.67% |
| `recomputed_budget_hard_ok` | 125/300 = 41.67% | 125/300 = 41.67% | +0.00% |
| `meal_grounding_ok` | 209/300 = 69.67% | 204/300 = 68.00% | -1.67% |
| `attraction_grounding_ok` | 280/300 = 93.33% | 275/300 = 91.67% | -1.66% |
| `attraction_diversity_ok` | 209/300 = 69.67% | 206/300 = 68.67% | -1.00% |
| `meal_diversity_ok` | 223/300 = 74.33% | 221/300 = 73.67% | -0.66% |
