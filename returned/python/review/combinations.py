# https://leetcode.com/problems/combinations/description/
from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []

        def backtrack(start, comb):
            if len(comb) == k:
                result.append(comb.copy())
                return

            for i in range(start, n+1):
                comb.append(i)
                backtrack(i+1, comb)
                comb.pop()
        
        backtrack(1, [])
        return result