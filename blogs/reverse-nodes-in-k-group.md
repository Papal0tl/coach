# Reverse Nodes in k-Group (LC 25)

## Problem Summary
Given the head of a singly linked list and an integer k, reverse the nodes of the list k at a time and return the new head. Only nodes may be rewired, not values. If the number of remaining nodes at the end is fewer than k, that final group must be left in its original order.

## Initial Intuition
TODO (user-filled): what was your first instinct when you read this problem, before you had a full plan?

## Brute Force
TODO (user-filled): describe an approach distinct from your final algorithm (for example, buffering each group's values or nodes and relinking), and its time/space cost.

## Key Insight
TODO (user-filled): what made this problem click? Consider: why does the algorithm need to check whether a full group of k nodes exists *before* reversing anything?

## Final Algorithm
1. Create a dummy/sentinel node pointing to `head`, and a `group_prev` pointer starting at the dummy — `group_prev` always trails the next group to process.
2. From `group_prev`, walk forward k steps to find `kth`, the last node of the next group. If fewer than k nodes remain (`kth` becomes `None`), stop and return `dummy.next` — the remainder is left untouched.
3. Save `group_next = kth.next`, the node immediately after this group, and `group_head = group_prev.next`, the first node of this group.
4. Reverse the k nodes in place: starting with `prev = group_next` and `cur = group_head`, repeatedly save `cur.next`, point `cur.next` back to `prev`, then advance both `prev` and `cur`, until `cur` reaches `group_next`.
5. Reconnect: `group_prev.next = kth` (the new head of this now-reversed group), then advance `group_prev = group_head` (the old head, now this group's tail).
6. Repeat from step 2 for the next group.

```python
class Solution:
    def reverseKGroup(self, head, k):
        dummy = ListNode(0)
        dummy.next = head
        group_prev = dummy

        while True:
            kth = group_prev
            for i in range(k):
                kth = kth.next
                if kth is None:
                    return dummy.next

            group_next = kth.next
            group_head = group_prev.next

            prev = group_next
            cur = group_head
            while cur != group_next:
                tmp = cur.next
                cur.next = prev
                prev = cur
                cur = tmp

            group_prev.next = kth
            group_prev = group_head
```

## Correctness Argument
TODO (user-filled, with agent prompts if needed): state the invariant that holds at the top of each `while True` iteration (what does `group_prev` represent?), and argue why the loop terminates with every full group reversed and any remainder untouched.

## Complexity
Time Complexity: O(n), where n is the number of nodes — each node is visited a constant number of times (once during the k-step lookahead, once during reversal).
Space Complexity: O(1) auxiliary space — only the dummy node and a fixed set of pointers, no buffering of node values.

## Edge Cases
- Empty list (`head = None`): the first k-step walk immediately hits `None`, returns `dummy.next = None`.
- `k == 1`: every "group" is a single node; the reversal loop body runs once per node with no visible effect (no-op).
- `k == n` (whole list is one group): the entire list reverses.
- `n` an exact multiple of `k`: every group reverses, no leftover.
- `n` not a multiple of `k`: the trailing partial group is detected by the lookahead (`kth` becomes `None`) and left in original order.
- Single-node list.

## Mistakes I Made
TODO (user-filled): describe the actual bugs you hit and how you found/fixed each one.

## How I Will Recognize This Pattern Next Time
TODO (user-filled): what signals in a problem statement point you toward this pattern?
