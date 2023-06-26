class Solution:
    def integerBreak(self, n: int) -> int:
        if n < 4:
            return n - 1
        
        output = 1

        while n > 2:
            n-= 3
            output *= 3
        
        if n == 2:
            return output * 2
        elif n == 1:
            return 4 * output//3
        
        return output
