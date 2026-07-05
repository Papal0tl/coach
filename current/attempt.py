"""
User attempt for Linked List Cycle II.

Write your reasoning in English comments when useful.
"""

from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        seen = set()

        cur = head
        while cur is not None:
            if cur in seen:
                return cur
            seen.add(cur)
            cur = cur.next
        return null
