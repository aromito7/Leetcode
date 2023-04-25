class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        # if x < 0:
        #     output = -1
        #     x *= -1
        # else:
        #     output = 1

        output = 0
        if x < 0:
            negative = -1
            x *= -1
        else:
            negative = 1

        while x > 0:
            output = output * 10 +  x % 10
            x //= 10
            #print(x, output)

        if output > 2**31:
            return 0

        return output * negative
