class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        output = k
        cur = 0

        start = 0
        end = 0


        while end < len(nums):
            if nums[end] == 1:
                cur += 1
                output = max(output, cur + k)
            else:
                while end - start - cur >= k:
                    if nums[start] == 1:
                        cur -= 1
                    start += 1
            end += 1

        return min(output, len(nums))
        
