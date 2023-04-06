def subset(nums):
    if len(nums) == 1:
        return [[], [nums[0]]]

    output = []
    temp = subset(nums[:-1])
    output += temp + [t + [nums[-1]] for t in temp]

    return output

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return subset(nums)
