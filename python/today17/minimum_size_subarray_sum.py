# https://leetcode.com/problems/minimum-size-subarray-sum/description/
from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans = float('inf')
        total = 0
        l = 0

        for r, num in enumerate(nums):
            total += num
            while total >= target:
                ans = min(ans, r-l+1)
                total -= nums[l]
                l += 1

        return 0 if ans == float('inf') else ans