class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i = 0
        while True:
            if i >= len(haystack):
                return -1
            if needle in haystack[i:(i + len(needle))]:
                return i
            else:
                i += 1
                
        