# Agent reference solution — do not read until after your attempt.

from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        # Step 1: transpose — swap upper triangle with lower triangle
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Step 2: reverse each row
        for row in matrix:
            row.reverse()
