"""
User attempt for Merge Two Sorted Lists.

Write your reasoning in English comments when useful.
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr = 

        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next

        if list1 is not None:
            cur.next = l1
        else:
            cur.next = l2
        return 
