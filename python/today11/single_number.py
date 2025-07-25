# https://leetcode.com/problems/single-number/
from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor = 0
        for n in nums:
            xor ^= n
        return xor