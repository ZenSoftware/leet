# https://leetcode.com/problems/range-sum-query-2d-immutable/description/
from typing import List

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        ROWS, COLS = len(matrix), len(matrix[0])
        self.matrix = [[0 for _ in range(COLS+1)] for _ in range(ROWS+1)]
        
        for r in range(1, ROWS+1):
            accum = 0
            for c in range(1, COLS+1):
                accum += matrix[r-1][c-1]
                self.matrix[r][c] = accum + self.matrix[r-1][c]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        A = self.matrix[row2+1][col2+1]
        B = self.matrix[row2+1][col1]
        C = self.matrix[row1][col2+1]
        D = self.matrix[row1][col1]
        return A - B - C + D