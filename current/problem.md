# Problem

- Name: Sort List
- Slug: `sort-list`
- Source: https://leetcode.cn/problems/sort-list/description/?envType=study-plan-v2&envId=top-100-liked (LeetCode 148)
- Archive path: (to be assigned at closeout)

## Statement

Given the `head` of a singly linked list, return the list after sorting it in ascending order.

## Examples

**Example 1**

Input: `head = [4,2,1,3]`
Output: `[1,2,3,4]`

**Example 2**

Input: `head = [-1,5,3,4,0]`
Output: `[-1,0,3,4,5]`

**Example 3**

Input: `head = []`
Output: `[]`

## Constraints

- The number of nodes in the list is in the range `[0, 5 * 10^4]`.
- `-10^5 <= Node.val <= 10^5`

## Follow-up

Can you sort the linked list in `O(n log n)` time and `O(1)` memory (i.e. constant space)?

## Clarifications

None requested yet.

## Input / Output Shape

- Input: `head` — the head of a singly linked list where each `ListNode` has `val: int`, `next: Optional[ListNode]`.
- Output: the head of the same list, sorted in ascending order by `val`.
