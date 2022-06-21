class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        res = [[] for i in range(numRows)]
        
        i = 0
        step = 1
        for el in s:
            res[i].append(el)
            i += step
            if i == 0 or i == numRows - 1:
                step *= -1
        st = ""
        for j in res:
            for k in j:
                st += k
        return st
            
        
        