from agent_solution import Solution

s = Solution()

# Provided examples
assert s.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]) == [1,2,3,6,9,8,7,4,5]
assert s.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]) == [1,2,3,4,8,12,11,10,9,5,6,7]

# Edge cases
assert s.spiralOrder([[1]]) == [1]                         # 1x1
assert s.spiralOrder([[1,2,3]]) == [1,2,3]                 # single row
assert s.spiralOrder([[1],[2],[3]]) == [1,2,3]             # single column
assert s.spiralOrder([[1,2],[3,4]]) == [1,2,4,3]           # 2x2

print("All tests passed.")
