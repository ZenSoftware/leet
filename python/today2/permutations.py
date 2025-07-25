# https://leetcode.com/problems/permutations/
from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]

        firstEl = nums[0]
        withoutFirst = nums[1:]
        permsWithoutFirst = self.permute(withoutFirst)
        allPermutations = []

        for perm in permsWithoutFirst:
            i = 0
            while i <= len(perm):
                permWithFirst = perm[0:i] + [firstEl] + perm[i:]
                allPermutations.append(permWithFirst)
                i += 1
        
        return allPermutations
