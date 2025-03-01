# https://leetcode.com/problems/coin-change/
from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dfs(remainder: int) -> int:
            if remainder == 0:
                return 0
            if remainder < 0:
                return float('inf')
            if remainder in memo:
                return memo[remainder]

            memo[remainder] = min(1 + dfs(remainder-coin) for coin in coins)
            return memo[remainder]
        
        result = dfs(amount)
        return result if result != float('inf') else -1