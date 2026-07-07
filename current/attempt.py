"""
User attempt for Swap Nodes in Pairs.

Write your reasoning in English comments when useful.
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        while prev.next and prev.next.next:
            a = prev.next
            b = a.next

            prev.next = b
            a.next = b.next
            b.next = a

            prev = a
        return dummy.next
