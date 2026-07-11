# Session Notes

- Problem slug: `lru-cache`
- Archive path: `archives/2026-07-11-lru-cache/`

## Agent Preparation

- Pattern: hash map (key -> node) + doubly linked list ordered by recency, with dummy head/tail sentinels.
- Key insight: a hash map alone gives O(1) key lookup but no O(1) way to know/update recency order; a linked list alone gives O(1) recency reordering but no O(1) key lookup. Combining them — hash map stores pointers directly into the linked list nodes — gives O(1) for both.
- Invariant or state: the list is always kept ordered by recency, most-recently-used at `head.next`, least-recently-used at `tail.prev`. Every `get` or `put` that touches a key removes that key's node from its current position and reinserts it at the front. Dummy `head`/`tail` sentinels mean removal/insertion never special-cases the first or last real node.
- Complexity target: O(1) average time for both `get` and `put`; O(capacity) space.

## Reference Solution Summary

`Node` holds `key`, `val`, `prev`, `next`. `LRUCache` keeps a `dict` from key to `Node` plus a doubly linked list bounded by dummy `head`/`tail` nodes. `_remove(node)` and `_add_front(node)` are the only two list-mutation primitives; both `get` and `put` are built from them. `get` moves the touched node to the front and returns its value (or -1 if absent). `put` either updates-and-refreshes an existing node, or — after evicting `tail.prev` if at capacity — inserts a new node at the front and records it in the map. Storing the `key` on the `Node` (not just the `val`) is what makes eviction able to delete the right entry from the map in O(1) without a reverse lookup.

## Edge Cases

- `capacity == 1`: every `put` on a new key evicts the sole existing entry.
- `get` on a key that was never inserted, or was already evicted.
- `put` on a key that already exists: must update the value AND refresh recency (not just append/ignore).
- Eviction must happen only when inserting a genuinely new key that pushes size over capacity — updating an existing key never triggers eviction.
- Repeated `get` calls on the same key should not change its position relative to itself, only relative to other keys.

## User-Facing Takeaways

Pending — filled after the user attempt and blog.

## Follow-Up Candidates

- Discuss why `OrderedDict` (Python stdlib) can implement this in a few lines via `move_to_end` + `popitem(last=False)`, as a "you now understand what the built-in is doing under the hood" comparison, offered only after the user has built the raw hash-map + doubly-linked-list version themselves.
- LFU Cache (LeetCode 460) as a natural next-step generalization if this session goes well.
