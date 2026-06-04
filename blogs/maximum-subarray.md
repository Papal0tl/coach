# Maximum Subarray

**Source:** LeetCode 53 · Medium
**Date:** 2026-06-03
**Language:** Python

---

## Problem Summary

Given an integer array `nums`, find the contiguous subarray with the largest sum and return its sum.

---

## Initial Intuition

TODO: What was your first instinct when you read this problem? Did brute force come to mind, or did a pattern emerge immediately?

Check every possible subarray and finding the one with the largest sum. Since the answer must be a continuous subarray, need to compare sums of different cntinuous ranges.

---

## Brute Force

TODO: Describe the brute force approach. What is its time complexity and why is it too slow?

Try every starting index and every ending index, then calculate the sum.
```
for i in range(len(nums)):
    for j in range(i, len(nums)):
        check sum(nums[i:j+1])
```
too slow because time complexity is O(n^3) if using sum() each time, O(n^2) if keeping a running sum.

---

## Key Insight

TODO: What is the insight that makes O(n) possible? Why can you decide at each index whether to extend the running subarray or start fresh?

O(n): at each index, decide whether to extend the previous subarray or start fresh from the current number.
```
nums[i] = nums[i] + max(nums[i - 1], 0)
```
if nums[i-1] > 0, keep it because it helps increase the sum.
if num[i-1] <= 0, drop it because it makes the sum worse.

---

## Final Algorithm

1. Set `nums[0]` as the starting point (no change needed).
2. For each index `i` from 1 to `len(nums) - 1`:
   - `nums[i] = nums[i] + max(nums[i - 1], 0)`
   - This stores the maximum subarray sum ending exactly at `i`.
3. Return `max(nums)` — the best ending-sum across all positions.

---

## Correctness Argument

TODO: Why does this algorithm never miss the optimal subarray? Specifically: why is `max(nums[i - 1], 0)` the right choice at each step?

Because any subarray ending at i has only two choices: either it starts at i: nums[i]
or it extends a best subarray ending at i - 1: nums[i - 1] + nums[i]

If the previous best sum is positive, extending it makes the current sum larger.
If the previous best sum is zero or negative, extending it does not help, so we start over at the current number.

---

## Complexity

- **Time:** O(n) — single pass through `nums`, plus one `max()` call which is also O(n).
- **Space:** O(1) — two scalars (`i` and the loop variable); the array is modified in place.

---

## Edge Cases

- **All negative:** `max(nums[i-1], 0)` never adds a negative prefix, so each element stays as-is. `max(nums)` returns the least-negative element. ✓
- **Single element:** loop body never executes; `max(nums)` returns `nums[0]`. ✓
- **All positive:** prefix is always positive, so every element accumulates the full running sum. ✓

---

## Mistakes Made

TODO: What bugs or wrong turns did you hit during this session? What did each one teach you?

nums[i] no longer means the original number. It becomes the maximum subarray sum ending at index i.

---

## How to Recognize This Pattern Next Time

TODO: What is the signature of a problem that calls for this technique? What keywords or constraints should trigger "track the best subarray ending here"?
