# https://leetcode.com/problems/pacific-atlantic-water-flow/
from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pacific, atlantic = set(), set()

        def dfs(r, c, h, ocean):
            if (r not in range(ROWS) or
                c not in range(COLS) or
                (r,c) in ocean or
                heights[r][c] < h):
                return
            
            ocean.add((r,c))
            for i, j in [[0,1],[0,-1],[1,0],[-1,0]]:
                dfs(r+i, c+j, heights[r][c], ocean)

        for r in range(ROWS):
            dfs(r, 0, -1, pacific)
            dfs(r, COLS-1, -1, atlantic)
            
        for c in range(COLS):
            dfs(0, c, -1, pacific)
            dfs(ROWS-1, c, -1, atlantic)

        result = []
        for coord in pacific.intersection(atlantic):
            result.append(list(coord))
        return result