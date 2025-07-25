# https://leetcode.com/problems/number-complement/description/
import math


class Solution:
    def findComplement(self, num: int) -> int:
        """
        Time: O(1)
        Space: O(1)
        ---------------------
        0   1   0   0   0
           2^3 2^2 2^1 2^0
        assert log 8 == 3
        bit_length = logn + 1
        we add 1 due to the LSB being 0th indexed

        Taking the floor for numbers between 01000 and 01111
        01000
        01111
        3 (log 8) < 3...(log 15) < 4 (log16)
        ---------------------
        10000 - 1
        01111
        mask = (1 << bit_length) - 1
        ---------------------
        0 xor 0 = 0
        0 xor 1 = 1
        1 xor 0 = 1
        1 xor 1 = 0
        mask     = 1111
        num      = 1011
        num^mask = 0100
        """

        bit_length = math.floor(math.log2(num)) + 1
        mask = (1 << bit_length) - 1
        return num ^ mask
