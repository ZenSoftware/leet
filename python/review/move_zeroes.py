# https://leetcode.com/problems/move-zeroes/description/
from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        result = []
        for i in range(len(nums)):
            if nums[i] != 0:
                result.append(nums[i])
                
        for i in range(len(result)):
            nums[i] = result[i]

        i += 1
        while i < len(nums):
            nums[i] = 0
            i += 1