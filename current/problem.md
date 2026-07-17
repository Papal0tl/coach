# Problem

- Name: Symmetric Tree
- Slug: `symmetric-tree`
- Source: https://leetcode.cn/problems/symmetric-tree/?envType=study-plan-v2&envId=top-100-liked (LeetCode 101)
- Archive path: `archives/2026-07-17-symmetric-tree/`

## Statement

Given the `root` of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

## Examples

```text
Input: root = [1,2,2,3,4,4,3]
Output: true

Input: root = [1,2,2,null,3,null,3]
Output: false
```

## Constraints

- The number of nodes in the tree is in the range `[1, 1000]`.
- `-100 <= Node.val <= 100`

## Clarifications

- Follow-up (from LeetCode): could you solve it both recursively and iteratively?

## Input / Output Shape

- Input: `root: Optional[TreeNode]`, a binary tree given as a LeetCode-style level-order list with `None` gaps.
- Output: `bool` — whether the tree is symmetric around its center.
