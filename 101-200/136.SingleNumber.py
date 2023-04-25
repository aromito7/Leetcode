class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """


        return reduce(lambda cur, num: cur^num, nums)
