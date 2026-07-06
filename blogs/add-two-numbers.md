# Add Two Numbers (LC 2)

## Problem Summary
Given two non-empty linked lists `l1` and `l2` representing non-negative integers with digits stored in reverse order (least significant digit first), add the two numbers and return the sum as a linked list in the same reverse-digit format.

## Initial Intuition
<!-- Write in your own words: what was your first idea when you saw this problem? -->

## Brute Force
<!-- Write in your own words: is there a less efficient approach you considered (e.g. convert each list to an integer, add, convert back)? How does it compare to your final solution? -->

## Key Insight
<!-- Write in your own words: what's the core idea that makes this solution work? Why does reverse-digit order make list traversal line up with how addition is normally done by hand? -->

## Final Algorithm
1. Create a dummy/sentinel node and a `cur` pointer starting at it, to avoid special-casing the first node of the result.
2. Track a running `carry`, initialized to 0.
3. While either list still has nodes, or `carry` is nonzero: take each list's current digit (or 0 if that list is exhausted), add them together with `carry`, and split the result into a new digit (`total % 10`) and the next carry (`total // 10`).
4. Append the new digit as a node, advance `cur`, and advance whichever of `l1`/`l2` still has nodes.
5. Return `dummy.next` (the real head, skipping the sentinel).

```python
class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(0)
        cur = dummy
        carry = 0

        while l1 is not None or l2 is not None or carry != 0:
            x = l1.val if l1 is not None else 0
            y = l2.val if l2 is not None else 0
            total = x + y + carry
            digit = total % 10
            carry = total // 10

            cur.next = ListNode(digit)
            cur = cur.next

            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next

        return dummy.next
```

## Correctness Argument
<!-- Write in your own words: why does this produce the correct sum, digit by digit? Consider what `carry` represents at the start of each loop iteration, and why the loop condition needs to check `carry` in addition to `l1`/`l2`. -->

## Complexity
Time Complexity: O(max(n, m)), where n and m are the lengths of `l1` and `l2` — each node is visited exactly once, plus at most one extra iteration for a final trailing carry.
Space Complexity: O(max(n, m)) for the output list (the result can have at most one more digit than the longer input); O(1) auxiliary space beyond the output.

## Edge Cases
- Lists of unequal length (shorter list treated as contributing 0 once exhausted).
- Trailing carry after both lists are exhausted, producing an extra digit (e.g. `[9,9] + [1]` -> `[0,0,1]`, `[5] + [5]` -> `[0,1]`).
- Both single-digit with no carry.
- Symmetric all-nines inputs (e.g. `[9,9] + [9,9]` -> `[8,9,1]`).

## Mistakes Made
<!-- Write in your own words: what bugs did you actually hit while writing this, and what was the real fix? Be precise about cause and effect. -->

## How to Recognize This Pattern Next Time
<!-- Write in your own words: what cues in a problem statement point to this digit-wise-sum-with-carry technique, and how does the dummy-node piece connect to problems you've solved before? -->
