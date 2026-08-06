# Rubric

- Problem slug: `rotting-oranges`
- Archive path: `archives/2026-08-06-rotting-oranges/`

## Target Skills

| Skill | Target | Evidence | Status |
| --- | --- | --- | --- |
| Problem restatement | Restate multi-source spread requirement | Not verbally restated during coding; revisit in blog problem summary | pending |
| Constraint analysis | Note small grid bound (<=10x10) permits simple BFS | Not explicitly discussed this session | pending |
| Brute-force construction | Consider repeated full-grid scan per minute | Not discussed; went straight to BFS | pending |
| Pattern recognition | Identify multi-source BFS (level-order spread) | Independently wrote `size = len(queue)` / drain-exactly-that-many level loop with no hint toward this specific structure | met |
| Invariant formulation | BFS level = minutes elapsed; queue holds current frontier | Same evidence as pattern recognition; minute counter incremented once per fully-drained level, correctly | met |
| Complexity analysis | O(m*n) time, O(m*n) space | Not discussed yet; revisit in blog complexity section | pending |
| Edge-case design | No fresh oranges, unreachable fresh orange, empty-ish grid | Missed the "fresh orange isolated by an empty cell" case on first pass (bug 3); code rotted/decremented for any in-bounds neighbor regardless of value. Fixed only after agent constructed and ran `[[2, 0, 1]]` as a counterexample — the user did not generate this edge case independently | gap identified |
| Debugging discipline | | Each of 4 bugs fixed in the round immediately after a concrete trace/counterexample was given; no unproductive edits. Two rounds had "check the code" with zero diff (procedural mixup, not a logic issue) | developing |
| Communication | | Responses are terse but precise and correct (e.g. "oh it's just pushing the number of rows, not the coordinates") | adequate |

## Intervention Count

- Clarifying questions: 3
- Hints: 4
- Direct explanations: 0
- Code-level nudges: 1

## Closeout Assessment

Pending — finalize after blog and review.
