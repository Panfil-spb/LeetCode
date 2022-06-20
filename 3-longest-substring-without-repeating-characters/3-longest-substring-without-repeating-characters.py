class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1
        j = i = 0
        max = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                if len(set(s[i:j+1])) == len(s[i:j+1]):
                    if len(s[i:j+1]) > max:
                        max = len(s[i:j+1])
                else:
                    break
        return max
        
                    
                
            
        