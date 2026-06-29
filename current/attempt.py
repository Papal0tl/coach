from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        for i in range(n//2):
            for j in range(i, n - i - 1):
                tmp = matrix[i][j]
                # top = left
                matrix[i][j] = matrix[n - 1 - j][i]
                # left = bottom
                matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 - j]
                # bottom = right
                matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 -i]
                # right = old top
                matrix[j][n - 1 -i] = tmp

            