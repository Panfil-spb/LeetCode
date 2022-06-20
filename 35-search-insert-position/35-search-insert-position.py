class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        elif target < nums[0]:
            return 0
        elif target > nums[-1]:
            return len(nums)
        else:
            for i in range(len(nums)):
                if nums[i] < target and nums[i+1] > target:
                    return i + 1
        