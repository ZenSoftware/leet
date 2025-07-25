# https://leetcode.com/problems/count-primes/

class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0

        primes = [True] * n
        primes[0], primes[1] = False, False
        for p in range(2, int(n**0.5)+1):
            for i in range(p**2, n, p):
                primes[i] = False
        return sum(primes)
