# https://leetcode.com/problems/split-array-largest-sum/description/
from typing import List
from functools import cache

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        @cache
        def dfs(i: int, m: int):
            if m == 1:
                return sum(nums[i:])
            current = 0
            res = float('inf')
            for j in range(i, len(nums)-m+1):
                current += nums[j]
                maxSum = max(current, dfs(j+1, m-1))
                res = min(res, maxSum)
                if current > res:
                    break
            return res
        return dfs(0, k)