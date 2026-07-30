# Session Notes: Path Sum III

## Timeline

- 2026-07-29: Session started. Problem sourced from user-provided LeetCode.cn link.
- 2026-07-29: Agent reference solution written (prefix-sum + hashmap DFS), 8/8 local tests pass.
- 2026-07-29: User's first attempt is the predicted brute force — a `dfs(node, target)` helper counting paths starting exactly at `node` (decrementing `target` by `node.val` at each step, matching when `node.val == target`), combined at the top level as `dfs(root) + pathSum(root.left) + pathSum(root.right)` (restart from every node). Correct structure, zero bugs, 8/8 tests pass on the first submission. This matches the "brute force first, correct on first try" pattern from LC 238/LC 148/LC 98. Next: probe complexity (should be O(n^2) worst case) and see if the prefix-sum optimization is reached independently.
- 2026-07-29: Stated O(n^2) worst case correctly and unprompted, attributing it precisely to "restarting a full DFS from every node." Now probing for the O(n) prefix-sum optimization.
- 2026-07-29: Independently connected this problem to subarray-sum-equals-k (array prefix sums + hashmap) when asked for a prior analogous problem, and correctly identified both halves of the tree adaptation unprompted: prefix sum = root-to-node running sum, and the extra step a tree needs beyond the array case is backtracking/removing the current node's sum after recursing into children. Declined to implement this optimization in `attempt.py`, asking to move straight to the blog instead — consistent with this user's frequent pattern of reasoning through an optimization correctly in conversation but not writing/running the code for it (e.g. LC 141's fast/slow pointer, LC 105's O(n) hash-map optimization, LC 114's complexity-analysis follow-up).

## Key Insight (agent-only, do not reveal directly)

Track the running sum from the root to the current node during a DFS. A downward
path from some ancestor `A` to the current node `cur` sums to `targetSum` exactly
when `running_sum(cur) - running_sum(A) == targetSum`, i.e. when
`running_sum(A) == running_sum(cur) - targetSum`. A hashmap of
`{prefix_sum: count}` seen so far *on the current root-to-node path* lets each
node look up in O(1) how many ancestors satisfy this, avoiding the O(n^2)
brute force of restarting a DFS from every node.

`prefix_count[0] = 1` seeds the case where the path starts at the current node
itself (an empty prefix before the root).

## Invariant

At the moment `dfs(node, running_sum)` is entered, `prefix_count` holds the
count of every prefix sum along the path from the root to `node`'s parent
(i.e., all ancestors, not siblings or unrelated subtrees). This is why the
count must be decremented on the way back up (backtracking) before returning
to the parent — otherwise a node's own prefix sum would leak into sibling
subtrees and produce false matches.

## Complexity

- Time: O(n) — each node visited once, O(1) hashmap work per node.
- Space: O(n) worst case (hashmap + recursion stack on a skewed tree), O(h) on
  a balanced tree for the recursion stack alone.

## Brute Force (for comparison)

For every node, run a separate DFS downward summing from that node as a new
"start," checking after each step if the running sum equals target. O(n^2)
worst case (skewed tree), O(n log n) average (balanced tree).

## Edge Cases

- Empty tree → 0.
- Single node equal to target → 1.
- Single node not equal to target → 0.
- Negative node values (path sum can decrease then match later).
- Target sum of 0 with a chain of 0-valued nodes (many overlapping paths).
- Path that doesn't start at the root (must not force root as the start).

## Target Coaching Skills (see rubric.md)

- First test of prefix-sum-on-a-tree pattern in the tree arc — distinct from
  the level-size-snapshot BFS pattern and all prior single-node-recursion
  shapes (visit, combine, mutate, pair-compare, validate, build, splice).
- Watch whether the "restart DFS from every node" brute force is reached
  first (expected, based on this user's consistent brute-force-first pattern
  in prior sessions), and whether the backtracking hashmap-decrement step is
  self-discovered or needs a prompt — this is the most error-prone part of
  the O(n) approach (forgetting to decrement causes silent overcounting
  across sibling subtrees, not a crash).
