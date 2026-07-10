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
        if head is None or head.next is None:
            return head
        prev = None
        fast = head
        slow = head
