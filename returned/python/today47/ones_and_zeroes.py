# https://leetcode.com/problems/ones-and-zeroes/description/
from typing import List
from functools import cache


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        counts = [[s.count("0"), s.count("1")] for s in strs]

        @cache
        def dfs(i: int, m_left: int, n_left: int) -> int:
            if m_left < 0 or n_left < 0:
                return float("-inf")

            if i == len(strs):
                return 0

            with_i = 1 + dfs(i + 1, m_left - counts[i][0], n_left - counts[i][1])
            without_i = dfs(i + 1, m_left, n_left)
            return max(with_i, without_i)

        return dfs(0, m, n)
