# v3 preference-fix eval comparison (vLLM w10)

- eval records: `training/data/v3/eval_harder_attraction_pref_fix_20260506/A_C/records.jsonl`
- base generations: `training/outputs/eval/base_qwen25_7b_pref_fix_vllm_20260506_A_C_w10/generations.jsonl`
- sft generations: `training/outputs/eval/sft_qwen25_7b_v3_1000_cp2_v1_pref_fix_vllm_20260506_A_C_w10/generations.jsonl`
- generation backend: vLLM, GPU2 base + GPU3 SFT, workers=10 per GPU, API failures=0/300 for both

| metric | Base | SFT cp2 v1 | delta |
|---|---:|---:|---:|
| `json_extract_ok` | 300/300 = 100.00% | 300/300 = 100.00% | +0.00 pp |
| `schema_ok` | 299/300 = 99.67% | 298/300 = 99.33% | -0.34 pp |
| `hard_pass` | 238/299 = 79.60% | 255/298 = 85.57% | +5.97 pp |
| `sft_no_budget_sum_hard_pass` | 238/299 = 79.60% | 255/298 = 85.57% | +5.97 pp |
| `attraction_grounding_ok` | 291/299 = 97.32% | 283/298 = 94.97% | -2.35 pp |
| `attraction_diversity_ok` | 265/299 = 88.63% | 207/298 = 69.46% | -19.17 pp |
| `hotel_grounding_ok` | 299/299 = 100.00% | 297/298 = 99.66% | -0.34 pp |
| `meal_complete` | 296/299 = 99.00% | 298/298 = 100.00% | +1.00 pp |
| `meal_grounding_ok` | 257/299 = 85.95% | 270/298 = 90.60% | +4.65 pp |
| `meal_diversity_ok` | 109/299 = 36.45% | 179/298 = 60.07% | +23.62 pp |
| `recomputed_budget_hard_ok` | 261/299 = 87.29% | 263/298 = 88.26% | +0.97 pp |
| `recomputed_budget_fit_ok` | 152/299 = 50.84% | 149/298 = 50.00% | -0.84 pp |
| `budget_selection_ok` | 152/299 = 50.84% | 149/298 = 50.00% | -0.84 pp |
| `budget_arithmetic_consistent` | 168/299 = 56.19% | 218/298 = 73.15% | +16.96 pp |
| `budget_preference_aligned` | 71/299 = 23.75% | 206/298 = 69.13% | +45.38 pp |

## Latency / Output

| run | avg latency | p50 | p90 | avg output chars |
|---|---:|---:|---:|---:|
| Base vLLM w10 | 69.15s | 69.80s | 85.11s | 6831 |
| SFT cp2 v1 vLLM w10 | 89.87s | 89.52s | 110.15s | 6983 |
