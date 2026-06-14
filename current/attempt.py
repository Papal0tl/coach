from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        first_row_zero = false
        first_col_zero = false

        for i in range(m):
            if matrix[i][0] == 0:
                first_row_zero = True

        for j in range(n):
            if matrix[0][j] == 0:
                first_col_zero = True

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(m):
            for j in range(n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

