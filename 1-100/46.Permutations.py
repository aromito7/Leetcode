def permute(nums):
    if len(nums) == 1:
        return [[nums[0]]]

    output = []
    for i, num in enumerate(nums):
        output += [[num] + p for p in permute(nums[:i] + nums[i+1:])]

    return output

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        return permute(nums)



