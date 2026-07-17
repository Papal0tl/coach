# Rubric

- Problem slug: `symmetric-tree`
- Archive path: `archives/2026-07-17-symmetric-tree/`

## Target Skills

| Skill | Target | Evidence | Status |
| --- | --- | --- | --- |
| Problem restatement | Distinguish "symmetric" from "equal" (mirrored, not identical) | First draft used `root.left == root.right` (identity/equality, not mirroring) | needs work initially, corrected by draft 2 |
| Constraint analysis | Recognize the crossed-child comparison (`t1.left` vs `t2.right`) | Draft 3 wrote `compare(left.left, right.right)` / `compare(left.right, right.left)` correctly, unprompted once the pair-helper idea landed | met |
| Brute-force construction | N/A — pattern is likely reached directly given tree-recursion history | No separate brute force attempted; went straight for the mirror recursion | N/A |
| Pattern recognition | Reach for a two-argument helper (pair recursion) rather than forcing single-node recursion | Took until draft 4 (after 2 guiding questions) to land on a nested `compare(left, right)` helper; first 3 drafts tried to force single-argument `isSymmetric(root)` to do pair work | met, with scaffolding |
| Invariant formulation | State the mirror invariant for `is_mirror(t1, t2)` precisely | Base-case shape (both-None/one-None/values-differ) was correct from draft 2 onward | met |
| Complexity analysis | O(n) time, O(h) recursive space vs. O(n) iterative queue space | Not yet discussed — pending iterative follow-up | pending |
| Edge-case design | None-vs-None, one-None, shape mismatch, duplicate-value trap | All handled correctly by draft 5; empty-tree case (`root is None`) was missed until directly tested and shown crashing | met after 1 correction |
| Debugging discipline | Run before predicting output | Every fix across all 5 drafts followed an actual run/error, never a mental-trace prediction offered first | met, consistent with established pattern |
| Communication | N/A | N/A | N/A |

## Session-Specific Target

- Iterative BFS/queue traversal as a primary task (not a declined follow-up) — closes a gap open since LC 94 (2026-07-14).

## Intervention Count

- Clarifying questions: 0
- Hints: 0
- Direct explanations: 0
- Code-level nudges: 0

## Closeout Assessment

TBD
