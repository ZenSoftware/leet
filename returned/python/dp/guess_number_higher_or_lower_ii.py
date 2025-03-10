# https://leetcode.com/problems/guess-number-higher-or-lower-ii/description/
from functools import cache

class Solution:
    def getMoneyAmount(self, n: int) -> int:
        @cache
        def dp(left: int, right: int):
            if left >= right:
                return 0    
            ans = float('inf')
            for guess in range((left+right)//2, right+1):
                cost = guess + max(dp(left, guess-1), dp(guess+1, right))
                ans = min(ans, cost)
            return ans
        
        return dp(1, n)