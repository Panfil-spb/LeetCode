class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        nums = {"I": 1,
               "V": 5,
               "X": 10,
               "L": 50,
               "C": 100,
               "D": 500,
               "M": 1000}
        sum = 0
        i = 0
        while i < len(s):
            if i == len(s) - 1:
                sum += nums[s[i]]
                break
            elif nums[s[i]] < nums[s[i+1]]:
                sum += nums[s[i+1]] - nums[s[i]]
                i += 1
            elif nums[s[i]] > nums[s[i+1]]:
                sum += nums[s[i]]
            else:
                sum += nums[s[i]]
            i += 1
        return sum
        