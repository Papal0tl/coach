# Rotate Image (LC 48)

## Problem Summary

Given an `n × n` matrix, rotate it 90° clockwise in-place. No extra matrix allowed.

## Initial Intuition

First figure out where each cell should go after a 90° clockwise rotation. For a cell at (row, col), its new position should be (col, n - 1 - row). However, directly assigning each value to its new position would overwrite values that are still needed, so need a way to move values safely in-place.

## Brute Force

Create a new n × n matrix and copy each value to its rotated position:

new[col][n - 1 - row] = matrix[row][col]

After filling the new matrix, we could copy it back into matrix. This works, but it uses O(n²) extra space, which violates the in-place requirement.

## Key Insight

The rotation can be done by moving four related positions at a time. Each cell belongs to a 4-position cycle: top, right, bottom, and left. Instead of using another matrix, we can save one value in tmp and rotate these four values in-place.

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

For each position (i, j) in the current layer, the four cells involved in one clockwise rotation are:

Top: (i, j)
Right: (j, n - 1 - i)
Bottom: (n - 1 - i, n - 1 - j)
Left: (n - 1 - j, i)

These four positions form one rotation cycle. In a clockwise rotation, the values move as:

Left -> Top
Bottom -> Left
Right -> Bottom
Top -> Right

The algorithm first stores the original top value in tmp, then assigns left to top, bottom to left, right to bottom, and finally puts the saved top value into right. This matches the clockwise rotation mapping and prevents any value from being lost.

The outer loop processes each ring of the matrix, and the inner loop processes each position on the top edge of that ring except the last corner, because the last corner is already included in the 4-way cycle.

## Complexity

- Time: O(n²) — every element moved exactly once.
- Space: O(1) — one `tmp` variable; fully in-place.

## Edge Cases

- 1×1: outer loop `range(1//2) = range(0)` — no iterations, matrix unchanged. Correct.
- 2×2: one ring, one position (i=0, j=0) — one 4-way swap of the four corners. Correct.

## Mistakes Made

Did not understand why the outer loop only runs n // 2 times. The matrix is processed one ring at a time, so only half of the layers need to be visited. For odd-sized matrices, the center cell never moves.

Mixed up the four coordinate pairs in the rotation cycle. The correct positions are (i, j), (j, n - 1 - i), (n - 1 - i, n - 1 - j), and (n - 1 - j, i).

the coordinate starts at (0,0) instead of (1,1)

## How to Recognize the Pattern Next Time

The matrix is square.
The transformation is based on coordinates.
The problem requires O(1) extra space.
Direct assignment would overwrite values.
Elements move in repeated cycles around layers or rings.
