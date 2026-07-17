# Diameter of Binary Tree

- Problem slug: `diameter-of-binary-tree`
- Archive path: `archives/2026-07-17-diameter-of-binary-tree/`

Write concise bullets or compact paragraphs. Cover every section, but do not pad.

Sections marked `Agent-filled` should be drafted by the coaching agent before the user writes. Sections marked `User-filled` must be written or revised by the user in their own words.

## Problem

Given the root of a binary tree, return the length (in edges) of the longest path between any two nodes in the tree. This path may or may not pass through the root.

## My Initial Intuition

Recursively calculate the depth of the left and right subtrees. Long path through a node should use both sides, but I initially mixed up the value that the helper func should return with the value used to calculate the diameter.

## Brute Force

For every node, independently calculate the maximum depth of its left and right subtrees, then use their sum as the longest path passing through that node. Repeating the depth calculation from every node can revisit the same subtrees many times.
O(n²) time in the worst case.

## Key Insight

The recursive helper and the final answer represent different things. getDepth(node) must return one downward path, so it returns 1 + max(left_depth, right_depth). However, the diameter through the current node can use both sides, so it is left_depth + right_depth. Checking this value at every node handles cases where the longest path does not pass through the root.

## Final Algorithm

Agent-filled as a concise outline; user should revise if it does not match their understanding.

A single post-order (bottom-up) recursive helper `getDepth(node)` computes the height of `node` (edges to its deepest leaf), returning `0` for `None` and `1 + max(getDepth(node.left), getDepth(node.right))` otherwise. At every node, before returning, update a running-best value (`self.length`) with `left_height + right_height` — the length of the longest path that "turns" at this node. `diameterOfBinaryTree(root)` calls `getDepth(root)` once (for its side effect) and returns `self.length`.

## Correctness Argument

For every node, getDepth correctly returns the length in nodes of the longest downward path starting there. After obtaining the left and right depths, their sum is the number of edges in the longest path that turns at the current node. Since the algorithm checks this value at every node and keeps the maximum, it returns the diameter of the entire tree.

## Complexity

Agent-filled; user should confirm they understand it.

Time: O(n) — every node is visited exactly once.
Space: O(h) — the recursion call stack grows with the tree's height h. O(log n) for a balanced tree, O(n) worst case for a fully skewed (chain-like) tree.

## Edge Cases

Agent-filled as a checklist; user should add any cases they personally missed.

- Empty tree (`root = None`) -> diameter `0`.
- Single node -> diameter `0` (no edges).
- Fully skewed tree (all-left or all-right chain) -> diameter equals the chain length, since no node ever has two children to combine.
- Diameter whose turning point is not the root -> must be found correctly without assuming the longest path passes through `root`.

## Mistakes I Made

- Originally returned left_depth + right_depth from getDepth. That value is the diameter through the current node, not the depth that the parent needs.
- A leaf node has two None children, my original helper returned 0 for a leaf. It should return 1 + max(0, 0) = 1.
- Assigned length inside the nested helper without using nonlocal, so Python treated it as a separate local variable. The outer length remained 0, which caused the final answer to print 0.
- Did not preserve the maximum diameter. The update must be max(current_best, left_depth + right_depth) rather than simply replacing the value at each node.

## How I Will Recognize This Pattern Next Time

When a tree problem asks for the longest path between two nodes, should think of post-order recursion. The helper usually returns one branch upward to the parent, while the answer at the current node may combine both the left and right branches. Keep a separate running maximum when the final answer may occur anywhere in the tree.
