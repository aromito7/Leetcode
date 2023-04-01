class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        output = nums[-1]

        for i in range(len(nums) - 1):
            num = nums[i]
            output = max(output, num)
            if num > 0:
                nums[i + 1] += num
                
        output = max(output, nums[-1])

        return output
