# https://leetcode.com/problems/random-flip-matrix/description/
from random import randint


class Solution(object):
    def __init__(self, m, n):
        self.matrix = [[0 for _ in range(n)] for _ in range(m)]
        self.m = m
        self.n = n

        self.rem = []
        for row in range(m):
            for col in range(n):
                self.rem.append([row, col])

    def flip(self):
        r = randint(0, len(self.rem) - 1)
        [self.rem[r], self.rem[len(self.rem) - 1]] = [
            self.rem[len(self.rem) - 1],
            self.rem[r],
        ]
        coord = self.rem.pop()
        self.matrix[coord[0]][coord[1]] = 1
        return coord

    def reset(self):
        self.rem = []
        for row in range(self.m):
            for col in range(self.n):
                self.rem.append([row, col])

        for r in range(self.m):
            for c in range(self.n):
                self.matrix[r][c] = 0
