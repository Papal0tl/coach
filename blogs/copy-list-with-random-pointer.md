# Copy List with Random Pointer (LC 138)

## Problem Summary
Given the head of a singly linked list where each node also has a `random` pointer (which may point to any node in the list, including itself, or to `None`), construct a deep copy of the entire list. The copy must consist of brand-new node objects with the same `val`, `next`, and `random` structure as the original, but no pointer in the copy may reference any node from the original list.

## Initial Intuition
TODO (user-filled): what was your first instinct when you read this problem, before you had a full plan?

## Brute Force
TODO (user-filled): describe an approach distinct from your final algorithm, and its time/space cost.

## Key Insight
TODO (user-filled): what made this problem click? Consider: why can't you set a copied node's `random` pointer at the same time you create that node?

## Final Algorithm
1. If `head` is `None`, return `None`.
2. First pass: walk the original list once, creating a new `Node(cur.val)` for every original node, and store the mapping `old node -> new node` in a dict (`mapp`).
3. Second pass: walk the original list again. For each `cur`, look up its copy `new_node = mapp[cur]`, then set `new_node.next = mapp[cur.next]` (or `None` if `cur.next` is `None`) and `new_node.random = mapp[cur.random]` (or `None` if `cur.random` is `None`).
4. Return `mapp[head]`.

```python
class Solution:
    def copyRandomList(self, head):
        if head is None:
            return None

        mapp = {}
        cur = head
        while cur:
            mapp[cur] = Node(cur.val)
            cur = cur.next

        cur = head
        while cur:
            new_node = mapp[cur]
            if cur.next:
                new_node.next = mapp[cur.next]
            else:
                new_node.next = None
            if cur.random:
                new_node.random = mapp[cur.random]
            else:
                new_node.random = None
            cur = cur.next
        return mapp[head]
```

## Correctness Argument
TODO (user-filled, with agent prompts if needed): state the invariant that holds after the first pass (what does `mapp` guarantee for every original node?), and argue why the second pass can always resolve `cur.next` and `cur.random` correctly regardless of whether they point forward or backward in the list.

## Complexity
Time Complexity: O(n), where n is the number of nodes — two linear passes over the list.
Space Complexity: O(n) — the `mapp` dictionary holds one entry per original node, plus the n new nodes themselves.

## Edge Cases
- Empty list (`head = None`): returns `None` immediately.
- A node whose `random` points to itself.
- No node has a `random` pointer (all `None`).
- Multiple nodes with the same `val` (must be distinguished by node identity, not value, since the mapping key is the node object itself).
- The original list must remain unmodified.

## Mistakes I Made
TODO (user-filled): describe the actual bugs you hit and how you found/fixed each one.

## How I Will Recognize This Pattern Next Time
TODO (user-filled): what signals in a problem statement point you toward this pattern?
