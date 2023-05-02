class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        is_missing = [0] * ((10 ** 5) + 2)
        output = 1

        nums = [num for num in nums if 0 < num <= 10**5]

        #print(is_missing)

        for num in nums:
            is_missing[num] = 1
            while is_missing[output]:
                output += 1

        return output
