class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        for i1, v1 in enumerate(nums):
            for i2, v2 in enumerate(nums[i1 + 1 :]):
                if v1 + v2 == target: return [i1, i2 + i1 + 1]

        return [0, 1]   
