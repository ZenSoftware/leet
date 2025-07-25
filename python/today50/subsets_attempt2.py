# https://leetcode.com/problems/subsets/description/
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]

        combs_without_first = self.subsets(nums[1:])
        combs_with_first = []

        for comb in combs_without_first:
            combs_with_first.append([nums[0]] + comb)
        combs_with_first.extend(combs_without_first)
        return combs_with_first
