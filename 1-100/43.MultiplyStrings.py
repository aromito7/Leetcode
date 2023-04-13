class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """

        result = 0

        for i1, digit1 in enumerate(num1[::-1]):
            for i2, digit2 in enumerate(num2[::-1]):
                result += int(digit1) * int(digit2) * 10 ** ( i1 + i2)

        return str(result)
