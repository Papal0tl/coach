# Construct Binary Tree from Preorder and Inorder Traversal

- Problem slug: `construct-binary-tree-from-preorder-and-inorder-traversal`
- Archive path: `archives/2026-07-28-construct-binary-tree-from-preorder-and-inorder-traversal/`

Write concise bullets or compact paragraphs. Cover every section, but do not pad.

Sections marked `Agent-filled` should be drafted by the coaching agent before the user writes. Sections marked `User-filled` must be written or revised by the user in their own words.

## Problem

Given two integer arrays `preorder` and `inorder`, where `preorder` and `inorder` are the preorder and inorder traversals of the same binary tree (with all node values unique), reconstruct and return the root of that tree.

## My Initial Intuition

User-filled. Guiding question: before you wrote any code, what did you think the first element of `preorder` told you about the tree, and why did you reach for `inorder.index(...)`?

## Brute Force

User-filled. Guiding question: is your submitted solution itself the "brute force" here, or is there a simpler/more naive approach you considered and rejected first? (If your submitted solution *is* the most naive correct approach, say so directly rather than inventing a distinct one.)

## Key Insight

User-filled. Guiding question: what is the relationship between the first value of `preorder` and the value at index `idx` in `inorder`, and why does that value split `inorder` into exactly the left and right subtrees?

## Final Algorithm

Agent-filled as a concise outline; user should revise if it does not match their understanding.

1. Base case: if `preorder` is empty, return `None`.
2. Take `root_val = preorder[0]` — the first element of any preorder slice is always the root of that subtree.
3. Find `idx = inorder.index(root_val)` — everything in `inorder` before `idx` belongs to the left subtree, everything after belongs to the right subtree.
4. Recurse: `root.left = buildTree(preorder[1:idx+1], inorder[:idx])`, `root.right = buildTree(preorder[idx+1:], inorder[idx+1:])`.
5. Return `root`.

## Correctness Argument

User-filled, with agent prompts if needed. Guiding question: why must the left subtree always occupy exactly the first `idx` values after the root in `preorder` (not some other split point)?

## Complexity

Agent-filled; user should confirm they understand it.

Time: O(n^2) worst case. There are n recursive calls; each call does `inorder.index(...)` (O(n) linear search) and builds two new sliced arrays (O(n) copy), so a skewed tree (e.g. every node has only a right child) produces O(n) + O(n-1) + ... = O(n^2) total work.
Space: O(n) for the slice copies across the recursion, plus O(h) recursion stack (up to O(n) on a skewed tree).

A faster O(n) approach precomputes a `value -> index` hash map for `inorder` (O(1) split lookup instead of O(n) `.index()`) and tracks a single shared pointer into `preorder` instead of slicing (O(1) per call instead of O(n) copies).

## Edge Cases

Agent-filled as a checklist; user should add any cases they personally missed.

- Single node (`preorder = [x]`, `inorder = [x]`).
- Left-skewed tree (every node has only a left child).
- Right-skewed tree (every node has only a right child).
- Root with only a left child (asymmetric split where `idx` is the last index).
- Balanced small tree with non-trivial left and right subtrees.

## Mistakes I Made

User-filled.

## How I Will Recognize This Pattern Next Time

User-filled.
