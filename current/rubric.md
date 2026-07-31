# Rubric

- Problem slug: `binary-tree-maximum-path-sum`
- Archive path: `archives/2026-07-31-binary-tree-maximum-path-sum/`

## Target Skills

| Skill | Target | Evidence | Status |
| --- | --- | --- | --- |
| Problem restatement | Distinguish "path" (any node-to-node sequence, may bend once) from a root-to-leaf or single-direction path | pending | pending |
| Constraint analysis | Recognize node values can be negative, so a branch must sometimes be excluded rather than always attached | pending | pending |
| Brute-force construction | Consider recomputing a path sum rooted at every node (O(n^2)) before optimizing to single-pass | pending | pending |
| Pattern recognition | Transfer the recursive-combine-with-tracked-side-state shape from diameter-of-binary-tree | pending | pending |
| Invariant formulation | Separate "value returned to caller" (best single-branch extension, `val + max(left,right,0-clamped)`) from "value tracked as running best" (`val + left + right`, allowed to bend) | pending | pending |
| Complexity analysis | State O(n) time / O(h) space unprompted | pending | pending |
| Edge-case design | Single node, all-negative tree, negative branch clamped to 0, best path not through root | pending | pending |
| Debugging discipline | Run code rather than predict output (established strength) | pending | pending |
| Communication | Blog Mistakes Made completeness (recurring watch area) | pending | pending |

## Intervention Count

- Clarifying questions: 0
- Hints: 0
- Direct explanations: 0
- Code-level nudges: 0

## Closeout Assessment

pending
