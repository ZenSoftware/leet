# https://leetcode.com/problems/number-of-islands/description/
from typing import List
from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        count = 0

        def bfs(row, col):
            if (0 <= row < rows and
                0 <= col < cols and
                grid[row][col] == '1' and
                (row, col) not in visited):
                
                visited.append((row, col))
                queue.append((row, col))

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    count += 1
                    visited = [(i,j)]
                    queue = deque([(i,j)])

                    while queue:
                        for _ in range(len(queue)):
                            row, col = queue.popleft()
                            grid[row][col] = 'X'
                            bfs(row+1,col)
                            bfs(row-1,col)
                            bfs(row,col+1)
                            bfs(row,col-1)
        return count