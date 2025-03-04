# https://leetcode.com/problems/longest-increasing-path-in-a-matrix/description/
from typing import List

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        memo = {}
        
        def dfs(r: int, c: int, prev: int) -> int:
            if r not in range(ROWS):
                return 0
            if c not in range(COLS):
                return 0
            if prev >= matrix[r][c]:
                return 0
            key = (r,c,prev)
            if key in memo:
                return memo[key]

            prev = matrix[r][c]
            right = dfs(r, c+1, prev) + 1
            left = dfs(r, c-1, prev) + 1
            up = dfs(r+1, c, prev) + 1
            down = dfs(r-1, c, prev) + 1

            memo[key] = max(right, left, up, down)
            return memo[key]
    
        largest = 0
        for r in range(ROWS):
            for c in range(COLS):
                largest = max(largest, dfs(r, c, float('-inf')))
        return largest