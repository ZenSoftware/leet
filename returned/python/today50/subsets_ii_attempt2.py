# https://leetcode.com/problems/subsets-ii/description/
from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        def combs(i: int, subset: List[int]):
            if i == len(nums):
                result.append(subset.copy())
                return

            subset.append(nums[i])
            combs(i + 1, subset)
            subset.pop()

            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            combs(i + 1, subset)

        combs(0, [])
        return result
