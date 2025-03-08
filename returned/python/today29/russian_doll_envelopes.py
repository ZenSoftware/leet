# https://leetcode.com/problems/russian-doll-envelopes/
from typing import List

class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort()
        memo = {}
        
        def dfs(i, prev):
            if i >= len(envelopes):
                return 0
            
            key = (i, tuple(prev))
            if key in memo:
                return memo[key]

            include = 0
            if prev[0] < envelopes[i][0] and prev[1] < envelopes[i][1]:
                include = dfs(i+1, envelopes[i]) + 1
            
            exclude = dfs(i+1, prev)
            
            memo[key] = max(include, exclude)
            return memo[key]
        
        return dfs(0, [float('-inf'), float('-inf')])