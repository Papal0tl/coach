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
    map = {}
    cur = head
    while cur:
        map[cur] =
        cur = cur.next

    cur = head
    while cur:
        new_node = map[cur]
        if cur.next:
        else:

        if cur.random:
        else:
    return map[head]
