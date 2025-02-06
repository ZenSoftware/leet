# https://leetcode.com/problems/sqrtx/description/

class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        result = 0
        while l <= r:
            mid = l + ((r - l) // 2)

            if mid ** 2 > x:
                r = mid - 1
            elif mid ** 2 < x:
                l = mid + 1
                result = mid
            else:
                return mid
        return result