# Copy List with Random Pointer (LC 138)

## Problem Summary
Given the head of a singly linked list where each node also has a `random` pointer (which may point to any node in the list, including itself, or to `None`), construct a deep copy of the entire list. The copy must consist of brand-new node objects with the same `val`, `next`, and `random` structure as the original, but no pointer in the copy may reference any node from the original list.

## Initial Intuition
Copy the list from left to right like a normal linked list: create a new node for each original node, connect the `next` pointers, and then somehow copy the `random` pointers too. But the `random` pointer made it harder because it can point anywhere, not just to the next node.


## Brute Force
First copy all the values into new nodes, then for each original node, find the index of its `random` target by scanning the original list. After that, scan the copied list to the same index and connect the copied `random` pointer.

Inefficient because each `random` pointer may require another full scan of the list. The time complexity is O(n²), and the space complexity is O(n).


## Key Insight
Need a way to quickly find the copied node that corresponds to any original node. Cannot always set `random` immediately while creating a node, because `random` might point forward to a node whose copy has not been created yet.

So should first create all copied nodes and store a mapping from original node to copied node. Then in a second pass, it can safely connect both `next` and `random`, because every possible target already has a copied node.

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
After first pass, `mapp` guarantees every original node has one corresponding new node with the same value. These new nodes are separate objects, so the copy will not reuse original nodes.

During the second pass, if at an original node `cur`, its copied node is `mapp[cur]`. If `cur.next` points to another original node, that node already has a copy in `mapp`, so `mapp[cur.next]` gives the correct copied `next` node. The same is true for `cur.random`: it may point forward, backward, to itself, or to `None`, but if it points to a real node, that node's copy already exists in `mapp`.

So, every copied node gets the same `val`, `next`, and `random` structure as the original list, while all pointers in the copied list point only to copied nodes.

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
- Wrote the whole method body (the `if head is None` check, both `while` loops, and the final `return`) directly inside the class body instead of inside a `def copyRandomList(self, head):` method. This caused a repeated `SyntaxError: 'return' outside function`, since `return` is only legal inside a function. This was the biggest blocker of the session and took several rounds to fix.
- The second-pass `while` loop initially had no `cur = cur.next`, which would have caused an infinite loop if it had ever actually run. I caught and fixed this myself before it ran, while the method-wrapping bug above was still blocking execution.
- Wrote `Node(cur)` instead of `Node(cur.val)`. That would pass the whole original node object into the constructor instead of copying only the node's value.
- Used `map` as a variable name at first, which works but is not a good habit because `map` is a built-in Python function. I changed it to `mapp`.

## How I Will Recognize This Pattern Next Time
Copy a structure with extra pointers, random pointers, or references that may point anywhere => Think about building a mapping from original objects to copied objects.

