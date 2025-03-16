# https://leetcode.com/problems/frog-jump/
from typing import List

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        def dfs(i: int, k: int) -> bool:
            if i == len(stones)-1:
                return True
            
            result = False

            if k-1 > 0:
                for j in range(i+1, len(stones)):
                    if k-1 < stones[j] - stones[i]:
                        break
                    elif k-1 == stones[j] - stones[i]:
                        result |= dfs(j, k-1)
            
            for j in range(i+1, len(stones)):
                if k < stones[j] - stones[i]:
                    break
                elif k == stones[j] - stones[i]:
                    result |= dfs(j, k)
            
            for j in range(i+1, len(stones)):
                if k+1 < stones[j] - stones[i]:
                    break
                elif k+1 == stones[j] - stones[i]:
                    result |= dfs(j, k+1)
            
            return result
        return dfs(0, 0)