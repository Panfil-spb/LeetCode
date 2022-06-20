class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1
        j = i = t = 0
        max = 0
        for i in range(len(s)):
            while j < len(s):
                sub = s[i:j+1]
                if len(set(sub)) == len(sub):
                    if len(sub) > max:
                        max = len(sub)
                    j += 1
                else:
                    t = j
                    break
        return max
        
                    
                
            
        