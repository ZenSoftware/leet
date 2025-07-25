# https://leetcode.com/problems/word-break-ii/description/
from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        result = []

        def dfs(l: int, r: int, segments: List[str]):
            if l == len(s) and r == len(s):
                result.append(" ".join(segments))
                return
            if r >= len(s):
                return
            
            seg = s[l:r+1]
            if seg in wordDict:
                segments.append(seg)
                dfs(r+1, r+1, segments)
                segments.pop()
            
            dfs(l, r+1, segments)

        dfs(0,0,[])
        return result