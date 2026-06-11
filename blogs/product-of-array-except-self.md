# Product of Array Except Self

**Problem:** LeetCode 238 — Medium  
**Date:** 2026-06-10  
**Language:** Python

---

## Problem Summary

Given an integer array `nums`, return an array `answer` where `answer[i]` is the product of all elements except `nums[i]`. Must run in O(n) time with no division.

---

## Initial Intuition

calculate the total product of the array and then divide by nums[i] for each position.
OR directly multiply all elements except the current one for every index, but that seemed inefficient because it repeats a lot of work.

---

## Brute Force

For each index i, iterate through the entire array and multiply every element except nums[i].

```
for i in range(n):
    product = 1
    for j in range(n):
        if i != j:
            product *= nums[j]
    answer[i] = product
```

Time Complexity: O(n²) because for every index we scan the whole array again.

Space Complexity: O(1) excluding the output array.

---

## Key Insight

For each position i, the answer can be split into two parts: (product of all elements to the left of i) × (product of all elements to the right of i)

don't need to recompute these products repeatedly, can build them incrementally.

precise invariant: 
```
At the moment answer[i] = left executes, left holds the product of nums[0..i-1], exclusive of nums[i] itself. 
```
So after the left pass, 
```
answer[i] = product of all elements to the left of i. 
```
Then in the right pass, 
```
At the moment answer[j] *= right executes, right holds the product of nums[j+1..n-1],exclusive of nums[j] itself. 
```
Therefore, answer[j] = left product × right product.

---

## Final Algorithm

1. Initialize `answer = [1] * n`.
2. Left pass (forward): for each `i`, store the running prefix product in `answer[i]`, then multiply the prefix by `nums[i]`.
3. Right pass (backward): for each `j` from `n-1` to `0`, multiply `answer[j]` by the running suffix product, then multiply the suffix by `nums[j]`.
4. Return `answer`.

---

## Correctness Argument

<!-- Why does answer[j] hold the correct value after both passes? -->
After first pass: answer[i] = product of all elements to the left of i => stores the running prefix product before nums[i] is included.

During second pass: right = product of all elements to the right of j  => traverse from right to left and update right after processing the current index.

So, when execute: answer[j] *= right, =>  (left product) × (right product). Contains every element except nums[j].

---

## Complexity

- Time: O(n) — two linear passes, no nested loops.
- Space: O(1) extra — the output array is reused; no separate prefix/suffix arrays allocated.

---

## Edge Cases

- Single zero: only the position of the zero gets a nonzero output (the product of all other elements); all other positions become 0.
- Two or more zeros: the entire output is 0.
- Negative numbers: no special handling needed; sign propagates naturally through multiplication.
- Minimum length (n = 2): both passes work correctly.

---

## Mistakes Made

Use the wrong algorithm. The time complexity is too large (O(n^2))

Originally wrote: answer[j] = right during right pass => Overwrite the left product that has been already stored in answer[j].
Fixed: answer[j] *= right.

using nums[i] instead of nums[j] in the right pass. The right pass iterates using j not i.

---

## How to Recognize the Pattern Next Time

Asks for information about every position in an array.
The answer for index i depends on elements before and after i.
Recompute left and right parts separately for every index would lead to O(n²).
Division is forbidden because of zeros.
The operation is associative (multiplication, sum, min/max with appropriate preprocessing, etc.).
