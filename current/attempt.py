"""
User attempt for Merge k Sorted Lists.

Write your reasoning in English comments when useful.
"""

from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if lists is None:
            return None
        merge = None
        for cur_list in lists:
            dummy = ListNode(0)
            cur = dummy
            list1 = merge
            list2 = cur_list
            while list1 is not None and list2 is not None:
                if list1.val <= list2.val:
                    cur.next = list1
                    cur = cur.next
                    list1 = list1.next
                else:
                    cur.next = list2
                    cur = cur.next
                    list2 = list2.next
            if list1 is not None:
                cur.next = list1
            else:
                cur.next = list2
            merge = dummy.next
        return merge
