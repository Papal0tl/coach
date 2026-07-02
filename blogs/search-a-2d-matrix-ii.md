# Search a 2D Matrix II

**Problem summary**: Given an m×n integer matrix where every row and every column is sorted in ascending order, return whether `target` exists. Constraints: 1 ≤ m, n ≤ 300.

**Initial intuition**: 
Use the corted property to narrow the search range. First determine a possible row using the first column, then search inside that row. => Not always work as the target may stil in an earlier row.


**Brute force**: 
Check every element one by one. If any element equals 'target', return true. If the whole matrix is scanned and nothing is found, return false.
Time complexity: O(mn)
Space complexity: O(1) 


**Key insight**: 


**Final algorithm**:
1. Start at position `(0, n-1)` — top-right corner.
2. While in bounds (`i < m` and `j >= 0`): if equal return True; if greater move left (`j -= 1`); if smaller move down (`i += 1`).
3. Return False.

**Correctness argument**: 

**Complexity**: Time O(m+n) — each step decrements `j` or increments `i`, at most m+n steps total. Space O(1).

**Edge cases**: 1×1 matrix; target smaller than `matrix[0][0]`; target larger than `matrix[m-1][n-1]`; target at a corner; single row or column.

**Mistakes made**: 


**How to recognize the pattern next time**: 
