class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return "1"
        
        s = '1'
        
        for i in range(n - 1):
            temp = []
            count = 1
         
            for index in range(1, len(s)):
                if s[index] != s[index - 1]:
                    temp.append(str(count))
                    temp.append(s[index - 1])
                    count = 1
                else:
                    count += 1

            temp.append(str(count))
            temp.append(s[-1])
            s = "".join(str(i) for i in temp)

        return s
        
        
        
                
                
        