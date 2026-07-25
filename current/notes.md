# Session Notes

- Problem slug: `binary-tree-right-side-view`
- Archive path: `archives/2026-07-24-binary-tree-right-side-view/`

## Agent Preparation

- Pattern: BFS level-order traversal (10th tree session, first requiring per-level extraction of a single "edge" node rather than combining/validating/building)
- Key insight: process the tree level by level; within each level, the last node dequeued is the rightmost one visible from the right side. This reuses the level-size-snapshot invariant from binary-tree-level-order-traversal (2026-07-18/19) but only keeps one value per level instead of the whole level.
- Invariant or state: `size = len(queue)` taken before popping any node in the current level guarantees the loop only processes nodes from the current level; the node popped when `i == size - 1` is the last (rightmost) node at that depth.
- Complexity target: O(n) time, O(w) space where w is the max width of the tree (queue holds at most one level at a time).

## Reference Solution Summary

Iterative BFS with a `deque`. For each level, snapshot the queue size, then pop that many nodes; append the value of the last one popped in that level to the result. Push children left-before-right so the last-popped node is genuinely the rightmost.

Alternative (not the primary reference): DFS visiting right child before left child, tracking depth; append a node's value only the first time that depth is reached (`if depth == len(result)`). Equivalent result, different mechanism (recursion depth vs. queue level) — a good comparison question if BFS is reached quickly.

## Edge Cases

- Empty tree (`root = None`) → `[]`.
- Single node → `[root.val]`.
- Left-skewed chain (every node only has a left child) → every node is still visible from the right, since it is the only node at its depth.
- Tree where a left subtree is deeper than the right subtree (e.g. `[1,2,3,4,None,None,None,5]`) → the deepest visible node comes from the left branch, not the right branch; tests this explicitly (test case 7).

## User-Facing Takeaways

First draft (single commit, `c0015db`) went directly from the empty stub to a fully correct BFS level-size-snapshot solution — structurally near-identical to the reference (`level_size`/`size`, `i == level_size - 1`, left-then-right push order). Zero bugs, all 10 tests pass, zero hints needed. Direct, clean transfer of the level-size-snapshot invariant from binary-tree-level-order-traversal (2026-07-18/19), now specialized to keep only the last node per level instead of the whole level. Tenth tree session; continues the pattern of strong first-attempt transfer for previously-seen sub-patterns.

## Follow-Up Candidates

- DFS right-first preorder with depth tracking, as a follow-up comparing recursion-depth-based "first visit wins" vs. BFS's level-size-snapshot "last visit wins."
