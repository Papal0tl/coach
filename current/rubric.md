# Rubric — Spiral Matrix

## Skill Targets

- **Boundary simulation**: independently reach shrinking top/bottom/left/right bounds (vs. direction-array + visited-set approach).
- **Direction cycling**: traverse right → down → left → up with correct range endpoints.
- **Guard conditions**: apply `if top <= bottom` and `if left <= right` before the last two traversals to prevent double-counting.
- **Termination**: `while top <= bottom and left <= right` — exact, no off-by-one.
- **Edge cases**: single row, single column, 1×1 handled without special-casing.

## Evaluation

| Criterion | Result |
|---|---|
| Reaches shrinking-boundary approach | |
| Correct traversal ranges (no off-by-one) | |
| Guard conditions on left/up passes | |
| Handles single-row input | |
| Handles single-column input | |
| Handles 1×1 input | |
| Clean termination condition | |
