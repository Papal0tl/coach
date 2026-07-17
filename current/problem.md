# Problem

- Name: Diameter of Binary Tree
- Slug: `diameter-of-binary-tree`
- Source: https://leetcode.cn/problems/diameter-of-binary-tree/description/?envType=study-plan-v2&envId=top-100-liked
- Archive path: `archives/2026-07-17-diameter-of-binary-tree/`

## Statement

Given the `root` of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the `root`.

The length of a path between two nodes is represented by the number of edges between them.

## Examples

**Example 1:**

```
Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
```

**Example 2:**

```
Input: root = [1,2]
Output: 1
```

## Constraints

- The number of nodes in the tree is in the range `[1, 10^4]`.
- `-100 <= Node.val <= 100`

## Clarifications

- "Length" is measured in edges, not nodes.
- The longest path does not need to pass through the root.

## Input / Output Shape

- Input: `root: Optional[TreeNode]`
- Output: `int` — the diameter (max edge count between any two nodes)
