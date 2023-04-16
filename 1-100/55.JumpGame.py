class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        maximum = 0
        for i, num in enumerate(nums):
            if i > maximum:
                return False

            if num + i >= len(nums):
                return True
            maximum = max(maximum, num + i)

        return True
