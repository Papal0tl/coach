# Session Notes: Binary Tree Maximum Path Sum

## Timeline

- 2026-07-31: Session started. Problem sourced from user-provided LeetCode.cn link. Full page content was not fetchable (client-rendered); statement, examples, and constraints recorded from the well-known canonical LeetCode 124 text.
- 2026-07-31: Agent reference solution written and validated against 8 local tests (all pass).
- 2026-07-31: User first draft committed. Correct overall shape (post-order dfs, clamping each child to `max(child, 0)`) transferred without prompting. Three issues present: (1) `dfs(root)` is defined but never called before `return self.res`, so the function always returns `-inf`; (2) `sef.res` typo (`self` misspelled); (3) the deeper logic issue predicted in the rubric — `self.res` is being used for both the per-call return value and the tracked global best, so the update `self.res = max(left, right)` drops `root.val` and never considers the "bend" case (`left + right` together). Asked user to run the code first (established empirical-debugging preference) before addressing the invariant conflation.
- 2026-07-31: User self-diagnosed the missing `dfs(root)` call unprompted after being shown the `-inf` output, and self-corrected the `sef` typo in the same edit while adding the call. Declined to have the agent make the edit (agent redirected per hint-only mode; no prior session has had the agent edit `attempt.py`).
- 2026-07-31: Second draft separated the per-call return value (`root.val + max(left, right)`) from the tracked best (`self.res = max(self.res, left + right)`) — correctly stopped overwriting `self.res` and correctly limited the *return* to one branch. Still missing `root.val` in the `self.res` update; traced the single-node `[1]` case (expected 1, got 0) to find it, then fixed it unprompted in the next edit: `self.res = max(self.res, root.val + left + right)`. All 8 local tests pass.
- 2026-07-31: Declined the invariant/complexity follow-up question and asked to move straight to the blog — first declined follow-up question in this specific problem's session (contrast with the invariant question in maximum-depth-of-binary-tree, 2026-07-15, which was also declined; and kth-smallest-element-in-a-bst, 2026-07-22, where it was answered only on a second ask).

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
