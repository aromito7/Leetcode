class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        dic = defaultdict(lambda: 0)

        for num in nums:
            dic[num] += 1
        
        end0 = dic[0]
        end1 = end0 + dic[1]

        for i in range(len(nums)):
            if i < end0:
                nums[i] = 0
            elif i < end1:
                nums[i] = 1
            else:
                nums[i] = 2

        return nums
