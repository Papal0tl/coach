# Linked List Cycle (LC 141)

## Problem Summary
Given the head of a linked list, determine whether the linked list has a cycle.

A cycle means that by repeatedly following `next`, we can reach a node that we have already visited before.

Return `true` if there is a cycle, otherwise return `false`.

## Initial Intuition
Walk through the linked list and remember every node I have visited.

If I ever see the same node again, that means the list loops back to an earlier node, so there is a cycle.

## Brute Force
Use a set to store visited nodes.
For each node:
- If the node is already in the set, return `True`.
- Otherwise, add it to the set and move to the next node.

If we reach `None`, return `False`.
This works, but it uses extra space.

## Key Insight
Instead of storing visited nodes, we can use two pointers moving at different speeds.

`slow` moves one step each time.

`fast` moves two steps each time.

If there is a cycle, `fast` will eventually catch up to `slow`.

If there is no cycle, `fast` will reach `None`.

## Final Algorithm
1. Set both `slow` and `fast` to `head`.
2. While `fast` and `fast.next` are not `None`:
   - Move `slow` one step.
   - Move `fast` two steps.
   - If `slow == fast`, return `True`.
3. If the loop ends, return `False`.

```python
class Solution(object):
    def hasCycle(self, head):
        slow = head
        fast = head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False
```

## Correctness Argument
If the list has no cycle, then following next will eventually reach None. Since fast moves faster, it will reach the end first, so the algorithm returns False.

If the list has a cycle, then once both pointers enter the cycle, they are moving around the same loop. Since fast moves one extra step more than slow each round, it gets closer to slow inside the cycle and must eventually meet it. When they meet, the algorithm returns True.

## Complexity
Time Complexity: O(n)
Space Complexity: O(1)

## Edge Cases
- Empty list: head = None, return False.
- One node without a cycle: return False.
- One node pointing to itself: return True.
- Two nodes with a cycle: return True.
- Long list with no cycle: fast eventually reaches None.

## Mistakes Made
N/A

## How to Recognize This Pattern Next Time
The problem is about a linked list and asks whether something repeats or loops, think about cycle detection.

If the problem asks for O(1) extra space, avoid using a set and consider fast and slow pointers:
linked list + cycle/repeated node + no extra space => use fast and slow pointers.
