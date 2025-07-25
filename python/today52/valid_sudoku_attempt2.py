# https://leetcode.com/problems/valid-sudoku/description/
from typing import List


class Solution:
    """
    Time: O(1)
    Space: O(1)
    """

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()

        # validate rows
        for r in range(9):
            seen.clear()
            for c in range(9):
                cell = board[r][c]
                if cell != "." and cell in seen:
                    return False
                seen.add(cell)

        # validate columns
        for c in range(9):
            seen.clear()
            for r in range(9):
                cell = board[r][c]
                if cell != "." and cell in seen:
                    return False
                seen.add(cell)

        # validate subgrids
        for i in range(3):
            for j in range(3):
                seen.clear()
                for row in range(3):
                    for col in range(3):
                        r = i * 3 + row
                        c = j * 3 + col
                        cell = board[r][c]
                        if cell != "." and cell in seen:
                            return False
                        seen.add(cell)

        return True
