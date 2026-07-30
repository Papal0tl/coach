# Path Sum III

- Problem slug: `path-sum-iii`
- Archive path: `archives/2026-07-29-path-sum-iii/`

## Problem

Agent-filled.

Given the root of a binary tree and an integer `targetSum`, count the number
of downward paths (parent to child, no direction changes) whose node values
sum to `targetSum`. A path can start and end at any node — it does not have
to start at the root or end at a leaf.

## My Initial Intuition

User-filled.

What was your first idea for how to find these paths, before writing any code?

## Brute Force

User-filled.

Describe the approach you actually implemented: a helper that counts paths
starting *exactly* at a given node, combined with restarting that helper from
every node in the tree. Why does restarting from every node give you all
possible paths, not just the ones through the root?

## Key Insight

User-filled.

You correctly connected this problem to subarray-sum-equals-k (prefix sums
over an array). What is the tree equivalent of a "prefix sum," and why does a
tree need an extra step (backtracking/removal) that a flat array traversal
does not?

## Final Algorithm

Agent-filled as a concise outline; user should revise if it does not match their understanding.

The submitted solution uses a helper `dfs(node, target)` that counts downward
paths starting exactly at `node`: it checks `node.val == target`, then
recurses into both children with `target - node.val`. The top-level function
combines three counts for each node: paths starting at that node
(`dfs(node, targetSum)`), plus all qualifying paths entirely within the left
subtree, plus all qualifying paths entirely within the right subtree
(`pathSum(node.left, targetSum) + pathSum(node.right, targetSum)`). This
restart-from-every-node strategy is the brute force; the O(n) prefix-sum +
hashmap optimization was discussed but not implemented this session.

## Correctness Argument

User-filled, with agent prompts if needed.

Why does `dfs(root, targetSum) + pathSum(root.left, targetSum) + pathSum(root.right, targetSum)` count every valid downward path in the tree exactly once (no double-counting, none missed)?

## Complexity

Agent-filled; user should confirm they understand it.

- Time: O(n^2) worst case (left- or right-skewed tree — `dfs` is restarted at
  each of the n nodes, and can walk up to n nodes downward from a node near
  the root). O(n log n) average case on a balanced tree.
- Space: O(h) for the recursion stack, where h is the tree height (ignoring
  the O(n) call-stack depth from `pathSum`'s own recursion, which is also
  bounded by h).

## Edge Cases

Agent-filled as a checklist; user should add any cases they personally missed.

- Empty tree.
- Single node, value equals target.
- Single node, value does not equal target.
- Negative node values.
- Target sum of 0 with a chain of 0-valued nodes (many overlapping valid paths).
- A valid path that does not start at the root.

## Mistakes I Made

User-filled.

## How I Will Recognize This Pattern Next Time

User-filled.

What signals in a future problem would tell you "this might need a prefix-sum-over-a-tree-path approach," the way subarray-sum-equals-k signaled it for arrays?
