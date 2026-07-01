# Coaching Notes — Search a 2D Matrix II

## Session

- Date: 2026-06-30
- Problem: LC 240 Search a 2D Matrix II
- Language: Python
- Mode: hint-only

## Key Insight

The top-right corner has a unique "bifurcation" property:
- Every element to its left is strictly smaller (row sorted ascending).
- Every element below it is strictly larger (column sorted ascending).

This means at any position `(r, c)`:
- If `matrix[r][c] > target`: target cannot be anywhere in column `c` at or below row `r`, so move left (`c -= 1`).
- If `matrix[r][c] < target`: target cannot be anywhere in row `r` at or to the left of column `c`, so move down (`r += 1`).

Start at the top-right corner. Each step eliminates an entire row or an entire column. After at most `m + n` steps, either the target is found or the pointer exits the matrix.

The bottom-left corner works symmetrically (move right if too small, move up if too large).

## Invariant

At each step, if `target` exists in the matrix, it lies within the submatrix bounded by rows `[r, m-1]` and columns `[0, c]`. Each elimination move shrinks this region by one row or one column without ever excluding the target.

## Algorithm

```
r, c = 0, n - 1          # top-right corner
while r < m and c >= 0:
    if matrix[r][c] == target:  return True
    elif matrix[r][c] > target: c -= 1
    else:                       r += 1
return False
```

## Complexity

- Time: O(m + n) — each step decrements c or increments r, so at most m + n steps total.
- Space: O(1).

## Edge Cases

- 1×1 matrix: one comparison, then either found or both bounds exit. Correct.
- Target smaller than `matrix[0][0]`: first comparison sends `c` left until c < 0. Correct.
- Target larger than `matrix[m-1][n-1]`: pointer walks down until r >= m. Correct.
- Target at top-right corner: found on first comparison.
- Target at bottom-left corner: pointer walks down and left, reaches it. Correct.
- Single row or single column: reduces to a linear scan in one dimension. Correct.

## Observations

- User initially drafted a row-by-row pruning loop (row truncation when element > target) — O(m*n) brute force with early row termination. Incomplete: no equality check, no return value.
- Before testing, switched entirely to the staircase search from the top-right corner. Correct on first complete attempt: bounds, direction logic, and return values all right.
- Explanation was clear and correct: top-right corner has the bifurcation property; each comparison eliminates a full row or column; O(m+n) follows from at most m+n steps.
- Zero bugs in final attempt. All edge cases pass.

## Coaching Targets

- Will the user try brute force first, or jump to binary search per row?
- Will the user discover the staircase search independently, or will they need a nudge about which corner to start from?
- Can the user explain *why* starting from a corner (not center or top-left) enables deterministic elimination?
- Does the user name the invariant (target remains in the shrinking submatrix) or only describe mechanics?
- Does the user handle the `c >= 0` and `r < m` bounds correctly in the while condition?
