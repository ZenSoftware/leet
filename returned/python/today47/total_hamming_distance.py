# https://leetcode.com/problems/total-hamming-distance/description/
from typing import List


class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        result = 0
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                result += (nums[i] ^ nums[j]).bit_count()
        return result
