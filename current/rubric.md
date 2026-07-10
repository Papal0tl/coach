# Rubric

- Problem slug: `sort-list`
- Archive path: (assigned at closeout)

## Target Skills

| Skill | Target | Evidence | Status |
| --- | --- | --- | --- |
| Problem restatement | Names the constraint that a linked list can't be randomly indexed, ruling out array-style sorts | | pending |
| Constraint analysis | Recognizes O(n log n) time is required (rules out insertion/selection sort) and considers the O(1)-space follow-up | | pending |
| Brute-force construction | Describes an O(n) space approach (dump values into an array, sort, rebuild list) as a valid but non-optimal baseline | | pending |
| Pattern recognition | Identifies merge sort as the natural fit; reuses fast/slow midpoint-finding and two-list merge from prior sessions | | pending |
| Invariant formulation | States why the recursive base case (length 0 or 1) is already sorted, and why merging two sorted halves yields a sorted whole | | pending |
| Complexity analysis | States O(n log n) time / O(log n) space (recursive) unprompted; aware O(1) space needs an iterative bottom-up variant | | pending |
| Edge-case design | Covers empty list, single node, two nodes, duplicate values | | pending |
| Debugging discipline | Traces the split step carefully (severing `slow.next`) since a missed severance causes infinite recursion or duplicated nodes | | pending |
| Communication | Clear English reasoning; notes the reuse of fast/slow and merge sub-patterns from prior sessions | | pending |

## Intervention Count

- Clarifying questions: 0
- Hints: 0
- Direct explanations: 0
- Code-level nudges: 0

## Closeout Assessment

Pending.
