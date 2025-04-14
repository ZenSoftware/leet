# https://leetcode.com/problems/valid-sudoku/description/
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()

        for r in range(9):
            seen.clear()
            for c in range(9):
                if board[r][c] != "." and board[r][c] in seen:
                    return False
                seen.add(board[r][c])

        for c in range(9):
            seen.clear()
            for r in range(9):
                if board[r][c] != "." and board[r][c] in seen:
                    return False
                seen.add(board[r][c])

        for i in range(3):
            for j in range(3):
                seen.clear()
                for row in range(3):
                    for col in range(3):
                        r = i * 3 + row
                        c = j * 3 + col
                        if board[r][c] != "." and board[r][c] in seen:
                            return False
                        seen.add(board[r][c])

        return True
