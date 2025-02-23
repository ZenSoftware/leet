# https://leetcode.com/problems/search-a-2d-matrix-ii/
from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        r, c = ROWS-1, 0
        while r >= 0 and c < COLS:
            if matrix[r][c] == target:
                return True
            
            if target < matrix[r][c] :
                r -= 1
            else:
                c += 1
        return False