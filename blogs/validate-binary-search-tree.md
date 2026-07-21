# Validate Binary Search Tree

- Problem slug: `validate-binary-search-tree`
- Archive path: `archives/2026-07-20-validate-binary-search-tree/`

Write concise bullets or compact paragraphs. Cover every section, but do not pad.

Sections marked `Agent-filled` should be drafted by the coaching agent before the user writes. Sections marked `User-filled` must be written or revised by the user in their own words.

## Problem

Given the root of a binary tree, determine whether it is a valid BST: every node's left subtree must contain only values strictly less than the node, every right subtree only values strictly greater, and this must hold recursively for every subtree (not just the immediate parent-child pair).

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

Inorder traversal of a valid BST visits values in strictly increasing order. Track `self.prev`, initialized to `float("-inf")`. Recursive helper `inorder(node)`: if `node` is `None`, return `True`. Recurse into `inorder(node.left)`; if it returns `False`, propagate `False`. Otherwise check `node.val <= self.prev` — if true, the sequence isn't strictly increasing, return `False`. Update `self.prev = node.val`, then recurse into `inorder(node.right)` and return its result. Top-level call is `inorder(root)`.

## Correctness Argument

User-filled, with agent prompts if needed.

{{correctness_argument}}

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

User-filled.

{{mistakes}}

## How I Will Recognize This Pattern Next Time

User-filled.

{{pattern_recognition}}
