class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """

        if n <= 0:
            return False

        if n < 1:
            n = 1/n

        while n > 1:
            if n % 2 > 0:
                return False
            n >>= 1


        return True
