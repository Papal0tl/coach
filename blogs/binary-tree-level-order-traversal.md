# Binary Tree Level Order Traversal

- Problem slug: `binary-tree-level-order-traversal`
- Archive path: `archives/2026-07-18-binary-tree-level-order-traversal/`

Write concise bullets or compact paragraphs. Cover every section, but do not pad.

Sections marked `Agent-filled` should be drafted by the coaching agent before the user writes. Sections marked `User-filled` must be written or revised by the user in their own words.

## Problem

Given the root of a binary tree, return the level order traversal of its nodes' values (from left to right, level by level) as a list of lists.

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

Use a FIFO queue (`collections.deque`), seeded with `root`. In each outer-loop iteration, snapshot `size = len(queue)` before popping anything — that snapshot is exactly the number of nodes in the current level, since every node already queued was enqueued while processing the previous level. Pop exactly `size` nodes, collect their `.val`s into `level`, and enqueue any non-`None` children (which will be processed in the next iteration, as the next level). Append `level` to the result after each outer iteration. Return `[]` immediately if `root` is `None`.

## Correctness Argument

User-filled, with agent prompts if needed.

{{correctness_argument}}

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

User-filled.

{{mistakes}}

## How I Will Recognize This Pattern Next Time

User-filled.

{{pattern_recognition}}
