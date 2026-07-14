# LRU Cache (LC 146)

## Problem Summary
Design a cache with a fixed `capacity` that supports `get(key)` and `put(key, value)`, both in O(1) average time. `get` returns the value for a key, or `-1` if absent. `put` inserts or updates a key's value; if inserting a new key pushes the cache over capacity, the least recently used key must be evicted. Both `get` and successful `put` calls count as "using" a key, making it the most recently used.

## Initial Intuition

Use a dictionary to store each key-value pair and another structure to record the order in which keys were used. Could keep the most recently used key at the front and the least recently used key at the back, then remove the back key whenever the cache exceeded its capacity.

## Brute Force

Use a dictionary for storing values and a list for tracking usage order. Whenever a key is accessed or updated, remove it from its current position in the list and insert it at the front. When the cache exceeds capacity, remove the key at the end of the list.

This approach gives O(1) average dictionary lookup, but removing an arbitrary key from the list takes O(n), so get and put can take O(n) time.

## Key Insight

Hash map can find a key quickly, but it does not efficiently maintain which key is least recently used. A linked list can maintain usage order and move or remove nodes efficiently, but finding a specific key in the list would take O(n).

Hash map finds the node in O(1) average time, and the doubly linked list moves, inserts, or removes that node in O(1) time.

## Final Algorithm
1. Define a `Node` holding `key`, `value`, `prev`, `next`.
2. `LRUCache` keeps a dict `cache` mapping key -> `Node`, plus a doubly linked list bounded by dummy `head`/`tail` sentinels. `head.next` is always the most-recently-used node; `tail.prev` is always the least-recently-used node.
3. `get(key)`: if `key` not in `cache`, return `-1`. Otherwise, unlink the node from its current position, relink it right after `head` (most-recently-used position), and return its value.
4. `put(key, value)`: if `key` already exists, update its value, then move it to the front the same way `get` does (no eviction). If `key` is new, create a `Node`, add it to `cache`, insert it at the front, then — only if `len(cache)` now exceeds `capacity` — remove `tail.prev` (the least-recently-used node) from both the list and the dict.

```python
class Node:
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
```

## Correctness Argument

The linked list always keeps keys from most recently used to least recently used. Every successful get or put moves the key to the front, so tail.prev is always the least recently used key. When the cache exceeds capacity, removing tail.prev therefore removes the correct key.

## Complexity
Time Complexity: O(1) average per `get` and `put` — dict lookup is O(1), and unlinking/relinking a node touches a constant number of pointers regardless of list size.
Space Complexity: O(capacity) — one `Node` and one dict entry per stored key, plus the two sentinel nodes.

## Edge Cases
- `capacity == 1`: any `put` of a new key evicts the sole existing entry.
- `get` on a key that was never inserted, or was already evicted.
- `put` on a key that already exists: must update the value and refresh recency, but must not evict anything.
- Eviction should only happen when inserting a genuinely new key pushes the size over capacity — updating an existing key never triggers it.
- Repeated `get` calls on the same key: recency updates relative to other keys, not to itself.

## Mistakes I Made

- Needed to clarify the meaning of “most recently used.” After put(1, 1) followed by put(2, 2), key 2 is the most recently used key because inserting a key also counts as using it.
- Focused only on storing key-value pairs and did not immediately see why a dictionary alone could not efficiently track the least recently used key.
- Had to understand why both the dictionary and the linked list must store information about the same entry. The dictionary is used to find a node quickly, while the linked list stores its usage order.
- Found the pointer updates difficult to follow, especially the four assignments used to insert a node after head.
- Needed to distinguish updating an existing key from inserting a new key. Updating changes the value and refreshes recency, but it does not increase the cache size or trigger eviction.

## How I Will Recognize This Pattern Next Time

- Fast lookup by key.
- A changing order based on recent access.
- Moving an arbitrary item to the front in O(1).
- Removing the oldest or least recently used item in O(1).
