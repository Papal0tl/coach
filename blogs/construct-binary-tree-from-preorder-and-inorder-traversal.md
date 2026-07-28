# Construct Binary Tree from Preorder and Inorder Traversal

- Problem slug: `construct-binary-tree-from-preorder-and-inorder-traversal`
- Archive path: `archives/2026-07-28-construct-binary-tree-from-preorder-and-inorder-traversal/`

Write concise bullets or compact paragraphs. Cover every section, but do not pad.

Sections marked `Agent-filled` should be drafted by the coaching agent before the user writes. Sections marked `User-filled` must be written or revised by the user in their own words.

## Problem

Given two integer arrays `preorder` and `inorder`, where `preorder` and `inorder` are the preorder and inorder traversals of the same binary tree (with all node values unique), reconstruct and return the root of that tree.

## My Initial Intuition

The first value in preorder had to be the root because preorder always visits the root first. Then used inorder.index(root) to find where the root appears so I could split the tree into its left and right subtrees.

## Brute Force

The recursive solution is the straightforward correct approach. For each subtree, find the root with preorder[0], search for it in inorder, split both arrays, and recursively build the left and right subtrees.

## Key Insight

The first value in `preorder` is always the root of the current subtree. In `inorder`, everything before the root belongs to the left subtree, and everything after it belongs to the right subtree. The size of the left subtree tells me exactly how to split the remaining `preorder` values.

## Final Algorithm

Agent-filled as a concise outline; user should revise if it does not match their understanding.

1. Base case: if `preorder` is empty, return `None`.
2. Take `root_val = preorder[0]` — the first element of any preorder slice is always the root of that subtree.
3. Find `idx = inorder.index(root_val)` — everything in `inorder` before `idx` belongs to the left subtree, everything after belongs to the right subtree.
4. Recurse: `root.left = buildTree(preorder[1:idx+1], inorder[:idx])`, `root.right = buildTree(preorder[idx+1:], inorder[idx+1:])`.
5. Return `root`.

## Correctness Argument

The first value in `preorder` is always the root. In `inorder`, the root splits the nodes into the left and right subtrees. If the left subtree has `idx` nodes, then the next idx values in `preorder` must belong to the left subtree because preorder always visits the entire left subtree before the right subtree. Therefore each recursive call receives the correct preorder and inorder slices, so every subtree is built correctly.

## Complexity

Time: O(n^2) worst case. There are n recursive calls; each call does `inorder.index(...)` (O(n) linear search) and builds two new sliced arrays (O(n) copy), so a skewed tree (e.g. every node has only a right child) produces O(n) + O(n-1) + ... = O(n^2) total work.
Space: O(n) for the slice copies across the recursion, plus O(h) recursion stack (up to O(n) on a skewed tree).

A faster O(n) approach precomputes a `value -> index` hash map for `inorder` (O(1) split lookup instead of O(n) `.index()`) and tracks a single shared pointer into `preorder` instead of slicing (O(1) per call instead of O(n) copies).

## Edge Cases

- Single node (`preorder = [x]`, `inorder = [x]`).
- Left-skewed tree (every node has only a left child).
- Right-skewed tree (every node has only a right child).
- Root with only a left child (asymmetric split where `idx` is the last index).
- Balanced small tree with non-trivial left and right subtrees.

## Mistakes I Made

- I initially used `inorder[idx:]` for the right subtree instead of `inorder[idx+1:]`. This mistakenly included the root value in the right subtree's inorder traversal, so the recursive split was incorrect. The right subtree should start after the root, not at the root itself.

## How I Will Recognize This Pattern Next Time

- preorder[0] is the root.
- Find the root in inorder to determine the left and right subtrees.
- Use the left subtree's size to split the remaining preorder values, then recursively build both subtrees.
