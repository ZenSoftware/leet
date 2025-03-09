# https://leetcode.com/problems/largest-divisible-subset/
from typing import List

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        res = []
        def dfs(i: int, path: List[int]):
            nonlocal res
            if i >= len(nums):
                if len(res) < len(path):
                    res = path.copy()
                return
            
            if len(path) == 0 or nums[i] % path[-1] == 0 or path[-1] % nums[i] == 0:
                path.append(nums[i])
                dfs(i+1, path)
                path.pop()
            
            dfs(i+1, path)
        dfs(0, [])
        return res
        