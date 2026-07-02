# LC 240 — Search a 2D Matrix II

https://leetcode.cn/problems/search-a-2d-matrix-ii/

## Problem

Write an efficient algorithm that searches for a value `target` in an `m x n` integer matrix. The matrix has the following properties:

- Integers in each row are sorted in ascending order from left to right.
- Integers in each column are sorted in ascending order from top to bottom.

Return `true` if `target` exists in the matrix, `false` otherwise.

## Examples

**Example 1:**
```
matrix = [
  [1,  4,  7, 11, 15],
  [2,  5,  8, 12, 19],
  [3,  6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
target = 5
Output: true
```

**Example 2:**
```
matrix = [
  [1,  4,  7, 11, 19],
  [2,  5,  8, 12, 20],
  [3,  6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
target = 20
Output: false
```

## Constraints

- `m == matrix.length`
- `n == matrix[i].length`
- `1 <= m, n <= 300`
- `-10^9 <= matrix[i][j] <= 10^9`
- All integers in each row are sorted in ascending order.
- All integers in each column are sorted in ascending order.
- `-10^9 <= target <= 10^9`
