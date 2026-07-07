# Problem

- Name: Reverse Nodes in k-Group
- Slug: `reverse-nodes-in-k-group`
- Source: https://leetcode.cn/problems/reverse-nodes-in-k-group/description/?envType=study-plan-v2&envId=top-100-liked
- Archive path: `archives/2026-07-07-reverse-nodes-in-k-group/`

## Statement

Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.

## Examples

```text
Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]

Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]
```

## Constraints

- The number of nodes in the list is `n`.
- `1 <= k <= n <= 5000`
- `0 <= Node.val <= 1000`

## Clarifications

- Follow-up (optional): can you solve it in O(1) extra memory space (in-place reversal, no buffering nodes in a list/stack)?

## Input / Output Shape

- Input: `head: Optional[ListNode]`, `k: int`
- Output: `Optional[ListNode]`
