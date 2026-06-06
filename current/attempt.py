from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        lst = []
        for i in range (n):
            lst = nums[-i:] + nums[:i]
        return lst