# Merge Two Sorted Lists (LC 21)

## Problem Summary
Given the heads of two sorted linked lists `list1` and `list2`, merge them into one sorted list by splicing together the existing nodes (not creating new ones), and return the head of the merged list.

## Initial Intuition
<!-- Write in your own words: what was your first idea when you saw this problem? -->

## Brute Force
<!-- Write in your own words: is there a less efficient approach you considered (e.g. collect all values, sort, rebuild)? How does it compare to your final solution? -->

## Key Insight
<!-- Write in your own words: what's the core idea that makes the efficient solution work? -->

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
<!-- Write in your own words: why does this produce a fully sorted list? Consider the state of the result at any point in the loop, and why attaching the leftover tail at the end preserves sortedness. -->

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
<!-- Write in your own words: what bugs did you actually hit while writing this, and what was the real fix? Be precise about cause and effect. -->

## How to Recognize This Pattern Next Time
<!-- Write in your own words: what cues in a problem statement point to this two-pointer merge + dummy-node technique? -->
