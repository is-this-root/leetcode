class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        flag = True
        for n, i in enumerate(reversed(digits)):
            if i == 9:
                digits[len(digits) - n - 1] = 0
            if i != 9:
                digits[len(digits) - n - 1] = i+1
                flag = False
                break
        if n == 0 and flag:
            digits = [1] + digits
        return digits
