# Rubric

- Problem slug: `binary-tree-right-side-view`
- Archive path: `archives/2026-07-24-binary-tree-right-side-view/`

## Target Skills

| Skill | Target | Evidence | Status |
| --- | --- | --- | --- |
| Problem restatement | Distinguish "rightmost visible node per level" from "rightmost leaf" or "right spine" | Blog Problem section states this precisely | met |
| Constraint analysis | Recognize this is per-level, not a single-path, traversal | Brute Force section frames it as "store nodes by depth" | met |
| Brute-force construction | Full level-order collection, then take last of each level | Stated distinctly from Final Algorithm in blog | met |
| Pattern recognition | Transfer BFS level-size-snapshot from binary-tree-level-order-traversal (2026-07-18/19) | First draft (`c0015db`) went directly to the level-size-snapshot BFS solution, zero hints; blog generalized to the wider "one value per level" family unprompted | met |
| Invariant formulation | State why the last-popped node in a level snapshot is the rightmost visible one | Blog Key Insight and Correctness Argument both state it precisely, including the push-order counterfactual | met |
| Complexity analysis | O(n) time, O(w) space (max width) | Blog Complexity section correct, matches reference | met |
| Edge-case design | Empty tree, single node, left-skewed chain, left-deeper-than-right | All 10 reference tests pass including these cases | met |
| Debugging discipline | | Zero bugs to debug this session | n/a |
| Communication | | Blog concise, technically precise, unprompted generalization to the pattern family | met |

## Intervention Count

- Clarifying questions: 0
- Hints: 0
- Direct explanations: 0
- Code-level nudges: 0

## Closeout Assessment

Cleanest session of the tree arc so far: zero bugs, zero hints on algorithmic shape, blog accepted with zero required revisions, and an unprompted generalization to the "one value per level" pattern family beyond this specific problem. Ready to archive.
