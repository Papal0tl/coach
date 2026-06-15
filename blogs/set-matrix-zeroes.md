# Set Matrix Zeroes

**Problem**: LC 73 — [Set Matrix Zeroes](https://leetcode.com/problems/set-matrix-zeroes/)  
**Date**: 2026-06-15  
**Difficulty**: Medium

---

## Problem Summary

Given an m×n integer matrix, if any element is 0, set its entire row and column to 0 in-place.

---

## Initial Intuition

Scan the matrix and immediately set the row and column to 0 when the loop find a 0. But this is wrong because the new zeros it creates may be treated as original zeros later, causing extra rows and columns to become 0.

---

## Brute Force

Scan the matrix, record every (row, col) pair where the value is 0, then zero those rows and columns. Space: O(mn) or O(m+n) with two sets.

---

## Key Insight

Simply zeroing the matrix on the first scan can cause problems because it creates new zeros that weren't present in the original matrix. These new zeros can incorrectly trigger more rows and columns to be zeroed.

Separate "recording" from "modifying". First, record which rows and columns need to be zeroed. To save O(1) of extra space, the matrix itself can be reused: the first column is used as the row label and the first row is used as the column label. Since the first row and first column are also part of the matrix, two boolean values ​​can be used to record whether they initially contained zeros.


---

## Final Algorithm (O(1) space)

1. Record whether row 0 (`first_row_zero`) or col 0 (`first_col_zero`) originally contain any zero.
2. Scan the interior (rows 1+, cols 1+). For each zero at `(i, j)`, mark `matrix[i][0] = 0` and `matrix[0][j] = 0`.
3. Scan the interior again. Zero `(i, j)` if `matrix[i][0] == 0` or `matrix[0][j] == 0`.
4. If `first_row_zero`, zero all of row 0.
5. If `first_col_zero`, zero all of col 0.

---

## Correctness Argument

After scanning the matrix, `matrix[i][0] == 0` is row `i` originally contained zero, and `matrix[0][j] == 0` is column `j` originally contained zero.

When scanning the matrix again, the value of cell `(i, j)` is set to 0 exactly when its row or column was marked.

The first row and first column are processed last using `first_row_zero` and `first_col_zero`, so they are only set to zero if they originally contained zero. 

---

## Complexity

- Time: O(mn) — four passes over at most the full matrix.
- Space: O(1) — only two booleans; first row and col reused as markers.

---

## Edge Cases

- Zero in `(0, 0)`: captured by both `first_row_zero` and `first_col_zero`; handled correctly in steps 4 and 5.
- Single-element matrix `[[0]]` and `[[1]]`: handled correctly.
- No zeros: nothing changes.
- All zeros: entire matrix stays zero.
- Zero only in first row or only in first col: the saved booleans ensure these are zeroed last, after markers are no longer needed.

---

## Mistakes Made

## Mistakes Made

1. Thought I could immediately zero a row and column as soon as I found a 0. This does not work because the newly created zeros may later be treated as original zeros, causing extra rows and columns to be incorrectly zeroed.

2. Confused about why the first row and first column can be used as markers. They are actually temporary labels that record which rows and columns need to be zeroed later.

3. Did not understand why the scan for markers starts from `(1, 1)` instead of `(0, 0)`. The reason is that the first row and first column are reserved for storing marker information, so modifying them during the scan would destroy the markers.

4. Overlooked the special case of `matrix[0][0]`. Since it belongs to both the first row and the first column, it cannot independently represent whether both should be zeroed. (why `first_row_zero` and `first_col_zero` are needed).

5. Considered zeroing the first row and first column immediately after finding their markers. But doing so would overwrite marker information before it is used, causing incorrect results. They must be processed last.

---

## How to Recognize This Pattern Next Time

1. The input is a matrix.
2. I need to remember information about entire rows and columns.
3. The obvious solution uses O(m+n) extra space (such as two sets or two arrays).
4. The problem explicitly asks for O(1) extra space or in-place modification.

For a matrix, the first column naturally provides one storage location for each row, and the first row naturally provides one storage location for each column. This makes them a perfect replacement for the row-marker and column-marker arrays.

When a problem requires tracking metadata about rows, columns, or indices under a strict space constraint, I should check whether part of the input can be repurposed as bookkeeping space.
