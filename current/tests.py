import copy
from agent_solution import Solution

s = Solution()


def check(matrix, expected):
    m = copy.deepcopy(matrix)
    s.rotate(m)
    assert m == expected, f"got {m}, want {expected}"


# Provided examples
check([[1,2,3],[4,5,6],[7,8,9]], [[7,4,1],[8,5,2],[9,6,3]])
check(
    [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]],
    [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]],
)

# Edge cases
check([[1]], [[1]])                          # 1×1
check([[1,2],[3,4]], [[3,1],[4,2]])          # 2×2
check([[1,2,3],[4,5,6],[7,8,9]], [[7,4,1],[8,5,2],[9,6,3]])  # 3×3 repeated

print("All tests passed.")
