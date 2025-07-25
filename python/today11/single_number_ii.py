# https://leetcode.com/problems/single-number-ii/description/
from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ones = 0
        twos = 0

        for n in nums:
            ones = (ones ^ n) & (~twos)
            twos = (twos ^ n) & (~ones)

        return ones