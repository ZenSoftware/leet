# https://leetcode.com/problems/dungeon-game/description/
from typing import List

class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        rows = len(dungeon)
        cols = len(dungeon[0])
        min_initial = float('inf')

        def dfs(x: int, y: int, current: int, initial: int):
            if x not in range(rows) or y not in range(cols):
                return
            
            new_current = current + dungeon[x][y]
            new_initial = initial
            if new_current <= 0:
                new_initial += abs(new_current) + 1
                new_current = 1

            if (x == rows-1) and (y == cols-1):
                nonlocal min_initial
                min_initial = min(min_initial, new_initial)
                return
            
            dfs(x, y+1, new_current, new_initial)
            dfs(x+1, y, new_current, new_initial)

        dfs(0, 0, 1, 1)
        
        return min_initial