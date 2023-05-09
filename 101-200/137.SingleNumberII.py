class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = 0
        uniques = set()

        for num in nums:
            total += num
            if not num in uniques:
                uniques.add(num)
                total -= 3 * num


        return total//-2
