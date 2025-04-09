# https://leetcode.com/problems/number-complement/description/
import math


class Solution:
    def findComplement(self, num: int) -> int:
        num_bits = math.floor(math.log2(num)) + 1
        mask = (1 << num_bits) - 1
        return num ^ mask
