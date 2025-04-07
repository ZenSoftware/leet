# https://leetcode.com/problems/implement-rand10-using-rand7/description/
from random import randint


def rand7():
    return randint(1, 7)


class Solution:
    def rand10(self):
        num = 41
        while num > 40:
            num = (rand7() - 1) * 7 + rand7()
        return num % 10 + 1
