# https://leetcode.com/problems/surrounded-regions/
from collections import deque
from typing import List, Tuple

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        row_count = len(board)
        col_count = len(board[0])

        for col in range(col_count):
            self.mark_exclude(board, (0, col))
            self.mark_exclude(board, (row_count-1, col))

        for row in range(1, row_count-1):
            self.mark_exclude(board, (row, 0))
            self.mark_exclude(board, (row, col_count-1))
        
        for row in range(row_count):
            for col in range(col_count):
                if board[row][col] == 'O':
                    board[row][col] = 'X'
                elif board[row][col] == 'T':
                    board[row][col] = 'O'

    def mark_exclude(self, board: List[List[str]], coord: Tuple[int, int]):
        if board[coord[0]][coord[1]] == 'X':
            return
        
        row_count = len(board)
        col_count = len(board[0])
        visited = set([coord])
        queue = deque([coord])

        def queue_add(row, col):
            if ((0 <= row < row_count) and
                (0 <= col < col_count) and
                board[row][col] == 'O' and
                (row,col) not in visited):
                visited.add((row,col))
                queue.append((row,col))

        while queue:
            for _ in range(len(queue)):
                row, col = queue.popleft()
                board[row][col]= 'T'
                queue_add(row+1, col)
                queue_add(row-1, col)
                queue_add(row, col+1)
                queue_add(row, col-1)