# https://leetcode.com/problems/spiral-matrix-ii/description/
from typing import List

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        size = n*n
        matrix: List[List[int]] = []
        for i in range(n):
            matrix.append([None] * n)
        
        top, bottom = 0, n-1
        left, right = 0, n-1
        count = 1
        
        while count <= size:
            for col in range(left, right+1):
                matrix[top][col] = count
                count += 1
            if count > size:
                return matrix
            top += 1
            
            for row in range(top, bottom+1):
                matrix[row][right] = count
                count += 1
            if count > size:
                return matrix
            right -= 1

            for col in range(right, left-1, -1):
                matrix[bottom][col] = count
                count += 1
            if count > size:
                return matrix
            bottom -= 1

            for row in range(bottom, top-1, -1):
                matrix[row][left] = count
                count += 1
            left += 1
