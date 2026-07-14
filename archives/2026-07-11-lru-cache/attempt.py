"""
User attempt for LRU Cache.

Write your reasoning in English comments when useful.
"""
class Node(object):

    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = Node()
        self.tail = Node()
        self.cache = {}
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        node.prev.next = node.next
        node.next.prev = node.prev

        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
        
        return node.value


    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value

            node.prev.next = node.next
            node.next.prev = node.prev

            node.next = self.head.next
            node.prev = self.head
            self.head.next.prev = node
            self.head.next = node
        else:
            node = Node(key, value)
            self.cache[key] = node
            node.next = self.head.next
            node.prev = self.head
            self.head.next.prev = node
            self.head.next = node

            if len(self.cache) > self.capacity:
                last = self.tail.prev
                last.prev.next = self.tail
                self.tail.prev = last.prev

                del self.cache[last.key]