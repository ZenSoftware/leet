# https://leetcode.com/problems/frog-jump/
from typing import List
from functools import cache

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        @cache
        def dfs(i: int, k: int) -> bool:
            if i == len(stones)-1:
                return True
            
            for kth in range(k-1, k+2):
                if kth > 0:
                    for j in range(i+1, len(stones)):
                        distance = stones[j] - stones[i]
                        if kth < distance:
                            break
                        elif kth == distance:
                            if dfs(j, kth):
                                return True
            return False
        return dfs(0, 0)