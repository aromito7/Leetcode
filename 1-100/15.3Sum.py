class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        output = []
        sorted_nums = sorted(nums)
        
        for i, first in enumerate(sorted_nums):
            start = i + 1
            end = len(sorted_nums) - 1
            
            if i > 0 and first == sorted_nums[i-1]:
                continue
            while start < end:
                second = sorted_nums[start]
                third = sorted_nums[end]

                if first + second + third == 0:
                    output += [[first, second, third]]
                    start += 1
                    end -= 1
                    while sorted_nums[start] == sorted_nums[start-1] and sorted_nums[end] == sorted_nums[end + 1] and start < end:
                        start += 1
                        end -= 1

                elif first + second + third > 0:
                    end -= 1
                else:
                    start += 1

            
        return output
        
