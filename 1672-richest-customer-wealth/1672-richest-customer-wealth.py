class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_sum = sum(accounts[0])
        for i in range(1, len(accounts)): 
            max_sum = max(sum(accounts[i]), max_sum)
        return max_sum
        