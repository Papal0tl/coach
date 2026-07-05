# Linked List Cycle II (LC 142)

## Problem Summary
Given the head of a linked list, return the node where the cycle begins, or `None` if there is no cycle.

A cycle means that by repeatedly following `next`, we eventually reach a node we have already visited. Unlike LC 141 (Linked List Cycle), this problem asks for the specific node where the cycle starts, not just whether a cycle exists.

## Initial Intuition
Remember every node I had visited. If I ever reached the same node again, that node must be the beginning of the cycle because it is the first node visited twice.

## Brute Force
Traverse the linked list while storing every visited node in a hash set.

- If the current node has already been seen, return it immediately.
- If the traversal reaches None, the list has no cycle.

## Key Insight
A node outside the cycle is visited only once. The first node that can ever be visited twice is exactly the cycle entry. Therefore, keeping a set of visited nodes lets us detect the entry as soon as we revisit it.

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
Every node before the cycle is visited exactly once, so none of them can be returned. Once we enter the cycle, we eventually return to the cycle entry after one full loop. Since the entry was already stored in the set, it is the first node detected as a repeat and is returned. If the traversal reaches None, no node is revisited, so the list has no cycle and returning None is correct.

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
- Forgot that Python uses `None`, not `null`.

## How to Recognize This Pattern Next Time
- The input is a linked structure (linked list or graph).
- You need to detect repeated visits.
- Returning the first repeated node or detecting a cycle is enough.
- Extra O(n) memory is allowed, making a hash set a simple solution.