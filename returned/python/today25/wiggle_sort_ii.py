# https://leetcode.com/problems/wiggle-sort-ii/description/
from typing import List

class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        temp = nums.copy()
        temp.sort()
        for i in range(1, len(nums), 2):
            nums[i] = temp.pop()
        for i in range(0, len(nums), 2):
            nums[i] = temp.pop()