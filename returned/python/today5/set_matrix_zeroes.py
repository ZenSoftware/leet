# https://leetcode.com/problems/set-matrix-zeroes/description/
from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row_count = len(matrix)
        col_count = len(matrix[0])

        for i in range(row_count):
            for j in range(col_count):
                if matrix[i][j] == 0:
                    matrix[i][j] = 'T'
        
        for i in range(row_count):
            for j in range(col_count):
                if matrix[i][j] == 'T':
                    for r in range(row_count):
                        if matrix[r][j] != 'T':
                            matrix[r][j] = 0
                    for c in range(col_count):
                        if matrix[i][c] != 'T':
                            matrix[i][c] = 0
        
        for i in range(row_count):
            for j in range(col_count):
                if matrix[i][j] == 'T':
                    matrix[i][j] = 0
