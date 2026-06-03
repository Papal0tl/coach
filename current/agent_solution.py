def max_subarray(nums: list[int]) -> int:
    current_sum = nums[0]
    max_sum = nums[0]

    for num in nums[1:]:
        # Either extend the running subarray or start fresh at num
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum
