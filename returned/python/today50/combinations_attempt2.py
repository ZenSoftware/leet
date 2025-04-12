# https://leetcode.com/problems/combinations/description/
from typing import List


class Solution:
    """
    Time: O(n^2)
    Space: O(n)
    """

    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []

        def combinations(start: int, path: List[int]) -> List[List[int]]:
            if len(path) == k:
                result.append(path.copy())
                return

            for i in range(start, n + 1):
                path.append(i)
                combinations(i + 1, path)
                path.pop()

        combinations(1, [])
        return result
