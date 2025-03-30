# https://leetcode.com/problems/arranging-coins/description/


class Solution:
    def arrangeCoins(self, n: int) -> int:
        total = 0
        rows = 0
        for i in range(1, n + 1):
            total += i
            if total <= n:
                rows += 1
            else:
                break
        return rows
