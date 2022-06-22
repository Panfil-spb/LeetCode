class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        j = i = 0
        mas = []
        while i < m or j < n:
            if i < m and j < n:
                if nums1[i] < nums2[j]:
                    mas.append(nums1[i])
                    i += 1
                else:
                    mas.append(nums2[j])
                    j += 1
            elif i >= m and j < n:
                mas.append(nums2[j])
                j += 1
            elif j >= n and i < m:
                mas.append(nums1[i])
                i += 1
        
        for i in range(len(nums1)):
            nums1.pop()
        for i in mas:
            nums1.append(i)
            
                
            
                

            
            
        