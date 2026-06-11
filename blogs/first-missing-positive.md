# First Missing Positive

**Problem**: LC 41 — Hard  
**Date**: 2026-06-11  
**Archive**: archives/2026-06-11-first-missing-positive/

## Problem Summary

Given an unsorted integer array `nums`, return the smallest positive integer not present in it. Must run in O(n) time and O(1) auxiliary space.

## Initial Intuition

Use a set. Put every number into a set, then check from 1 upward until I find the first number not in the set. 
O(n) extra space, violates the requirement.

## Brute Force

1. use a set:
(1) Put every number in nums into a set.
(2) Start from x = 1.
(3) Keep checking whether x exists in the set.
(4) The first x not in the set is the answer.

2. sort the array 
(1) Sort the array 
(2) Scan from left to right to find the first missing positive number.

## Key Insight

The smallest missing positive must be in the range 1 to len(nums) + 1. So for numbers in [1, n]. Any number less than or equal to 0, or greater than n, cannot help deciding the missing number inside the array.

So, use the array itself as a hash map. For a number x, its correct position should be index x - 1. So:
* 1 should be at index 0
* 2 should be at index 1
* 3 should be at index 2

After placing numbers into their correct positions, scan the array. The first index i where nums[i] != i + 1 tells that i + 1 is missing.

## Final Algorithm

1. For each index `i`, while `nums[i]` is in `[1, n]` and `nums[nums[i]-1] != nums[i]`, swap `nums[i]` to its home index `nums[i]-1`.
2. Scan left to right; return the first `i+1` where `nums[i] != i+1`.
3. If all positions satisfy the invariant, return `n+1`.

## Correctness Argument

*(Write in your own words: why does the placement loop terminate? Why does the invariant — `nums[i] == i+1` wherever `i+1` was present — guarantee the scan gives the right answer?)*

Every successful swap puts at least one valid number into its correct home position. A number x in [1, n] belongs at index x - 1.

nums[nums[i] - 1] != nums[i] prevents infinite loops when duplicates exist.

After the placement loop finishes, if a positive integer x in [1, n] exists in the array, then it must be located at index x - 1. Therefore, during the final scan, the first index i where nums[i] != i + 1 means that i + 1 was not present in the array.

If every index is correct, then all numbers from 1 to n are present, so the smallest missing positive integer is n + 1.


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

Forget the duplicate guard: nums[nums[i] - 1] != nums[i]. Without this condition, the code can get stuck swapping duplicate values forever.

Not sure why only care about values from 1 to n: numbers greater than n do not need to be placed because they cannot be the smallest missing positive inside the range we are checking.


## How to Recognize This Pattern Next Time

missing or duplicate numbers, and the numbers are belong to a small fixed range like 1 to n.
