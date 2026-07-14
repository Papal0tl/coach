# Binary Tree Inorder Traversal

**Problem**: LC 94 — [Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/)
**Date**: 2026-07-14
**Difficulty**: Easy

---

## Problem Summary

Given the root of a binary tree, return the values of its nodes in inorder order (left subtree, then the node itself, then right subtree) as a flat list.

---

## Initial Intuition

A standard inorder traversal. Required order is "left, node, right," use recursion to implement it.

---

## Brute Force

The standard recursive DFS visits each node exactly once, which is optimal in both simplicity and time complexity.

---

## Key Insight

Traversal order: "left subtree → current node → right subtree." Since every subtree follows the same rule, recursion naturally solves the problem by applying the same steps to each subtree until reaching an empty node.

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

The recursive function first completely traverses the left subtree, then visits the current node, and finally traverses the right subtree. Since every subtree is processed using the same left-node-right order, the entire tree is visited in inorder.

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

N/A

---

## How to Recognize This Pattern Next Time

Asks for preorder, inorder, or postorder traversal of a tree => a strong signal to use DFS. 
If recursion is not allowed or the tree is very deep, the same traversal can be implemented iteratively using an explicit stack instead of the recursion call stack.
