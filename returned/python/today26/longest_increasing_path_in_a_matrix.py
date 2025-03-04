# https://leetcode.com/problems/longest-increasing-path-in-a-matrix/description/
from typing import List

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        memo = [[0]*COLS for _ in range(ROWS)]
        
        def dfs(i: int, j: int) -> int:
            if memo[i][j]:
                return memo[i][j]
            path = 1
            for x, y in [[0,1], [0,-1], [1,0], [-1,0]]:
                if i+x in range(ROWS) and j+y in range(COLS) and matrix[i][j] < matrix[i+x][j+y]:
                    path = max(path, 1 + dfs(i+x, j+y))
            memo[i][j] = path
            return path
    
        res = 0
        for i in range(ROWS):
            for j in range(COLS):
                res = max(res, dfs(i, j))
        return res