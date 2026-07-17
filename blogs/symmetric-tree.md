# Symmetric Tree

- Problem slug: `symmetric-tree`
- Archive path: `archives/2026-07-17-symmetric-tree/`

Write concise bullets or compact paragraphs. Cover every section, but do not pad.

Sections marked `Agent-filled` should be drafted by the coaching agent before the user writes. Sections marked `User-filled` must be written or revised by the user in their own words.

## Problem

Given the root of a binary tree, check whether it is a mirror of itself (symmetric around its center).

## My Initial Intuition

User-filled.

## Brute Force

User-filled.

## Key Insight

User-filled.

## Final Algorithm

Agent-filled as a concise outline; user should revise if it does not match their understanding.

Define a nested/helper function `compare(left, right)` (or `is_mirror(t1, t2)`) that checks whether two subtrees are mirror images of each other: return `True` if both are `None`; return `False` if exactly one is `None`; return `False` if their values differ; otherwise return `compare(left.left, right.right) and compare(left.right, right.left)` — comparing children *crossed*, not in parallel. `isSymmetric(root)` returns `True` immediately if `root is None`, otherwise returns `compare(root.left, root.right)`.

## Correctness Argument

User-filled, with agent prompts if needed.

## Complexity

Agent-filled; user should confirm they understand it.

Time: O(n) — every node is visited exactly once across the whole call tree.
Space: O(h) — the recursion call stack grows with the tree's height h. O(log n) for a balanced tree, O(n) worst case for a fully skewed (chain-like) tree.

## Edge Cases

Agent-filled as a checklist; user should add any cases they personally missed.

- Empty tree (`root = None`) -> symmetric, `True`.
- Single node -> symmetric, `True` (no children to compare).
- Symmetric values but different shape (e.g. one side has a child the other lacks) -> `False`.
- Equal values across subtrees that are not actually mirrored in structure -> `False` (value equality alone is not sufficient).

## Mistakes I Made

User-filled.

## How I Will Recognize This Pattern Next Time

User-filled.
