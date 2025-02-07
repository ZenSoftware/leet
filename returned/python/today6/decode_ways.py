# https://leetcode.com/problems/decode-ways/description/

class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}

        def dfs(i: int) -> int:
            if i == len(s):
                return 1
            if s[i] == '0':
                return 0
            if i in memo:
                return memo[i]
            count = dfs(i+1)
            if i+1 < len(s) and int(s[i]+s[i+1]) <= 26:
                count += dfs(i+2)
            memo[i] = count
            return count

        return dfs(0)