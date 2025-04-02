# https://leetcode.com/problems/132-pattern/description/
from typing import List


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                if nums[i] >= nums[j]:
                    continue
                for k in range(j + 1, n):
                    if nums[i] < nums[k] < nums[j]:
                        return True
        return False
