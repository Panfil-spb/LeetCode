class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        xs = abs(x)
        while xs > 0:
            res = res * 10 + xs % 10
            xs //= 10
            if res >= (2 ** 31):
                return 0
        
        if x >= 0:
            if res > (2 ** 31) - 1:
                return 0
            else:
                return res
        else:
            if -res < (-2 ** 31):
                return 0
            else:
                return -res
        