# https://leetcode.com/problems/largest-divisible-subset/
from typing import List

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        memo = {}

        def dfs(i: int) -> List[int]:
            if i >= len(nums):
                return []
            
            res = [nums[i]]
            for j in range(i+1, len(nums)):
                if nums[j] % nums[i] == 0:
                    tmp = [nums[i]] + dfs(j)
                    if len(tmp) > len(res):
                        res = tmp
            return res
        
        res = []
        for i in range(len(nums)):
            tmp = dfs(i)
            if len(tmp) > len(res):
                res = tmp
        return res