# Budget Revision Eval: budget_revision_patch_sft_cp2_A_C_20

- records: `training/data/v3/eval_harder_prompt_ablation_20260505/A_C/records.jsonl`
- first_generations: `training/outputs/eval/sft_qwen25_7b_v3_1000_cp2_v1_A_C_w8/generations.jsonl`
- output_file: `training/outputs/eval/budget_revision_patch_sft_cp2_A_C_20/budget_revision_generations.postprocessed.jsonl`
- raw_output_file: `training/outputs/eval/budget_revision_patch_sft_cp2_A_C_20/budget_revision_generations.raw.jsonl`
- base_url: `http://127.0.0.1:4397/v1`
- workers: 10
- revision_mode: `patch`
- total compared: 20
- revision_attempted: 13
- skipped_budget_already_fit: 7
- failed_or_unparseable_after_postprocess: 1

## Before vs After

| Metric | Before | After | Delta |
| --- | ---: | ---: | ---: |
| `planner_draft_hard_pass` | 15/20 = 75.00% | 14/20 = 70.00% | -5.00% |
| `budget_selection_ok` | 7/20 = 35.00% | 10/20 = 50.00% | +15.00% |
| `draft_budget_fit_pass` | 5/20 = 25.00% | 7/20 = 35.00% | +10.00% |
| `recomputed_budget_hard_ok` | 10/20 = 50.00% | 11/20 = 55.00% | +5.00% |
| `meal_grounding_ok` | 15/20 = 75.00% | 14/20 = 70.00% | -5.00% |
| `attraction_grounding_ok` | 20/20 = 100.00% | 19/20 = 95.00% | -5.00% |
| `attraction_diversity_ok` | 12/20 = 60.00% | 10/20 = 50.00% | -10.00% |
| `meal_diversity_ok` | 17/20 = 85.00% | 16/20 = 80.00% | -5.00% |
