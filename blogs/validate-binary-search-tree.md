# Validate Binary Search Tree

- Problem slug: `validate-binary-search-tree`
- Archive path: `archives/2026-07-20-validate-binary-search-tree/`

Write concise bullets or compact paragraphs. Cover every section, but do not pad.

Sections marked `Agent-filled` should be drafted by the coaching agent before the user writes. Sections marked `User-filled` must be written or revised by the user in their own words.

## Problem

Given the root of a binary tree, determine whether it is a valid BST: every node's left subtree must contain only values strictly less than the node, every right subtree only values strictly greater, and this must hold recursively for every subtree (not just the immediate parent-child pair).

## My Initial Intuition

Use inorder traversal because I remembered that the inorder traversal of a BST is sorted. The idea was to visit nodes in left → root → right order and compare each value with the previously visited one. If the sequence was no longer strictly increasing, the tree could not be a valid BST.

## Brute Force

Checking every node against all values in its left and right subtrees => repeatedly traverse subtrees, leading to about O(n²) time in the worst case.

## Key Insight

An inorder traversal of a valid BST always produces a strictly increasing sequence. Instead of checking every ancestor explicitly, only need to compare each visited node with the previously visited value.

## Final Algorithm

Agent-filled as a concise outline; user should revise if it does not match their understanding.

Inorder traversal of a valid BST visits values in strictly increasing order. Track `self.prev`, initialized to `float("-inf")`. Recursive helper `inorder(node)`: if `node` is `None`, return `True`. Recurse into `inorder(node.left)`; if it returns `False`, propagate `False`. Otherwise check `node.val <= self.prev` — if true, the sequence isn't strictly increasing, return `False`. Update `self.prev = node.val`, then recurse into `inorder(node.right)` and return its result. Top-level call is `inorder(root)`.

## Correctness Argument

- Base case: An empty subtree returns True, so it is a valid BST.
- Inductive Case: Assume the left and right recursive calls correctly validate their subtrees. During inorder traversal, every visited value must be greater than self.prev. If any value is not strictly greater, the BST property is violated and the algorithm returns False. Otherwise every visited value is in increasing order, so the entire tree satisfies the BST property.

## Complexity

Agent-filled; user should confirm they understand it.

Time: O(n) — each node is visited exactly once.
Space: O(h) additional space for the recursion call stack, where h is the tree height (O(log n) balanced, O(n) worst-case skewed), not counting the input tree itself.

## Edge Cases

Agent-filled as a checklist; user should add any cases they personally missed.

- Single node -> valid BST, trivially.
- Duplicate values anywhere in the tree -> invalid, since the property requires strict inequality (`<=` check catches this).
- Values at the 32-bit int boundary (`2^31 - 1`, `-2^31`) -> handled correctly since `self.prev` starts at `float("-inf")`, which is strictly less than any valid int, avoiding a sentinel-collision bug.
- A node that satisfies its immediate parent but violates an ancestor further up (e.g. `[5,4,6,None,None,3,7]`, where 3 is under 6 but 3 < 5) -> caught because the inorder sequence itself becomes non-increasing, not because of any per-parent comparison.
- Fully skewed (left-only or right-only) trees -> still O(n) time; recursion depth becomes O(n).

## Mistakes I Made

- Wrote return inorder(node.left) at the end instead of node.right, so the recursion revisited the left subtree and never checked the right subtree.
- Before tracing the recursion carefully, didn't notice that the final recursive call was going to the wrong subtree.
- Focused on the comparison logic (self.prev) instead of verifying that the traversal order itself was correct.

## How I Will Recognize This Pattern Next Time

Asks whether a tree is a valid BST (not to modify it), checking whether the inorder sequence is strictly increasing is often the simplest solution.
