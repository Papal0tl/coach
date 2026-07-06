# Add Two Numbers (LC 2)

## Problem Summary
Given two non-empty linked lists `l1` and `l2` representing non-negative integers with digits stored in reverse order (least significant digit first), add the two numbers and return the sum as a linked list in the same reverse-digit format.

## Initial Intuition
Store the digits from both linked lists, then add them together. 
After noticing the digits are already in reverse order, I realized can add them directly from head to tail, just like adding numbers from right to left by hand.


## Brute Force
Convert each linked list into an integer, add the two integers, then convert the result back into a linked list.

This is less aligned with the linked list structure and may be unsafe for very large numbers in some languages. The final solution is better because it processes the lists digit by digit without converting the whole number.


## Key Insight
The key idea is that reverse order makes the head of each linked list represent the ones digit. That means we can start adding immediately from the head, just like normal addition starts from the smallest digit.

At each step, we add the current digit from `l1`, the current digit from `l2`, and the carry from the previous step. The result digit is `total % 10`, and the carry for the next step is `total // 10`.

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
At the start of each loop iteration, `carry` represents the carry produced by adding the previous lower digit. The current iteration adds the next digit from `l1`, the next digit from `l2`, and this carry, so it correctly computes the next digit of the final sum.

The algorithm appends `total % 10`, which is exactly the digit that should appear in the current position, and saves `total // 10` as the carry for the next higher position. Since the lists are stored in reverse order, moving forward in the linked lists is the same as moving from lower digits to higher digits.

The loop also checks `carry != 0` because even after both lists end, there may still be one final carry that needs to become a new node.


## Complexity
Time Complexity: O(max(n, m)), where n and m are the lengths of `l1` and `l2` — each node is visited exactly once, plus at most one extra iteration for a final trailing carry.
Space Complexity: O(max(n, m)) for the output list (the result can have at most one more digit than the longer input); O(1) auxiliary space beyond the output.

## Edge Cases
- Lists of unequal length (shorter list treated as contributing 0 once exhausted).
- Trailing carry after both lists are exhausted, producing an extra digit (e.g. `[9,9] + [1]` -> `[0,0,1]`, `[5] + [5]` -> `[0,1]`).
- Both single-digit with no carry.
- Symmetric all-nines inputs (e.g. `[9,9] + [9,9]` -> `[8,9,1]`).

## Mistakes Made
- Initially tried to use something like `set1()` and `set2()`, but sets are not useful here because this problem depends on digit order. A set would lose order and duplicate digits.
- I was thinking about collecting values first, but the better fix is to process both linked lists directly with two pointers.
- When one list ends earlier, its missing digit should be treated as `0`.
- Need to include `carry != 0` in the loop condition; otherwise cases like `[5] + [5]` would incorrectly return `[0]` instead of `[0,1]`.


## How to Recognize This Pattern Next Time
- Add numbers digit by digit, especially when the digits are stored in reverse order. Words like “each node stores one digit,” “reverse order,” and “return the sum as a linked list” should immediately suggest using carry.
