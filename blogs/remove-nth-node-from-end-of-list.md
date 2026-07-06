# Remove Nth Node From End of List (LC 19)

## Problem Summary
Given the head of a singly linked list, remove the nth node counting from the end of the list, and return the head of the resulting list. `n` is guaranteed to be between 1 and the length of the list.

## Initial Intuition
User-filled.

## Brute Force
User-filled.

## Key Insight
User-filled.

## Final Algorithm
1. Create a dummy/sentinel node pointing to `head`, so the head itself can be removed without special-casing it.
2. First pass: walk the real list from `head` to count its length.
3. Starting from `dummy`, walk `length - n` steps forward. This lands on the node immediately before the one to remove.
4. Skip the target node: `cur.next = cur.next.next`.
5. Return `dummy.next` (the real head, skipping the sentinel).

```python
class Solution:
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0)
        dummy.next = head
        length = 0
        cur = head

        while cur:
            length += 1
            cur = cur.next

        cur = dummy
        for i in range(length - n):
            cur = cur.next

        cur.next = cur.next.next
        return dummy.next
```

## Correctness Argument
User-filled.

## Complexity
Time Complexity: O(L), where L is the length of the list — one pass to count the length, one pass to walk to the removal point.
Space Complexity: O(1) auxiliary space (only the dummy node and a few pointers).

## Edge Cases
- Removing the head node (`n == length`), handled by the dummy node so `cur` always has a valid predecessor.
- Removing the tail node (`n == 1`).
- Single-node list (`length == 1`, `n == 1`).

## Mistakes Made
User-filled.

## How to Recognize This Pattern Next Time
User-filled.
