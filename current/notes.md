# Session Notes

- Problem slug: `diameter-of-binary-tree`
- Archive path: `archives/2026-07-17-diameter-of-binary-tree/`

## Agent Preparation

- Pattern: recursive bottom-up combine (post-order), same family as maximum-depth-of-binary-tree, but with a second, distinct piece of state maintained alongside the return value.
- Key insight: the diameter's "turning point" can be any node; at each node, the longest path passing through it equals left_height + right_height (no root-only assumption needed). A single post-order pass can evaluate this at every node while still returning height to the parent.
- Invariant or state: `depth(node)` returns the height of `node` (edges to its deepest leaf) to its caller. A separate running-max (`self.best`) is updated at each node with `left_height + right_height`, which is the diameter candidate rooted at that node, not returned up the call stack.
- Complexity target: O(n) time, O(h) space (recursion stack).

## Reference Solution Summary

Single post-order DFS. At each node, recursively compute left and right subtree heights. Update a running best diameter with `left + right`. Return `max(left, right) + 1` as this node's height to its parent. Final answer is the running best.

## Edge Cases

- Empty tree (root is None): diameter is 0.
- Single node: diameter is 0 (no edges).
- Skewed tree (all left or all right children): diameter equals the chain length (height), since the two "children" contributing to any turning point never both exist.
- Diameter not passing through the root: the turning point is some internal node other than the root; the algorithm must not special-case the root.

## User-Facing Takeaways

- This is the fourth prior tree session's recursive-combine shape, but now the function must track two things at once: what it returns (height, for the caller to use) vs. a side value it updates as it goes (best diameter, which no caller needs). Watch whether the user separates these cleanly or tries to force the diameter itself to be the return value (which breaks the parent's height computation).
- "Length" is in edges. A common off-by-one trap is measuring path length in node count instead of edge count.

## Follow-Up Candidates

- None planned by default (user has declined optional follow-ups in 4/4 prior tree sessions); offer only if the user asks.
