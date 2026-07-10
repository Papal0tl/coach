"""
Reference solution for Sort List (LC 148).

Approach: merge sort.
1. Split the list into two halves using fast/slow pointers.
2. Recursively sort each half.
3. Merge the two sorted halves (same merge routine as merge-two-sorted-lists).

Recursion depth is O(log n), so this is O(n log n) time, O(log n) space
(call stack), not the O(1)-space follow-up variant.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head):
        if head is None or head.next is None:
            return head

        # Split into two halves.
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        slow.next = None

        left = self.sortList(head)
        right = self.sortList(mid)

        return self._merge(left, right)

    def _merge(self, a, b):
        dummy = ListNode()
        tail = dummy
        while a and b:
            if a.val <= b.val:
                tail.next = a
                a = a.next
            else:
                tail.next = b
                b = b.next
            tail = tail.next
        tail.next = a if a else b
        return dummy.next
