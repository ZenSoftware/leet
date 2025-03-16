# https://leetcode.com/problems/frog-jump/
from typing import List

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        def dfs(i: int, k: int) -> bool:
            if i == len(stones)-1:
                return True
            
            result = False

            for kth in range(k-1, k+2):
                if kth > 0:
                    for j in range(i+1, len(stones)):
                        distance = stones[j] - stones[i]
                        if kth < distance:
                            break
                        elif kth == distance:
                            result |= dfs(j, kth)
                            
            return result
        return dfs(0, 0)