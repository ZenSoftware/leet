# https://leetcode.com/problems/rotate-function/
from typing import List

class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        ans = float('-inf')
        for rotations in range(len(nums)):
            offset = len(nums) - rotations
            total = 0
            for i in range(len(nums)):
                if offset + i >= len(nums):
                    offset = -i
                total += nums[offset + i] * i
            ans = max(ans, total)
        return ans