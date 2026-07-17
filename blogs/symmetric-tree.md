# Symmetric Tree

- Problem slug: `symmetric-tree`
- Archive path: `archives/2026-07-17-symmetric-tree/`

Write concise bullets or compact paragraphs. Cover every section, but do not pad.

Sections marked `Agent-filled` should be drafted by the coaching agent before the user writes. Sections marked `User-filled` must be written or revised by the user in their own words.

## Problem

Given the root of a binary tree, check whether it is a mirror of itself (symmetric around its center).

## My Initial Intuition

Simply compare root.left and root.right. If they were equal, return True; otherwise, return False. Then realized that checking whether two node objects are equal does not tell whether the whole tree is symmetric.

## Brute Force

Serialize the left and right subtrees and compare whether one is the mirror of the other => Requires extra space to store the traversal results. A recursive mirror comparison is simpler and uses the tree structure directly.

## Key Insight

Symmetry means mirror, not equality. Instead of comparing left with left and right with right, need to compare the left subtree's left child with the right subtree's right child, and the left subtree's right child with the right subtree's left child. The recursive helper function naturally checks this mirror relationship.

## Final Algorithm

Agent-filled as a concise outline; user should revise if it does not match their understanding.

Define a nested/helper function `compare(left, right)` (or `is_mirror(t1, t2)`) that checks whether two subtrees are mirror images of each other: return `True` if both are `None`; return `False` if exactly one is `None`; return `False` if their values differ; otherwise return `compare(left.left, right.right) and compare(left.right, right.left)` — comparing children *crossed*, not in parallel. `isSymmetric(root)` returns `True` immediately if `root is None`, otherwise returns `compare(root.left, root.right)`.

## Correctness Argument

The helper function correctly determines whether two subtrees are mirror images. If both nodes are None, they are symmetric. If only one is None or their values differ, they cannot be symmetric. Otherwise, the current nodes match, and the function recursively checks the outer pair (left.left vs. right.right) and the inner pair (left.right vs. right.left). Therefore, it returns True if and only if the entire tree is symmetric.

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

- First tried comparing root.left == root.right, but that only compares the two node objects instead of checking whether the subtrees are mirrors.
- Put the recursive calls after return True / return False, so they never executed because the function had already returned.
- Tried calling self.isSymmetric(root.left) instead of writing a helper function that compares two nodes at the same time.
- After rewriting the base cases, I used left and right without defining them, which caused NameError: name 'left' is not defined.
- After adding the crossed compare(...) calls, the final return line was indented at the class-body level instead of inside isSymmetric, which caused SyntaxError: 'return' outside function.
- I forgot to handle root is None before accessing root.left and root.right, which caused an AttributeError.

## How I Will Recognize This Pattern Next Time

A tree problem asks whether two parts are mirrors or symmetric => writing a helper function that takes two nodes instead of one. Mirror problems compare children crosswise (left.left with right.right, and left.right with right.left) rather than in parallel.
