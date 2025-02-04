# https://leetcode.com/problems/spiral-matrix/description/
from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left = 0
        right = len(matrix[0]) - 1
        top = 0
        bottom = len(matrix) - 1
        
        size = len(matrix) * len(matrix[0])
        result = []

        while len(result) < size:
            for col in range(left, right+1):
                result.append(matrix[top][col])
                if len(result) == size:
                    return result
            top += 1
            for row in range(top, bottom+1):
                result.append(matrix[row][right])
                if len(result) == size:
                    return result
            right -= 1
            for col in range(right, left-1, -1):
                result.append(matrix[bottom][col])
                if len(result) == size:
                    return result
            bottom -= 1
            for row in range(bottom, top-1, -1):
                result.append(matrix[row][left])
                if len(result) == size:
                    return result
            left += 1
        return result