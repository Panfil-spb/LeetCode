class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        dd = {}
        
        for i in nums1:
            dd[i] = dd.get(i, 0) + 1
        
        
        for j in nums2:
            if dd.get(j, 0) != 0:
                res.append(j)
                dd[j] = dd[j] - 1
        
        return res