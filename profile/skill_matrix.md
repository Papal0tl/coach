# Skill Matrix

Scale:

- `0`: not observed.
- `1`: needs heavy prompting.
- `2`: succeeds with light prompting.
- `3`: independent and reliable.

| Skill | Score | Evidence | Last Updated |
| --- | ---: | --- | --- |
| Problem restatement | 0 | Not observed. | — |
| Constraint analysis | 0 | Not observed. | — |
| Brute-force construction | 2 | Correctly described O(n²)/O(n³) brute force in both session blogs without prompting. | 2026-06-03 |
| Pattern recognition | 2 | First-attempt solves for sliding window (LC 76) and DP (LC 53). Novel patterns (interval sort+scan LC 56, prefix/suffix product LC 238) required guided tracing. Score reflects consistent performance on unfamiliar patterns. | 2026-06-10 |
| Invariant formulation | 2 | Stated Kadane invariant precisely when asked. Prefix/suffix invariant correctly verbalized after one prompt. Blog Key Insight sections need one revision for precision in most sessions. | 2026-06-10 |
| Data structure selection | 3 | Reached for two frequency maps + coverage counter without hints (LC 76). | 2026-06-03 |
| Complexity analysis | 2 | Stated O(n) time and O(n) space correctly for rotate-array without prompting. Consistent across sessions. | 2026-06-06 |
| Edge-case design | 2 | Handled all-negative (Kadane) and duplicates-in-t (sliding window) correctly in code; edge cases in blogs are accurate. | 2026-06-03 |
| Debugging discipline | 2 | No bugs in LC 53. In LC 76, found range bug after prompt to trace; fixed structural issue after direct callout. | 2026-06-03 |
| Code clarity | 2 | Clean solutions; paste artifact caused syntax error in LC 76. No issues in LC 53. | 2026-06-03 |
| Test design | 0 | Not observed (agent wrote tests). | — |
| Communication | 2 | Terse but accurate. Blog pattern-recognition section revised from listing problem names to describing signals (one revision required across all three sessions so far). | 2026-06-05 |
