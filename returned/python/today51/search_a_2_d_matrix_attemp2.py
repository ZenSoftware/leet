# https://leetcode.com/problems/search-a-2d-matrix/description/
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def get_row():
            top, bottom = 0, len(matrix) - 1
            while top <= bottom:
                mid = (top + bottom) // 2
                if matrix[mid][0] <= target <= matrix[mid][-1]:
                    return mid
                if target < matrix[mid][-1]:
                    bottom = mid - 1
                else:
                    top = mid + 1
            return -1

        row = get_row()
        if row == -1:
            return False

        left, right = 0, len(matrix[0]) - 1
        while left <= right:
            mid = (left + right) // 2
            if matrix[row][mid] == target:
                return True
            if matrix[row][mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False
