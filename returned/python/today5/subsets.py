# https://leetcode.com/problems/subsets/description/
from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        
        firstEl = nums[0]
        withoutFirst = nums[1:]
        permsWithoutFirst = self.subsets(withoutFirst)
        permsWithFirst = []

        for perm in permsWithoutFirst:
            permsWithFirst.append([firstEl] + perm)

        permsWithoutFirst.extend(permsWithFirst)
        return permsWithoutFirst