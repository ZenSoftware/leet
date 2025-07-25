# https://leetcode.com/problems/number-of-boomerangs/description/
from typing import List


class Solution:
    """
    Time: O(n^2)
    Space: O(n)
    """

    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        res = 0
        for x1, y1 in points:
            counts = {}
            for x2, y2 in points:
                dist = (x2 - x1) ** 2 + (y2 - y1) ** 2
                counts[dist] = counts.get(dist, 0) + 1
            for n in counts.values():
                res += n * (n - 1)
        return res
