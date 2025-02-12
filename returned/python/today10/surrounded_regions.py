# https://leetcode.com/problems/surrounded-regions/
from collections import deque
from typing import List, Tuple

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])

        for col in range(cols):
            self.mark_exclude(board, (0, col))
            self.mark_exclude(board, (rows-1, col))

        for row in range(1, rows-1):
            self.mark_exclude(board, (row, 0))
            self.mark_exclude(board, (row, cols-1))
        
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == 'O':
                    board[row][col] = 'X'
                elif board[row][col] == 'T':
                    board[row][col] = 'O'

    def mark_exclude(self, board: List[List[str]], coord: Tuple[int, int]):
        if board[coord[0]][coord[1]] == 'X':
            return
        
        rows = len(board)
        cols = len(board[0])
        visited = set([coord])
        queue = deque([coord])

        def queue_add(row, col):
            if (row in range(rows) and
                col in range(cols) and
                board[row][col] == 'O' and
                (row,col) not in visited):
                
                visited.add((row, col))
                queue.append((row, col))

        while queue:
            for _ in range(len(queue)):
                row, col = queue.popleft()
                board[row][col]= 'T'
                queue_add(row+1, col)
                queue_add(row-1, col)
                queue_add(row, col+1)
                queue_add(row, col-1)