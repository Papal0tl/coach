import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from agent_solution import Solution

s = Solution()

# Provided examples
assert s.firstMissingPositive([1, 2, 0]) == 3
assert s.firstMissingPositive([3, 4, -1, 1]) == 2
assert s.firstMissingPositive([7, 8, 9, 11, 12]) == 1

# All negatives / zeros
assert s.firstMissingPositive([-1, -2, 0]) == 1

# Single element
assert s.firstMissingPositive([1]) == 2
assert s.firstMissingPositive([2]) == 1

# Complete prefix 1..n
assert s.firstMissingPositive([1, 2, 3, 4, 5]) == 6

# Duplicates
assert s.firstMissingPositive([1, 1, 2, 2]) == 3

# Gap in the middle
assert s.firstMissingPositive([1, 3]) == 2

# Large values beyond n
assert s.firstMissingPositive([100, 200, 300]) == 1

print("All tests passed.")
