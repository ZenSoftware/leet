from collections import deque
from typing import List, Tuple

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        row_count = len(board)
        col_count = len(board[0])

        for col in range(col_count):
            self.bfs((0, col), board)
            self.bfs((row_count-1, col), board)

        for row in range(1, row_count-1):
            self.bfs((row, 0), board)
            self.bfs((row, col_count-1), board)
        
        for row in range(row_count):
            for col in range(col_count):
                if board[row][col] == 'O':
                    board[row][col] = 'X'
                elif board[row][col] == 'T':
                    board[row][col] = 'O'

    def bfs(self, coord: Tuple[int, int], board: List[List[str]]):
        if board[coord[0]][coord[1]] == 'X':
            return
        
        row_count = len(board)
        col_count = len(board[0])
        visited = set()
        visited.add(coord)
        queue = deque()
        queue.append(coord)

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