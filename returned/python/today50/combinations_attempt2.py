# https://leetcode.com/problems/combinations/description/
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def combinations(elements: List[int]) -> List[List[int]]:
            if not elements:
                return [[]]

            first_el = elements[0]
            without_first = elements[1:]
            combs_without_first = combinations(without_first)
            combs_with_first = []

            for comb in combs_without_first:
                combs_with_first.append([first_el] + comb)
            combs_with_first.extend(combs_without_first)
            return combs_with_first

        result = combinations(list(range(1, n + 1)))
        print(result)
        return result


# Solution().combine(3, 2)
