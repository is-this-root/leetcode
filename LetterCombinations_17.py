from collections import deque


class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        q = deque([''])
        digit_dic = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'],
                     '5': ['j', 'k', 'l'], '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'],
                     '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}
        for c in digits:
            letters = digit_dic[c]
            last_turn = len(q)
            while last_turn != 0:
                seed = q.popleft()
                for l in letters:
                    q.append(seed + l)
                last_turn -= 1
        return list(q)
