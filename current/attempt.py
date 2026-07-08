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
        t_prev = dummy

        while true:
            kth = t_prev
            for i in range(k):
                if kth is None:
                    return dummy.next
            t_next = kth.next
            t_head = t_prev.next

            prev = t_next
            cur = t_head
            


        

