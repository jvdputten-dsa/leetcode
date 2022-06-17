class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        largest_sum = nums[0]
        cur_sum = 0

        for num in nums:
            cur_sum = max(cur_sum, 0)
            cur_sum += num
            largest_sum = max(largest_sum, cur_sum)
        return largest_sum