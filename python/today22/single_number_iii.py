# https://leetcode.com/problems/single-number-iii/description/
from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        for n in nums:
            xor ^= n
        
        dif_bit = 1
        while not (dif_bit & xor):
            dif_bit <<= 1

        a, b = 0, 0
        for n in nums:
            if n & dif_bit:
                a ^= n
            else:
                b ^= n
        
        return [a, b]