# https://leetcode.com/problems/minimum-size-subarray-sum/description/
from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len = float('inf')
        total = 0
        l = 0
        
        for r, num in enumerate(nums):
            total += num
            while total >= target:
                min_len = min(min_len, r-l+1)
                total -= nums[l]
                l += 1

        return 0 if min_len == float('inf') else min_len