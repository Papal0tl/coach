# Problem

- Name: Binary Tree Inorder Traversal
- Slug: `binary-tree-inorder-traversal`
- Source: https://leetcode.cn/problems/binary-tree-inorder-traversal/?envType=study-plan-v2&envId=top-100-liked (LeetCode 94, top-100-liked study plan)
- Archive path: `archives/2026-07-14-binary-tree-inorder-traversal/`

## Statement

Given the `root` of a binary tree, return the inorder traversal of its nodes' values.

## Examples

Input: `root = [1,null,2,3]`
Output: `[1,3,2]`

Input: `root = []`
Output: `[]`

Input: `root = [1]`
Output: `[1]`

## Constraints

- The number of nodes in the tree is in the range `[0, 100]`.
- `-100 <= Node.val <= 100`

## Clarifications

- Follow-up (official): the recursive solution is trivial — can you do it iteratively?

## Input / Output Shape

- Input: `root: Optional[TreeNode]`, using the standard LeetCode `TreeNode` definition (`val`, `left`, `right`).
- Output: `List[int]` — node values in inorder order (left, node, right).
