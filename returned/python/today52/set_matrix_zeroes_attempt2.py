# https://leetcode.com/problems/set-matrix-zeroes/description/
from typing import List


class Solution:
    """
    Time: O(n * m)
    Space: O(n + m)
    """

    def setZeroes(self, matrix: List[List[int]]) -> None:
        n, m = len(matrix), len(matrix[0])
        row = [False] * n
        col = [False] * m
        for r in range(n):
            for c in range(m):
                if matrix[r][c] == 0:
                    row[r] = col[c] = True
        for r in range(n):
            for c in range(m):
                if row[r] or col[c]:
                    matrix[r][c] = 0
