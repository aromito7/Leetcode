class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        output = 0

        #print(n)
        for _ in range(32):
            #print(n, n % 2, output)
            output *= 2
            output += n % 2
            n >>= 1
               
        return output
