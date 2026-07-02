# Rubric — Search a 2D Matrix II

## Skill Targets

- **Corner selection**: recognizes that top-right (or bottom-left) is the uniquely useful starting point because it supports one-dimensional elimination.
- **Elimination reasoning**: can explain why `> target` eliminates a column and `< target` eliminates a row (not the other way around).
- **Loop bounds**: correct while condition (`r < m and c >= 0`); no off-by-one.
- **Invariant articulation**: can state that target, if it exists, is always in the remaining submatrix bounded by current `(r, c)`.
- **Complexity**: states O(m+n) time and explains why (at most m+n steps, each shrinking one dimension by 1).
- **Brute force awareness**: can describe O(m*n) brute force and O(m log n) binary-search-per-row as alternatives.
- **Edge cases**: 1×1 matrix, target out of range, target at corners, single row/column.

## Evaluation

| Criterion | Result |
|---|---|
| Selects a useful starting corner (not top-left or center) | Yes — top-right chosen independently |
| Correct elimination direction for > and < cases | Yes — correct on first complete attempt |
| While loop bounds correct | Yes — `i < m and j >= 0` correct, no off-by-one |
| Identifies or states the invariant | Partial — explained elimination reasoning correctly in conversation; blog correctness argument written correctly after prompting |
| States O(m+n) and justifies it | Yes — stated O(m+n) and explained why |
| Handles edge cases without special-casing | Yes — all test cases pass including 1×1, single row/col, corners |
