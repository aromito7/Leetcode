class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        start = 0
        end = len(nums) - 1

        
        if nums[0] == target:
            return 0
        elif nums[end] == target:
            return end

        while start < end:
            curr = (start + end)//2
            if nums[curr] == target:
                return curr
            elif target < nums[start] < nums[curr] or nums[curr] < target < nums[start] or nums[start] < nums[curr] < target:
                start = curr
            else:
                end = curr

        return -1

        
