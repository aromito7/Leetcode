class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1: return 1
        
        root_5 = math.sqrt(5)
        n += 1
        

        return int((((1 + root_5)/2)**n)/root_5 - (((1 - root_5)/2)**n)/root_5)
