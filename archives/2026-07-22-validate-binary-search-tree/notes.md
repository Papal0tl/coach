# Session Notes

- Problem slug: `validate-binary-search-tree`
- Archive path: `archives/2026-07-22-validate-binary-search-tree/`

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
- User pivoted to inorder traversal (self.prev + strictly-increasing check),
  the correct pattern. Bug: the final line recurses `inorder(node.left)`
  again instead of `inorder(node.right)` — the right subtree is never
  visited. Chose a trace request (same style as before) rather than pointing
  at the line directly.
- User self-diagnosed the bug from the trace request ("it re-checks the left
  subtree instead of the right") and fixed it to `inorder(node.right)`
  unprompted. All 10 local tests pass. Zero direct explanations needed this
  session — every bug was found via the user's own trace.
- Blog's first draft skipped the parent-only-check attempt entirely,
  narrating inorder traversal as the original idea. Revision requested;
  the user added the actual first attempt, the concrete failure trace, and
  a generalized "check local vs. global before trusting a per-parent
  comparison" lesson — accepted on first pass with zero further requests.

## Follow-Up Candidates

- Iterative inorder traversal variant (track previous value, check strictly increasing).
- Iterative version of the bounds-propagation approach using an explicit stack.
