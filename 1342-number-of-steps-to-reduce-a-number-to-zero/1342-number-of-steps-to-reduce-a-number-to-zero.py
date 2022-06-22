class Solution:
    def numberOfSteps(self, num: int) -> int:
        n, step = num, 0
        while n != 0:
            if n % 2 == 0:
                step += 1
                n //= 2
            else:
                step += 1
                n -= 1
        return step
        