class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum_so_far = nums[0]
        curr_sum = nums[0]
        for i in range(1, len(nums)):
            curr_sum = max(nums[i], curr_sum + nums[i])
            max_sum_so_far = max(curr_sum, max_sum_so_far)
        return max_sum_so_far
            
        