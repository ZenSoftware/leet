# https://leetcode.com/problems/rotate-function/
from typing import List

class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        ans = float('-inf')
        for rotations in range(len(nums)):
            start = len(nums) - rotations
            total = 0
            for i in range(len(nums)):
                if start + i >= len(nums):
                    start = -i
                total += nums[start + i] * i
            ans = max(ans, total)
        return ans