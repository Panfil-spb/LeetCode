class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        d = collections.Counter(s1)
        for i in range(0, len(s2) - len(s1) + 1):
                d2 = collections.Counter(s2[i:i+len(s1)])
                if d == d2:
                    return True
        return False
    
        