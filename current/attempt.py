"""
User attempt for Copy List with Random Pointer.

Write your reasoning in English comments when useful.
"""


class Node:
    def __init__(self, x: int, next: "Node | None" = None, random: "Node | None" = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head):
        if head is None:
            return None

        mapp = {}
        cur = head
        while cur:
            mapp[cur] = Node(cur.val)
            cur = cur.next

        cur = head
        while cur:
            new_node = mapp[cur]
            if cur.next:
                new_node.next = mapp[cur.next]
            else:
                new_node.next = None
            if cur.random:
                new_node.random = mapp[cur.random]
            else:
                new_node.random = None
            cur = cur.next
        return mapp[head]
