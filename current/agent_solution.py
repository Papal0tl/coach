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
    pass
