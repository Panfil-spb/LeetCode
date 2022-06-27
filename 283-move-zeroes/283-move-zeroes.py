class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = 0
        res = []
        
        for i in nums:
            if i != 0:
                res.append(i)
            else:
                count += 1
        
        for i in range(count):
            res.append(0)
        
        for i in range(len(nums)):
            nums[i] = res[i]
        
        return nums
        