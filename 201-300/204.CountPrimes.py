class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0
        primes = [1] * n
        primes[0] = 0
        primes[1] = 0

        for p in range(2, len(primes)):
            if primes[p] == 0:
                continue
            for n in range(p**2, len(primes), p):
                primes[n] = 0
            #print(p, primes)

        return sum(primes)
