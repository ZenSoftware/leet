# https://leetcode.com/problems/coin-change-ii/description/


class Solution(object):
    def change(self, amount, coins):
        memo = {}

        def search(current, i):
            if (current, i) in memo:
                return memo[(current, i)]
            if i == len(coins):
                return 0
            if current > amount:
                return 0
            if current == amount:
                return 1

            with_first = search(current + coins[i], i)
            without_first = search(current, i + 1)

            memo[(current + coins[i], i)] = with_first
            memo[(current, i + 1)] = without_first

            return with_first + without_first

        return search(0, 0)
