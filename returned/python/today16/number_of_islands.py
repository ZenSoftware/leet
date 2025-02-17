# https://leetcode.com/problems/number-of-islands/description/
from typing import List
from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        count = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    count += 1
                    queue = deque([(i,j)])
                    while queue:
                        for _ in range(len(queue)):
                            x, y = queue.popleft()
                            if 0 <= x < rows and 0 <= y < cols and grid[x][y] == '1':
                                grid[x][y] = 'X'
                                queue.append((x+1, y))
                                queue.append((x-1, y))
                                queue.append((x, y+1))
                                queue.append((x, y-1))
        return count