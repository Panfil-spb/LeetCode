# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r = 1, n
        while l <= r:
            p = (r + l) // 2
            res = isBadVersion(p)
            if(res):
                r = p - 1
            else:
                l = p + 1
            if l > r:
                return l
            
            
            
                
        