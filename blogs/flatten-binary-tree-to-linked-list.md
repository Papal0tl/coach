# Flatten Binary Tree to Linked List

- Problem slug: `flatten-binary-tree-to-linked-list`
- Archive path: `archives/2026-07-25-flatten-binary-tree-to-linked-list/`

Write concise bullets or compact paragraphs. Cover every section, but do not pad.

Sections marked `Agent-filled` should be drafted by the coaching agent before the user writes. Sections marked `User-filled` must be written or revised by the user in their own words.

## Problem

Given the root of a binary tree, flatten it in place into a "linked list": reuse the same `TreeNode` objects, always set `left` to `None`, and chain nodes together via `right` in the same order as a pre-order traversal (root, then left subtree, then right subtree).

## My Initial Intuition

Doing a preorder traversal first, storing all nodes in a list, and then reconnecting them into a right-only chain. It is easy to understand but uses extra space, so I looked for an in-place solution instead.

## Brute Force

Traverse the tree in preorder and store every node in a list. Then iterate through the list, set each node's left to None, and connect its right pointer to the next node. This works in O(n) time but needs O(n) extra space for the list.

## Key Insight

After recursively flattening both subtrees, the left subtree has already become a preorder chain. I only need to attach that chain to root.right, walk to its tail, and connect the original right subtree there.

## Final Algorithm

Agent-filled as a concise outline; user should revise if it does not match their understanding.

1. Recursively flatten `root.left` and `root.right` first (post-order).
2. Save `left = root.left`, `right = root.right`; set `root.left = None`, `root.right = left`.
3. Walk `cur` from `root` along `.right` until `cur.right is None` — this is the tail of the newly attached (already-flattened) left chain.
4. Attach `cur.right = right`.
5. Base case: `root is None` returns immediately.

## Correctness Argument

User-filled, with agent prompts if needed.

When processing a node, both its left and right subtrees have already been flattened by recursion. The flattened left subtree contains exactly the preorder sequence of the original left subtree, so its tail is the correct place to attach the original right subtree. Therefore the final order becomes: root → left subtree → right subtree, which is exactly preorder. Applying this at every node produces the correct flattened tree.

## Complexity

Time: this specific implementation is **not** O(n) in the worst case. Each call re-walks the entire newly-attached left chain to find its tail via `while cur.right`. On a left-skewed tree (every node has only a left child), the walk length at depth `k` from the bottom is proportional to `k`, so the total work is `1 + 2 + ... + n = O(n^2)`. On a balanced or right-skewed tree it is closer to O(n), but the worst case is O(n^2).
Space: O(h) recursion stack, where `h` is the tree height (up to O(n) for a skewed tree).

The reference solution avoids this by using an iterative Morris-style walk that finds each node's splice point exactly once overall, giving true O(n) time and O(1) extra space.

## Edge Cases

- Empty tree (`root is None`).
- Single node (no children).
- Left-only chain (every node has only a left child) — the case that exposes the O(n^2) worst case.
- Right-only chain already (no node has a left child) — should be a no-op.
- Mixed left/right children across multiple levels.

## Mistakes I Made

N/A

## How I Will Recognize This Pattern Next Time

A tree problem asks me to modify the tree in place while preserving a traversal order, I will consider solving the subtrees first and then reconnecting them. When one processed subtree should come before another, attaching the second subtree to the tail of the first is a useful pattern to remember.
