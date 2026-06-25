# Coaching Notes — Rotate Image

## Session

- Date: 2026-06-25
- Problem: LC 48 Rotate Image
- Language: Python
- Mode: hint-only

## Key Insight

A 90° clockwise rotation maps element `(i, j)` to position `(j, n-1-i)`. This can be decomposed into two sequential in-place operations:

1. **Transpose**: swap `matrix[i][j]` with `matrix[j][i]` for all `i < j` (upper triangle only). Maps `(i,j) → (j,i)`.
2. **Reverse each row**: reverses row `j` in-place. Maps `(j,i) → (j, n-1-i)`.

Composing the two steps gives `(i,j) → (j, n-1-i)`, exactly 90° clockwise.

## Invariant

After the transpose, `matrix[i][j] == original[j][i]` for all i, j.  
After the row reversals, `matrix[i][j] == original[j][n-1-i]` for all i, j — which is the 90° CW result.

## Algorithm

```
for i in range(n):
    for j in range(i+1, n):          # upper triangle only
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

for row in matrix:
    row.reverse()
```

## Complexity

- Time: O(n²) — each element touched at most twice (once in transpose, once in reversal).
- Space: O(1) — fully in-place.

## Edge Cases

- 1×1: transpose loop body never executes (j range is empty for i=0); row reversal is a no-op. Correct.
- 2×2: one swap in transpose, then two row reversals. Correct.
- Any n×n: upper-triangle constraint (`j > i`) ensures each pair swapped exactly once.

## Coaching Targets

- Will the user attempt the brute-force extra-matrix approach first?
- Will the user discover the transpose + reverse decomposition independently, or try to figure out the 4-way cycle directly?
- Does the user restrict the transpose loop to the upper triangle (`j in range(i+1, n)`) or inadvertently transpose twice (undoing the work)?
- Does the user get the row-reversal step right vs. column reversal?
- Can the user articulate *why* transpose + reverse equals 90° CW?

## Observations

(Populated during coaching.)
