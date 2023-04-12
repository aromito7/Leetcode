class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        if digits == [9] * len(digits):
            return [1] + [0] * len(digits)
            
        digits[-1] += 1

        i = -1

        while digits[i] > 9:
            digits[i] -= 10
            digits[i - 1] += 1
            i -= 1


        return digits
