class Solution(object):

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        leftSymb = []
        for el in s:
            if el in ['(', '[', '{']:
                leftSymb.append(el)
            elif el == ')' and len(leftSymb) != 0 and leftSymb[-1] == '(':
                leftSymb.pop()
            elif el == ']' and len(leftSymb) != 0 and leftSymb[-1] == '[':
                leftSymb.pop()
            elif el == '}' and len(leftSymb) != 0 and leftSymb[-1] == '{':
                leftSymb.pop()
            else:
                return False
        return leftSymb == []
                
                
        