# https://leetcode.com/problems/pacific-atlantic-water-flow/
from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pacific, atlantic = set(), set()

        def bfs(r, c, h, ocean, visited):
            if r not in range(ROWS) or c not in range(COLS) or (r,c) in visited:
                return
            
            if heights[r][c] >= h:
                ocean.add((r,c))
            else:
                return
            
            visited.add((r,c))
            for i, j in [[0,1],[0,-1],[1,0],[-1,0]]:
                bfs(r+i, c+j, heights[r][c], ocean, visited)
            visited.pop()

        for r in range(ROWS):
            bfs(r, 0, -1, pacific, set())
            bfs(r, COLS-1, -1, atlantic, set())
            
        for c in range(COLS):
            bfs(0, c, -1, pacific, set())
            bfs(ROWS-1, c, -1, atlantic, set())

        result = []
        for coord in pacific.intersection(atlantic):
            result.append(list(coord))
        return result