class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        mas = s.split()
        return len(mas[-1])
        