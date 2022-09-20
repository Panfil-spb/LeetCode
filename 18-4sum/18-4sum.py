class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans = []
        nums.sort()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                l = j + 1
                r = len(nums) - 1
                
                while(l < r):
                    if nums[i] + nums[j] + nums[l] + nums[r] == target:
                        ans.append((nums[i], nums[j], nums[l], nums[r]))
                        l += 1
                        r -= 1
                    elif nums[i] + nums[j] + nums[l] + nums[r] > target:
                        r -= 1
                    else:
                        l += 1
        return set(ans)