# LRU Cache (LC 146)

## Problem Summary
Design a cache with a fixed `capacity` that supports `get(key)` and `put(key, value)`, both in O(1) average time. `get` returns the value for a key, or `-1` if absent. `put` inserts or updates a key's value; if inserting a new key pushes the cache over capacity, the least recently used key must be evicted. Both `get` and successful `put` calls count as "using" a key, making it the most recently used.

## Initial Intuition

_User-filled: what was your first instinct for tracking "least recently used," before settling on the final design?_

## Brute Force

_User-filled: describe an approach that gets the right answer but isn't O(1) per operation (e.g. a dict plus a separate list you scan/update linearly), and state its complexity._

## Key Insight

_User-filled: why does neither a hash map alone nor a linked list alone solve this, and what does combining them give you?_

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

_User-filled: state the invariant the doubly linked list maintains (what does its order represent at all times?), and why every `get`/`put` that touches a key preserves that invariant._

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

_User-filled: describe the actual bugs from your git history, in your own words._

## How I Will Recognize This Pattern Next Time

_User-filled: what signals in a problem statement point to "hash map + doubly linked list" as the shape?_
