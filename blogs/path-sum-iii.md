# Path Sum III

- Problem slug: `path-sum-iii`
- Archive path: `archives/2026-07-29-path-sum-iii/`

## Problem

Given the root of a binary tree and an integer `targetSum`, count the number
of downward paths (parent to child, no direction changes) whose node values
sum to `targetSum`. A path can start and end at any node — it does not have
to start at the root or end at a leaf.

## My Initial Intuition

Using DFS. For each node, treat it as the starting point and check all downward paths from it.

## Brute Force

Use one DFS to count paths starting from the current node, and another recursion to make every node a possible starting point.

Restarting from every node works because a valid path can start anywhere in the tree, not only at the root. So every possible starting node gets checked.

## Key Insight

The tree version of a prefix sum is the sum from the root to the current node.

The difference is that a tree branches, so after exploring one child, I need to remove its prefix sum before exploring the other child. This backtracking keeps the hashmap only for the current root-to-node path.

## Final Algorithm

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

For each node, `dfs(node, targetSum)` counts all valid paths starting at that node.

Then `pathSum` recursively does the same thing for the left and right subtrees. Since every path has exactly one starting node, it is counted once when that starting node is processed. So no valid path is missed or counted twice.

## Complexity

Agent-filled; user should confirm they understand it.

- Time: O(n^2) worst case (left- or right-skewed tree — `dfs` is restarted at
  each of the n nodes, and can walk up to n nodes downward from a node near
  the root). O(n log n) average case on a balanced tree.
- Space: O(h) for the recursion stack, where h is the tree height (ignoring
  the O(n) call-stack depth from `pathSum`'s own recursion, which is also
  bounded by h).

## Edge Cases

- Empty tree.
- Single node, value equals target.
- Single node, value does not equal target.
- Negative node values.
- Target sum of 0 with a chain of 0-valued nodes (many overlapping valid paths).
- A valid path that does not start at the root.

## Mistakes I Made

N/A

## How I Will Recognize This Pattern Next Time

If a tree problem asks for the sum of a downward path and the path can start anywhere, I should think about prefix sums. It is similar to subarray sum: check whether `current_sum - targetSum` has appeared before.

