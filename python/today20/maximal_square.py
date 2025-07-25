# https://leetcode.com/problems/maximal-square/
from typing import List

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        cache = {}
        def helper(r,c):
            if r >= ROWS or c >= COLS:
                return 0
            if (r,c) in cache:
                return cache[(r,c)]
            right = helper(r+1, c)
            diag = helper(r+1, c+1)
            down = helper(r, c+1)
            if matrix[r][c] == '1':
                cache[(r,c)] = 1 + min(right, diag, down)
            else:
                cache[(r,c)] = 0
            return cache[(r,c)]
        helper(0,0)
        return max(cache.values()) ** 2

        