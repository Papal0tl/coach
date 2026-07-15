# Problem

- Name: Invert Binary Tree
- Slug: `invert-binary-tree`
- Source: https://leetcode.cn/problems/invert-binary-tree/description/?envType=study-plan-v2&envId=top-100-liked
- Archive path: `archives/2026-07-15-invert-binary-tree/`

## Statement

Given the root of a binary tree, invert the tree (mirror it: swap every node's left and right child), and return its root.

## Examples

Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

Input: root = [2,1,3]
Output: [2,3,1]

Input: root = []
Output: []

## Constraints

- The number of nodes in the tree is in the range [0, 100].
- -100 <= Node.val <= 100

## Clarifications

None needed; standard LeetCode 226 statement.

## Input / Output Shape

- Input: `root: Optional[TreeNode]`
- Output: `Optional[TreeNode]` (the same root, now inverted, or `None` for an empty tree)
