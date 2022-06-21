class Solution:
    def myAtoi(self, s: str) -> int:

        num = s.strip()
        if len(num) == 0:
            return 0
        dig = 1
        if num[0] == '-':
            dig = -dig
            num = num[1:]
        elif num[0] == '+':
            num = num[1:]
        
        res = 0
        for i in num:
            if i.isnumeric():
                res = res * 10 + int(i)
            else:
                break
        res = res * dig
        if res > 0 and res > 2 ** 31 - 1:
            return 2 ** 31 - 1
        elif res < 0 and res < -2 ** 31:
            return -2 ** 31
        else:
            return res