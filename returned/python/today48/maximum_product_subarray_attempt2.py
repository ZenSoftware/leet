# https://leetcode.com/problems/maximum-product-subarray/description/
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = float("-inf")
        for i in range(len(nums)):
            accum = 1
            for j in range(i, len(nums)):
                accum *= nums[j]
                result = max(result, accum)
        return result
