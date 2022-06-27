class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = collections.Counter(s)
        len = 0
        ml = 0
        for i in count:
            if count[i] % 2 == 0:
                len += count[i]
            else:
                len += count[i] - 1
                ml = 1
        return len + ml
            
        