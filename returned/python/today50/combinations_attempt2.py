# https://leetcode.com/problems/combinations/description/
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def combinations(remaining: int) -> List[List[int]]:
            if remaining == 0:
                return [[]]

            combs_without_first = combinations(remaining - 1)
            combs_with_first = []

            for comb in combs_without_first:
                combs_with_first.append(comb + [remaining])
            combs_with_first.extend(combs_without_first)
            return combs_with_first

        result = combinations(n)
        return [comb for comb in result if len(comb) == k]


print(Solution().combine(3, 2))
