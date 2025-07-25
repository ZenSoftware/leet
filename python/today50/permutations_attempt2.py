# https://leetcode.com/problems/permutations/description/
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]

        all_perms = []
        for perm in self.permute(nums[1:]):
            for i in range(len(perm) + 1):
                all_perms.append(perm[:i] + [nums[0]] + perm[i:])
        return all_perms
