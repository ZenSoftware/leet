# https://leetcode.com/problems/partition-equal-subset-sum/description/
from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        def dfs(i: int, sum1: int, sum2: int) -> bool:
            if i >= len(nums):
                return sum1 == sum2
            
            if dfs(i+1, sum1 + nums[i], sum2):
                return True

            return dfs(i+1, sum1, sum2 + nums[i])
        return dfs(0, 0, 0)