# https://leetcode.com/problems/interleaving-string/description/

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        memo = {}
        def dfs(i1: int, i2: int, i3: int) -> bool:
            if i1 == len(s1) and i2 == len(s2):
                return True
            
            if (i1, i2) in memo:
                return memo[(i1, i2)]

            r1 = False
            if i1 < len(s1) and s1[i1] == s3[i3]:
                r1 = dfs(i1+1, i2, i3+1)

            r2 = False
            if i2 < len(s2) and s2[i2] == s3[i3]:
                r2 = dfs(i1, i2+1, i3+1)
            
            memo[(i1, i2)] = r1 or r2
            return r1 or r2

        return dfs(0,0,0)
