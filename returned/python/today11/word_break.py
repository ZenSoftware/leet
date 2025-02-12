# https://leetcode.com/problems/word-break/description/
from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}

        def dfs(l: int, r: int) -> bool:
            if l == len(s) and r == len(s):
                return True
            if r >= len(s):
                return False
            if (l,r) in memo:
                return memo[(l,r)]
            
            result = False
            if s[l:r+1] in wordDict:
                result = dfs(r+1, r+1)

            memo[(l,r)] = result or dfs(l, r+1)
            return memo[(l,r)]

        return dfs(0,0)
