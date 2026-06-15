# Session Notes — set-matrix-zeroes

## Session Info
- Date: 2026-06-14
- Mode: hint-only

## Key Insight

Detection and mutation must be separated. If you zero a row/col during the scan, newly placed zeros corrupt subsequent detection — a cell that was originally non-zero gets treated as a zero source.

## Invariant

After pass 1: `zero_rows` and `zero_cols` contain exactly the rows and columns that had an original zero. No scan has yet mutated the matrix. After pass 2: every cell whose row or col appears in those sets is zero.

For the O(1) variant: the first row and first column are repurposed as the marker arrays. `matrix[i][0] == 0` means row i must be zeroed; `matrix[0][j] == 0` means col j must be zeroed. But since the first row/col are themselves subject to zeroing, their original zero-status must be saved before being overwritten.

## Complexity

- O(mn) time (two full scans).
- O(m+n) space for the set-based solution.
- O(1) space for the first-row/col marker solution.

## Edge Cases

- Zero in the first row or first column (O(1) solution must save these before using row/col as markers).
- Single-element matrix: [[0]] and [[1]].
- Single row or single column.
- No zeros at all — matrix unchanged.
- All zeros — entire matrix stays zero.

## Coaching Log

- User jumped straight to O(1) marker approach without attempting O(m+n) first — strongest space-instinct shown yet.
- Bug 1: `false` → `False` (syntax). Not self-caught.
- Bug 2: Marking and zeroing loops started at (0,0), causing cascade corruption of col-0 markers. Identified after two trace prompts ("what happens to matrix[1][0] at j=0?"). User correctly named the root cause: "overwrite marker cells while still relying on them."
- Bug 3: Detection loops had swapped variable names (`first_row_zero` set by col-0 scan, `first_col_zero` set by row-0 scan). Not self-caught; identified after hint asking which dimension each loop scans.
- Bug 4: `range(n)` → `range(m)` in final col cleanup. Caught quickly after prompt.
- Blog: correctness argument was solid (iff condition stated correctly). "How to Recognize" needed one revision — revised well, added four-step signal and generalised to "repurpose input structure under strict space constraint."
- 5 of 7 sessions with uncaught bugs before reporting. Intervention still needed: ask user to trace a concrete example before first feedback request.
