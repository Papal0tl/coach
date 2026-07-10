# Sort List (LC 148)

## Problem Summary
Given the head of a singly linked list, return the list after sorting it in ascending order by node value. Follow-up: do it in O(n log n) time and O(1) extra space.

## Initial Intuition
<!-- Your words: what was your first idea when you read this problem, before you knew it wouldn't work or would need refining? -->

## Brute Force
<!-- Your words: describe a valid but non-optimal approach (e.g. dumping values into an array, sorting, rebuilding the list) and its complexity. -->

## Key Insight
<!-- Your words: why doesn't an array-style sort transfer directly to a linked list, and what makes merge sort the natural fit here? -->

## Final Algorithm
1. Base case: if `head` is `None` or `head.next` is `None`, return `head` unchanged (already sorted).
2. Split: use a fast/slow pointer walk to find a cut point, then sever the list into two independent halves.
3. Recurse: sort each half with the same function.
4. Merge: combine the two sorted halves into one sorted list (same merge routine as merge-two-sorted-lists).
5. Return the merged, fully sorted list.

```python
class Solution:
    def sortList(self, head):
        if head is None or head.next is None:
            return head
        prev = None
        fast = head
        slow = head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = None
        left = head
        right = slow
        left = self.sortList(left)
        right = self.sortList(right)
        dummy = ListNode(0)
        cur = dummy
        while left and right:
            if left.val <= right.val:
                cur.next = left
                left = left.next
                cur = cur.next
            else:
                cur.next = right
                right = right.next
                cur = cur.next
        if left:
            cur.next = left
        else:
            cur.next = right
        return dummy.next
```

## Correctness Argument
<!-- Your words: why does the base case guarantee a sorted result, and why does merging two sorted halves always produce a sorted whole? -->

## Complexity
Time Complexity: O(n log n) — each of the O(log n) levels of recursion does O(n) total work merging.
Space Complexity: O(log n) — the recursion stack depth, since this is the recursive (not the O(1)-space iterative) variant.

## Edge Cases
- Empty list (`head = None`): returns `None` immediately.
- Single node: returns as-is via the base case.
- Two-node list: exercises the split logic at its smallest non-trivial size.
- Duplicate values: merge must not drop or reorder ties.
- Already sorted or reverse-sorted input: correctness doesn't depend on initial order.

## Mistakes I Made
<!-- Your words: what actually went wrong along the way, in the order it happened. Check the git log for `sort-list` commits if you want to jog your memory — don't invent or omit steps. -->

## How I Will Recognize This Pattern Next Time
<!-- Your words: what's the general signal that should make you reach for merge sort (or this split+recurse+merge shape) on a future problem? -->
