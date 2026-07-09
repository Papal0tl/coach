# Session Notes

- Problem slug: `copy-list-with-random-pointer`
- Archive path: `archives/2026-07-09-copy-list-with-random-pointer/`

## Agent Preparation

- Pattern: hash map (old node -> new node) built in a first pass, then a second pass to wire `next`/`random` pointers using the map. This is the first session combining a hash map with linked-list construction rather than pure pointer rewiring.
- Key insight: you cannot set `copy.random` correctly while creating nodes, because the target of a `random` pointer might not exist yet (it could point forward in the list). Splitting into two passes — "create all copies first," then "wire pointers second" — resolves the ordering problem. The map itself is what lets `random` (an arbitrary, non-sequential pointer) be translated from an old-node reference to a new-node reference in O(1).
- Invariant or state: after pass 1, `old_to_new[old_node]` holds the fresh copy for every node in the list, plus `old_to_new[None] = None` as a sentinel so pass 2 needs no branching for `next`/`random` pointers that are `None`.
- Complexity target: O(n) time, O(n) space (hash map + n new nodes). Follow-up candidate: O(1) extra space via interleaving copied nodes into the original list (old1 -> new1 -> old2 -> new2 -> ...), reading `random` off the interleaved structure, then detaching.

## Reference Solution Summary

Two linear passes over the list.
Pass 1: walk `head`, create `Node(cur.val)` for each original node, store `old_to_new[cur] = copy`. Include `old_to_new[None] = None` up front.
Pass 2: walk `head` again, and for each `cur` set `copy.next = old_to_new[cur.next]` and `copy.random = old_to_new[cur.random]` where `copy = old_to_new[cur]`.
Return `old_to_new[head]`.

## Edge Cases

- Empty list (`head is None`) -> return `None`.
- Single node whose `random` points to itself.
- No node has a `random` pointer (all `None`).
- Original list must remain unmodified (no leaked references from the copy back into the original).
- Multiple nodes with the same `val` (duplicates should not collapse via any value-based lookup — mapping must be by node identity).

## User-Facing Takeaways

- The two-pass hash-map pattern (build all nodes first, wire pointers second) generalizes to any problem where a pointer/reference can point "forward" to something not yet constructed.
- Watch whether the user tries to set `random` inline during node creation and hits the forward-reference problem, or anticipates it up front.

## Follow-Up Candidates

- O(1) space interleaving solution, if the user finishes the hash-map version cleanly and wants a harder variant (matches the pattern of prior sessions offering space-optimized follow-ups).
