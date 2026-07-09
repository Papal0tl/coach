# Rubric

- Problem slug: `copy-list-with-random-pointer`
- Archive path: `archives/2026-07-09-copy-list-with-random-pointer/`

## Target Skills

| Skill | Target | Evidence | Status |
| --- | --- | --- | --- |
| Problem restatement | Names both `next` and `random` as pointers to reproduce, and that copies must be structurally identical but reference-distinct from the originals | | pending |
| Constraint analysis | Recognizes `random` can point forward, backward, to self, or be `None` | | pending |
| Brute-force construction | Any working approach (even O(n^2) lookup by value/index) before optimizing | | pending |
| Pattern recognition | Identifies the need for a mapping from old node identity to new node, likely via hash map | | pending |
| Invariant formulation | States why two passes are needed (forward-reference problem) rather than just copying in one pass | | pending |
| Complexity analysis | States O(n) time / O(n) space for the map-based solution unprompted | | pending |
| Edge-case design | Covers empty list, self-referential random, no-random-pointers cases | | pending |
| Debugging discipline | Uses concrete tracing if bugs appear (e.g., prints/inspects `old_to_new` mapping) | | pending |
| Communication | Clear English reasoning in comments and discussion | | pending |

## Intervention Count

- Clarifying questions: 0
- Hints: 0
- Direct explanations: 0
- Code-level nudges: 0

## Closeout Assessment

Pending — to be filled in after user attempt and blog review.
