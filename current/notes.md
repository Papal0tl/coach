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

## Coaching Log

- First draft (`__init__` + `get`, `put` still `pass`): independently reached for `Node()` and a `self.cache` dict without any hint — correctly identifies the hash-map-of-nodes + linked-list shape on the first try, first design-problem session in the arc. Not yet run (unfinished statement `node.next = ` on the last line of `get` is a syntax error as-is).
- Structural gap: `__init__(self, capacity)` body reads `self.key = key` / `self.value = value`, but `__init__` only receives `capacity` — these lines conflate "the cache object" with "one entry in the cache." Also `capacity` itself is never stored on `self`. `Node` is used but never defined in this file.
- `get`: references bare `cache` instead of `self.cache`. Unlink logic (`node.prev.next = node.next`, `node.next.prev = node.prev`) is correct for removing a node from a doubly linked list, but the move-to-front reinsertion and the `return node.val` are not yet written.
- Intervention used: clarifying question about the `__init__` body (tier 1), not yet a direct explanation.
- Second draft: fully resolved the earlier structural gap unprompted — added a standalone `Node` class (`key`, `value`, `prev`, `next`), stored `capacity` on `self`, and wired up `head`/`tail` sentinels correctly in `__init__`. `get` and `put` are both structurally complete: unlink-then-reinsert-at-front logic is correct in both, `put`'s existing-key branch updates value and refreshes recency without evicting, and the new-key branch evicts `self.tail.prev` only when `len(self.cache) > self.capacity` (correct boundary, evicts after insert only when actually over). No `_remove`/`_add_front` helpers — logic is duplicated inline across `get` and both `put` branches; correct but a candidate for a later simplification note, not a bug.
- Remaining bug (repeat of the same mechanical slip from the first draft, now in two places): `get` and `put` both check `if key in cache` / `if key not in cache` instead of `self.cache` — confirmed via running `LRUCache(2).put(1, 1)`, which raises `NameError: name 'cache' is not defined`.
- Intervention used: ran the code directly (matches this user's established empirical-debugging preference from prior sessions) and will point to the traceback rather than naming the fix directly.

## Follow-Up Candidates

- Discuss why `OrderedDict` (Python stdlib) can implement this in a few lines via `move_to_end` + `popitem(last=False)`, as a "you now understand what the built-in is doing under the hood" comparison, offered only after the user has built the raw hash-map + doubly-linked-list version themselves.
- LFU Cache (LeetCode 460) as a natural next-step generalization if this session goes well.
