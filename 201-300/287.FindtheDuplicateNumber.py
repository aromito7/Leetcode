class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start = 0
        end = len(nums) - 1
    
        while start < end:
            half = (start + end + 1)//2
            
            count = 0
            for num in nums:
                if half <= num <= end:
                    count += 1
            if count > end - half + 1:
                start = half
            else:
                end = half - 1
        
        return start
