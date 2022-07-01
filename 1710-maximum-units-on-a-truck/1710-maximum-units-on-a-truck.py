class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        res = 0
        boxTypes.sort(key= lambda x: x[1])
        boxTypes = boxTypes[::-1]
        for countBox, size in boxTypes:
            if countBox <= truckSize:
                res += countBox * size
                truckSize -= countBox
            else:
                res += truckSize * size
                truckSize = 0
        return res
        