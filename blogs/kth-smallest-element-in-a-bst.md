# Kth Smallest Element in a BST

- Problem slug: `kth-smallest-element-in-a-bst`
- Archive path: `archives/2026-07-22-kth-smallest-element-in-a-bst/`

## Problem

Given the root of a binary search tree and an integer `k`, return the `k`th smallest value (1-indexed) among all node values in the tree. `1 <= k <= n` where `n` is the number of nodes, so `k` is always in range.

## My Initial Intuition

_(User-filled: what was your first instinct when you read this problem?)_

## Brute Force

_(User-filled: what's the simplest correct approach, even if not optimal? What's its cost?)_

## Key Insight

_(User-filled: what property of a BST makes this problem solvable, and how does it connect to what you did in validate-binary-search-tree?)_

## Final Algorithm

Recursive inorder traversal that stops as soon as the kth node is visited:

- Recurse into the left subtree first.
- If the left subtree already found the answer (a non-`None` return value), propagate it straight back up without doing any more work.
- Otherwise, increment a visited-node counter for the current node; if the counter now equals `k`, return this node's value.
- Otherwise, recurse into the right subtree and propagate whatever it returns.

## Correctness Argument

_(User-filled, with agent prompts if needed: why does this always return the correct kth value, and never too early or too late?)_

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

_(Add any cases you personally had to think through.)_

## Mistakes I Made

_(User-filled: what actually went wrong while you were writing this, if anything?)_

## How I Will Recognize This Pattern Next Time

_(User-filled: what signal in a future problem should make you reach for this approach?)_
