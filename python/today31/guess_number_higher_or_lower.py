# https://leetcode.com/problems/guess-number-higher-or-lower/description/

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
def guess(num: int, pick = 6) -> int:
    if num > pick: return -1
    elif num < pick: return 1
    else: return 0

class Solution:
    def guessNumber(self, n: int) -> int:
        l, r = 0, n
        while l <= r:
            m = l + ((r-l) // 2)
            hint = guess(m)
            if hint == -1:
                r = m - 1
            elif hint == 1:
                l = m + 1
            else:
                return m
        return l