# Rubric

- Problem slug: `kth-smallest-element-in-a-bst`
- Archive path: `archives/2026-07-22-kth-smallest-element-in-a-bst/`

## Target Skills

| Skill | Target | Evidence | Status |
| --- | --- | --- | --- |
| Problem restatement | Recognize this asks for a rank (kth) among sorted values, not just validity or a traversal order | | not observed |
| Constraint analysis | Note `1 <= k <= n`, so no out-of-range handling is required within given constraints | | not observed |
| Brute-force construction | Full inorder traversal collecting all values into a list, then index `[k-1]` | | not observed |
| Pattern recognition | Connect "inorder traversal of a BST is sorted" from validate-binary-search-tree to this problem's rank-extraction need | | not observed |
| Invariant formulation | State that inorder visit order corresponds to ascending value order, and that a running visited-count reaching k identifies the answer | | not observed |
| Complexity analysis | Distinguish O(n) time/space (collect-all) from O(h+k) time / O(h) space (early-stopping iterative) | | not observed |
| Edge-case design | Single node, k=1, k=n, skewed trees | | not observed |
| Debugging discipline | Use running code / concrete traces over mental prediction, consistent with established preference | | not observed |
| Communication | Clear English explanation of the early-stopping mechanism if reached | | not observed |

## Intervention Count

- Clarifying questions: 0
- Hints: 0
- Direct explanations: 0
- Code-level nudges: 0

## Closeout Assessment

Pending — session in progress.
