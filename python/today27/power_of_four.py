# https://leetcode.com/problems/power-of-four/description/
from math import log

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        logarithm = log(n, 4)
        return round(logarithm) == logarithm