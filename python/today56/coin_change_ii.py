# https://leetcode.com/problems/coin-change-ii/description/


class Solution(object):
    def change(self, amount, coins):
        def search(current_sum, denominations):
            if len(denominations) == 0:
                return 0
            if current_sum > amount:
                return 0
            if current_sum == amount:
                return 1

            return search(current_sum + denominations[0], denominations) + search(
                current_sum, denominations[1:]
            )

        return search(0, coins)
