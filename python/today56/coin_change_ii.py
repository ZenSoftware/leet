# https://leetcode.com/problems/coin-change-ii/description/


class Solution(object):
    def change(self, amount, coins):
        memo = {}

        def search(current, remaining):
            if (current, len(remaining)) in memo:
                return memo[(current, len(remaining))]
            if len(remaining) == 0:
                return 0
            if current > amount:
                return 0
            if current == amount:

                return 1

            with_first = search(current + remaining[0], remaining)
            without_first = search(current, remaining[1:])

            memo[(current + remaining[0], len(remaining))] = with_first
            memo[current, len(remaining) - 1] = without_first

            return with_first + without_first

        return search(0, coins)
