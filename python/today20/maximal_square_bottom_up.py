# https://leetcode.com/problems/maximal-square/
from typing import List

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        ans = [[0 for _ in range(COLS+1)] for _ in range(ROWS+1)]
        for r in reversed(range(ROWS)):
            for c in reversed(range(COLS)):
                if matrix[r][c] == '1':
                    right = ans[r+1][c]
                    diag = ans[r+1][c+1]
                    down = ans[r][c+1]
                    ans[r][c] = 1 + min(right, diag, down)
        largest = 0
        for r in range(ROWS):
            for c in range(COLS):
                largest = max(largest, ans[r][c])
        return largest ** 2