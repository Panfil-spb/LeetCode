class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        res = [[]]
        ri = 0
        rj = 0
        l = 0
        for i in mat:
            l += len(i)
            for j in i:
                res[ri].append(j)
                rj += 1
                if rj == c:
                    res.append([])
                    ri += 1
                    rj = 0
        if l == r * c:
            res.pop()
            return res
        else:
            return mat
        