class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        start = 0
        res = 0
        
        for i in range(1, len(prices)):
            res = max(res, prices[i] - prices[start])
            
            if prices[i] - prices[start] < 0:
                start = i
        return res
                
        