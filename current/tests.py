from agent_solution import Solution

sol = Solution()


def check(nums, k, expected):
    sol.rotate(nums, k)
    assert nums == expected, f"got {nums}, want {expected}"


# provided examples
check([1, 2, 3, 4, 5, 6, 7], 3, [5, 6, 7, 1, 2, 3, 4])
check([-1, -100, 3, 99], 2, [3, 99, -1, -100])

# k = 0: no change
check([1, 2, 3], 0, [1, 2, 3])

# k = n: full rotation, back to original
check([1, 2, 3], 3, [1, 2, 3])

# k > n: wraps around
check([1, 2, 3], 4, [3, 1, 2])

# single element
check([42], 0, [42])
check([42], 7, [42])

# two elements
check([1, 2], 1, [2, 1])
check([1, 2], 2, [1, 2])

# k = n - 1: last element moves to front
check([1, 2, 3, 4], 3, [2, 3, 4, 1])

print("All tests passed.")
