# https://leetcode.com/problems/can-i-win/description/
from functools import cache


class Solution:
    """
    Time: O(2^n)
    Space: O(2^n)
    """

    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if desiredTotal <= 0:
            return True
        elif (maxChoosableInteger) * (maxChoosableInteger + 1) // 2 < desiredTotal:
            return False

        @cache
        def doesP1Win(total, bitmask):
            if total <= 0:
                return False

            for i in range(1, maxChoosableInteger + 1):
                i_bit = 1 << i
                if bitmask & i_bit == 0:
                    if not doesP1Win(total - i, bitmask | i_bit):
                        return True
            return False

        return doesP1Win(desiredTotal, 0)
