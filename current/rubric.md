# Rubric

- Problem slug: `reverse-nodes-in-k-group`
- Archive path: `archives/2026-07-07-reverse-nodes-in-k-group/`

## Target Skills

| Skill | Target | Evidence | Status |
| --- | --- | --- | --- |
| Problem restatement | Correctly restate that groups of size < k at the tail are left untouched | | pending |
| Constraint analysis | Recognize k can equal n (single group) and k can be 1 (no-op) as boundary cases | | pending |
| Brute-force construction | Optional: could describe a buffer-and-relink approach (collect k nodes, reverse via list, relink) before in-place | | pending |
| Pattern recognition | Generalize the pairwise-swap pattern (LC 24) to parameterized group size k; recognize need for a lookahead check before committing to reverse | | pending |
| Invariant formulation | State what `group_prev` (or equivalent) represents at each outer-loop iteration | | pending |
| Complexity analysis | State O(n) time / O(1) space unprompted | | pending |
| Edge-case design | Cover empty list, k=1, k=n, exact multiple, remainder shorter than k | | pending |
| Debugging discipline | Track any bugs and how they were resolved | | pending |
| Communication | Blog accuracy on first submission | | pending |

## Intervention Count

- Clarifying questions: 0
- Hints: 0
- Direct explanations: 0
- Code-level nudges: 0

## Closeout Assessment

TBD — fill in after user attempt and blog are complete.
