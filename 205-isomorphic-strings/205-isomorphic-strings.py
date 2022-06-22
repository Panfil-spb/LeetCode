class Solution:
    
    def trans(self, s: str) -> str:
        index_maping = {}
        new_s = []
        
        for i, c in enumerate(s):
            if c not in index_maping:
                index_maping[c] = i
            new_s.append(str(index_maping[c]))
        
        return " ".join(new_s)
    
    def isIsomorphic(self, s: str, t: str) -> bool:
        return self.trans(s) == self.trans(t)
       
        