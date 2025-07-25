# https://leetcode.com/problems/combination-sum-iv/description/
from typing import List
from functools import cache

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()

        @cache
        def dfs(sum: int) -> int:
            if sum == target:
                return 1
            count = 0
            for n in nums:
                if sum+n > target:
                    break
                count += dfs(sum+n)    
            return count
        
        return dfs(0)