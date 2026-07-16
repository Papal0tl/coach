# Rubric

- Problem slug: `invert-binary-tree`
- Archive path: `archives/2026-07-15-invert-binary-tree/`

## Target Skills

| Skill | Target | Evidence | Status |
| --- | --- | --- | --- |
| Problem restatement | Correctly restates "swap children recursively" | | pending |
| Constraint analysis | Notes tree size bound, handles empty tree | | pending |
| Brute-force construction | N/A (problem is already near-optimal) | not applicable |
| Pattern recognition | Transfers recursive DFS pattern from prior tree sessions | Blog states the general trigger unprompted: same operation on every node -> recursive DFS, generalized to "each node can be solved using the same steps as its children" | met |
| Invariant formulation | States that each call returns a fully-inverted subtree | Correctly explained unprompted why discarding recursive return values still works: recursion mutates the existing subtree in place rather than building and returning a new one | met |
| Complexity analysis | O(n) time, O(h) space (recursion stack) | Correctly stated O(n) time, O(h) space, unprompted about recursion stack as the driver | met |
| Edge-case design | Empty tree, single node, skewed tree | | pending |
| Debugging discipline | Runs code rather than predicting output (watch for recurrence of prior session's gap) | | pending |
| Communication | Clear English explanation in blog | Blog is concise, correct, and includes a formal induction-based correctness argument | met |

## Intervention Count

- Clarifying questions: 2
- Hints: 0
- Direct explanations: 0
- Code-level nudges: 0

## Closeout Assessment

Pending.
