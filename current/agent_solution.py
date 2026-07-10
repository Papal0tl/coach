"""
Agent reference solution for Merge k Sorted Lists.

This file is separate from the user's attempt. Do not reveal it by default.
"""

import heapq
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for i, node in enumerate(lists):
            if node is not None:
                # Tie-break on i so the heap never has to compare ListNode
                # objects directly when two values are equal.
                heapq.heappush(heap, (node.val, i, node))

        dummy = ListNode()
        tail = dummy

        while heap:
            val, i, node = heapq.heappop(heap)
            tail.next = node
            tail = tail.next
            if node.next is not None:
                heapq.heappush(heap, (node.next.val, i, node.next))

        return dummy.next
