from functools import reduce

class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        if len(stones) == 0:
            return 0
        elif len(stones) == 1:
            return stones[0]

        stones = sorted(stones, key = lambda x: -x)

        while len(stones) > 2:
            temp = stones[0] - stones[1]
            stones = sorted(stones[2:] + [temp], key = lambda x: -x)
            
        
        return abs(stones[0] - stones[1])
