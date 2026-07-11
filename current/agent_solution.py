"""
Agent reference solution for LRU Cache.

This file is separate from the user's attempt. Do not reveal it by default.
"""


class Node:
    def __init__(self, key: int = 0, val: int = 0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {}
        # Dummy head/tail sentinels remove all edge-casing around empty
        # lists or removing the first/last real node.
        # head.next is the most-recently-used node; tail.prev is the least.
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: Node) -> None:
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    def _add_front(self, node: Node) -> None:
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        node = self.map[key]
        self._remove(node)
        self._add_front(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            node = self.map[key]
            node.val = value
            self._remove(node)
            self._add_front(node)
            return

        if len(self.map) >= self.capacity:
            lru = self.tail.prev
            self._remove(lru)
            del self.map[lru.key]

        node = Node(key, value)
        self.map[key] = node
        self._add_front(node)
