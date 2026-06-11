from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            while 1 <= nums[i]:
                
        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1
            
        return n + 1
