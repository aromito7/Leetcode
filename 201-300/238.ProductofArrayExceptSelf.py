class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        product = 1
        zero_position = -1
        zero_count = 0
        for i, num in enumerate(nums):
            if not num == 0: 
                product *= num
            else:
                zero_count += 1
                zero_position = i
                if zero_count > 1:
                    return [0 for i in range(len(nums))]

        if zero_count == 1:
            return [product if i == zero_position else 0 for i in range(len(nums))]
        
        return [product// num for num in nums]
