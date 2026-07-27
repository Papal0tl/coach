# Problem

- Name: Flatten Binary Tree to Linked List
- Slug: `flatten-binary-tree-to-linked-list`
- Source: https://leetcode.cn/problems/flatten-binary-tree-to-linked-list/description/?envType=study-plan-v2&envId=top-100-liked (LeetCode 114)
- Archive path: `archives/2026-07-27-flatten-binary-tree-to-linked-list/`

## Statement

Given the `root` of a binary tree, flatten the tree into a "linked list":

- The "linked list" should use the same `TreeNode` class, where the `right` child pointer points to the next node in the list and the `left` child pointer is always `null`.
- The "linked list" should be in the same order as a **pre-order** traversal of the binary tree.

The transformation must be done in place (mutate the existing tree structure; do not return a new structure).

## Examples

Example 1:

```text
Input: root = [1,2,5,3,4,null,6]
Output: [1,null,2,null,3,null,4,null,5,null,6]
```

Example 2:

```text
Input: root = []
Output: []
```

Example 3:

```text
Input: root = [0]
Output: [0]
```

## Constraints

- The number of nodes in the tree is in the range `[0, 2000]`.
- `-100 <= Node.val <= 100`

## Clarifications

- "In place" here conventionally means: reuse existing nodes and only `left`/`right` pointers; recursion stack space is allowed (the follow-up asks whether it can be done with O(1) *extra* space beyond the recursion/implicit stack).

## Input / Output Shape

- Input: `root: Optional[TreeNode]`
- Output: `None` (the tree is mutated in place; graders typically serialize the tree after the call to check order)
