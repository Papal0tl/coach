# Binary Tree Maximum Path Sum

- Problem slug: `binary-tree-maximum-path-sum`
- Archive path: `archives/2026-07-31-binary-tree-maximum-path-sum/`

## Problem

Given the root of a binary tree, find the maximum path sum of any non-empty
path. A path is any sequence of nodes connected by edges where no node
repeats; it does not need to pass through the root, and it may "bend" at
exactly one node (go up one child, then down the other).

## My Initial Intuition

The path could go through a node and use both its left and right sides. Could use recursion to calculate the best path from each node.

## Brute Force

Try different paths and calculate their sums, but there are too many possible paths. This would be inefficient for a large tree.

## Key Insight

At each node, the answer can use both left and right branches, but when returning to the parent, it can only choose one branch. Negative branches should be ignored.

## Final Algorithm

A single post-order DFS with a helper `gain(node)` that returns the maximum
sum of a downward path starting at `node` and extending into at most one
child. Each child's contribution is clamped with `max(child_gain, 0)` so a
negative branch is never attached. At every node, a separate tracked value
`self.res` is updated with `node.val + left_gain + right_gain` — the best
path *through* this node, allowed to use both children since this is not
what gets returned upward. `gain(node)` itself returns only
`node.val + max(left_gain, right_gain)`, since a path continuing to the
parent can only extend one branch. The final answer is the maximum value
`self.res` ever reached.

## Correctness Argument

For each node, gain(node) returns the best path starting from that node and going down through only one child. At the same time, self.res checks the path using both children and the current node. Since every node is checked once, the maximum value found is the maximum path sum.

## Complexity

- Time: O(n) — every node is visited exactly once by `gain`.
- Space: O(h) — recursion stack depth equals tree height (worst case O(n)
  for a skewed tree, O(log n) for a balanced tree).

## Edge Cases

- Single node (positive or negative) — the path is just that node.
- All-negative tree — the best path is the least-negative single node, not
  the whole tree.
- A branch with a negative subtree sum must be excluded (clamped to 0), not
  attached.
- The best path may not pass through the root at all.
- Left-skewed and right-skewed trees.

## Mistakes I Made

- Updated self.res with max(left, right) instead of the full path root.val + left + right.
- Returned root.val + self.res, but self.res is the overall answer, not the path that should be passed to the parent.
- Did not understand why return root.val + max(left, right) only uses one side.
- Thought the returned path should include both the left and right branches.

## How I Will Recognize This Pattern Next Time

When a tree path can go through both children, should separate the value used for the answer from the value returned to the parent. The answer can use both sides, while the returned path can only use one side.
