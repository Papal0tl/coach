# Spiral Matrix (LC 54)

## Problem Summary
Given an m×n matrix, return all elements in spiral order (right → down → left → up, peeling inward layer by layer).

## Initial Intuition
<!-- Write in your own words: what did you think of first when you saw this problem? -->

## Brute Force
<!-- Write in your own words: what would a naive approach look like? -->

## Key Insight
<!-- Write in your own words: what is the core idea that makes the solution work? -->

## Final Algorithm
Maintain four boundaries: top, bottom, left, right.
While top ≤ bottom and left ≤ right:
  1. Traverse right along row `top`; top += 1
  2. Traverse down along col `right`; right -= 1
  3. If top ≤ bottom: traverse left along row `bottom`; bottom -= 1
  4. If left ≤ right: traverse up along col `left`; left += 1

## Correctness Argument
<!-- Write in your own words: why do the two guards (if top <= bottom, if left <= right) prevent double-counting the last row or column? -->

## Complexity
- Time: O(m × n) — every element visited exactly once.
- Space: O(1) auxiliary (output list not counted).

## Edge Cases
- 1×1: single element collected in step 1; steps 2–4 are empty.
- Single row (m=1): after step 1, top > bottom; guards block steps 3 and 4.
- Single column (n=1): after step 2, left > right; guards block steps 3 and 4.

## Mistakes Made
<!-- Write in your own words: what bugs did you introduce and how did you catch them? -->

## How to Recognize This Pattern Next Time
<!-- Write in your own words: what cues in a future problem would make you reach for shrinking-boundary simulation? -->
