class Solution:
    def reverseWords(self, s: str) -> str:

        return " ".join(i for i in [word[::-1] for word in s.split()])
            
            
        