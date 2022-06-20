class Solution:
    def longestPalindrome(self, s: str) -> str:
        j = i = t = 0
        sub_max = s[0]
        sub_len = 0
        for i in range(len(s)):
            l = r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > sub_len:
                    sub_max = s[l:r+1]
                    sub_len = r - l + 1
                l -= 1
                r += 1
            
            l, r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > sub_len:
                    sub_max = s[l:r+1]
                    sub_len = r - l + 1
                l -= 1
                r += 1
            
            
                
                
        return sub_max
        