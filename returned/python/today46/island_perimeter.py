# https://leetcode.com/problems/island-perimeter/description/
from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])

        def calc_perim(i: int, j: int) -> int:
            perim = 0
            if i - 1 < 0 or grid[i - 1][j] == 0:
                perim += 1
            if i + 1 >= n or grid[i + 1][j] == 0:
                perim += 1
            if j - 1 < 0 or grid[i][j - 1] == 0:
                perim += 1
            if j + 1 >= m or grid[i][j + 1] == 0:
                perim += 1
            return perim

        res = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    res += calc_perim(i, j)
        return res
