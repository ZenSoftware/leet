# https://leetcode.com/problems/unique-paths-ii/description/
from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        row_count = len(obstacleGrid)
        col_count = len(obstacleGrid[0])
        ans = [[0 for i in range(col_count+1)] for j in range(row_count+1)]
        ans[row_count][col_count-1] = 1

        for i in range(row_count-1, -1, -1):
            for j in range(col_count-1, -1, -1):
                if obstacleGrid[i][j] == 1:
                    ans[i][j] = 0
                else:
                    ans[i][j] = ans[i+1][j] + ans[i][j+1]
        return ans[0][0]