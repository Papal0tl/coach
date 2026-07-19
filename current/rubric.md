# Rubric

- Problem slug: `convert-sorted-array-to-binary-search-tree`
- Archive path: `archives/2026-07-19-convert-sorted-array-to-binary-search-tree/`

## Target Skills

| Skill | Target | Evidence | Status |
| --- | --- | --- | --- |
| Problem restatement | Recognize this builds a new tree from an array, not a traversal of an existing one | | |
| Constraint analysis | Note the sorted/unique input and the height-balanced requirement specifically (not just "any BST") | | |
| Brute-force construction | Consider why an arbitrary root choice (e.g., always leftmost) fails the balance requirement | | |
| Pattern recognition | Reach for divide-and-conquer / recursion on an index range, transferring the split-recurse shape from sort-list (LC 148) | | |
| Invariant formulation | Articulate why picking the middle element guarantees balance | | |
| Complexity analysis | State O(n) time / O(log n) recursion-stack space unprompted | | |
| Edge-case design | Cover single element, even-length arrays, and confirm no explicit comparisons are needed since input is sorted | | |
| Debugging discipline | Run code rather than mentally trace when bugs appear | | |
| Communication | English, clear reasoning in comments/blog | | |

## Intervention Count

- Clarifying questions: 0
- Hints: 0
- Direct explanations: 0
- Code-level nudges: 0

## Closeout Assessment

TBD
