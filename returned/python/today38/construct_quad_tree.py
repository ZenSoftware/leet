# https://leetcode.com/problems/construct-quad-tree/description/
# Solution: https://leetcode.com/problems/construct-quad-tree/solutions/3234560/python-fully-optimized-recursion-o-n-2/
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
        def is_same(r, c, size):
            val = grid[r][c]
            for i in range(r, r+size):
                for j in range(c, c+size):
                    if grid[i][j] != val:
                        return False
            return True
        
        def dfs(r, c, size):
            if is_same(r, c, size):
                return Node(grid[r][c], True, None, None, None, None)
            
            half = size//2
            topLeft = dfs(r, c, half)
            topRight = dfs(r, c+half, half)
            bottomLeft = dfs(r+half, c, half)
            bottomRight = dfs(r+half, c+half, half)
            return Node(0, False, topLeft, topRight, bottomLeft, bottomRight)
        
        return dfs(0, 0, len(grid))