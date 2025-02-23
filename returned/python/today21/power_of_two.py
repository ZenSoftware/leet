# https://leetcode.com/problems/power-of-two/description/
from math import log2, floor

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 1:
            return False
        x = log2(n)
        return x - floor(x) == 0