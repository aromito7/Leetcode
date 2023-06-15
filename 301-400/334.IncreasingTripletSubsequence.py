class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        chain_1 = float('inf')
        chain_2 = float('inf')

        for num in nums:
            if num > chain_2:
                return True
            elif num > chain_1:
                chain_2 = num
            else:
                chain_1 = num

        return False

