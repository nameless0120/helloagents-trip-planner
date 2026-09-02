# Budget Revision Eval: budget_revision_smoke_base2

- records: `training/data/v3/eval_harder_prompt_ablation_20260505/A_C/records.jsonl`
- first_generations: `training/outputs/eval/prompt_ablation_20260505/base_qwen25_7b_prompt_ablation_20260505_A_C/generations.jsonl`
- output_file: `training/outputs/eval/budget_revision_smoke_base2/budget_revision_generations.postprocessed.jsonl`
- raw_output_file: `training/outputs/eval/budget_revision_smoke_base2/budget_revision_generations.raw.jsonl`
- base_url: `http://127.0.0.1:4396/v1`
- workers: 2
- total compared: 2
- revision_attempted: 0
- skipped_budget_already_fit: 2
- failed_or_unparseable_after_postprocess: 0

## Before vs After

| Metric | Before | After | Delta |
| --- | ---: | ---: | ---: |
| `planner_draft_hard_pass` | 1/2 = 50.00% | 1/2 = 50.00% | +0.00% |
| `budget_selection_ok` | 2/2 = 100.00% | 2/2 = 100.00% | +0.00% |
| `draft_budget_fit_pass` | 1/2 = 50.00% | 1/2 = 50.00% | +0.00% |
| `recomputed_budget_hard_ok` | 2/2 = 100.00% | 2/2 = 100.00% | +0.00% |
| `meal_grounding_ok` | 1/2 = 50.00% | 1/2 = 50.00% | +0.00% |
| `attraction_grounding_ok` | 2/2 = 100.00% | 2/2 = 100.00% | +0.00% |
| `attraction_diversity_ok` | 2/2 = 100.00% | 2/2 = 100.00% | +0.00% |
| `meal_diversity_ok` | 2/2 = 100.00% | 2/2 = 100.00% | +0.00% |
