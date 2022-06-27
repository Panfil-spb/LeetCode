class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = collections.Counter(s)
        
        for i, el in enumerate(s):
            if count[el] == 1:
                return i
        return -1
        