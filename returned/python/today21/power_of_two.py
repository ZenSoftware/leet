# https://leetcode.com/problems/power-of-two/description/

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        power2 = 1
        for i in range(31):
            if n == power2:
                return True
            power2 <<= 1
        return False