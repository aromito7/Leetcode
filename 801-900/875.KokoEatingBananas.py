import math
class Solution(object):
    def is_valid(self, piles, h, k):
        if k == 0:
            return False
        return sum([math.ceil(1.0 * pile/k) for pile in piles]) <= h

    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        
        start = 0
        end = max(piles)

        while True:
            k = (start + end) // 2
            if not self.is_valid(piles, h, k):
                if start == k:
                    start += 1
                else:
                    start = k
            elif self.is_valid(piles, h, k-1):
                end = k
            else:
                return k



        
        return 0
