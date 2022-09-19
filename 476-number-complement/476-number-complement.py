class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        binary = bin(num).replace("0b", "")
        dictBin = {
            "0" : "1",
            "1" : "0"
        }
        
        n = ''.join(dictBin[x] for x in binary)
        return int(n, 2)