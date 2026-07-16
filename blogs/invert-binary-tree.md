# Invert Binary Tree

- Problem slug: `invert-binary-tree`
- Archive path: `archives/2026-07-15-invert-binary-tree/`

Write concise bullets or compact paragraphs. Cover every section, but do not pad.

Sections marked `Agent-filled` should be drafted by the coaching agent before the user writes. Sections marked `User-filled` must be written or revised by the user in their own words.

## Problem

Agent-filled.

Given the root of a binary tree, invert the tree (mirror it: swap every node's left and right child), and return its root.

## My Initial Intuition

User-filled.

## Brute Force

User-filled.

## Key Insight

User-filled.

## Final Algorithm

Agent-filled as a concise outline; user should revise if it does not match their understanding.

Recursive DFS that mutates in place: `invertTree(node)` returns `None` if `node is None`. Otherwise, swap `node.left` and `node.right`, then recursively call `invertTree` on each (now-swapped) child to invert their subtrees in place, and return `node`. Because the recursion mutates the actual child node objects, the recursive calls' return values don't need to be reassigned back — the swap already repointed `node.left`/`node.right` at the correct children, and recursion finishes inverting each subtree in place.

## Correctness Argument

User-filled, with agent prompts if needed.

## Complexity

Agent-filled; user should confirm they understand it.

Time: O(n) — every node is visited exactly once.
Space: O(h) — the recursion call stack grows with the tree's height h. O(log n) for a balanced tree, O(n) worst case for a fully skewed (chain-like) tree.

## Edge Cases

Agent-filled as a checklist; user should add any cases they personally missed.

- Empty tree (`root = None`) -> returns `None`.
- Single node -> returns itself unchanged (no children to swap).
- Left-skewed or right-skewed tree -> skew direction flips.
- Symmetric tree -> structure unchanged but still correctly mirrored (values may still move).

## Mistakes I Made

User-filled.

## How I Will Recognize This Pattern Next Time

User-filled.
