"""
Agent reference solution for Copy List with Random Pointer.

This file is separate from the user's attempt. Do not reveal it by default.
"""


class Node:
    def __init__(self, x: int, next: "Node | None" = None, random: "Node | None" = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: "Node | None") -> "Node | None":
        if head is None:
            return None

        old_to_new: dict["Node | None", "Node | None"] = {None: None}

        cur = head
        while cur is not None:
            old_to_new[cur] = Node(cur.val)
            cur = cur.next

        cur = head
        while cur is not None:
            copy = old_to_new[cur]
            copy.next = old_to_new[cur.next]
            copy.random = old_to_new[cur.random]
            cur = cur.next

        return old_to_new[head]
