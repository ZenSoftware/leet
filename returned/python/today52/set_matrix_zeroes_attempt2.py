# https://leetcode.com/problems/set-matrix-zeroes/description/
from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n, m = len(matrix), len(matrix[0])
        for r in range(n):
            for c in range(m):
                if matrix[r][c] == 0:
                    for i in range(m):
                        if matrix[r][i] != 0:
                            matrix[r][i] = None
                    for i in range(n):
                        if matrix[i][c] != 0:
                            matrix[i][c] = None
        for r in range(n):
            for c in range(m):
                if matrix[r][c] == None:
                    matrix[r][c] = 0
