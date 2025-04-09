# https://leetcode.com/problems/total-hamming-distance/description/
from typing import List


class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        n = len(nums)
        result = 0
        for i in range(max(nums).bit_length()):
            ones = 0
            for num in nums:
                if (num >> i) & 1:
                    ones += 1
            result += ones * (n - ones)
        return result
