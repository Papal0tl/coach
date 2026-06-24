# Coaching Notes — Spiral Matrix

## Session

- Date: 2026-06-17
- Problem: LC 54 Spiral Matrix
- Language: Python
- Mode: hint-only

## Key Insight

Peel the matrix layer by layer using shrinking boundaries (top, bottom, left, right).
Each round visits the outermost ring in order: right → down → left → up.
After each direction, shrink the corresponding boundary inward.

## Invariant

At the start of each iteration, `matrix[top..bottom][left..right]` is exactly the unvisited sub-matrix.

## Algorithm

```
while top <= bottom and left <= right:
    traverse right along row `top`  ; top += 1
    traverse down along col `right` ; right -= 1
    if top <= bottom:  traverse left along row `bottom` ; bottom -= 1
    if left <= right:  traverse up along col `left`     ; left += 1
```

The guards `if top <= bottom` and `if left <= right` prevent double-counting the final single row or column.

## Complexity

- Time: O(m × n) — every element visited exactly once.
- Space: O(1) auxiliary (output list excluded).

## Edge Cases

- 1×1: one element, collected in the "right" pass; all other passes are empty.
- Single row (m=1): after "right" pass, top > bottom, left/up guards fire correctly.
- Single column (n=1): after "down" pass, left > right, left/up guards fire correctly.

## Coaching Targets

- Will the user reach for shrinking-boundary simulation or try direction arrays + visited set?
- Can they write the boundary-shrink guard conditions without off-by-one?
- Do they catch the double-counting risk on the last row/column?
- Do they handle single-row and single-column inputs?

## Observations

- User independently reached shrinking-boundary simulation on first complete attempt — did not try direction-array + visited-set approach.
- Guard conditions (`if top <= bottom`, `if left <= right`) were present in the first complete attempt without prompting.
- Two bugs: typo `amd` → `and` on while line; `right += 1` should be `right -= 1` (wrong boundary direction). Neither self-caught; both fixed quickly after one hint each.
- All 6 tests passed after fixes including single-row, single-column, 1×1, 2×2.
- Blog: correctness argument explained guards correctly; invariant not named explicitly. Mistakes section removed (user declined to correct inaccurate content).
- Self-catching pattern continues: 6 of 8 sessions with uncaught bugs.
