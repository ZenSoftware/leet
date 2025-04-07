# https://leetcode.com/problems/implement-rand10-using-rand7/description/
from random import randint


def rand7():
    return randint(1, 7)


class Solution:
    def rand10(self):
        total = 0
        for _ in range(5):
            total += rand7()
        return (total % 10) + 1
