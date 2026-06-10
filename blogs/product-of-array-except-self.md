# Product of Array Except Self

**Problem:** LeetCode 238 — Medium  
**Date:** 2026-06-10  
**Language:** Python

---

## Problem Summary

Given an integer array `nums`, return an array `answer` where `answer[i]` is the product of all elements except `nums[i]`. Must run in O(n) time with no division.

---

## Initial Intuition

<!-- Write in your own words: what did you think of first when you read the problem? -->

---

## Brute Force

<!-- Describe what you coded first and why. What is its time complexity? -->

---

## Key Insight

<!-- What is the insight that makes O(n) possible without division? State the invariant explicitly. -->

---

## Final Algorithm

1. Initialize `answer = [1] * n`.
2. Left pass (forward): for each `i`, store the running prefix product in `answer[i]`, then multiply the prefix by `nums[i]`.
3. Right pass (backward): for each `j` from `n-1` to `0`, multiply `answer[j]` by the running suffix product, then multiply the suffix by `nums[j]`.
4. Return `answer`.

---

## Correctness Argument

<!-- Why does answer[j] hold the correct value after both passes? -->

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

<!-- What bugs did you introduce, and what caused them? -->

---

## How to Recognize the Pattern Next Time

<!-- What is the trigger for reaching for prefix/suffix products in a future problem? -->
