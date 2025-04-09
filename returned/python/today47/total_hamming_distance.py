# https://leetcode.com/problems/total-hamming-distance/description/
from typing import List
import math


class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        n = len(nums)
        bit_count = math.floor(math.log2(max(nums))) + 1
        result = 0
        for i in range(bit_count):
            ones = 0
            for num in nums:
                if (num >> i) & 1:
                    ones += 1
            result += ones * (n - ones)
        return result
