class Solution:
    def fib(self, n: int) -> int:
        f0 = 0
        f1 = 1
        if n == 1 or n == 2:
            return 1
        elif n == 0:
            return 0
        for i in range(1, n):
            f = f0 + f1
            f0 = f1
            f1 = f
        return f1
        