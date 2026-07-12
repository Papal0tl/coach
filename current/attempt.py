"""
User attempt for LRU Cache.

Write your reasoning in English comments when useful.
"""


class LRUCache:

    def __init__(self, capacity: int):
        self.key = key
        self.value = value
        self.head = Node()
        self.tail = Node()
        self.cache = {}

    def get(self, key: int) -> int:
        if key not in cache:
            return -1
        node = self.cache[key]

        node.prev.next = node.next
        node.next.prev = node.prev
        node.next = 

    def put(self, key: int, value: int) -> None:
        pass
