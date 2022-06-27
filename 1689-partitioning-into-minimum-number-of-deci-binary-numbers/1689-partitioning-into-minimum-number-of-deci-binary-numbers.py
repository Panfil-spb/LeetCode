class Solution:
    def minPartitions(self, n: str) -> int:
        res = int(n[0])
        for i in n:
            res = max(res, int(i))
        return res
        