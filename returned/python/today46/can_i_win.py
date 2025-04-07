# https://leetcode.com/problems/can-i-win/description/
from typing import Tuple
from functools import cache


class Solution:
    """
    Time: O(2^n)
    Space: O(2^n)
    """

    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if desiredTotal <= 0:
            return True
        elif maxChoosableInteger * (maxChoosableInteger + 1) / 2 < desiredTotal:
            return False

        choices = tuple(range(1, maxChoosableInteger + 1))
        return self.compute_win(choices, desiredTotal)

    @cache
    def compute_win(self, choices: Tuple[int], target: int) -> bool:
        if choices[-1] >= target:
            return True

        for i in range(len(choices)):
            next_choices = choices[:i] + choices[i + 1 :]
            next_target = target - choices[i]
            if not self.compute_win(next_choices, next_target):
                return True

        return False
