# Problem

- Name: Validate Binary Search Tree
- Slug: `validate-binary-search-tree`
- Source: https://leetcode.cn/problems/validate-binary-search-tree/description/?envType=study-plan-v2&envId=top-100-liked
- Archive path: `archives/2026-07-22-validate-binary-search-tree/`

## Statement

Given the `root` of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

- The left subtree of a node contains only nodes with keys strictly less than the node's key.
- The right subtree of a node contains only nodes with keys strictly greater than the node's key.
- Both the left and right subtrees must also be binary search trees.

## Examples

**Example 1:**

```
Input: root = [2,1,3]
Output: true
```

**Example 2:**

```
Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
```

## Constraints

- The number of nodes in the tree is in the range `[1, 10^4]`.
- `-2^31 <= Node.val <= 2^31 - 1`

## Clarifications

- "Valid BST" is a global property, not just parent-child comparison: every node in a left subtree must be strictly less than the node above it, not only its immediate parent.
- Values are `int`s within the given range; duplicates are not valid (strict inequality required).

## Input / Output Shape

- Input: `root: Optional[TreeNode]`
- Output: `bool`
