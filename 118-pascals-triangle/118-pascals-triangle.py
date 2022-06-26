class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for i in range(1, numRows+1):
            res.append([])
            for j in range(i):
                if j == 0 or j == i - 1:
                    res[i-1].append(1)
                else:
                    res[i-1].append(res[i-2][j] + res[i-2][j-1])
        return res
                    
        