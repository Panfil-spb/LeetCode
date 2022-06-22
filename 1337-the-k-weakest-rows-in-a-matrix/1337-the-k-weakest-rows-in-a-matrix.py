class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        sums = [[sum(el), i] for i, el in enumerate(mat)]
        sums.sort()
        return [sums[i][1] for i in range(k)]
            