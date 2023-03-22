class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        left = 0
        right = len(height) - 1
        output = 0

        while left < right:
            temp = min(height[left], height[right]) * (right - left)
            if temp > output:
                output = temp

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            

        return output
