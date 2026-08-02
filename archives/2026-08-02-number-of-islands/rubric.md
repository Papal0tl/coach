# Rubric

- Problem slug: `number-of-islands`
- Archive path: `archives/2026-08-02-number-of-islands/`

## Target Skills

| Skill | Target | Evidence | Status |
| --- | --- | --- | --- |
| Problem restatement | Observe if restated unprompted | Not observed; moved straight to code. | not observed |
| Constraint analysis | Observe if 300x300 bound / recursion-depth risk is raised unprompted | Not raised unprompted in code, but when asked directly what a large winding island would do, answered correctly and specifically (`RecursionError`) with only the constraint restated, no mechanism hint given. | light prompting |
| Brute-force construction | N/A for this problem (flood fill is the natural first approach) | N/A | n/a |
| Pattern recognition | First graph/connected-components problem: does BFS/DFS-for-connectivity transfer from tree-traversal experience without heavy prompting? | Recursive DFS flood fill (base cases, in-place marking via `'0'`, count increment) written correctly and unprompted on the first draft; only bug was a loop-variable typo, not a pattern/algorithm error. | independent |
| Invariant formulation | Can state precisely: a cell is never recounted once visited/marked | Not asked directly this session; implicit in the correct code (marks `'0'` immediately on visit). | not directly observed |
| Complexity analysis | O(rows*cols) time; space tradeoff between in-place marking and a visited set | Not asked directly; deferred to blog's agent-filled Complexity section. | pending (blog) |
| Edge-case design | Diagonal-not-connected, empty grid, all-water/all-land, non-square grid | Not authored by user; covered by agent test suite (9/9 passing against `attempt.py`). Deferred to blog Edge Cases review. | pending (blog) |
| Debugging discipline | Track bug count and whether self-caught vs. hint-driven | One bug (`for i in range(n)` shadowing outer `i`, leaving `j` undefined -> `NameError`). Self-diagnosed correctly after being shown the traceback and asked one guiding question ("what does this error tell you about the loops") — did not need the fix stated. | light prompting, fast resolution |
| Communication | Terse but accurate correctness argument | Terse answers throughout ("the inner loop reuses i instead of j"; "it could hit the recursion limit and crash"), both accurate. Full written correctness argument deferred to user-filled blog section. | consistent with prior sessions |

## Intervention Count

- Clarifying questions: 2 (traceback -> "what does this error tell you about the loops"; recursion-depth scenario question)
- Hints: 0
- Direct explanations: 0
- Code-level nudges: 0

## Closeout Assessment

Pending blog completion and review.
