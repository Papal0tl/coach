# Problem

- Name: Construct Binary Tree from Preorder and Inorder Traversal
- Slug: `construct-binary-tree-from-preorder-and-inorder-traversal`
- Source: https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/?envType=study-plan-v2&envId=top-100-liked (LeetCode 105)
- Archive path: `archives/2026-07-28-construct-binary-tree-from-preorder-and-inorder-traversal/`

## Statement

Given two integer arrays `preorder` and `inorder` where `preorder` is the preorder traversal of a binary tree and `inorder` is the inorder traversal of the same tree, construct and return the binary tree.

## Examples

Example 1:

```text
Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]
```

Example 2:

```text
Input: preorder = [-1], inorder = [-1]
Output: [-1]
```

## Constraints

- `1 <= preorder.length <= 3000`
- `inorder.length == preorder.length`
- `-3000 <= preorder[i], inorder[i] <= 3000`
- `preorder` and `inorder` consist of unique values.
- Each value of `inorder` also appears in `preorder`.
- `preorder` is guaranteed to be the preorder traversal of the tree.
- `inorder` is guaranteed to be the inorder traversal of the tree.

## Clarifications

- Values are unique across the tree, so a value can be used to locate a node's position in `inorder` unambiguously.

## Input / Output Shape

- Input: `preorder: List[int]`, `inorder: List[int]`
- Output: `Optional[TreeNode]` (root of the constructed tree)
