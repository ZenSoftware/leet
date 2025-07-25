# https://leetcode.com/problems/minimum-path-sum/description/
from typing import Dict, List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        last_row = len(grid) - 1
        last_col = len(grid[0]) - 1
        memo: Dict[str, int] = {}
        def dfs(x: int, y: int, sum: int):
            if x == last_row and y == last_col:
                return sum
            
            key = str(x) + '-' + str(y) + '-' + str(sum)
            if key in memo:
                return memo[key]

            min_x = float('inf')
            if x+1 <= last_row:
                min_x = dfs(x+1, y, sum + grid[x+1][y])
            
            min_y = float('inf')
            if y+1 <= last_col:
                min_y = dfs(x, y+1, sum + grid[x][y+1])

            memo[key] = min(min_x, min_y)
            return memo[key]
        
        return dfs(0,0,grid[0][0])