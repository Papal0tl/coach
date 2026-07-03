# Coaching Notes — Reverse Linked List

## Session

- Date: 2026-07-03
- Problem: LC 206 Reverse Linked List
- Language: Python
- Mode: hint-only

## Key Insight

Reversing a singly linked list in place requires flipping every `next` pointer to point backward. Because each node's `next` is overwritten, the node that comes after it must be saved *before* the overwrite, or the rest of the list becomes unreachable.

The standard iterative approach keeps three references: `prev` (the reversed portion so far, starts at `None`), `cur` (the node being processed), and `nxt` (saved before rewiring). Each step: save `cur.next`, point `cur.next` back to `prev`, then advance both `prev` and `cur`.

A recursive version reverses the rest of the list first, then fixes up the link between the current node and its (now-reversed) successor.

## Invariant

At the top of each iteration, `prev` is the head of the correctly-reversed sublist of all nodes processed so far, and `cur` is the head of the remaining (still-forward) sublist. When `cur` becomes `None`, `prev` is the new head of the fully reversed list.

## Algorithm (iterative)

```
prev, cur = None, head
while cur:
    nxt = cur.next
    cur.next = prev
    prev = cur
    cur = nxt
return prev
```

## Complexity

- Time: O(n) — each node visited once.
- Space: O(1) iterative; O(n) recursive (call stack).

## Edge Cases

- Empty list (`head = None`): loop never runs, returns `None`. ✓
- Single node: loop runs once, `cur.next` set to `None` (already `None`), returns the same node as new head. ✓
- Two nodes: verifies the pointer swap direction is correct, not just a no-op.
- List with repeated/negative values: confirms comparison is by structure/order, not value uniqueness.

## Coaching Targets

- Does the user save `cur.next` before overwriting it (the classic bug: losing the rest of the list)?
- Does the user initialize `prev = None` (so the original head's `next` correctly becomes `None`)?
- Can the user state the loop invariant (prev = reversed-so-far, cur = remaining)?
- Will the user attempt the recursive version, and can they explain the recursive invariant (reverse the rest, then fix the link)?
- Does the user handle the empty-list case without a special-case branch?
