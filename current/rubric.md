# Rubric

- Problem slug: `merge-k-sorted-lists`
- Archive path: `archives/2026-07-10-merge-k-sorted-lists/`

## Target Skills

| Skill | Target | Evidence | Status |
| --- | --- | --- | --- |
| Problem restatement | Names this as a generalization of merge-two-sorted-lists to k lists | pending | pending |
| Constraint analysis | Notes k can be 0 or contain empty lists; total N bounded at 10^4 | pending | pending |
| Brute-force construction | Names collect-all-then-sort (O(N log N)) or naive pairwise scan (O(Nk)) before optimizing | pending | pending |
| Pattern recognition | Reaches for a min-heap or divide-and-conquer pairwise merge for the k-way minimum-extraction pattern | pending | pending |
| Invariant formulation | States that the heap holds at most one current head per list, and that the global min must be one of those heads | pending | pending |
| Complexity analysis | States O(N log k) time and O(k) auxiliary space, and why log k beats scanning k heads | pending | pending |
| Edge-case design | Covers empty `lists`, `lists` of all `None`, single list, duplicate values | pending | pending |
| Debugging discipline | Runs code / traces concrete example rather than guessing on heap-tuple comparison errors | pending | pending |
| Communication | Explains tradeoff between heap and divide-and-conquer approaches if asked | pending | pending |

## Intervention Count

- Clarifying questions: 0
- Hints: 0
- Direct explanations: 0
- Code-level nudges: 0

## Closeout Assessment

pending
