# https://leetcode.com/problems/spiral-matrix/
from typing import List


class Solution:
    """
    Time: O(n*m)
    Space: O(1)
    """

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top, left = 0, 0
        bottom, right = len(matrix) - 1, len(matrix[0]) - 1
        num_elements = len(matrix) * len(matrix[0])
        result = []
        while len(result) < num_elements:
            for c in range(left, right + 1):
                result.append(matrix[top][c])
            top += 1

            if len(result) >= num_elements:
                return result

            for r in range(top, bottom + 1):
                result.append(matrix[r][right])
            right -= 1

            if len(result) >= num_elements:
                return result

            for c in range(right, left - 1, -1):
                result.append(matrix[bottom][c])
            bottom -= 1

            if len(result) >= num_elements:
                return result

            for r in range(bottom, top - 1, -1):
                result.append(matrix[r][left])
            left += 1
        return result
