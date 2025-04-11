# https://leetcode.com/problems/first-missing-positive/description/
from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        out_of_bounds = n + 1
        for i in range(n):
            if nums[i] <= 0:
                nums[i] = out_of_bounds

        for i in range(n):
            pos_num = abs(nums[i])
            if 1 <= pos_num <= n and nums[pos_num - 1] > 0:
                nums[pos_num - 1] *= -1

        for i in range(n):
            if nums[i] > 0:
                return i + 1

        return n + 1
