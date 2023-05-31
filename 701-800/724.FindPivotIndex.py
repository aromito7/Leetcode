class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        right = sum(nums[1:])
        left = 0
        if left == right:
            return 0
        for n in range(1, len(nums)):
            left += nums[n - 1]
            right -= nums[n]

            if left == right:
                return n

        return -1
