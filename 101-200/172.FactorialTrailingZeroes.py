class Solution:
    def trailingZeroes(self, n: int) -> int:
        output = 0

        i = 5
        p = 1

        while i ** p <= n:
            output += n//(i ** p)
            p += 1


        return output
