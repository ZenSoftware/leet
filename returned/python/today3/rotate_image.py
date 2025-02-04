# https://leetcode.com/problems/rotate-image/description/
from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        top = 0
        bottom = len(matrix) - 1
        left = 0
        right = bottom

        while left < right and top < bottom:
            i = left
            while i < right:
                tmp_right = matrix[top+i][right]
                matrix[top+i][right] = matrix[top][left+i]

                tmp_bottom = matrix[bottom][right-i]
                matrix[bottom][right-i] = tmp_right

                tmp_left = matrix[bottom-i][left]
                matrix[bottom-i][left] = tmp_bottom

                matrix[top][left+i] = tmp_left

                i += 1
            left += 1
            right -= 1
            top += 1
            bottom -= 1