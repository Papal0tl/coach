# Agent reference solution — do not read until after your attempt.

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        r, c = 0, n - 1  # start at top-right corner
        while r < m and c >= 0:
            if matrix[r][c] == target:
                return True
            elif matrix[r][c] > target:
                c -= 1  # target cannot be in this column below
            else:
                r += 1  # target cannot be in this row to the left
        return False
