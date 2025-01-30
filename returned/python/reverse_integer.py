# https://leetcode.com/problems/reverse-integer/description/

class Solution:
    def reverse(self, x: int) -> int:
        if(x < 0):
            y = int('-' + str(x)[1:][::-1])
            if y < (-2)**31:
                return 0
            else:
                return y
        else:
            y = int(str(x)[::-1])
            if y > 2**31 - 1:
                return 0
            else:
                return y
