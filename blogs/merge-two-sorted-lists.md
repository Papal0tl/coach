# Merge Two Sorted Lists (LC 21)

## Problem Summary
Given the heads of two sorted linked lists `list1` and `list2`, merge them into one sorted list by splicing together the existing nodes (not creating new ones), and return the head of the merged list.

## Initial Intuition
Creating a new list and repeatedly choosing the smaller value from the two lists. Since both lists are already sorted, it seemed unnecessary to collect all values and sort them again.

## Brute Force
Copy all values from both linked lists into an array, sort the array, then create a brand new linked list from the sorted values.

This works, but it uses extra space for the array and creates new nodes, while the problem allows us to reuse the existing nodes.

Time Complexity: O((n + m) log(n + m))

Space Complexity: O(n + m)

## Key Insight
Both linked lists are already sorted.

At every step, the smaller of the two current head nodes must be the next node in the merged list. We only need to compare the current heads, attach the smaller one, and move that list's pointer forward.

Using a dummy node makes building the result much simpler because we never need to treat the first node as a special case.

## Final Algorithm
1. Create a dummy/sentinel node and a `cur` pointer starting at it, to avoid special-casing the first node of the result.
2. While both `list1` and `list2` have remaining nodes, splice whichever head has the smaller (or equal) value onto `cur.next`, advance that list's pointer, and advance `cur`.
3. Once one list is exhausted, attach the remainder of the other list directly (it's already sorted).
4. Return `dummy.next` (the real head, skipping the sentinel).

```python
class Solution:
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode(0)
        cur = dummy

        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next

        if list1 is not None:
            cur.next = list1
        else:
            cur.next = list2

        return dummy.next
```

## Correctness Argument
At the beginning of every loop iteration, the merged list already contains all previously selected nodes in sorted order.

Since both remaining lists are still individually sorted, the smaller of their two head nodes is the smallest remaining node overall. Appending that node preserves the sorted order of the merged list.

When one list becomes empty, every remaining node in the other list is already greater than or equal to the last node that was appended, so attaching the remaining nodes directly keeps the entire merged list sorted.

## Complexity
Time Complexity: O(n + m), where n and m are the lengths of `list1` and `list2` — each node is visited exactly once.
Space Complexity: O(1) extra space — no new nodes are allocated, only existing nodes are relinked.

## Edge Cases
- Both lists empty → return `None`.
- One list empty, the other non-empty → return the non-empty list unchanged.
- Duplicate values across lists.
- One list's values are entirely smaller or larger than the other's (no interleaving).
- Single-node lists.

## Mistakes Made
- Initially wanted to create completely new nodes instead of reusing the existing ones, but the problem can be solved more efficiently by simply changing the next pointers.
- Forgot that building a linked list needs a pointer (cur) to track the last node of the result. Without it, it is difficult to know where the next node should be attached.
- Didn't realize why a dummy node is useful at first. Without it, the first node of the merged list needs special handling, making the code more complicated.

## How to Recognize This Pattern Next Time
- The input consists of two sorted linked lists.
- The problem asks you to merge them into one sorted list.
- Only ever need to compare the current heads of the two lists.
- The problem allows to reuse the existing nodes instead of creating new ones.
