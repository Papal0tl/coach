# Problem

- Name: Maximum Depth of Binary Tree
- Slug: `maximum-depth-of-binary-tree`
- Source: https://leetcode.cn/problems/maximum-depth-of-binary-tree/ (LeetCode 104)
- Archive path: `archives/2026-07-15-maximum-depth-of-binary-tree/`

## Statement

Given the `root` of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

## Examples

Example 1:

```text
Input: root = [3,9,20,null,null,15,7]
Output: 3
```

Example 2:

```text
Input: root = [1,null,2]
Output: 2
```

## Constraints

- The number of nodes in the tree is in the range `[0, 10^4]`.
- `-100 <= Node.val <= 100`

## Clarifications

- None requested yet.

## Input / Output Shape

- Input: `root: Optional[TreeNode]`, using the same `TreeNode` class as the prior binary-tree-inorder-traversal session.
- Output: `int`, the maximum depth (0 for an empty tree).
