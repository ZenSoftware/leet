# https://leetcode.com/problems/shuffle-an-array/description/
from typing import List
from random import randint

class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def reset(self) -> List[int]:
        return self.nums

    def shuffle(self) -> List[int]:
        res = self.nums.copy()
        for i in range(len(res)):
            rand = randint(0, len(res)-1)
            res[i], res[rand] = res[rand], res[i]
        return res