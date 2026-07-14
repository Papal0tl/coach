# Binary Tree Inorder Traversal

**Problem**: LC 94 — [Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/)
**Date**: 2026-07-14
**Difficulty**: Easy

---

## Problem Summary

Given the root of a binary tree, return the values of its nodes in inorder order (left subtree, then the node itself, then right subtree) as a flat list.

---

## Initial Intuition

_(Your words: what was your first instinct when you read the problem?)_

---

## Brute Force

_(Your words: is there a distinct "brute force" here, or did you go straight to the natural recursive approach? If the latter, say so — not every problem has a separate brute force.)_

---

## Key Insight

_(Your words: what makes "left, visit, right" the right order to produce a sorted-looking traversal, and why does recursion make this easy to express?)_

---

## Final Algorithm

Recursive DFS:

1. If the current node is `None`, return (base case).
2. Recurse into the left subtree.
3. Append the current node's value to the result.
4. Recurse into the right subtree.

```python
def inorderTraversal(self, root):
    res = []

    def dfs(node):
        if node is None:
            return
        dfs(node.left)
        res.append(node.val)
        dfs(node.right)

    dfs(root)
    return res
```

---

## Correctness Argument

_(Your words: why does visiting left, then the node, then right — recursively at every level — produce values in inorder order for the whole tree, not just at the top level?)_

---

## Complexity

- Time: O(n) — every node is visited exactly once.
- Space: O(h) — recursion call stack depth equals the tree height h (worst case O(n) for a skewed tree, O(log n) for a balanced tree). The output list itself is O(n) but isn't usually counted as "extra" space.

---

## Edge Cases

- Empty tree (`root is None`) → returns `[]`.
- Single node → returns `[node.val]`.
- Left-skewed or right-skewed tree (only one child direction) → degenerates to a linear traversal.
- Root with only a right child, no left child (the problem's own first example, `[1, null, 2, 3]`).

---

## Mistakes Made

_(Your words: what actually went wrong while you were writing this, if anything? If there were zero bugs, say that plainly rather than inventing something.)_

---

## How to Recognize This Pattern Next Time

_(Your words: what's the signal that a problem wants a tree traversal, and what's the signal that an iterative version would need an explicit stack instead of recursion?)_
