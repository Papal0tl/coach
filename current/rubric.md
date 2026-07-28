# Rubric

- Problem slug: `construct-binary-tree-from-preorder-and-inorder-traversal`
- Archive path: `archives/2026-07-28-construct-binary-tree-from-preorder-and-inorder-traversal/`

## Target Skills

| Skill | Target | Evidence | Status |
| --- | --- | --- | --- |
| Problem restatement | Can state that the first preorder value is always the current subtree's root | | pending |
| Constraint analysis | Notices values are unique, which licenses a value->index map for O(1) split lookup | | pending |
| Brute-force construction | Can produce a working slicing-based recursive solution (even if O(n^2)) | | pending |
| Pattern recognition | Connects this to prior index-range tree-building session (convert-sorted-array-to-binary-search-tree) | | pending |
| Invariant formulation | States precisely why left subtree must be built before right subtree (preorder consumption order) | | pending |
| Complexity analysis | Distinguishes O(n^2) (slicing/linear search) from O(n) (pointer + hash map) and explains why | | pending |
| Edge-case design | Covers single node, left-skewed, right-skewed, asymmetric split | | pending |
| Debugging discipline | Runs code / traces concrete example rather than guessing | | pending |
| Communication | English, precise invariant and complexity statements | | pending |

## Intervention Count

- Clarifying questions: 0
- Hints: 0
- Direct explanations: 0
- Code-level nudges: 0

## Closeout Assessment

TBD
