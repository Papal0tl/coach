# Maximum Depth of Binary Tree

- Problem slug: `maximum-depth-of-binary-tree`
- Archive path: `archives/2026-07-15-maximum-depth-of-binary-tree/`

Write concise bullets or compact paragraphs. Cover every section, but do not pad.

Sections marked `Agent-filled` should be drafted by the coaching agent before the user writes. Sections marked `User-filled` must be written or revised by the user in their own words.

## Problem

Agent-filled.

Given the root of a binary tree, return its maximum depth: the number of nodes along the longest path from the root down to the farthest leaf. An empty tree has depth 0.

## My Initial Intuition

Traverse the whole tree while keeping track of the current depth, then return the largest depth I found.

## Brute Force

Traverse every root-to-leaf path while carrying the current depth as a parameter. Whenever a leaf is reached, compare its depth with the curent maximum. This visits every node once, time complexity is O(n).

## Key Insight

The maximum depth of a tree is determined entirely by its left and right subtrees. If I already know their depths, the current node's depth is simply the larger one plus one for the current node itself.

## Final Algorithm

Agent-filled as a concise outline; user should revise if it does not match their understanding.

Recursive DFS: `maxDepth(node)` returns 0 if `node is None`. Otherwise it returns `1 + max(maxDepth(node.left), maxDepth(node.right))` — the depth of a subtree is 1 (for the current node) plus the deeper of its two child subtrees. This mirrors the tree's own recursive definition, so no explicit stack, queue, or depth counter is needed.

## Correctness Argument

The recursive call correctly computes the depth of the left and right subtrees. Taking the larger one and adding one counts the current node, so every subtree returns its correct maximum depth. Therefore, the root returns the maximum depth of the entire tree.

## Complexity

Agent-filled; user should confirm they understand it.

Time: O(n) — every node is visited exactly once.
Space: O(h) — the recursion call stack grows with the tree's height h. O(log n) for a balanced tree, O(n) worst case for a fully skewed (chain-like) tree.

## Edge Cases

Agent-filled as a checklist; user should add any cases they personally missed.

- Empty tree (`root = None`) -> 0.
- Single node -> 1.
- Left-skewed or right-skewed chain -> depth equals node count.
- Balanced tree -> depth matches expected level count.

## Mistakes I Made

N/A

## How I Will Recognize This Pattern Next Time

Ask for a property of an entire subtree (height, depth, size, or whether it is balanced).
