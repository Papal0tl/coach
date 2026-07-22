# Problem

- Name: Kth Smallest Element in a BST
- Slug: `kth-smallest-element-in-a-bst`
- Source: https://leetcode.cn/problems/kth-smallest-element-in-a-bst/description/?envType=study-plan-v2&envId=top-100-liked
- Archive path: `archives/2026-07-22-kth-smallest-element-in-a-bst/`

## Statement

Given the root of a binary search tree, and an integer `k`, return the `k`th smallest value (1-indexed) among all the values of the nodes in the tree.

## Examples

Example 1:

```text
Input: root = [3,1,4,null,2], k = 1
Output: 1
```

Example 2:

```text
Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3
```

## Constraints

- The number of nodes in the tree is `n`.
- `1 <= k <= n <= 10^4`
- `0 <= Node.val <= 10^4`

## Clarifications

- Follow-up (optional, not required for the base solution): the BST may be modified (insert/delete) frequently and you need to find the kth smallest value in `O(h)` time, where `h` is the tree height. Note this is available as a stretch/follow-up but is not required to close the session.

## Input / Output Shape

- Input: `root: Optional[TreeNode]`, `k: int`
- Output: `int` — the value of the kth smallest node
