# https://leetcode.com/problems/product-of-array-except-self/description/
from typing import List


class Solution:
    """
    Time: O(3n)
    Space: O(2n)
    """

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        accum = 1
        forward = []
        for i in range(len(nums)):
            accum *= nums[i]
            forward.append(accum)

        accum = 1
        reverse = [None] * len(nums)
        for i in reversed(range(len(nums))):
            accum *= nums[i]
            reverse[i] = accum

        result = []
        for i in range(len(nums)):
            f = 1 if i - 1 not in range(len(nums)) else forward[i - 1]
            r = 1 if i + 1 not in range(len(nums)) else reverse[i + 1]
            result.append(f * r)
        return result
