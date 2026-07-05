# Linked List Cycle II (LC 142)

## Problem Summary
Given the head of a linked list, return the node where the cycle begins, or `None` if there is no cycle.

A cycle means that by repeatedly following `next`, we eventually reach a node we have already visited. Unlike LC 141 (Linked List Cycle), this problem asks for the specific node where the cycle starts, not just whether a cycle exists.

## Initial Intuition


## Brute Force


## Key Insight


## Final Algorithm
1. Walk the list with `cur`, tracking visited nodes in a set.
2. If `cur` is already in the set, it is the first repeated node — return it as the cycle entry.
3. If `cur` reaches `None`, there is no cycle; return `None`.

```python
class Solution:
    def detectCycle(self, head):
        seen = set()

        cur = head
        while cur:
            if cur in seen:
                return cur
            seen.add(cur)
            cur = cur.next
        return None
```

## Correctness Argument


## Complexity
Time Complexity: O(n)
Space Complexity: O(n)

## Edge Cases
- Empty list: `head = None`, return `None`.
- Single node, no cycle: return `None`.
- Single node pointing to itself: return that node.
- Cycle starts at head.
- Cycle starts at the last node.
- No cycle, long list.

## Mistakes Made


## How to Recognize This Pattern Next Time
