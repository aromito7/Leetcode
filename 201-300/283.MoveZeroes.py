class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        

        i = 0
        zeros = 0

        while i < len(nums):
            if nums[i] == 0:
                zeros += 1
            else:
                nums[i], nums[i - zeros] = nums[i - zeros], nums[i]

            i += 1

        return nums
