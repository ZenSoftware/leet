# https://leetcode.com/problems/count-primes/

class Solution:
    def countPrimes(self, n: int) -> int:
        count = 0

        for x in range(2,n):
            if self.isPrime(x):
                count += 1
        
        return count

    def isPrime(self, n: int) -> bool:
        if n < 2:
            return False
        
        for divisor in range(2, int(n**0.5)+1):
            if n % divisor == 0:
                return False
            
        return True