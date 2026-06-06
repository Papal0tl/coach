from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n  # k >= n is equivalent to k % n steps

        def reverse(l: int, r: int) -> None:
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        reverse(0, n - 1)   # reverse entire array
        reverse(0, k - 1)   # restore first segment (the rotated-in tail)
        reverse(k, n - 1)   # restore second segment (the original head)
