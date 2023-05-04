class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        output = 0
        stack = []

        for i, height in enumerate(heights):
            pos = i
            output = max(height, output)
            # for s in stack:
            #     output = max((i - s[1] + 1) * min(s[0], height), output) 

            while len(stack) > 0 and stack[-1][0] >= height:
                s = stack[-1]
                output = max((i - s[1]) * s[0], output) 
                _, pos = stack.pop()

            stack.append([height, pos])


            #print(stack)

        for s in stack:
            output = max((i - s[1] + 1) * s[0], output) 

        return output
