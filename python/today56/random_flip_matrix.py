# https://leetcode.com/problems/random-flip-matrix/description/
from random import randint


class Solution(object):
    def __init__(self, m, n):
        self.matrix = [[0 for _ in range(n)] for _ in range(m)]
        self.m = m
        self.n = n

    def flip(self):
        row = randint(0, self.m - 1)
        col = randint(0, self.n - 1)
        self.matrix[row][col] = 1
        return [row, col]

    def reset(self):
        for r in range(self.m):
            for c in range(self.n):
                self.matrix[r][c] = 0
