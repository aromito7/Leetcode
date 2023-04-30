class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        output = 0
        prev = None

        for i, num in enumerate(nums):
            if num != prev:
                nums[output] = num
                output += 1
                prev = num
            

        return output
