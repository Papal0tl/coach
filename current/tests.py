from agent_solution import Solution

sol = Solution()


def test(nums, expected):
    result = sol.productExceptSelf(nums)
    assert result == expected, f"nums={nums}\n  got:      {result}\n  expected: {expected}"


# Provided examples
test([1, 2, 3, 4], [24, 12, 8, 6])
test([-1, 1, 0, -3, 3], [0, 0, 9, 0, 0])

# Single zero — only the zero position gets a nonzero product
test([0, 4, 5], [20, 0, 0])

# Two zeros — everything becomes 0
test([0, 0, 3], [0, 0, 0])

# All ones
test([1, 1, 1, 1], [1, 1, 1, 1])

# Minimum length
test([3, 7], [7, 3])

# Negatives
test([-2, -3, 4], [-12, -8, 6])

print("All tests passed.")
