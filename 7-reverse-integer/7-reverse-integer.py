class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        xs = str(abs(x))
        for i in range(len(xs)):
            res += int(xs[i]) * (10 ** i)
        
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
        