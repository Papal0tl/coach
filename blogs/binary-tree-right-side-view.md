# Binary Tree Right Side View

- Problem slug: `binary-tree-right-side-view`
- Archive path: `archives/2026-07-24-binary-tree-right-side-view/`

Write concise bullets or compact paragraphs. Cover every section, but do not pad.

Sections marked `Agent-filled` should be drafted by the coaching agent before the user writes. Sections marked `User-filled` must be written or revised by the user in their own words.

## Problem

Given the root of a binary tree, return the values of the nodes visible when standing on the right side of the tree, ordered from top to bottom (LeetCode 199). For each depth level, exactly one node's value is visible: the rightmost node at that depth.

## My Initial Intuition

Read all the whole node in the tree first, then find the rightmost node of each level.

## Brute Force

Traverse the whole tree and store nodes by their depth, then take the last node of each level. But BFS can directly get the last node of each level.

## Key Insight

`size = len(queue)` is a snapshot of how many nodes are in the current level before removing any nodes.

Because it process the current level from left to right, the node popped at index `size - 1` is always the last node in that level, which is exactly the node visible from the right side.

The next level's nodes are added after we save the current `size`, so they do not affect the current level.

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

For each level, `size` records the exact number of nodes in that level before processing starts. Since nodes are popped from left to right, the last popped node is the rightmost node of that level. We append only this node, so the result contains exactly the nodes visible from the right side.

If pushed right children before left children, the last popped node would become the leftmost node.

## Complexity

- Time: O(n) — every node is pushed and popped from the queue exactly once.
- Space: O(w) — the queue holds at most one level's worth of nodes at a time, where w is the maximum width of the tree. In the worst case (a complete tree) w is O(n).

## Edge Cases

- Empty tree (`root = None`) → `[]`.
- Single node → `[root.val]`.
- Left-skewed chain (every node only has a left child) → every node is still visible, since each is the only node at its depth.
- A left subtree deeper than the right subtree → the deepest visible node comes from the left branch, not the right branch (tested with `[1,2,3,4,None,None,None,5]` → `[1,3,4,5]`).

## Mistakes I Made

N/A

## How I Will Recognize This Pattern Next Time

Problem asks for one value from each depth/level of a binary tree, such as the rightmost node, leftmost node, maximum value, or average value of each level, should think of BFS with a level-size snapshot.

The key pattern is:

```python
size = len(queue)

for i in range(size):
    node = queue.popleft()

    if i == size - 1:
        record(node)
```
