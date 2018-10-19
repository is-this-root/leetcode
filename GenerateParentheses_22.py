from collections import deque

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        q = deque(['()'])
        while n > 0:
            curr_set = set()
            curr_size = len(q)
            while curr_size != 0:
                seed = q.popleft()
                curr_set.add()
