# https://leetcode.com/problems/combination-sum-iii/
from typing import List

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
        def dfs(num: int, sum: int, combination: List[int]):
            if len(combination) >= k:
                if sum == n:
                    result.append(combination.copy())
                return

            for i in range(num+1, 10):
                if sum+i > n:
                    break
                combination.append(i)
                dfs(i, sum+i, combination)
                combination.pop()
        dfs(0, 0, [])
        return result
