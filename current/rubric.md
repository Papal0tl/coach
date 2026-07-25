# Rubric

- Problem slug: `binary-tree-right-side-view`
- Archive path: `archives/2026-07-24-binary-tree-right-side-view/`

## Target Skills

| Skill | Target | Evidence | Status |
| --- | --- | --- | --- |
| Problem restatement | Distinguish "rightmost visible node per level" from "rightmost leaf" or "right spine" | | pending |
| Constraint analysis | Recognize this is per-level, not a single-path, traversal | | pending |
| Brute-force construction | Full level-order collection, then take last of each level | | pending |
| Pattern recognition | Transfer BFS level-size-snapshot from binary-tree-level-order-traversal (2026-07-18/19) | First draft (`c0015db`) went directly to the level-size-snapshot BFS solution, zero hints | met |
| Invariant formulation | State why the last-popped node in a level snapshot is the rightmost visible one | Not yet asked | pending |
| Complexity analysis | O(n) time, O(w) space (max width) | Not yet asked | pending |
| Edge-case design | Empty tree, single node, left-skewed chain, left-deeper-than-right | All 10 reference tests pass including these cases | met |
| Debugging discipline | | Zero bugs to debug this session | n/a |
| Communication | | | pending |

## Intervention Count

- Clarifying questions: 0
- Hints: 0
- Direct explanations: 0
- Code-level nudges: 0

## Closeout Assessment

Pending.
