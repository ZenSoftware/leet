# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        i = 0
        for j in range(1, len(prices)):
            if prices[j] < prices[i]:
                i = j
            else:
                profit = max(profit, prices[j] - prices[i])
        return profit
