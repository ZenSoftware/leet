# https://leetcode.com/problems/arithmetic-slices/description/
from typing import List

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        dp = [None] * (len(nums)-1)
        for i in range(1, len(nums)):
            dp[i-1] = nums[i] - nums[i-1]
        
        result = 0
        m = 1
        for i in range(1, len(dp)):
            if dp[i-1] == dp[i]:
                result += m
                m += 1
            else:
                m = 1
        return result