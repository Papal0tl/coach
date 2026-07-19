# Problem

- Name: Binary Tree Level Order Traversal
- Slug: `binary-tree-level-order-traversal`
- Source: https://leetcode.cn/problems/binary-tree-level-order-traversal/?envType=study-plan-v2&envId=top-100-liked
- Archive path: `archives/2026-07-18-binary-tree-level-order-traversal/`

## Statement

Given the `root` of a binary tree, return the level order traversal of its nodes' values (i.e., from left to right, level by level).

## Examples

**Example 1:**

```
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
```

**Example 2:**

```
Input: root = [1]
Output: [[1]]
```

**Example 3:**

```
Input: root = []
Output: []
```

## Constraints

- The number of nodes in the tree is in the range `[0, 2000]`.
- `-1000 <= Node.val <= 1000`

## Clarifications

- Output is grouped by level: one inner list per depth, in top-to-bottom order.
- Within each level, values are ordered left to right.

## Input / Output Shape

- Input: `root: Optional[TreeNode]`
- Output: `List[List[int]]` — node values grouped by level
