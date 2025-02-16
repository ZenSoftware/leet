# https://leetcode.com/problems/reverse-bits/

class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for i in range(32):
            place = 1 << i
            digit = n & place
            if i <= 15:
                shifted = digit << (31-i*2)
            else:
                shifted = digit >> (i-15)*2-1
            result = result | shifted
        return result
