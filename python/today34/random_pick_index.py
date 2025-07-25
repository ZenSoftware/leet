# https://leetcode.com/problems/random-pick-index/description/
from typing import List
from collections import defaultdict
from random import randint

class Solution:

    def __init__(self, nums: List[int]):
        self.nums_dict = defaultdict(list)
        for i, n in enumerate(nums):
            self.nums_dict[n].append(i)

    def pick(self, target: int) -> int:
        indexes = self.nums_dict[target]
        rand_pick = randint(0, len(indexes)-1)
        return indexes[rand_pick]