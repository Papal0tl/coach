# Rotate Image (LC 48)

## Problem Summary

Given an `n × n` matrix, rotate it 90° clockwise in-place. No extra matrix allowed.

## Initial Intuition

<!-- Write in your own words: what was your first thought when you saw the problem? -->

## Brute Force

<!-- Write in your own words: what would the simplest (non-in-place) solution look like? -->

## Key Insight

<!-- Write in your own words: what was the key realization that made an in-place solution possible? -->

## Final Algorithm

4-way cycle over rings:

```
for i in range(n//2):
    for j in range(i, n-i-1):
        tmp = matrix[i][j]
        matrix[i][j]           = matrix[n-1-j][i]
        matrix[n-1-j][i]       = matrix[n-1-i][n-1-j]
        matrix[n-1-i][n-1-j]   = matrix[j][n-1-i]
        matrix[j][n-1-i]       = tmp
```

## Correctness Argument

<!-- Write in your own words: why does this produce a correct 90° CW rotation? Name the four positions in the cycle and explain why the assignments are in the right order. -->

## Complexity

- Time: O(n²) — every element moved exactly once.
- Space: O(1) — one `tmp` variable; fully in-place.

## Edge Cases

- 1×1: outer loop `range(1//2) = range(0)` — no iterations, matrix unchanged. Correct.
- 2×2: one ring, one position (i=0, j=0) — one 4-way swap of the four corners. Correct.

## Mistakes Made

<!-- Write in your own words: what went wrong during your attempt, if anything? -->

## How to Recognize the Pattern Next Time

<!-- Write in your own words: what cues in a future problem would tell you to reach for this approach? -->
