# https://leetcode.com/problems/number-of-boomerangs/description/
from typing import List


class Solution:
    """
    Time: O(n^3)
    Space: O(n^2)
    """

    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        n = len(points)
        distances = {}

        for i in range(n - 1):
            for j in range(i + 1, n):
                x_delta = points[i][0] - points[j][0]
                y_delta = points[i][1] - points[j][1]
                dist = x_delta**2 + y_delta**2
                distances[(i, j)] = dist
                distances[(j, i)] = dist

        res = 0
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    if distances[(i, j)] == distances[(i, k)]:
                        res += 2
                    if distances[(j, i)] == distances[(j, k)]:
                        res += 2
                    if distances[(k, i)] == distances[(k, j)]:
                        res += 2
        return res
