# https://leetcode.com/problems/ugly-number-ii/description/

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        num = 1
        count = 0
        while count < n:
            if self.isUgly(num):
                count += 1
            num += 1
        return num - 1

    def isUgly(self, n: int) -> bool:
        for p in [5, 3, 2]:
            while n % p == 0:
                n //= p
        return n == 1