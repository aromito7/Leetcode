class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        length = len(nums)
        min_jumps = [float('inf')] * length
        min_jumps[0] = 0

        for i, num in enumerate(nums):
            for j in range(i + 1, min(num + i + 1, length)):
                min_jumps[j] = min(min_jumps[j], min_jumps[i] + 1)


        return min_jumps[-1]


