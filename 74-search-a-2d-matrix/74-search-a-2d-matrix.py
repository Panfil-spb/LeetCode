class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in matrix:
            if target >= i[0] and target <= i[-1]:
                    for j in i:
                        if j == target:
                            return True
                    return False
        return False
            
                
        