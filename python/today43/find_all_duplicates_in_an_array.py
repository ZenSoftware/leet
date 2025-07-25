# https://leetcode.com/problems/find-all-duplicates-in-an-array/description/
from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            if nums[index] < 1:
                res.append(index + 1)
            nums[index] *= -1
        return res
