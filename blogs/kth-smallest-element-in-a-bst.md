# Kth Smallest Element in a BST

- Problem slug: `kth-smallest-element-in-a-bst`
- Archive path: `archives/2026-07-22-kth-smallest-element-in-a-bst/`

## Problem

Given the root of a binary search tree and an integer `k`, return the `k`th smallest value (1-indexed) among all node values in the tree. `1 <= k <= n` where `n` is the number of nodes, so `k` is always in range.

## My Initial Intuition

Perform an inorder traversal, store every value in a list, and return `values[k - 1]`. Since I already knew that inorder traversal of a BST produces values in sorted order, this immediately gives the kth smallest element.

Didn't actually need to build the whole list. Since the traversal is already visiting nodes in ascending order, could simply count how many nodes had been visited and stop as soon as the kth node was reached.

## Brute Force

Perform an inorder traversal of the BST, append every visited value to a list, then return `values[k - 1]`.

- Time: O(n)
- Space: O(n)

Although correct, this always traverses and stores every node, even if `k` is very small.

## Key Insight

The key property is that an inorder traversal of a Binary Search Tree visits nodes in strictly increasing order.

In the previous BST validation problem, used inorder traversal to verify that the visited values were increasing. Here, reuse exactly the same property, but instead of checking the ordering, count how many nodes have been visited. The kth visited node is therefore the kth smallest value.

## Final Algorithm

Recursive inorder traversal that stops as soon as the kth node is visited:

- Recurse into the left subtree first.
- If the left subtree already found the answer (a non-`None` return value), propagate it straight back up without doing any more work.
- Otherwise, increment a visited-node counter for the current node; if the counter now equals `k`, return this node's value.
- Otherwise, recurse into the right subtree and propagate whatever it returns.

## Correctness Argument

Because an inorder traversal of a Binary Search Tree visits nodes in increasing order, the nodes are visited from the smallest value to the largest.

The algorithm counts each visited node. When the counter reaches `k`, the current node is exactly the kth smallest value, so returning it is correct.

## Complexity

- Time: O(h + k), where `h` is the tree height — reaching the leftmost node costs O(h), and at most `k` nodes are visited (via the counter) before an early return, with no wasted work once found.
- Space: O(h) for the recursion call stack.
- Compared to collecting every value via inorder traversal into a list and indexing `[k-1]`: that approach is O(n) time and O(n) space, since it visits and stores every node regardless of `k`.

## Edge Cases

- Single-node tree (`k == 1 == n`).
- `k == 1` (smallest value, leftmost node).
- `k == n` (largest value, rightmost node in inorder order).
- Left-skewed or right-skewed trees.
- `k` in the middle of a tree with multiple levels on both sides.

## Mistakes I Made

N/A

## How I Will Recognize This Pattern Next Time

See a Binary Search Tree problem asking for the kth smallest/largest element, sorted order, or "next" value, should immediately think about inorder traversal.

If only need one position in that ordering instead of the entire sequence, consider counting during traversal and returning early instead of storing every value.
