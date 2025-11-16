# https://leetcode.com/problems/random-flip-matrix/description/
from random import randint


class Solution(object):
    def __init__(self, m, n):
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
        return self.rem.pop()

    def reset(self):
        self.rem = []
        for row in range(self.m):
            for col in range(self.n):
                self.rem.append([row, col])
