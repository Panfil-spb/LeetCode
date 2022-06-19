class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        else:
            pref = strs[0]
            for i in range(1, len(strs)):
                while True:
                    if pref == "":
                        return ""
                    if pref in strs[i][:len(pref)]:
                        break
                    else:
                        pref = pref[:-1]
            return pref
                        
                
            
            
            
        