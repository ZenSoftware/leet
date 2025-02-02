# https://leetcode.com/problems/valid-sudoku/
from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            check_row = set()
            check_col = set()
            for j in range(9):
                if board[i][j] in check_row:
                    return False
                if board[i][j] != '.':
                    check_row.add(board[i][j])
                
                if board[j][i] in check_col:
                    return False
                if board[j][i] != '.':
                    check_col.add(board[j][i])
        
        for gr in range(3):
            for gc in range(3):
                check_grid = set()
                for r in range(3):
                    for c in range(3):
                        cell = board[gr*3+r][gc*3+c]
                        if cell in check_grid:
                            return False
                        if cell != '.':
                            check_grid.add(cell)
        return True
