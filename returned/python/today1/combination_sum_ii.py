# https://leetcode.com/problems/combination-sum-ii/description/
from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []

        def dfs(i: int, cur: List[int], total: int):
            if total == target:
                result.append(cur.copy())
                return
            if total > target or i >= len(candidates):
                return

            cur.append(candidates[i])
            dfs(i+1, cur, total+candidates[i])
            cur.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            dfs(i+1, cur, total)

        dfs(0,[],0)
        return result