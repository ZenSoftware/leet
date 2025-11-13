# https://leetcode.com/problems/fibonacci-number/


class Solution(object):
    def fib(self, n):
        if n == 0 or n == 1:
            return n

        f0 = 0
        f1 = 1
        res = 0
        for _ in range(n - 1):
            res = f0 + f1
            f0 = f1
            f1 = res
        return res
