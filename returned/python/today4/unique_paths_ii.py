# https://leetcode.com/problems/unique-paths-ii/description/
from typing import Dict, List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        last_row = len(obstacleGrid) - 1
        last_col = len(obstacleGrid[0]) - 1
        memo: Dict[str, int] = {}
        
        def dfs(row: int, col: int) -> int:
            if row > last_row or col > last_col or obstacleGrid[row][col] == 1:
                return 0
            if row == last_row and col == last_col:
                return 1
            key = str(row) + '-' + str(col)
            if key in memo:
                return memo[key]
            
            count = dfs(row, col+1)
            count += dfs(row+1, col)

            memo[key] = count
            return count

        return dfs(0, 0)