# https://leetcode.com/problems/combination-sum/description/
from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        
        def dfs(i: int, current: List[int], total: int):
            if total == target:
                result.append(current.copy())
                return
            if total > target or i >= len(candidates):
                return
            
            current.append(candidates[i])
            dfs(i, current, total + candidates[i])
            current.pop()
            dfs(i+1, current, total)

        dfs(0, [], 0)
        return result