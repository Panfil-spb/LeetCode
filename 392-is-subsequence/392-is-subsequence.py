class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        res = ""
        i, j = 0, 0
        while j < len(t):
            if i == len(s):
                return True
            if s[i] == t[j]:
                res += s[i]
                j += 1
                i += 1
            else:
                j += 1
        return res == s