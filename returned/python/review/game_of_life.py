# https://leetcode.com/problems/game-of-life/description/
from typing import List

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        m = len(board)
        n = len(board[0])

        for r in range(m):
            for c in range(n):
                ones = 0
                for x in range(max(0, r-1), min(m, r+2)):
                    for y in range(max(0, c-1), min(n, c+2)):
                        ones += board[x][y] & 1
        
                # Any live cell with two or three live neighbors lives on to the next generation.
                if board[r][c] == 1 and (ones == 3 or ones == 4):
                    board[r][c] += 0b10
        
                # Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
                if board[r][c] == 0 and ones == 3:
                    board[r][c] += 0b10
        
        for r in range(m):
            for c in range(n):
                board[r][c] >>= 1