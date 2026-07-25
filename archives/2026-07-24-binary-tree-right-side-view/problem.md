# Problem

- Name: Binary Tree Right Side View
- Slug: `binary-tree-right-side-view`
- Source: https://leetcode.cn/problems/binary-tree-right-side-view/ (LeetCode 199)
- Archive path: `archives/2026-07-24-binary-tree-right-side-view/`

## Statement

Given the `root` of a binary tree, imagine yourself standing on the right side of it. Return the values of the nodes you can see, ordered from top to bottom.

## Examples

Example 1:

```text
Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]
```

Example 2:

```text
Input: root = [1,null,3]
Output: [1,3]
```

Example 3:

```text
Input: root = []
Output: []
```

## Constraints

- The number of nodes in the tree is in the range `[0, 100]`.
- `-100 <= Node.val <= 100`

## Clarifications

None yet.

## Input / Output Shape

- Input: `root: Optional[TreeNode]`
- Output: `List[int]`, one value per level, the rightmost node at each depth, ordered top to bottom.
