# Invert Binary Tree

- Problem slug: `invert-binary-tree`
- Archive path: `archives/2026-07-15-invert-binary-tree/`

Write concise bullets or compact paragraphs. Cover every section, but do not pad.

Sections marked `Agent-filled` should be drafted by the coaching agent before the user writes. Sections marked `User-filled` must be written or revised by the user in their own words.

## Problem

Given the root of a binary tree, invert the tree (mirror it: swap every node's left and right child), and return its root.

## My Initial Intuition

Swap each node's left and right children. Since every node needs the same operation, recursion seemed like the most natural way to visit the entire tree.

## Brute Force

The recursive DFS approach is already straightforward and visits each node exactly once, so I went directly to that solution.

## Key Insight

The same operation applies to every node: swap its two children, then do the same for each child subtree. Because the tree is modified in place, the recursive calls directly update the existing child subtrees, so there is no need to build a new tree.

## Final Algorithm

Agent-filled as a concise outline; user should revise if it does not match their understanding.

Recursive DFS that mutates in place: `invertTree(node)` returns `None` if `node is None`. Otherwise, swap `node.left` and `node.right`, then recursively call `invertTree` on each (now-swapped) child to invert their subtrees in place, and return `node`. Because the recursion mutates the actual child node objects, the recursive calls' return values don't need to be reassigned back — the swap already repointed `node.left`/`node.right` at the correct children, and recursion finishes inverting each subtree in place.

## Correctness Argument

Prove correctness by induction on the size of the subtree. The base case is an empty subtree, which is already inverted. For a non-empty node, the algorithm first swaps its left and right children, then recursively inverts both child subtrees. By the induction hypothesis, each child subtree is correctly inverted, so the entire subtree rooted at the current node is the mirror image of the original. Therefore, the algorithm correctly inverts the whole tree.

## Complexity

Time: O(n) — every node is visited exactly once.
Space: O(h) — the recursion call stack grows with the tree's height h. O(log n) for a balanced tree, O(n) worst case for a fully skewed (chain-like) tree.

## Edge Cases

- Empty tree (`root = None`) -> returns `None`.
- Single node -> returns itself unchanged (no children to swap).
- Left-skewed or right-skewed tree -> skew direction flips.
- Symmetric tree -> structure unchanged but still correctly mirrored (values may still move).

## Mistakes I Made
N/A

## How I Will Recognize This Pattern Next Time

If every node in a tree requires the same operation and the result for a node depends only on applying that same operation to its children, I will consider recursive DFS. When the modification can be done in place, do not need to build a new tree.
