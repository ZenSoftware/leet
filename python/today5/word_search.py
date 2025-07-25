# https://leetcode.com/problems/word-search/description/
from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row_count = len(board)
        col_count = len(board[0])
        visited = set()
        def dfs(x: int, y: int, k: 0) -> bool:
            if k == len(word):
                return True
            
            if x < 0 or x >= row_count or y < 0 or y >= col_count:
                return False
            
            if (x,y) in visited:
                return False

            if word[k] != board[x][y]:
                return False
            
            visited.add((x,y))
            up = dfs(x, y-1, k+1)
            down = dfs(x, y+1, k+1)
            left = dfs(x-1, y, k+1)
            right = dfs(x+1, y, k+1)
            visited.remove((x,y))

            return up or down or left or right

        for x in range(row_count):
            for y in range(col_count):
                if dfs(x,y,0):
                    return True
        return False
