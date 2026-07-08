# Reverse Nodes in k-Group (LC 25)

## Problem Summary
Given the head of a singly linked list and an integer k, reverse the nodes of the list k at a time and return the new head. Only nodes may be rewired, not values. If the number of remaining nodes at the end is fewer than k, that final group must be left in its original order.

## Initial Intuition
Like reversing a linked list, but instead of reversing the whole list, it needs to reverse it group by group. => Need a pointer before each group, then reverse the next k nodes and connect them back.

## Brute Force
A brute force approach is to collect all nodes into an array first. Then for every group of size k, reverse that part of the array. If the last group has fewer than k nodes, leave it unchanged. Finally, relink the nodes in the array one by one.

Time Complexity: O(n)
Space Complexity: O(n)

## Key Insight
Check whether there are k nodes first before reversing. If start reversing immediately and later discover there are fewer than k nodes left, I would have already changed nodes that should stay in their original order.

group_prev always points to the node right before the group that about to reverse. Then group_prev.next is the first node of the current group, and after walking k steps, kth becomes the last node of that group.

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
At the top of each loop, group_prev points to the node right before the next group that has not been processed yet. All groups before group_prev have already been reversed correctly and reconnected to the list.

First checks whether a full group of k nodes exists. If not, it returns immediately, so the remaining nodes stay unchanged. If a full group exists, it reverses exactly the nodes from group_head to kth, reconnects the reversed group by setting group_prev.next = kth, and then moves group_prev to group_head, which is now the tail of the reversed group. Therefore, after each loop, one more full group is correctly reversed. When the loop stops, all full k-sized groups have been reversed, and any leftover nodes are untouched.

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
- Wrote while true instead of while True. In Python, booleans must be capitalized.
- Confused about group_head = group_prev.next. I thought for k = 2, group_head should be 3, but actually in the first round the current group is 1 -> 2, so group_head is 1. It only becomes 3 in the second round.
- Forgot that kth must actually move inside the for loop with kth = kth.next. Without that line, kth would stay at group_prev and never find the end of the group.
- Confused by cur.next = prev. The key is that tmp = cur.next saves the next node first, then cur.next = prev reverses one pointer.

## How I Will Recognize This Pattern Next Time
- The problem says “every k nodes” or “k at a time.”
- Must rewire nodes, not just change values.
- The leftover group should stay unchanged if it has fewer than k nodes.
- Need a pointer before the group (group_prev), the group head, the group tail (kth), and the next group start (group_next).
