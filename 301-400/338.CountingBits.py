class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """

        output = [0] * (n + 1)
        p = 1

        while p <= n:
            for i in range(p , min(2 * p, n + 1)):
                output[i] = output[i - p] + 1

            p *= 2
                


        return output
