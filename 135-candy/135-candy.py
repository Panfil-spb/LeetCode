class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        
        if n == 1:
            return 1
        s = 0
        mas1 = [1 for i in ratings]
        mas2 = [1 for i in ratings]
        
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                mas1[i] = mas1[i - 1] + 1
        
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                mas2[i] = mas2[i + 1] + 1
        
        for i in range(n):
            s += max(mas1[i], mas2[i])
        
        return s
            