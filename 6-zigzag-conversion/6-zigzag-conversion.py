class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        res = ["" for i in range(numRows)]
        
        i = 0
        step = 1
        for el in s:
            res[i] += el
            i += step
            if i == 0 or i == numRows - 1:
                step *= -1
        st = "".join(el for el in res)

        return st
            
        
        