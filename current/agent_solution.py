from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """O(m+n) space solution — straightforward, two-pass."""
        m, n = len(matrix), len(matrix[0])
        zero_rows: set[int] = set()
        zero_cols: set[int] = set()

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    zero_rows.add(i)
                    zero_cols.add(j)

        for i in range(m):
            for j in range(n):
                if i in zero_rows or j in zero_cols:
                    matrix[i][j] = 0


class SolutionO1:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """O(1) space — use first row/col as markers."""
        m, n = len(matrix), len(matrix[0])

        first_row_zero = any(matrix[0][j] == 0 for j in range(n))
        first_col_zero = any(matrix[i][0] == 0 for i in range(m))

        # Use first row and col to record which rows/cols need zeroing
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # Zero interior based on markers
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # Handle first row and col last, using the saved booleans
        if first_row_zero:
            for j in range(n):
                matrix[0][j] = 0
        if first_col_zero:
            for i in range(m):
                matrix[i][0] = 0
