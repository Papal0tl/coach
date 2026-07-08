"""
Agent reference solution for Reverse Nodes in k-Group.

This file is separate from the user's attempt. Do not reveal it by default.
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        group_prev = dummy

        while True:
            kth = self._get_kth(group_prev, k)
            if not kth:
                break
            group_next = kth.next

            prev, cur = group_next, group_prev.next
            while cur is not group_next:
                tmp = cur.next
                cur.next = prev
                prev = cur
                cur = tmp

            new_group_prev = group_prev.next
            group_prev.next = kth
            group_prev = new_group_prev

        return dummy.next

    def _get_kth(self, cur: Optional[ListNode], k: int) -> Optional[ListNode]:
        while cur and k > 0:
            cur = cur.next
            k -= 1
        return cur
