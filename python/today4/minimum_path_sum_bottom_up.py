# https://leetcode.com/problems/minimum-path-sum/description/
from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        row_count = len(grid)
        col_count = len(grid[0])
        ans = [[0 for j in range(col_count+1)] for i in range(row_count+1)]
        
        for i in range(row_count+1):
            ans[i][col_count] = float('inf')
        for j in range(col_count+1):
            ans[row_count][j] = float('inf')
        
        ans[row_count][col_count-1] = 0

        for i in range(row_count-1, -1, -1):
            for j in range(col_count-1, -1, -1):
                ans[i][j] = grid[i][j] + min(ans[i+1][j], ans[i][j+1])

        return ans[0][0]