class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        mas = []
        i = j = 0
        while i < len(nums1):
            if j >= len(nums2):
                for k in range(i, len(nums1)):
                    mas.append(nums1[k])
                break
            if nums1[i] < nums2[j]:
                mas.append(nums1[i])
                i += 1
            else:
                mas.append(nums2[j])
                j += 1
        for k in range(j, len(nums2)):
            mas.append(nums2[k])
        
        if len(mas) % 2 == 0:
            return (mas[len(mas) // 2] + mas[len(mas) // 2 - 1]) / 2
        else:
            return mas[len(mas) // 2]
        