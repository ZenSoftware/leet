# https://leetcode.com/problems/integer-break/description/

class Solution:
    def integerBreak(self, n: int) -> int:
        memo = { 1: 1 }
        
        def dfs(num: int) -> int:
            if num in memo:
                return memo[num]
                
            res = 0 if num == n else num
            for i in range(1, num):
                val = dfs(i) * dfs(num-i)
                res = max(res, val)
            memo[num] = res
            return res
        
        return dfs(n)