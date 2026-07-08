"""
User attempt for Reverse Nodes in k-Group.

Write your reasoning in English comments when useful.
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        dummy.next = head
        group_prev = dummy

        while true:
            kth = group_prev
            for i in range(k):
                kth = kth.next
                if kth is None:
                    return dummy.next

            group_next = kth.next
            group_head = group_prev.next

            prev = group_next
            cur = group_head

            while cur != group_next:
                tmp = cur.next
                cur.next = prev
                prev = cur
                cur = tmp
            group_prev.next = kth
            group_prev = group_head

                



        

