# Problem

- Name: Merge k Sorted Lists
- Slug: `merge-k-sorted-lists`
- Source: https://leetcode.cn/problems/merge-k-sorted-lists/description/?envType=study-plan-v2&envId=top-100-liked (LeetCode 23)
- Archive path: `archives/2026-07-10-merge-k-sorted-lists/`

## Statement

You are given an array of `k` linked-lists `lists`, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

## Examples

```text
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6

Input: lists = []
Output: []

Input: lists = [[]]
Output: []
```

## Constraints

- `k == lists.length`
- `0 <= k <= 10^4`
- `0 <= lists[i].length <= 500`
- `-10^4 <= lists[i][j] <= 10^4`
- `lists[i]` is sorted in ascending order.
- The sum of `lists[i].length` will not exceed `10^4`.

## Clarifications

- Standard singly-linked list, `ListNode` with `val` and `next`.
- Return the head of the fully merged, sorted list.

## Input / Output Shape

- Input: `lists: List[Optional[ListNode]]`
- Output: `Optional[ListNode]`
