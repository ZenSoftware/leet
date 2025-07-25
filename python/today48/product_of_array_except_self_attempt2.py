# https://leetcode.com/problems/product-of-array-except-self/description/
from typing import List


class Solution:
    """
    Time: O(n)
    Space: O(n)
    """

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)

        left_product = 1
        for i in range(len(nums)):
            result[i] = left_product
            left_product *= nums[i]

        right_product = 1
        for i in reversed(range(len(nums))):
            result[i] *= right_product
            right_product *= nums[i]

        return result
