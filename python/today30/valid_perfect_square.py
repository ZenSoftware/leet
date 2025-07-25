# https://leetcode.com/problems/valid-perfect-square/description/

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l, r = 0, num
        while l <= r:
            m = l + ((r-l) // 2)
            squared = m * m
            if num < squared:
                r = m - 1
            elif num > squared:
                l = m + 1
            else:
                return True
        return False