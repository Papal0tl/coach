# Problem

- Name: Convert Sorted Array to Binary Search Tree
- Slug: `convert-sorted-array-to-binary-search-tree`
- Source: https://leetcode.cn/problems/convert-sorted-array-to-binary-search-tree/description/?envType=study-plan-v2&envId=top-100-liked
- Archive path: `archives/2026-07-19-convert-sorted-array-to-binary-search-tree/`

## Statement

Given an integer array `nums` where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.

A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.

## Examples

**Example 1:**

```
Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-1,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted. Multiple height-balanced BSTs are valid.
```

**Example 2:**

```
Input: nums = [1,3]
Output: [3,1]
Explanation: [1,null,3] is also accepted.
```

## Constraints

- `1 <= nums.length <= 10^4`
- `-10^4 <= nums[i] <= 10^4`
- `nums` is sorted in a strictly increasing order.

## Clarifications

- Any valid height-balanced BST is accepted; the judge does not require a specific tree shape.
- Values are unique (strictly increasing input).

## Input / Output Shape

- Input: `nums: List[int]`
- Output: `Optional[TreeNode]` — root of a height-balanced BST
