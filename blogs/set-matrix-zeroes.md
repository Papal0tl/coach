# Set Matrix Zeroes

**Problem**: LC 73 — [Set Matrix Zeroes](https://leetcode.com/problems/set-matrix-zeroes/)  
**Date**: 2026-06-15  
**Difficulty**: Medium

---

## Problem Summary

Given an m×n integer matrix, if any element is 0, set its entire row and column to 0 in-place.

---

## Initial Intuition

<!-- Write in your own words: what was your first instinct when you read the problem? -->

---

## Brute Force

Scan the matrix, record every (row, col) pair where the value is 0, then zero those rows and columns. Space: O(mn) or O(m+n) with two sets.

---

## Key Insight

<!-- Write in your own words: what is the core idea that enables O(1) space? Why does naively zeroing during the scan cause problems? -->

---

## Final Algorithm (O(1) space)

1. Record whether row 0 (`first_row_zero`) or col 0 (`first_col_zero`) originally contain any zero.
2. Scan the interior (rows 1+, cols 1+). For each zero at `(i, j)`, mark `matrix[i][0] = 0` and `matrix[0][j] = 0`.
3. Scan the interior again. Zero `(i, j)` if `matrix[i][0] == 0` or `matrix[0][j] == 0`.
4. If `first_row_zero`, zero all of row 0.
5. If `first_col_zero`, zero all of col 0.

---

## Correctness Argument

<!-- Write in your own words: why does this algorithm produce exactly the right zeros — no more, no less? Focus on the invariant the first row/col markers maintain. -->

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

<!-- Write in your own words: what bugs did you introduce and why? -->

---

## How to Recognize This Pattern Next Time

<!-- Write in your own words: what is the signal that tells you to use the matrix's own first row/col as marker space? -->
