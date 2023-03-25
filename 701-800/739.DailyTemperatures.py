class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """


        output = [0 for i in range(len(temperatures))]
        stack = []

        for i, temp in enumerate(temperatures):
            while (len(stack) > 0) and (stack[-1][0] < temp):
                output[stack[-1][1]] = i - stack[-1][1]
                stack.pop()

            stack += [[temp, i]]

        return output
