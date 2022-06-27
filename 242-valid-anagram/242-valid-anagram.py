class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count1 = collections.Counter(s)
        count2 = collections.Counter(t)
    
        for i in max(s ,t):
            if count1[i] != count2[i]:
                return False
        return True
                
        