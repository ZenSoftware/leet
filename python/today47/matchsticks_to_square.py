# https://leetcode.com/problems/matchsticks-to-square/description/
from typing import List


class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if len(matchsticks) < 4:
            return False

        total = sum(matchsticks)
        if total % 4:
            return False

        req_len = total // 4
        sides = [0] * 4
        matchsticks.sort(reverse=True)

        def dfs(i: int) -> bool:
            if i == len(matchsticks):
                return True

            for j in range(4):
                if sides[j] + matchsticks[i] <= req_len:
                    sides[j] += matchsticks[i]
                    if dfs(i + 1):
                        return True
                    sides[j] -= matchsticks[i]
                    if sides[j] == 0:
                        return False
            return False

        return dfs(0)
