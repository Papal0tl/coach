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
| Reaches in-place decomposition (no extra matrix) | Yes — stated from the start |
| Correct approach: transpose + reverse-rows or 4-way cycle | Yes — 4-way cycle (stated "transpose+flip" but implemented cycle) |
| Upper-triangle-only transpose (no double-swap) | N/A — used 4-way cycle |
| Correct direction: row reversal (not column) after transpose | N/A — used 4-way cycle |
| No off-by-one in loop bounds | Yes — `range(n//2)` and `range(i, n-i-1)` correct on first attempt |
| Handles 1×1 without special case | Yes |
| Handles 2×2 correctly | Yes |
| Can articulate why decomposition works | Yes — named four positions and explained cycle in blog |
