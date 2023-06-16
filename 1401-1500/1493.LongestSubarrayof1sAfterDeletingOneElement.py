class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        output = 0

        zero = -1
        start = -1
        end = 0

        while end < len(nums):
            if nums[end] == 1:
                output = max(end - start, output)
            else:
                start = zero + 1
                zero = end

            end += 1
            
        return min(output, len(nums) - 1)
