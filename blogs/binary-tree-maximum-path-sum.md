# Binary Tree Maximum Path Sum

- Problem slug: `binary-tree-maximum-path-sum`
- Archive path: `archives/2026-07-31-binary-tree-maximum-path-sum/`

## Problem

Given the root of a binary tree, find the maximum path sum of any non-empty
path. A path is any sequence of nodes connected by edges where no node
repeats; it does not need to pass through the root, and it may "bend" at
exactly one node (go up one child, then down the other).

## My Initial Intuition

_Write in your own words._

## Brute Force

_Write in your own words._

## Key Insight

_Write in your own words._

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

_Write in your own words._

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

_Write in your own words._

## How I Will Recognize This Pattern Next Time

_Write in your own words._
