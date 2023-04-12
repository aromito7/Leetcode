class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """

        nums = set([n])

        while n > 1:
            n = str(n)
            nex = sum([int(x)**2 for x in n])
            if nex in nums:
                return False
            nums.add(nex)
            n = nex




        return True