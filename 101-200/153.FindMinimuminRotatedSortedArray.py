class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        start = 0
        end = len(nums) - 1

        if end == 0 or nums[0] < nums[-1]:
            return nums[0]
        elif nums[-1] < nums[-2]:
            return nums[-1]

        while start < end:
            curr = (start + end) //2
            if nums[curr] < nums[curr - 1]:
                return nums[curr]
            elif nums[curr] < nums[end]:
                end = curr
            else:
                start = curr


        return nums[0]


