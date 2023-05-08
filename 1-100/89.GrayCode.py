class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """

        output = [0]

        for i in range(n):
            output += [o + len(output) for o in output[::-1]]

        # for i in range(n):
        #     length = len(output)
        #     for o in range(length - 1, -1, -1):
        #         output.append(output[o] + length)

        return output
