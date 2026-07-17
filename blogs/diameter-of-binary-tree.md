# Diameter of Binary Tree

- Problem slug: `diameter-of-binary-tree`
- Archive path: `archives/2026-07-17-diameter-of-binary-tree/`

Write concise bullets or compact paragraphs. Cover every section, but do not pad.

Sections marked `Agent-filled` should be drafted by the coaching agent before the user writes. Sections marked `User-filled` must be written or revised by the user in their own words.

## Problem

Given the root of a binary tree, return the length (in edges) of the longest path between any two nodes in the tree. This path may or may not pass through the root.

## My Initial Intuition

User-filled.

{{initial_intuition}}

## Brute Force

User-filled.

{{brute_force}}

## Key Insight

User-filled.

{{key_insight}}

## Final Algorithm

Agent-filled as a concise outline; user should revise if it does not match their understanding.

A single post-order (bottom-up) recursive helper `getDepth(node)` computes the height of `node` (edges to its deepest leaf), returning `0` for `None` and `1 + max(getDepth(node.left), getDepth(node.right))` otherwise. At every node, before returning, update a running-best value (`self.length`) with `left_height + right_height` — the length of the longest path that "turns" at this node. `diameterOfBinaryTree(root)` calls `getDepth(root)` once (for its side effect) and returns `self.length`.

## Correctness Argument

User-filled, with agent prompts if needed.

{{correctness_argument}}

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

User-filled.

{{mistakes}}

## How I Will Recognize This Pattern Next Time

User-filled.

{{pattern_recognition}}
