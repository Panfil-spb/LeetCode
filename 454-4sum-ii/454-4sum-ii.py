class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :type nums4: List[int]
        :rtype: int
        """
        ans = 0
        d = {}
        
        for i in nums1:
            for j in nums2:
                num = i + j
                if num in d:
                    d[num] += 1
                else:
                    d[num] = 1
        
        for i in nums3:
            for j in nums4:
                num = -(i + j)
                if num in d:
                    ans += d[num]

                    
        return ans
        
                
        