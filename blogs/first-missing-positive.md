# First Missing Positive

**Problem**: LC 41 — Hard  
**Date**: 2026-06-11  
**Archive**: archives/2026-06-11-first-missing-positive/

## Problem Summary

Given an unsorted integer array `nums`, return the smallest positive integer not present in it. Must run in O(n) time and O(1) auxiliary space.

## Initial Intuition

*(Write in your own words: what did you reach for first? A set? Sorting? Why?)*

## Brute Force

*(Describe the O(n) space or O(n log n) approach and why it violates the constraints.)*

## Key Insight

*(Write in your own words: what is the key observation that makes O(1) space possible? What bound on the answer matters?)*

## Final Algorithm

1. For each index `i`, while `nums[i]` is in `[1, n]` and `nums[nums[i]-1] != nums[i]`, swap `nums[i]` to its home index `nums[i]-1`.
2. Scan left to right; return the first `i+1` where `nums[i] != i+1`.
3. If all positions satisfy the invariant, return `n+1`.

## Correctness Argument

*(Write in your own words: why does the placement loop terminate? Why does the invariant — `nums[i] == i+1` wherever `i+1` was present — guarantee the scan gives the right answer?)*

## Complexity

- Time: O(n) — each element is moved to its home at most once; total swaps across all iterations is bounded by n.
- Space: O(1) auxiliary — in-place swaps only.

## Edge Cases

- All non-positive (`[-1, -2, 0]`) → 1
- `[1]` → 2; `[2]` → 1
- Complete prefix `[1, 2, ..., n]` → n+1
- Duplicates (`[1, 1, 2, 2]`) → duplicate guard prevents infinite loop
- All values > n (`[100, 200]`) → 1

## Mistakes Made

*(Write in your own words: what bugs did you hit or nearly hit? What did tracing reveal?)*

## How to Recognize This Pattern Next Time

*(Write in your own words: what is the trigger for "use the array as its own hash map"? What family of problems uses this?)*
