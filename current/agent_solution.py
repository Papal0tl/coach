"""
Agent reference solution for Linked List Cycle II.

This file is separate from the user's attempt. Do not reveal it by default.
"""

from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                ptr = head
                while ptr is not slow:
                    ptr = ptr.next
                    slow = slow.next
                return ptr

        return None
