# https://leetcode.com/problems/convert-a-number-to-hexadecimal/description/

class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return '0'
        
        HEX_DIGITS = '0123456789abcdef'

        if num < 0:
            num = (1<<32) + num
        
        res = ''
        while num > 0:
            res = HEX_DIGITS[num % 16] + res
            num //= 16
        return res