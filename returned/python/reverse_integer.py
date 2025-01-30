# https://leetcode.com/problems/reverse-integer/description/
class Solution:
    def reverse(self, x: int) -> int:
        if(x < 0):
            res = int('-' + str(x)[1:][::-1])
            if res < (-2)**31:
                return 0
            else:
                return res
        else:
            res = int(str(x)[::-1])
            if res > 2**31 - 1:
                return 0
            else:
                return res
