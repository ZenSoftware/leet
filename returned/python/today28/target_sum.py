# https://leetcode.com/problems/target-sum/description/
from typing import List

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}

        def dfs(i: int, total: int) -> int:
            if (i,total) in memo:
                return memo[(i,total)]
            
            if i >= len(nums):
                if total == target:
                    return 1
                else:
                    return 0

            memo[(i,total)] = dfs(i+1, total+nums[i]) + dfs(i+1, total-nums[i])
            return memo[(i,total)]
            
        return dfs(0, 0)