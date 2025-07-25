# https://leetcode.com/problems/dungeon-game/
from typing import List

class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        rows = len(dungeon)
        cols = len(dungeon[0])
        result = [[None for _ in range(cols+1)] for _ in range(rows+1)]
        
        for r in range(rows):
            result[r][cols] = float('inf')
        for c in range(cols):
            result[rows][c] = float('inf')

        result[rows][cols-1] = 1

        for r in range(rows-1, -1, -1):
            for c in range(cols-1, -1, -1):
                result[r][c] = max(min(result[r+1][c], result[r][c+1]) - dungeon[r][c], 1)
        
        return result[0][0]