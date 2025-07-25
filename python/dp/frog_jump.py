# https://leetcode.com/problems/frog-jump/
from typing import List
from functools import cache

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        @cache
        def dfs(i: int, k: int) -> bool:
            if i == len(stones)-1:
                return True
            
            for next_k in range(k-1, k+2):
                if next_k > 0:
                    for j in range(i+1, len(stones)):
                        distance = stones[j] - stones[i]
                        if next_k < distance:
                            break
                        elif next_k == distance and dfs(j, next_k):
                            return True
            return False
        return dfs(0, 0)