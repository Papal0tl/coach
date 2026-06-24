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
| Reaches shrinking-boundary approach | Yes — independently, without prompting |
| Correct traversal ranges (no off-by-one) | Yes |
| Guard conditions on left/up passes | Yes — in first complete attempt |
| Handles single-row input | Yes — passes tests |
| Handles single-column input | Yes — passes tests |
| Handles 1×1 input | Yes — passes tests |
| Clean termination condition | Yes |
