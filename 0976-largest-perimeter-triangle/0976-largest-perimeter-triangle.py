class Solution(object):
    def largestPerimeter(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        

        per = 0
        nums.sort(reverse=True)
        for i in range(0, len(nums)-2):
            a, b, c = nums[i], nums[i+1], nums[i+2]
            if (a+b>c and a+c>b and c+b>a):
                cur = sum([a,b,c])
                per = cur if cur > per else per
        return per
        