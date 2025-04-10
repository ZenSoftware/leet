# https://leetcode.com/problems/maximum-product-subarray/description/
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = nums[0]
        curMin, curMax = 1, 1
        for n in nums:
            tmp = curMax * n
            curMax = max(tmp, curMin * n, n)
            curMin = min(tmp, curMin * n, n)
            result = max(result, curMax)
        return result
