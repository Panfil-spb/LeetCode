class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        else:
            s = str(x)
            for i in range(len(s) // 2):
                if s[i] != s[-i-1]:
                    return False
            return True
                
        