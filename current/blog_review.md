# Blog Review — Search a 2D Matrix II

## Correctness

- Problem summary: correct.
- Initial intuition: honest and correct — names the row-scan idea and identifies why it fails (earlier rows can have larger values further right). Minor typo ("corted").
- Brute force: correct. O(mn) time, O(1) space.
- Key insight: correct in substance. Correctly identifies the top-right corner property and the elimination logic (too large → move left, too small → move down). Slight imprecision: "eliminate the current column" should be "eliminate column j from row i downward" — what's eliminated is a partial column, not the full column. Acceptable for a concise blog.
- Final algorithm: pre-filled, correct.
- Correctness argument: **BLANK** — not written. This is required.
- Complexity: correct.
- Edge cases: correct.
- Mistakes made: accurate and specific. First attempt (binary row scan) failure mode is explained clearly.
- How to recognize: good. Names the structural cue (sorted both row-wise and column-wise, corner with opposing directions) and the two valid starting corners.

## Missing

**Correctness argument is blank.** This section must explain why the algorithm never misses the target — specifically, that at every step the target (if it exists) is guaranteed to remain in the submatrix bounded by rows [i, m-1] and columns [0, j]. Without this, the blog does not close the loop on *why* the elimination is safe.

## Clarity

Good overall. The key insight section is the clearest — it connects the corner property directly to the elimination logic. The mistakes section is honest and specific.

## Transfer Readiness

High conditional on the correctness argument being written. The pattern-recognition cue is the strongest in recent sessions — naming the structural condition ("sorted both row-wise and column-wise, corner with opposing move directions") is precise enough to transfer.

## Required Revisions

1. Write the **Correctness argument** section: explain that each elimination step is safe because when `matrix[i][j] > target`, every element in column `j` at rows `i` and below is also `> target` (column sorted), so target cannot be there. Similarly, when `matrix[i][j] < target`, every element in row `i` at columns `0` through `j` is also `< target` (row sorted), so target cannot be there. Therefore the remaining submatrix always contains the target if it exists.

## Final Assessment

Pending revision.