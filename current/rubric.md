# Rubric — Rotate Image

## Skill Targets

- **In-place recognition**: understands that allocating a full copy is disallowed and finds a decomposition that avoids it.
- **Decomposition discovery**: reaches transpose + reverse-rows (or equivalent 4-way cycle) independently.
- **Transpose correctness**: loops only over the upper triangle (`j in range(i+1, n)`) so each pair is swapped exactly once.
- **Row reversal vs. column reversal**: correctly reverses each row (not each column) after transposing.
- **Index arithmetic**: no off-by-one in the transpose bounds.
- **Edge cases**: 1×1 and 2×2 handled without special-casing.
- **Invariant articulation**: can explain why the two-step decomposition produces 90° CW.

## Evaluation

| Criterion | Result |
|---|---|
| Reaches in-place decomposition (no extra matrix) | — |
| Correct approach: transpose + reverse-rows or 4-way cycle | — |
| Upper-triangle-only transpose (no double-swap) | — |
| Correct direction: row reversal (not column) after transpose | — |
| No off-by-one in loop bounds | — |
| Handles 1×1 without special case | — |
| Handles 2×2 correctly | — |
| Can articulate why decomposition works | — |
