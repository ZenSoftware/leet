# https://leetcode.com/problems/find-peak-element/
from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + (r - l) // 2

            if m > 0 and nums[m-1] > nums[m]:
                r = m - 1
            elif m < len(nums) - 1 and nums[m] < nums[m+1]:
                l = m + 1
            else:
                return m
