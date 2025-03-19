# https://leetcode.com/problems/construct-quad-tree/description/
from typing import List

class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        ROWS, COLS = len(grid), len(grid[0])
        
        i, j = 0, 0
        while i < ROWS:
            if grid[i][j] != 0:
                break
            j += 1
            if j == COLS:
                j = 0
                i += 1
        else:
            return Node(0, True, None, None, None, None)
        
        i, j = 0, 0
        while i < ROWS:
            if grid[i][j] != 1:
                break
            j += 1
            if j == COLS:
                j = 0
                i += 1
        else:
            return Node(1, True, None, None, None, None)

        topLeftGrid = []
        topRightGrid = []
        for i in range(ROWS//2):
            topLeftGrid.append(grid[i][:COLS//2])
            topRightGrid.append(grid[i][COLS//2:])

        bottomLeftGrid = []
        bottomRightGrid = []
        for i in range(ROWS//2, ROWS):
            bottomLeftGrid.append(grid[i][:COLS//2])
            bottomRightGrid.append(grid[i][COLS//2:])

        topLeft = self.construct(topLeftGrid)
        topRight = self.construct(topRightGrid)
        bottomLeft = self.construct(bottomLeftGrid)
        bottomRight = self.construct(bottomRightGrid)
        return Node(0, False, topLeft, topRight, bottomLeft, bottomRight)