# https://leetcode.com/problems/game-of-life/description/
from typing import List

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        ROWS = len(board)
        COLS = len(board[0])

        def is_alive(r: int, c: int) -> int:
            return r in range(ROWS) and c in range(COLS) and board[r][c] == 1
        
        def count_ones(r: int, c: int) -> int:
            ones = 0
            if is_alive(r-1,c): ones += 1
            if is_alive(r+1,c): ones += 1
            if is_alive(r,c-1): ones += 1
            if is_alive(r,c+1): ones += 1
            if is_alive(r-1,c-1): ones += 1
            if is_alive(r-1,c+1): ones += 1
            if is_alive(r+1,c-1): ones += 1
            if is_alive(r+1,c+1): ones += 1
            return ones
        
        temp = [[None for _ in range(COLS)] for _ in range(ROWS)]
        for r in range(ROWS):
            for c in range(COLS):
                temp[r][c] = board[r][c]
                ones = count_ones(r,c)

                # Any live cell with fewer than two live neighbors dies as if caused by under-population.
                if board[r][c] == 1 and ones < 2:
                    temp[r][c] = 0

                # Any live cell with two or three live neighbors lives on to the next generation.
                # if board[r][c] == 1 and 2 <= live_neighbors <= 3:
                #     temp[r][c] = 1

                # Any live cell with more than three live neighbors dies, as if by over-population.
                if board[r][c] == 1 and ones > 3:
                    temp[r][c] = 0

                # Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
                if board[r][c] == 0 and ones == 3:
                    temp[r][c] = 1
        
        for r in range(ROWS):
            for c in range(COLS):
                board[r][c] = temp[r][c]
