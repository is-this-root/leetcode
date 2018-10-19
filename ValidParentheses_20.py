class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for c in s:
            if c == '(' or c == '[' or c == '{':
                stack.append(c)
            elif len(stack) == 0:
                return False
            else:
                p = stack.pop()
                if (p == '(' and c != ')') or (p == '[' and c != ']') or (p == '{' and c != '}'):
                    return False
        if len(stack) != 0:
            return False
        return True
