class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """

        output = 0
        while n > 0:
            output += n%2
            n = n >> 1

        return output
