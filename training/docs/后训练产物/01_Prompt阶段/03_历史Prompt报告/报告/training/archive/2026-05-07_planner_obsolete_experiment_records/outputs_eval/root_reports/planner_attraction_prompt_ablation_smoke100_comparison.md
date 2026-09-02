# Attraction Prompt Ablation Smoke100

- Same first 100 records from `eval_harder_attraction_pref_fix_20260506/A_C`.
- Model: SFT cp2 v1 via vLLM on GPU3, workers=10.
- These are prompt-only appended-rule ablations; request/context/tool snapshots are unchanged.

| variant | schema | attr grounding | attr diversity | attr count | meal grounding | meal diversity | hard pass | budget pref | avg attr/day | repeat trips | food-as-attr | unknown attr |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| original | 99/100=99.00% | 94/99=94.95% | 64/99=64.65% | 97/99=97.98% | 93/99=93.94% | 63/99=63.64% | 87/99=87.88% | 65/99=65.66% | 2.26 | 35 | 3 | 3 |
| dedupe_only | 99/100=99.00% | 94/99=94.95% | 55/99=55.56% | 97/99=97.98% | 97/99=97.98% | 69/99=69.70% | 89/99=89.90% | 65/99=65.66% | 2.37 | 45 | 7 | 2 |
| source_guard_only | 98/100=98.00% | 87/98=88.78% | 66/98=67.35% | 96/98=97.96% | 95/98=96.94% | 70/98=71.43% | 84/98=85.71% | 60/98=61.22% | 2.21 | 32 | 10 | 6 |
| dedupe_source_guard | 99/100=99.00% | 94/99=94.95% | 51/99=51.52% | 98/99=98.99% | 94/99=94.95% | 61/99=61.62% | 89/99=89.90% | 67/99=67.68% | 2.38 | 48 | 8 | 1 |
| dedupe_source_self_check | 97/100=97.00% | 89/97=91.75% | 62/97=63.92% | 97/97=100.00% | 91/97=93.81% | 68/97=70.10% | 82/97=84.54% | 59/97=60.82% | 2.27 | 36 | 7 | 6 |

## Delta vs original

| variant | attr grounding delta | attr diversity delta | schema delta | hard pass delta |
|---|---:|---:|---:|---:|
| dedupe_only | +0.00 pp | -9.09 pp | +0.00 pp | +2.02 pp |
| source_guard_only | -6.17 pp | +2.70 pp | -1.00 pp | -2.17 pp |
| dedupe_source_guard | +0.00 pp | -13.13 pp | +0.00 pp | +2.02 pp |
| dedupe_source_self_check | -3.20 pp | -0.73 pp | -2.00 pp | -3.34 pp |
