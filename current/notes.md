# Session Notes

- Problem slug: `validate-binary-search-tree`
- Archive path: `archives/2026-07-20-validate-binary-search-tree/`

## Agent Preparation

- Pattern: recursive bounds propagation over a binary tree
- Key insight: withheld from the user until they attempt or ask; see agent_solution.py
- Invariant or state: withheld from the user until they attempt or ask; see agent_solution.py
- Complexity target: O(n) time, O(h) space (h = tree height; recursion stack)

## Reference Solution Summary

Recursive `validate(node, low, high)` that carries an open interval each node's
value must fall strictly inside. Descending left tightens `high` to the
parent's value; descending right tightens `low`. Using `None` as a sentinel
for "unbounded" avoids relying on a fixed integer sentinel that could collide
with real node values at the 32-bit boundary. Verified against 10 local test
cases (10/10 passing), including duplicates and boundary int values.

## Edge Cases

- Single node.
- Duplicate values anywhere in the tree (not valid; strict inequality).
- Values at the 32-bit int boundary (2^31 - 1, -2^31).
- A node that satisfies its immediate parent comparison but violates an
  ancestor further up (the classic trap for a naive parent-only check).
- Fully skewed (left-only or right-only) trees.

## User-Facing Takeaways

- First attempt checks only the immediate parent-child relationship
  (`root.left.val >= root.val`, `root.right.val <= root.val`) with no
  recursion into subtrees and no explicit `True`/`None`-root handling. This
  is exactly the naive trap the rubric anticipated. Intervention used:
  concrete trace request (Intervention Count updated in rubric.md).
- User correctly traced `[5,4,6,None,None,3,7]` and identified the bug
  themselves: "it returns True, but that's wrong since 3 < 5." Confirms the
  naive-trap diagnosis without needing a direct explanation.

## Follow-Up Candidates

- Iterative inorder traversal variant (track previous value, check strictly increasing).
- Iterative version of the bounds-propagation approach using an explicit stack.
