# Session Notes

- Problem slug: `flatten-binary-tree-to-linked-list`
- Archive path: `archives/2026-07-27-flatten-binary-tree-to-linked-list/`

## Agent Preparation

- Pattern: In-place tree restructuring into a degenerate right-only chain, in pre-order sequence. Eleventh tree session; first "rewire the tree itself" task rather than traverse/combine/validate/build/BFS-extract.
- Key insight: For any node with a left child, the left subtree's pre-order sequence must be spliced entirely between the node and its original right subtree. The splice point is the *rightmost* node of the left subtree (its last node in pre-order), whose `.right` should become the node's original `.right`.
- Invariant or state (reference solution, Morris-style iterative): when the cursor `cur` advances, everything to the left of it in pre-order has already been fixed up and is unreachable via `.left`. Only `cur`'s own left subtree (if present) ever needs a splice before moving on. This gives O(n) time with O(1) extra space, since each edge is walked a bounded number of times total (amortized, like Morris traversal).
- Complexity target: O(n) time. Space: O(1) extra for the iterative/Morris-style version; O(h) recursion stack for a recursive version (e.g., reverse pre-order right→left→root with a `prev` pointer).

## Reference Solution Summary

Iterative cursor walk (see `agent_solution.py`):
1. `cur = root`.
2. While `cur`: if `cur.left` exists, find the rightmost descendant of `cur.left` (`predecessor`), attach `predecessor.right = cur.right`, then `cur.right = cur.left`, `cur.left = None`.
3. Advance `cur = cur.right`.

Alternative (not implemented as primary, worth offering as a follow-up): recursive reverse pre-order (visit `right`, then `left`, then `node`), keeping a `self.prev` pointer and setting `node.right = self.prev; node.left = None; self.prev = node` on the way back up. Builds the list back-to-front. O(n) time, O(h) space.

Brute-force baseline: pre-order traversal into a list, then rebuild the tree as a right-only chain in a second pass. O(n) time, O(n) space (list) + O(h) recursion — not in place in the strict follow-up sense, but a valid first correct solution.

## Edge Cases

- Empty tree (`root is None`): must return without error, no mutation needed.
- Single node: no left/right, loop body never touches anything.
- Left-only chain: every node has only a left child — collapses to a right-only chain in reverse order relative to depth-first left descent (still valid pre-order for this shape).
- Right-only chain already: solution should leave it unchanged (no node ever has `cur.left`).
- Mixed left/right at multiple levels: verifies the splice logic composes across levels, not just one splice at the root.

## User-Facing Takeaways

- First attempt (commit `3aa901a`): recursive post-order splice — `flatten(root.left)`, `flatten(root.right)`, detach `left`/`right`, set `root.right = left`, walk `cur = root` along `.right` until the tail, then `cur.right = right`. Correct on the first attempt, zero bugs, all 6 reference tests pass. This is exactly the alternative predicted in Follow-Up Candidates below (not the O(1)-space Morris-style reference solution).
- Time complexity discussion was raised twice (asked to trace the `while cur.right` walk on a left-skewed tree) but the user moved directly to the blog without answering either time. The O(n^2)-worst-case point is preserved as a guiding question in the blog's Complexity section (agent-filled with the answer given, since the user did not engage) and flagged here for the profile's declined-follow-up tracking.

## Follow-Up Candidates

- If the user's first attempt is the O(n) extra-space brute force (collect pre-order list, rebuild), offer the in-place splice as a follow-up.
- If the user reaches the recursive splice-per-node approach (flatten left, flatten right, walk to find the left subtree's tail, splice) independently, note that this is correct but can be O(n^2) on a left-skewed tree because of repeated tail-walks — a good complexity-analysis discussion point, and a lead-in to the O(1)-space Morris-style walk that avoids repeated tail-finding, or the reverse-pre-order-with-prev-pointer recursive alternative that avoids it via processing right-to-left.
