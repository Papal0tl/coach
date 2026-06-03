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
| Brute-force construction | 2 | Correctly described O(m²·n) brute force in blog without prompting. | 2026-06-03 |
| Pattern recognition | 3 | Independently chose sliding window + coverage counter on first attempt (LC 76, Hard). | 2026-06-03 |
| Invariant formulation | 2 | Understood v/formed counter in code; needed one blog revision to articulate it clearly in words. | 2026-06-03 |
| Data structure selection | 3 | Reached for two frequency maps + integer coverage counter without hints. | 2026-06-03 |
| Complexity analysis | 2 | Stated O(m + n) correctly in blog; did not discuss unprompted during coding. | 2026-06-03 |
| Edge-case design | 2 | Handled duplicates in t correctly; mentioned no-solution and len(t) > len(s) in blog. | 2026-06-03 |
| Debugging discipline | 2 | Found range bug after being prompted to trace Example 1; fixed structural issue after direct callout. | 2026-06-03 |
| Code clarity | 2 | Clean sliding window structure; paste artifact caused syntax error not caught before submission. | 2026-06-03 |
| Test design | 0 | Not observed (agent wrote tests). | — |
| Communication | 2 | Terse but accurate. Typed blog revisions into chat instead of saving to file — repeated twice. | 2026-06-03 |
