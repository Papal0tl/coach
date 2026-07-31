# Session Notes: Binary Tree Maximum Path Sum

## Timeline

- 2026-07-31: Session started. Problem sourced from user-provided LeetCode.cn link. Full page content was not fetchable (client-rendered); statement, examples, and constraints recorded from the well-known canonical LeetCode 124 text.
- 2026-07-31: Agent reference solution written and validated against 8 local tests (all pass).

## Agent Preparation

- Pattern: recursive tree combine with tracked side-state, same family as diameter-of-binary-tree (2026-07-17) — a helper returns one value upward while a separate running best is updated as a side effect.
- Key insight: a node's path can "bend" (use both children) only when that node is being scored as a full path; but the value a node *returns to its parent* can only extend one side, because a path cannot branch once it continues upward. This is the core distinction the user needs to articulate — it's a step beyond diameter-of-binary-tree (which combines two heights) and closer in shape to path-sum-iii (2026-07-29, restart-from-every-node) but requires a single global-best track instead of counting.
- Invariant/state: `gain(node)` returns the maximum sum of a downward path starting at `node` and using at most one child. `best` (nonlocal/self attribute) tracks the maximum sum over all paths seen so far, each candidate computed as `node.val + max(left_gain, 0) + max(right_gain, 0)`.
- Complexity target: O(n) time, O(h) space (recursion stack).

## Reference Solution Summary

Single post-order DFS. At each node, clamp each child's gain to 0 (a negative branch should never be attached). Update `best` with the node acting as the path's turning point (`val + left_gain + right_gain`). Return `val + max(left_gain, right_gain)` upward, since a path continuing through the parent can only take one branch.

## Edge Cases

- Single node (positive or negative) — path is just that node.
- All-negative tree — best path is the least-negative single node, not the whole tree.
- A branch with a negative subtree sum must be clamped to 0, not attached.
- Best path may not pass through the root at all (example 2 in the problem statement already exercises this).
- Left-skewed and right-skewed trees.

## User-Facing Takeaways

(to be filled during/after the feedback loop)

## Follow-Up Candidates

- Compare explicitly against diameter-of-binary-tree: same recursive-combine-with-side-state shape, but this problem needs value clamping (`max(gain, 0)`) since node values can be negative, whereas diameter's height combine has no such clamp.
