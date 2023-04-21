class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        root_5 = 5 ** .5
        return int((((1 + root_5)/2) ** n - ((1 - root_5)/2) ** n)/root_5)
