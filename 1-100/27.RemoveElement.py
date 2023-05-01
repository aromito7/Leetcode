class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        i = 0
        end = len(nums) - 1


        while i <= end:
            if nums[i] == val:
                nums[i], nums[end] = nums[end], nums[i]
                end -= 1
            else:
                i += 1

        print(nums)

        return end + 1
