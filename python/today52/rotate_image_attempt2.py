# https://leetcode.com/problems/rotate-image/description/
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        transposed = list(zip(*matrix))
        for r in range(len(matrix)):
            matrix[r] = list(transposed[r][::-1])
