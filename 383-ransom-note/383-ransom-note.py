class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        m1 = [i for i in ransomNote]
        m2 = [i for i in magazine]
        for i in range(len(m2)):
            if m2[i] in m1:
                m1.remove(m2[i])
        return len(m1) == 0
        