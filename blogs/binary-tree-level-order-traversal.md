# Binary Tree Level Order Traversal

- Problem slug: `binary-tree-level-order-traversal`
- Archive path: `archives/2026-07-18-binary-tree-level-order-traversal/`

Write concise bullets or compact paragraphs. Cover every section, but do not pad.

Sections marked `Agent-filled` should be drafted by the coaching agent before the user writes. Sections marked `User-filled` must be written or revised by the user in their own words.

## Problem

Given the root of a binary tree, return the level order traversal of its nodes' values (from left to right, level by level) as a list of lists.

## My Initial Intuition

Using recursion, but recursion naturally goes depth-first, while this problem wants nodes grouped by level. I realized I needed a way to process all nodes of one level before moving to the next.

## Brute Force

Use DFS and record each node's depth in a dictionary or list of lists (e.g., levels[depth].append(node.val)). This correctly groups nodes by level but requires tracking the depth explicitly. BFS with a queue is more direct because it naturally visits nodes level by level.

## Key Insight

A queue processes nodes in the same order they are discovered. At the start of each iteration, the queue contains exactly one level. By saving size = len(queue) before processing, I know exactly how many nodes belong to the current level, and any children added during the loop automatically become the next level.

## Final Algorithm

Agent-filled as a concise outline; user should revise if it does not match their understanding.

Use a FIFO queue (`collections.deque`), seeded with `root`. In each outer-loop iteration, snapshot `size = len(queue)` before popping anything — that snapshot is exactly the number of nodes in the current level, since every node already queued was enqueued while processing the previous level. Pop exactly `size` nodes, collect their `.val`s into `level`, and enqueue any non-`None` children (which will be processed in the next iteration, as the next level). Append `level` to the result after each outer iteration. Return `[]` immediately if `root` is `None`.

## Correctness Argument

The queue contains exactly the nodes of one level at the beginning. Save size = len(queue) before processing, so only those size nodes are removed and added to level. Any children are enqueued for the next iteration, so nodes from different depths are never mixed. Therefore, every node appears exactly once in the correct level.

## Complexity

Agent-filled; user should confirm they understand it.

Time: O(n) — every node is enqueued and dequeued exactly once.
Space: O(n) — the queue holds at most O(w) nodes at a time, where w is the maximum width of any level; in the worst case (e.g. the bottom level of a complete tree) w is O(n). The output also holds all n values.

## Edge Cases

Agent-filled as a checklist; user should add any cases they personally missed.

- Empty tree (`root = None`) -> `[]`.
- Single node -> `[[val]]`.
- Fully skewed tree (all-left or all-right chain) -> each level has exactly one node.
- Uneven levels (some nodes missing a child) -> level lists have varying lengths, not just powers of two.

## Mistakes I Made

- Tied to solve the problem with recursive DFS, but that naturally traverses by depth rather than by level, making the solution more complicated than using BFS.

## How I Will Recognize This Pattern Next Time

If a tree problem asks to process nodes level by level, one layer at a time, or from left to right within each depth. Should immediately think of BFS with a queue. If need to keep the levels separate, record size = len(queue) before processing each level.
