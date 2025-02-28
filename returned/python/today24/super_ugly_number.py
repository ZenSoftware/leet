# https://leetcode.com/problems/super-ugly-number/
from typing import List

class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        i = 1
        count = 0
        while count < n:
            if self.isUgly(i, primes):
                count += 1
            i += 1
        return i - 1
    
    def isUgly(self, i: int, primes: List[int]) -> bool:
        for p in primes:
            while i % p == 0:
                i //= p
        return i == 1
                