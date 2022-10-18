class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        power = 0
        while 2 ** power <= n:
            if 2 ** power == n:
                return True
            else:
                power += 1
        return False