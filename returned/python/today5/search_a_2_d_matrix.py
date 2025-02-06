# https://leetcode.com/problems/search-a-2d-matrix/description/
from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_count, col_count = len(matrix), len(matrix[0])
        top, bottom = 0, row_count-1
        row_index = -1
        while top <= bottom:
            mid = (top + bottom) // 2
            if matrix[mid][0] <= target <= matrix[mid][col_count-1]:
                row_index = mid
                break
            elif target < matrix[mid][0]:
                bottom = mid - 1
            else:
                top = mid + 1
        
        if row_index == -1:
            return False
        
        left, right = 0, col_count-1
        while left <= right:
            mid = (left + right) // 2
            if target == matrix[row_index][mid]:
                return True
            elif target < matrix[row_index][mid]:
                right = mid - 1
            else:
                left = mid + 1
                
        return False
