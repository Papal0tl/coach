from agent_solution import Solution

s = Solution()

M = [
    [1,  4,  7, 11, 15],
    [2,  5,  8, 12, 19],
    [3,  6,  9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30],
]

# Provided examples
assert s.searchMatrix(M, 5) is True
assert s.searchMatrix(M, 20) is False

# Corners
assert s.searchMatrix(M, 1) is True   # top-left
assert s.searchMatrix(M, 30) is True  # bottom-right
assert s.searchMatrix(M, 15) is True  # top-right (found immediately)
assert s.searchMatrix(M, 18) is True  # bottom-left

# Out of range
assert s.searchMatrix(M, 0) is False   # smaller than all
assert s.searchMatrix(M, 31) is False  # larger than all

# 1×1 matrix
assert s.searchMatrix([[7]], 7) is True
assert s.searchMatrix([[7]], 5) is False

# Single row
assert s.searchMatrix([[1, 3, 5, 7]], 5) is True
assert s.searchMatrix([[1, 3, 5, 7]], 4) is False

# Single column
assert s.searchMatrix([[2], [4], [6]], 4) is True
assert s.searchMatrix([[2], [4], [6]], 5) is False

# Negative values
assert s.searchMatrix([[-5, -3], [-1, 0]], -3) is True
assert s.searchMatrix([[-5, -3], [-1, 0]], -4) is False

print("All tests passed.")
