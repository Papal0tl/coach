# Agent reference solution — do not read until after your own attempt.
#
# Pattern: prefix/suffix product arrays (two-pass)
# Time:  O(n)
# Space: O(1) extra (output array excluded per LeetCode convention)

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n

        # Left pass: answer[i] holds product of nums[0..i-1]
        prefix = 1
        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]

        # Right pass: multiply answer[i] by product of nums[i+1..n-1]
        suffix = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]

        return answer
