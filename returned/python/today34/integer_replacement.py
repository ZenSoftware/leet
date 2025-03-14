# https://leetcode.com/problems/integer-replacement/description/
from functools import cache

class Solution:
    @cache
    def integerReplacement(self, n: int) -> int:
        if n == 1:
            return 0

        if n % 2 == 0:
            return 1 + self.integerReplacement(n // 2)
        else:
            steps_inc = 1 + self.integerReplacement(n+1)
            steps_dec = 1 + self.integerReplacement(n-1)
            return min(steps_inc, steps_dec)