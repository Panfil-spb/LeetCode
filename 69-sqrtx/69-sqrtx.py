class Solution:
    def mySqrt(self, x: int) -> int:
        res = 0
        while res <= x:
            if res * res == x:
                return res
            elif (res + 1) * (res + 1) > x:
                return res
            else:
                res += 1
        