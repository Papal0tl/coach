# Binary Tree Right Side View

- Problem slug: `binary-tree-right-side-view`
- Archive path: `archives/2026-07-24-binary-tree-right-side-view/`

Write concise bullets or compact paragraphs. Cover every section, but do not pad.

Sections marked `Agent-filled` should be drafted by the coaching agent before the user writes. Sections marked `User-filled` must be written or revised by the user in their own words.

## Problem

Agent-filled.

Given the root of a binary tree, return the values of the nodes visible when standing on the right side of the tree, ordered from top to bottom (LeetCode 199). For each depth level, exactly one node's value is visible: the rightmost node at that depth.

## My Initial Intuition

User-filled.

## Brute Force

User-filled.

## Key Insight

User-filled.

## Final Algorithm

Agent-filled as a concise outline; user should revise if it does not match their understanding.

BFS traversal with a queue, processing one level at a time:

1. If `root` is `None`, return `[]`.
2. Initialize a queue with `root`.
3. While the queue is non-empty:
   - Snapshot `size = len(queue)` (the number of nodes at the current level, before any children of this level are pushed).
   - Pop `size` nodes one at a time. Push each popped node's left child (if any), then right child (if any).
   - The node popped when the loop index reaches `size - 1` (the last node popped in this level) is the rightmost node at this depth — append its value to the result.
4. Return the result.

## Correctness Argument

User-filled, with agent prompts if needed.

## Complexity

Agent-filled; user should confirm they understand it.

- Time: O(n) — every node is pushed and popped from the queue exactly once.
- Space: O(w) — the queue holds at most one level's worth of nodes at a time, where w is the maximum width of the tree. In the worst case (a complete tree) w is O(n).

## Edge Cases

Agent-filled as a checklist; user should add any cases they personally missed.

- Empty tree (`root = None`) → `[]`.
- Single node → `[root.val]`.
- Left-skewed chain (every node only has a left child) → every node is still visible, since each is the only node at its depth.
- A left subtree deeper than the right subtree → the deepest visible node comes from the left branch, not the right branch (tested with `[1,2,3,4,None,None,None,5]` → `[1,3,4,5]`).

## Mistakes I Made

User-filled.

## How I Will Recognize This Pattern Next Time

User-filled.
