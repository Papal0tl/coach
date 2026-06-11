from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        # Place each number x in [1, n] at index x-1.
        # Invariant: after this phase, nums[i] == i+1 iff i+1 was present.
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                j = nums[i] - 1
                nums[i], nums[j] = nums[j], nums[i]

        # First index where the value is wrong gives the answer.
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        return n + 1
