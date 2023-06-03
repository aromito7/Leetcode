class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        cur = -float('inf')
        count = 0
        output = 0

        for num in nums:
            if num > cur:
                cur = num
                count += 1
            else:
                output = max(count, output)
                count = 1
                cur = num
        
        return max(count, output)
