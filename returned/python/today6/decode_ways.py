# https://leetcode.com/problems/decode-ways/description/

class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}

        def dfs(i: int) -> int:
            if i == len(s):
                return 1
            if i in memo:
                return memo[i]
            count = 0
            if s[i] != '0':
                count += dfs(i+1)
            if i <= len(s)-2 and s[i] != '0' and int(s[i:i+2]) <= 26:
                count += dfs(i+2)
            memo[i] = count
            return count

        return dfs(0)