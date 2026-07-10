"""
User attempt for Sort List.

Write your reasoning in English comments when useful.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head):
        if not head:
            return head
        dummy = ListNode(0)
        dummy.next = head
        cur = head
        tmp = dummy
        while cur and cur.next:
            if cur.val > cur.next.val:
                tmp = cur.next
                cur.next = tmp.next
                tmp.next = cur
                cur = tmp
            cur = cur.next
        return dummy.next
