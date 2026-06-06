# Rotate Array

## Problem Summary
Given an integer array, rotate it right by k steps in-place. Rotating right by k moves the last k elements to the front.

## Initial Intuition
Simulate the rotation process.
For each rotation: Remove the last element and insert it at the front of the array. eg: [1,2,3,4,5,6,7]. After one rotation: [7,1,2,3,4,5,6]
Repeating this process k times eventually produces the correct answer.

## Brute Force
Rotate the array one step at a time.

```
for _ in range(k):
    last = nums.pop()
    nums.insert(0, last)
```

Each insertion at the front takes O(n) time because all existing elements must shift right.
Complexity is: Time -> O(n·k). Space -> O(1)
Too slow when n and k are large.

## Key Insight
Rotate by n positions returns the array to its original state.
The final list should be (last k elements)+(first n-k elements)
So use slicing. Therefore: `k %= n` removes unnecessary full rotations.

## Final Algorithm
1. Reduce k: `k = k % n` (rotating n steps is the identity).
2. Slice assignment: `nums[:] = nums[-k:] + nums[:-k]`.

## Correctness Argument
After reducing k, we have: `0 ≤ k < n`
The last k elements are the elements that should appear at the beginning after a right rotation: `nums[-k:]` extracts precisely these elements.

The remaining elements are the first n-k elements: `nums[:-k]`

Therefore: `nums[-k:] + nums[:-k]`

## Complexity
- Time: O(n) — one slice copy of the full array.
- Space: O(n) — temporary list of size n before copying back.

## Edge Cases
- k = 0 or k % n = 0: slice is a no-op; array unchanged.
- k ≥ n: modulo reduces to the equivalent rotation within [0, n).
- n = 1: k % 1 = 0 always; no rotation.

## Mistakes Made
wrote a loop over all possible split positions instead of rotating by the requested k. The code ignored the actual input value of k.

I tried: `nums[-k:] + nums[:k]`. 
[1,2,3,4,5,6,7], k = 3
produces: [5,6,7] + [1,2,3], loses the element 4.
The second slice must be the remaining elements: nums[:-k], not the first k elements.

When: k > n, Python slicing behaves differently than expected.
nums[-10:] on a length-7 array returns the entire array.


## How to Recognize This Pattern Next Time
Rotation, cyclic shift, or reordering of an array.
The final position of each element can be described by splitting the array into two contiguous parts.

